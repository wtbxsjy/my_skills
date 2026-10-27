---
name: read-file
description: >
  Read any data file (CSV, JSON, Parquet, Avro, Excel, spatial, SQLite) or remote URL (S3, HTTPS).
  Use when user references a data file, asks "what's in this file", or wants to preview/profile a dataset.
  Not for source code.
argument-hint: <filename or URL> [question about the data]
allowed-tools: Bash
---

You are helping the user read and analyze a data file using DuckDB.

Filename given: `$0`
Question: `${1:-describe the data}`

## Step 1 — Read it

`RESOLVED_PATH` is `$0`. If the user gave a bare filename (no `/`), resolve it to a full path with `find` first.

Run a single DuckDB command that defines the `read_any` macro inline and reads the file.

For **remote files**, prepend the necessary LOAD/SECRET before the macro:

| Protocol | Prepend |
|---|---|
| `https://` / `http://` | `LOAD httpfs;` |
| `s3://` | `LOAD httpfs; CREATE SECRET (TYPE S3, PROVIDER credential_chain);` |
| `gs://` / `gcs://` | `LOAD httpfs; CREATE SECRET (TYPE GCS, PROVIDER credential_chain);` |
| `az://` / `azure://` / `abfss://` | `LOAD httpfs; LOAD azure; CREATE SECRET (TYPE AZURE, PROVIDER credential_chain);` |

For **local files**, no prefix needed.

```bash
duckdb -csv -c "
CREATE OR REPLACE MACRO read_any(file_name) AS TABLE
  WITH json_case AS (FROM read_json_auto(file_name))
     , csv_case AS (FROM read_csv(file_name))
     , parquet_case AS (FROM read_parquet(file_name))
     , avro_case AS (FROM read_avro(file_name))
     , blob_case AS (FROM read_blob(file_name))
     , spatial_case AS (FROM st_read(file_name))
     , excel_case AS (FROM read_xlsx(file_name))
     , sqlite_case AS (FROM sqlite_scan(file_name, (SELECT name FROM sqlite_master(file_name) LIMIT 1)))
     , ipynb_case AS (
         WITH nb AS (FROM read_json_auto(file_name))
         SELECT cell_idx, cell.cell_type,
                array_to_string(cell.source, '') AS source,
                cell.execution_count
         FROM nb, UNNEST(cells) WITH ORDINALITY AS t(cell, cell_idx)
         ORDER BY cell_idx
     )
  FROM query_table(
    CASE
      WHEN file_name ILIKE '%.json' OR file_name ILIKE '%.jsonl' OR file_name ILIKE '%.ndjson' OR file_name ILIKE '%.geojson' OR file_name ILIKE '%.geojsonl' OR file_name ILIKE '%.har' THEN 'json_case'
      WHEN file_name ILIKE '%.csv' OR file_name ILIKE '%.tsv' OR file_name ILIKE '%.tab' OR file_name ILIKE '%.txt' THEN 'csv_case'
      WHEN file_name ILIKE '%.parquet' OR file_name ILIKE '%.pq' THEN 'parquet_case'
      WHEN file_name ILIKE '%.avro' THEN 'avro_case'
      WHEN file_name ILIKE '%.xlsx' OR file_name ILIKE '%.xls' THEN 'excel_case'
      WHEN file_name ILIKE '%.shp' OR file_name ILIKE '%.gpkg' OR file_name ILIKE '%.fgb' OR file_name ILIKE '%.kml' THEN 'spatial_case'
      WHEN file_name ILIKE '%.ipynb' THEN 'ipynb_case'
      WHEN file_name ILIKE '%.db' OR file_name ILIKE '%.sqlite' OR file_name ILIKE '%.sqlite3' THEN 'sqlite_case'
      ELSE 'blob_case'
    END
  );

DESCRIBE FROM read_any('RESOLVED_PATH');
SELECT count(*) AS row_count FROM read_any('RESOLVED_PATH');
FROM read_any('RESOLVED_PATH') LIMIT 20;
"
```

**If this fails:**
- **`duckdb: command not found`** → invoke `/duckdb-skills:install-duckdb` and retry.
- **Missing extension** (e.g. spatial files, xlsx, sqlite) → retry with `INSTALL spatial; LOAD spatial;` or `INSTALL sqlite_scanner; LOAD sqlite_scanner;` prepended before the macro.
- **Wrong reader / parse error** → use the correct `read_*` function directly instead of `read_any`.

## DuckDB 2.0 notes

Check `duckdb --version`. The `read_any` macro and the readers above work unchanged on 2.0 (verified
for CSV, JSON and Parquet on 2.0.0). What changes:

- **Output / agent mode (2.x only).** The command above passes `-csv`, which switches the CLI's
  automatic *agent mode* off. On 2.x, drop `-csv` (or prefix `DUCKDB_AGENT_MODE=1`, which older CLIs
  ignore) to get compact Markdown tables with column types, a row-count + hash footer, and JSON
  errors. Read the footer: `first 20 and last 20 of N rows` means the middle was cut. Keep `-csv`
  on 1.x. Details: `/duckdb-skills:duckdb-2-0` (`references/agent-mode.md`).
- **Cheap profiling of big files.** `DESCRIBE FROM read_any(...)` is already cheap; for a quick
  profile use `SUMMARIZE FROM read_any(...)`. `DESCRIBE <query>` shows result columns without running it.
- **Remote files are faster.** 2.0 reads Parquet, CSV and DuckDB files asynchronously (many requests in
  flight), which mostly helps `s3://`, `gs://` and `https://` sources. Related settings:
  `async_threads`, `http_client_pool_capacity`.
- **S3 credentials must come from secrets.** Passing S3 settings as URL parameters
  (`s3://bucket/f.csv?s3_access_key_id=...`) is disabled in 2.0; the `?...` becomes part of the object
  key. Use the `CREATE SECRET` lines in the table above.
- **JSON with different shapes per row.** `read_json_auto` unions all keys into many sparse columns.
  On 2.x, `SELECT json::VARIANT AS payload FROM read_json_objects('FILE')` keeps each row as is, and
  `variant_type`, `variant_keys(payload)`, `variant_extract_string(payload, 'key')` inspect it
  (verified on 2.0.0).
- **Database files from 2.0** (`.db`/`.duckdb`) cannot be opened by an older CLI (error mentions
  "version number 69"); upgrade with `/duckdb-skills:install-duckdb --update`.

## Step 2 — Answer

Using the schema, row count, and sample rows, answer:

`${1:-describe the data: summarize column types, row count, and any notable patterns.}`

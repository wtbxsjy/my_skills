---
name: s3-explore
description: >
  Explore and query data on S3, Cloudflare R2, GCS, MinIO, or any S3-compatible storage.
  Use when the user mentions an s3://, r2://, gs://, or gcs:// URL, asks "what's in this bucket",
  wants to list remote files, preview remote Parquet/CSV/JSON, or query data on object storage
  without downloading it. Also triggers when the user wants to know the size, schema, or row count
  of remote datasets.
argument-hint: <s3-url> [question about the data]
allowed-tools: Bash
---

You are helping the user explore data on remote object storage using DuckDB.

URL: `$0`
Question: `${1:-list and describe what's there}`

## Step 1 — Detect provider and set up credentials

Based on the URL or user context, prepend the appropriate secret configuration:

| Provider | URL patterns | Secret setup |
|---|---|---|
| **AWS S3** | `s3://` | `CREATE SECRET (TYPE S3, PROVIDER credential_chain);` |
| **Cloudflare R2** | `r2://`, `s3://` with R2 endpoint | `CREATE SECRET (TYPE R2, PROVIDER credential_chain);` |
| **GCS** | `gs://`, `gcs://` | `CREATE SECRET (TYPE GCS, PROVIDER credential_chain);` |
| **MinIO / custom** | `s3://` with custom endpoint | `CREATE SECRET (TYPE S3, KEY_ID '...', SECRET '...', ENDPOINT '...', USE_SSL true);` |

For R2, if the user provides an account ID, the endpoint is `<account_id>.r2.cloudflarestorage.com`. R2 URLs like `r2://bucket/path` should be rewritten to `s3://bucket/path` with the R2 secret.

For public buckets (e.g., Overture Maps, AWS open data), no secret is needed — skip this step.

Always prepend:
```sql
LOAD httpfs;
```

## Step 2 — Determine what the URL points to

If the URL looks like a **directory or bucket** (no file extension, or ends with `/`), list its contents with sizes:

```bash
duckdb -c "
LOAD httpfs;
<SECRET_SETUP>
SELECT filename, (size / 1024 / 1024)::DECIMAL(10,1) AS size_mb, last_modified
FROM read_blob('<URL>/*')
ORDER BY filename
LIMIT 50;
"
```

Note: only select `filename`, `size`, `last_modified` — never select `content`, which would download the actual files.

If the URL points to a **specific file or glob pattern** (has a file extension or contains `*`), preview it:

```bash
duckdb -c "
LOAD httpfs;
<SECRET_SETUP>
DESCRIBE FROM '<URL>';
SELECT count(*) AS row_count FROM '<URL>';
FROM '<URL>' LIMIT 20;
"
```

For **Parquet files**, get row counts and sizes from metadata (no data download):

```bash
duckdb -c "
LOAD httpfs;
<SECRET_SETUP>
SELECT file_name,
       sum(row_group_num_rows) AS total_rows,
       (sum(row_group_compressed_bytes) / 1024 / 1024)::DECIMAL(10,1) AS compressed_mb
FROM parquet_metadata('<URL>')
GROUP BY file_name;
"
```

## Step 3 — Answer the question

Using the listing, schema, or sample data, answer:

`${1:-list and describe what's there}`

If the user asks an analytical question (e.g., "how many rows match X"), write and run the appropriate SQL query. DuckDB pushes predicates down into Parquet on S3, so filtering is efficient even on large remote datasets.

## DuckDB 2.0 notes

- **Faster remote reads.** 2.0 reads Parquet, CSV and DuckDB files asynchronously (reads issued in the
  background, many requests in flight), so queries on `s3://`/`https://` data are noticeably faster than
  on 1.x without any change. Tuning, if needed: `SET async_threads = <n>;`,
  `SET http_client_pool_capacity = <n>;` (setting names exist in 2.0.0).
- **Credentials only via secrets.** S3 settings in URL parameters (`s3://bucket/key?s3_access_key_id=...`)
  are disabled by default in 2.0 — everything after `?` becomes part of the key, which shows up as
  "not found". Use the `CREATE SECRET` forms above; the legacy opt-in is
  `SET s3_enable_deprecated_url_parameters = true;` (after `LOAD httpfs`).
- **Catalogs that are just views.** A small `.duckdb` file holding only `CREATE VIEW ... AS SELECT * FROM 's3://.../*.parquet'`
  can be shared by URL and attached with `ATTACH 'https://example.com/catalog.duckdb' AS cat (READ_ONLY);`
  — a convenient way to give people a stable set of names over a data lake (the file must have been written
  by a DuckDB version the reader can open; 2.0-created files need a 2.x CLI).
- **Output.** With a 2.x CLI in agent mode the result of `read_blob('<URL>/*')` listings is capped
  (1,000 rows / 10,000 bytes, first and last 20 rows otherwise) and ends with a footer; keep the `LIMIT 50`.
  Read `/duckdb-skills:duckdb-2-0` for how to interpret the footer.

## Error handling

- **`duckdb: command not found`** → delegate to `/duckdb-skills:install-duckdb`
- **Access denied / 403** → suggest the user check credentials: `aws configure`, environment variables, or provide explicit key/secret
- **Bucket not found / 404** → check the URL and region
- **Timeout on large listing** → suggest narrowing the glob pattern or adding a prefix

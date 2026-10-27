# DuckDB 2.0 — what's new (summary)

DuckDB **2.0.0 LTS "Cinnamon Teal"** (GitHub release name "Cyanoptera") was released on
**2026-10-21**. It is the largest feature release so far (close to 20,000 commits since 1.5).

Sources: the official announcement (duckdb.org/2026/10/21/announcing-duckdb-200), the
"What's New in the Docs for 2.0" page, the migration guide, and the "Agent Mode in the DuckDB CLI"
post. Items marked **[verified]** were executed against the `duckdb==2.0.0` Python package while
writing this skill. Agent mode is a CLI feature and could not be run in that environment, so it is
described from the official documentation only.

## Support and versions

| Line | Status |
|---|---|
| 2.0 | LTS, supported until at least October 2027 |
| 1.5 | support extended to March 2027 (effectively LTS) |
| 1.4 | LTS, end of life 2026-11-17 |

- The first 2.0 patch release is planned for November 2026. For mission-critical workloads, test on a
  shadow system first and consider waiting for it.
- Python client requires Python 3.11 or newer; CLI and Python were released first, other clients
  (R, Rust, ...) and some extensions can lag by a few days.
- A C++17 compiler is now required to build DuckDB. Release builds use Clang.

## 1. Agent mode in the CLI (headline feature for coding agents)

The CLI detects when it is driven by a coding agent and changes its output defaults: compact
Markdown tables, explicit truncation markers, a result hash, JSON errors, cost estimates and plain
progress lines. In the DuckDB team's TPC-H test (22 questions, scale factor 100, 132 runs, all
correct) the output the model had to read dropped from 123.6k to 50.8k tokens (-59%). The saving is
small relative to total cost because the agent's system prompt dominates.

Details, flags and how to read the output: see `agent-mode.md`.

## 2. DuckDB as a server: Quack and `CONNECT`

- The Quack protocol (introduced in 1.5.3) is polished: an HTTP-based client/server protocol with
  `application/duckdb` serialization, one round trip per query, default port **9494**, URIs like
  `quack:localhost` or `quack:host:port`.
- Server: `CALL quack_serve('quack:localhost', token = 'my_token');` (stop with `quack_stop`).
  By default it only binds to localhost; for remote access put it behind a TLS-terminating reverse
  proxy. `allow_other_hostname = true` is meant for testing.
- Client, recommended path:
  ```sql
  ATTACH 'quack:server.example.com' AS qk (TOKEN 'my_token');
  CONNECT qk;            -- route the whole session to the remote
  SELECT count(*) FROM events;   -- runs on the server
  DISCONNECT;            -- back to the local database
  ```
  Other ways: `ATTACH 'quack:host' AS name` and qualify table names, or the stateless
  `FROM quack_query('quack:host', 'SELECT 42', token = '...')`.
- `CONNECT` also accepts a connection string for PostgreSQL (`CONNECT 'postgres:dbname=mydb host=localhost'`)
  and MySQL; a new remote pushdown optimizer ships SQL to the server instead of pulling tables.
  Plain in-process databases (memory or a file) do not support `CONNECT`.
- CLI shortcuts: `duckdb -serve` (serves an in-memory DB on `localhost:9494`),
  `duckdb analytics.duckdb -serve`, `duckdb -connect`, and `TYPE:SECRET` forms such as
  `duckdb -connect quack:analytics`. `.serve_command` / `.connect_command` customize what they run.
  `-connect` cannot be combined with a local database path.

## 3. Performance

- **Asynchronous I/O** for Parquet, CSV and DuckDB's native format: reads are issued in the
  background with many requests in flight, scaling independently of query processing. Big wins on
  object storage (`s3://`, ...). Settings: `async_threads`, `http_client_pool_capacity` **[verified: both exist]**.
- Faster recursive CTEs, better row-group pruning with min-max indexes (zonemaps), remote pushdown
  for PostgreSQL/MySQL, and other optimizer/engine improvements (including on Windows).

## 4. `VARIANT` is first class

`VARIANT` stores semi-structured, schema-less data (think "JSON, but not text") while keeping
columnar speed. DuckDB 2.0 detects the common structure and "shreds" it into column-like storage,
end to end from storage to Parquet reading/writing.

Functions **[verified]**: `variant_type`, `variant_typeof`, `variant_keys`, `variant_extract`,
`variant_extract_string`, `variant_array_length`, `variant_exists`, `variant_contains`,
`variant_comparator`, `variant_normalize`, aggregates `variant_group_object(key, value)` and
`variant_group_array(x)`.

```sql
CREATE TABLE events (payload VARIANT);
INSERT INTO events VALUES ('{"user": {"id": 42}}'::JSON::VARIANT);
SELECT variant_type(payload), variant_keys(payload) FROM events;
```

## 5. Triggers

`CREATE TRIGGER` / `DROP TRIGGER` with `BEFORE`/`AFTER`, `FOR EACH ROW`/`FOR EACH STATEMENT`,
transition tables (`REFERENCING OLD TABLE AS o NEW TABLE AS n`), several triggers per event and
`RETURNING` on triggered tables **[verified: statement-level AFTER UPDATE audit trigger]**.
Typical uses: audit tables and incrementally maintained summary tables (a step toward materialized views).

Limitations in 2.0: no `BEFORE ... FOR EACH ROW`, no `UPDATE ... FOR EACH ROW`, no `INSTEAD OF` or
triggers on views, no temporary triggers, no `MERGE INTO` on tables with triggers, and
`INSERT OR REPLACE` / `OR IGNORE` / `ON CONFLICT` fail on tables with `UPDATE`/`DELETE` triggers.
`FOR EACH ROW` and `FOR EACH STATEMENT` cannot be mixed for the same event on one table.

## 6. New SQL syntax and functions

All **[verified]** unless noted.

| Feature | Example |
|---|---|
| `$variable` shorthand for `getvariable()` | `SET VARIABLE x = 30; SELECT 20 + $x;` |
| SQL-standard `FETCH FIRST` | `... ORDER BY c FETCH FIRST 5 ROWS ONLY` / `OFFSET 5 ROWS FETCH NEXT 10 ROWS ONLY` |
| Data-modifying CTEs (`INSERT`/`UPDATE`/`DELETE`/`COPY`) | `WITH moved AS MATERIALIZED (DELETE FROM staging RETURNING *) INSERT INTO archive SELECT * FROM moved;` |
| `NEAREST` joins (top-k similarity as a join) | `... INNER JOIN products t NEAREST 1 BY DISTANCE array_distance(q.embedding, t.embedding)`; `APPROX NEAREST k BY SIMILARITY ...` |
| Nested schemas | `CREATE SCHEMA finance.reports;` |
| JSON mutation functions | `json_set`, `json_insert`, `json_replace`, `json_remove` |
| `UNNEST` in `GROUP BY`; `EXCEPT` as synonym of `EXCLUDE` in `*` | `SELECT * EXCEPT (b) FROM t` |
| Backtick-quoted identifiers | ``SELECT 1 AS `my col` `` |
| `EXPLAIN (SQL)` renders the optimized plan as SQL | `EXPLAIN (SQL) SELECT ...` |
| `EXPLAIN (FORMAT compact)` one operator per line | default `EXPLAIN` format in agent mode |
| Well-defined `MERGE INTO` / `UPDATE ... FROM` for multiple matching source rows | now raises an error (see migration) |
| Misc | `SECURE VIEW`, `SHOW` statement, setting a sequence value, empty `STRUCT` types, `TIMESTAMPTZ_NS`, `lttb` aggregate, `decimal_division()`, `decimal_average()`, no-argument `GROUPING_ID()` (documented, not individually run) |

New or changed settings **[verified in the 2.0.0 build]**: `max_execution_time` (ms, bounds query
wall-clock time), `max_memory` (also accepts a percentage, e.g. `'50%'`), `checkpoint_on_detach`,
`tracked_metrics`, `storage_compatibility_version`, `allow_extension_repositories`,
`error_on_division_by_zero`, `legacy_disable_null_type`, `regex_match_operator_semantics`,
`table_function_identifier_conversion`, `async_threads`, `http_client_pool_capacity`.
`SET lambda_syntax = 'enable_single_arrow'` is accepted although `lambda_syntax` is not listed in
`duckdb_settings()`; `enable_legacy_parser` only exists once the `legacy_parser` extension is loaded.

## 7. Parser

The new **PEG-based parser** (opt-in in 1.5) is the default. It is designed to be compatible, gives
precise error locations, and lets extensions add grammar. Escape hatch:
`INSTALL AND LOAD legacy_parser; SET enable_legacy_parser = true;`.

## 8. Storage format v2.0 (storage version 69)

New database files use the 2.0 format: lazy metadata loading, better compression, corruption
validation. **Older DuckDB versions cannot open them**, while 2.0 can still read and write older files
(they keep their old storage version). See `migration.md`.

## 9. Extensions and ecosystem

- **Self-hosted extension repositories**: `SET allow_extension_repositories = 'allowed'; CREATE EXTENSION REPOSITORY my_repo WITH PREFIX 'https://...'; INSTALL AND LOAD my_ext FROM my_repo;` (work in progress; syntax may change).
- **C API v2** (not yet stable) lets extensions use file systems and table functions; statically linked extensions are documented.
- **ICU removed** from the core build; the `icu` extension implements time zones, calendars and
  collations natively (tz data from IANA, ~45 kB). No query changes needed.
- **DuckLake 1.1** (spec + reference extension). **Iceberg**: REST catalog `ATTACH` options (namespace-derived location, `metadata-location`).
  **Delta**: `CREATE TABLE`, time travel, better `VARIANT`.
- `duckdb_functions()` has a new `extension_name` column **[verified]**; `duckdb_secret_type_parameters()` lists secret parameters **[verified]**.

## 10. Data import / export

- Parquet: `schema` parameter for reading, new writing options (`TIMESTAMP_IS_ADJUSTED_TO_UTC`,
  `WRITE_TIMESTAMP_AS_INT96`), `file_row_group_number` virtual column.
- `COPY`: `PARTITION_PATH` (custom partition sub-directories) and `ORDER_BY` (sort rows within partitions).
- GeoJSON writing and loading are documented on the JSON import/export pages; CSV gained
  `rejects_line_size_limit` (bounds the stored rejected lines).

## 11. CLI additions (besides agent mode)

- `.manual ⟨function⟩` and `duckdb -manual ⟨function⟩` show signatures, description and examples
  of a function (backed by `duckdb_functions()`).
- `.history` and the `shell_history()` table function; `.schema` pretty-prints and highlights
  (`--no-indent` restores one line); `.web` opens the query graph in a browser;
  `.tables ⟨LIKE pattern⟩` lists tables with columns, types and row counts.
- `-storage-version VER` (use `latest` for the newest), `-safe` / `.safe_mode` (no external file
  access, `enable_external_access=false`; cannot be undone in the session), `-no-init`.
- CLI log storage is `shell_log_storage` (warnings only); to query logs use
  `CALL enable_logging(storage = 'memory')`.

## 12. Deprecations and removals

- Single-arrow lambda `x -> x + 1` is **disabled by default**; removed in 2.1.
- Amalgamation builds deprecated; macOS x86_64 (`osx_amd64`) phased out (community extensions no
  longer built; unsupported in 2.1).
- Removed settings: `custom_profiling_settings` (use `tracked_metrics`), `enable_http_logging` and
  `http_logging_output` (use `CALL enable_logging('HTTP')`); `profiling_mode` is deprecated.

## Related reading

- "A Preview of DuckDB v2.0" (2026-08-17), "Asynchronous I/O in DuckDB" (2026-07-31),
  "Agent Mode in the DuckDB CLI" (2026-10-09), "A DuckDB Database with No Data in It" (2026-10-07,
  a database file that only holds views over remote Parquet, attached with `(READ_ONLY)`).

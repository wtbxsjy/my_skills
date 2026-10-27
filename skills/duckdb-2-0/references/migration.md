# Migrating to DuckDB 2.0

Source: the official migration guide (`docs/2.0/operations_manual/migration`). Behaviors marked
**[verified]** were reproduced on the `duckdb==2.0.0` Python package; the error text is copied
from that run.

## Before you migrate

- Run 2.0 on a **shadow system** that tracks the real workload before switching production.
- Mission-critical workloads may wait for the first patch release (planned for November 2026).
  DuckDB 1.5 is supported until March 2027; 1.4 LTS ends on 2026-11-17.
- Complex deployments with many DuckDB processes need the most care because of the storage format.

## 1. Storage format (the most likely source of problems)

- New database files written by 2.0 use **storage version 69** and **cannot be read by DuckDB < 2.0**.
- 2.0 can read and write older files; they keep their old storage version, so older versions can
  still read them afterwards.
- Error seen by an old version opening a new file:
  `IO Error: Trying to read a database file with version number 69, but we can only read versions between 64 and 68. The database file was created with a newer version of DuckDB.`

Writing files an older version can read:

```bash
duckdb my.db -storage-version v1.5.6 -c "CREATE TABLE t (x INT);"
```

Equivalent: `SET storage_compatibility_version = 'v1.5.0';` **[verified]** or the `STORAGE_VERSION`
option of `ATTACH` **[verified]**: `ATTACH 'x.duckdb' AS x (STORAGE_VERSION 'v1.5.0');`.
`-storage-version latest` selects the newest format. The default value of
`storage_compatibility_version` in 2.0 is `latest`.

Converting an existing database to the 2.0 format: export with the old version, import with 2.0
(or use `COPY FROM DATABASE`):

```bash
/older/duckdb mydata.old.db -c "EXPORT DATABASE 'tmp'"
/newer/duckdb mydata.new.db -c "IMPORT DATABASE 'tmp'"
```

## 2. Quick triage: symptom → cause → fix

| Symptom (2.0.0) | Cause | Fix |
|---|---|---|
| `Binder Error: Deprecated lambda arrow (->) detected. Please transition to the new lambda syntax ...` **[verified]** | single-arrow lambdas are disabled by default | write `list_transform(l, lambda x: x + 1)`; temporary bridge: `SET lambda_syntax = 'enable_single_arrow';` (removed in 2.1) |
| `Invalid Input Error: Division by zero in expression (1 // 0). Use TRY(...) ...` **[verified]** | integer `//` and `%` by zero now error instead of `NULL` (`1 / 0` still gives `inf`) | `TRY(1 // 0)` for one expression, or `SET error_on_division_by_zero = false;` |
| `'abc' ~ 'b'` now `true` **[verified]** | `~` / `!~` do partial regex matching, like PostgreSQL | use `regexp_full_match(s, p)` for full matching, or `SET regex_match_operator_semantics = 'full';` (deprecated) |
| `2 * 3!` is `12`, not `720` **[verified]** | the factorial operator `!` binds tighter | parenthesize: `(2 * 3)!` |
| `X'41'` is a `BLOB`, `B'101'` is a `BITSTRING` **[verified]** | literals no longer produce `VARCHAR` | cast if a string is wanted |
| `CREATE TABLE t AS SELECT NULL AS x` makes a column of type `"NULL"` **[verified]**; later inserts fail | untyped `NULL` keeps the `NULL` type instead of `INTEGER` | `NULL::VARCHAR AS x`, or `SET legacy_disable_null_type = true;` |
| `MERGE INTO command cannot affect the same target row more than once ...` **[verified]** | a target row matched several source rows | deduplicate the source or make the `ON` condition unique |
| S3 path with `?s3_access_key_id=...` stops working | S3 settings in URL parameters are disabled; `?...` is part of the object key | use `CREATE SECRET`; legacy: `SET s3_enable_deprecated_url_parameters = true;` (after `LOAD httpfs`) |
| `Setting enable_http_logging / http_logging_output` unknown | removed | `CALL enable_logging('HTTP');` |
| `custom_profiling_settings` unknown | removed | use `tracked_metrics` |
| Querying `duckdb_logs` in the CLI returns nothing | CLI log storage is `shell_log_storage` (console only) | `CALL enable_logging(storage = 'memory');` |
| Python import fails / API errors | Python 3.11+ required; several API changes | see the Python migration page in the docs |
| A query that parsed on 1.x fails to parse | new PEG parser | report it upstream; workaround: `INSTALL AND LOAD legacy_parser; SET enable_legacy_parser = true;` |
| `preserve_identifier_case` rejects/changes values | now a `VARCHAR`: `'preserve_case'` (default), `'lowercase'`, `'uppercase'` (old `true`/`false` still accepted) | use the new values |

Other changes that need no query edits: ICU is no longer bundled (the `icu` extension reimplements
time zones, calendars and collations), the C API v2 is new and not yet stable, and C++17 is required
to build.

## 3. Upgrade checklist for an agent

1. `duckdb --version` (and `PRAGMA version;`) — know which line you are on.
2. Find databases shared with other tools or processes. If any of them runs < 2.0, either write
   with `-storage-version <old>` or upgrade all of them together.
3. `grep` SQL files for ` -> ` lambdas, `//` and `%` on possibly-zero divisors, `~` operators,
   `MERGE INTO`, untyped `NULL` in `CREATE TABLE AS`, S3 URLs with `?` parameters.
4. Run the workload on 2.0 against a copy; compare results (agent mode footers contain an
   order-independent result hash that makes comparisons cheap).
5. Update extensions: `UPDATE EXTENSIONS;` (see the `install-duckdb` skill).
6. Keep a rollback path: the old binary plus a pre-upgrade copy of every database file.

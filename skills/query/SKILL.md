---
name: query
description: >
  Run SQL queries against the attached DuckDB database or ad-hoc against files.
  Accepts raw SQL or natural language questions. Uses DuckDB Friendly SQL idioms.
argument-hint: <SQL or question> [--file path]
allowed-tools: Bash
---

You are helping the user query data using DuckDB.

Input: `$@`

Follow these steps in order.

## Step 1 — Resolve state and determine the mode

Look for an existing state file in either location:

```bash
STATE_DIR=""
test -f .duckdb-skills/state.sql && STATE_DIR=".duckdb-skills"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
PROJECT_ID="$(echo "$PROJECT_ROOT" | tr '/' '-')"
test -f "$HOME/.duckdb-skills/$PROJECT_ID/state.sql" && STATE_DIR="$HOME/.duckdb-skills/$PROJECT_ID"
```

If found, verify the databases it references are still accessible:

```bash
duckdb -init "$STATE_DIR/state.sql" -c "SHOW DATABASES;"
```

Now determine the mode:

- **Ad-hoc mode** if: the `--file` flag is present, or the SQL references file paths/literals (e.g. `FROM 'data.csv'`), or `STATE_DIR` is empty.
- **Session mode** if: `STATE_DIR` is set and the input references table names, is natural language, or is SQL without file references.

If no state file exists and no file is referenced, fall back to ad-hoc mode against `:memory:` — the user must reference files directly in their SQL.

If the state file exists but any ATTACH in it fails, warn the user and fall back to ad-hoc mode.

## Step 2 — Check DuckDB is installed (and which version)

```bash
command -v duckdb && duckdb --version
```

If not found, delegate to `/duckdb-skills:install-duckdb` and then continue.

Remember the major version: **DuckDB 2.x** has a CLI *agent mode*, new syntax (`$var`, `FETCH FIRST`,
`NEAREST` joins, triggers, `CONNECT`) and a few breaking changes; **1.x** has none of these, so do not
generate 2.0-only syntax or flags for it. Details: `/duckdb-skills:duckdb-2-0`.

## Step 3 — Generate SQL if needed

If the input is natural language (not valid SQL), generate SQL using the Friendly SQL reference below.

In **session mode**, first retrieve the schema to inform query generation:

```bash
duckdb -init "$STATE_DIR/state.sql" -csv -c "
SELECT table_name FROM duckdb_tables() ORDER BY table_name;
"
```

Then for relevant tables:

```bash
duckdb -init "$STATE_DIR/state.sql" -csv -c "DESCRIBE <table_name>;"
```

Use the schema context and the Friendly SQL reference to generate the most appropriate query.

## Step 4 — Estimate result size

Before executing, estimate whether the query could produce a very large result that would
consume excessive tokens when returned to this conversation.

**Session mode** — check row counts for the tables involved:

```bash
duckdb -init "$STATE_DIR/state.sql" -csv -c "
SELECT table_name, estimated_size, column_count
FROM duckdb_tables()
WHERE table_name IN ('<table1>', '<table2>');
"
```

**Ad-hoc mode** — probe the source:

```bash
duckdb :memory: -csv -c "
SET allowed_paths=['FILE_PATH'];
SET enable_external_access=false;
SET allow_persistent_secrets=false;
SET lock_configuration=true;
SELECT count() AS row_count FROM 'FILE_PATH';
"
```

**Evaluate**:
- If the query already has a `LIMIT`, `count()`, or other aggregation that bounds the output -> safe, proceed.
- If the source has **>1M rows** and the query has no LIMIT or aggregation -> tell the user:
  *"This query would return a very large result set. Displaying it here would consume a lot of tokens and increase cost. I'd recommend adding `LIMIT 1000` or an aggregation to keep the output manageable."*
  Ask for confirmation before running as-is.
- If the data size is **>10 GB** -> additionally warn:
  *"This table is over 10 GB — the query may take a while to complete."*
  Proceed if the user confirms.

Skip this step for queries that are intrinsically bounded (e.g. `DESCRIBE`, `SUMMARIZE`, aggregations, `count()`).

**DuckDB 2.x extras** (skip on 1.x):
- `DESCRIBE <query>` returns the result columns without running the query.
- `EXPLAIN` prints a compact plan with row estimates in agent mode (`EXPLAIN (FORMAT compact)` elsewhere).
- Add `SET max_execution_time = 60000;` (milliseconds) before an expensive query so it cannot run away.
- In agent mode the CLI itself prints `estimate: ~N rows read ...` on stderr for statements that read
  1M+ rows and stops printing after the cap; treat that line like the estimate above and rewrite the
  query (filter, aggregate, `LIMIT`) instead of waiting.

## Step 5 — Execute the query

**Output format.**
- **DuckDB 2.x:** when this skill runs inside a coding agent, the CLI turns on *agent mode* by itself
  (an agent environment variable such as `CLAUDECODE` is set and stdout is a pipe) **as long as you do
  not pass `-csv`, `-json` or `-markdown`**. Those flags switch it off. So on 2.x omit `-csv` below, or
  force it with `DUCKDB_AGENT_MODE=1 duckdb ...` (older CLIs ignore the variable). You then get compact
  Markdown tables, JSON errors, and a footer with the row count and a result hash. See
  `/duckdb-skills:duckdb-2-0` (`references/agent-mode.md`).
- **DuckDB 1.x (or when exact CSV is required):** keep `-csv`, and bound the output yourself (`LIMIT`,
  aggregation) because there are no result caps.

The commands below show `-csv`; drop it on 2.x as described above.

**Ad-hoc mode** (sandboxed — only the referenced file is accessible):

```bash
duckdb :memory: -csv <<'SQL'
SET allowed_paths=['FILE_PATH'];
SET enable_external_access=false;
SET allow_persistent_secrets=false;
SET lock_configuration=true;
<QUERY>;
SQL
```

Replace `FILE_PATH` with the actual file path extracted from the query or `--file` argument.
If multiple files are referenced, include all paths in the `allowed_paths` list.

**Session mode** (user-trusted database):

```bash
duckdb -init "$STATE_DIR/state.sql" -csv -c "<QUERY>"
```

For multi-line queries, use a heredoc with `-init`:

```bash
duckdb -init "$STATE_DIR/state.sql" -csv <<'SQL'
<QUERY>;
SQL
```

Always use heredocs (`<<'SQL'`) for multi-line queries to avoid shell quoting issues.

## Step 6 — Handle errors

- **Syntax error**: show the error, suggest a corrected query, and re-run.
- **Missing extension** (e.g. `Extension "X" not loaded`): delegate to `/duckdb-skills:install-duckdb <ext>`, then retry.
- **Table not found** (session mode): list available tables with `FROM duckdb_tables()` and suggest corrections.
- **File not found** (ad-hoc mode): use `find "$PWD" -name "<filename>" 2>/dev/null` to locate the file and suggest the corrected path.
- **Persistent or unclear DuckDB error**: use `/duckdb-skills:duckdb-docs <error message or relevant keywords>` to search the documentation for guidance, then apply the fix and retry.
- **Errors that appear only on DuckDB 2.x** (the full table is in `/duckdb-skills:duckdb-2-0`, `references/migration.md`):
  - `Deprecated lambda arrow (->) detected` → rewrite the lambda as `lambda x: x + 1`.
  - `Division by zero in expression (1 // 0)` → `TRY(a // b)` or guard the divisor.
  - `MERGE INTO command cannot affect the same target row more than once` → deduplicate the source rows.
  - `Trying to read a database file with version number 69` (on an old CLI) → the file was written by
    2.0; upgrade the CLI or re-create the file with `-storage-version`.
  - In agent mode errors arrive as JSON on stderr (`exception_type`, `exception_message`,
    `error_subtype`, `position`); read `exception_message` and `error_subtype` instead of pattern-matching text.

## Step 7 — Present results

Show the query output to the user. If the result has more than 100 rows, note the truncation and suggest adding `LIMIT` to the query.

**Agent-mode footers (DuckDB 2.x).** Read the last line of the output before summarizing:
- `first 20 and last 20 of N rows` → only 40 of N rows were shown; do not claim things about the omitted rows.
  Aggregate in SQL, or re-run with `.maxrows -1` / `.maxbytes 0` only if the full result is really needed.
- `first 20 of at least N rows (query stopped early ...)` → N is a lower bound.
- `hash ...` → an order-independent hash of the whole result; if two runs print the same hash the
  result did not change (useful after editing a query).

For natural language questions, also provide a brief interpretation of the results.

---

## DuckDB Friendly SQL Reference

When generating SQL, prefer these idiomatic DuckDB constructs:

### Compact clauses
- **FROM-first**: `FROM table WHERE x > 10` (implicit `SELECT *`)
- **GROUP BY ALL**: auto-groups by all non-aggregate columns
- **ORDER BY ALL**: orders by all columns for deterministic results
- **SELECT * EXCLUDE (col1, col2)**: drop columns from wildcard
- **SELECT * REPLACE (expr AS col)**: transform a column in-place
- **UNION ALL BY NAME**: combine tables with different column orders
- **Percentage LIMIT**: `LIMIT 10%` returns a percentage of rows
- **Prefix aliases**: `SELECT x: 42` instead of `SELECT 42 AS x`
- **Trailing commas** allowed in SELECT lists

### Query features
- **count()**: no need for `count(*)`
- **Reusable aliases**: use column aliases in WHERE / GROUP BY / HAVING
- **Lateral column aliases**: `SELECT i+1 AS j, j+2 AS k`
- **COLUMNS(*)**: apply expressions across columns; supports regex, EXCLUDE, REPLACE, lambdas
- **FILTER clause**: `count() FILTER (WHERE x > 10)` for conditional aggregation
- **GROUPING SETS / CUBE / ROLLUP**: advanced multi-level aggregation
- **Top-N per group**: `max(col, 3)` returns top 3 as a list; also `arg_max(arg, val, n)`, `min_by(arg, val, n)`
- **DESCRIBE table_name**: schema summary (column names and types)
- **SUMMARIZE table_name**: instant statistical profile
- **PIVOT / UNPIVOT**: reshape between wide and long formats
- **SET VARIABLE x = expr**: define SQL-level variables, reference with `getvariable('x')`

### Data import
- **Direct file queries**: `FROM 'file.csv'`, `FROM 'data.parquet'`
- **Globbing**: `FROM 'data/part-*.parquet'` reads multiple files
- **Auto-detection**: CSV headers and schemas are inferred automatically

### Expressions and types
- **Dot operator chaining**: `'hello'.upper()` or `col.trim().lower()`
- **List comprehensions**: `[x*2 FOR x IN list_col]`
- **List/string slicing**: `col[1:3]`, negative indexing `col[-1]`
- **STRUCT.* notation**: `SELECT s.* FROM (SELECT {'a': 1, 'b': 2} AS s)`
- **Square bracket lists**: `[1, 2, 3]`
- **format()**: `format('{}->{}', a, b)` for string formatting

### Joins
- **ASOF joins**: approximate matching on ordered data (e.g. timestamps)
- **POSITIONAL joins**: match rows by position, not keys
- **LATERAL joins**: reference prior table expressions in subqueries

### Data modification
- **CREATE OR REPLACE TABLE**: no need for `DROP TABLE IF EXISTS` first
- **CREATE TABLE ... AS SELECT (CTAS)**: create tables from query results
- **INSERT INTO ... BY NAME**: match columns by name, not position
- **INSERT OR IGNORE INTO / INSERT OR REPLACE INTO**: upsert patterns

### New in DuckDB 2.0 (do not use on 1.x)
- **`$name` variable shorthand**: `SET VARIABLE t = 100; SELECT * FROM sales WHERE amount > $t` (same as `getvariable('t')`)
- **`FETCH FIRST`**: `... ORDER BY x FETCH FIRST 5 ROWS ONLY`; with paging `OFFSET 5 ROWS FETCH NEXT 10 ROWS ONLY`
- **NEAREST joins** (top-k as a join): `FROM users q JOIN products t NEAREST 3 BY DISTANCE array_distance(q.emb, t.emb)`; `APPROX NEAREST k BY SIMILARITY ...` for approximate search
- **Data-modifying CTEs**: `WITH moved AS MATERIALIZED (DELETE FROM staging RETURNING *) INSERT INTO archive SELECT * FROM moved;` (`INSERT`/`UPDATE`/`DELETE`/`COPY` allowed; use `RETURNING` and `MATERIALIZED` when later steps depend on it)
- **Nested schemas**: `CREATE SCHEMA finance.reports;` then `finance.reports.q3`
- **`SELECT * EXCEPT (col)`** is a synonym of `EXCLUDE`; backtick-quoted identifiers work: `` `my col` ``
- **VARIANT** (semi-structured data, faster than JSON text): `payload::JSON::VARIANT`,
  `variant_type`, `variant_keys`, `variant_extract(v, 'field')`, `variant_extract_string(v, 'field')`,
  `variant_exists`, `variant_contains`, aggregates `variant_group_object(k, v)` / `variant_group_array(x)`
- **JSON mutation**: `json_set`, `json_insert`, `json_replace`, `json_remove` return a modified copy
- **Lambdas use the Python style**: `list_transform(l, lambda x: x + 1)`; the old `x -> x + 1` is disabled by default
- **`EXPLAIN (SQL) SELECT ...`** prints the optimized plan as SQL; `EXPLAIN (FORMAT compact)` one operator per line
- **Triggers**: `CREATE TRIGGER ... AFTER INSERT ON t REFERENCING NEW TABLE AS n FOR EACH STATEMENT <stmt>` (statement-level `AFTER` triggers are the safe choice; row-level `BEFORE`/`UPDATE` triggers are not supported yet)
- **Remote DuckDB**: `ATTACH 'quack:host' AS qk (TOKEN '...'); CONNECT qk; ... DISCONNECT;`

### 2.0 behavior changes that silently alter results
- `~` / `!~` now do **partial** regex matching (`'abc' ~ 'b'` is `true`); use `regexp_full_match(s, p)` for full matches
- `2 * 3!` is `12` (the factorial `!` binds tighter); `X'41'` is a `BLOB`, `B'101'` a `BITSTRING`
- Integer `//` and `%` by zero raise an error (use `TRY(...)`); `1 / 0` still returns `inf`
- An untyped `NULL` keeps type `"NULL"` in `CREATE TABLE AS SELECT NULL AS x`; cast it (`NULL::VARCHAR`)

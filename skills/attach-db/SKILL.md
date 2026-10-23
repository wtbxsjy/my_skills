---
name: attach-db
description: >
  Attach a DuckDB database file for use with /duckdb-skills:query.
  Explores the schema (tables, columns, row counts) and writes a SQL state file
  so subsequent queries can restore this session automatically via duckdb -init.
argument-hint: <path-to-database.duckdb>
allowed-tools: Bash
---

You are helping the user attach a DuckDB database file for interactive querying.

Database path given: `$0`

Follow these steps in order, stopping and reporting clearly if any step fails.

**State file convention**: see the "Resolve state directory" section below. All skills share a single `state.sql` file per project. Once resolved, any skill can use it with `duckdb -init "$STATE_DIR/state.sql" -c "<QUERY>"`.

## Step 1 — Resolve the database path

If `$0` is a relative path, resolve it against `$PWD` to get an absolute path (`RESOLVED_PATH`).

```bash
RESOLVED_PATH="$(cd "$(dirname "$0")" 2>/dev/null && pwd)/$(basename "$0")"
```

Check the file exists:

```bash
test -f "$RESOLVED_PATH"
```

- **File exists** -> continue to Step 2.
- **File not found** -> ask the user if they want to create a new empty database (DuckDB creates the file on first write). If yes, continue. If no, stop.

## Step 2 — Check DuckDB is installed

```bash
command -v duckdb
```

If not found, delegate to `/duckdb-skills:install-duckdb` and then continue.

## Step 3 — Validate the database

```bash
duckdb "$RESOLVED_PATH" -c "PRAGMA version;"
```

- **Success** -> continue. Note the version it prints (`v2.x` or `v1.x`).
- **Failure** -> report the error clearly (e.g. corrupt file, not a DuckDB database) and stop.
  - **`Trying to read a database file with version number 69, but we can only read versions between ...`**
    is *not* corruption: the file was written by DuckDB 2.0 (storage format v69) and your CLI is older.
    Offer to upgrade the CLI (`/duckdb-skills:install-duckdb --update`), or ask whoever owns the file to
    re-create it for the old version (`duckdb file.db -storage-version v1.5.6 ...`). Stop until resolved.

**DuckDB 2.0 storage compatibility (tell the user when it matters).** A 2.0 CLI can read and write
older database files and keeps their old storage version, so older tools can still open them. But a
**new** file created by 2.0 uses storage version 69 and **cannot be opened by DuckDB < 2.0**. If the
user says this database is shared with other tools, CI jobs or colleagues who may run 1.x, create it
with `ATTACH '<path>' AS <alias> (STORAGE_VERSION 'v1.5.0');` (or `duckdb -storage-version v1.5.0`)
instead of the default. See `/duckdb-skills:duckdb-2-0` (`references/migration.md`).

## Step 4 — Explore the schema

First, list all tables:

```bash
duckdb "$RESOLVED_PATH" -csv -c "
SELECT table_name, estimated_size
FROM duckdb_tables()
ORDER BY table_name;
"
```

If the database has **no tables**, note that it is empty and skip to Step 5.

For each table discovered (up to 20), run:

```bash
duckdb "$RESOLVED_PATH" -csv -c "
DESCRIBE <table_name>;
SELECT count() AS row_count FROM <table_name>;
"
```

Collect the column definitions and row counts for the summary.

## Step 5 — Resolve the state directory

Check if a state file already exists in either location:

```bash
# Option 1: in the project directory
test -f .duckdb-skills/state.sql && STATE_DIR=".duckdb-skills"

# Option 2: in the home directory, scoped by project root path
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
PROJECT_ID="$(echo "$PROJECT_ROOT" | tr '/' '-')"
test -f "$HOME/.duckdb-skills/$PROJECT_ID/state.sql" && STATE_DIR="$HOME/.duckdb-skills/$PROJECT_ID"
```

If **neither exists**, ask the user:

> Where would you like to store the DuckDB session state for this project?
>
> 1. **In the project directory** (`.duckdb-skills/state.sql`) — colocated with the project, easy to find. You can choose to gitignore it.
> 2. **In your home directory** (`~/.duckdb-skills/<project-id>/state.sql`) — keeps the project directory clean.

Based on their choice:

**Option 1:**
```bash
STATE_DIR=".duckdb-skills"
mkdir -p "$STATE_DIR"
```
Then ask: *"Would you like to gitignore `.duckdb-skills/`?"* If yes:
```bash
echo '.duckdb-skills/' >> .gitignore
```

**Option 2:**
```bash
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "$PWD")"
PROJECT_ID="$(echo "$PROJECT_ROOT" | tr '/' '-')"
STATE_DIR="$HOME/.duckdb-skills/$PROJECT_ID"
mkdir -p "$STATE_DIR"
```

## Step 6 — Append to the state file

`state.sql` is a shared, accumulative init file used by all duckdb-skills. It may already contain macros, LOAD statements, secrets, or other ATTACH statements written by other skills. **Never overwrite it** — always check for duplicates and append.

Derive the database alias from the filename without extension (e.g. `my_data.duckdb` → `my_data`). Check if this ATTACH already exists:

```bash
grep -q "ATTACH.*RESOLVED_PATH" "$STATE_DIR/state.sql" 2>/dev/null
```

If not already present, append:

```bash
cat >> "$STATE_DIR/state.sql" <<'STATESQL'
ATTACH IF NOT EXISTS 'RESOLVED_PATH' AS my_data;
USE my_data;
STATESQL
```

Replace `RESOLVED_PATH` and `my_data` with the actual values. If the alias would conflict with an existing one in the file, ask the user for a name.

## Step 7 — Verify the state file works

```bash
duckdb -init "$STATE_DIR/state.sql" -c "SHOW TABLES;"
```

If this fails, fix the state file and retry.

## Step 8 — Report

Summarize for the user:

- **Database path**: the resolved absolute path
- **Alias**: the database alias used in the state file
- **State file**: the resolved `STATE_DIR/state.sql` path
- **Tables**: name, column count, row count for each table (or note the DB is empty)
- Confirm the database is now active for `/duckdb-skills:query`

If the database is empty, suggest creating tables or importing data.

## Attaching a remote DuckDB server (DuckDB 2.0 and later)

If `$0` starts with `quack:` (for example `quack:db.example.com` or `quack:localhost:9494`), it is a
remote DuckDB server reached over the Quack protocol, not a file. Skip Steps 1 and 3, require
DuckDB 2.x (`duckdb --version`), and instead:

1. Ask the user for the access token. **Do not write the token into `state.sql`** if that file lives
   in the project directory and may be committed. Prefer a secret scoped to the server URI:
   ```sql
   CREATE SECRET (TYPE quack, TOKEN '<token>', SCOPE 'quack:db.example.com');
   ```
   (`CREATE PERSISTENT SECRET` keeps it across sessions in DuckDB's secret directory, outside the
   project.) A token can also be passed once with `ATTACH ... (TOKEN '<token>')`, which overrides a secret.
2. Validate: `duckdb -c "ATTACH 'quack:db.example.com' AS qk (TYPE quack); FROM qk.query('SELECT 42');"`
   or the stateless `FROM quack_query('quack:db.example.com', 'SELECT 42', token = '<token>')`.
3. Explore with `DESCRIBE`/`duckdb_tables()` qualified by the alias (`qk.`), or route the whole
   session to the server with `CONNECT qk;` (undo with `DISCONNECT;`).
4. Append to the state file (Step 6) only the non-secret lines, e.g.
   `ATTACH IF NOT EXISTS 'quack:db.example.com' AS qk (TYPE quack);` — this relies on the secret
   existing at restore time; say so in the report.

Notes: plain HTTP is used automatically only for local URIs (`localhost`, `127.0.0.1`, `::1`),
HTTPS otherwise; the default port is 9494. `CONNECT` also accepts `'postgres:...'` connection
strings, but plain local database files do not support `CONNECT`. This section is based on the
DuckDB 2.0 documentation; the quack extension was not exercised when the skill was written.

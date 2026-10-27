---
name: install-duckdb
description: >
  Install or update DuckDB extensions. Each argument is either a plain
  extension name (installs from core) or name@repo (e.g. magic@community).
  Pass --update to update extensions instead of installing.
argument-hint: "[--update] [ext1 ext2@repo ext3 ...]"
allowed-tools: Bash
---

Arguments: `$@`

Each extension argument has the form `name` or `name@repo`.
- `name` → `INSTALL name;`
- `name@repo` → `INSTALL name FROM repo;`

## Step 1 — Locate DuckDB

```bash
DUCKDB=$(command -v duckdb)
```

If not found, tell the user:

> **DuckDB is not installed.** Install it first with one of:
> - macOS:   `brew install duckdb`
> - Linux:   `curl -fsSL https://install.duckdb.org | sh`
> - Windows: `winget install DuckDB.cli`
>
> Then re-run `/duckdb-skills:install-duckdb`.

Stop if DuckDB is not found.

## Step 2 — Check for --update flag

If `--update` is present in `$@`, remove it from the argument list and set mode to **update**.
Otherwise mode is **install**.

## Step 3 — Build and run statements

**Install mode:**

Parse each remaining argument:
- If it contains `@`, split on `@` → `INSTALL <name> FROM <repo>;`
- Otherwise → `INSTALL <name>;`

Run all in a single DuckDB call:

```bash
"$DUCKDB" :memory: -c "INSTALL <ext1>; INSTALL <ext2> FROM <repo2>; ..."
```

**Update mode:**

First, check if the DuckDB CLI itself is up to date:

```bash
CURRENT=$(duckdb --version | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
LATEST=$(curl -fsSL https://duckdb.org/data/latest_stable_version.txt)
```

- If `CURRENT` == `LATEST` → report DuckDB CLI is up to date.
- If `CURRENT` != `LATEST` and the **major version is the same** → ask the user:
  > **DuckDB CLI is outdated** (installed: `CURRENT`, latest: `LATEST`). Upgrade now?

  If the user agrees, detect the platform and run the appropriate upgrade command:
  - macOS (`brew` available): `brew upgrade duckdb`
  - Linux: `curl -fsSL https://install.duckdb.org | sh`
  - Windows: `winget upgrade DuckDB.cli`
- If `CURRENT` is **1.x** and `LATEST` is **2.x** (DuckDB 2.0, released 2026-10-21) → this is a major
  upgrade. Do not just run the command; first tell the user, briefly:
  > **DuckDB 2.0 is a major upgrade.** New database files it creates cannot be opened by DuckDB 1.x
  > (storage format v69). Old files keep working, and 2.0 keeps their old format. Breaking changes:
  > single-arrow lambdas (`x -> ...`) are disabled, integer division by zero now raises an error,
  > `~` does partial regex matching, and a few more (see `/duckdb-skills:duckdb-2-0`, `references/migration.md`).
  > Upgrade now? 2.0.0 is an LTS release; the first patch release is planned for November 2026.

  Proceed only if the user agrees (for mission-critical workloads suggest testing first). Afterwards
  run `duckdb --version`, then update/reinstall extensions (see below): extensions are installed per
  DuckDB version, so extensions installed for 1.x are not reused by 2.x.
  Note: macOS x86_64 (`osx_amd64`) is being phased out — community extensions are no longer built for it.

Then update extensions:

- No extension names → update all: `UPDATE EXTENSIONS;`
- With extension names → update in a single call (ignore `@repo`):
  `UPDATE EXTENSIONS (<name1>, <name2>, ...);`

```bash
"$DUCKDB" :memory: -c "UPDATE EXTENSIONS;"
# or
"$DUCKDB" :memory: -c "UPDATE EXTENSIONS (<ext1>, <ext2>, ...);"
```

Report success or failure after the call completes.

## DuckDB 2.0 notes

- After a 1.x → 2.x upgrade, `UPDATE EXTENSIONS;` only updates what is already installed for the
  current version. Re-run `INSTALL <name>;` for the extensions the project needs (`httpfs`, `spatial`,
  `excel`, `fts`, `avro`, `sqlite_scanner`, `quack`, `ducklake`, ...). Extensions that depend on the C
  API may lag a few days behind a major release; if `INSTALL` reports that an extension is not
  available for `v2.0.0` for this platform, say so instead of retrying.
- New core extension: `quack` (DuckDB as a server, `CALL quack_serve(...)`, `CONNECT`).
  `legacy_parser` restores the old SQL parser: `INSTALL AND LOAD legacy_parser; SET enable_legacy_parser = true;`
  (only as a stop-gap when a query that parsed on 1.x no longer parses; please report such queries upstream).
- Organizations can host their own signed extension repository (work in progress, syntax may change):
  ```sql
  SET allow_extension_repositories = 'allowed';
  CREATE EXTENSION REPOSITORY my_repo WITH PREFIX 'https://extensions.example.org';
  INSTALL AND LOAD my_ext FROM my_repo;
  ```
  Note that `name@repo` in this skill maps to `INSTALL name FROM repo;`, so `my_ext@my_repo` works
  once the repository exists.
- To see which extension provides a function on 2.x: `SELECT function_name, extension_name FROM duckdb_functions() WHERE function_name = '<name>';`
  (the `extension_name` column is new in 2.0).

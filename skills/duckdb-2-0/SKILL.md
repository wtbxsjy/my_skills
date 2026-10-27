---
name: duckdb-2-0
description: "DuckDB 2.0 (LTS) for agents: check version, use CLI agent mode (compact output, result caps, JSON errors), migrate from 1.x (storage v69, lambda syntax, PEG parser), use Quack/VARIANT/triggers/NEAREST joins. Use for DuckDB 2.0, upgrading, post-upgrade errors."
argument-hint: <question, or "agent mode" / "migrate" / "what's new">
allowed-tools: Bash
---

You are helping with DuckDB 2.0. Question: `$@`

This skill extends the duckdb-skills collection (originally from github.com/duckdb/duckdb-skills,
which has no 2.0 support yet). The other skills (`query`, `read-file`, `attach-db`, `duckdb-docs`,
`install-duckdb`, ...) link here for 2.0 specifics.

## Step 1 — Find out which DuckDB you are talking to

```bash
duckdb --version
duckdb :memory: -c "PRAGMA version;"
```

- Not found → use `/duckdb-skills:install-duckdb`.
- `v2.x` → everything below applies.
- `v1.x` → do **not** use 2.0-only syntax (`$var`, `FETCH FIRST`, `NEAREST`, `CREATE TRIGGER`,
  `CONNECT`, `-agent`, `.manual`, ...). Offer the upgrade path in `references/migration.md` first.

For Python/Node/other clients check the package version instead (`python -c "import duckdb; print(duckdb.__version__)"`).
Agent mode exists only in the CLI.

## Step 2 — Pick the task

| The user wants... | Do this |
|---|---|
| A summary of what changed in 2.0 | read `references/whats-new.md` and answer from it |
| To run DuckDB from an agent efficiently (tokens, truncation, errors) | read `references/agent-mode.md` |
| To upgrade, or a query/file broke after upgrading | read `references/migration.md`, match the symptom in its triage table |
| Exact syntax of a function or statement | `duckdb -manual <function>` (2.0 CLI), `/duckdb-skills:duckdb-docs <topic>`, or `duckdb_functions()` |
| To run queries | `/duckdb-skills:query` (it already contains the 2.0 notes) |

## Agent mode in 30 seconds

- The 2.0 CLI switches to agent mode **automatically** when an agent environment variable
  (`CLAUDECODE`, `AI_AGENT`, `CODEX_CI`, `CURSOR_AGENT`, `GEMINI_CLI`, ...) is set, stdout is not a
  terminal, and no output-format flag (`-csv`, `-json`, `-markdown`) was given.
- Force it with `-agent` or `DUCKDB_AGENT_MODE=1`; disable with `-no-agent` or `DUCKDB_AGENT_MODE=0`.
  Prefer the environment variable in shared commands: older CLIs ignore it, but reject `-agent`.
- Output: compact Markdown tables with column types, at most 1,000 rows / 10,000 bytes / 500
  characters per cell shown whole (otherwise first and last 20 rows), a footer with the row count and an
  order-independent hash, errors as JSON on stderr, `estimate:` / `progress:` lines on stderr for
  queries reading 1M+ rows.
- **Always read the footer.** `first 20 and last 20 of N rows` or `at least N rows (query stopped
  early)` means you saw only part of the result; raise limits with `.maxrows -1`, `.maxbytes 0`,
  `.maxcellwidth 0` or, better, aggregate / `LIMIT` in SQL.
- Useful for agents: `SET max_execution_time = <ms>`, `DESCRIBE <query>`, `SUMMARIZE`, `.tables`,
  `duckdb_functions()`, `.help agent`.

## Common recipes (all verified on DuckDB 2.0.0 unless noted)

```sql
SET VARIABLE threshold = 100;
SELECT * FROM sales WHERE amount > $threshold FETCH FIRST 10 ROWS ONLY;      -- $var and FETCH FIRST

SELECT list_transform([1, 2, 3], lambda x: x + 1);                            -- new lambda syntax

SELECT q.user_id, t.product_id FROM users q                                   -- top-k similarity as a join
INNER JOIN products t NEAREST 3 BY DISTANCE array_distance(q.embedding, t.embedding);

WITH moved AS MATERIALIZED (DELETE FROM staging RETURNING *)                  -- data-modifying CTE
INSERT INTO archive SELECT * FROM moved;

SELECT variant_type(payload), variant_extract_string(payload, 'name') FROM events;  -- VARIANT
SELECT json_set('{"a":1}', '$.b', '2');                                       -- JSON mutation
```

Remote DuckDB over Quack (documented; needs the `quack` extension, not run here):

```sql
ATTACH 'quack:server.example.com' AS qk (TOKEN 'my_token');
CONNECT qk;           -- queries now run on the server
DISCONNECT;
```

Never write a Quack token into a shared `state.sql` that is committed to git; create a secret
instead (see the Quack security docs).

## Step 3 — Answer

Lead with the answer, quote the exact error text or syntax, and say which parts you verified by
running DuckDB 2.0.0 versus which come only from the documentation (agent mode, Quack, extension
repositories). When the user is upgrading, always mention the storage-format one-way door.

If the docs and your memory disagree, search `/duckdb-skills:duckdb-docs` (2.0 docs are indexed
under version `2.0`) rather than guessing.

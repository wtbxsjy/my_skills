# DuckDB CLI agent mode (DuckDB 2.0+)

Agent mode renders the CLI's output for an AI coding agent instead of a person at a terminal.
It is a **CLI feature only** (not the Python/Node/... clients and not a SQL setting). Everything
below comes from the official docs (`docs/2.0/clients/cli/agent_mode`) and the announcement blog
post; it was not executed locally because only the Python 2.0 package was available.

> "Agent mode" is not a model and not an AI feature inside the database. It only changes how the
> CLI prints results, errors, plans and progress.

## When it turns on

Automatically, when **all three** hold:

1. A known agent environment variable is set — `AI_AGENT`, `AGENT` (Claude Code, Goose, Amp),
   `CLAUDECODE` (Claude Code), `CODEX_CI` / `CODEX_SANDBOX` / `CODEX_THREAD_ID` (Codex),
   `CURSOR_AGENT` (Cursor), `GEMINI_CLI` (Gemini CLI),
   `COPILOT_AGENT` / `COPILOT_CLI` / `COPILOT_AGENT_SESSION_ID` (GitHub Copilot);
2. stdout is **not** a terminal (the agent captures output through a pipe);
3. **no output-format flag** was passed (`-csv`, `-json`, `-markdown`, ... count as a deliberate
   choice and switch auto-detection off).

Explicit control:

| Control | Effect |
|---|---|
| `-agent` | force on |
| `-no-agent` | force off |
| `DUCKDB_AGENT_MODE=1` / `=0` | force on / off from the environment (flags win over the variable) |
| `.show` | prints `agent: claude-code` (or similar) when active |
| `.help agent` | prints the longer explanation of the rules |

`-agent` combines with format flags: `duckdb -agent -csv` keeps agent behavior (JSON errors, caps,
estimates) and only changes how rows are printed.

When auto-detection turns it on, the CLI prints one line on stderr, e.g.
`duckdb agent mode on: CLAUDECODE is set and stdout is not a terminal; -no-agent turns it off, .help agent explains the output`.
Hide it with `.startup_text none` as the first line of `~/.duckdbrc`.
If an agent is *not* recognized and a pipe write fails, one `hint: -agent renders errors as JSON ...` line is printed on stderr.

## What changes (all defaults; explicit `.mode`, `.maxrows`, `EXPLAIN (FORMAT ...)` still win)

**Compact Markdown tables** with the type in the header cell and no padding (25–65% smaller than boxes):

```text
| name:VARCHAR | n:BIGINT | total:HUGEINT | avg_amount:DECIMAL(10,2) |
|---|---|---|---|
| customer_0 | 3 | 777 | 259.00 |
```

**Result caps.** A result of up to **1,000 rows and 10,000 bytes** is shown whole. A larger result is
shown as the **first 20 and last 20 rows** around a marker row such as `| … 4960 rows omitted … |`.
Cells are cut at **500 characters** with a marker like `…(+4500 chars)`.

| Dot command | Meaning |
|---|---|
| `.maxrows N` | max rows shown whole (`-1` = all) |
| `.maxbytes N` | max bytes of rows shown whole (`0` = all) |
| `.maxcellwidth N` | max characters per cell (`0` = all) |

**Footer with the row count and a result hash**, e.g.
`first 20 and last 20 of 5000 rows (.maxbytes 0 for all), hash 7389c2f5ff3cefb6`.
The hash covers the *whole* result including rows past the cap, ignores row order and distinguishes
`NULL` from the string `'NULL'`; compare two footers to learn whether a result changed after an edit.
The footer is printed for empty results, results of 10 or more rows, and whenever the output was
capped. It is omitted when the query was stopped early.

**Early stop.** After the cap, remaining rows are only counted and hashed; after 100,000 more rows
the query is stopped and the count is a lower bound, e.g.
`first 20 of at least 102400 rows (query stopped early; .maxrows -1 for all)`.
`FROM range(1_000_000_000);` returns in about 30 ms.

**Errors as JSON on stderr** (`errors_as_json`), shell errors such as an unknown dot command included:

```json
{"exception_type":"Binder","exception_message":"Referenced column \"foo\" not found in FROM clause!\nCandidate bindings: \"bar\"","error_subtype":"COLUMN_NOT_FOUND","location":"[7,3]","position":"7","name":"foo"}
```

**Compact query plans.** `EXPLAIN` defaults to `FORMAT compact`, one operator per line, indented by
depth, estimates in parentheses (`HASH_JOIN (est=0) Join Type: INNER; ...`).
`EXPLAIN ANALYZE` starts with `QUERY (time=0.0012s, read=1.2 MB)`.
`EXPLAIN (FORMAT compact)` also works outside agent mode (verified on 2.0.0).

**Cost estimate and progress on stderr.** When the planner expects to read **1,000,000 rows or more**:
`estimate: ~7501215 rows read (lineitem ~6001215, orders ~1500000), ~4 rows returned`.
While a long query runs, a plain line every 5 s replaces the progress bar:
`progress: 42% (elapsed 12.0s, remaining ~16.5s)` then `progress: done (elapsed 28.7s)`.
If the estimate looks too large, interrupt and rewrite the query (filter, aggregate, `LIMIT`).

**`.tables`** prints one line per table with an approximate row count and columns:
`memory.main.t1 (table, ~15 rows): a INTEGER PK, b VARCHAR` — the schema in one call.

## Tips the DuckDB team lists for agents

- `SET max_execution_time = <ms>;` bounds how long a query may run.
- `DESCRIBE <query>` returns the result columns without running the query.
- `SUMMARIZE <table or query>` gives a quick profile.
- `.tables` for the schema; `duckdb_functions()` for function descriptions and examples;
  `duckdb -manual <function>` / `.manual <function>` for a function manual page.

## How the duckdb-skills use it

- Do **not** add `-csv`/`-json`/`-markdown` just to be "machine-friendly" on DuckDB 2.0 if you want
  the caps, hash footer and JSON errors; those flags switch auto-detection off.
- Version-safe way to force it: prefix `DUCKDB_AGENT_MODE=1` (older CLIs ignore an unknown
  environment variable, whereas an unknown flag such as `-agent` makes them fail). Example:
  `DUCKDB_AGENT_MODE=1 duckdb -init "$STATE_DIR/state.sql" -c "FROM t LIMIT 5"`.
- Keep `-csv` when another program must parse the rows exactly (for instance to feed values into
  the next command); keep `-json` when you need typed JSON. You lose the footer and caps then, so
  bound the query yourself (`LIMIT`, aggregation).
- Read the footer before drawing conclusions: "first 20 and last 20 of N rows" or "at least N rows"
  means you saw only part of the result.
- Treat `estimate:` and `progress:` lines on stderr as cost signals, not as part of the data.
- Reported by users (not the DuckDB team): on tiny results plain `-json` can be as small or smaller
  than agent mode because agent mode adds a startup line to stderr on every call; and `-json`
  drops the footer/hash. The saving is in large or wide results, not in every call.

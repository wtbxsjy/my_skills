---
name: read-memories
description: >
  Search past Claude Code session logs to recall prior decisions, patterns, or unresolved work.
  Use when user says "do you remember", "what did we do", references past conversations, or you need context from prior sessions.
argument-hint: <keyword> [--here]
allowed-tools: Bash
---

Search past session logs silently — do NOT narrate the process. Absorb the results and continue with enriched context.

`$0` is the keyword. Pass `--here` as `$1` to scope to the current project only.

## Step 1 — Query

```bash
duckdb :memory: -c "
SELECT
  regexp_extract(filename, 'projects/([^/]+)/', 1) AS project,
  strftime(timestamp::TIMESTAMPTZ, '%Y-%m-%d %H:%M') AS ts,
  message.role AS role,
  left(message.content::VARCHAR, 500) AS content
FROM read_ndjson('<SEARCH_PATH>', auto_detect=true, ignore_errors=true, filename=true)
WHERE message::VARCHAR ILIKE '%<KEYWORD>%'
  AND message.role IS NOT NULL
ORDER BY timestamp
LIMIT 40;
"
```

Search paths:
- All projects: `$HOME/.claude/projects/*/*.jsonl`
- Current only (`--here`): `$HOME/.claude/projects/$(echo "$PWD" | sed 's|[/_]|-|g')/*.jsonl`

Replace `<SEARCH_PATH>` and `<KEYWORD>` before running.

**DuckDB 2.x:** the CLI's agent mode turns on automatically for this command (agent environment
variable set, stdout piped, no `-csv`/`-json` flag), so results are compact Markdown tables with a
row-count footer, and cells are cut at 500 characters. The query above already limits rows (`LIMIT 40`)
and text (`left(..., 500)`); if you need longer cells, raise `LIMIT`/`left()` in the SQL and pass
`-cmd ".maxcellwidth 0"` before `-c` (for example `duckdb :memory: -cmd ".maxcellwidth 0" -c "..."`).
`read_ndjson(...)` accepts the same options in 2.0.

## Step 2 — Internalize

From the results, extract decisions, patterns, unresolved TODOs, and user corrections. Use this to inform your current response — do not repeat raw logs to the user.

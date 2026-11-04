---
name: notion-media-upload
description: >-
  Insert local images or files into a Notion page as native blocks via the
  multipart upload API (the JSON-only MCP cannot). Use for figures or report
  PDFs (把图/PDF 插进 Notion); covers anchors, captions, in-place replacement
  and multi-workspace MCP/DSH setup.
---

# Notion Media Upload

## Overview

The Notion MCP tools in this environment (`mcp__notion__*`) talk JSON only.
Uploading a local file needs a **multipart** body, so the MCP cannot do it: a
markdown image with a local path produces an `image` block whose
`external.url` is `""` (an empty frame in the page).

`scripts/notion_upload.py` closes that gap. It calls the Notion REST API
directly (curl underneath, stdlib only) and does the three-step dance:

1. `POST /v1/file_uploads` — reserve an upload slot (`mode=single_part`);
2. `POST <upload_url>` — send the bytes as `multipart/form-data`;
3. `PATCH /v1/blocks/{page}/children` — insert an `image`/`file` block that
   references the uploaded file (optionally `after` a chosen block).

Result: the file is a **native Notion block** hosted by Notion, exactly as if
it had been dragged in. Blocks can be opened full size, resized, and reordered.

The same `~/.dsh/notion.tokens` file also backs this environment's **multiplexed
Notion MCP**: one server, five tools, four workspaces selected by a `workspace`
argument. See [the multi-workspace setup reference](references/notion-mcp-multiplex-setup.md)
for how that server and its DSH configuration are built.

## Prerequisites

- A token file at `~/.dsh/notion.tokens` (one `label token` per line, e.g.
  `hotmail`, `cuhk`, `bgi`, `polyu`) — pick one with `--workspace`.
- The target page must be **shared with that integration**
  (page `...` → `Connections` → add the integration). Otherwise every call
  returns `404 object_not_found` with a hint. Access is inherited, so sharing a
  parent covers its children; if a page is *moved* out of a shared tree the
  integration can lose access until the new parent is shared.
- Files must fit the **workspace** limit — it varies by workspace (measured:
  cuhk 5 GiB, hotmail/bgi/polyu 5 MiB). Check with
  `notion_upload.py limits --workspace <label>` before uploading.
- Run `scripts/check_workspaces.py` to confirm every label in the token file is
  alive and see `label -> workspace / bot / upload_limit` at a glance.
- Not a converter: `.qmd`/`.html` cannot be embedded. Render to PDF or PNG
  first (PDFs become `file` blocks with Notion's PDF preview).

## Multi-workspace MCP in this environment

Do not spin up one official Notion MCP server per workspace: the official server
exposes 24 tools each, so four workspaces cost 96 tools and ~300 KB of schema in
every request. This machine runs a small multiplexing server instead
(`~/.dsh/notion-multiplex/server.mjs`, stdio JSON-RPC, no dependencies) that
exposes five tools and routes each call by a `workspace` argument:

| piece | path |
|---|---|
| token file (label + token per line, mode 600) | `~/.dsh/notion.tokens` |
| multiplex server + launcher + probe | `~/.dsh/notion-multiplex/{server.mjs,run.sh,probe.mjs}` |
| official per-workspace server (kept for rollback) | `~/.dsh/notion-mcp/run-notion-mcp.sh <label>` |
| DSH MCP config (insert block) | `~/.dsh/profiles/<profile>/cordis.patch.yml` |
| token checker | `scripts/check_workspaces.py` |

The MCP tools are `mcp__notion__search`, `mcp__notion__read_page`,
`mcp__notion__create_page`, `mcp__notion__update_page_markdown`, and
`mcp__notion__api` — all take `workspace`. Changing the YAML requires a client
restart; adding a workspace is just a new token-file line plus a restart. The
rollback config (one official server per workspace) stays in the same insert
block, `disabled: true`.

Read [references/notion-mcp-multiplex-setup.md](references/notion-mcp-multiplex-setup.md)
for the full YAML, the from-scratch rebuild steps, and the permission nuances
(e.g. internal integrations cannot create workspace-level pages).

## Workflow

```bash
U=~/my_skills/skills/notion-media-upload/scripts/notion_upload.py

# 0. optional: confirm token labels, workspaces, and per-workspace size limits
python3 ~/my_skills/skills/notion-media-upload/scripts/check_workspaces.py

# 1. find the page id
python3 $U find "PN 极性"
python3 $U limits                       # check upload size limit

# 2. see the block tree to choose an anchor
python3 $U blocks <page_id>

# 3. dry-run first: shows target anchor + captions, uploads nothing
python3 $U upload <page_id> fig1.png fig2.png \
    --section-end "4. 定性维度" \
    --caption "图 1 · ..." --caption "图 2 · ..." --dry-run

# 4. real run
python3 $U upload <page_id> fig1.png fig2.png \
    --section-end "4. 定性维度" \
    --caption "图 1 · ..." --caption "图 2 · ..."

# 5. verify (or use mcp__notion__read_page)
python3 $U blocks <page_id>
```

### Insertion position

| flag | meaning |
|---|---|
| *(none)* | append at the end of the page |
| `--after <block_id>` | insert right after that block |
| `--section-end "4. 定性维度"` | insert at the end of the H2 section whose text starts with that string (i.e. after its last block, before the next H2) |

Multiple children passed in one `PATCH` keep their order. `--section-end`
matches `heading_2` blocks only, and refuses ambiguous prefixes.

### Captions and replacement

- `--caption` is repeatable; it pairs 1:1 with the file list. Files without a
  caption fall back to the file stem.
- `--manifest captions.json` supplies captions in bulk (a dict of
  `filename -> caption`, or a list of `{"caption": ...}`).
- `--replace-caption "图 6 · DR≥90% 特征 Venn"` finds the **unique** `image` or
  `file` block whose caption matches exactly, uploads the new file, and patches
  that block in place — so the figure stays where it is in the page. It
  refuses when zero or several blocks match.

### Cleanup

`trash-page <page_id>` and `trash-block <block_id>` move test artifacts to the
trash. Always test on a scratch page, never on the real one.

## Troubleshooting

| symptom | cause / fix |
|---|---|
| `invalid_request_url` | endpoint is `/v1/file_uploads` (underscore). `/v1/file/uploads` does not exist. |
| `404 object_not_found ... shared with your integration` | page not connected to the token's integration; share it (`...` → `Connections`) |
| MCP markdown image renders as an empty frame | MCP cannot upload; use this script |
| `body.image.type should be not present` when replacing | update-block payload must not carry the `type` discriminator (`{"image": {"file_upload": {...}}}`) |
| empty/invalid upload (`status != uploaded`) | multipart body missing; `curl -F "file=@path;type=image/png"` |
| file too large | check `limits`; resize/split |
| images inserted in the wrong order | pass all files in one `upload` call (one PATCH keeps order) |
| `unknown workspace "x"` | label typo or missing line in `~/.dsh/notion.tokens`; run `check_workspaces.py` |
| `HTTP 401` | token revoked/rotated; refresh the label's line in the token file |
| upload limit differs between runs | the limit is per workspace (cuhk 5 GiB vs others 5 MiB) |

## Notes

- The block references an uploaded file id hosted by Notion; signed URLs in the
  API response expire, but the block itself keeps working.
- Uploading the same file twice creates two independent blocks — upload only
  when the figure/PDF actually changed.
- The script is deliberately generic (images and non-image files); anything
  Notion cannot preview becomes a downloadable `file` block.

## Files

| path | purpose |
|---|---|
| `scripts/notion_upload.py` | upload local files and insert native blocks (find / blocks / upload / trash / limits) |
| `scripts/check_workspaces.py` | validate every token label: workspace name, bot, upload limit, file mode |
| `references/notion-file-upload-api.md` | raw request/response shapes, payload rules, error catalog, worked case |
| `references/notion-mcp-multiplex-setup.md` | multiplexed MCP architecture, DSH YAML config, rebuild + rollback steps |

See [references/notion-file-upload-api.md](references/notion-file-upload-api.md)
for the raw request/response shapes, the exact payload rules, and a worked
case (16 figures inserted into a report page by section).

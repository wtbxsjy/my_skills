# Notion file upload + block insertion — API notes

Derived from a working implementation (Nov 2026, Notion API version
`2025-09-03`). Everything below was verified against a live workspace.

## 1. Create the upload

```http
POST https://api.notion.com/v1/file_uploads
Authorization: Bearer <token>
Notion-Version: 2025-09-03
Content-Type: application/json

{"mode": "single_part", "filename": "fig1.png", "content_type": "image/png"}
```

Note the **underscore**: `/v1/file_uploads`. `/v1/file/uploads` returns
`400 invalid_request_url`.

Response (abridged):

```json
{
  "object": "file_upload",
  "id": "40e5f2b7-...",
  "status": "pending",
  "upload_url": "https://api.notion.com/v1/file_uploads/<id>/send",
  "filename": "fig1.png",
  "content_type": "image/png"
}
```

## 2. Send the bytes (multipart)

```bash
curl -s -X POST "<upload_url>" \
  -H "Authorization: Bearer <token>" \
  -H "Notion-Version: 2025-09-03" \
  -F "file=@fig1.png;type=image/png"
```

Response: `{"id": "...", "status": "uploaded", ...}`. Any status other than
`uploaded` means the block will not be usable. This multipart step is the
reason the JSON-only MCP tools cannot do uploads.

## 3. Insert a block

Append at the end of the page:

```http
PATCH https://api.notion.com/v1/blocks/<page_id>/children
{"children": [
  {"object": "block", "type": "image", "image": {
    "type": "file_upload",
    "file_upload": {"id": "<upload_id>"},
    "caption": [{"type": "text", "text": {"content": "图 1 · ..."}}]
  }}
]}
```

Insert after a specific block (order among `children` is preserved):

```json
{"after": "<block_id>", "children": [ ... ]}
```

Non-image file (PDF, CSV, zip): use a `file` block instead of `image`:

```json
{"object": "block", "type": "file", "file": {
  "type": "file_upload", "file_upload": {"id": "<upload_id>"},
  "name": "report.pdf",
  "caption": [{"type": "text", "text": {"content": "..."}}]
}}
```

## 4. Replace media in an existing block

`PATCH /v1/blocks/<block_id>` with **no type discriminator**:

```json
{"image": {"file_upload": {"id": "<new_upload_id>"}}}
```

Sending `{"image": {"type": "file_upload", ...}}` fails with
`validation_error: body.image.type should be not present`. This is the opposite
of the create-block payload, which *requires* `type`.

## 5. Limits and metadata

- `GET /v1/users/me` → `bot.workspace_limits.max_file_upload_size_in_bytes`
  (observed: `5242880`, i.e. 5 MiB).
- `GET /v1/blocks/<page_id>/children?page_size=100` (paginate with
  `start_cursor`) — used to pick an anchor block id.
- `POST /v1/search` with `{"query": ..., "filter": {"property": "object",
  "value": "page"}}` — find a page id by title.

## 6. Error catalog

| code | message pattern | meaning |
|---|---|---|
| `invalid_request_url` | `Invalid request URL.` | wrong path — use `/v1/file_uploads` |
| `object_not_found` | `Make sure the relevant pages and databases are shared with your integration "..."` | page not connected to the integration (or moved out of a shared parent) |
| `validation_error` | `body.image.type should be not present` | update-block payload included `type` |
| `validation_error` | `body failed validation: body.children...` | usually a missing `object: "block"` or missing `type` on create |

Notion permission nuance: access is inherited from the parent at creation time.
Moving a page into a page the integration cannot see makes it `404` until the
new parent is shared (`...` → `Connections` → integration). This bit us when a
weekly-report page was dragged into a freshly created top-level page.

## 7. Worked case — 16 report figures into one page

- Target page: `PN 极性切换采集模式分析` (9 H2 sections).
- Figures: `f1…f16` PNGs, 34–497 KB, each 1:1 with a section.
- Anchors: `heading_2` blocks were located via `blocks`, and for each section
  the insertion anchor was *the last block before the next `heading_2`*
  (`--section-end` does this automatically).
- Result: 4 images after §4, 2 after §5, 7 after §6, 3 after §7; page went from
  65 to 81 top-level blocks, text/tables untouched.
- Script: `scripts/notion_upload.py` (`find` → `blocks` → `upload --dry-run` →
  `upload`), reusable for any workspace token in `~/.dsh/notion.tokens`.

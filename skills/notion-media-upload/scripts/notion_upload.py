#!/usr/bin/env python3
"""Attach local files (images, PDFs, ...) to Notion pages as native blocks.

Why this exists
---------------
The Notion MCP tools here only speak JSON, but Notion's file-upload API needs a
multipart body. This script calls the REST API directly (curl) to upload a local
file and insert it as a native image/file block, so the result looks exactly
like a file dragged in by hand -- no format conversion, no attachment-only block.

Commands
--------
  find <query>                 search pages by title
  blocks <page_id>             list top-level blocks (id / type / text) for anchors
  upload <page_id> <files...>  upload files and insert blocks
  trash-page <page_id>         move a page to the trash (test cleanup)
  trash-block <block_id>       move a block to the trash
  limits                       show the workspace file-upload size limit

Examples
--------
  notion_upload.py find "PN 极性"
  notion_upload.py blocks 40e5f2b7-e43a-810e-8ae8-d39aec5c2ea6
  notion_upload.py upload <page> a.png b.png --section-end "4. 定性维度" \
      --caption "图 1 · ..." --caption "图 2 · ..."
  notion_upload.py upload <page> report.pdf --after <block_id>
  notion_upload.py upload <page> a.png --replace-caption "图 6 · Venn"
"""

from __future__ import annotations

import argparse
import json
import mimetypes
import subprocess
import sys
from pathlib import Path

API = "https://api.notion.com"
API_VERSION = "2025-09-03"
DEFAULT_TOKEN_FILE = Path.home() / ".dsh/notion.tokens"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp", ".tif", ".tiff", ".svg"}


# ------------------------------------------------------------------ transport
class NotionError(SystemExit):
    pass


def load_token(label: str, token_file: Path) -> str:
    if not token_file.exists():
        raise NotionError(f"token file not found: {token_file}")
    for line in token_file.read_text().splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] == label:
            return parts[1]
    raise NotionError(f"no token labelled {label!r} in {token_file}")


class Notion:
    def __init__(self, token: str):
        self.token = token
        self.version = API_VERSION

    def _curl(self, args: list[str]) -> bytes:
        out = subprocess.run(["curl", "-s", *args], check=True, capture_output=True).stdout
        return out

    def api(self, method: str, path: str, body: dict | None = None) -> dict:
        args = [f"{API}{path}", "-X", method,
                "-H", f"Authorization: Bearer {self.token}",
                "-H", f"Notion-Version: {self.version}"]
        if body is not None:
            args += ["-H", "Content-Type: application/json", "-d", json.dumps(body)]
        data = json.loads(self._curl(args) or b"{}")
        if data.get("object") == "error":
            hint = ""
            if data.get("code") == "object_not_found":
                hint = ("\nhint: the page is not shared with this integration -- "
                        "open it in Notion, ... -> Connections -> add the integration")
            raise NotionError(f"{method} {path} -> {data.get('code')}: "
                              f"{data.get('message')}{hint}")
        return data

    # -- file upload -------------------------------------------------------
    def upload(self, path: Path) -> str:
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        created = self.api("POST", "/v1/file_uploads",
                           {"mode": "single_part", "filename": path.name,
                            "content_type": mime})
        upload_id, url = created["id"], created["upload_url"]
        sent = self._curl([url, "-X", "POST",
                           "-H", f"Authorization: Bearer {self.token}",
                           "-H", f"Notion-Version: {self.version}",
                           "-F", f"file=@{path};type={mime}"])
        data = json.loads(sent or b"{}")
        if data.get("status") != "uploaded":
            raise NotionError(f"upload failed for {path.name}: {data}")
        return upload_id

    # -- helpers -----------------------------------------------------------
    def workspace_limit(self) -> int | None:
        me = self.api("GET", "/v1/users/me")
        return (me.get("bot", {}).get("workspace_limits", {}) or {}).get(
            "max_file_upload_size_in_bytes")

    def search_pages(self, query: str) -> list[dict]:
        d = self.api("POST", "/v1/search",
                     {"query": query, "page_size": 20, "filter": {"property": "object",
                                                                  "value": "page"}})
        out = []
        for r in d.get("results", []):
            title = ""
            for v in r.get("properties", {}).values():
                if v.get("type") == "title":
                    title = "".join(x.get("plain_text", "") for x in v.get("title", []))
            out.append({"id": r["id"], "title": title,
                        "parent": r.get("parent", {}).get("page_id", "")})
        return out

    def blocks(self, page_id: str) -> list[dict]:
        items, cursor = [], None
        while True:
            q = f"/v1/blocks/{page_id}/children?page_size=100"
            if cursor:
                q += f"&start_cursor={cursor}"
            d = self.api("GET", q)
            items += d.get("results", [])
            if not d.get("has_more"):
                return items
            cursor = d.get("next_cursor")

    def insert(self, parent: str, children: list[dict], after: str | None) -> dict:
        body: dict = {"children": children}
        if after:
            body["after"] = after
        return self.api("PATCH", f"/v1/blocks/{parent}/children", body)

    def update_block_media(self, block_id: str, payload: dict) -> dict:
        # the update-block endpoint rejects the type discriminator that the
        # create-block endpoint requires; keep only the media payload keys
        kind = payload["type"]
        body = {kind: {k: v for k, v in payload[kind].items() if k != "type"}}
        return self.api("PATCH", f"/v1/blocks/{block_id}", body)


# ------------------------------------------------------------------ payloads
def plain(block: dict) -> str:
    t = block["type"]
    payload = block.get(t, {})
    rt = payload.get("rich_text") or payload.get("caption") or []
    return "".join(x.get("plain_text", "") for x in rt)


def media_block(path: Path, upload_id: str, caption: str) -> dict:
    is_image = path.suffix.lower() in IMAGE_SUFFIXES
    if is_image:
        payload = {"type": "file_upload", "file_upload": {"id": upload_id}}
        if caption:
            payload["caption"] = [{"type": "text", "text": {"content": caption}}]
        return {"object": "block", "type": "image", "image": payload}
    name = caption or path.name
    return {"object": "block", "type": "file", "file": {
        "type": "file_upload", "file_upload": {"id": upload_id},
        "name": name,
        "caption": [{"type": "text", "text": {"content": caption}}] if caption else []}}


def resolve_anchor(blocks: list[dict], after: str | None, section_end: str | None) -> str | None:
    if after:
        return after
    if not section_end:
        return None
    headings = [(i, plain(b)) for i, b in enumerate(blocks) if b["type"] == "heading_2"]
    matches = [(i, text) for i, text in headings if text.startswith(section_end)]
    if not matches:
        raise NotionError(f"section heading not found: {section_end!r}")
    if len(matches) > 1:
        raise NotionError(f"section heading is ambiguous ({len(matches)} matches): {section_end!r}")
    start = matches[0][0]
    later = [i for i, _ in headings if i > start]
    end = later[0] if later else len(blocks)
    return blocks[end - 1]["id"]


# ------------------------------------------------------------------ commands
def cmd_find(n: Notion, args) -> None:
    rows = n.search_pages(args.query)
    if not rows:
        print("no pages found (is the page shared with the integration?)")
        return
    for r in rows:
        print(f"{r['id']}  {r['title']}")


def cmd_blocks(n: Notion, args) -> None:
    blocks = n.blocks(args.page_id)
    for b in blocks:
        t = b["type"]
        print(f"{b['id']}  {t:20s}  {plain(b)[:90]}")
    print(f"\n{len(blocks)} top-level blocks")


def cmd_limits(n: Notion, args) -> None:
    limit = n.workspace_limit()
    print(f"max_file_upload_size_in_bytes: {limit} ({limit / 1024 / 1024:.1f} MiB)"
          if limit else "workspace limit unavailable")


def cmd_trash_page(n: Notion, args) -> None:
    n.api("PATCH", f"/v1/pages/{args.page_id}", {"in_trash": True})
    print(f"trashed page {args.page_id}")


def cmd_trash_block(n: Notion, args) -> None:
    n.api("PATCH", f"/v1/blocks/{args.block_id}", {"in_trash": True})
    print(f"trashed block {args.block_id}")


def cmd_upload(n: Notion, args) -> None:
    files = [Path(f).expanduser().resolve() for f in args.files]
    for f in files:
        if not f.exists():
            raise NotionError(f"file not found: {f}")

    captions = list(args.caption or [])
    if args.manifest:
        manifest = json.loads(Path(args.manifest).read_text())
        if isinstance(manifest, dict):
            captions += [manifest.get(f.name, "") for f in files]
        else:
            captions += [entry.get("caption", "") for entry in manifest]
    captions += [""] * (len(files) - len(captions))
    if not any(captions):
        captions = [f.stem for f in files]
    else:
        captions = [c or f.stem for c, f in zip(captions, files)]

    limit = n.workspace_limit()
    for f in files:
        if limit and f.stat().st_size > limit:
            raise NotionError(f"{f.name} is {f.stat().st_size} bytes > workspace limit {limit}")

    blocks = n.blocks(args.page_id)
    anchor = resolve_anchor(blocks, args.after, args.section_end)

    if args.replace_caption:
        targets = [b for b in blocks
                   if b["type"] in ("image", "file") and plain(b) == args.replace_caption]
        if not targets:
            raise NotionError(f"no image/file block with caption {args.replace_caption!r}")
        if len(targets) > 1:
            raise NotionError(f"{len(targets)} blocks match caption {args.replace_caption!r}; "
                              "refusing to guess")
        if args.dry_run:
            print(f"[dry-run] would replace block {targets[0]['id']} with {files[0].name}")
            return
        upload_id = n.upload(files[0])
        n.update_block_media(targets[0]["id"], media_block(files[0], upload_id,
                                                          args.replace_caption))
        print(f"replaced block {targets[0]['id']} with {files[0].name}")
        return

    if args.dry_run:
        where = anchor or "page end"
        for f, c in zip(files, captions):
            print(f"[dry-run] {f.name} ({f.stat().st_size/1024:.0f} KB) -> {where} | {c}")
        return

    children = []
    for f, c in zip(files, captions):
        upload_id = n.upload(f)
        children.append(media_block(f, upload_id, c))
        print(f"uploaded {f.name} -> {upload_id}")
    n.insert(args.page_id, children, anchor)
    print(f"inserted {len(children)} block(s) after {anchor or 'page end'}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workspace", default="hotmail",
                    help="token label in ~/.dsh/notion.tokens (default: hotmail)")
    ap.add_argument("--token-file", default=str(DEFAULT_TOKEN_FILE))
    # accept --workspace / --token-file after the subcommand as well
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--workspace", default=argparse.SUPPRESS)
    common.add_argument("--token-file", default=argparse.SUPPRESS)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("find", help="search pages by title", parents=[common])
    p.add_argument("query")
    p.set_defaults(func=cmd_find)

    p = sub.add_parser("blocks", help="list top-level blocks of a page", parents=[common])
    p.add_argument("page_id")
    p.set_defaults(func=cmd_blocks)

    p = sub.add_parser("limits", help="show workspace file upload limit", parents=[common])
    p.set_defaults(func=cmd_limits)

    p = sub.add_parser("trash-page", help="move a page to the trash", parents=[common])
    p.add_argument("page_id")
    p.set_defaults(func=cmd_trash_page)

    p = sub.add_parser("trash-block", help="move a block to the trash", parents=[common])
    p.add_argument("block_id")
    p.set_defaults(func=cmd_trash_block)

    p = sub.add_parser("upload", help="upload files and insert blocks", parents=[common])
    p.add_argument("page_id")
    p.add_argument("files", nargs="+")
    p.add_argument("--after", help="block id to insert after")
    p.add_argument("--section-end", help="heading text; insert at the end of that section")
    p.add_argument("--caption", action="append", help="caption (repeatable, one per file)")
    p.add_argument("--manifest", help="JSON file with captions (dict name->caption or list)")
    p.add_argument("--replace-caption", help="replace the existing block with this caption")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_upload)

    args = ap.parse_args()
    args.workspace = getattr(args, "workspace", "hotmail")
    args.token_file = getattr(args, "token_file", str(DEFAULT_TOKEN_FILE))
    token = load_token(args.workspace, Path(args.token_file).expanduser())
    n = Notion(token)
    args.func(n, args)


if __name__ == "__main__":
    main()

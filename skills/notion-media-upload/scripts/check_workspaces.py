#!/usr/bin/env python3
"""Check every Notion workspace label in the token file.

Prints, per label: bot name, workspace name, upload size limit, token file mode.
Useful after adding/rotating a token, or when a Notion MCP call hits 401/404.

Usage:
  python3 check_workspaces.py [--token-file ~/.dsh/notion.tokens]
"""

from __future__ import annotations

import argparse
import json
import os
import stat
import subprocess
from pathlib import Path

API = "https://api.notion.com"
VERSION = "2025-09-03"


def labels(path: Path) -> list[tuple[str, str]]:
    out = []
    for line in path.read_text().splitlines():
        parts = line.split()
        if len(parts) >= 2:
            out.append((parts[0], parts[1]))
    return out


def me(token: str) -> dict:
    """GET /v1/users/me via curl (urllib is unreliable on this network)."""
    out = subprocess.run(
        ["curl", "-sS", "--max-time", "30", f"{API}/v1/users/me",
         "-H", f"Authorization: Bearer {token}", "-H", f"Notion-Version: {VERSION}"],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        return {"error": f"curl failed: {out.stderr.strip()[:200]}"}
    try:
        data = json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"error": f"bad response: {out.stdout[:200]}"}
    if data.get("object") == "error":
        return {"error": f"{data.get('code')}: {data.get('message', '')[:160]}"}
    return data


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--token-file", default=str(Path.home() / ".dsh/notion.tokens"))
    args = ap.parse_args()
    path = Path(args.token_file).expanduser()

    mode = stat.S_IMODE(os.stat(path).st_mode)
    print(f"token file: {path} (mode {oct(mode)})")
    if mode & 0o077:
        print("  WARNING: token file is readable by group/others; chmod 600 it")

    rows = labels(path)
    print(f"labels: {len(rows)}\n")
    width = max((len(label) for label, _ in rows), default=8)
    for label, token in rows:
        info = me(token)
        if "error" in info:
            print(f"{label:<{width}}  ERROR  {info['error']}")
            continue
        bot = info.get("name", "?")
        limits = info.get("bot", {}).get("workspace_limits", {}) or {}
        limit = limits.get("max_file_upload_size_in_bytes")
        ws = info.get("bot", {}).get("workspace_name", "?")
        print(f"{label:<{width}}  workspace={ws}  bot={bot}  upload_limit={limit}")


if __name__ == "__main__":
    main()

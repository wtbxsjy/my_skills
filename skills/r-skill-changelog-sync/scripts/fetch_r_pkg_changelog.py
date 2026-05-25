#!/usr/bin/env python3
"""Fetch compact CRAN and changelog snapshots for one or more R packages.

This script is intentionally stdlib-only so it can run in minimal Codex
environments. It retrieves authoritative metadata from CRAN and then attempts
to discover an official NEWS source from the CRAN package page or the package
homepage.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

USER_AGENT = "Codex-R-Skill-Changelog-Sync/1.0"


def fetch_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=20) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def find_first(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)
    return clean_text(match.group(1)) if match else None


def find_links_in_row(label: str, html: str, base_url: str) -> list[dict[str, str]]:
    pattern = rf"<td>{re.escape(label)}:</td>\s*<td>(.*?)</td>"
    match = re.search(pattern, html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return []
    row = match.group(1)
    links = []
    for href, text in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', row, flags=re.DOTALL):
        links.append({"text": clean_text(text), "url": urljoin(base_url, href)})
    return links


def normalize_homepage(urls: Iterable[dict[str, str]]) -> str | None:
    for item in urls:
        url = item["url"]
        if "github.com" not in url.lower():
            return url.rstrip("/")
    for item in urls:
        return item["url"].rstrip("/")
    return None


@dataclass
class PackageSnapshot:
    package: str
    cran_url: str
    version: str | None = None
    published: str | None = None
    homepage_url: str | None = None
    news_url: str | None = None
    news_version: str | None = None
    news_release_date: str | None = None
    notable_changes: list[dict[str, str]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


class NewsHTMLParser(HTMLParser):
    def __init__(self, limit: int):
        super().__init__()
        self.limit = limit
        self.active_section = False
        self.done = False
        self.capture_h2 = False
        self.capture_h3 = False
        self.capture_h4 = False
        self.capture_release = False
        self.capture_li = False
        self.skip_depth = 0
        self.list_depth = 0
        self.buffer: list[str] = []
        self.current_heading = "General"
        self.version_heading: str | None = None
        self.release_date: str | None = None
        self.items: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.done:
            return
        attrs_dict = {key: value or "" for key, value in attrs}
        if tag == "pre":
            self.skip_depth += 1
            return
        if tag == "h2" and "pkg-version" in attrs_dict.get("class", ""):
            if self.active_section:
                self.done = True
                self.active_section = False
                return
            self.active_section = True
            self.capture_h2 = True
            self.buffer = []
            return
        if not self.active_section:
            return
        if tag == "p" and "text-muted" in attrs_dict.get("class", ""):
            self.capture_release = True
            self.buffer = []
        elif tag == "h3":
            self.capture_h3 = True
            self.buffer = []
        elif tag == "h4":
            self.capture_h4 = True
            self.buffer = []
        elif tag == "li":
            self.list_depth += 1
            if self.list_depth == 1 and len(self.items) < self.limit:
                self.capture_li = True
                self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.done:
            return
        if tag == "h2" and self.capture_h2:
            self.version_heading = self._consume_buffer()
            self.capture_h2 = False
        elif tag == "p" and self.capture_release:
            text = self._consume_buffer()
            if text.lower().startswith("cran release:"):
                self.release_date = text.split(":", 1)[1].strip()
            else:
                self.release_date = text
            self.capture_release = False
        elif tag == "h3" and self.capture_h3:
            self.current_heading = self._consume_buffer() or self.current_heading
            self.capture_h3 = False
        elif tag == "h4" and self.capture_h4:
            subheading = self._consume_buffer()
            if subheading:
                self.current_heading = subheading
            self.capture_h4 = False
        elif tag == "li":
            if self.capture_li and self.list_depth == 1:
                text = self._consume_buffer()
                if text:
                    self.items.append({"section": self.current_heading, "text": text})
                self.capture_li = False
            if self.list_depth:
                self.list_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.done or self.skip_depth:
            return
        if self.capture_h2 or self.capture_h3 or self.capture_h4 or self.capture_release or self.capture_li:
            self.buffer.append(data)

    def _consume_buffer(self) -> str:
        text = clean_text(" ".join(self.buffer))
        self.buffer = []
        return text


def parse_markdown_news(markdown: str, limit: int) -> tuple[str | None, str | None, list[dict[str, str]]]:
    lines = markdown.splitlines()
    version_heading = None
    current_heading = "General"
    items: list[dict[str, str]] = []
    release_date = None
    active = False
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if re.match(r"^##+\s+.*\d+\.\d+", line):
            if version_heading is not None:
                break
            version_heading = re.sub(r"^##+\s+", "", line).strip()
            active = True
            continue
        if not active:
            continue
        if re.match(r"^###\s+", line):
            current_heading = re.sub(r"^###\s+", "", line).strip()
            continue
        if re.match(r"^[-*]\s+", line) and len(items) < limit:
            items.append(
                {
                    "section": current_heading,
                    "text": re.sub(r"^[-*]\s+", "", line).strip(),
                }
            )
        elif "CRAN release:" in line and release_date is None:
            release_date = line.split(":", 1)[1].strip()
    return version_heading, release_date, items


def discover_news_url(package: str, homepage_url: str | None, cran_news_links: list[dict[str, str]]) -> str | None:
    for link in cran_news_links:
        if link["text"].upper() == "NEWS":
            return link["url"]
    if homepage_url:
        candidates = [
            f"{homepage_url}/news/index.html",
            f"{homepage_url}/news.html",
            f"{homepage_url}/NEWS.html",
            f"{homepage_url}/NEWS.md",
        ]
        return candidates[0]
    return None


def fetch_snapshot(package: str, limit: int) -> PackageSnapshot:
    cran_url = f"https://cran.r-project.org/web/packages/{package}/index.html"
    snapshot = PackageSnapshot(package=package, cran_url=cran_url)
    try:
        cran_html = fetch_text(cran_url)
    except (HTTPError, URLError) as exc:
        snapshot.errors.append(f"Failed to fetch CRAN page: {exc}")
        return snapshot

    snapshot.version = find_first(r"<td>Version:</td>\s*<td>(.*?)</td>", cran_html)
    snapshot.published = find_first(
        r'<meta name="citation_publication_date" content="([^"]+)"', cran_html
    ) or find_first(r"<td>Published:</td>\s*<td>(.*?)</td>", cran_html)
    homepage_links = find_links_in_row("URL", cran_html, cran_url)
    snapshot.homepage_url = normalize_homepage(homepage_links)
    news_links = find_links_in_row("Materials", cran_html, cran_url)
    snapshot.news_url = discover_news_url(package, snapshot.homepage_url, news_links)

    if not snapshot.news_url:
        return snapshot

    news_candidates = [snapshot.news_url]
    if snapshot.homepage_url:
        news_candidates.extend(
            [
                f"{snapshot.homepage_url}/news/index.html",
                f"{snapshot.homepage_url}/news.html",
                f"{snapshot.homepage_url}/NEWS.md",
            ]
        )

    attempted = []
    for news_url in news_candidates:
        if news_url in attempted:
            continue
        attempted.append(news_url)
        try:
            news_text = fetch_text(news_url)
        except (HTTPError, URLError):
            continue

        snapshot.news_url = news_url
        if "<html" in news_text.lower():
            parser = NewsHTMLParser(limit=limit)
            parser.feed(news_text)
            snapshot.news_version = parser.version_heading
            snapshot.news_release_date = parser.release_date
            snapshot.notable_changes = parser.items
        else:
            version_heading, release_date, items = parse_markdown_news(news_text, limit=limit)
            snapshot.news_version = version_heading
            snapshot.news_release_date = release_date
            snapshot.notable_changes = items

        if snapshot.notable_changes or snapshot.news_version:
            break

    if not snapshot.notable_changes and snapshot.news_url:
        snapshot.errors.append("Fetched NEWS source but could not parse notable changes.")
    return snapshot


def render_markdown(snapshots: list[PackageSnapshot]) -> str:
    blocks = []
    for snapshot in snapshots:
        lines = [
            f"## {snapshot.package}",
            f"- CRAN: {snapshot.cran_url}",
        ]
        if snapshot.version:
            lines.append(f"- Current version: {snapshot.version}")
        if snapshot.published:
            lines.append(f"- Published: {snapshot.published}")
        if snapshot.homepage_url:
            lines.append(f"- Homepage: {snapshot.homepage_url}")
        if snapshot.news_url:
            lines.append(f"- NEWS: {snapshot.news_url}")
        if snapshot.news_version:
            lines.append(f"- Latest changelog section: {snapshot.news_version}")
        if snapshot.news_release_date:
            lines.append(f"- Changelog release date: {snapshot.news_release_date}")
        if snapshot.notable_changes:
            lines.append("")
            lines.append("### Notable changes")
            for item in snapshot.notable_changes:
                lines.append(f"- {item['section']}: {item['text']}")
        if snapshot.errors:
            lines.append("")
            lines.append("### Errors")
            for error in snapshot.errors:
                lines.append(f"- {error}")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch CRAN/package changelog summaries.")
    parser.add_argument(
        "--package",
        action="append",
        required=True,
        help="R package name to fetch. Repeat for multiple packages.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of notable changelog bullets per package.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--write",
        help="Optional path to write the output to.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    snapshots = [fetch_snapshot(package, limit=args.limit) for package in args.package]

    if args.format == "json":
        output = json.dumps([asdict(snapshot) for snapshot in snapshots], indent=2, ensure_ascii=False)
    else:
        output = render_markdown(snapshots)

    if args.write:
        Path(args.write).write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())

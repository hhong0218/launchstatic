#!/usr/bin/env python3
"""Check internal links in LaunchStatic HTML files."""
from __future__ import annotations
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parent.parent
SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "#")
EXTERNAL_OK = True


def html_files() -> list[Path]:
    return sorted(ROOT.rglob("*.html"))


def extract_links(content: str) -> list[str]:
    return re.findall(r'href=["\']([^"\']+)["\']', content, re.I)


def resolve_link(base_file: Path, href: str) -> Path | None:
    if any(href.startswith(s) for s in SKIP_SCHEMES):
        return None
    if href.startswith("http://") or href.startswith("https://"):
        return None
    if href.startswith("//"):
        return None
    href = href.split("?", 1)[0].split("#", 1)[0]
    if href.startswith("/"):
        target = ROOT / href.lstrip("/")
    else:
        target = (base_file.parent / href).resolve()
    if href.endswith("/"):
        if target.is_dir():
            for name in ("index.html", "index.htm"):
                idx = target / name
                if idx.exists():
                    return idx
            return target
        for suffix in ("", ".html", "/index.html"):
            cand = Path(str(target) + suffix) if suffix else target
            if cand.exists():
                return cand
        return target
    if not target.suffix:
        html = target.with_suffix(".html")
        if html.exists():
            return html
        idx = target / "index.html"
        if idx.exists():
            return idx
    if target.suffix in (".md", ".txt") and target.exists():
        return target
    return target


def main() -> int:
    broken: list[tuple[str, str, str]] = []
    checked = 0
    for f in html_files():
        if "scripts" in f.parts:
            continue
        for href in extract_links(f.read_text(encoding="utf-8", errors="replace")):
            if any(href.startswith(s) for s in SKIP_SCHEMES):
                continue
            if href.startswith("http"):
                continue
            checked += 1
            target = resolve_link(f, href)
            if target is None:
                continue
            if not target.exists():
                broken.append((str(f.relative_to(ROOT)), href, str(target.relative_to(ROOT))))
    print(f"Checked {checked} internal links across {len(html_files())} HTML files")
    if broken:
        print(f"BROKEN: {len(broken)}")
        for src, href, tgt in broken:
            print(f"  {src} -> {href} (expected {tgt})")
        return 1
    print("All internal links OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
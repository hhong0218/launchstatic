#!/usr/bin/env python3
"""Inject GA4 scripts and cookie banner into LaunchStatic HTML pages."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"demos", "downloads", "scripts", ".git"}

COOKIE_BANNER = """  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="Cookie notice" hidden>
    <p>We use Google Analytics after you accept, plus essential Cloudflare cookies. <a href="/cookies.html">Learn more</a>.</p>
    <button type="button" id="cookie-accept" class="btn btn-primary">Accept</button>
  </div>"""

SCRIPTS_BLOCK = """  <script src="/assets/js/analytics-config.js" defer></script>
  <script src="/assets/js/analytics.js" defer></script>
  <script src="/assets/js/main.js" defer></script>"""

OLD_BANNER_PATTERNS = [
    re.compile(
        r'<div id="cookie-banner"[^>]*>.*?</div>',
        re.DOTALL | re.IGNORECASE,
    ),
    re.compile(
        r'<p>We use essential cookies via Cloudflare\. <a href="/cookies\.html">Learn more</a>\.</p>',
        re.IGNORECASE,
    ),
]

MAIN_ONLY = re.compile(r'<script src="/assets/js/main\.js" defer></script>', re.IGNORECASE)
ANALYTICS_ALREADY = re.compile(r'analytics-config\.js', re.IGNORECASE)


def should_process(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.suffix == ".html"


def patch(content: str) -> str:
    if not MAIN_ONLY.search(content) and "main.js" not in content:
        return content
    if ANALYTICS_ALREADY.search(content):
        content = MAIN_ONLY.sub(SCRIPTS_BLOCK, content)
    else:
        content = MAIN_ONLY.sub(SCRIPTS_BLOCK, content)

    for pat in OLD_BANNER_PATTERNS:
        if pat.search(content):
            content = pat.sub(COOKIE_BANNER.strip(), content, count=1)
            break
    else:
        if 'id="cookie-banner"' not in content:
            content = content.replace(SCRIPTS_BLOCK, COOKIE_BANNER + "\n" + SCRIPTS_BLOCK)

    return content


def main() -> None:
    count = 0
    for path in sorted(ROOT.rglob("*.html")):
        if not should_process(path):
            continue
        text = path.read_text(encoding="utf-8")
        updated = patch(text)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            count += 1
            print(f"  {path.relative_to(ROOT)}")
    print(f"Updated {count} files")


if __name__ == "__main__":
    main()
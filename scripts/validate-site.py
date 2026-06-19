#!/usr/bin/env python3
"""Validate LaunchStatic page counts, word counts, and HTTP status locally."""
from __future__ import annotations
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "http://127.0.0.1:8765"


def word_count_html(path: Path) -> int:
    text = re.sub(r"<script[^>]*>.*?</script>", "", path.read_text(encoding="utf-8"), flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    return len(text.split())


def collect_urls() -> list[str]:
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    return re.findall(r"<loc>([^<]+)</loc>", sm)


def main() -> int:
    urls = collect_urls()
    print(f"Sitemap URLs: {len(urls)}")
    ok = fail = 0
    for loc in urls:
        local = loc.replace("https://launchstatic.dev", BASE)
        try:
            with urllib.request.urlopen(local, timeout=5) as r:
                status = r.status
            if status == 200:
                ok += 1
            else:
                print(f"  {status} {loc}")
                fail += 1
        except Exception as e:
            print(f"  FAIL {loc}: {e}")
            fail += 1
    print(f"HTTP 200: {ok}/{len(urls)}, failures: {fail}")

    templates = list((ROOT / "templates").glob("*.html"))
    templates = [t for t in templates if t.name != "index.html"]
    for t in templates:
        wc = word_count_html(t)
        flag = "OK" if wc >= 700 else "LOW"
        print(f"  template {t.name}: {wc} words [{flag}]")
    return 0 if fail == 0 and len(urls) >= 25 else 1


if __name__ == "__main__":
    sys.exit(main())
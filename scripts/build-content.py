#!/usr/bin/env python3
"""Generate LaunchStatic content pages, hubs, and sitemap."""
from __future__ import annotations
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import ROOT, hub_page, write_article, word_count, sections_html
from content_pillar import PILLAR_ARTICLES
from content_howto import HOWTO_ARTICLES
from content_tools import ARTICLES as TOOL_ARTICLES
from content_commercial import PAGES as COMMERCIAL_PAGES
from render_commercial import write_commercial

TODAY = date.today().isoformat()


def build_articles():
    stats = []
    for article in PILLAR_ARTICLES + HOWTO_ARTICLES + TOOL_ARTICLES:
        path, wc = write_article(article)
        stats.append((str(path.relative_to(ROOT)), wc, article.get("min_words", 500)))
        print(f"  {path.name}: {wc} words")
    return stats


def build_hubs():
    guides_items = [
        {"url": a["path"], "title": a["h1"], "desc": a["meta_description"], "meta": a.get("read_time", "")}
        for a in PILLAR_ARTICLES
    ]
    howto_items = [
        {"url": a["path"], "title": a["h1"], "desc": a["meta_description"], "meta": a.get("read_time", "")}
        for a in HOWTO_ARTICLES
    ]
    (ROOT / "guides" / "index.html").write_text(
        hub_page(
            "Guides — LaunchStatic",
            "In-depth pillar guides for building, deploying, and optimizing static landing pages.",
            "/guides/",
            guides_items,
        ),
        encoding="utf-8",
    )
    (ROOT / "how-to" / "index.html").write_text(
        hub_page(
            "How-to — LaunchStatic",
            "Step-by-step tutorials for domains, forms, analytics, SEO, and deployment.",
            "/how-to/",
            howto_items,
        ),
        encoding="utf-8",
    )
    print("  guides/index.html, how-to/index.html")


def build_commercial():
    for page in COMMERCIAL_PAGES:
        dest, wc = write_commercial(page)
        print(f"  {dest.relative_to(ROOT)}: {wc} words")


def collect_urls() -> list[str]:
    urls = [f"{BASE_PATH}/"]
    static_pages = [
        "index.html", "about.html", "contact.html", "privacy.html", "terms.html",
        "disclaimer.html", "cookies.html", "licenses.html", "attributions.html",
        "pricing.html", "404.html", "en/index.html",
        "templates/index.html", "templates/saas.html", "templates/app.html",
        "templates/waitlist.html", "templates/portfolio.html", "templates/newsletter.html",
        "deploy-guides/index.html", "tools/index.html",
        "blog/index.html",
        "blog/why-static-beats-wordpress-for-saas.html",
        "blog/deploy-static-site-cloudflare-5-minutes.html",
        "blog/waitlist-page-conversion-tips.html",
        "blog/mit-license-templates-commercial-use.html",
        "blog/static-site-legal-pages-checklist.html",
        "demos/saas/index.html", "demos/app/index.html", "demos/waitlist/index.html",
        "demos/portfolio/index.html", "demos/newsletter/index.html",
        "downloads/portfolio-landing.html", "downloads/newsletter-landing.html",
        "guides/index.html", "how-to/index.html",
        "free-static-landing-kit/index.html", "pro-template-pack/index.html",
        "landing-page-audit/index.html", "done-for-you/index.html",
        "license/index.html", "refund-policy/index.html",
    ]
    for p in static_pages:
        if (ROOT / p).exists():
            urls.append(url_for(p))
    for a in PILLAR_ARTICLES + HOWTO_ARTICLES + TOOL_ARTICLES:
        urls.append(f"https://launchstatic.dev{a['path']}")
    return sorted(set(urls))


BASE_PATH = "https://launchstatic.dev"


def url_for(rel: str) -> str:
    if rel == "index.html":
        return f"{BASE_PATH}/"
    if rel.endswith("/index.html"):
        return f"{BASE_PATH}/{rel.replace('/index.html', '/')}"
    return f"{BASE_PATH}/{rel}"


def build_sitemap():
    urls = collect_urls()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        pri = "1.0" if u.endswith(".dev/") else "0.6"
        if "/guides/" in u or "/how-to/" in u:
            pri = "0.8"
        if "/templates/" in u or "pro-template" in u:
            pri = "0.7"
        lines.append(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{pri}</priority></url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  sitemap.xml: {len(urls)} URLs")


def main():
    print("Building articles...")
    stats = build_articles()
    print("Building hubs...")
    build_hubs()
    print("Building commercial pages...")
    build_commercial()
    print("Building sitemap...")
    build_sitemap()
    fails = [s for s in stats if s[1] < s[2]]
    if fails:
        print("WARN: below minimum word count:", fails)
    print("Done.")


if __name__ == "__main__":
    main()
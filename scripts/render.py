"""HTML renderer for LaunchStatic articles and hub pages."""
from __future__ import annotations
import html
import json
import re
from pathlib import Path

BASE = "https://launchstatic.dev"
ROOT = Path(__file__).resolve().parent.parent
SHELL = ROOT / "scripts" / "article-shell.html"


def word_count(text: str) -> int:
    return len(re.sub(r"<[^>]+>", " ", text).split())


def sections_html(sections: list[dict]) -> str:
    parts: list[str] = []
    for s in sections:
        t = s.get("type", "p")
        if t == "h2":
            parts.append(f"<h2>{html.escape(s['text'])}</h2>")
        elif t == "h3":
            parts.append(f"<h3>{html.escape(s['text'])}</h3>")
        elif t == "p":
            parts.append(f"<p>{s['text']}</p>")
        elif t == "ul":
            items = "".join(f"<li>{i}</li>" for i in s["items"])
            parts.append(f"<ul>{items}</ul>")
        elif t == "ol":
            items = "".join(f"<li>{i}</li>" for i in s["items"])
            parts.append(f"<ol>{items}</ol>")
        elif t == "pre":
            parts.append(f"<pre><code>{html.escape(s['code'])}</code></pre>")
        elif t == "checklist":
            items = "".join(f"<li><input type=\"checkbox\" disabled> {i}</li>" for i in s["items"])
            parts.append(f'<ul class="checklist">{items}</ul>')
        elif t == "table":
            rows = s["rows"]
            head = "".join(f"<th>{c}</th>" for c in rows[0])
            body = "".join(
                "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows[1:]
            )
            parts.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
    return "\n".join(parts)


def faq_html(faqs: list[dict]) -> str:
    blocks = []
    for f in faqs:
        blocks.append(
            f'<div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">'
            f'<h3 itemprop="name">{html.escape(f["q"])}</h3>'
            f'<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">'
            f'<p itemprop="text">{f["a"]}</p></div></div>'
        )
    return "\n".join(blocks)


def json_ld(article: dict) -> str:
    article_node = {
        "@type": "Article",
        "headline": article["h1"],
        "description": article["meta_description"],
        "author": {"@type": "Organization", "name": "LaunchStatic"},
        "publisher": {"@type": "Organization", "name": "LaunchStatic"},
        "datePublished": article.get("date", "2026-06-19"),
        "mainEntityOfPage": f"{BASE}{article['path']}",
    }
    if article.get("faqs"):
        faq_node = {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f["q"],
                    "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", f["a"])},
                }
                for f in article["faqs"]
            ],
        }
        return json.dumps(
            {"@context": "https://schema.org", "@graph": [article_node, faq_node]},
            separators=(",", ":"),
        )
    return json.dumps({"@context": "https://schema.org", **article_node}, separators=(",", ":"))


def breadcrumb(section: str, section_url: str, title: str) -> str:
    return (
        f'<nav class="breadcrumb" aria-label="Breadcrumb">'
        f'<a href="/">Home</a><span aria-hidden="true">/</span>'
        f'<a href="{section_url}">{section}</a><span aria-hidden="true">/</span>'
        f"<span>{html.escape(title)}</span></nav>"
    )


def render_article(article: dict) -> str:
    shell = SHELL.read_text(encoding="utf-8")
    body = sections_html(article["sections"])
    internal = article.get("internal_links", [])
    if internal:
        pairs = []
        for item in internal:
            if isinstance(item, dict):
                pairs.append((item["url"], item["text"]))
            else:
                pairs.append((item[0], item[1]))
        links = " ".join(f'<a href="{u}">{t}</a>' for u, t in pairs)
        body += f'<p class="text-muted mt-3"><strong>Related:</strong> {links}</p>'
    cta = article.get("cta", {})
    cta_html = (
        f'<h2>{html.escape(cta.get("title", "Next step"))}</h2>'
        f'<p>{cta.get("text", "")}</p>'
        f'<a href="{cta.get("url", "/templates/")}" class="btn btn-primary">{cta.get("button", "Browse templates")}</a>'
    )
    if cta.get("secondary_url"):
        cta_html += f' <a href="{cta["secondary_url"]}" class="btn btn-secondary">{cta.get("secondary_button", "Learn more")}</a>'
    repl = {
        "{{META_TITLE}}": article["meta_title"],
        "{{META_DESCRIPTION}}": article["meta_description"],
        "{{CANONICAL_PATH}}": article["path"],
        "{{JSON_LD}}": json_ld(article),
        "{{BREADCRUMB}}": breadcrumb(article["section"], article["section_url"], article["h1"]),
        "{{H1}}": article["h1"],
        "{{DATE}}": article.get("date_display", "June 19, 2026"),
        "{{READ_TIME}}": article.get("read_time", "8 min read"),
        "{{CATEGORY}}": article.get("category", "Guide"),
        "{{BODY}}": body,
        "{{FAQ_HTML}}": faq_html(article["faqs"]),
        "{{CTA_HTML}}": cta_html,
    }
    out = shell
    for k, v in repl.items():
        out = out.replace(k, v)
    return out


def write_article(article: dict) -> tuple[Path, int]:
    rel = article["path"].lstrip("/")
    dest = ROOT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = render_article(article)
    dest.write_text(content, encoding="utf-8")
    wc = word_count(sections_html(article["sections"]))
    return dest, wc


def hub_page(title: str, desc: str, path: str, items: list[dict]) -> str:
    cards = []
    for it in items:
        cards.append(
            f'<article class="card"><h3><a href="{it["url"]}">{html.escape(it["title"])}</a></h3>'
            f'<p>{it["desc"]}</p><p class="text-muted">{it.get("meta", "")}</p></article>'
        )
    card_html = "\n".join(cards)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{BASE}{path}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{BASE}{path}">
  <meta name="twitter:card" content="summary">
  <link rel="stylesheet" href="/assets/css/main.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="container header-inner">
    <a href="/" class="logo"><span class="logo-mark" aria-hidden="true">LS</span> LaunchStatic</a>
    <nav class="nav-desktop" aria-label="Main">
      <a href="/guides/">Guides</a><a href="/how-to/">How-to</a><a href="/templates/">Templates</a><a href="/tools/">Tools</a>
      <a href="/contact.html" class="nav-cta">Contact</a>
    </nav>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav">Menu</button>
    <nav id="mobile-nav" class="nav-mobile" aria-label="Mobile"><a href="/guides/">Guides</a><a href="/how-to/">How-to</a><a href="/templates/">Templates</a></nav>
  </div></header>
  <main id="main" class="section"><div class="container">
    <h1>{html.escape(title.split("—")[0].strip())}</h1>
    <p class="section-lead">{html.escape(desc)}</p>
    <div class="grid grid-2 mt-4">{card_html}</div>
  </div></main>
  <footer class="site-footer"><div class="container footer-bottom"><span>© <span id="year"></span> LaunchStatic</span>
    <span><a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a></span></div></footer>
  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="Cookie notice" hidden>
    <p>We use Google Analytics after you accept, plus essential Cloudflare cookies. <a href="/cookies.html">Learn more</a>.</p>
    <button type="button" id="cookie-accept" class="btn btn-primary">Accept</button></div>
  <script src="/assets/js/analytics-config.js" defer></script>
  <script src="/assets/js/analytics.js" defer></script>
  <script src="/assets/js/main.js" defer></script>
</body>
</html>"""
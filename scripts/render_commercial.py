"""HTML renderer for LaunchStatic commercial and legal landing pages."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from render import BASE, ROOT, sections_html, word_count

NEWSLETTER_ENDPOINT = "YOUR_FORM_ID"


def canonical_path(path: str) -> str:
    """Normalize index.html paths to trailing-slash URLs for canonical tags."""
    if path.endswith("/index.html"):
        return path[: -len("index.html")]
    return path


def site_header(active: str | None = None) -> str:
    links = [
        ("templates", "/templates/", "Templates"),
        ("pricing", "/pricing.html", "Pricing"),
        ("deploy", "/deploy-guides/", "Deploy"),
        ("tools", "/tools/", "Tools"),
        ("blog", "/blog/", "Blog"),
    ]
    desktop = []
    for key, href, label in links:
        cls = ' class="active"' if active == key else ""
        desktop.append(f'<a href="{href}"{cls}>{label}</a>')
    desktop.append('<a href="/contact.html" class="nav-cta">Contact</a>')
    mobile = [f'<a href="{href}">{label}</a>' for _, href, label in links]
    mobile.append('<a href="/contact.html">Contact</a>')
    return f"""  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo" aria-label="LaunchStatic home">
        <span class="logo-mark" aria-hidden="true">LS</span>
        LaunchStatic
      </a>
      <nav class="nav-desktop" aria-label="Main navigation">
        {"".join(desktop)}
      </nav>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav">Menu</button>
      <nav id="mobile-nav" class="nav-mobile" aria-label="Mobile navigation">
        {"".join(mobile)}
      </nav>
    </div>
  </header>"""


def site_footer() -> str:
    return """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/" class="logo"><span class="logo-mark" aria-hidden="true">LS</span> LaunchStatic</a>
          <p>Static landing page templates and deployment guides for indie hackers, no-code builders, and solo founders.</p>
        </div>
        <div class="footer-col">
          <h4>Product</h4>
          <ul>
            <li><a href="/templates/">Templates</a></li>
            <li><a href="/deploy-guides/">Deploy Guides</a></li>
            <li><a href="/tools/">Tools</a></li>
            <li><a href="/blog/">Blog</a></li>
            <li><a href="/free-static-landing-kit/">Free Kit</a></li>
            <li><a href="/pro-template-pack/">Pro Pack</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="/landing-page-audit/">Page Audit</a></li>
            <li><a href="/done-for-you/">Done-for-you</a></li>
            <li><a href="/pricing.html">Pricing</a></li>
            <li><a href="/contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Legal</h4>
          <ul>
            <li><a href="/license/">License</a></li>
            <li><a href="/refund-policy/">Refund Policy</a></li>
            <li><a href="/privacy.html">Privacy Policy</a></li>
            <li><a href="/terms.html">Terms of Service</a></li>
            <li><a href="/disclaimer.html">Disclaimer</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year"></span> LaunchStatic. All rights reserved.</span>
        <span>Static HTML · Cloudflare Pages ready</span>
      </div>
    </div>
  </footer>"""


def cookie_banner() -> str:
    return """  <div id="cookie-banner" class="cookie-banner" role="dialog" aria-label="Cookie notice" hidden>
    <p>We use essential cookies via Cloudflare. <a href="/cookies.html">Learn more</a>.</p>
    <button type="button" id="cookie-accept" class="btn btn-primary">OK</button>
  </div>"""


def newsletter_form(form_id: str = "page-newsletter") -> str:
    return f"""        <form data-newsletter data-endpoint="{NEWSLETTER_ENDPOINT}" class="card mt-4" aria-label="Email updates">
          <h3>Get launch tips by email</h3>
          <p class="text-muted">Occasional notes on static sites and template updates. No spam, unsubscribe anytime.</p>
          <div class="form-group mt-2">
            <label for="{form_id}">Email</label>
            <input type="email" id="{form_id}" name="email" required autocomplete="email" placeholder="you@example.com">
          </div>
          <button type="submit" class="btn btn-primary">Subscribe</button>
          <p class="newsletter-ok text-muted mt-2" hidden>Thanks — you're on the list.</p>
        </form>"""


def contact_cta_block(title: str = "Questions?") -> str:
    return f"""        <section class="card mt-4" aria-label="Contact">
          <h3>{html.escape(title)}</h3>
          <p>Email <a href="mailto:hello@launchstatic.dev">hello@launchstatic.dev</a> — we reply within two business days. For purchase support, include your order email and product name.</p>
          <a href="/contact.html" class="btn btn-secondary mt-2">Contact page</a>
        </section>"""


def highlights_html(highlights: list[dict]) -> str:
    cards = []
    for h in highlights:
        badge = ""
        if h.get("badge"):
            badge = f'<span class="badge-free">{html.escape(h["badge"])}</span> '
        cards.append(
            f'<article class="card">{badge}<h3 class="mt-2">{html.escape(h["title"])}</h3>'
            f'<p>{h.get("text", "")}</p></article>'
        )
    return f'<div class="grid grid-3 mt-3">{"".join(cards)}</div>'


def price_hero(page: dict) -> str:
    badge = page.get("badge")
    badge_html = f'<p class="hero-badge"><span>{html.escape(badge)}</span></p>' if badge else ""
    price = page.get("price_display")
    period = page.get("price_period", "")
    price_html = ""
    if price:
        period_bit = f' <span style="font-size:1rem;color:var(--muted)">{html.escape(period)}</span>' if period else ""
        price_html = f'<p class="price" style="font-size:2rem;font-weight:800;margin:1rem 0">{html.escape(price)}{period_bit}</p>'
    return f"""    <section class="hero section-sm">
      <div class="container text-center">
        {badge_html}
        <h1>{html.escape(page["h1"])}</h1>
        {price_html}
        <p class="section-lead" style="margin-inline:auto">{page.get("hero_lead", "")}</p>
      </div>
    </section>"""


def primary_cta_html(cta: dict | None) -> str:
    if not cta:
        return ""
    parts = [
        f'<a href="{cta.get("url", "/contact.html")}" class="btn btn-primary">{html.escape(cta.get("button", "Get started"))}</a>'
    ]
    if cta.get("secondary_url"):
        parts.append(
            f'<a href="{cta["secondary_url"]}" class="btn btn-secondary">{html.escape(cta.get("secondary_button", "Learn more"))}</a>'
        )
    return f'<div class="hero-actions mt-3">{"".join(parts)}</div>'


def json_ld_webpage(page: dict) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page["h1"],
        "description": page["meta_description"],
        "url": f"{BASE}{canonical_path(page['path'])}",
        "publisher": {"@type": "Organization", "name": "LaunchStatic"},
    }
    if page.get("price_display"):
        offer = {
            "@type": "Offer",
            "price": re.sub(r"[^\d.]", "", page["price_display"]) or "0",
            "priceCurrency": "USD",
        }
        if page.get("price_period"):
            offer["description"] = page["price_period"]
        data["offers"] = offer
    return json.dumps(data, separators=(",", ":"))


def render_commercial(page: dict) -> str:
    """Render a full commercial/legal HTML page from a page dict."""
    path = page["path"]
    canon = canonical_path(path)
    body = sections_html(page["sections"])
    highlights = highlights_html(page["highlights"]) if page.get("highlights") else ""
    cta_block = primary_cta_html(page.get("primary_cta"))
    extras = []
    if page.get("show_newsletter", True):
        slug = re.sub(r"[^a-z0-9]+", "-", path.lower()).strip("-")[:40]
        extras.append(newsletter_form(f"newsletter-{slug}"))
    if page.get("show_contact", True):
        extras.append(contact_cta_block(page.get("contact_title", "Questions?")))
    extras_html = "\n".join(extras)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(page["meta_title"])}</title>
  <meta name="description" content="{html.escape(page["meta_description"])}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{BASE}{html.escape(canon)}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{html.escape(page["meta_title"])}">
  <meta property="og:description" content="{html.escape(page["meta_description"])}">
  <meta property="og:url" content="{BASE}{html.escape(canon)}">
  <meta property="og:site_name" content="LaunchStatic">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{html.escape(page["meta_title"])}">
  <meta name="twitter:description" content="{html.escape(page["meta_description"])}">
  <link rel="stylesheet" href="/assets/css/main.css">
  <script type="application/ld+json">{json_ld_webpage(page)}</script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
{site_header(page.get("nav_active"))}
  <main id="main">
{price_hero(page)}
    <section class="section">
      <div class="container prose">
        {body}
        {highlights}
        {cta_block}
        {extras_html}
      </div>
    </section>
  </main>
{site_footer()}
{cookie_banner()}
  <script src="/assets/js/main.js" defer></script>
</body>
</html>"""


def write_commercial(page: dict) -> tuple[Path, int]:
    rel = page["path"].lstrip("/")
    dest = ROOT / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = render_commercial(page)
    dest.write_text(content, encoding="utf-8")
    wc = word_count(sections_html(page["sections"]))
    return dest, wc


def write_all(pages: list[dict]) -> list[tuple[str, int]]:
    results = []
    for p in pages:
        dest, wc = write_commercial(p)
        results.append((str(dest), wc))
    return results
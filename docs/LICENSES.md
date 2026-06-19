# LaunchStatic — License Inventory

Last audited: June 2026

This document lists every licensable component in the LaunchStatic repository and whether it may be used commercially.

## Summary

| Category | Count | Commercial use | Notes |
|----------|-------|----------------|-------|
| Site HTML/CSS/JS | 1 bundle | Yes | © LaunchStatic; templates MIT |
| Downloadable templates | 3 files | Yes | MIT License |
| Demo landing pages | 3 sites | Yes | MIT License |
| Fonts | 0 external | Yes | System UI stack only |
| Images | 0 raster | Yes | CSS gradients and markup only |
| Icons | Unicode text | Yes | No icon font libraries |
| Third-party logos | 0 | N/A | Text references only; no SVG/PNG logos |

---

## 1. LaunchStatic marketing site

| Asset | Path | License | Commercial | Attribution required |
|-------|------|---------|------------|----------------------|
| Main stylesheet | `assets/css/main.css` | Proprietary (site) | View/use for reference only; do not resell as template pack | No |
| Main script | `assets/js/main.js` | Proprietary (site) | Same as above | No |
| Site copy & blog articles | `*.html`, `blog/` | © LaunchStatic | Readable on site; not licensed for redistribution | N/A |
| Logo mark "LS" | CSS gradient box | Original work | LaunchStatic trademark | N/A |

**Blog and guide text:** Original content written for LaunchStatic. Not MIT-licensed. AI-assisted drafting was used; see `docs/ATTRIBUTIONS.md` and `/disclaimer.html`.

---

## 2. Free templates (MIT License)

| Template | Paths | License file |
|----------|-------|--------------|
| SaaS Landing (Flowboard demo) | `demos/saas/`, `downloads/saas-landing.html` | `docs/MIT-LICENSE.txt` |
| App Landing (PocketHabit demo) | `demos/app/`, `downloads/app-landing.html` | `docs/MIT-LICENSE.txt` |
| Waitlist (MetricJar demo) | `demos/waitlist/`, `downloads/waitlist-landing.html` | `docs/MIT-LICENSE.txt` |
| Portfolio (Casey Dev demo) | `demos/portfolio/`, `downloads/portfolio-landing.html` | `docs/MIT-LICENSE.txt` |
| Newsletter (Draft & Ship demo) | `demos/newsletter/`, `downloads/newsletter-landing.html` | `docs/MIT-LICENSE.txt` |

**Permitted:** Use, modify, deploy commercially, sublicense, sell products built with these templates.

**Required:** Include MIT copyright notice in copies or substantial portions.

**Prohibited:** Claiming you authored the original template source code without license notice; reselling unmodified templates as your own template marketplace product (see Terms § Paid materials).

---

## 3. Fonts

| Font stack | Source | License |
|------------|--------|---------|
| `system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, sans-serif` | OS bundled | System font license — commercial OK |
| `ui-monospace, Cascadia Code, Segoe UI Mono, Consolas, monospace` | OS bundled | System font license — commercial OK |

No Google Fonts, Adobe Fonts, or CDN font loading.

---

## 4. Icons and decorative characters

| Usage | Location | License |
|-------|----------|---------|
| Unicode symbols (⚡ 🔓 📱 → ✓ 🔥) | `index.html`, demos | Unicode — no restriction |
| CSS-only phone mockup | `demos/app/` | Original — MIT with template |

No Font Awesome, Heroicons, or third-party icon packs.

---

## 5. Images and media

| Type | Status |
|------|--------|
| PNG/JPG/WebP/SVG photos | **None used** |
| Stock photography | **None** |
| Lottie/video | **None** |
| Favicon | **Not yet added** — when added, must be original or licensed |

---

## 6. Third-party brand references (text only)

| Brand | Usage | Logo used? |
|-------|-------|------------|
| Cloudflare, GitHub, Netlify, Formspree, etc. | Text links in guides/tools | **No** |
| App Store / Google Play | Plain text buttons in app demo | **No official badges** |
| Google AdSense | Described in Privacy/Cookie policy | **Not integrated yet** |

---

## 7. Paid template packs (future)

Paid materials will ship under a separate **LaunchStatic Commercial Template License** with:

- Single-project or multi-project use tiers
- No redistribution or resale of source files
- Clear file headers in each paid HTML/CSS/JS asset

Until paid packs launch, everything in `downloads/` and `demos/` remains MIT.

---

## 8. Removed or rejected assets

| Item | Reason |
|------|--------|
| GitHub repo template copy-paste (awesome-landing-pages, html5up, etc.) | Not used — originals written to avoid unclear/commercial-restricted terms |
| Fake Formspree form ID | Removed — replaced with `YOUR_FORM_ID` placeholder |
| Third-party logos (Google, Cloudflare, PH, IH) | Never added |
| External CDN CSS/JS | Never used |

---

## Contact

License questions: [hello@launchstatic.dev](mailto:hello@launchstatic.dev)  
DMCA / copyright: [dmca@launchstatic.dev](mailto:dmca@launchstatic.dev)
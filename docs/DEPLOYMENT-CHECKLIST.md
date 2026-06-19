# LaunchStatic Pre-Deploy Checklist

Use this checklist before pointing a custom domain at production or announcing a launch. Work top to bottom; check each item on desktop and mobile.

**Site:** launchstatic.dev  
**Host:** Cloudflare Pages (static output, no build command)

---

## 1. Links and navigation

- [ ] Every internal link resolves (no 404s): header nav, footer, CTAs, breadcrumbs
- [ ] Template pages link to correct demos and download files
- [ ] External links open in a new tab where appropriate (`target="_blank"` + `rel="noopener noreferrer"`)
- [ ] Logo and "Home" links point to `/`
- [ ] Legal footer links work: Privacy, Terms, Disclaimer, About, Contact
- [ ] Mobile menu opens, closes, and all items are tappable

## 2. Mobile and responsive

- [ ] Test on a real phone (iOS and Android if possible)
- [ ] No horizontal scroll at 320px–428px widths
- [ ] Hero text readable without zooming
- [ ] Buttons and form fields are at least 44×44px touch targets
- [ ] Sticky header does not obscure focused content or skip link
- [ ] Tables and code blocks scroll horizontally inside containers, not the page

## 3. Lighthouse and performance

- [ ] Run Lighthouse in Chrome DevTools (Incognito): **Performance ≥ 90**
- [ ] Run Lighthouse **Accessibility ≥ 90**
- [ ] Run Lighthouse **Best Practices ≥ 90**
- [ ] Run Lighthouse **SEO ≥ 90**
- [ ] Confirm no render-blocking resources beyond essential CSS/JS
- [ ] Images use appropriate dimensions and formats (WebP/AVIF where used)
- [ ] `main.css` and `main.js` load from `/assets/` with correct cache headers (Cloudflare default is fine)

## 4. Legal & commercial safety (LS-002)

- [ ] `docs/LICENSES.md` and `docs/ATTRIBUTIONS.md` reviewed
- [ ] `/licenses.html`, `/attributions.html`, `/cookies.html` live
- [ ] Privacy Policy covers cookies, ads, logs, retention, international transfers
- [ ] Terms distinguish free MIT vs paid commercial license
- [ ] Contact lists `hello@launchstatic.dev` and `dmca@launchstatic.dev`
- [ ] No third-party logos embedded; no fake Formspree IDs
- [ ] `docs/ADSENSE-POLICY-CHECKLIST.md` reviewed before AdSense application

## 5. SEO files

- [ ] `sitemap.xml` lists all public URLs with `https://launchstatic.dev` canonical paths
- [ ] `robots.txt` allows crawling and references the sitemap URL
- [ ] Submit sitemap in Google Search Console and Bing Webmaster Tools after deploy

## 5. 404 page

- [ ] `404.html` exists at project root (Cloudflare Pages serves it for missing routes)
- [ ] 404 page uses same header/footer and links back to home and templates
- [ ] Trigger a bad URL in preview and confirm custom 404 appears (not generic host error)

## 6. Meta tags (every HTML page)

- [ ] Unique `<title>` per page (50–60 characters, descriptive)
- [ ] Unique `<meta name="description">` per page (140–160 characters)
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- [ ] `<link rel="canonical" href="https://launchstatic.dev/...">` matches production URL
- [ ] `<html lang="en">` set on all pages
- [ ] Open Graph / Twitter cards added if you use social sharing (optional but recommended)

## 7. Forms

- [ ] Contact form `mailto:` action opens the correct address (`hello@launchstatic.dev`)
- [ ] Required fields validated in HTML (`required`, `type="email"`)
- [ ] Waitlist template docs note Formspree/Netlify setup if demo forms are placeholders
- [ ] Test submit on desktop and mobile mail clients
- [ ] Privacy policy linked near any email collection UI

## 8. Custom domain and DNS

- [ ] Domain added in Cloudflare Pages → **Custom domains**
- [ ] DNS records set per Cloudflare instructions (CNAME or flattened A/AAAA)
- [ ] `www` redirects to apex (or apex to `www`) — pick one canonical host
- [ ] SSL/TLS certificate status: **Active**
- [ ] HTTPS enforced; no mixed-content warnings in browser console
- [ ] Canonical URLs and sitemap use the chosen primary domain

## 9. Cloudflare Pages settings

- [ ] **Production branch:** `main` (or your release branch)
- [ ] **Build command:** empty / none
- [ ] **Build output directory:** `/` (repository root)
- [ ] **Environment variables:** none required for static site (document any if added)
- [ ] Preview deployments enabled for PRs (optional)
- [ ] **Caching:** default static asset caching acceptable; purge cache after major CSS/JS changes
- [ ] **Security headers** (optional via `_headers` file): `X-Frame-Options`, `Referrer-Policy`, etc.

## 10. Final smoke test

- [ ] Open site in Chrome, Firefox, and Safari
- [ ] Verify `#year` footer script runs (`/assets/js/main.js`)
- [ ] Download each template ZIP/HTML from `/downloads/` paths
- [ ] Demo iframes or `/demos/*` pages load without console errors
- [ ] Archive a Lighthouse report PDF or screenshot for the release

---

## Quick reference

| File            | Production URL                                      |
|-----------------|-----------------------------------------------------|
| Sitemap         | `https://launchstatic.dev/sitemap.xml`              |
| Robots          | `https://launchstatic.dev/robots.txt`               |
| Privacy         | `https://launchstatic.dev/privacy.html`             |
| Terms           | `https://launchstatic.dev/terms.html`               |
| Disclaimer      | `https://launchstatic.dev/disclaimer.html`          |

**Contact:** hello@launchstatic.dev
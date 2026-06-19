# Google Search Console Submission Checklist — LaunchStatic

## Prerequisites
- [ ] Site deployed to Cloudflare Pages with public HTTPS URL
- [ ] Custom domain `launchstatic.dev` connected (apex preferred)
- [ ] `robots.txt` allows crawling (`Allow: /`)
- [ ] `sitemap.xml` lists all indexable URLs (55+ pages)
- [ ] No `noindex` on primary content pages

## Domain verification
1. Open [Google Search Console](https://search.google.com/search-console)
2. Add property: **URL prefix** `https://launchstatic.dev/` or **Domain** `launchstatic.dev`
3. Verify via DNS TXT record in Cloudflare (recommended for domain property)
4. Confirm HTTPS certificate is valid (Cloudflare Universal SSL)

## Sitemap submission
1. GSC → Sitemaps → Add `https://launchstatic.dev/sitemap.xml`
2. Wait 24–48 hours; check "Discovered pages" count
3. Fix any "Couldn't fetch" errors (usually DNS or 404 on sitemap path)

## URL inspection (priority pages)
Inspect and request indexing for:
- `/` (home)
- `/guides/static-landing-page-playbook.html`
- `/templates/saas.html`
- `/free-static-landing-kit/`
- `/about.html`, `/contact.html`, `/privacy.html`

## Canonical policy
- **Preferred host:** apex `https://launchstatic.dev` (no www)
- Configure Cloudflare redirect: `www.launchstatic.dev` → `https://launchstatic.dev` (301)
- Every page has `<link rel="canonical">` matching apex URL

## Post-submission monitoring (weekly)
- Coverage report: zero "Excluded by noindex" on content pages
- Core Web Vitals: mobile LCP under 2.5s
- Manual actions: none
- Indexed pages trend upward after content publish

## Common blockers
| Issue | Fix |
|-------|-----|
| Sitemap 404 | Ensure `sitemap.xml` at repo root, not in `/docs/` |
| Redirect chain | Single hop www → apex |
| Soft 404 | Ensure real content on all sitemap URLs |
| Crawled, not indexed | Improve internal links; add unique titles/descriptions |
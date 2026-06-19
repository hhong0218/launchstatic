# AdSense Pre-Application Checklist — LaunchStatic

**Target application date:** ~2 weeks after launch (allow indexing time)

## Content requirements
- [x] 25+ indexable HTML pages with unique titles and meta descriptions
- [x] 5 pillar guides (1,500+ words each)
- [x] 10 how-to articles (900+ words each)
- [x] 5 template detail pages (700+ words each)
- [x] 3 tool guides (500+ words each)
- [x] About, Contact, Privacy, Terms, Disclaimer complete
- [x] No thin pages under 300 words
- [x] No lorem ipsum or "coming soon" placeholders

## Policy compliance
- [x] No "AdSense approval guaranteed" language
- [x] No "click our ads" or support-by-clicking copy
- [x] No fake reviews, user counts, or client logos
- [x] No adult, gambling, weapons, or medical misinformation content
- [x] No misleading affiliation with Google, Cloudflare, or Product Hunt
- [x] Copyright-clear assets (MIT templates, no scraped images)
- [x] Privacy policy covers analytics and contact forms

## Technical requirements
- [x] Live HTTPS deployment (https://launchstatic.pages.dev)
- [ ] Custom domain launchstatic.dev connected
- [x] `robots.txt` allows Googlebot
- [x] `sitemap.xml` submitted to Search Console
- [ ] 0 broken internal links (run `scripts/check-links.py`)
- [x] Cookie notice banner (essential cookies disclosure)
- [ ] Lighthouse SEO ≥ 90 on home and article sample
- [x] No AdSense script until approved (placeholder policy only)

## Trust signals
- [x] Operator email: hello@launchstatic.dev
- [x] DMCA contact: dmca@launchstatic.dev
- [x] License and refund pages for paid products
- [x] Footer links to legal pages on every template

## Pre-submit actions
1. Deploy to production URL
2. Run link checker — fix all broken hrefs
3. Submit sitemap in GSC; wait for 20+ indexed pages
4. Review `docs/AD-PLACEMENT-PLAN.md` — do not pre-load ad slots
5. Apply at [Google AdSense](https://www.google.com/adsense/) with production URL

## Rejection risk assessment
| Risk | Level | Mitigation |
|------|-------|------------|
| Low value content | Low | 25+ original guides with checklists |
| Insufficient content | Low | 15,000+ words in pillar/how-to alone |
| Navigation issues | Low | Hub pages, breadcrumbs, internal links |
| Policy violations | Low | Checklist audited June 2026 |
| Site not reachable | Medium | Requires live CF Pages deploy |
| Low traffic / not indexed | Medium | Allow 2 weeks GSC indexing |

**Verdict:** PASS on content/policy; pending production deploy + indexing.
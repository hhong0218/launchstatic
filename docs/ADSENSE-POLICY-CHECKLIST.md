# AdSense Policy Risk Checklist — LaunchStatic

Use before applying to Google AdSense. This checklist does **not** guarantee approval.

## Content quality

- [x] Original articles (not scraped Reddit/X posts)
- [x] No lorem ipsum or empty placeholder pages
- [x] Clear site purpose (static templates for indie hackers)
- [x] About page with operator contact
- [ ] 10+ substantive blog posts (target for LS-005 — currently 5)
- [x] Privacy Policy published
- [x] Terms of Service published
- [x] Disclaimer published
- [x] Cookie Notice published

## Prohibited / risky content

- [x] No "guaranteed AdSense approval" claims
- [x] No "legally perfect document" claims
- [x] No counterfeit / misleading product claims
- [x] No fake testimonials or customer logos
- [x] No unauthorized third-party logos
- [x] Demo metrics clearly fictional
- [x] No adult, gambling, or restricted vertical content

## Technical / UX

- [x] Mobile responsive layout
- [x] Working navigation on all pages
- [x] `robots.txt` allows crawling
- [x] `sitemap.xml` present
- [x] Custom 404 page
- [x] HTTPS (required at production on Cloudflare)
- [ ] Custom domain live (launchstatic.dev)
- [ ] Lighthouse Performance ≥ 90 (verify post-deploy)

## Privacy & cookies (required before enabling ads)

- [x] Privacy Policy covers cookies, ads, analytics
- [x] Cookie Notice explains AdSense/third-party ad cookies (future-ready)
- [x] Instructions for user opt-out / cookie controls
- [ ] Consent banner implemented **when** AdSense script is added
- [x] Contact email for privacy requests

## Copyright

- [x] LICENSES.md inventory complete
- [x] ATTRIBUTIONS.md complete
- [x] MIT license on free templates
- [x] No unclear GitHub repo code paste
- [x] DMCA contact published

## Monetization clarity

- [x] Free vs paid templates clearly labeled
- [ ] Paid pack checkout page live (LS-004 — pricing page added, checkout TBD)
- [x] No deceptive "free" labeling on paid items

## Pre-application recommendation

1. Deploy to production domain and run 2–4 weeks with analytics (Umami/Plausible).
2. Publish 5+ additional blog posts.
3. Add Consent Management Platform or minimal cookie banner when inserting AdSense code.
4. Re-run Lighthouse and fix regressions.

**Estimated readiness score: 72/100** (see LS-002 final report)
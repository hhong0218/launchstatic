# Custom Domain Guide — LaunchStatic on Cloudflare Pages

## Recommended policy
- **Canonical host:** `https://launchstatic.dev` (apex, no www)
- **Redirect:** `www.launchstatic.dev` → apex (301, Cloudflare Bulk Redirect or Page Rule)

## Step 1 — Add domain in Cloudflare Pages
1. Cloudflare Dashboard → Workers & Pages → launchstatic project
2. Custom domains → Set up a custom domain
3. Enter `launchstatic.dev` and `www.launchstatic.dev`
4. Cloudflare creates required DNS records if zone is on Cloudflare

## Step 2 — DNS records (external registrar)
If DNS is outside Cloudflare:
| Type | Name | Value |
|------|------|-------|
| CNAME | www | launchstatic.pages.dev |
| A | @ | 192.0.2.0 (or CF Pages apex setup per dashboard) |

Prefer transferring DNS to Cloudflare for automatic SSL and apex support.

## Step 3 — HTTPS
- Universal SSL: enabled by default
- SSL mode: **Full (strict)**
- Always Use HTTPS: ON
- Minimum TLS: 1.2

## Step 4 — Update site references
- Canonical URLs already use `https://launchstatic.dev`
- Regenerate sitemap after domain goes live
- Update GSC property to production domain

## Step 5 — Verify
```bash
curl -I https://launchstatic.dev/
curl -I https://www.launchstatic.dev/   # should 301 to apex
curl https://launchstatic.dev/sitemap.xml
curl https://launchstatic.dev/robots.txt
```

## Troubleshooting
- **SSL pending:** Wait up to 24h; check DNS propagation
- **Redirect loop:** Set SSL to Full strict; avoid flexible mode
- **404 on apex:** Confirm custom domain attached to correct Pages project
# LaunchStatic

Static landing page templates and deployment guides for indie hackers. HTML, CSS, and vanilla JavaScript — no build step required.

## Live site

- **Production:** https://launchstatic.pages.dev
- **GitHub:** https://github.com/hhong0218/launchstatic
- **Custom domain (planned):** https://launchstatic.dev — add in Cloudflare Pages → Custom domains when the zone is on Cloudflare

## Deploy to Cloudflare Pages

**Direct deploy (current):**

```bash
npx wrangler pages deploy . --project-name=launchstatic --branch=main
```

**Git-connected deploy (optional):**

1. Cloudflare Dashboard → Workers & Pages → launchstatic → Settings → Connect to Git
2. Select `hhong0218/launchstatic`. **Build command:** empty. **Output directory:** `/`
3. Future pushes to `main` auto-deploy.

See `docs/CUSTOM-DOMAIN-GUIDE.md` for apex domain and www redirect.

## Local preview

```bash
python -m http.server 8080 --directory .
```

Open `http://localhost:8080`.

## Structure

- `index.html` — marketing site home
- `templates/` — template catalog and detail pages
- `demos/` — live template previews
- `downloads/` — single-file HTML downloads
- `deploy-guides/` — Cloudflare Pages walkthrough
- `docs/DEPLOYMENT-CHECKLIST.md` — pre-launch QA

## License

Site content © LaunchStatic. Template files in `downloads/` and `demos/` are MIT licensed — see `docs/MIT-LICENSE.txt`.
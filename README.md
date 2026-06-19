# LaunchStatic

Static landing page templates and deployment guides for indie hackers. HTML, CSS, and vanilla JavaScript — no build step required.

## Deploy to Cloudflare Pages

1. Push this folder to a GitHub repository.
2. In Cloudflare Dashboard → Workers & Pages → Create → Connect to Git.
3. Select the repo. Set **Build command** to empty and **Build output directory** to `/`.
4. Deploy. Your site is live at `*.pages.dev`.
5. Add a custom domain under Pages → Custom domains.

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

Site content © LaunchStatic. Template files in `downloads/` and `demos/` are MIT licensed — see `LICENSE`.
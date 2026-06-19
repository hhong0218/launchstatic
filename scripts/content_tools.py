"""Tool guide articles for LaunchStatic /tools/ section."""
from __future__ import annotations

ARTICLES: list[dict] = [
    {
        "path": "/tools/cloudflare-pages.html",
        "meta_title": "Cloudflare Pages Guide for Static Sites — LaunchStatic",
        "meta_description": "Deploy static HTML to Cloudflare Pages with Git integration, free SSL, global CDN, and custom domains. Step-by-step setup for indie hackers.",
        "h1": "Cloudflare Pages for Static Sites",
        "section": "Tools",
        "section_url": "/tools/",
        "category": "Tool Guide",
        "date": "2026-06-19",
        "date_display": "June 19, 2026",
        "read_time": "9 min read",
        "sections": [
            {
                "type": "p",
                "text": (
                    "Cloudflare Pages is the default hosting recommendation on LaunchStatic because it "
                    "solves the three problems indie hackers care about most: cost, speed, and simplicity. "
                    "You push HTML files to a Git repository, connect that repo to Cloudflare, and your "
                    "site is served from hundreds of edge locations worldwide with automatic HTTPS. There "
                    "is no build step required for plain static sites, no bandwidth cap on the free tier, "
                    "and no credit card needed to get started."
                ),
            },
            {
                "type": "h2",
                "text": "Why Cloudflare Pages beats generic static hosts",
            },
            {
                "type": "p",
                "text": (
                    "Many static hosts work fine for a single landing page, but Cloudflare Pages combines "
                    "hosting with the same CDN infrastructure that protects large enterprises. That means "
                    "your waitlist page loads quickly in Tokyo, Berlin, and São Paulo without you "
                    "configuring regional servers. Preview deployments are generated for every Git branch "
                    "and pull request, which is invaluable when you want a client or cofounder to review "
                    "copy changes before merging to production."
                ),
            },
            {
                "type": "p",
                "text": (
                    "Unlike some competitors, Cloudflare does not throttle free projects after a traffic "
                    "spike. A Product Hunt launch or a viral tweet will not trigger a surprise invoice. "
                    "For pre-revenue founders, predictable $0 hosting removes one more reason to delay "
                    "shipping. You still own your files — if you outgrow Pages or want a different "
                    "workflow, download your repo and move elsewhere."
                ),
            },
            {
                "type": "h2",
                "text": "What you need before connecting",
            },
            {
                "type": "ul",
                "items": [
                    "A GitHub, GitLab, or Bitbucket account with your site files in a repository",
                    "An <code>index.html</code> at the repository root (not buried in a subfolder)",
                    "Root-relative asset paths like <code>/assets/css/main.css</code>",
                    "A free Cloudflare account at dash.cloudflare.com",
                ],
            },
            {
                "type": "p",
                "text": (
                    "LaunchStatic templates are structured exactly for this layout. Download a template, "
                    "customize copy locally, initialize Git, push to GitHub, and you are one dashboard "
                    "wizard away from a live URL ending in <code>*.pages.dev</code>."
                ),
            },
            {
                "type": "h2",
                "text": "Create a Pages project (Git-connected)",
            },
            {
                "type": "ol",
                "items": [
                    "Log in to Cloudflare Dashboard → Workers &amp; Pages → Create application → Pages → Connect to Git.",
                    "Authorize Cloudflare to read your repository provider and select the repo containing your landing page.",
                    "Set the production branch to <code>main</code> (or <code>master</code> if older repos use that name).",
                    "Leave <strong>Build command</strong> empty. Set <strong>Build output directory</strong> to <code>/</code> (repository root).",
                    "Click Save and Deploy. First deploy usually finishes in under two minutes.",
                    "Visit the generated <code>your-project.pages.dev</code> URL and verify CSS, images, and links.",
                ],
            },
            {
                "type": "h3",
                "text": "Build settings for plain HTML",
            },
            {
                "type": "p",
                "text": (
                    "If Cloudflare detects a framework it may suggest a build command. For LaunchStatic "
                    "templates, ignore those prompts. An empty build command tells Pages to publish files "
                    "as-is. This is faster and eliminates an entire class of CI failures caused by "
                    "missing Node versions or npm lockfile drift. You edit HTML, commit, push — done."
                ),
            },
            {
                "type": "h2",
                "text": "Custom domains and DNS",
            },
            {
                "type": "p",
                "text": (
                    "After the first deploy succeeds, open your Pages project → Custom domains → Set up "
                    "a custom domain. Enter your apex domain (<code>example.com</code>) or subdomain "
                    "(<code>www.example.com</code>). Cloudflare walks you through DNS records. If your "
                    "domain is already on Cloudflare, the record is often added automatically. "
                    "If your registrar is elsewhere, create the CNAME Cloudflare displays and wait for "
                    "propagation — usually minutes, occasionally up to 24 hours."
                ),
            },
            {
                "type": "p",
                "text": (
                    "SSL certificates provision automatically. Do not pay for third-party certificates "
                    "unless you have a specific compliance requirement. For standard landing pages, "
                    "Cloudflare's Universal SSL is sufficient and renews without manual intervention."
                ),
            },
            {
                "type": "h2",
                "text": "Headers, caching, and security basics",
            },
            {
                "type": "p",
                "text": (
                    "Add a <code>_headers</code> file at your project root to set security headers without "
                    "a server. A minimal example sets <code>X-Frame-Options</code>, "
                    "<code>Referrer-Policy</code>, and cache lifetimes for static assets. Pages reads "
                    "this file on deploy and applies rules at the edge."
                ),
            },
            {
                "type": "pre",
                "code": (
                    "/*\n"
                    "  X-Frame-Options: DENY\n"
                    "  Referrer-Policy: strict-origin-when-cross-origin\n"
                    "\n"
                    "/assets/*\n"
                    "  Cache-Control: public, max-age=31536000, immutable"
                ),
            },
            {
                "type": "p",
                "text": (
                    "For redirects — for example forcing <code>www</code> to apex — add a "
                    "<code>_redirects</code> file. Cloudflare Pages supports the same syntax Netlify "
                    "popularized, which keeps migration straightforward if you switch hosts later."
                ),
            },
            {
                "type": "h2",
                "text": "Common mistakes and fixes",
            },
            {
                "type": "table",
                "rows": [
                    ["Symptom", "Likely cause", "Fix"],
                    ["404 on homepage", "No index.html at repo root", "Move index.html to top level"],
                    ["Unstyled page", "Relative CSS paths break on subroutes", "Use root-relative /assets/ paths"],
                    ["Old content after deploy", "Browser or CDN cache", "Hard refresh; bump asset query strings"],
                    ["Build fails", "Accidental npm build command", "Clear build command; redeploy"],
                ],
            },
            {
                "type": "h2",
                "text": "When to choose something else",
            },
            {
                "type": "p",
                "text": (
                    "Cloudflare Pages is not the only valid choice. GitHub Pages is simpler if your "
                    "audience lives entirely inside GitHub and you do not need preview URLs per branch. "
                    "Netlify Drop is unbeatable for one-off ZIP uploads without Git. Choose Pages when you "
                    "want production-grade CDN, generous free limits, and a path to custom domains without "
                    "migrating DNS providers later."
                ),
            },
        ],
        "faqs": [
            {
                "q": "Is Cloudflare Pages really free for landing pages?",
                "a": (
                    "Yes. Static HTML sites on the free tier include unlimited bandwidth for reasonable "
                    "use, automatic SSL, and global CDN delivery. You pay only if you add paid Cloudflare "
                    "products or exceed specific Workers/Pages paid-plan limits — unlikely for a single "
                    "marketing site."
                ),
            },
            {
                "q": "Do I need Wrangler CLI?",
                "a": (
                    "No. Git-connected deploys handle everything from the dashboard. Wrangler is optional "
                    "for direct uploads or advanced Workers integration."
                ),
            },
            {
                "q": "Can I deploy without GitHub?",
                "a": (
                    "Yes. Use Direct Upload via Wrangler or drag-and-drop workflows documented by "
                    "Cloudflare. Git integration is recommended because it gives you version history "
                    "and preview URLs."
                ),
            },
            {
                "q": "How does Pages work with Formspree or Umami?",
                "a": (
                    "They are client-side integrations. Pages serves your HTML; forms post to Formspree "
                    "and analytics scripts call Umami. No server configuration on Cloudflare is required."
                ),
            },
        ],
        "internal_links": [
            ("/deploy-guides/", "Cloudflare deployment walkthrough"),
            ("/tools/formspree.html", "Formspree form guide"),
            ("/templates/waitlist.html", "Waitlist template"),
        ],
        "cta": {
            "title": "Deploy your template today",
            "text": (
                "Grab a free LaunchStatic template, push to GitHub, and connect Cloudflare Pages. "
                "Most founders have a live HTTPS URL within fifteen minutes."
            ),
            "url": "/templates/",
            "button": "Browse templates",
            "secondary_url": "/deploy-guides/",
            "secondary_button": "Full deploy guide",
        },
    },
    {
        "path": "/tools/formspree.html",
        "meta_title": "Formspree for Static Site Forms — LaunchStatic",
        "meta_description": "Add contact and waitlist forms to static HTML without a backend. Formspree setup, spam protection, free tier limits, and LaunchStatic integration.",
        "h1": "Formspree for Static HTML Forms",
        "section": "Tools",
        "section_url": "/tools/",
        "category": "Tool Guide",
        "date": "2026-06-19",
        "date_display": "June 19, 2026",
        "read_time": "8 min read",
        "sections": [
            {
                "type": "p",
                "text": (
                    "Static sites are fast, cheap, and easy to host — but HTML alone cannot process form "
                    "submissions. You need an endpoint that accepts POST requests and delivers messages "
                    "to your inbox or CRM. Formspree is the most approachable option for indie hackers: "
                    "create a form in their dashboard, paste the endpoint URL into your "
                    "<code>action</code> attribute, and submissions start arriving by email. No Lambda "
                    "functions, no Express server, no database."
                ),
            },
            {
                "type": "h2",
                "text": "How Formspree fits the static stack",
            },
            {
                "type": "p",
                "text": (
                    "A typical pre-launch stack pairs Cloudflare Pages for hosting with Formspree for "
                    "lead capture. The browser loads your page from the CDN; when a visitor submits the "
                    "waitlist form, the browser sends data directly to Formspree's servers. Your static "
                    "host never sees POST traffic. This separation keeps hosting simple while still "
                    "giving you structured submissions you can forward to Slack, Zapier, or Airtable on "
                    "paid plans."
                ),
            },
            {
                "type": "h2",
                "text": "Free tier and when to upgrade",
            },
            {
                "type": "p",
                "text": (
                    "Formspree's free plan includes a limited number of submissions per month — enough "
                    "for early waitlists and contact forms while you validate an idea. Monitor volume "
                    "in the dashboard; if you approach the cap, upgrade or add honeypot fields to reduce "
                    "spam waste. Paid tiers add file uploads, custom redirect URLs after submit, and "
                    "team inboxes. None of that is required on day one."
                ),
            },
            {
                "type": "h2",
                "text": "Minimal waitlist form markup",
            },
            {
                "type": "p",
                "text": (
                    "Every Formspree form needs a unique <code>action</code> URL and explicit "
                    "<code>method=\"post\"</code>. Name attributes become column headers in export "
                    "files — use clear names like <code>email</code> instead of <code>field1</code>."
                ),
            },
            {
                "type": "pre",
                "code": (
                    '<form action="https://formspree.io/f/YOUR_FORM_ID" method="post">\n'
                    '  <label for="email">Email</label>\n'
                    '  <input type="email" id="email" name="email" required>\n'
                    '  <button type="submit">Join waitlist</button>\n'
                    "</form>"
                ),
            },
            {
                "type": "p",
                "text": (
                    "Replace <code>YOUR_FORM_ID</code> with the ID from your Formspree project settings. "
                    "Deploy to Cloudflare Pages and test with a real address. First submission triggers "
                    "a confirmation email from Formspree — click the link to activate delivery."
                ),
            },
            {
                "type": "h2",
                "text": "Spam protection without backend code",
            },
            {
                "type": "p",
                "text": (
                    "Public forms attract bots. Formspree supports reCAPTCHA and hCaptcha integrations "
                    "you enable in the dashboard. For lighter protection, add a honeypot field hidden "
                    "with CSS that humans never see but bots fill in. Formspree silently drops honeypot "
                    "submissions. LaunchStatic waitlist templates leave a commented honeypot slot you "
                    "can uncomment before launch."
                ),
            },
            {
                "type": "h3",
                "text": "Honeypot field pattern",
            },
            {
                "type": "pre",
                "code": (
                    '<p class="hp" aria-hidden="true" style="display:none">\n'
                    '  <label>Leave blank<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label>\n'
                    "</p>"
                ),
            },
            {
                "type": "h2",
                "text": "Custom fields and hidden metadata",
            },
            {
                "type": "p",
                "text": (
                    "Add optional inputs for name, company size, or use case — Formspree records every "
                    "named field. Hidden inputs track campaign source: "
                    "<code>&lt;input type=\"hidden\" name=\"utm_source\" value=\"producthunt\"&gt;</code>. "
                    "Append UTM parameters to your landing URL and copy them into hidden fields with "
                    "a few lines of JavaScript if you want cleaner attribution without Google Analytics."
                ),
            },
            {
                "type": "h2",
                "text": "Success states and UX polish",
            },
            {
                "type": "p",
                "text": (
                    "By default, Formspree redirects to a generic thank-you page. For on-brand UX, use "
                    "AJAX submission with <code>fetch</code> and show an inline success message. "
                    "Formspree supports JSON responses when you set <code>Accept: application/json</code> "
                    "and handle errors for validation failures. Keep a mailto fallback link for visitors "
                    "if JavaScript is disabled — accessibility still matters on marketing pages."
                ),
            },
            {
                "type": "h2",
                "text": "Privacy and compliance notes",
            },
            {
                "type": "p",
                "text": (
                    "When you use Formspree, visitor emails pass through their servers. Update your "
                    "privacy policy to name Formspree as a processor and link to their DPA if you "
                    "target EU users. Do not collect sensitive health or financial data through a "
                    "simple marketing form. For GDPR, mention lawful basis (consent) and provide "
                    "a contact address for deletion requests — standard for waitlist pages."
                ),
            },
            {
                "type": "h2",
                "text": "Alternatives worth knowing",
            },
            {
                "type": "ul",
                "items": [
                    "<strong>Netlify Forms</strong> — convenient if you already host on Netlify; attribute-based setup.",
                    "<strong>Getform / Basin</strong> — similar POST-to-inbox models with different pricing curves.",
                    "<strong>Cloudflare Workers</strong> — roll your own endpoint when you need custom validation logic.",
                    "<strong>mailto: links</strong> — zero setup but poor UX and no structured exports.",
                ],
            },
            {
                "type": "p",
                "text": (
                    "Formspree wins on documentation quality and time-to-first-submission. You can always "
                    "migrate endpoints later without changing hosting — swap the <code>action</code> URL "
                    "and redeploy."
                ),
            },
        ],
        "faqs": [
            {
                "q": "Does Formspree work on Cloudflare Pages?",
                "a": (
                    "Yes. The form POST goes from the visitor's browser to Formspree, not to Cloudflare. "
                    "Any static host works identically."
                ),
            },
            {
                "q": "Can I receive submissions in Slack?",
                "a": (
                    "Paid plans and Zapier integrations support Slack notifications. Free tier is "
                    "email-first; forward rules in Gmail are a zero-cost workaround early on."
                ),
            },
            {
                "q": "What happens if I exceed the free submission limit?",
                "a": (
                    "Additional submissions may be blocked until the next billing cycle or until you "
                    "upgrade. Watch the dashboard during launch week."
                ),
            },
            {
                "q": "Is AJAX required?",
                "a": (
                    "No. Standard HTML form POST with redirect is fine for MVPs. AJAX improves UX but "
                    "adds JavaScript you must maintain."
                ),
            },
        ],
        "internal_links": [
            ("/tools/cloudflare-pages.html", "Cloudflare Pages guide"),
            ("/templates/waitlist.html", "Waitlist template"),
            ("/blog/waitlist-page-conversion-tips.html", "Waitlist conversion tips"),
        ],
        "cta": {
            "title": "Ship a waitlist this week",
            "text": (
                "Our Waitlist template includes form markup ready for Formspree. Customize headline "
                "copy, paste your endpoint, deploy."
            ),
            "url": "/templates/waitlist.html",
            "button": "Get waitlist template",
            "secondary_url": "/tools/cloudflare-pages.html",
            "secondary_button": "Set up hosting",
        },
    },
    {
        "path": "/tools/umami.html",
        "meta_title": "Umami Analytics for Static Sites — LaunchStatic",
        "meta_description": "Privacy-friendly analytics with Umami: self-host free or use cloud hosting. Setup script, GDPR considerations, and comparison to Plausible and GA4.",
        "h1": "Umami Analytics for Static Sites",
        "section": "Tools",
        "section_url": "/tools/",
        "category": "Tool Guide",
        "date": "2026-06-19",
        "date_display": "June 19, 2026",
        "read_time": "10 min read",
        "sections": [
            {
                "type": "p",
                "text": (
                    "You cannot improve a landing page you do not measure — but mainstream analytics "
                    "tools often bring cookie banners, heavy scripts, and data practices that feel "
                    "overkill for a single pre-launch page. Umami is an open-source analytics platform "
                    "built for simplicity: pageviews, referrers, devices, and basic events without "
                    "tracking individuals across the web. It fits static sites because integration is "
                    "one async script tag and a website ID."
                ),
            },
            {
                "type": "h2",
                "text": "Self-hosted vs Umami Cloud",
            },
            {
                "type": "p",
                "text": (
                    "Umami is AGPL-licensed and runs on PostgreSQL or MySQL. Self-hosting on a $5 VPS "
                    "or a small Docker container on Fly.io costs less than SaaS analytics over a year "
                    "if you are comfortable running updates. Umami Cloud (hosted by the creators) "
                    "trades money for convenience — reasonable when your time is worth more than "
                    "server maintenance. Both options respect visitor privacy more than legacy "
                    "enterprise analytics stacks."
                ),
            },
            {
                "type": "table",
                "rows": [
                    ["Approach", "Cost profile", "Best for"],
                    ["Self-host Docker", "VPS + your time", "Technical founders, multiple sites"],
                    ["Umami Cloud", "Monthly subscription", "Fast setup, no DevOps"],
                    ["Plausible Cloud", "Monthly subscription", "Teams wanting hosted EU option"],
                    ["No analytics", "$0", "Absolute minimum before launch"],
                ],
            },
            {
                "type": "h2",
                "text": "What Umami tracks (and does not)",
            },
            {
                "type": "p",
                "text": (
                    "Umami records page URL, referrer, browser, OS, device type, and country derived "
                    "from IP — then discards raw IP per their design. It does not fingerprint users "
                    "for cross-site profiling. You get aggregate dashboards: which blog post drove "
                    "signups, whether mobile bounce is high, if a Hacker News spike happened. It is not "
                    "a replacement for product analytics inside your SaaS app; it is marketing-site "
                    "telemetry done ethically."
                ),
            },
            {
                "type": "h2",
                "text": "Add Umami to LaunchStatic templates",
            },
            {
                "type": "p",
                "text": (
                    "Create a website entry in Umami admin, copy the tracking ID, and paste the script "
                    "before <code>&lt;/body&gt;</code> on every page you want measured — at minimum "
                    "<code>index.html</code>, plus legal pages if you care about privacy-policy traffic."
                ),
            },
            {
                "type": "pre",
                "code": (
                    '<script defer src="https://your-umami.example.com/script.js" '
                    'data-website-id="YOUR_WEBSITE_ID"></script>'
                ),
            },
            {
                "type": "p",
                "text": (
                    "Use the <code>defer</code> attribute so HTML parsing is not blocked. Host the script "
                    "on the same domain as your Umami instance (or Umami Cloud URL). After deploy, visit "
                    "your live site and confirm realtime views increment in the dashboard."
                ),
            },
            {
                "type": "h2",
                "text": "Self-hosting quick path with Docker",
            },
            {
                "type": "p",
                "text": (
                    "The official Docker Compose file spins up Umami and PostgreSQL. Point a subdomain "
                    "like <code>analytics.yourdomain.com</code> at the server, terminate TLS with "
                    "Caddy or Nginx, and set a strong admin password on first login. Schedule automatic "
                    "image updates — Umami releases security patches like any public-facing app. "
                    "Back up the database volume; losing stats is not catastrophic but hurts trend analysis."
                ),
            },
            {
                "type": "h3",
                "text": "Environment variables that matter",
            },
            {
                "type": "ul",
                "items": [
                    "<code>DATABASE_URL</code> — PostgreSQL connection string",
                    "<code>APP_SECRET</code> — session signing secret; generate a long random string",
                    "<code>DISABLE_TELEMETRY</code> — set true if you prefer no phone-home from the app itself",
                    "<code>CORS</code> — restrict origins if you embed the script on multiple domains",
                ],
            },
            {
                "type": "h2",
                "text": "Custom events for conversion tracking",
            },
            {
                "type": "p",
                "text": (
                    "Beyond pageviews, Umami supports custom events — useful for button clicks without "
                    "full tag-manager complexity. Track waitlist submits by firing an event after "
                    "successful Formspree response:"
                ),
            },
            {
                "type": "pre",
                "code": (
                    "if (window.umami) {\n"
                    "  umami.track('waitlist_signup', { source: 'hero' });\n"
                    "}"
                ),
            },
            {
                "type": "p",
                "text": (
                    "Keep event names consistent and documented. Three well-chosen events beat fifty "
                    "noisy ones you never review."
                ),
            },
            {
                "type": "h2",
                "text": "GDPR, cookie banners, and privacy policies",
            },
            {
                "type": "p",
                "text": (
                    "Umami markets itself as cookieless analytics when configured without local storage. "
                    "Many EU sites still mention analytics in privacy policies and offer opt-out where "
                    "required. LaunchStatic is not a law firm — consult your counsel for your markets. "
                    "Practically, teams choose Umami to reduce intrusive consent banners compared to "
                    "AdTech-heavy alternatives. Document what you collect and why in "
                    "<a href=\"/privacy.html\">your privacy page</a>."
                ),
            },
            {
                "type": "h2",
                "text": "Umami vs Plausible vs Google Analytics 4",
            },
            {
                "type": "p",
                "text": (
                    "<strong>Plausible</strong> is a polished hosted product with transparent pricing "
                    "and excellent docs — great if you want zero servers and will pay monthly from day one. "
                    "<strong>GA4</strong> is free but complex, script-heavy, and tied to Google's ecosystem; "
                    "overkill for a waitlist. <strong>Umami</strong> shines when you want open source, "
                    "self-host optionality, and a clean dashboard without learning a tag manager. "
                    "You can switch tools later — analytics snippets are a few lines in shared layout partials."
                ),
            },
            {
                "type": "h2",
                "text": "Operational tips for launch week",
            },
            {
                "type": "checklist",
                "items": [
                    "Verify tracking on production domain, not just localhost",
                    "Exclude your own IP in Umami settings to avoid skewing data",
                    "Share read-only dashboard links with cofounders instead of screenshots",
                    "Set a weekly reminder to review top referrers and adjust messaging",
                    "Remove analytics from password-protected staging environments",
                ],
            },
        ],
        "faqs": [
            {
                "q": "Will Umami slow my landing page?",
                "a": (
                    "The tracker is lightweight — far smaller than typical GA4 bundles. Use "
                    "<code>defer</code> and load from a nearby host to minimize impact on Core Web Vitals."
                ),
            },
            {
                "q": "Do I need cookies consent with Umami?",
                "a": (
                    "Depends on jurisdiction and configuration. Many sites use Umami specifically to "
                    "avoid cookie banners, but you must align with your legal advice and disclose "
                    "analytics in your privacy policy."
                ),
            },
            {
                "q": "Can I run Umami on Cloudflare Workers?",
                "a": (
                    "Umami expects Node and a SQL database; Workers alone are not a fit. Host on a VPS, "
                    "Railway, Render, or Umami Cloud instead."
                ),
            },
            {
                "q": "Does Umami support multiple sites?",
                "a": (
                    "Yes. One Umami instance can track many websites with separate IDs — ideal for "
                    "portfolio founders running several experiments."
                ),
            },
        ],
        "internal_links": [
            ("/tools/cloudflare-pages.html", "Cloudflare Pages guide"),
            ("/tools/formspree.html", "Formspree guide"),
            ("/privacy.html", "Privacy policy template"),
        ],
        "cta": {
            "title": "Measure what you ship",
            "text": (
                "Deploy a LaunchStatic template, add Umami in two minutes, and know where your first "
                "visitors come from before you scale ad spend."
            ),
            "url": "/templates/",
            "button": "Browse templates",
            "secondary_url": "/tools/",
            "secondary_button": "All tool guides",
        },
    },
]


def all_articles() -> list[dict]:
    return ARTICLES
"""Commercial and legal page content for LaunchStatic."""
from __future__ import annotations

PAGES: list[dict] = [
    {
        "path": "/free-static-landing-kit/index.html",
        "meta_title": "Free Static Landing Kit — LaunchStatic",
        "meta_description": "Download the free LaunchStatic landing kit: MIT templates, deploy checklist, and tool stack guide. Ship a static page without a framework or monthly fees.",
        "h1": "Free Static Landing Kit",
        "hero_lead": (
            "Everything you need to publish a credible landing page this weekend — templates, "
            "deployment steps, and form hooks. No account required to download."
        ),
        "badge": "Free",
        "nav_active": "templates",
        "sections": [
            {
                "type": "p",
                "text": (
                    "The Free Static Landing Kit bundles LaunchStatic's MIT-licensed templates with "
                    "the deployment and tooling guidance founders actually use. You are not signing up "
                    "for a platform trial that expires in fourteen days. You download HTML files, edit "
                    "them in any text editor, and host them on Cloudflare Pages or GitHub Pages for $0. "
                    "This kit exists because too many builders stall on toolchain decisions instead of "
                    "talking to customers."
                ),
            },
            {
                "type": "h2",
                "text": "What is inside the kit",
            },
            {
                "type": "ul",
                "items": [
                    "<strong>SaaS Landing template</strong> — hero, features, pricing table, FAQ, footer CTA",
                    "<strong>App Landing template</strong> — store badges, screenshot gallery, privacy link slots",
                    "<strong>Waitlist template</strong> — single-focus email capture with Formspree-ready markup",
                    "<strong>Deployment checklist</strong> — pre-launch QA from <code>docs/DEPLOYMENT-CHECKLIST.md</code>",
                    "<strong>Tool stack primer</strong> — Cloudflare Pages, Formspree, and analytics options",
                    "<strong>Legal page starters</strong> — pointers to privacy, terms, and cookie notice patterns",
                ],
            },
            {
                "type": "p",
                "text": (
                    "Each template is a self-contained HTML file with embedded CSS patterns matching "
                    "launchstatic.dev. Total page weight stays under 50 KB gzipped on typical pages — "
                    "fast on mobile networks and friendly to Core Web Vitals. You may use these templates "
                    "in commercial products, client work, and funded startups under the MIT License."
                ),
            },
            {
                "type": "h2",
                "text": "Who this kit is for",
            },
            {
                "type": "p",
                "text": (
                    "Solo founders validating an idea need a professional page before they write backend "
                    "code. Agencies prototyping client concepts need a neutral starting point they can "
                    "hand off. Developers allergic to WordPress and Webflow billing want files they own. "
                    "Students and bootcamp graduates benefit from readable markup they can study without "
                    "unpicking a React build chain. If you already run a mature design system, this kit "
                    "may be too minimal — but for first versions it is deliberately constrained."
                ),
            },
            {
                "type": "h2",
                "text": "How to use the kit in one afternoon",
            },
            {
                "type": "ol",
                "items": [
                    "Pick the template closest to your product story — SaaS for B2B tools, Waitlist for pre-launch.",
                    "Replace placeholder headline, subhead, and feature bullets with your positioning.",
                    "Swap colors in CSS variables at the top of each file; keep contrast accessible.",
                    "Connect the waitlist or contact form to Formspree by pasting your endpoint URL.",
                    "Push the folder to a new GitHub repository with <code>index.html</code> at the root.",
                    "Connect the repo to Cloudflare Pages with an empty build command and output directory <code>/</code>.",
                    "Run through the deployment checklist: mobile layout, form test, legal links, favicon.",
                ],
            },
            {
                "type": "h2",
                "text": "Free vs paid on LaunchStatic",
            },
            {
                "type": "p",
                "text": (
                    "This kit is and will remain free. Paid offerings — the "
                    "<a href=\"/pro-template-pack/\">Pro Template Pack</a>, "
                    "<a href=\"/landing-page-audit/\">Landing Page Audit</a>, and "
                    "<a href=\"/done-for-you/\">Done-for-you builds</a> — add vertical layouts, expert "
                    "review, or hands-on implementation. We label free assets clearly so you never "
                    "download a paid file by accident. Upgrading is optional; shipping with the free "
                    "kit is a complete path to production."
                ),
            },
            {
                "type": "h2",
                "text": "License summary",
            },
            {
                "type": "p",
                "text": (
                    "Kit templates fall under the MIT License. You can modify, deploy, and ship products "
                    "built with them. You cannot misrepresent LaunchStatic as the author of your final "
                    "product branding. Full terms live on our "
                    "<a href=\"/license/\">License page</a> and in the repository <code>LICENSE</code> file. "
                    "Site copy and blog articles are not MIT-licensed — write your own marketing text."
                ),
            },
            {
                "type": "h2",
                "text": "Download and next steps",
            },
            {
                "type": "p",
                "text": (
                    "Browse live demos on the <a href=\"/templates/\">templates catalog</a>, download "
                    "single-file HTML from <code>/downloads/</code>, or clone the repository. No email "
                    "gate for downloads. If you want occasional deploy tips, use the newsletter below — "
                    "otherwise jump straight to the <a href=\"/deploy-guides/\">deploy guide</a> and ship."
                ),
            },
            {
                "type": "h2",
                "text": "Frequently asked questions",
            },
            {
                "type": "p",
                "text": (
                    "<strong>Do I need an account?</strong> No. Downloads are direct links from our site "
                    "and repository. <strong>Can I remove LaunchStatic branding?</strong> Yes — templates "
                    "use neutral placeholders; replace logo text and footer credits with your own. "
                    "<strong>Will the kit work on Netlify or GitHub Pages?</strong> Yes. Any static host "
                    "that serves HTML from a root directory works; Cloudflare Pages is our recommended "
                    "default because of bandwidth and preview URLs. <strong>Is support included?</strong> "
                    "Community-scale support via email for broken links or unclear docs — not custom design "
                    "work. For hands-on help, see paid services on our pricing page."
                ),
            },
        ],
        "highlights": [
            {
                "title": "MIT licensed",
                "text": "Commercial use allowed. Keep the copyright notice in source copies per MIT requirements.",
                "badge": "Free",
            },
            {
                "title": "No build step",
                "text": "Upload HTML as-is to Cloudflare Pages. Skip npm, webpack, and framework migrations.",
            },
            {
                "title": "Form-ready",
                "text": "Waitlist markup works with Formspree out of the box — paste your endpoint and test.",
            },
        ],
        "primary_cta": {
            "url": "/templates/",
            "button": "Browse free templates",
            "secondary_url": "/deploy-guides/",
            "secondary_button": "Deploy guide",
        },
        "show_newsletter": True,
        "show_contact": True,
    },
    {
        "path": "/pro-template-pack/index.html",
        "meta_title": "Pro Template Pack — LaunchStatic",
        "meta_description": "Six additional vertical landing layouts, i18n-ready structure, and a single-project commercial license. $49 one-time — not redistributable.",
        "h1": "Pro Template Pack",
        "hero_lead": (
            "Polished layouts for niches the free trio does not cover — with structure ready for "
            "translation files and client handoff."
        ),
        "badge": "Pro",
        "price_display": "$49",
        "price_period": "one-time",
        "nav_active": "pricing",
        "sections": [
            {
                "type": "p",
                "text": (
                    "The Pro Template Pack extends LaunchStatic beyond the free SaaS, App, and Waitlist "
                    "starters. You get six additional vertical layouts aimed at common indie hacker "
                    "segments: developer tools, newsletters, open-source projects, consulting offers, "
                    "course launches, and simple ecommerce lead-gen. Each file follows the same "
                    "lightweight philosophy — semantic HTML, CSS variables, vanilla JS only where "
                    "interaction is unavoidable."
                ),
            },
            {
                "type": "h2",
                "text": "What you receive",
            },
            {
                "type": "ul",
                "items": [
                    "Six production HTML templates with matching demo pages and download bundles",
                    "Shared partial patterns for nav, footer, FAQ, and pricing tables",
                    "i18n-ready <code>data-i18n</code> hooks and a sample JSON dictionary file",
                    "Dark-mode CSS variable sets you can toggle with one class on <code>&lt;html&gt;</code>",
                    "Accessibility pass: focus states, skip links, landmark roles, form labels",
                    "Changelog and migration notes when we ship pack updates",
                ],
            },
            {
                "type": "h2",
                "text": "Pricing and license",
            },
            {
                "type": "p",
                "text": (
                    "The Pro Template Pack is <strong>$49 one-time</strong> per purchase. That is not a "
                    "subscription — you keep the files you download. License terms differ from the free "
                    "MIT templates: you may use the pack in your own projects and client deliverables "
                    "per the tier described on our <a href=\"/license/\">License page</a>, but you "
                    "<strong>may not redistribute, resell, or publish the source files</strong> on "
                    "template marketplaces or public GitHub repos. End products you build for users are "
                    "allowed; sharing the raw HTML pack with competitors is not."
                ),
            },
            {
                "type": "h2",
                "text": "Who should buy",
            },
            {
                "type": "p",
                "text": (
                    "Buy the pack if you ship multiple landing pages per year and want consistent "
                    "quality without rebuilding layout grids each time. Freelancers delivering client "
                    "sites save billable hours. Founders who outgrew the free templates but do not "
                    "want a $29/month site builder subscription get a predictable one-time cost. "
                    "If you need only one page and the free templates suffice, save the $49 until "
                    "you feel layout constraints — there is no artificial feature lock on the free tier."
                ),
            },
            {
                "type": "h2",
                "text": "How purchase works",
            },
            {
                "type": "ol",
                "items": [
                    "Email <a href=\"mailto:hello@launchstatic.dev?subject=Pro%20Template%20Pack%20purchase\">hello@launchstatic.dev</a> with subject \"Pro Template Pack purchase\" or use the contact page.",
                    "We send a secure payment link and confirm the email address for delivery.",
                    "After payment, you receive a download link and license confirmation within two business days.",
                    "Keep your receipt — it documents the license grant date for your records.",
                ],
            },
            {
                "type": "p",
                "text": (
                    "We are a small operator — not a faceless marketplace. If you have questions about "
                    "client work or agency use, ask before buying so we can confirm the license fits "
                    "your workflow."
                ),
            },
            {
                "type": "h2",
                "text": "Updates and support",
            },
            {
                "type": "p",
                "text": (
                    "Pack updates for typos, accessibility fixes, and compatibility with hosting guides "
                    "are included for twelve months from purchase. Major new verticals may ship as a "
                    "separate pack rather than diluting this SKU. Email support covers broken downloads "
                    "and license clarification — not unlimited custom design work. For implementation "
                    "help, see <a href=\"/done-for-you/\">Done-for-you</a> or "
                    "<a href=\"/landing-page-audit/\">Landing Page Audit</a>."
                ),
            },
            {
                "type": "h2",
                "text": "Comparison with free templates",
            },
            {
                "type": "table",
                "rows": [
                    ["", "Free templates", "Pro Template Pack"],
                    ["Price", "$0", "$49 one-time"],
                    ["License", "MIT", "Commercial single-project license"],
                    ["Layouts", "3 core", "6 vertical + shared patterns"],
                    ["Redistribution", "Allowed with MIT notice", "Prohibited"],
                    ["i18n structure", "Basic", "Dictionary-ready hooks"],
                ],
            },
            {
                "type": "h2",
                "text": "Technical requirements",
            },
            {
                "type": "p",
                "text": (
                    "The pack ships as plain HTML/CSS/JS — the same stack as free templates. Open files "
                    "in VS Code, Zed, or any editor. Preview locally with "
                    "<code>python -m http.server</code> or your editor's live server. No Node version "
                    "to pin, no package lockfile to audit. Custom fonts load from system stacks by "
                    "default; swap in self-hosted or Google Fonts if your brand guide requires it. "
                    "Images use responsive <code>srcset</code> placeholders you replace with WebP or AVIF "
                    "exports from Figma. Deployment targets remain Cloudflare Pages, Netlify, or S3 — "
                    "anywhere static files are served."
                ),
            },
            {
                "type": "p",
                "text": (
                    "Refund eligibility before download is described on our "
                    "<a href=\"/refund-policy/\">Refund Policy</a> page. We do not promise AdSense "
                    "approval, search rankings, or revenue — the pack is design and structure, not "
                    "a growth guarantee."
                ),
            },
        ],
        "primary_cta": {
            "url": "mailto:hello@launchstatic.dev?subject=Pro%20Template%20Pack%20purchase",
            "button": "Request purchase link",
            "secondary_url": "/license/",
            "secondary_button": "Read license",
        },
        "show_newsletter": True,
        "show_contact": True,
        "contact_title": "Purchase questions",
    },
    {
        "path": "/landing-page-audit/index.html",
        "meta_title": "Landing Page Audit — LaunchStatic",
        "meta_description": "Expert review of your static landing page: messaging, mobile UX, performance, forms, and legal basics. $199 fixed price — actionable report in five business days.",
        "h1": "Landing Page Audit",
        "hero_lead": (
            "A focused review of your live or staging page before you spend on ads or Product Hunt. "
            "Written report, prioritized fixes, no fluff."
        ),
        "badge": "Service",
        "price_display": "$199",
        "price_period": "fixed price",
        "nav_active": "pricing",
        "sections": [
            {
                "type": "p",
                "text": (
                    "You built a page — or shipped a LaunchStatic template — but conversion feels soft "
                    "and you cannot tell if the problem is copy, layout, speed, or trust signals. The "
                    "Landing Page Audit is a fixed-scope review by operators who deploy static sites "
                    "daily. We do not sell hourly retainers or upsell you into a rebuild unless you "
                    "explicitly want <a href=\"/done-for-you/\">Done-for-you</a> work afterward."
                ),
            },
            {
                "type": "h2",
                "text": "What we review",
            },
            {
                "type": "ul",
                "items": [
                    "<strong>Positioning clarity</strong> — headline, subhead, and CTA alignment with your offer",
                    "<strong>Above-the-fold impact</strong> — mobile and desktop screenshots with annotations",
                    "<strong>Performance snapshot</strong> — Lighthouse-style metrics and asset weight notes",
                    "<strong>Form and tracking setup</strong> — Formspree endpoints, success states, analytics presence",
                    "<strong>Trust and compliance basics</strong> — privacy link, cookie notice, contact visibility",
                    "<strong>Accessibility spot check</strong> — contrast, focus order, form labels, heading hierarchy",
                ],
            },
            {
                "type": "h2",
                "text": "What you get",
            },
            {
                "type": "p",
                "text": (
                    "Within five business days of receiving your URL and payment confirmation, you get a "
                    "PDF or shared-doc report typically eight to twelve pages. Each issue is tagged "
                    "Critical, Important, or Nice-to-have so you know what blocks launch versus what "
                    "can wait. We include copy suggestions where helpful — not a full rewrite, but "
                    "concrete examples you can paste and adapt. One round of clarification questions "
                    "by email is included."
                ),
            },
            {
                "type": "h2",
                "text": "Pricing: $199 fixed",
            },
            {
                "type": "p",
                "text": (
                    "The audit is <strong>$199 USD</strong> for a single landing page URL (including "
                    "localized variants if they share one template). No per-seat fees, no surprise "
                    "overages. Additional pages or full site crawls are quoted separately before work "
                    "starts. Refunds follow our <a href=\"/refund-policy/\">Refund Policy</a> — we "
                    "want you to feel the report earned its price."
                ),
            },
            {
                "type": "h2",
                "text": "How to book",
            },
            {
                "type": "ol",
                "items": [
                    "Email <a href=\"mailto:hello@launchstatic.dev?subject=Landing%20Page%20Audit\">hello@launchstatic.dev</a> with your page URL and launch timeline.",
                    "We confirm scope, send payment instructions, and schedule your review slot.",
                    "You receive the report within five business days after payment clears.",
                    "Implement fixes yourself or ask about Done-for-you implementation starting at $799.",
                ],
            },
            {
                "type": "h2",
                "text": "What we do not promise",
            },
            {
                "type": "p",
                "text": (
                    "An audit is not a guarantee of conversion rate, search ranking, ad approval, or "
                    "revenue outcomes. We do not certify your site for Google AdSense or any ad network — "
                    "platform policies change and account decisions are theirs alone. We do not provide "
                    "legal advice; compliance notes are practical checklists, not attorney opinions. "
                    "We will not invent vanity metrics or fake social proof for your page — ever."
                ),
            },
            {
                "type": "h2",
                "text": "Good fit vs poor fit",
            },
            {
                "type": "p",
                "text": (
                    "<strong>Good fit:</strong> pre-launch SaaS, waitlist pages, static marketing sites "
                    "on Cloudflare Pages, template-based pages you customized yourself. "
                    "<strong>Poor fit:</strong> complex multi-page apps, heavy SPAs requiring codebase "
                    "access, enterprises needing WCAG 2.2 formal certification, or teams wanting ongoing "
                    "CRO experimentation. Be honest about scope upfront — it saves everyone time."
                ),
            },
            {
                "type": "h2",
                "text": "Sample findings (illustrative)",
            },
            {
                "type": "p",
                "text": (
                    "Past audits commonly surface fixable issues: hero headlines that describe features "
                    "instead of outcomes, CTAs below the fold on mobile, uncompressed hero images adding "
                    "seconds to LCP, forms missing labels for screen readers, and privacy links buried "
                    "in footer fine print. We prioritize fixes that improve clarity and trust before "
                    "cosmetic tweaks. You receive enough detail to hand tasks to a developer or tackle "
                    "them yourself in an afternoon."
                ),
            },
            {
                "type": "p",
                "text": (
                    "We do not fabricate user counts, testimonial quotes, or revenue figures for your "
                    "page. If social proof is thin, we say so and suggest ethical ways to build trust "
                    "— operator contact visibility, clear pricing, and honest feature lists beat fake "
                    "metrics every time."
                ),
            },
            {
                "type": "h2",
                "text": "After the audit",
            },
            {
                "type": "p",
                "text": (
                    "You implement recommendations at your own pace. Many founders fix Critical items "
                    "the same day — often copy and mobile spacing — and defer Nice-to-have polish until "
                    "after first traffic. If you prefer implementation help, forward the report when "
                    "requesting a <a href=\"/done-for-you/\">Done-for-you quote</a> so we scope against "
                    "documented findings instead of starting from zero."
                ),
            },
        ],
        "primary_cta": {
            "url": "mailto:hello@launchstatic.dev?subject=Landing%20Page%20Audit",
            "button": "Book an audit",
            "secondary_url": "/refund-policy/",
            "secondary_button": "Refund policy",
        },
        "show_newsletter": False,
        "show_contact": True,
        "contact_title": "Audit inquiries",
    },
    {
        "path": "/done-for-you/index.html",
        "meta_title": "Done-for-You Static Landing Pages — LaunchStatic",
        "meta_description": "We build and deploy your static landing page on Cloudflare Pages. Custom copy, brand styling, forms, and analytics — from $799. Inquiry-based pricing.",
        "h1": "Done-for-You Landing Pages",
        "hero_lead": (
            "You focus on product; we ship the page. Static HTML, fast hosting, handoff you own."
        ),
        "badge": "Service",
        "price_display": "From $799",
        "price_period": "project inquiry",
        "nav_active": "pricing",
        "sections": [
            {
                "type": "p",
                "text": (
                    "Not everyone wants to tweak CSS variables at midnight before a launch. Done-for-you "
                    "is LaunchStatic's implementation service: we take your brief, select the right "
                    "template foundation, customize copy and visuals, wire forms and analytics, deploy to "
                    "Cloudflare Pages, and hand you the repository. You get static files — not a "
                    "proprietary CMS login that disappears if you stop paying."
                ),
            },
            {
                "type": "h2",
                "text": "Starting at $799 — what that covers",
            },
            {
                "type": "p",
                "text": (
                    "Base projects <strong>start from $799 USD</strong> for a single landing page with "
                    "up to two revision rounds, mobile-responsive layout, Formspree or equivalent form "
                    "hookup, basic analytics script placement, and Cloudflare Pages deployment with "
                    "custom domain guidance. Final quotes depend on content volume, illustration needs, "
                    "number of sections, integrations, and timeline. We confirm price in writing before "
                    "deposit — no scope creep without your approval."
                ),
            },
            {
                "type": "h2",
                "text": "Typical deliverables",
            },
            {
                "type": "ul",
                "items": [
                    "Customized static HTML/CSS/JS based on LaunchStatic templates or Pro Pack layouts",
                    "Git repository you own, with README deploy instructions",
                    "Production deploy on Cloudflare Pages plus staging preview URL",
                    "Form endpoint connected and tested with a live submission",
                    "Analytics snippet (Umami, Plausible, or your choice) installed",
                    "Links to privacy, terms, and contact pages — or stubs you replace later",
                    "Short Loom-style walkthrough video showing how to edit copy",
                ],
            },
            {
                "type": "h2",
                "text": "Process and timeline",
            },
            {
                "type": "ol",
                "items": [
                    "<strong>Inquiry</strong> — email hello@launchstatic.dev with offer summary, deadline, and example sites you like.",
                    "<strong>Quote</strong> — we respond within two business days with price, timeline, and assumptions.",
                    "<strong>Kickoff</strong> — 50% deposit via agreed payment method; you share brand assets and copy doc.",
                    "<strong>Build</strong> — first draft on staging within 5–10 business days for standard scope.",
                    "<strong>Revisions</strong> — two structured rounds included; additional rounds billed hourly if needed.",
                    "<strong>Launch</strong> — final payment, production deploy, repo transfer, and handoff call optional.",
                ],
            },
            {
                "type": "h2",
                "text": "What affects price",
            },
            {
                "type": "table",
                "rows": [
                    ["Factor", "Impact"],
                    ["Multiple pages or blog index", "Quoted above base"],
                    ["Custom illustrations or photography sourcing", "Quoted above base"],
                    ["Copywriting from scratch", "Optional add-on"],
                    ["Rush delivery under five business days", "Rush fee if calendar allows"],
                    ["Pro Template Pack layouts", "Pack purchase or license confirmation required"],
                ],
            },
            {
                "type": "h2",
                "text": "Ownership and licensing",
            },
            {
                "type": "p",
                "text": (
                    "You own the deployed site and Git repo. Free MIT template portions remain MIT; "
                    "Pro Pack elements require a valid pack license. We do not claim your product "
                    "trademarks or copy. Portfolio display: we may list your page as a case study "
                    "only with your written permission. Maintenance retainers are available on request "
                    "but never required — static pages do not need weekly patches like WordPress."
                ),
            },
            {
                "type": "h2",
                "text": "Honest limits",
            },
            {
                "type": "p",
                "text": (
                    "We build marketing landing pages, not full web applications. No user auth dashboards, "
                    "payment processing backends, or database admin panels. We do not guarantee ad network "
                    "approval, VC outcomes, or specific conversion rates. If you need strategy before "
                    "build, start with a <a href=\"/landing-page-audit/\">$199 audit</a> to align "
                    "messaging first."
                ),
            },
            {
                "type": "h2",
                "text": "What to send in your inquiry",
            },
            {
                "type": "p",
                "text": (
                    "Strong inquiries include a one-paragraph product description, target visitor, "
                    "deadline, budget range, and two or three reference URLs whose tone you admire — "
                    "not necessarily competitors. Attach logo SVG or PNG, hex colors, and draft copy "
                    "if you have it; we can refine rough notes. Mention required integrations (Formspree, "
                    "Cal.com embed, Umami instance URL). We respond with a fixed quote or questions "
                    "within two business days. No automated checkout — every project is confirmed human-to-human."
                ),
            },
            {
                "type": "p",
                "text": (
                    "Deposits and refunds follow the <a href=\"/refund-policy/\">Refund Policy</a>. "
                    "We never add fake urgency timers, fabricated user counts, or misleading scarcity "
                    "widgets to your page unless you explicitly provide real data to display."
                ),
            },
            {
                "type": "h2",
                "text": "Maintenance after launch",
            },
            {
                "type": "p",
                "text": (
                    "Static pages rarely need emergency patches. Optional maintenance blocks cover "
                    "quarterly copy tweaks, form endpoint rotation, and analytics script updates — quoted "
                    "separately, never auto-billed. You keep full repo access so any developer can take "
                    "over without our involvement. That independence is a feature, not a gap."
                ),
            },
        ],
        "primary_cta": {
            "url": "mailto:hello@launchstatic.dev?subject=Done-for-you%20landing%20page%20inquiry",
            "button": "Request a quote",
            "secondary_url": "/landing-page-audit/",
            "secondary_button": "Start with audit",
        },
        "show_newsletter": False,
        "show_contact": True,
        "contact_title": "Project inquiries",
    },
    {
        "path": "/license/index.html",
        "meta_title": "License Terms — LaunchStatic",
        "meta_description": "LaunchStatic license terms for free MIT templates and paid Pro Template Pack. Permitted use, redistribution limits, and client work clarification.",
        "h1": "License Terms",
        "hero_lead": (
            "Free templates and paid packs follow different rules. Read this before you ship or resell."
        ),
        "nav_active": None,
        "sections": [
            {
                "type": "p",
                "text": (
                    "LaunchStatic publishes two categories of downloadable materials: "
                    "<strong>free MIT-licensed templates</strong> and <strong>paid commercial packs</strong>. "
                    "Confusing them creates legal risk for you and misrepresentation risk for us. This page "
                    "summarizes human-readable terms; the MIT License text in the repository remains the "
                    "authoritative license for free files. Paid purchases include a license confirmation "
                    "email that states your grant date and permitted uses."
                ),
            },
            {
                "type": "h2",
                "text": "Free templates (MIT License)",
            },
            {
                "type": "p",
                "text": (
                    "Files in <code>/downloads/</code>, <code>/demos/</code>, and the Free Static Landing "
                    "Kit are released under the MIT License unless marked otherwise. You may use, copy, "
                    "modify, merge, publish, distribute, sublicense, and sell copies of the software "
                    "subject to including the copyright notice and permission notice in substantial "
                    "portions of the source. You may deploy unchanged templates to unlimited domains."
                ),
            },
            {
                "type": "ul",
                "items": [
                    "Commercial products and client websites are allowed",
                    "Modification and rebranding are allowed",
                    "Redistribution of source is allowed with MIT notice preserved",
                    "No warranty — provided as-is per MIT standard language",
                ],
            },
            {
                "type": "h2",
                "text": "Pro Template Pack (commercial license)",
            },
            {
                "type": "p",
                "text": (
                    "The <a href=\"/pro-template-pack/\">Pro Template Pack</a> is <strong>not</strong> MIT. "
                    "One purchase grants a non-exclusive license to use the pack's source HTML/CSS/JS in "
                    "projects you build and operate. Typical permitted uses include your startup marketing "
                    "site, client deliverables where the client receives a built site (not the raw template "
                    "files), and internal agency starter kits kept private to your team."
                ),
            },
            {
                "type": "h3",
                "text": "Prohibited for paid pack source",
            },
            {
                "type": "ul",
                "items": [
                    "Reselling or sublicensing the unmodified or lightly modified pack as templates",
                    "Uploading pack files to ThemeForest, Gumroad clone shops, or free GitHub template repos",
                    "Sharing download links publicly or in community Discord files",
                    "Claiming authorship of the original LaunchStatic pack files",
                ],
            },
            {
                "type": "p",
                "text": (
                    "Built end products — the compiled experience users see in the browser — may be sold "
                    "and deployed without royalty. If your client asks for source, clarify contractually "
                    "whether they receive a site license only or broader rights. When in doubt, email "
                    "<a href=\"mailto:hello@launchstatic.dev\">hello@launchstatic.dev</a> before sharing files."
                ),
            },
            {
                "type": "h2",
                "text": "Site content and brand",
            },
            {
                "type": "p",
                "text": (
                    "Blog posts, tool guides, marketing copy on launchstatic.dev, and the LaunchStatic "
                    "name and logo styling are not covered by the MIT template license. Do not scrape "
                    "articles into AI training sets presented as your own work. Do not imply official "
                    "partnership or endorsement without written consent. Trademarks of third-party tools "
                    "mentioned in guides belong to their owners."
                ),
            },
            {
                "type": "h2",
                "text": "Services and deliverables",
            },
            {
                "type": "p",
                "text": (
                    "<a href=\"/done-for-you/\">Done-for-you</a> projects transfer repository ownership "
                    "to you per statement of work. Audit reports are licensed for your internal use; "
                    "reselling the report itself is not permitted. Custom code we write outside template "
                    "bases is yours unless otherwise agreed in writing."
                ),
            },
            {
                "type": "h2",
                "text": "Updates and termination",
            },
            {
                "type": "p",
                "text": (
                    "MIT files you already downloaded remain MIT even if we update site terms. Paid pack "
                    "licenses are perpetual for versions delivered at purchase; major new packs may require "
                    "a new purchase. We may terminate a license for breach — especially redistribution "
                    "violations — with notice when practical. Refund eligibility is described on the "
                    "<a href=\"/refund-policy/\">Refund Policy</a> page."
                ),
            },
            {
                "type": "h2",
                "text": "Agency and client work",
            },
            {
                "type": "p",
                "text": (
                    "Freelancers often ask whether they can use free MIT templates in client projects — "
                    "yes, with MIT notice preserved in source handoffs if required. For Pro Pack work, "
                    "the client may receive the built website without receiving pack source files unless "
                    "you have a multi-seat agreement confirmed in writing. White-label agencies building "
                    "dozens of sites per year should email us for volume clarification before assuming "
                    "one purchase covers unlimited brands."
                ),
            },
            {
                "type": "h2",
                "text": "Questions",
            },
            {
                "type": "p",
                "text": (
                    "Licensing for agencies, white-label shops, and multi-brand holdings varies. Describe "
                    "your use case in plain language and we will confirm in email. This page is not legal "
                    "advice; consult your counsel for high-stakes deployments. Related documents: "
                    "<a href=\"/terms.html\">Terms of Service</a>, "
                    "<a href=\"/licenses.html\">Third-party licenses</a>, and "
                    "<a href=\"/refund-policy/\">Refund Policy</a>. Free template MIT text is also "
                    "included in the repository root <code>LICENSE</code> file for offline reference."
                ),
            },
        ],
        "primary_cta": {
            "url": "/templates/",
            "button": "Free templates",
            "secondary_url": "/pro-template-pack/",
            "secondary_button": "Pro Pack",
        },
        "show_newsletter": False,
        "show_contact": True,
        "contact_title": "License questions",
    },
    {
        "path": "/refund-policy/index.html",
        "meta_title": "Refund Policy — LaunchStatic",
        "meta_description": "LaunchStatic refund policy for Pro Template Pack, Landing Page Audit, and Done-for-you services. Clear eligibility windows and how to request a refund.",
        "h1": "Refund Policy",
        "hero_lead": (
            "Straightforward rules for digital products and services. No hidden hoops."
        ),
        "nav_active": None,
        "sections": [
            {
                "type": "p",
                "text": (
                    "LaunchStatic sells digital templates and fixed-scope services. Because downloads "
                    "cannot be \"returned\" like physical goods, refunds are limited to specific situations "
                    "below. Read this before purchasing the "
                    "<a href=\"/pro-template-pack/\">Pro Template Pack</a>, booking a "
                    "<a href=\"/landing-page-audit/\">Landing Page Audit</a>, or depositing on "
                    "<a href=\"/done-for-you/\">Done-for-you</a> work. Free templates cost nothing — "
                    "no payment means no refund process."
                ),
            },
            {
                "type": "h2",
                "text": "Pro Template Pack ($49)",
            },
            {
                "type": "ul",
                "items": [
                    "<strong>Within 14 days</strong> of purchase if you have not downloaded the pack files — full refund.",
                    "<strong>Technical failure</strong> — if we cannot deliver a working download link within 5 business days after payment, full refund or alternate delivery at your choice.",
                    "<strong>Not eligible</strong> — after download, because digital goods are delivered instantly; or if license terms were violated (redistribution).",
                ],
            },
            {
                "type": "p",
                "text": (
                    "If you purchased by mistake before downloading, email "
                    "<a href=\"mailto:hello@launchstatic.dev\">hello@launchstatic.dev</a> immediately with "
                    "your receipt. We verify server logs and process eligible refunds within 10 business days "
                    "to the original payment method."
                ),
            },
            {
                "type": "h2",
                "text": "Landing Page Audit ($199)",
            },
            {
                "type": "ul",
                "items": [
                    "<strong>Before work starts</strong> — full refund if you cancel before we begin the review.",
                    "<strong>After delivery</strong> — refunds are not available once the report is sent; you received the contracted service.",
                    "<strong>Quality issue</strong> — if the report omits agreed scope items, we will complete the missing sections or offer a partial refund proportional to deficiency.",
                ],
            },
            {
                "type": "p",
                "text": (
                    "Audits measure opinionated best practices for static landing pages — not guaranteed "
                    "business outcomes. Dissatisfaction with recommendations that follow agreed scope is "
                    "not grounds for refund, but we welcome feedback to improve future reports."
                ),
            },
            {
                "type": "h2",
                "text": "Done-for-you (from $799)",
            },
            {
                "type": "ul",
                "items": [
                    "<strong>Before kickoff</strong> — deposit fully refunded if either party cancels before work begins.",
                    "<strong>After kickoff</strong> — deposit is non-refundable once customization starts; it covers scheduling and discovery.",
                    "<strong>Project cancellation mid-build</strong> — you receive work-in-progress files prorated to hours completed; remaining deposit balance refunded minus rush fees if any.",
                    "<strong>Our failure to deliver</strong> — if we miss a written milestone without renegotiation, you may cancel for refund of undelivered portion.",
                ],
            },
            {
                "type": "p",
                "text": (
                    "Scope documents sent before deposit list deliverables explicitly. Change requests "
                    "outside scope are quoted separately — approving them does not reopen refund windows "
                    "on completed work."
                ),
            },
            {
                "type": "h2",
                "text": "How to request a refund",
            },
            {
                "type": "ol",
                "items": [
                    "Email <a href=\"mailto:hello@launchstatic.dev\">hello@launchstatic.dev</a> with subject \"Refund request\".",
                    "Include purchase date, product name, payment reference, and reason.",
                    "We acknowledge within two business days and decide eligibility per this policy.",
                    "Approved refunds process within 10 business days to the original payment method.",
                ],
            },
            {
                "type": "h2",
                "text": "Chargebacks",
            },
            {
                "type": "p",
                "text": (
                    "Contact us before initiating a card chargeback. Chargebacks on delivered digital "
                    "goods may result in license revocation for paid packs and refusal of future service. "
                    "We provide documentation to payment processors when goods were delivered per scope."
                ),
            },
            {
                "type": "h2",
                "text": "Policy changes",
            },
            {
                "type": "p",
                "text": (
                    "We may update this page with a revised effective date. Purchases are governed by "
                    "the policy in effect at payment time. Material changes will not retroactively remove "
                    "refund rights you already qualified for."
                ),
            },
            {
                "type": "h2",
                "text": "EU and UK consumers",
            },
            {
                "type": "p",
                "text": (
                    "If mandatory consumer protection laws in your country provide withdrawal rights for "
                    "digital content, those laws may apply alongside this policy. Contact us with your "
                    "jurisdiction if unsure. We honor valid statutory rights regardless of this summary. "
                    "For privacy-related data deletion requests, see "
                    "<a href=\"/privacy.html\">Privacy Policy</a> and email "
                    "<a href=\"mailto:hello@launchstatic.dev\">hello@launchstatic.dev</a>."
                ),
            },
            {
                "type": "h2",
                "text": "Disputes and goodwill",
            },
            {
                "type": "p",
                "text": (
                    "Most issues resolve with a single email. If delivery failed due to our error, we "
                    "fix it or refund — your choice. We do not argue over good-faith misunderstandings "
                    "when you have not downloaded paid files or when audit scope was genuinely missed. "
                    "Abusive chargebacks on completed work may result in declined future service."
                ),
            },
            {
                "type": "h2",
                "text": "Free products",
            },
            {
                "type": "p",
                "text": (
                    "The Free Static Landing Kit and MIT templates cost $0 — there is nothing to refund. "
                    "If a download link breaks, report it via "
                    "<a href=\"mailto:hello@launchstatic.dev\">hello@launchstatic.dev</a> and we will "
                    "restore access or provide an alternate mirror. Donations and tips are not accepted "
                    "today; support us by citing LaunchStatic when helpful, not by sending payment for "
                    "free files."
                ),
            },
        ],
        "primary_cta": {
            "url": "mailto:hello@launchstatic.dev?subject=Refund%20request",
            "button": "Email refund request",
            "secondary_url": "/contact.html",
            "secondary_button": "Contact page",
        },
        "show_newsletter": False,
        "show_contact": True,
        "contact_title": "Refund support",
    },
]


def all_pages() -> list[dict]:
    return PAGES
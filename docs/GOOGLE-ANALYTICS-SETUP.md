# Google Analytics 4 — LaunchStatic Setup

## 1. Create GA4 property

1. Open [Google Analytics](https://analytics.google.com/)
2. Admin → Create property → name: **LaunchStatic**
3. Data stream → **Web** → URL: `https://launchstatic.pages.dev` (add `https://launchstatic.matchiq.co.kr` when live)
4. Copy **Measurement ID** (format `G-XXXXXXXXXX`)

## 2. Add Measurement ID to the site

Edit `assets/js/analytics-config.js`:

```javascript
window.LS_GA_MEASUREMENT_ID = 'G-YOUR_REAL_ID';
```

Deploy after changing:

```bash
npx wrangler pages deploy . --project-name=launchstatic --branch=main
```

## 3. How it works on LaunchStatic

- **Consent-first:** GA4 loads only after the visitor clicks **Accept** on the cookie banner.
- **Consent Mode v2:** Default `analytics_storage: denied` until accept.
- **Privacy defaults:** `anonymize_ip: true`, Google signals and ad personalization disabled in GA4 config.
- **Files:** `analytics-config.js` (ID), `analytics.js` (loader), `main.js` (banner handler).

## 4. Link Search Console (recommended)

1. [Google Search Console](https://search.google.com/search-console) → add property for your live URL
2. Analytics → Admin → Product links → **Search Console links** → Link
3. Submit `https://launchstatic.pages.dev/sitemap.xml` in GSC

## 5. Verify tracking

1. Visit the live site in an incognito window
2. Click **Accept** on the cookie banner
3. GA4 → Reports → Realtime — confirm 1 active user
4. Or use [Google Tag Assistant](https://tagassistant.google.com/)

## 6. AdSense path

GA4 data helps AdSense applications (traffic proof). Keep consent banner before analytics. Do not enable AdSense ad tags until approved.
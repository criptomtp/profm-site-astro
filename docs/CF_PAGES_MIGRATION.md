# Cloudflare Pages migration

Branch: `cf-pages-migration`

## Why

Vercel Hobby Auto DDoS Mitigation blocks the entire site when Claude Code's
dev traffic exceeds an undocumented threshold from a single residential IP.
No bypass exists on Hobby. Upgrading costs $20/mo for a fix that CF Pages
gives for free, with more edge locations covering Ukraine.

## What changed

- `functions/api/*.js` — 7 CF Pages Functions ported from `api/*.js`
  (Vercel Serverless Functions). Handler signature switched from
  `(req, res)` to `onRequest{Method}({ request, env })`.
- `public/_redirects` — generated from `vercel.json` by
  `scripts/convert-vercel-to-cf.mjs` (177 rules, 1:1 parity).
- `public/_headers` — CSP/HSTS/cache headers from `vercel.json`.
- `functions/api/_crypto.js` — Web Crypto PBKDF2 replaces Node `scrypt`
  (scrypt does not exist in CF Workers runtime).

## What did NOT change

- Any `src/` code. Zero Astro component changes.
- `astro.config.mjs`. Build output (`dist/`) is identical.
- URLs, canonical tags, hreflang, sitemap, robots.txt, schema.org.
- Telegram delivery, CRM logic, GSC sync, admin auth flow.

## Vercel still runs

`main` branch is unchanged. Vercel continues to serve production until
DNS is cut over. Deploying `cf-pages-migration` to CF Pages gives a
`fulfillmentmtp.pages.dev` preview URL that can be tested end-to-end
before flipping DNS.

## CF Pages project setup (user steps)

1. Dashboard → Workers & Pages → Create → Pages → Connect to Git
2. Select `profm-site-astro` repo, branch `cf-pages-migration`
3. Build settings:
   - Framework preset: Astro
   - Build command: `npm run build`
   - Build output: `dist`
   - Root directory: (leave empty)
4. Environment variables — copy from Vercel Project Settings:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `KV_REST_API_URL` (Upstash Redis REST endpoint)
   - `KV_REST_API_TOKEN`
   - `LEADS_API_KEY`
   - `ADMIN_PASSWORD`
   - `GSC_CLIENT_ID`, `GSC_CLIENT_SECRET`, `GSC_REFRESH_TOKEN`
   - `WEB3FORMS_KEY` (optional)
5. Deploy. First build takes ~3-5 min.

## Smoke tests on preview URL

Before DNS cutover, verify on `fulfillmentmtp.pages.dev`:

- [ ] Homepage loads, all 3 languages (`/`, `/ru/`, `/en/`)
- [ ] Pick 10 random redirects, test each returns 301 to correct target
- [ ] Hero CTA form submits → Telegram message arrives
- [ ] CRM login with admin password works (first login re-hashes legacy
      password from scrypt to PBKDF2 automatically if stored password
      matches `ADMIN_PASSWORD` env value)
- [ ] `/api/gsc` returns JSON
- [ ] PageSpeed on preview URL: Performance ≥ 85 mobile, SEO 100

## DNS cutover (when preview is green)

1. Lower DNS TTL at registrar to 300s (do this 24h before cutover)
2. CF Pages → Custom domains → Add `www.fulfillmentmtp.com.ua`
   and `fulfillmentmtp.com.ua`
3. Update registrar nameservers OR update A/CNAME records to point
   at CF Pages values shown in dashboard
4. Wait for propagation (typically 5-30 min with low TTL)
5. Test: `curl -sI https://www.fulfillmentmtp.com.ua/` should show
   `server: cloudflare` instead of `server: Vercel`
6. Monitor GSC for 48h. Roll back by reverting DNS if anything drops.

## Rollback

DNS revert = instant rollback. No code changes needed.

## Scrypt password migration

CF Workers cannot verify Node scrypt hashes (`salt:hash` format with
64-byte hash). The auth handler detects legacy hashes and:

- If user is `admin` AND `ADMIN_PASSWORD` env var matches the entered
  password → re-hashes to PBKDF2 and logs in.
- For non-admin users with scrypt hashes → returns 403 with message
  asking admin to reset via `update_user` action.
- Plain-text legacy passwords → hashed to PBKDF2 on first successful
  login (existing migration path preserved).

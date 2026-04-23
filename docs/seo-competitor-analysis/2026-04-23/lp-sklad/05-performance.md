# lp-sklad.online — Core Web Vitals & Performance Audit

**Date:** 2026-04-23
**Target:** https://lp-sklad.online
**Method:** Lighthouse 12 (local, simulate throttling) — PSI API daily quota exhausted, CrUX API requires registered key. Lab data used as proxy for CWV; field data unavailable without CrUX key.
**Tool versions:** Lighthouse 12.x via `npx lighthouse@12`, Chrome headless.

---

## 1. Site shape — what is actually public

lp-sklad.online is a gated SaaS for fulfillment/warehouse (Yii2 PHP framework, "advanced" template). Only **two URLs are publicly reachable** without auth:

| URL | Type | Status |
|---|---|---|
| `/` | Marketing landing page | 200, full SPA-like single page |
| `/site/login` | Auth form | 200 |

Everything else (`/about`, `/pricing`, `/services`, `/cabinet`, `/site/signup`, `/tariffs`, `/uslugi` …) → **302 → `/site/login`**. The sitemap-style `/sitemap.xml` redirects (302) into the login flow. No blog, no service pages, no editorial content indexed. Probed 10 candidate URLs — all gated.

**SEO implication:** lp-sklad has exactly **one landing page's worth of crawlable surface**. Scope of this perf audit is therefore narrower than a normal competitor — we measured `/` and `/site/login`, which is the entire public site.

---

## 2. Core Web Vitals — Lab Measurements

### Mobile

| Page | Perf Score | FCP | LCP | CLS | TBT | TTFB | SI | Bytes |
|---|---|---|---|---|---|---|---|---|
| `/` (home) | **93 / 100** | 2.02 s | **2.88 s** ⚠ | **0.031** ✅ | 0 ms ✅ | 118 ms ✅ | 2.02 s | 891 KiB |
| `/site/login` | **78 / 100** | 3.23 s | **4.00 s** ✗ | **0.000** ✅ | 0 ms ✅ | 113 ms ✅ | 251 KiB |

### Desktop

| Page | Perf Score | FCP | LCP | CLS | TBT | TTFB | SI | Bytes |
|---|---|---|---|---|---|---|---|---|
| `/` (home) | **98 / 100** | 0.72 s | **1.05 s** ✅ | **0.004** ✅ | 0 ms ✅ | 190 ms ✅ | 0.75 s | 891 KiB |
| `/site/login` | **99 / 100** | 0.71 s | **0.71 s** ✅ | **0.000** ✅ | 0 ms ✅ | 126 ms ✅ | 0.71 s | 251 KiB |

### Core Web Vitals verdict (mobile, 75p lab proxy)

| Metric | Home Mobile | Login Mobile | Threshold |
|---|---|---|---|
| LCP | 2.88 s — **Needs Improvement** | 4.00 s — borderline **Poor** | ≤2.5 s Good |
| INP | n/a (no interactions measured in lab; TBT = 0 ms suggests clean main thread) | n/a (TBT 0 ms) | ≤200 ms Good |
| CLS | 0.031 — **Good** | 0.000 — **Good** | ≤0.1 Good |
| TTFB | 118 ms — **Good** | 113 ms — **Good** | ≤200 ms target |
| FCP | 2.02 s — borderline | 3.23 s — Poor | ≤1.8 s Good |

**Summary**: CLS and INP are not problems. LCP is the single failing metric on mobile. The home barely misses "Good" (2.88 s vs 2.5 s). The login page misses badly (4 s) and that is the conversion gateway for every logged-out user.

INP could not be measured in lab (no interaction trace); TBT = 0 ms across all 4 runs strongly suggests INP will be well under 200 ms — the JS payload is light and mostly inert jQuery/Bootstrap.

---

## 3. LCP breakdown (home mobile)

**LCP element:** `div.landing-grid > div.hero-visual > div#openVideoBtn > img.img-responsive` — a hero video-thumbnail image.

**LCP subparts (2.88 s total, mobile simulate):**
- TTFB: 600 ms (21%)
- **Resource Load Delay: 1,429 ms (50%)** ← the fix target
- Resource Load Time: 308 ms (11%)
- Element Render Delay: ~540 ms (~19%)

50% of LCP is spent waiting for the browser to discover the image, because render-blocking CSS blocks resource discovery. Root cause is render-blocking stylesheets (see §5) — not the image itself.

---

## 4. Infrastructure / stack fingerprint

| Facet | Value | Signal |
|---|---|---|
| Server | `nginx/1.24.0` | Modern nginx, self-hosted |
| HTTP version (origin) | **HTTP/1.1** | No HTTP/2, no HTTP/3 on lp-sklad.online itself |
| CDN | **None detected** in front of origin | No Cloudflare/Vercel/Fastly headers; single-host direct |
| TLS | Yes (standard nginx) | — |
| CMS / framework | **Yii2** (PHP) — `yii.js`, `advanced-frontend` session cookie, `_csrf-frontend` token | Custom SaaS, not WordPress |
| Front-end | jQuery, Bootstrap 3/4 era (`bd4c439a/css/bootstrap.css`), select2, daterangepicker, moment.min.js | Legacy jQuery stack |
| Analytics | Umami (self-hosted `unami.top`, HTTP/3) | Privacy-friendly, good |
| Fonts | Google Fonts (Montserrat, Unbounded) via fonts.googleapis.com | Render-blocking |
| External hosts | `cdn.jsdelivr.net`, `select2.github.io`, `images.unsplash.com`, `fonts.gstatic.com`, `unami.top` | 6 third-party origins on a landing page |

**Protocol mix on page `/` (42 requests):**
- lp-sklad.online origin: **HTTP/1.1 only** (33 requests) ← biggest infra weakness
- Google Fonts / jsdelivr / select2.github.io: h2
- Google Fonts .woff2 (fonts.gstatic.com): h3
- Unsplash images: h2
- Umami: http/1.1

**Cookie leak:** `_csrf-frontend` cookie is set on the public landing — app code is bleeding into the marketing page.

---

## 5. Bundle & asset analysis (home)

**Total transfer: 891 KiB / 42 requests**

| Resource type | Size | Notes |
|---|---|---|
| Images | 527.7 KiB | Dominant payload |
| Script | 170.4 KiB | jQuery + yii.js + daterangepicker + moment + select2 + my.js + productAccounting.js |
| Font | 136.2 KiB | 4 woff2 from gstatic |
| Stylesheet | 39.5 KiB | 6 CSS files, all render-blocking |
| Document (HTML) | 12.3 KiB | Small, fine |

### Images
- **No WebP, no AVIF** on first-party images. All JPG/PNG. (Unsplash hero delivers AVIF, but that's 3rd-party.)
- Lighthouse estimated savings from modern formats: **333 KiB** (37% of page weight)
- Lighthouse estimated savings from proper responsive sizing: **365 KiB**
- Top image: 93.7 KiB unsplash.com photo (AVIF)
- Integration logos (lp_crm.jpg 80.8 KiB, salesdrive.jpg 57.6 KiB, 6 others ~35–56 KiB each) are oversize JPGs delivered at small display size

### CSS — 6 render-blocking stylesheets
| URL | Size | Wasted ms |
|---|---|---|
| `fonts.googleapis.com/css2?family=Montserrat…` | 1 KiB | 871 ms |
| `/assets/…/bootstrap.css` | 28 KiB | 1068 ms |
| `/css/daterangepicker.css` | 2 KiB | 653 ms |
| `select2.github.io/…/select2-bootstrap.css` | 4 KiB | 784 ms |
| `/css/site.css` | 1 KiB | 653 ms |
| `cdn.jsdelivr.net/…/select2.min.css` | 3 KiB | 780 ms |

**Render-blocking total impact: ~760 ms** (Lighthouse estimate). Every single CSS file blocks the critical path. daterangepicker and select2 are admin-panel controls — they have no business on the public landing page.

### JS
- Unused JS savings: 67 KiB (est)
- Unused CSS savings: 27 KiB (est)
- No deferred/async on most scripts; `defer` only on Umami analytics.
- `jquery.js + yii.js + moment.min.js + daterangepicker.js + select2.min.js + my.js + productAccounting.js` — a classic 2015-era stack shipped to everyone who lands on the marketing page.

### DOM
- Home: 318 elements — fine (<1500 threshold)
- Login: 58 elements — tiny

---

## 6. Why login page is slower than home (mobile)

Login perf score is 78 vs home's 93 despite being 1/4 the bytes. Reasons:
1. LCP element on login is delayed by the same render-blocking CSS chain.
2. Login triggers an extra CSRF cookie + session cookie round-trip.
3. Speed Index is 5.08 s on login vs 2.02 s on home — the hero (blank white form card) renders late because Bootstrap + select2 CSS load first.
4. No above-the-fold content optimization — login form is a card centered in the viewport, so LCP is the card background/button rendering after all CSS is parsed.

---

## 7. Bottleneck ranking (impact × effort)

| # | Bottleneck | Impact | Effort | Recommendation |
|---|---|---|---|---|
| 1 | **Render-blocking CSS chain (6 files)** | Very High — adds ~1.4 s to LCP load-delay | Low | Inline critical CSS; defer bootstrap/select2/daterangepicker (the latter two not needed on `/` at all — drop them) |
| 2 | **No HTTP/2 on origin** | High — 33 requests serialized over HTTP/1.1 on single domain | Medium | Enable `listen 443 ssl http2` in nginx (one-line nginx change) |
| 3 | **No CDN in front of origin** | High — single-origin serving static assets | Medium | Put Cloudflare free tier in front — one-hour DNS change, instant HTTP/2+3, caching, Brotli |
| 4 | **Images not in WebP/AVIF** | High — 333 KiB savings (37% of page) | Low | Convert `/logo/integrations/*.jpg` to WebP, serve via `<picture>` |
| 5 | **Images not responsive-sized** | High — 365 KiB savings | Low | Serve integration logos at display resolution (not 1:1 full-size) |
| 6 | **Legacy jQuery + bootstrap + moment.js on landing** | Medium — 170 KiB of JS for a static marketing page | High | Extract marketing landing out of the Yii2 frontend app — serve a static page (Astro, or plain HTML) from a separate subdirectory |
| 7 | **Google Fonts CSS render-blocking** | Medium — 871 ms wasted | Low | Use `font-display: swap` + self-host woff2 + preload |
| 8 | **Cookies + CSRF on landing** | Low perf, High hygiene | Low | Marketing page should be cookie-free / cacheable at CDN edge |
| 9 | **daterangepicker + select2 on `/`** | Medium | Low | Load these only on pages that need them (authenticated order forms) |

---

## 8. Does fast load contribute to AI citation?

**Yes, indirectly — and this is where lp-sklad is double-penalized.**

AI search systems (Perplexity, ChatGPT Search, Google AI Overviews, Claude search) use their own crawlers (PerplexityBot, OAI-SearchBot, GPTBot, ClaudeBot) that:
- Time out faster than Googlebot — typically ~5–10 s budgets per page
- Skip pages where main content is behind auth / JS
- Prefer pages with clean HTML + fast TTFB because they process at scale
- Prefer HTTP/2+ origins (fewer connection hangs in bulk crawling)

lp-sklad.online is hit by **two separate problems** for AI citation:
1. **Surface:** only one page (`/`) is crawlable — the entire "knowledge" of the company is gated. AI bots cannot read pricing, services, FAQs, case studies because everything 302s to login. There's literally nothing to cite.
2. **Speed on that one page:** LCP 2.88 s mobile and render-blocking CSS mean the page is on the slow end; TTFB 600 ms in LCP waterfall means the origin is slow. Not disqualifying for AI crawlers, but not a positive signal.

For AI citation, (1) is the decisive problem, (2) is secondary. Even if they fix perf to 100/100, there's still only one URL to cite. MTP has 120+ crawlable pages by contrast.

---

## 9. MTP vs lp-sklad — head-to-head

Recent MTP (from similar audits, `fulfillmentmtp.com.ua` on Vercel edge + Cloudflare DNS):

| Metric | MTP (home, mobile) | lp-sklad (home, mobile) | Winner |
|---|---|---|---|
| Perf score | 90–95 (recent PSI runs post-font-preload) | 93 | Tie |
| LCP | ~2.1–2.4 s | 2.88 s | **MTP ahead** |
| CLS | ~0.02–0.05 | 0.031 | Tie |
| TBT | ~50–150 ms | 0 ms | **lp-sklad ahead** (smaller JS) |
| TTFB | ~80–150 ms (Vercel edge) | 118 ms | Tie |
| HTTP version | h2/h3 (Vercel) | **h1.1** | **MTP ahead** |
| CDN | Vercel + CF DNS | None | **MTP ahead** |
| Image format | WebP primary | JPG/PNG | **MTP ahead** |
| Crawlable pages | 120+ (UA/RU/EN) | 2 (home + login) | **MTP massively ahead** |
| Dual-MD (AI-friendly `.md` twin) | Yes | No | **MTP ahead** |
| Render-blocking CSS | 2–3 (fonts + base) | 6 | **MTP ahead** |

**Net: MTP is decisively ahead on infrastructure, image optimization, and — most importantly — crawlable surface for AI citation. lp-sklad's only advantage is a lean JS bundle (0 ms TBT) because it's a near-static Yii2 landing. That advantage evaporates the moment their render-blocking CSS chain is considered.**

lp-sklad is not a performance threat to MTP. Their weakness is strategic: the whole site is a gated SaaS funnel, and they rely on paid traffic / referrals to push users into the login, not on SEO or AI citation.

---

## 10. Recommendations for MTP (things to keep/strengthen)

- Keep Vercel edge + Cloudflare stack — lp-sklad has no equivalent.
- Keep dual-MD integration — lp-sklad has zero AI-crawlable surface.
- Continue image pipeline (WebP + dimensions) — lp-sklad gifts us 30%+ page-weight advantage on comparable pages.
- Monitor LCP on 3 pillar pages quarterly — our ongoing font preload work (commit `095da3d`) is the right direction.

## 11. Data sources & caveats

- PSI API returned HTTP 429 "quota exceeded for anonymous daily limit" — results above are from **local Lighthouse 12** with `--throttling-method=simulate`. Lab ≠ field. CrUX field data would require a registered Google Cloud API key (not configured in this repo). Recommend storing a `PSI_KEY` in env for future audits — script `scripts/psi-audit.sh` already supports it.
- INP cannot be measured in lab without user traces; TBT = 0 ms is the best available proxy (strong suggestion that INP is "Good" for lp-sklad).
- Results are single-run; production field data (CrUX 28-day) could differ ±15%.

## Raw Lighthouse JSON
- `/tmp/lh-lp-sklad/mobile-home.json`
- `/tmp/lh-lp-sklad/desktop-home.json`
- `/tmp/lh-lp-sklad/mobile-login.json`
- `/tmp/lh-lp-sklad/desktop-login.json`

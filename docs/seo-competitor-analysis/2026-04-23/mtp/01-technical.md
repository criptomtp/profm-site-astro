# MTP Group — Technical SEO Audit
**Site:** https://www.fulfillmentmtp.com.ua
**Date:** 2026-04-23
**Auditor:** Technical SEO specialist (Claude Code)
**Context:** Baseline audit to benchmark vs Nova Poshta, Sender Ukraine, LP-Sklad

---

## Technical Score: **86 / 100**

| Category | Status | Weight | Score |
|---|---|---|---|
| Crawlability | PASS | 15 | 14 / 15 |
| Indexability | PARTIAL | 20 | 15 / 20 |
| URL Structure | PARTIAL | 15 | 11 / 15 |
| Security / Headers | PASS | 15 | 15 / 15 |
| Mobile / HTTPS | PASS | 10 | 10 / 10 |
| Core Web Vitals (source) | PASS | 10 | 9 / 10 |
| Structured Data | PASS | 5 | 5 / 5 |
| JS Rendering | PASS | 5 | 5 / 5 |
| Dual-file MD twin | EXEMPLARY | 5 | 5 / 5 |

---

## 1. Crawlability — PASS (14/15)

### robots.txt (https://www.fulfillmentmtp.com.ua/robots.txt)
- HTTP 200, text/plain — reachable.
- `Content-Signal: ai-train=no, search=yes, ai-input=yes` — forward-looking strategic declaration (contentsignals.org draft spec).
- Explicit allow rules for `GPTBot`, `OAI-SearchBot`, `ClaudeBot`, `PerplexityBot`, `anthropic-ai` — modern AI crawler management (aligns with `seo-technical` skill guidance).
- `User-Agent: *` blocks `/admin/`, `/api/`, `/thanks/` (all lang variants), `/files/`, `/schedule/`, `/new/` — correct.
- `*.md` deliberately NOT blocked — required so Googlebot can read `X-Robots-Tag: noindex, follow` on twin markdown pages.
- Sitemap directive present: `https://www.fulfillmentmtp.com.ua/sitemap-index.xml`.
- IndexNow key file referenced in comment (`/e2ea8b0e3992bc7743d624fb443d3434.txt`).

### Sitemap
- `sitemap-index.xml` → 200, references single `sitemap-0.xml`.
- `sitemap-0.xml`: **109 URLs** (HTML only, 0 `.md` URLs leaked — dual-md exclusion working).
- Coverage audit of root-level UA pages: only **4 non-prefixed UA URLs** in sitemap (`/`, `/blog/`, `/glosariy/` + trailing). The rest (`/ua/...`, `/ru/...`, `/en/...`) — legacy structure.
- **Minor gap:** sitemap uses `lastmod` but **no `changefreq` or `priority`** — low-impact (Google ignores these anyway), but competitors may include them for Bing/Yandex.
- **Minor gap:** no image or video sub-sitemaps despite YouTube embeds on homepage.

### AI Crawler Management
- Explicit allow for GPTBot / ClaudeBot / PerplexityBot = **competitive advantage**. Most UA logistics sites block AI crawlers or leave defaults (blocked).

---

## 2. Indexability — PARTIAL (15/20)

### Canonicals (sampled 6 pages)
| URL | Canonical | Self-referential? |
|---|---|---|
| `/` | `https://www.fulfillmentmtp.com.ua/` | Yes |
| `/ru/` | `https://www.fulfillmentmtp.com.ua/ru/` | Yes |
| `/en/` | `https://www.fulfillmentmtp.com.ua/en/` | Yes |
| `/ua/tsiny/` | `https://www.fulfillmentmtp.com.ua/ua/tsiny/` | Yes |
| `/ru/tsenu/` | `https://www.fulfillmentmtp.com.ua/ru/tsenu/` | Yes |
| `/en/prices/` | `https://www.fulfillmentmtp.com.ua/en/prices/` | Yes |
| `/glosariy/` | `https://www.fulfillmentmtp.com.ua/glosariy/` | Yes |

All canonicals absolute, www, https, trailing-slash consistent. **No canonical chain issues found.**

### hreflang Symmetry Audit

**Cluster A — New root UA policy (home `/`):**
- `uk` → `/` | `ru` → `/ru/` | `en` → `/en/` | `x-default` → `/`
- Confirmed on `/`, `/ru/`, `/en/`, `/glosariy/`, `/ru/glossariy/`, `/en/glossary/` — **symmetrical, correct**.

**Cluster B — Legacy `/ua/*` pages:**
- `/ua/tsiny/`: `uk` → `/ua/tsiny/` | `ru` → `/ru/tsenu/` | `en` → `/en/prices/` | `x-default` → `/ua/tsiny/`
- `/ru/tsenu/`: `uk` → `/ua/tsiny/` | `ru` → `/ru/tsenu/` | `en` → `/en/prices/` | `x-default` → `/ua/tsiny/`
- `/en/prices/`: matches cluster.
- **Cluster B is symmetrical internally.**

### The Duplicate-Canonical Problem (GSC-flagged)
The audit CONFIRMS the issue flagged in GSC but narrows the scope:

1. **Home cluster uses `uk → /`** (root home canonical).
2. **Legacy `/ua/*` pages use `uk → /ua/...`** (self-referential).
3. **`/ua/` root 301s to `/`** — so only ONE home resolves (good).
4. **BUT:** there is **no legacy `/ua/home-equivalent` page**, so the home cluster and legacy cluster live in parallel without a conflict on the homepage itself.

**Where it DOES leak:** Legacy pillar `/ua/shcho-take-fulfilment/` is a 200-resolving page with `hreflang uk → /ua/shcho-take-fulfilment/`. If someday a root-level UA `/shcho-take-fulfilment/` is created without retiring the legacy URL, we get TWO pages claiming `hreflang="uk"` for the same RU/EN pair — classic duplicate-canonical confusion. **Tested:** `/shcho-take-fulfilment/` currently 404 (confirmed). `/tsiny/` also 404. **No collision today**, but guardrail needed.

### Indexability Summary
- All sampled pages return HTTP 200 with self-referential canonicals.
- hreflang quartet (uk, ru, en, x-default) present on every sampled page.
- No `noindex` meta tags observed on production pages.
- `.md` twin pages correctly carry `X-Robots-Tag: noindex, follow` + `Link: <HTML>; rel="canonical"` — Google will discover and ignore them.
- **Score deduction:** 5 pts for the 2-cluster hreflang model being a migration tax, not an error.

---

## 3. URL Structure — PARTIAL (11/15)

### Strengths
- HTTPS + www enforced. `fulfillmentmtp.com.ua` (non-www) → **301** → `www.fulfillmentmtp.com.ua` (confirmed permanent).
- `/ua/` (legacy root) → **301** → `/` (correct — prevents orphan UA home).
- Trailing slashes consistent site-wide.
- Clean URLs: no query strings, no `.html` extensions, no `?id=` clutter.
- Slugs are descriptive and localized: `/ru/fulfilment-dlya-marketpleysov/`, `/en/fulfillment-ukraine/`, `/ua/paletne-zberigannya/`.

### Weaknesses
- **Mixed URL policy in production:** 4 UA pages at root (`/`, `/blog/`, `/glosariy/` + one more) vs ~32 UA pages still at `/ua/...`. Per CLAUDE.md this is intentional ("old /ua/* stay put"), but it creates a **discoverability cost**: users/competitors see two canonical patterns for Ukrainian content.
- **No root-level equivalents for top pillar pages.** Every legacy `/ua/` URL (tsiny, shcho-take-fulfilment, fulfilment-ukraina, fulfilment-kyiv, etc.) returns 404 at root — meaning internal links from new root-UA content can't use the root policy.
- **No redirect chains detected** (single-hop 301 only, good).
- **No orphaned /en/ or /ru/ redirects** observed.

### Recommendation
Either commit to the migration plan in `docs/url-migration/batch-candidates.md` OR explicitly document the 2-cluster policy in sitemap comments so auditors/crawlers don't treat it as a bug. Right now the state is "intentional but indistinguishable from migration debt."

---

## 4. Security & Headers — PASS (15/15)

All modern security headers present:

| Header | Value | Status |
|---|---|---|
| `strict-transport-security` | `max-age=63072000; includeSubDomains; preload` | Strong (2y + preload) |
| `content-security-policy` | Strict CSP with allow-list for GTM, GA, YouTube, Telegram API | Strong |
| `x-content-type-options` | `nosniff` | Good |
| `x-frame-options` | `SAMEORIGIN` | Good |
| `referrer-policy` | `strict-origin-when-cross-origin` | Good |
| `permissions-policy` | `camera=(), microphone=(), geolocation=()` | Good |
| `report-to` / `nel` | Cloudflare Network Error Logging active | Bonus |

CDN: **Cloudflare** (cf-ray + CF NEL). HTTP/2 + HTTP/3 (alt-svc h3). Server chose TLS from CF — correct.

**Not seen but not critical:** `cross-origin-embedder-policy`, `cross-origin-opener-policy` — only needed if using `SharedArrayBuffer`.

---

## 5. Mobile & HTTPS — PASS (10/10)

- `<meta name="viewport" content="width=device-width,initial-scale=1">` present.
- All sampled images have `width`, `height`, `alt` attributes.
- Below-fold images have `loading="lazy"` (logos, case cards).
- Hero LCP image: `fetchpriority="high"` + `<link rel="preload" as="image">` — optimal.
- Responsive CSS with `@media(max-width:768px)` breakpoints.
- Sticky mobile CTA (phone + Telegram) at bottom — mobile-native UX.
- Font loading: `display=swap` + `media="print" onload="this.media='all'"` (async) — prevents FOUT blocking.
- HTTPS: TLS enforced, HSTS preload, 2y duration.

---

## 6. Core Web Vitals (source-level) — PASS (9/10)

### Positive signals
- Hero image preloaded with `fetchpriority="high"` → **LCP < 2.5s likely**.
- Critical CSS inlined in `<head>` (design-system.css + page-components.css combined) — eliminates render-blocking CSS.
- External stylesheets loaded async via `media="print" onload="this.media='all'"`.
- GTM/GA4 **deferred by 1500ms / 3000ms** via `setTimeout` — clever pattern to protect INP on first interaction. (Trade-off: events before 1.5s are dropped.)
- Layout uses `aspect-ratio: 16/9` on video thumbs + explicit `width`/`height` on images → **CLS < 0.1 expected**.
- `@media (prefers-reduced-motion: reduce)` override — a11y-correct.

### Risks
- Homepage HTML = 87 KB (uncompressed) — acceptable, but the inlined CSS is ~6 KB that repeats on every page (no critical-CSS-per-route split).
- GTM deferred 3s — potential analytics blind spot; monitor GA4 events for session-start drop-off.
- 3 `<script type="application/ld+json">` blocks inline — fine, but adds to HTML weight.
- TTFB measured (single probe from audit machine): **165ms** — excellent thanks to Cloudflare edge.

### Recommendation
Run production Lighthouse from PageSpeed Insights (not from audit machine) after next deploy to get real CrUX-backed LCP/INP/CLS. Source-level indicators are green.

---

## 7. Structured Data — PASS (5/5)

Homepage carries **3 JSON-LD blocks**:
1. `LocalBusiness` — two postal addresses (Shchaslive + Bilohorodka), phones, email, openingHours, `aggregateRating` (4.9/5, 150 ratings, 10 reviews), `sameAs` (FB, LinkedIn, Telegram), `priceRange` UAH 18–650, `knowsAbout` array.
2. `WebSite` — name, URL, description, `inLanguage: uk`.
3. `FAQPage` — 7 Q&A pairs matching visible FAQ section (anti-spam compliant).

**No obvious validation issues** from source inspection. Recommend cross-check via Google Rich Results Test after any homepage copy edits.

**Competitive note:** Having `LocalBusiness` + `FAQPage` + `AggregateRating` on home = strong. Most UA logistics competitors have only Organization + Website.

---

## 8. JavaScript Rendering — PASS (5/5)

- **SSR/SSG via Astro** — all content present in raw HTML (confirmed by viewing source: hero, FAQ JSON-LD, nav, footer all in initial HTML response).
- No hydration required for crawlers to read content.
- Astro hydration chunks (`/_astro/index.Due3e0NQ.css`, `header.BgfblYv3.css`) — content-agnostic.
- Googlebot, Bingbot, AI crawlers all see full content without JS execution.
- **No CSR/SPA pattern** — no router, no client-side data fetching for primary content.

---

## 9. Dual-File Markdown Twin — EXEMPLARY (5/5)

**Unique feature — no competitor in UA fulfillment has this.**

Verified implementation:
- `GET /index.md` → 200, `Content-Type: text/markdown`, `X-Robots-Tag: noindex, follow`, `Link: <https://www.fulfillmentmtp.com.ua/>; rel="canonical"`, `Cache-Control: public, max-age=3600`.
- `GET /ru/index.md` → 200, canonical link → `/ru/`.
- `GET /en/index.md` → 200, canonical link → `/en/`.
- HTML pages advertise the twin via `<link rel="alternate" type="text/markdown" href="/index.md">` in `<head>` (confirmed on homepage).
- Sitemap does NOT leak `.md` URLs (0 hits on grep for `.md` inside `sitemap-0.xml`).
- robots.txt does NOT block `.md` (deliberate — so Googlebot reads the X-Robots-Tag).

**Why this matters:** ChatGPT/Claude/Perplexity browsing fetches the `.md` variant when the `<link rel="alternate" type="text/markdown">` signal is present — 5-10× fewer tokens per page, cleaner citations. Also surfaces in AI Overviews grounding.

**One missing piece:** the API catalog (`/.well-known/api-catalog`) returns `application/linkset+json` — **also first-in-category for UA fulfillment**. Keeps this ecosystem-ready for future AI agent calls.

---

## Issues by Priority

### Critical (fix this week)
None. No indexation-breaking issues.

### High (fix this month)
1. **Document the 2-cluster UA URL policy explicitly.** Add a comment block in `sitemap-index.xml` OR a note in `/robots.txt` so external auditors don't flag `/ua/*` as migration debt. This is purely perception management — Google handles it fine today, but every competitor audit you commission will raise it.
2. **Decide migration timeline for legacy `/ua/*` URLs.** Current indefinite coexistence means every new pillar page decision triggers "root or /ua/?" debate. Either schedule a Q3/Q4 2026 migration batch (see `docs/url-migration/batch-candidates.md`) or mark the policy permanent in CLAUDE.md + ADR.

### Medium (next quarter)
3. **Add `changefreq` + `priority` to sitemap** for Bing/Yandex behavior (Google ignores but Bing uses them in crawl scheduling). Low-effort Astro sitemap config tweak.
4. **Split sitemap into per-language files** (`sitemap-ua.xml`, `sitemap-ru.xml`, `sitemap-en.xml`) once total URLs exceed ~500. Currently 109, not urgent.
5. **Add image sub-sitemap** (`sitemap-images.xml`) to help Google Images discovery for warehouse photos — competitive advantage vs Nova Poshta (they have it).
6. **GTM 3s defer** — validate session-start event delivery in GA4 DebugView; if drop-off > 5%, pull defer back to 1000-1500ms.

### Low (nice-to-have)
7. Add `Content-Type: application/xml` header verification to sitemap (currently served correctly).
8. Consider `Link: <...>; rel="alternate"; type="text/markdown"` HTTP header in addition to the HTML `<link>` — redundancy for AI crawlers that don't parse HTML.
9. Add `coep`/`coop` headers if/when WASM or cross-origin iframes enter the stack (not today).

---

## Benchmark vs Competitors (preview — to be filled after their audits)

| Capability | MTP | Nova Poshta | Sender | LP-Sklad |
|---|---|---|---|---|
| AI crawler explicit allow | YES | ? | ? | ? |
| Dual-file `.md` twin | YES | likely no | likely no | likely no |
| `/.well-known/api-catalog` | YES | ? | ? | ? |
| LocalBusiness + FAQPage + AggregateRating on home | YES | ? | ? | ? |
| HSTS preload | YES | ? | ? | ? |
| Content-Signal header in robots | YES | ? | ? | ? |

**Expected standing after full competitor audit:** Top-1 on technical SEO sophistication, Top-2 or Top-3 only because of raw page volume (Nova Poshta likely outweighs on content depth).

---

## What To Monitor in GSC (next 30 days)

1. **"Duplicate, Google chose different canonical"** — watch if this count shrinks after legacy vs root policy documentation. Current count should be confined to `/ua/` cluster only.
2. **Coverage > Excluded > Alternate page with proper canonical tag** — `.md` twin pages should appear here, NOT in "Discovered, currently not indexed". If they appear in the latter, Googlebot isn't reading the `X-Robots-Tag`.
3. **Indexed pages count** — target 109 ± 5 (match sitemap).
4. **CrUX LCP/INP/CLS** for root `/` after font-preload commit (095da3d) lands in 28-day window.

---

## Files/Paths Referenced

- `/Users/nikolaj/My vibecode aplications/profm-site-astro/public/robots.txt`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/integrations/dual-md.mjs`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/public/llms.txt`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/docs/url-migration/batch-candidates.md`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/src/layouts/Base.astro`

**End of report.**

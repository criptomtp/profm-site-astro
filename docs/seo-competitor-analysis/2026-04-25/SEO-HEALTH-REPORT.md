# SEO Health Report — fulfillmentmtp.com.ua

**Audit date:** 2026-04-25
**Baseline:** 2026-04-23
**Business type detected:** Local Service / 3PL Fulfillment Provider (UA)
**Scope:** 122 pages, 256 JSON-LD blocks, 108 dual-md twins, 3 languages (UA/RU/EN)

---

## TL;DR

**SEO Health Score: 88 / 100** (▲ +7 vs 04-23 baseline 81/100)

Six remediation batches (A → F) shipped between 04-23 and 04-25 closed the largest gaps from the prior audit (orphan AggregateRating, AI crawler robots, llms.txt spec compliance, image sitemap, sitemap priority ladder, datePublished + Person + author bylines). Schema is the standout (+18 points). Performance is mixed: UA home jumped from 74 → 93 mobile (font preload win), but EN home and the UA pillar still fail mobile LCP (>5s). Content E-E-A-T improved modestly via 3 pillar pages + EDRPOU on About, but Footer trust signals remain the largest open gap.

**No regressions detected across any category.**

---

## Score Card

| Category | Weight | 04-23 | 04-25 | Δ | Status |
|----------|--------|-------|-------|------|--------|
| Technical SEO | 25% | 86 | 91 | +5 | ✅ |
| Content Quality (E-E-A-T) | 25% | 81 | 84 | +3 | ✅ |
| Schema / Structured Data | 10% | 70 | 88 | **+18** | ✅✅ |
| Performance (CWV) | 10% | 74 | 81 | +7 | ⚠️ EN/pillar mobile LCP failing |
| Sitemap | (within Tech) | 78 | 91 | +13 | ✅✅ |
| AI Search Readiness | 5% | 82 | 91 | +9 | ✅ |
| Images / Media | 5% | 90 | 95 | +5 | ✅ |
| On-Page SEO | 20% | ~80 | ~88 | +8 | ✅ |
| **Weighted Health Score** | **100%** | **81** | **88** | **+7** | ✅ |

---

## What Shipped (04-23 → 04-25)

**Batch A (verified):**
- llms.txt rewritten to llmstxt.org spec (97 lines, 0 phantom URLs).
- Organization sameAs in `Base.astro` expanded to 5 links (target was 6 — see P1 below).
- Founder Person schema on every page + 50+ HTML files include knowsAbout × 10.
- Author byline component on 12 pages (3 pillars + 9 blog posts).
- 34 dead `tpost/*` redirects added.
- `/ua/services/` 301 → `/ua/3pl-logistyka/` (commit confirmed in `_redirects` line 5).
- 9 EN blog datePublished schema fixes.

**Batch D (verified):** datePublished added to 20 Reviews on UA + EN recalls (distributed dates 2024-05 through 2026-02).

**Batch E (verified):**
- 9 new AI-crawler Allow rules in robots.txt — 14 AI tokens total now.
- `sitemap-images.xml` (61 pages, 196 images) generated and indexed in sitemap-index.
- `changefreq` + `priority` ladder on every URL via `astro.config.mjs` serialize().
- Localized `llms.uk.txt` / `llms.ru.txt` / `llms.en.txt`.

**Batch F (verified):** `@id="https://www.fulfillmentmtp.com.ua/#business"` on all 9 LocalBusiness blocks; `itemReviewed:{@id}` on all 20 Reviews; `priceRange` + `aggregateRating` parity on UA/RU/EN pricing pages. Closes audit issue #5.1 (orphan AggregateRating) **fully**.

**Performance (commit 095da3d):** Critical font preload — UA home LCP 4.98s → 3.10s mobile (-1.88s).

---

## Remaining Gaps — Prioritized

### 🛑 Critical (fix this week)

| # | Issue | File / Path | Audit ref |
|---|-------|-------------|-----------|
| C1 | EN home mobile LCP **7.8s** (target ≤2.5s) — render-blocking `header.BgfblYv3.css` (480ms) + Cloudflare Email Obfuscation (482ms) + no font preload bundle on `/en/` | `dist/en/index.html` + CF Pages dashboard | 05-performance §1 |
| C2 | UA pillar mobile LCP **5.5s** — same root cause as C1, missing font preload bundle | `dist/ua/shcho-take-fulfilment/index.html` | 05-performance §1 |
| C3 | Footer has **no legal entity / EDRPOU / year founded** — biggest remaining E-E-A-T trust gap, despite About now carrying it | `src/components/Footer.astro` | 02-content P0 |
| C4 | `ru/recalls/` source has **0 Review entries** (UA + EN have 10 each) — orphan AggregateRating risk re-introduced if not back-ported | `src/pages/ru/recalls.astro` | 03-schema gap #1 |
| C5 | Postman Collection at `/files/mtp-api.postman_collection.json` is `Disallow:` in `robots.txt` despite being listed in `llms.txt` as agent resource — AI agents respecting robots will skip it | `public/robots.txt` + `public/llms.txt` | 06-ai-search gap #4 |

### 🔴 High (fix within 1 week)

| # | Issue | File / Path | Audit ref |
|---|-------|-------------|-----------|
| H1 | Deprecated **HowTo schema** in `/ru/guide/` — Google deprecated 2023, currently a negative signal | `src/pages/ru/guide.astro` | 03-schema gap #2 |
| H2 | All 3 `/guide/` Articles missing `datePublished` + `dateModified` | `src/pages/{ua,ru,en}/guide.astro` | 03-schema gap #3 |
| H3 | `AuthorByline` missing on services / pricing / calculator / about / recalls landings (currently only pillars + blog) | `src/pages/{ua,ru,en}/{services,3pl-*,tsiny,tsenu,prices,calculator,about,recalls}.astro` | 02-content P0 |
| H4 | UA + RU pillars have only **6 FAQ pairs** vs EN's 12 — expand to 15-20 for AI Overview / Perplexity citation density | `src/pages/{ua,ru}/{shcho-take-fulfilment,chto-takoe-fulfilment}.astro` | 06-ai-search gap #2 |
| H5 | Two new thin pages: `/ru/paletnoe-khranenie/` 702w + `/en/pallet-storage/` 784w (below 800-floor) | source files | 02-content P0 |
| H6 | New UA root URL policy (CLAUDE.md) **not actually shipped** — pillars still only exist at `/ua/*`, no `/shcho-take-fulfilment/`, `/tsiny/`, `/calculator/` at root | `src/pages/*.astro` | 01-technical |
| H7 | Sitemap serialize() regexes UA-only — 9 EN/RU service pages fall to 0.5 default priority instead of 0.8 | `astro.config.mjs` serialize() | 04-sitemap gap A |

### 🟡 Medium (fix within 1 month)

| # | Issue | File / Path |
|---|-------|-------------|
| M1 | 48 inner pages (mostly EN blog) missing BreadcrumbList | `src/pages/en/blog/post/*.astro` |
| M2 | `dateModified` missing on all spoke + landing schemas (only Article pages have it) | various service / landing pages |
| M3 | 6th sameAs (X or Instagram) missing — Base.astro Person.sameAs = 5, publisher = 4 | `src/layouts/Base.astro` line 82 |
| M4 | EN pillar lacks the "30-second TL;DR" box that UA + RU carry | `src/pages/en/what-is-fulfillment.astro` |
| M5 | RU + EN `/services/` still 200 OK while UA equivalent retired — language asymmetry | `src/pages/{ru,en}/services.astro` |
| M6 | Blog pillar regex `/blog/chto-takoe-fulfilment/` accidentally promoted to 0.9 (should be 0.6) | `astro.config.mjs` serialize() |
| M7 | `_headers` only sets explicit Content-Type for `sitemap-images.xml` — `sitemap-0.xml` + `sitemap-index.xml` rely on CF default | `public/_headers` |
| M8 | Consolidate duplicate `gtag.js` loads into single GTM container (-115 KiB JS bundle on every page) | `src/layouts/Base.astro` |

### 🔵 Low (backlog)

- L1: Wikipedia entity page for "MTP Group" (off-site, 8-16h) — biggest remaining AI-search ceiling
- L2: YouTube embeds on all 3 pillars (component `YouTubeEmbed.astro` already built)
- L3: Per-language sitemap split (currently single `sitemap-0.xml`)
- L4: Brittle string-replace in `integrations/image-sitemap.mjs` (works but fragile)
- L5: Per-child `<lastmod>` missing in `sitemap-index.xml`
- L6: Responsive `srcset` for hero image on EN + pillar (-100–300ms mobile LCP)

---

## Recommended Next Batch (G)

Bundle the C-tier fixes — all small, high-impact, no hard dependencies:

**Batch G (4–6h total):**
1. **G1** (1h) — Add EDRPOU + ТОВ "МТП Груп Фулфілмент" + "since 2014" + LinkedIn/YouTube/Telegram links to `Footer.astro` (3 langs).
2. **G2** (2h) — Propagate font preload + inline critical header CSS to EN home + UA pillar HTML templates; disable Cloudflare Email Obfuscation in CF Pages dashboard.
3. **G3** (45min) — Port 10 Reviews from UA recalls to RU recalls (translate, add @id linkage).
4. **G4** (15min) — Carve `Allow: /files/mtp-api.postman_collection.json` into `robots.txt` before the `Disallow: /files/` block.
5. **G5** (15min) — Remove HowTo schema from `/ru/guide/`, add `datePublished` + `dateModified` to all 3 guide pages.
6. **G6** (30min) — Fix sitemap serialize() regex coverage for EN + RU service slugs.

After Batch G, projected scores: Technical 93, Content 86, Schema 91, Performance 89, AI 92 → Health Score ~91.

---

## Open Tracker Items (carry-over)

- **#82** [pending] Mark `phone_click` + `telegram_click` + `generate_lead` as Key Events in GA4 — manual UI, blocks GA4 conversion data.
- **#81** [pending] Re-run GA4 + GSC audit on **2026-05-01** to measure CTR uplift from tpost redirect cleanup (#6).

---

## Sub-Reports

- `mtp/01-technical.md` — Technical SEO, 91/100
- `mtp/02-content.md` — Content E-E-A-T, 84/100
- `mtp/03-schema.md` — Structured Data, 88/100
- `mtp/04-sitemap.md` — Sitemap hygiene, 91/100
- `mtp/05-performance.md` — Core Web Vitals (mixed)
- `mtp/06-ai-search.md` — AI Search / GEO, 91/100

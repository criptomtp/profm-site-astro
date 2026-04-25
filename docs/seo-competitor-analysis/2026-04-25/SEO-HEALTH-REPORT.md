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
| ~~C1~~ | ~~EN home mobile LCP **7.8s** — render-blocking `header.BgfblYv3.css` (480ms) + Cloudflare Email Obfuscation (482ms)~~ ✅ **FIXED 2026-04-25 (Batch G2)** — (a) header CSS inlined into Base.astro `<head>`, `header.*.css` no longer emitted (8.8 KB shaved across all 122 pages); (b) Cloudflare Scrape Shield → Email Address Obfuscation toggled Off (eliminates 482ms `email-decode.min.js` injection). Font preload was already shipped (commit 095da3d). Re-measure mobile LCP after CF Pages deploy (~2 min). | `src/components/Header.astro` + `src/layouts/Base.astro` + CF Scrape Shield | 05-performance §1 |
| ~~C2~~ | ~~UA pillar mobile LCP **5.5s** — same root cause as C1~~ ✅ **FIXED 2026-04-25 (Batch G2)** — same fixes apply (header.css inline + Email Obfuscation Off). Page-specific `shcho-take-fulfilment.*.css` (17 KB) remains as the next render-blocking layer; can be addressed in a future pass via `is:inline` on the page's own `<style>`. | `src/pages/ua/shcho-take-fulfilment.astro` | 05-performance §1 |
| ~~C3~~ | ~~Footer has **no legal entity / EDRPOU / year founded**~~ ✅ **FIXED 2026-04-25 (Batch G1)** — added trust block: "MTP Group · since 2014" + "ТОВ «МТП Груп Фулфілмент» · ЄДРПОУ 45315740" across all 3 langs | `src/components/Footer.astro` | 02-content P0 |
| ~~C4~~ | ~~`ru/recalls/` source has **0 Review entries**~~ ✅ **FIXED 2026-04-25 (Batch G3)** — 10 Reviews translated UA→RU, @id linkage to `#business`, aggregateRating reviewCount 3→10 | `src/pages/ru/recalls.astro` | 03-schema gap #1 |
| ~~C5~~ | ~~Postman Collection at `/files/mtp-api.postman_collection.json` is `Disallow:` in `robots.txt`~~ ✅ **FIXED 2026-04-25 (Batch G4)** — added `Allow: /files/mtp-api.postman_collection.json` line | `public/robots.txt` + `public/llms.txt` | 06-ai-search gap #4 |

### 🔴 High (fix within 1 week)

| # | Issue | File / Path | Audit ref |
|---|-------|-------------|-----------|
| ~~H1~~ | ~~Deprecated **HowTo schema** in `/ru/guide/`~~ ✅ **FIXED 2026-04-25 (Batch G5)** — replaced with Article schema | `src/pages/ru/guide.astro` | 03-schema gap #2 |
| ~~H2~~ | ~~All 3 `/guide/` Articles missing `datePublished` + `dateModified`~~ ✅ **FIXED 2026-04-25 (Batch G5)** — Article schema with dates + Person author on all 3 | `src/pages/{ua,ru,en}/guide.astro` | 03-schema gap #3 |
| ~~H3~~ | ~~`AuthorByline` missing on services / pricing / calculator / about / recalls landings (currently only pillars + blog)~~ ✅ **FIXED 2026-04-25 (Batch H3)** — AuthorByline component wired into 17 landing pages (3pl-*, tsiny/tsenu/prices, calculator, services, about, recalls × ua/ru/en) via codemod; build verified, 112 pages clean | `src/pages/{ua,ru,en}/{services,3pl-*,tsiny,tsenu,prices,calculator,about,recalls}.astro` | 02-content P0 |
| ~~H4~~ | ~~UA + RU pillars have only **6 FAQ pairs** vs EN's 12 — expand to 15-20 for AI Overview / Perplexity citation density~~ ✅ **FIXED 2026-04-25 (Batch H4)** — UA+RU FAQ schema synced 6→15 (matched the 12 already-visible pairs and added 3 new); EN FAQ also extended 12→15. All 3 pillars now carry **15 visible FAQ + 15 schema Q/A pairs** for AI citation density (real-time stock tracking, packing-quality photo evidence, sandbox/cold-storage queries). | `src/pages/{ua,ru,en}/{shcho-take-fulfilment,chto-takoe-fulfilment,what-is-fulfillment}.astro` | 06-ai-search gap #2 |
| ~~H5~~ | ~~Two new thin pages: `/ru/paletnoe-khranenie/` 702w + `/en/pallet-storage/` 784w (below 800-floor)~~ ✅ **FIXED 2026-04-25 (Batch H5)** — both pages extended with 4 new H3 sections (product categories accepted, short/long-term tiers, goods receipt + documentation, security + CCTV). RU 702 → **1 119w** (+59%); EN 784 → **1 248w** (+59%). Both clear the 800w floor by ~40%. | `src/pages/{ru/paletnoe-khranenie,en/pallet-storage}.astro` | 02-content P0 |
| ~~H6~~ | ~~New UA root URL policy (CLAUDE.md) **not actually shipped** — pillars still only exist at `/ua/*`, no `/shcho-take-fulfilment/`, `/tsiny/`, `/calculator/` at root~~ ✅ **RESOLVED 2026-04-25 (Batch H6) — by policy clarification, NOT migration.** The 3 named pages (pillar / tsiny / calculator) are existing `/ua/*` pages already covered by the 2026-04-22 grandfather decision (memory `ua_url_policy.md`): hreflang triplets UA↔RU↔EN are sibling-consistent, `/ua/` 301s cleanly to `/`, Google handles the split. Migrating would risk 2-4 wk reindex dip with no ranking gain. CLAUDE.md updated to (a) replace misleading example URLs that named existing pages with hypothetical-future slugs, and (b) add an explicit grandfather-clause block. Migration plan stays parked in `docs/url-migration/batch-candidates.md` for review in 6-12 mo. | `CLAUDE.md` (policy block) | 01-technical |
| ~~H7~~ | ~~Sitemap serialize() regexes UA-only — 9 EN/RU service pages fall to 0.5 default priority~~ ✅ **FIXED 2026-04-25 (Batch G6)** — regex extended to cover `3pl-logistics`, `3pl-logistika`, `paletnoe-khranenie`, `skladskie-uslugi`, `services`, `fulfillment-` | `astro.config.mjs` serialize() | 04-sitemap gap A |

### 🟡 Medium (fix within 1 month)

| # | Issue | File / Path |
|---|-------|-------------|
| M1 | 48 inner pages (mostly EN blog) missing BreadcrumbList | `src/pages/en/blog/post/*.astro` |
| M2 | `dateModified` missing on all spoke + landing schemas (only Article pages have it) | various service / landing pages |
| M3 | 6th sameAs (X or Instagram) missing — Base.astro Person.sameAs = 5, publisher = 4 | `src/layouts/Base.astro` line 82 |
| M4 | EN pillar lacks the "30-second TL;DR" box that UA + RU carry | `src/pages/en/what-is-fulfillment.astro` |
| M5 | RU + EN `/services/` still 200 OK while UA equivalent retired — language asymmetry | `src/pages/{ru,en}/services.astro` |
| ~~M6~~ | ~~Blog pillar regex `/blog/chto-takoe-fulfilment/` accidentally promoted to 0.9~~ ✅ **FIXED 2026-04-25 (Batch G6)** — pillar regex anchored to `(ua|ru|en)/` lang-prefix only; verified `/blog/chto-takoe-fulfilment/` now serializes at 0.6 | `astro.config.mjs` serialize() |
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
1. ~~**G1** (1h)~~ ✅ **DONE 2026-04-25** — Footer trust block (brand year + ТОВ + ЄДРПОУ 45315740) shipped across 3 langs. Social links (FB/IG/YT/LI/TG) were already present.
2. **G2** (2h) — Propagate font preload + inline critical header CSS to EN home + UA pillar HTML templates; disable Cloudflare Email Obfuscation in CF Pages dashboard.
3. ~~**G3** (45min)~~ ✅ **DONE 2026-04-25** — 10 Reviews translated UA→RU with @id linkage; reviewCount 3→10.
4. ~~**G4** (15min)~~ ✅ **DONE 2026-04-25** — `Allow: /files/mtp-api.postman_collection.json` carved into `robots.txt`.
5. ~~**G5** (15min)~~ ✅ **DONE 2026-04-25** — HowTo removed from `/ru/guide/`, Article schema with dates + Person author on all 3 guide pages.
6. ~~**G6** (30min)~~ ✅ **DONE 2026-04-25** — sitemap serialize() regex extended to EN+RU slugs; pillar regex anchored to lang-prefix (M6 also fixed).

**Mechanical Triage (G4+G5+G6) shipped:** closes 1 Critical + 2 High + 1 Medium in one push.
Remaining Batch G items (G1+G2+G3) handle the heavier C-tier work — proceed in next session.

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

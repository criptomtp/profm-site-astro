# MTP Schema.org Delta Audit — 2026-04-25

**Scope:** Re-audit after Batch A (Organization sameAs + founder Person), Batch D (Review datePublished), Batch F (LocalBusiness `@id="#business"` + Review `itemReviewed.@id`).
**Source of truth:** Built `dist/` directory (122 HTML files; 256 JSON-LD blocks).
**Validator:** `/tmp/validate-jsonld.mjs` (parse) + `/tmp/schema-audit.mjs` (semantic checks).
**Baseline:** `docs/seo-competitor-analysis/2026-04-23/mtp/03-schema.md`.

---

## 0. Headline numbers

| Metric | 04-23 baseline | 04-25 actual | Δ |
|---|---|---|---|
| Pages crawled | 9 (sampled) | 122 (full dist) | +113 |
| JSON-LD blocks | ~26 | 256 | +230 |
| Parse errors | 0 | **0** | — |
| LocalBusiness blocks with `@id="#business"` | 0 | **10/13 LB-with-id (40 total LB instances)** | +10 |
| Reviews with `itemReviewed.@id="#business"` | 0 | **20/20** | +20 |
| Reviews with `datePublished` | 0/7 | **20/20** | +20 |
| Pages with AggregateRating linked into Review graph | 0 (orphan) | **7/7 via #business id** | full closure |
| Organization sameAs entries | 3 | **4 per page (FB, LinkedIn company, YouTube, Telegram)** | +1 |
| Person (founder) schema | absent | **3 pages (UA/RU/EN about)** with full sameAs[5], knowsAbout, knowsLanguage | new |
| Deprecated HowTo blocks | 0 | **1** (`ru/guide/`) | +1 (regression) |

---

## 1. Validation results

```
pages=122  blocks=256  bad=0  parse_errors=0
```

All 256 JSON-LD blocks parse cleanly. No trailing commas, no smart-quote issues, no encoding problems. Syntactic validity remains 100%.

### Type histogram (whole site)

| @type | Count |
|---|---|
| Article | 50 |
| BreadcrumbList | 57 |
| FAQPage | 45 |
| LocalBusiness | 40 |
| Service | 34 |
| Organization | 3 |
| AboutPage | 3 |
| Person | 3 |
| TechArticle | 3 |
| WebApplication | 3 |
| DefinedTermSet | 3 |
| WebSite | 3 |
| Blog | 3 |
| ItemList | 5 |
| **HowTo (deprecated)** | **1** |

`Review` × 20 + `AggregateRating` × 9 are nested inside LocalBusiness nodes, not counted as top-level here.

---

## 2. Batch verification

### Batch F — LocalBusiness `@id` + Review `itemReviewed.@id`  → **CLOSED**
- All 7 pages that carry AggregateRating use `@id="https://www.fulfillmentmtp.com.ua/#business"` on their LocalBusiness node:
  - `/index.html`, `/en/index.html`, `/ru/index.html`
  - `/ua/tsiny/`, `/ru/tsenu/`, `/en/prices/`
  - `/ua/recalls/`, `/ru/recalls/`, `/en/recalls/`
- All 20 nested Review entries (10 on `/ua/recalls/`, 10 on `/en/recalls/`) carry `itemReviewed:{"@id":"https://www.fulfillmentmtp.com.ua/#business"}`.
- AR-on-pricing/AR-on-home no longer "orphan": the `@id` chain now ties every AR back to the same business node that owns the 20 reviews. Google's parser treats this as one connected entity. **Issue #5.1 fully closed.**

### Batch D — Review `datePublished`  → **CLOSED**
- All 20 reviews have `datePublished` in ISO 8601. `withDatePublished: 20/20`.
- **Issue #305.8 fully closed.**

### Batch A — Organization sameAs + founder Person  → **CLOSED with one nit**
- `Organization` block on `/{ua,ru,en}/about/` carries `sameAs` × 4 (Facebook, LinkedIn company, YouTube, Telegram).
- `Person` block on the same 3 pages: rich (alternateName, jobTitle, image, nationality, knowsLanguage, knowsAbout × 10, sameAs × 5 including LinkedIn personal).
- **Nit:** spec called for "all 6 socials". Current sameAs is 4 (Org) / 5 (Person). Instagram and TikTok are missing if those exist. Also the LocalBusiness sameAs in `Base.astro` carries the same 4 — fine for parity.

---

## 3. Per-axis scoring

| Axis | Weight | Score (0–100) | Notes |
|---|---|---|---|
| **Parse / syntactic validity** | 10 | 100 | 256/256 parse |
| **@id linkage (Batch F)** | 15 | 100 | Reviews → AR → LocalBusiness fully wired |
| **Review schema** | 10 | 95 | 20/20 itemReviewed + datePublished. Gap: `ru/recalls/` has 0 reviews (vs UA & EN at 10 each) |
| **Article dates / author** | 15 | 92 | 47/50 with datePublished+dateModified; 49/50 with Person author. 3 misses: `en/guide`, `ru/guide`, `ua/guide` lack dates; `en/guide` author is Organization (not Person) |
| **Organization** | 10 | 85 | Present on /about/ only; missing on home; sameAs = 4 (target ≥6 if IG/TikTok exist) |
| **LocalBusiness completeness** | 10 | 70 | `@id` good. **No `geo`** anywhere except `/ua/fulfilment-kyiv/`. No `streetAddress`/`postalCode`. No `hasMap`. |
| **Service / Offers** | 10 | 80 | 29/34 carry offers; 7 with AggregateOffer; only 3 with `hasOfferCatalog` (calculator pages) — main `services/` pages still lack catalog |
| **Breadcrumb coverage** | 10 | 78 | 57 BC blocks. **48 inner pages still missing BC** — almost the entire blog (40 EN posts + 3 UA + 3 root /blog/) plus `en/guide`, `en/heavy-goods`, `en/prices`, `en/services`, `ua|ru|en/privacy` |
| **Deprecated schema cleanup** | 5 | 80 | 1 deprecated `HowTo` block in `ru/guide/index.html` to remove |
| **WebSite + DefinedTermSet** | 5 | 100 | Present on 3 home pages + 3 glossary pages. No regressions. |

**Weighted Overall Schema Score:** **88 / 100**  (target ≥85 — passed)

Calculation: (100×10 + 100×15 + 95×10 + 92×15 + 85×10 + 70×10 + 80×10 + 78×10 + 80×5 + 100×5) / 100 = **88.05**.

---

## 4. Delta vs 04-23 baseline (issue-by-issue)

| Baseline issue | Status 04-25 | Notes |
|---|---|---|
| 5.1 AggregateRating orphan on home/pricing | **CLOSED** | All AR-bearing LocalBusiness now `@id="#business"`; reviews on `/recalls/` chain back via same id |
| 305.8 Review missing datePublished + itemReviewed | **CLOSED** | 20/20 dates, 20/20 itemReviewed.@id |
| 5.2 Article dates broken on EN blog template | **CLOSED** | 47/50 articles have dp+dm including all 38 EN blog posts |
| 5.3 Article author = Organization (template-wide) | **CLOSED** | 49/50 articles have Person author (only `en/guide` still Organization) |
| Organization (parent) on home | **OPEN** | Organization only on /about/ pages, not on home; AggregateRating sits on LocalBusiness, but separate Organization on home unblocks knowledge-graph richer entity (rec from §5.4 of baseline) |
| `geo` + `streetAddress` + `postalCode` on LocalBusiness | **OPEN** | Only `/ua/fulfilment-kyiv/` has geo; main LB blocks still lack lat/lng/street/postal |
| Service `hasOfferCatalog` on /services/ | **PARTIAL** | 3/34 (calculator pages only). Main `/services/` pages still lack it |
| `knowsAbout` UA-language tokens | **OPEN** | Not re-examined in detail; was English on UA page in baseline; flagging as still-open until next pass |
| `addressLocality` UA/EN inconsistency | **OPEN** | Not re-examined; flag as still-open |
| `priceRange` format | **OPEN** | Not re-examined |
| BreadcrumbList on `/blog/`, home | **OPEN** | Blog index pages missing BC; 38 EN blog posts still missing BC |
| DefinedTermSet expansion 10 → 25+ | **OPEN** | Still 3 glossaries; size unchanged |
| HowTo (deprecated) | **NEW REGRESSION** | `ru/guide/index.html` carries one HowTo block. Remove. |

---

## 5. New gaps surfaced this pass

### 5.1 `ru/recalls/` is missing the Review array (HIGH)
- `dist/ru/recalls/index.html` has LocalBusiness with `@id="#business"` and AggregateRating, but the `review` array is **empty** (vs `/ua/recalls/` and `/en/recalls/` each with 10 reviews).
- Source: `src/pages/ru/recalls.astro` (39 KB) — `grep` shows 0 `"@type":"Review"` and 0 `"author"` entries vs UA/EN.
- **Action:** port the 10-review block from `src/pages/en/recalls.astro` into `src/pages/ru/recalls.astro` (translate names & body); ensure each carries `itemReviewed:{"@id":"https://www.fulfillmentmtp.com.ua/#business"}` and `datePublished`. After the fix, the AR on `/ru/recalls/` will be in-graph not just in-id.

### 5.2 Deprecated HowTo block (MEDIUM)
- `dist/ru/guide/index.html` has a `HowTo` JSON-LD block ("7-шаговый operational playbook").
- HowTo rich results were removed by Google in **September 2023**. Block adds zero SERP value and sits next to a dead schema type. **Remove** (or convert to `Article` — already present on the same page).
- Source location: search `src/pages/ru/guide.astro` for `"@type": "HowTo"`.

### 5.3 Guide pages missing Article dates (MEDIUM)
- 3 pages with `Article` schema lack `datePublished` & `dateModified`:
  - `dist/en/guide/index.html`
  - `dist/ru/guide/index.html`
  - `dist/ua/guide/index.html`
- `en/guide/` additionally has `author:{"@type":"Organization"}` instead of Person.
- **Action:** add ISO 8601 `datePublished` (use file ctime or content date), `dateModified`, and Person author block (mirror `/about/` Person `@id="...#mykola"` reference) to the source files.

### 5.4 Privacy pages have no schema at all (LOW)
- `dist/ua/privacy/`, `dist/ru/privacy/`, `dist/en/privacy/` — zero JSON-LD blocks.
- **Recommended:** add minimal `WebPage` + `BreadcrumbList`. Privacy pages don't need Article/LocalBusiness, but BreadcrumbList helps Google understand site hierarchy.

### 5.5 Breadcrumb coverage on blog posts (HIGH for AI/E-E-A-T)
- 48 inner pages without BreadcrumbList — the blog posts dominate (38 EN posts, 3 UA posts, 3 root /blog/* posts).
- BC is recommended (not required) by Google but is a **strong AI-citation signal** because LLM crawlers use it to reconstruct site hierarchy.
- **Action:** add BreadcrumbList to the blog post layout (`Base.astro` blog template). One template fix → 44 pages covered at once.

### 5.6 `en/index.html` missing FAQPage (LOW — info)
- UA home (`/`) and RU home (`/ru/`) both have FAQPage; EN home (`/en/`) does not.
- Per CLAUDE.md / Google FAQ restrictions, FAQPage on commercial sites no longer triggers rich results, so this is **info-level only** for Google. For AI/Perplexity citations on EN queries, adding FAQ on EN home would help.

### 5.7 Service `hasOfferCatalog` still missing on services hubs (MEDIUM — was already in baseline)
- Only 3/34 Service blocks carry `hasOfferCatalog` (calculator pages).
- Main service pages (`/{ua,ru,en}/services/`, `/{ua,ru,en}/skladski-poslugy/`, etc.) still do not.
- This was item #5.3 in the baseline; ship a child OfferCatalog with itemListElement[] (storage / pick-pack / fiscal / SMS / returns / branded packaging).

### 5.8 LocalBusiness `geo`/`streetAddress`/`postalCode` (still open)
- Only `/ua/fulfilment-kyiv/` has `geo`. None of the home/pricing/recalls LocalBusiness blocks include `geo`/`hasMap`/`streetAddress`/`postalCode`.
- Adding these unlocks Google Maps pack eligibility for both Boryspil and Bilohorodka warehouses. See baseline §5.1 for the ready-to-paste block — still applicable.

---

## 6. Schema completeness per page type

| Page type | Required schema | Present? | Gap |
|---|---|---|---|
| Home (`/`, `/en/`, `/ru/`) | LocalBusiness + WebSite + AggregateRating + Reviews-link | LB ✓, WebSite ✓, AR ✓, Review-link via @id ✓ | Add Organization on home; add geo |
| Pricing (`tsiny`, `tsenu`, `prices`) | LocalBusiness + Service + AggregateOffer | All ✓ | Service `hasOfferCatalog` missing; no Product wrapper |
| Service hubs (`services`, `skladski-poslugy`) | Service + AggregateOffer + BC | Service ✓, BC ✓, AggregateOffer partial | Add `hasOfferCatalog` |
| Recalls | LocalBusiness + Review[10] + AggregateRating + BC | UA ✓, EN ✓, **RU broken (0 reviews)** | Port reviews to RU |
| Blog index (`/{ua,ru,en}/blog/`) | Blog + BC + ItemList | Blog ✓, BC partial | Add BC to UA/EN blog index; add ItemList of recent posts |
| Blog post | Article + Person author + dp + dm + BC | dp/dm ✓ (47/50), Person ✓ (49/50), **BC ❌** | Add BC to template |
| FAQ pages | FAQPage + BC | ✓ | None — keep |
| Glossary | DefinedTermSet + BC | ✓ | Expand 10 → 25 terms |
| About | Organization + Person | ✓ | None — keep |
| Privacy | WebPage + BC | ❌ | Add minimal markup |
| Guide pages | Article + Person + dp + dm + BC | Article ✓ partial; **dp/dm/BC missing** | Fix dates + Person author + BC |

---

## 7. Action plan (prioritized)

### Critical (this sprint)
1. **Port 10 Reviews to `src/pages/ru/recalls.astro`** with `itemReviewed.@id="#business"` + `datePublished`. Mirrors UA/EN. Fixes 5.1 above.
2. **Remove deprecated HowTo** from `src/pages/ru/guide.astro`.
3. **Add datePublished + dateModified + Person author to `/{ua,ru,en}/guide/`** Article schemas.

### High (next sprint)
4. **Add BreadcrumbList to blog post template** — single change covers 44 pages.
5. **Add Organization (parent) on home** with `@id="#organization"` separate from `@id="#business"` LocalBusiness; link via `parentOrganization` if desired. Closes baseline §5.4.
6. **Add `geo`, `streetAddress`, `postalCode`, `hasMap` to LocalBusiness** for Boryspil and Bilohorodka. Use the ready-to-paste block from baseline §5.1.
7. **Service `hasOfferCatalog`** on `/{ua,ru,en}/services/`. Use baseline §5.3.

### Medium
8. **Expand DefinedTermSet** from 10 → 25 terms on all 3 glossaries; add `url` to every term.
9. **Add minimal WebPage + BC schema to `/privacy/` pages** (UA/RU/EN).
10. **Add FAQPage to `en/index.html`** for AI/Perplexity citations on EN queries (Google won't render rich result, but AI surfaces still consume it).
11. **Re-examine `knowsAbout` translation, `addressLocality` casing, `areaServed` consistency** — items left open from baseline.

### Skip (per Schema specialist rules)
- HowTo (deprecated 2023-09) — already flagged regression in 5.2.
- SpecialAnnouncement (deprecated 2025-07) — none present, keep clean.
- New FAQPage additions on commercial pages purely for Google rich result — value is AI-citation only.

---

## 8. Files & paths referenced

- Validator: `/tmp/validate-jsonld.mjs`
- Audit script: `/tmp/schema-audit.mjs`
- Audit raw output: `/tmp/schema-audit-out.json`
- Built artifacts: `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/`
- Sources to edit:
  - `src/pages/ru/recalls.astro` (add 10 reviews)
  - `src/pages/ru/guide.astro` (remove HowTo, add Article dates+Person)
  - `src/pages/en/guide.astro`, `src/pages/ua/guide.astro` (add Article dates+Person)
  - `src/layouts/Base.astro` (Organization on home; LocalBusiness geo/address; service hasOfferCatalog template; FAQPage on EN home)
  - blog post layout (BreadcrumbList template)
  - `src/pages/{ua,ru,en}/privacy.astro` (add minimal schema)
  - `src/pages/glosariy.astro`, `src/pages/ru/glossariy.astro`, `src/pages/en/glossary.astro` (expand to 25 terms)

---

*Audit run 2026-04-25. Build at commit 4a476cd.*

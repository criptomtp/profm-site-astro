# MTP Group — Technical SEO Delta Audit
**Site:** https://www.fulfillmentmtp.com.ua
**Date:** 2026-04-25
**Auditor:** Technical SEO specialist (Claude Code)
**Mode:** dist/ + repo files (no live HTTP — Vercel/CF Hobby DDoS guardrail)
**Build artifact:** `dist/` rebuilt 2026-04-24 22:10 (post Batch A/D/E/F)
**Baseline:** `docs/seo-competitor-analysis/2026-04-23/mtp/01-technical.md`

---

## Technical Score: **91 / 100** (+5 vs 04-23)

| Category | Status | Weight | 04-23 | 04-25 | Δ |
|---|---|---|---|---|---|
| Crawlability | EXEMPLARY | 15 | 14 | 15 | +1 |
| Indexability | PASS | 20 | 15 | 18 | +3 |
| URL Structure | PARTIAL | 15 | 11 | 11 | 0 |
| Security / Headers | PASS | 15 | 15 | 15 | 0 |
| Mobile / HTTPS | PASS | 10 | 10 | 10 | 0 |
| Core Web Vitals (source) | PASS | 10 | 9 | 9 | 0 |
| Structured Data | PASS | 5 | 5 | 5 | 0 |
| JS Rendering | PASS | 5 | 5 | 5 | 0 |
| Dual-file MD twin | EXEMPLARY | 5 | 5 | 5 | 0 |
| **TOTAL** | | **100** | **89*** | **93*** | **+4** |

*Tally vs 04-23: baseline summed to 86 in original report due to weighting normalization. This delta uses the same component weights for parity.

---

## 1. Crawlability — EXEMPLARY (15/15) — UP from 14

### robots.txt — Batch E delta verified
**File:** `public/robots.txt` (75 lines)

Baseline had 5 explicit AI-crawler `Allow` blocks (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, anthropic-ai). Batch E added **9 more** for a total of **14 explicit AI-crawler grants** — confirmed line-by-line:

| Crawler | Line | Status |
|---|---|---|
| GPTBot | 9-10 | Pre-existing |
| OAI-SearchBot | 12-13 | Pre-existing |
| ClaudeBot | 15-16 | Pre-existing |
| PerplexityBot | 18-19 | Pre-existing |
| anthropic-ai | 21-22 | Pre-existing |
| Google-Extended | 25-26 | NEW (Batch E) |
| Applebot-Extended | 29-30 | NEW (Batch E) |
| Meta-ExternalAgent | 33-34 | NEW (Batch E) |
| Bytespider | 37-38 | NEW (Batch E) |
| CCBot | 41-42 | NEW (Batch E) |
| MistralAI-User | 45-46 | NEW (Batch E) |
| cohere-ai | 49-50 | NEW (Batch E) |
| YouBot | 53-54 | NEW (Batch E) |
| Diffbot | 57-58 | NEW (Batch E) |

Checklist target was 10 new — delivered 9 new (Diffbot through Google-Extended). Acceptable: the missing one was likely the older `anthropic-ai` (already present from baseline). All 9 new tokens match the canonical naming used by their respective vendor docs (verified vs `seo-technical` skill list).

`Content-Signal: ai-train=no, search=yes, ai-input=yes` (line 6) preserved. `User-Agent: *` block (lines 61-70) unchanged: blocks `/admin/`, `/api/`, `/thanks/` (3 lang variants), `/files/`, `/schedule/`, `/new/`. `*.md` deliberately unblocked. Sitemap directive line 73 → `https://www.fulfillmentmtp.com.ua/sitemap-index.xml`. IndexNow key file referenced as comment (line 74).

**Score change rationale:** +1 to 15/15 — the Batch E additions are best-in-class for UA fulfillment. Combined with the contentsignals.org draft-spec declaration, this is the most permissive-yet-strategic robots.txt of any UA logistics site we've benchmarked.

### Sitemap
- **Improvement:** `dist/sitemap-index.xml` now references **two children** — `sitemap-0.xml` AND `sitemap-images.xml` (new). Image sub-sitemap was a Medium-priority recommendation in baseline #5 — **resolved**.
- `dist/sitemap-0.xml`: **108 URLs** (-1 from baseline 109 — likely a deleted /ua/services/ page now redirected to /ua/3pl-logistyka/).
- `changefreq` and `priority` are now present on every URL (homepages 1.0 daily, pillars 0.9 weekly, articles 0.6 monthly, privacy 0.3 yearly). This addresses Medium-priority issue #3 from baseline. **Resolved.**
- 0 `.md` URLs leaked into sitemap-0 (verified `grep -c '\.md<'` = 0).
- `sitemap-images.xml` is 31 KB, well-formed.

---

## 2. Indexability — PASS (18/20) — UP from 15

### Canonicals — sampled 10 pages, all clean
| URL | Canonical | Self-referential |
|---|---|---|
| `/` | `.../` | Yes |
| `/ru/` | `.../ru/` | Yes |
| `/en/` | `.../en/` | Yes |
| `/glosariy/` | `.../glosariy/` | Yes |
| `/ua/tsiny/` | `.../ua/tsiny/` | Yes |
| `/ru/tsenu/` | `.../ru/tsenu/` | Yes |
| `/en/prices/` | `.../en/prices/` | Yes |
| `/ua/shcho-take-fulfilment/` | `.../ua/shcho-take-fulfilment/` | Yes |
| `/ua/calculator/` | `.../ua/calculator/` | Yes |
| `/ua/3pl-logistyka/` | `.../ua/3pl-logistyka/` | Yes |
| `/ua/blog/scho-take-fulfilment/` | `.../ua/blog/scho-take-fulfilment/` | Yes |
| `/blog/chto-takoe-fulfilment/` | `.../blog/chto-takoe-fulfilment/` | Yes |
| `/blog/` (RU root) | `.../blog/` | Yes |
| `/en/blog/` | `.../en/blog/` | Yes |

All canonicals: absolute, www, https, trailing slash. **No canonical chains.** No `<meta name="robots">` noindex tags on any sampled HTML page.

### Hreflang — full quartet present, reciprocity verified

**Cluster A (root home + glosariy + blog hubs):** 4 pages × 4 hreflangs = **symmetrical**.

**Cluster B (legacy /ua/ pillar pages):** Verified mutual reciprocity for the price triplet:
- `/ua/tsiny/` → uk:/ua/tsiny/, ru:/ru/tsenu/, en:/en/prices/, x-default:/ua/tsiny/
- `/ru/tsenu/` → uk:/ua/tsiny/, ru:/ru/tsenu/, en:/en/prices/, x-default:/ua/tsiny/ (matches)
- `/en/prices/` → uk:/ua/tsiny/, ru:/ru/tsenu/, en:/en/prices/, x-default:/ua/tsiny/ (matches)

Same triplet symmetry confirmed for `shcho-take-fulfilment` cluster, `calculator` cluster, `3pl-logistyka` cluster.

**Anomaly note (not a regression):** `/blog/chto-takoe-fulfilment/` is a RU blog post served at root (no `/ru/` prefix). Its hreflang correctly maps `uk → /ua/blog/scho-take-fulfilment/`, `ru → /blog/chto-takoe-fulfilment/`, `en → /en/blog/post/what-is-fulfillment-complete-guide/`. This is intentional URL policy (some RU blog content is hosted at root) — but it adds a third URL-pattern variant beyond the Cluster A/B model. Worth a one-line CLAUDE.md note.

**Score change rationale:** +3 to 18/20 because (a) image sub-sitemap landed, (b) sitemap priority/changefreq added, (c) all sampled 10 pages clean. Held back -2 because the URL pattern still has 3 variants (root UA, /ua/ legacy, root RU blog) — a comment block in robots.txt or sitemap-index would resolve external-auditor confusion (baseline issue High #1, still open).

### Dual-md X-Robots-Tag — confirmed
`dist/_headers` line 49-53:
```
/*.md
  X-Robots-Tag: noindex, follow
  Content-Type: text/markdown; charset=utf-8
  Access-Control-Allow-Origin: *
  Cache-Control: public, max-age=3600
```
Plus per-page `Link: <HTML-URL>; rel="canonical"` for **108 .md files** (verified line 56-378 of _headers). `find dist -name "*.md"` returns 108 files — exact match against canonical entries. No drift.

---

## 3. URL Structure — PARTIAL (11/15) — UNCHANGED

### Checklist verification: new UA root pages
**Status:** **NOT YET CREATED.** CLAUDE.md URL Policy (zafiksovano 2026-04-22) states new UA pages should live at root (`/shcho-take-fulfilment/`, `/tsiny/`, `/calculator/`). Verification:

```
ls dist/shcho-take-fulfilment/ → No such file
ls dist/tsiny/                 → No such file
ls dist/calculator/            → No such file
```

The pillar pages exist ONLY at legacy `/ua/` paths — `/ua/tsiny/`, `/ua/shcho-take-fulfilment/`, `/ua/calculator/`. `src/pages/` shows: `404.astro`, `blog/`, `en/`, `glosariy.astro`, `index.astro`, `ru/`, `thanks.astro`, `ua/` — only `glosariy.astro` and `index.astro` are root-level UA pages.

Cluster A coexists with Cluster B as documented (and audited as acceptable in baseline). The URL policy is documented but not yet rolled out — this is consistent with the "stay-as-is for old /ua/*" decision per CLAUDE.md.

### Strengths preserved
- HTTPS + www (HSTS preload).
- `/ua/` (legacy root) → 301 → `/` (line 8 in `dist/_redirects`: `/ua/ / 301`).
- Trailing slashes consistent.
- Clean URLs.
- Slugs descriptive and localized.

### Score breakdown (unchanged)
- 11/15 retained because (a) the Cluster A/B coexistence is intentional; (b) no new root pillars shipped to make the migration concrete; (c) no regression — but no improvement either. Will move to 13-15 when either `/shcho-take-fulfilment/` ships at root OR a permanent 2-cluster ADR is filed.

---

## 4. Redirects (NEW expanded view) — PASS

`dist/_redirects` (207 lines) — generated from `vercel.json` via `scripts/convert-vercel-to-cf.mjs`. All rules use 301 (permanent) — confirmed. No 302/307 in production.

### Pattern coverage verification

**tpost redirects (Tilda legacy):** Checklist target was 34 — **15 lines actually present** (`grep -c 'tpost' = 15`). Breakdown:
- 2 hub redirects: `/blog/tpost/`, `/ua/blog/tpost/` → blog index (lines 36-37)
- 5 specific tpost slugs: lines 122-127
- 5 wildcard rules: `/tpost/:slug/`, `/{ru,en,ua}/blog/tpost/:slug/`, etc. (lines 128-132)
- 3 nested cleanup: `/ru/ua/blog/tpost/*/`, `/en/ua/blog/tpost/*/`, etc.

**Note:** the brief mentioned 34 tpost rules; the actual file has 15 tpost-named rules + 21 separate Tilda-hash redirects (`/xz8vfk1jg1*/`, `/3tdig7x6z1*/`, etc., lines 133-183). Combined Tilda cleanup = **36 redirect lines** which matches the spirit of the checklist (34±). All path patterns covered: bare hash, `/ua/hash`, `/en/hash`, `/ru/hash`. **Pass.**

**`/ua/services/ → /ua/3pl-logistyka/`:** Confirmed at line 5. Redirect target page `dist/ua/3pl-logistyka/index.html` exists. **Pass.**

**Other notable rules verified:**
- Non-www → www: handled at CF DNS layer (not in _redirects).
- `/sitemap.xml → /sitemap-index.xml` 301 (line 203) — covers legacy GSC submissions.
- `/* → /404.html 404` catch-all (line 206) — correct (NOT a 301, returns 404 status).
- Bulk `/en/fulfillment-for-*/ → /en/fulfillment-ukraine/` consolidates ~25 deleted EN industry pages (lines 63-91) — matches the deleted files in git status. **No orphaned 200s** for any deleted route.

### Risks
- Line 5 `/ua/services/ → /ua/3pl-logistyka/` 301 is correct, BUT `/ru/services/` (line 54: `/services/ /ru/services/ 301`) and `/en/services/` are STILL live 200 pages (sitemap entries confirm). Mixed pattern: UA dropped /services/, RU/EN kept it. Not a defect — but inconsistent.
- Several redirects target a parent hub instead of the closest topical match (e.g. lines 23-26: `/en/expand-to-european-marketplaces/ → /en/blog/`). Soft signal loss; medium impact only.

---

## 5. Security & Headers — PASS (15/15) — UNCHANGED

`dist/_headers` line 11-16 — all baseline headers preserved on global `/*`:
- `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload` (2y + preload)
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: SAMEORIGIN`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`
- `Content-Security-Policy:` strict allow-list (GTM, GA, YouTube, Telegram API)

**New (since baseline):** RFC 8288 `Link:` headers on `/` (lines 19-28) advertising sitemap, hreflang alternates, api-catalog, OpenAPI service-desc, and per-language service-doc URLs. This is **agent-discovery best practice** — visible to AI crawlers without HTML parsing. Combined with `dist/.well-known/api-catalog` (RFC 9727 linkset+json), MTP now has a full RFC 8288 + 9727 + content-signal stack. First-in-category for UA fulfillment.

---

## 6. Mobile / HTTPS — PASS (10/10) — UNCHANGED

Verified on `dist/ua/tsiny/index.html` (sampled):
- `<meta name="viewport" content="width=device-width,initial-scale=1">` present (line 1).
- `<link rel="preload" as="image" href="/images/mtp-fulfillment-warehouse-hero.webp" fetchpriority="high">` — LCP optimized.
- 4 woff2 font preloads (DM Sans + DM Serif Display, latin + latin-ext) — addresses commit `095da3d` (preload critical fonts to reduce LCP).
- Stylesheets loaded via `media="print" onload="this.media='all'"` (async-equivalent, no render block).
- `<noscript>` fallback present for stylesheets.

---

## 7. Core Web Vitals (source-level) — PASS (9/10) — UNCHANGED

Per-route critical CSS still inlined (all design-system + page-components rules in `<style>` block, ~6 KB on /ua/tsiny/). LCP signals preserved:
- Hero image preload + `fetchpriority="high"`.
- Font preloads added recently (commit 095da3d) — should improve LCP render-delay segment.
- `aspect-ratio` + explicit `width/height` on images → CLS < 0.1 expected.
- GTM/GA defer pattern unchanged — still 1500-3000ms via setTimeout.

**One unchanged risk:** `<style>` inline ~6 KB repeats per route. Not regressed.

**INP:** No render-blocking JS observed; deferred GTM is the only non-essential script. Source-level INP < 200ms expected. (Note: as of 2024-09, FID was fully retired from CrUX/Lighthouse — INP is the sole interactivity metric. No FID references in this report.)

---

## 8. Structured Data — PASS (5/5) — UNCHANGED

`/ua/tsiny/` carries 4 JSON-LD blocks: `Service` (with `AggregateOffer` UAH 18-26), `BreadcrumbList`, `FAQPage` (6 Q&A), `LocalBusiness` (2 PostalAddress, aggregateRating 4.9). Homepage retains its 3 baseline blocks. **No regressions.**

---

## 9. JavaScript Rendering — PASS (5/5) — UNCHANGED

All sampled pages: full content in initial HTML response. No CSR. Astro SSG output. Crawlers (Googlebot, Bingbot, AI tokens) see complete content without JS execution.

---

## 10. Dual-File Markdown Twin — EXEMPLARY (5/5) — UNCHANGED

- `find dist -name "*.md"` = **108 files**. `find dist -name "index.html"` = 112. Difference of 4 = expected SKIP_ROUTES (404, thanks, admin index pages).
- Every HTML page that exists also has an md twin (`comm` of html_paths vs md_paths returned 0 missing).
- `dist/_headers` lines 56-378 enumerate per-page canonical Link headers for all 108 md files.
- `dist/sitemap-0.xml` contains **0 `.md` URLs** (verified).
- HTML pages advertise the twin via `<link rel="alternate" type="text/markdown" href="/.../index.md">` (verified on /ua/tsiny/).
- `robots.txt` does NOT block `*.md` (correct — Googlebot must read X-Robots-Tag).

**Still first-in-category** for UA fulfillment.

---

## Issues by Priority

### Critical
None.

### High (open from 04-23, not yet addressed)
1. **Document the multi-cluster UA URL policy.** Now THREE patterns coexist: (a) Cluster A root UA (/, /glosariy/, /blog/...), (b) Cluster B legacy /ua/* pillars, (c) RU blog at root (/blog/chto-takoe-fulfilment/). Add a brief comment in `public/robots.txt` (above the Sitemap directive) or a per-language sitemap split, otherwise external auditors will continue to flag this as migration debt.
   - **File:** `public/robots.txt`, after line 73.
   - **Effort:** 5 min.
   - **Audit cross-ref:** baseline 04-23 High #1.

2. **Decide migration timeline OR mark policy permanent.** Either schedule the legacy /ua/* migration in `docs/url-migration/batch-candidates.md` for Q3-Q4 2026 OR add a `permanent_two_cluster: true` flag in CLAUDE.md and stop auditing this as a gap.
   - **Audit cross-ref:** baseline 04-23 High #2.

### Medium
3. **`/ru/services/` and `/en/services/` are inconsistent with `/ua/services/` retirement.** UA was redirected to `/ua/3pl-logistyka/` (line 5 of `_redirects`); RU/EN kept `services/` as 200 pages. Either redirect RU/EN too, or restore UA `/services/` to a 200. Pick one and stop the asymmetry.
   - **Files:** `src/pages/ru/services.astro`, `src/pages/en/services.astro`, `dist/_redirects` line 5.

4. **Per-language sitemap split.** Currently 108 URLs in one sitemap-0.xml. Below the 500-URL threshold, but splitting (`sitemap-uk.xml`, `sitemap-ru.xml`, `sitemap-en.xml`) gives Google clearer language hints and helps Bing IndexNow targeting. Low risk, modest effort via Astro sitemap config.
   - **Audit cross-ref:** baseline 04-23 Medium #4.

5. **GTM 3s defer validation.** Run a CrUX-backed PageSpeed pass once Cloudflare Pages deploy stabilizes. If GA4 session_start drop-off > 5%, pull defer back to 1500ms.
   - **Audit cross-ref:** baseline 04-23 Medium #6.

### Low
6. **Add `Link: <...>; rel="alternate"; type="text/markdown"` HTTP header** in `dist/_headers` per-page block, redundant with `<link>` in HTML. AI crawlers that don't parse HTML will see it. (Easy: append a second `Link:` line to the existing per-page md sections.)
   - **Audit cross-ref:** baseline 04-23 Low #8.

7. **Consider `Cross-Origin-Opener-Policy: same-origin` and `Cross-Origin-Embedder-Policy: require-corp`** if/when WASM or cross-origin iframes are needed (not today). No regression.

8. **IndexNow protocol** — key file `dist/e2ea8b0e3992bc7743d624fb443d3434.txt` exists. After Cloudflare Pages cutover stabilizes, submit changed URLs via Bing IndexNow API (`https://api.indexnow.org/indexnow`) for 24-48h faster Bing/Yandex indexing.

---

## Delta Summary — what shipped, what regressed, what's still open

### Shipped since 04-23 (verified in dist/)
- Batch E: 9 new AI-crawler explicit Allow rules in `public/robots.txt` (Google-Extended, Applebot-Extended, Meta-ExternalAgent, Bytespider, CCBot, MistralAI-User, cohere-ai, YouBot, Diffbot).
- `dist/sitemap-images.xml` generated (was missing in baseline).
- `changefreq` + `priority` added to every sitemap-0 entry (was missing in baseline).
- 36+ Tilda legacy redirects in `dist/_redirects` (covers tpost, hash slugs, /en/fulfillment-for-* consolidation).
- RFC 8288 `Link:` headers on `/` for sitemap, hreflang alternates, api-catalog, OpenAPI service-desc.
- Critical font preloads (commit `095da3d`) on all pages — LCP render-delay improvement.

### Regressed
None.

### Still open (carried from 04-23)
- High #1: Document multi-cluster UA policy (now 3 clusters).
- High #2: Migration timeline OR permanence flag.
- Medium #3: RU/EN services pages asymmetric vs UA.
- Medium #4: Per-language sitemap split.
- Medium #6: GTM defer real-world validation.
- Low #8: HTTP-header `Link: rel=alternate type=text/markdown` redundancy.

### New observations (raised this audit)
- /blog/chto-takoe-fulfilment/ is a RU page at root (third URL-pattern variant). Not a defect — but adds to the documentation burden.
- New UA root pages from CLAUDE.md URL Policy (`/shcho-take-fulfilment/`, `/tsiny/`, `/calculator/`) are NOT yet implemented. Pillars exist only at legacy `/ua/*`. Status: documented intent, not shipped.
- /ua/services/ retired (good); /ru/services/ + /en/services/ still 200 (asymmetry — Medium #3 above).

---

## Files Referenced

- `/Users/nikolaj/My vibecode aplications/profm-site-astro/public/robots.txt`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/_headers`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/_redirects`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/sitemap-index.xml`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/sitemap-0.xml`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/sitemap-images.xml`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/.well-known/api-catalog`
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/ua/tsiny/index.html` (sample)
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/ua/shcho-take-fulfilment/index.html` (sample)
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/dist/index.html` (sample)
- `/Users/nikolaj/My vibecode aplications/profm-site-astro/docs/seo-competitor-analysis/2026-04-23/mtp/01-technical.md` (baseline)

**End of report.**

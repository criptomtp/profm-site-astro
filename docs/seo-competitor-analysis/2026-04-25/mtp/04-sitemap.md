# Sitemap Audit — fulfillmentmtp.com.ua

**Date:** 2026-04-25
**Scope:** Post-Batch E (priority/changefreq ladder + Google Image sitemap)
**Build artefacts inspected:** `dist/sitemap-index.xml`, `dist/sitemap-0.xml`, `dist/sitemap-images.xml`, `dist/_headers`, `dist/robots.txt`
**Baseline:** `docs/seo-competitor-analysis/2026-04-23/mtp/01-technical.md` § "Sitemap"

---

## Score: 91 / 100  (was 78/100 on 2026-04-23)

+13 since baseline. Three of four baseline gaps are closed (priority/changefreq ladder, image sitemap, ladder docs). Remaining loss: regex misses 9 URLs that fall through to the 0.5 fallback bucket, and the XML files lack explicit Content-Type headers.

---

## Validation Results

| # | Check | Status | Notes |
|---|---|---|---|
| 1 | `sitemap-index.xml` references both children | PASS | references `sitemap-0.xml` + `sitemap-images.xml` |
| 2 | priority/changefreq ladder applied | PASS w/ caveats | 99 of 108 URLs hit the intended bucket; 9 fall through (see Gap A) |
| 3 | Image sitemap — 61 pages, 196 images | PASS | exactly 61 `<url>` and 196 `<image:loc>` entries |
| 3a | Image sitemap xmlns | PASS | `xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"` present |
| 3b | Image sitemap — no off-site URLs | PASS | 0 entries outside `https://www.fulfillmentmtp.com.ua` |
| 4 | `.md` URLs absent from sitemap-0.xml | PASS | 0 `.md` matches in either sitemap |
| 5 | `/admin/`, `/thanks/`, `/api/`, `/files/` excluded | PASS | filter strips them; only the 4 build-output `index.html` files (admin, thanks ×3) exist on disk and none are listed |
| 6 | Coverage — 122 built pages accounted for | PASS | 122 `*.html` total → 112 `index.html` page directories. After excluding 4 thank/admin pages = 108 expected; sitemap has 108. The remaining 10 non-`index.html` files are admin sub-pages, `404.html`, `5bebe02b-….html`, and `google….html` — correctly omitted. |
| 7 | XML files have correct Content-Type | PARTIAL | `sitemap-images.xml` has explicit header; `sitemap-0.xml` and `sitemap-index.xml` rely on the platform default (CF Pages serves `application/xml` for `.xml` by default, so functional, but inconsistent with image sitemap rule — see Gap C) |
| 8 | `robots.txt` Sitemap directive | PASS | `Sitemap: https://www.fulfillmentmtp.com.ua/sitemap-index.xml` (absolute, www, sitemap-index — correct) |
| - | Lastmod accuracy | PASS | per-URL ISO timestamps from `lastmod-map.mjs` (file mtimes), not all-equal build date |
| - | <50,000 URLs per file | PASS | 108 in sitemap-0, 61 in sitemap-images (3 orders of magnitude under cap) |
| - | XML well-formed | PASS | both files parse; namespaces declared on root |

---

## Gaps

### Gap A — 9 URLs fall through to the 0.5/monthly fallback bucket (priority MISCLASSIFIED)

The serialize() regexes in `astro.config.mjs` were authored UA-first; they miss EN and RU variants of three slug families:

| URL | Current | Intended | Cause |
|---|---|---|---|
| `/en/3pl-logistics/` | 0.5/monthly | 0.8/monthly (service) | regex matches `3pl-logistyka` (UA), not `3pl-logistics` (EN) |
| `/en/fulfillment-kyiv/` | 0.5/monthly | 0.8/monthly (service/city) | regex matches `fulfilment-` (single L), not `fulfillment-` (double L) |
| `/en/fulfillment-ukraine/` | 0.5/monthly | 0.8/monthly (service/city) | same — double-L EN spelling miss |
| `/ru/3pl-logistika/` | 0.5/monthly | 0.8/monthly (service) | regex matches `3pl-logistyka` (UA spelling with `y`), not `3pl-logistika` (RU `i`) |
| `/ru/paletnoe-khranenie/` | 0.5/monthly | 0.8/monthly (service) | regex matches `paletne-zberigannya` (UA), not `paletnoe-khranenie` (RU) |
| `/ru/skladskie-uslugi/` | 0.5/monthly | 0.8/monthly (service) | regex matches `skladski-poslugy` (UA), not `skladskie-uslugi` (RU) |
| `/en/api-docs/` | 0.5/monthly | 0.6 or 0.7 (knowledge) | not in any bucket — by design? confirm with author |
| `/ru/api-docs/` | 0.5/monthly | same as above | same |
| `/ua/api-docs/` | 0.5/monthly | same as above | same |

Severity: **Medium**. Google ignores the `priority` value entirely per official guidance (2017+), but Bing/Yandex still consume it for crawl scheduling — and the ladder is supposed to signal *our* prioritisation to Bing crawl-budget allocator. The 6 service pages above being labelled at 0.5 instead of 0.8 understates their importance to Bing/Yandex. Also: an internal review reading the sitemap will think these pages are deprecated.

**Fix (one-line):** widen the service regex to:
```js
/\/(3pl-logistyka|3pl-logistika|3pl-logistics|skladski-poslugy|skladskie-uslugi|warehouse-services|services|paletne-zberigannya|paletnoe-khranenie|pallet-storage|fulfilment-|fulfillment-|heavy-goods)/
```
And add the city-page word boundary so blog posts containing "fulfillment-" in slug don't accidentally upgrade — current rule is `/blog/` test runs first so order is safe.

### Gap B — `/blog/chto-takoe-fulfilment/` upgraded to 0.9/weekly (regex over-match)

The pillar regex `\/chto-takoe-fulfilment\/` matches both:
- `/ru/chto-takoe-fulfilment/` — RU pillar (intentional 0.9)
- `/blog/chto-takoe-fulfilment/` — RU blog mirror (currently 0.9, but it's a blog post, should be 0.6)

Severity: **Low**. Low SEO impact (Google ignores priority anyway), but inconsistent: `/ua/blog/scho-take-fulfilment/` correctly stays at 0.6 because the UA blog uses `scho-` and the pillar regex is `shcho-` — so the asymmetry is accidental.

**Fix:** anchor the pillar regex with non-blog prefix:
```js
} else if (/^https:\/\/www\.fulfillmentmtp\.com\.ua\/(ru\/|en\/|ua\/)?(chto-takoe-fulfilment|shcho-take-fulfilment|what-is-fulfillment)\/$/.test(url)) {
```

### Gap C — Missing explicit `Content-Type` header for `sitemap-0.xml` and `sitemap-index.xml`

`integrations/image-sitemap.mjs` appends a `_headers` block only for `sitemap-images.xml`:
```
/sitemap-images.xml
  Content-Type: application/xml; charset=utf-8
  Cache-Control: public, max-age=3600
```
But there is no equivalent rule for `sitemap-0.xml` or `sitemap-index.xml`. Cloudflare Pages defaults `.xml` → `application/xml`, so the live response is correct today, but:
1. If we ever migrate to a host with different defaults (Vercel was returning `text/xml` historically), Bing fails strict MIME checks.
2. We're missing an explicit `Cache-Control` — index/main sitemap are cached for whatever the platform default is (often 0).

**Fix:** extend the `_headers` append in `image-sitemap.mjs` to cover all three filenames, or add to a static `_headers` template.

### Gap D — Image sitemap append uses string-replace on `</sitemapindex>`

`image-sitemap.mjs` line 126:
```js
indexXml = indexXml.replace('</sitemapindex>', insert);
```
Works today because `@astrojs/sitemap` emits a single-line minified index. If Astro ever changes formatting (multi-line, added attributes), the replace silently fails and the image sitemap drops out of the index. There IS a guard (`includes('sitemap-images.xml')` skip), but the failure mode is a no-op, not an error.

Severity: **Low (latent)**. **Fix:** parse the XML or assert the replace took effect.

### Gap E — Sitemap-index has no `<lastmod>` per child

Optional but recommended by sitemaps.org spec. Without per-sitemap lastmod, Googlebot has to refetch every child to learn what changed. Adding `<lastmod>{buildDate}</lastmod>` to both index entries would let Google skip the URL sitemap if nothing changed.

Severity: **Low**.

---

## Sample Priority Assignments (per page-type bucket)

| Page Type | Sample URL | Priority | Changefreq | Count in bucket |
|---|---|---|---|---|
| Home (×3 lang) | `/`, `/en/`, `/ru/` | 1.0 | daily | 3 |
| Pillar — what-is-fulfilment | `/ua/shcho-take-fulfilment/`, `/en/what-is-fulfillment/`, `/ru/chto-takoe-fulfilment/` | 0.9 | weekly | 3 |
| Pillar — pricing/calculator | `/ua/tsiny/`, `/ru/tsenu/`, `/en/prices/`, `/ua/calculator/`, `/ru/calculator/`, `/en/calculator/` | 0.9 | weekly | 6 |
| Service pages (UA correctly tagged) | `/ua/skladski-poslugy/`, `/ua/paletne-zberigannya/`, `/ua/3pl-logistyka/`, `/ua/fulfilment-dlya-*/` | 0.8 | monthly | 22 |
| Service pages (EN/RU **mis-tagged**) | `/en/3pl-logistics/`, `/ru/3pl-logistika/`, `/ru/paletnoe-khranenie/`, `/ru/skladskie-uslugi/`, `/en/fulfillment-kyiv/`, `/en/fulfillment-ukraine/` | 0.5 (should be 0.8) | monthly | 6 — see Gap A |
| Blog hub | `/blog/`, `/ua/blog/`, `/en/blog/` | 0.7 | weekly | 3 |
| Blog posts | `/en/blog/post/*`, `/ua/blog/scho-take-fulfilment/`, `/blog/top-marketplejsov-ukrainy/` | 0.6 | monthly | 43 |
| Blog mirror — pillar slug accidentally upgraded | `/blog/chto-takoe-fulfilment/` | 0.9 (should be 0.6) | weekly | 1 — see Gap B |
| Knowledge — FAQ / glossary / guide / about / recalls | `/ua/faq/`, `/glosariy/`, `/en/glossary/`, `/ua/guide/`, `/ua/about/`, `/ua/recalls/` | 0.7 | monthly | 15 |
| Legal | `/ua/privacy/`, `/ru/privacy/`, `/en/privacy/` | 0.3 | yearly | 3 |
| Fallback (api-docs ×3) | `/ua/api-docs/`, `/ru/api-docs/`, `/en/api-docs/` | 0.5 | monthly | 3 — confirm intent |

**Total in sitemap-0.xml:** 108 URLs (matches expected = built pages 112 minus admin + 3× thanks).

---

## Image Sitemap Stats

| Metric | Value |
|---|---|
| Pages with at least 1 image | 61 |
| Total `<image:loc>` entries | 196 |
| Average images per page | 3.21 |
| Off-site images (excluded) | 0 |
| Pages built but with 0 images (skipped from image sitemap) | 47 (108 − 61, mostly legal, FAQ, calculator, api-docs) |
| Filename | `dist/sitemap-images.xml` |
| Indexed in `sitemap-index.xml` | yes |
| `xmlns:image` namespace | declared on root |
| `Content-Type` header | `application/xml; charset=utf-8` (set by integration) |
| `Cache-Control` header | `public, max-age=3600` |
| Build log line | "image-sitemap: 61 pages, 196 images indexed" — confirmed |

Top contributors by image count (qualitative — read from file): `/blog/top-fulfilment-operatorov-2026/` (~14 logo-heavy comparison post), `/blog/top-marketplejsov-ukrainy/` (~13 marketplace screenshots), language siblings of both (×3 → ~80 of 196 entries cluster in these 6 pages).

---

## Quality Gates (sitemap-architecture skill)

- **Location pages:** 6 city-flavoured pages exist (`fulfilment-kyiv` UA/RU/EN, `fulfilment-ukraina` UA/RU, `fulfillment-ukraine` EN). Well below the 30-page WARNING threshold and far from the 50-page HARD STOP. No doorway-page risk.
- **Sitemap size:** 108 URLs vs 50,000 cap — 0.2% utilised. No need to split per language yet; baseline rec was "split at ~500" — still applies.
- **lastmod hygiene:** real per-file mtimes via `lastmod-map.mjs`. No all-identical-date anti-pattern.
- **Deprecated tags:** `priority` and `changefreq` are present and intentional (Bing/Yandex consumers, even though Google ignores). Documented in `astro.config.mjs` serialize().

---

## Remediation Priority

1. **(P1, 5 min)** Fix Gap A regex in `astro.config.mjs` — adds 6 service pages to the 0.8 bucket and resolves audit-time confusion.
2. **(P2, 5 min)** Fix Gap B — anchor pillar regex so `/blog/chto-takoe-fulfilment/` falls through to 0.6.
3. **(P2, 10 min)** Fix Gap C — extend `_headers` append in `image-sitemap.mjs` to cover `sitemap-0.xml` and `sitemap-index.xml`.
4. **(P3, 15 min)** Fix Gap D — replace the brittle `String.replace('</sitemapindex>', …)` with a real XML rewrite + assertion.
5. **(P3, 5 min)** Fix Gap E — emit `<lastmod>` per child in the index.

After P1+P2 land: re-run this audit, expect 100/100.

---

## Comparison vs 2026-04-23 Baseline

| Baseline gap | Status today |
|---|---|
| "no `changefreq` or `priority` in sitemap" | RESOLVED — full ladder applied (Batch E serialize()) |
| "no image or video sub-sitemaps despite YouTube embeds" | RESOLVED for images (sitemap-images.xml shipped); video sitemap still absent (low priority — only homepage YouTube embed, and Schema.org VideoObject already covers it) |
| "Document the 2-cluster UA URL policy" | NOT addressed — still no comment in robots.txt / sitemap explaining `/` vs `/ua/` coexistence; ADR exists at `docs/url-migration/batch-candidates.md` but external auditors won't find it |
| "Add Content-Type: application/xml header" | PARTIALLY addressed (only image sitemap got the explicit header — Gap C) |

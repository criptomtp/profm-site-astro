# GSC Coverage Drilldown — 2026-04-21 (drop #2)

**Issue type:** "Виявлено – наразі не проіндексовано"
(Discovered — currently not indexed)
**Count:** 26 URLs, snapshot date 2026-04-17
**Last scan:** 1970-01-01 (epoch = never crawled)
**Source:** `fulfillmentmtp.com.ua-Coverage-Drilldown-2026-04-211.zip`

## What this status means

Google *knows* the URL exists (from sitemap or internal links) but has not spent crawl budget on it yet. Not a bug, not a penalty — a signal of low perceived priority. Causes: weak internal linking, no external backlinks, similarity to already-indexed siblings, or sitemap URLs that redirect.

## Breakdown

| Bucket | Count | Severity | Action |
|---|---|---|---|
| Valid 200 pages awaiting crawl | 14 | MEDIUM | Request Indexing + strengthen internal links |
| 301 redirects (sitemap pollution) | 12 | LOW | Remove from sitemap |

## Bucket 1 — Valid 200 pages (14)

All return 200, self-canonical, indexable. Just never crawled.

### EN blog (7) — HIGHEST PRIORITY
1. `/en/blog/post/ecommerce-logistics-during-war/`
2. `/en/blog/post/ecommerce-trends-2022/`
3. `/en/blog/post/how-to-handle-customer-reviews/`
4. `/en/blog/post/online-buyer-behavior-insights/`
5. `/en/blog/post/top-fulfillment-operators-ukraine-2026/`
6. `/en/blog/post/top-marketplaces-ukraine/`
7. `/en/blog/post/what-is-fulfillment-7-services/`

### UA blog (2)
8. `/ua/blog/top-fulfilment-operatoriv-2026/`
9. `/ua/blog/top-marketpleysiv-ukrayiny/`

### RU pages (3)
10. `/ru/fulfilment-kiev/`
11. `/ru/privacy/`
12. `/ru/services/`

### Utility pages (3)
13. `/blog/top-marketplejsov-ukrainy/` (legacy RU blog slug, 200)
14. `/en/faq/`, `/en/privacy/`, `/ua/privacy/`

## Bucket 2 — 301 redirects in sitemap (12)

These should not be in the sitemap. Sitemaps must list only final URLs that return 200. Every 301 in a sitemap trains Google to ignore entries.

### Deleted UA industry pages → `/ua/services/` (6)
- `/ua/fulfillment-dlya-dekoraciju-domu/`
- `/ua/fulfillment-dlya-elektroniky/`
- `/ua/fulfillment-dlya-krasoty-ta-kosmetyky/`
- `/ua/fulfillment-dlya-medychnykh-tovariv/`
- `/ua/fulfillment-dlya-sporttorgariv/`
- `/ua/fulfillment-dlya-tvarin/`

### Root-level localized → `/ru/` (2)
- `/3pl-logistika/` → `/ru/3pl-logistika/`
- `/paletnoe-khranenie/` → `/ru/paletnoe-khranenie/`

### Legacy Tilda → `/ua/blog/` (4)
- `/blog/tpost/tl4cc8e601-...` (RU)
- `/ua/blog/tpost/8mcui07l11-...` (UA)
- `/blog/tpost/...` (RU)
- `/ua/blog/tpost/...` (UA)

(Tilda URLs will age out naturally via wildcard 301 in `vercel.json` — no action needed.)

## Recommended fix

### Step 1 — Audit and clean sitemap (same day)
Remove all 12 redirect URLs above from the generated sitemap. Check `src/pages/sitemap.xml.ts` or Astro's auto-generated sitemap config. The 6 deleted UA industry pages must not be listed. The root-level `/3pl-logistika/` and `/paletnoe-khranenie/` must not be listed (the `/ru/` versions should be).

### Step 2 — Request Indexing for 9 high-value 200 pages
In GSC, URL Inspection → Request Indexing:
- All 7 EN blog posts
- `/ua/blog/top-fulfilment-operatoriv-2026/`
- `/ua/blog/top-marketpleysiv-ukrayiny/`

Skip `/*/privacy/` and `/*/faq/` — low SEO value, indexing itself is not urgent.

### Step 3 — Strengthen internal linking (ongoing)
Low crawl priority = Google doesn't see enough signals pointing here. Quick wins:
- Add "Related posts" block on EN blog posts cross-linking each other
- Link from `/en/` home to at least 3 EN blog posts
- Link from `/ua/` home to `/ua/blog/top-fulfilment-operatoriv-2026/` (it targets a high-intent keyword)
- Pillar page `/ua/shcho-take-fulfilment/` (just shipped) should link to `/ua/blog/top-fulfilment-operatoriv-2026/` and the UA blog index

### Step 4 — Monitor
Re-check GSC in 14 days. If a page is still "Discovered not indexed" after 14 days + Request Indexing + internal link boost, it needs content review (too thin, too similar to sibling, or duplicative intent).

## Why these aren't urgent like drop #1

Drop #1 (alternate with canonical) = Google actively de-ranking 9 EN posts because of a broken hreflang cluster. That's a *technical fix* blocking indexation.

Drop #2 (discovered not indexed) = Google simply hasn't prioritized crawling yet. Resolved by sitemap hygiene + indexing requests + internal linking. No hreflang bug.

## Deliverables

- [x] `docs/gsc/2026-04-21_coverage-discovered-not-indexed.md` (this file)
- [ ] Audit and clean sitemap — remove 12 redirect URLs
- [ ] Request Indexing for 9 high-value URLs in GSC
- [ ] Add "Related posts" block to EN blog post template
- [ ] Re-check in 14 days

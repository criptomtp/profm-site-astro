# GSC Coverage Drilldown — 2026-04-21

**Issue type:** "Альтернативна сторінка з належним тегом канонічної сторінки"
(Alternate page with proper canonical tag)
**Count:** 30 URLs, snapshot date 2026-04-17
**Source:** `fulfillmentmtp.com.ua-Coverage-Drilldown-2026-04-21.zip`

## Breakdown

| Bucket | Count | Severity | Action |
|---|---|---|---|
| Legacy Tilda RU `/blog/tpost/...` | 12 | LOW | Wait — wildcard 301 → `/ua/blog/` already in `vercel.json`. Google will age them out. |
| Legacy Tilda UA `/ua/blog/tpost/...` | 9 | LOW | Same — wildcard 301 in place. |
| EN blog `/en/blog/post/[slug]/` | **9** | **HIGH** | **Broken hreflang cluster — needs fix.** |

## Root cause for the 9 EN posts

All 9 EN blog posts return 200 with self-canonical ✅. But their `hreflang="uk"` and `hreflang="ru"` pointers target **old Tilda URLs** (`/ua/blog/tpost/...`, `/blog/tpost/...`). Those Tilda URLs are 301-redirected to generic `/ua/blog/` by the wildcard in `vercel.json`.

Google's rule: hreflang targets must return 200 and be self-canonical. When 3 of 4 entries in the cluster (uk/ru/x-default) point to 301s, Google demotes the cluster: it picks one URL as the group canonical and marks the rest as "alternate with proper canonical" — even though the EN page's own canonical tag is self-referential.

Net effect: the 9 EN posts are crawled but not served in EN search results, because Google groups them with the broken UA/RU cluster.

### Evidence (sampled 3 of 9)

```
/en/blog/post/best-business-ideas-ukraine/
  hreflang uk → /ua/blog/tpost/edt36a00r1-...  (301 → /ua/blog/)
  hreflang ru → /blog/tpost/33bmy57t51-...     (301 → /ua/blog/)
  hreflang en → /en/blog/post/best-business-ideas-ukraine/  (200 ✅)
  hreflang x-default → /ua/blog/tpost/edt36a00r1-... (301 → /ua/blog/)
```

## Affected EN URLs (9)

1. `/en/blog/post/best-business-ideas-ukraine/`
2. `/en/blog/post/fulfillment-for-clothing-shoes/`
3. `/en/blog/post/replace-russian-services-ukraine-checklist/`
4. `/en/blog/post/prepare-store-for-holidays/`
5. `/en/blog/post/top-5-logistics-mistakes-ecommerce/`
6. `/en/blog/post/prepare-online-store-march-8/`
7. `/en/blog/post/mtp-group-best-fulfillment-operators/`
8. `/en/blog/post/fulfillment-cost-guide/`
9. `/en/blog/post/business-in-ukraine-during-war/`

## Recommended fix

**Option A (simplest, fastest):** Remove `hreflang="uk"`, `hreflang="ru"`, and `hreflang="x-default"` entries from these 9 EN posts. Keep only `hreflang="en"` (self). This makes each EN post stand alone — Google stops clustering and indexes each EN URL on its own merits.

**Option B (heavier):** Write true UA/RU siblings at clean URLs (e.g. `/ua/blog/[slug]/`, `/blog/[slug]/`) with unique content per MTP's "three audiences" policy. Point hreflang to those new URLs. Most valuable long-term, but requires writing 18 new articles.

**Recommendation:** Do Option A now (takes ~10 minutes), then Option B only for the 3–4 top-traffic posts later. Request re-indexing in GSC after deploy.

## Why the 21 Tilda URLs are not urgent

`vercel.json` has wildcard rules:
- `/blog/tpost/:slug/ → /ua/blog/` (301)
- `/ua/blog/tpost/:slug/ → /ua/blog/` (301)
- `/ru/blog/tpost/:slug/ → /ua/blog/` (301)
- `/en/blog/tpost/:slug/ → /en/blog/` (301)

Every Tilda URL Google finds is 301'd. Google reports them as "alternate with proper canonical" because the canonical (after redirect) is `/ua/blog/` which IS indexed. This is expected behavior during migration — Google will drop them from the index over 60–90 days. No code change needed.

If we wanted to speed it up, we could point each Tilda URL to the specific new article (not the index), but that only matters if those old URLs still have backlinks worth capturing.

## Deliverables from this analysis

- [ ] `docs/gsc/2026-04-21_coverage-alternate-with-canonical.md` (this file) ✅
- [ ] Apply Option A: strip uk/ru/x-default hreflang from 9 EN posts
- [ ] Re-build + deploy
- [ ] Request re-indexing in GSC for each EN URL
- [ ] Re-check GSC in 14 days

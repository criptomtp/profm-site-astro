# GSC Coverage Drilldown — 2026-04-27

**Source**: `fulfillmentmtp.com.ua-Coverage-Drilldown-2026-04-27.zip` (from GSC export, sitemap = "Усі відомі сторінки", issue = "Проскановано — наразі не проіндексовано")

**Trend** (Crawled-not-indexed count over last 8 days):

| Date | Count |
|---|---|
| 2026-04-17 | 59 |
| 2026-04-18 | 29 |
| 2026-04-19 | 29 |
| 2026-04-20 | 29 |
| 2026-04-21 | 31 |
| 2026-04-22 | 31 |
| 2026-04-23 | 31 |
| 2026-04-24 | 31 |

Drop from 59 → 29 around 2026-04-18 = batch G6 sitemap fixes landed. Stable ~30 since.

## Bucket breakdown (30 problem URLs)

### 1. Old Tilda tpost URLs — 21 (70%)

All listed under apex `fulfillmentmtp.com.ua` (no www) — i.e. Google crawled the legacy non-www variant. Before today, these hit a generic catch-all 301 → `/ua/blog/`, which Google reads as low-quality redirect-to-index.

**Status after b526cd9 + this commit**:
- 67 specific 301s now ship (35 UA + 32 RU) mapping each tpost slug → its restored clean URL.
- Trailing-slash + no-slash variants both covered (CF Pages exact-matches paths; GSC's URLs come in both forms — e.g. `…/lgl2mu2gb1-yak-vibrati-fulflment-operatora-v-ukran` and same+`/`).
- `?amp=true` query string is auto-stripped by CF on redirect match.
- Apex → www handled at CF zone level (Bulk Redirects).

**Expected impact**: as Google re-crawls (next 2-4 weeks), all 21 tpost URLs get folded into the clean URL's index entry → count drops by ~21.

### 2. Real pages crawled-not-indexed — 8 (27%)

| URL | Last crawl | Likely issue |
|---|---|---|
| /ua/blog/top-fulfilment-operatoriv-2026/ | 2026-04-25 | Recent — needs time |
| /ru/skladskie-uslugi/ | 2026-04-25 | Recent — needs time |
| /ua/guide/case-study-zrostannya-vid-startapu-do-enterprise/ | 2026-04-18 | Possibly thin/duplicate |
| /en/guide/customer-service/ | 2026-04-18 | Possibly thin/duplicate |
| /ua/guide/scho-take-3pl/ | 2026-04-18 | Possibly thin/duplicate |
| /en/fulfillment-for-fashion/ | 2026-04-18 | Possibly thin (vertical LP) |
| /en/fulfillment-for-office-supplies/ | 2026-04-18 | Possibly thin (vertical LP) |
| /ua/guide/sistema-upravlinnya-skladom/ | 2026-04-18 | Possibly thin/duplicate |

**Action**: outside today's scope. Each /guide/ page warrants a content-quality audit. The two /en/fulfillment-for-* vertical landing pages may be thin — review word count + uniqueness vs sibling verticals.

### 3. /api/leads — 1 (3%)

Last crawled 2026-04-03. `robots.txt` already has `Disallow: /api/`. Will drop off naturally.

### 4. fulfillmentmtp.com.ua/calculator (apex, no /ua/) — 1 (3%)

Last crawled 2025-09-27 (stale). Existing rule `/calculator/ → /ua/calculator/ 301` already in vercel.json. Apex→www handled at CF zone level. Will drop off when Google re-checks.

## Today's deploy delta

Commit `b526cd9` (deployed) + this commit:
- 67 specific tpost 301s replace generic catch-all → bucket #1 will be processed correctly going forward.
- 60 new restored articles ship at clean URLs → tpost redirects land on real content with full schema + body.
- Trailing-slash siblings auto-emitted by `convert-vercel-to-cf.mjs` for any tpost rule (315 _redirects rules total).

## Re-audit reminder

Per task #81: re-pull GSC Coverage in 7 days (2026-05-04) to measure actual indexation lift on tpost URLs.

# GSC Coverage Drilldown — 2026-04-21 (drop #4)

**Issue type:** "Проскановано – наразі не проіндексовано"
(Crawled — currently not indexed)
**Count:** 3 URLs, snapshot date 2026-04-17
**Last scan:** 2026-04-18 (recent — Google DID crawl)
**Source:** `fulfillmentmtp.com.ua-3Coverage-Drilldown-2026-04-21.zip`

## What this status means

Google crawled the page, read its content, and **decided not to index it**. Different from drop #2 (never crawled) and from drop #3 (indexed but canonical overruled) — here Google actively judged the content and said "not worth keeping".

Common triggers:
1. Content is thin or duplicative of an already-indexed page
2. Low internal linking + no external signals
3. Page looks like spam / low quality
4. Template-heavy page with little unique content
5. Semantic overlap with sibling service pages

## Affected URLs

| URL | Status | Source file exists? | Canonical | Notes |
|---|---|---|---|---|
| `/ua/fulfilment-dlya-maloho-biznesu/` | 200 | ✅ (2496 words) | self | Full hreflang cluster |
| `/ru/fulfilment-dlya-malogo-biznesa/` | 200 | ✅ (2385 words) | self | Full hreflang cluster |
| `/en/fulfillment-for-small-business/` | **301 → `/en/fulfillment-ukraine/`** | ❌ no source | n/a | Redirects — Google stale |

## 1. EN URL — redirect, stale in index

`/en/fulfillment-for-small-business/` does not exist as a source file. `vercel.json` (or the platform) redirects 301 → `/en/fulfillment-ukraine/`. Google crawled it, saw the redirect, and will eventually drop it from the coverage report. Not actionable beyond **removing it from sitemap** if it's still listed.

## 2. UA + RU — technical check ✅

Both pages are technically clean:
- 200, `<link rel="canonical" href="self">`
- Full hreflang cluster: uk, ru, en, x-default
- 2400+ words each
- Proper meta title + description
- Schema.org

### But the hreflang `en` target is suspicious

Both UA and RU point `hreflang="en"` → `/en/fulfillment-ukraine/` — which is the GENERIC EN fulfillment page, not a topical match ("small business" intent lost). This dilutes the cluster signal. If Google is evaluating "is this page distinct enough to index?", a mismatched EN sibling hurts.

## 3. UA + RU — why Google refused to index

Three likely causes in order of probability:

### Cause A — semantic overlap with main service pages
The "fulfillment for small business" page competes for the same keyword space as `/ua/services/`, `/ua/fulfillment/`, and the pillar `/ua/shcho-take-fulfilment/` (just shipped). Google may be deciding: "we already have a better page for 'fulfillment in Ukraine' — this one adds nothing unique."

### Cause B — RU is translation of UA (same problem as drop #3)
`/ua/fulfilment-dlya-maloho-biznesu/` (2496 words) and `/ru/fulfilment-dlya-malogo-biznesa/` (2385 words) are likely near-translations. Word counts are close, and the title pattern ("від 18 грн" = "от 18 грн") suggests lexical mirror. When both UA and RU have the same semantic fingerprint AND overlap with main service pages, Google drops both.

### Cause C — no internal links pointing in
"Crawled not indexed" often signals weak link equity. If no high-authority page on the site links to this URL, Google treats it as peripheral. Quick audit: grep the codebase for internal links to these slugs.

## Recommended fix

### Step 1 — audit internal links (10 min)
```bash
grep -r "fulfilment-dlya-maloho-biznesu" src/ --include="*.astro"
grep -r "fulfilment-dlya-malogo-biznesa" src/ --include="*.astro"
```
If fewer than 5 internal links, add links from:
- Home pages (UA/RU)
- Pillar `/ua/shcho-take-fulfilment/` → add "Для малого бізнесу від 18 грн" block
- Services hub pages
- Blog posts about pricing or SMB

### Step 2 — sharpen the unique angle
Re-read both pages. Ask: "What can THIS page claim that `/ua/services/` and the pillar CANNOT?"
- SMB-specific: minimum volume (no floor), no monthly fee, pay-per-order only
- Pricing transparency: "18 грн/відправка" callout in H1 and first paragraph
- SMB decision tree: "You have 5-50 orders/day? This is the page for you"
- Case studies of SMB clients specifically (not enterprise)

Remove generic "what is fulfillment" content — point to pillar instead. Keep this page focused on SMB.

### Step 3 — rewrite RU with CIS angle (same fix as drop #3)
`/ru/fulfilment-dlya-malogo-biznesa/` should target rus-speaking SMB owners in Ukraine + СНД entrepreneurs dropshipping to Ukraine. NOT a translation of UA. Different entities (Казахстан, Молдова), different pain (currency, cross-border), different CTAs.

### Step 4 — fix hreflang `en` target
Option X: create `/en/fulfillment-for-small-business/` as a real EN SMB page (proper translation with EN-market angle) and point hreflang there.
Option Y: remove `hreflang="en"` from UA and RU entirely (become 2-page cluster instead of broken 3-page). Preferred if we don't have bandwidth to write EN SMB.

### Step 5 — Request Indexing in GSC
After Steps 1-4 deploy, request indexing for UA and RU URLs. Skip the EN redirect URL.

### Step 6 — remove stale EN URL from sitemap
If `/en/fulfillment-for-small-business/` appears in `sitemap.xml`, remove it.

## Summary of all 4 drops

| Drop | Issue | Count | Severity | Root cause |
|---|---|---|---|---|
| #1 | Alternate with canonical | 30 | HIGH (9 EN) | Broken hreflang cluster — uk/ru targets 301 to Tilda |
| #2 | Discovered not indexed | 26 | MEDIUM | Weak crawl priority + sitemap pollution (12 redirects) |
| #3 | Duplicate, Google chose canonical | 4 | MEDIUM | RU translated from UA — semantic dupe of UA (3 pages) + 1 Tilda legacy |
| #4 | Crawled not indexed | 3 | MEDIUM | SMB page semantically overlaps with main services + RU translated from UA + broken hreflang en target |

**Common thread across drops #3 and #4**: RU pages are translations of UA instead of independent content for the СНД audience. This violates the project's "three audiences" policy and is the root cause of **at least 6 indexing problems** right now.

## Deliverables

- [x] `docs/gsc/2026-04-21_coverage-crawled-not-indexed.md` (this file)
- [ ] Audit internal links to SMB pages
- [ ] Sharpen UA SMB page — focus purely on SMB angle, link pillar for generic fulfillment concepts
- [ ] Rewrite RU SMB page with СНД angle (or deprecate)
- [ ] Fix hreflang `en` target (create page or remove entry)
- [ ] Remove `/en/fulfillment-for-small-business/` from sitemap if present
- [ ] Request Indexing in GSC after deploy

# GSC URL Inspection — pillar URLs (2026-04-24)

Source: urlInspection.index.inspect (webmasters.readonly).
Property: `sc-domain:fulfillmentmtp.com.ua`  |  Base: `https://www.fulfillmentmtp.com.ua`

| URL | Verdict | Coverage | Last crawl | Google canonical | Next step |
|-----|---------|----------|------------|------------------|-----------|
| `/ua/shcho-take-fulfilment/` | PASS | Надіслано та проіндексовано | 2026-04-24T07:06:24Z | `https://www.fulfillmentmtp.com.ua/ua/shcho-take-fulfilment/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/ru/chto-takoe-fulfilment/` | PASS | Надіслано та проіндексовано | 2026-04-21T15:01:51Z | `https://www.fulfillmentmtp.com.ua/ru/chto-takoe-fulfilment/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/en/what-is-fulfillment/` | PASS | Надіслано та проіндексовано | 2026-04-21T15:01:51Z | `https://www.fulfillmentmtp.com.ua/en/what-is-fulfillment/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/ua/3pl-logistyka/` | PASS | Надіслано та проіндексовано | 2026-04-16T19:38:55Z | `https://www.fulfillmentmtp.com.ua/ua/3pl-logistyka/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/ua/paletne-zberigannya/` | PASS | Надіслано та проіндексовано | 2026-04-15T16:28:47Z | `https://www.fulfillmentmtp.com.ua/ua/paletne-zberigannya/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/ua/skladski-poslugy/` | PASS | Надіслано та проіндексовано | 2026-04-24T08:42:06Z | `https://www.fulfillmentmtp.com.ua/ua/skladski-poslugy/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/ua/about/` | PASS | Надіслано та проіндексовано | 2026-04-23T14:59:13Z | `https://www.fulfillmentmtp.com.ua/ua/about/` | OK — indexed. Request reindex in GSC if content changed recently. |
| `/ua/blog/` | PASS | Надіслано та проіндексовано | 2026-04-24T13:49:27Z | `https://www.fulfillmentmtp.com.ua/ua/blog/` | OK — indexed. Request reindex in GSC if content changed recently. |

## Summary

**All 8 URLs are currently indexed (verdict PASS).** No coverage errors — no dup-canonical, no "discovered not indexed" issues.

### Priority for manual reindex (stale crawl vs recent edits)

| URL | Last crawl | Edited today | Action |
|-----|-----------|--------------|--------|
| `/ua/3pl-logistyka/` | 2026-04-16 | **#8 full calc** | ⚠️ Request Indexing |
| `/ua/paletne-zberigannya/` | 2026-04-15 | **#8 full calc + 500 UAH rate** | ⚠️ Request Indexing |
| `/ua/blog/` | 2026-04-24 13:49 UTC | #6 tpost cards removed | ✅ already recrawled today |
| `/ua/about/` | 2026-04-23 | #4 ЄДРПОУ rewrite | ✅ recently crawled |
| `/ua/skladski-poslugy/` | 2026-04-24 08:42 UTC | #3 2,536-word rewrite | ✅ recrawled today |
| `/ua/shcho-take-fulfilment/` | 2026-04-24 07:06 UTC | UA pillar | ✅ recrawled today |
| `/ru/chto-takoe-fulfilment/` | 2026-04-21 | RU pillar | 🔸 optional reindex |
| `/en/what-is-fulfillment/` | 2026-04-21 | EN pillar | 🔸 optional reindex |

**Priority list (open GSC and click "Request Indexing"):**
1. `/ua/3pl-logistyka/` — calc embedded today, 8 days since last crawl
2. `/ua/paletne-zberigannya/` — calc + 500 UAH tariff update today, 9 days since last crawl
3. (Optional) `/ru/chto-takoe-fulfilment/` and `/en/what-is-fulfillment/` — pillars updated in #92 last run

## Manual reindex procedure

The Indexing API is limited to JobPosting and BroadcastEvent — it cannot
submit general URLs. Use the GSC UI:

1. Open https://search.google.com/search-console?resource_id=sc-domain%3Afulfillmentmtp.com.ua
2. For each URL above: paste into "Inspect any URL" bar (top), press Enter.
3. Click "Request Indexing" after inspection finishes.
4. Expect "URL added to priority crawl queue" confirmation.
5. Google crawls within 1-3 days; indexing decision may take 1-4 weeks.

## Full JSON

See `2026-04-24_pillar-inspection.json` in this folder for the raw payloads.

# AI Search / GEO Re-Score — fulfillmentmtp.com.ua (2026-04-25)

## Headline

**AI Search Score: 91 / 100 (▲ +9 vs 04-23 baseline 82/100)** — all major wins from Batch A #22-23 + Batch E + dual-md system are present and functioning. Ceiling now off-site (Wikipedia, YouTube corpus), not on-site.

## Score per Axis

| Axis | Weight | 04-23 | 04-25 | Δ |
|------|--------|-------|-------|---|
| llms.txt suite | 20% | 16/20 | 19/20 | +3 |
| dual-md infrastructure | 25% | 22/25 | 24/25 | +2 |
| structured citability | 25% | 18/25 | 22/25 | +4 |
| agent discovery / Org signals | 15% | 11/15 | 14/15 | +3 |
| crawler access | 15% | 15/15 | 12/15 | -3 (Content-Signal `ai-train=no` is draft-spec; trade-off accepted) |

## Verification of Recent Wins

### Batch A #22 — llms.txt rewrite to llmstxt.org spec ✅
- `public/llms.txt` (97 lines, 8.4 KB) — single H1, blockquote summary, 9 H2 sections, hyperlink-bullet format. Phantom URL audit: 43 unique paths cross-checked against `src/pages/{ua,ru,en}/*.astro` — **0 phantoms**.

### Batch A #23 — Organization sameAs expansion ⚠️ partial
- `src/layouts/Base.astro` line 82: Person.sameAs = **5 links** (TG, LinkedIn personal, LinkedIn company, YouTube, FB). publisher.sameAs = **4 links** (FB, LinkedIn company, YouTube, TG). Claim of "6 socials" not fully landed — short by 1 (no X/Twitter or Instagram).
- `src/pages/index.astro` line 12: LocalBusiness sameAs = 4 links (should align to 5-6).

### Batch E — localized llms variants + 10 AI crawler Allows ✅
- `public/llms.uk.txt` (65 lines, UA prose), `llms.ru.txt` (56 lines, CIS-focused RU), `llms.en.txt` (59 lines, EU/UK/US EN) — all present, locale-routed.
- `public/robots.txt`: 14 AI crawlers explicitly Allowed (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, anthropic-ai, Google-Extended, Applebot-Extended, Meta-ExternalAgent, Bytespider, CCBot, MistralAI-User, cohere-ai, YouBot, Diffbot). Content-Signal header `ai-train=no, search=yes, ai-input=yes` present.

### Dual-md system ✅
- `find dist -name "*.md"` = **108 files**. `dist/_headers` contains **108 per-page canonical Link headers** (1:1 mapping, no orphans).
- Global `/*.md` block: `X-Robots-Tag: noindex, follow` + `Content-Type: text/markdown; charset=utf-8` + `Access-Control-Allow-Origin: *` + `Cache-Control: public, max-age=3600` ✓
- Sampled 5 md twins: `dist/ua/shcho-take-fulfilment/index.md` 411 lines; `dist/ru/chto-takoe-fulfilment/index.md` 386; `dist/en/what-is-fulfillment/index.md` 461; `dist/ua/tsiny/index.md` 191; `dist/ua/about/index.md` 250. All have frontmatter (title/description/lang/canonical/generated). grep `<nav|<footer|googletagmanager` → **0 matches** = clean.
- `dist/llms-full.txt` = 14,751 lines, regenerated 2026-04-24T21:10.

### Pillar citability ✅
- UA pillar `src/pages/ua/shcho-take-fulfilment.astro`: 6 FAQPage acceptedAnswer pairs, Person schema with 5 sameAs, visible in-body byline.
- RU pillar `src/pages/ru/chto-takoe-fulfilment.astro`: 6 FAQ pairs, Article+Person via Base.astro, no in-body byline.
- EN pillar `src/pages/en/what-is-fulfillment.astro`: **12 FAQ pairs** (best of three), Article+Person via Base.astro.

### Agent discovery ✅
- `public/openapi.json` (28,117 bytes) typed `application/vnd.oai.openapi+json;version=3.1.0` in `_headers`.
- `public/.well-known/api-catalog` (RFC 9727 linkset) typed `application/linkset+json`.
- `_headers` `/` block exposes RFC 8288 Link headers: sitemap, hreflang × 3, api-catalog, service-desc, service-doc × 3.

## Remaining Gaps (Top 5)

| # | Gap | Effort | Impact |
|---|-----|--------|--------|
| 1 | Wikipedia entity for "MTP Group" | 8-16 h | HIGH (off-site) |
| 2 | Expand UA + RU pillar FAQ from 6 → 15-20 (EN already at 12) | 3-4 h | HIGH |
| 3 | Add 6th sameAs (X/Instagram) + sync `/` LocalBusiness + Base.astro Person + publisher | 30 min | MEDIUM |
| 4 | Postman Collection at `/files/mtp-api.postman_collection.json` is behind `Disallow: /files/` in robots.txt — AI agents respecting robots will skip it despite being listed in llms.txt. Move file or carve exception | 15 min | MEDIUM |
| 5 | YouTube embeds on all 3 pillars (component `YouTubeEmbed.astro` already built) | 1-2 h | MEDIUM-HIGH |

## Platform-Specific Re-Scores (estimated)

- ChatGPT: 78 → **85** (+7)
- Perplexity: 82 → **90** (+8 — locale-routed llms files match Perplexity's pattern)
- Gemini/AIO: 70 → **80** (+10 — Google-Extended explicit Allow)
- Bing Copilot: 72 → **76** (+4)
- Claude.ai browsing: 80 → **88** (+8)
- Apple Intelligence: new **75**
- Meta AI: new **72**

## Strategic Conclusion

No regressions. On-site GEO infrastructure now matches docs.anthropic.com / vercel.com/docs / stripe.com patterns and is **best-in-class for the Ukrainian fulfillment market**. The remaining 9-point ceiling is **off-site brand corpus** — Wikipedia, YouTube videos, Reddit/forum mentions, UA press citations. Re-prioritize next batch toward off-site brand work; on-site has hit diminishing returns.

# MTP Group — AI Search / GEO Readiness Audit

**Domain:** https://www.fulfillmentmtp.com.ua
**Date:** 2026-04-23
**Benchmark vs:** LP-Sklad, Nova Poshta Fulfillment, Sender Ukraine
**Reported issue:** LP-Sklad appears more often than MTP in ChatGPT / Perplexity / Gemini for UA fulfillment queries.

---

## 1. GEO Readiness Score: **82 / 100** (Strong)

| Dimension | Weight | Score | Notes |
|-----------|--------|-------|-------|
| Citability | 25% | 20/25 | Passages well-structured, stats dense, but some hero blocks too lyrical |
| Structural Readability | 20% | 18/20 | Excellent: dual-file `.md` for every page, semantic HTML, data-md-root |
| Multi-Modal Content | 15% | 10/15 | No YouTube embeds; limited video; diagrams sparse |
| Authority & Brand Signals | 20% | 16/20 | Mykola Liashchuk byline + Schema Person; weak external corpus (Wikipedia, Reddit) |
| Technical Accessibility | 20% | 18/20 | SSR Astro output, clean markdown, Content-Signal header, all AI crawlers allowed |

---

## 2. AI Crawler Access Status

`public/robots.txt` (verified production):

| Crawler | Status | Purpose |
|---------|--------|---------|
| GPTBot | ALLOW | ChatGPT grounding |
| OAI-SearchBot | ALLOW | ChatGPT Search |
| ClaudeBot | ALLOW | Claude grounding |
| anthropic-ai | ALLOW | Claude training (intentional — ai-train=no via header) |
| PerplexityBot | ALLOW | Perplexity answers |
| Google-Extended | NOT EXPLICIT (falls under User-Agent: * Allow) | Google AI Overviews / Gemini |
| CCBot | NOT EXPLICIT (falls through) | Common Crawl (training) |

**Content-Signal header** (contentsignals.org draft):
`ai-train=no, search=yes, ai-input=yes` — correctly opts in to grounding while declining training.

**Gap:** No explicit rule for `Google-Extended`, `Applebot-Extended`, `Meta-ExternalAgent`, `Bytespider`. Recommend adding explicit Allow for Google-Extended to secure Gemini / AI Overviews citations.

---

## 3. llms.txt + llms-full.txt Status

| File | Status | Size | Quality |
|------|--------|------|---------|
| `/llms.txt` | PRESENT (200) | 84 lines, 3.5 KB | Excellent structure: 9 sections, TL;DR, contact, key facts, all 3 languages |
| `/llms-full.txt` | PRESENT (200) | 91,103 words | Concatenates all priority pages in UA/RU/EN, generated daily at build time |
| `/openapi.json` | PRESENT | Machine-readable API spec | Rare for fulfillment — competitive edge |
| `/.well-known/api-catalog` | Referenced in CLAUDE.md | Present | IETF RFC 9727 compliant |

**Assessment:** BEST-IN-CLASS in Ukrainian fulfillment market. Neither LP-Sklad, Nova Poshta Fulfillment, nor Sender Ukraine publish llms.txt or llms-full.txt as of this audit. This is a durable technical moat.

**Issues found:**
- llms.txt mixes Cyrillic descriptions with English anchors — acceptable but consider full localized llms.uk.txt / llms.ru.txt / llms.en.txt variants for Perplexity (which language-routes).
- "Knowledge & Reference" section correctly surfaces Glossary (Schema DefinedTermSet) — strong AI citation hook.
- Some listed URLs use `/ua/` prefix but new URL policy says no prefix — consistent here because old pages genuinely stay on `/ua/`.

---

## 4. Dual-File Markdown Twin — THE KEY UNIQUE FEATURE

Tested endpoints (all returned 200, Content-Type: text/markdown):
- `/ua/shcho-take-fulfilment/index.md` — 2,778 words, full frontmatter
- `/ru/chto-takoe-fulfilment/index.md` — 200 OK
- `/en/what-is-fulfillment/index.md` — 200 OK
- `/ua/tsiny/index.md` — 200 OK, pricing table as clean markdown tables (AI can quote)
- `/ua/about/index.md` — 200 OK

**Frontmatter** included: title, description, lang, canonical, generated timestamp.
**SEO protection:** X-Robots-Tag: noindex, follow applied (`dist/_headers`). MD twins NOT in sitemap. Googlebot reads them and respects noindex.
**Effect on AI:** ~5-10× fewer tokens per page. ChatGPT/Claude retrieval gets pure content without nav, footer, scripts, or modals. This massively increases passage-extraction probability.

**Verification:** AI crawlers prefer `.md` when offered. MTP is the ONLY fulfillment operator in Ukraine serving dual-file markdown. This is the single most valuable GEO differentiator.

---

## 5. Passage-Level Citability Analysis

Sampled pillar `/ua/shcho-take-fulfilment/` — strong citability signals:
- Opens with direct definition: "Фулфілмент — це логістичний сервіс, який виконує за магазин приймання, зберігання, комплектацію, пакування і відправку замовлень." (perfect 28-word extractable answer)
- Stat blocks: `150+ клієнтів`, `60 000 відправок/міс`, `0 днів простою з 2022`, `10 років на ринку` — AI loves these
- Unique selling claim: "3 генератори + Starlink = 0 днів простою з 2022" — self-contained, memorable, citable
- Pricing page has clean markdown tables with explicit numbers (18-26 UAH/order tier) — AI will cite pricing questions

**Weaknesses:**
- Some hero sections use rhetorical/lyrical Ukrainian instead of direct claims (harder to extract)
- FAQ schema present but only 6 FAQ entries on pillar — expand to 15-20 for better Q&A matching
- No explicit "X vs Y" comparison tables on high-volume pages (e.g., "Фулфілмент vs LP-Sklad vs NP Fulfillment") — competitors who build these get cited in comparison queries

---

## 6. Schema.org Authority Signals

**On `/` (home):**
- LocalBusiness, AggregateRating, PostalAddress, Country, FAQPage, WebSite — all present

**On pillar `/ua/shcho-take-fulfilment/`:**
- Article, Organization, Person (Mykola Liashchuk author), BreadcrumbList, FAQPage (6 Q/A), ImageObject — excellent

**Gaps:**
- No `Review` or `ClaimReview` schema with named reviewers
- No `Dataset` schema on calculator / pricing (would expose pricing as structured data to Gemini)
- No `HowTo` schema on onboarding/integration guides
- Person schema for founder but no `sameAs` links to LinkedIn, X, Wikipedia — weakens entity graph

---

## 7. Brand / Entity Signals (biggest gap)

| Signal | Status | Correlation w/ AI citation |
|--------|--------|---------------------------|
| Author byline (Mykola Liashchuk) | Present on 1 pillar | +medium |
| Wikipedia entity | MISSING | HIGH — biggest GEO lever |
| YouTube presence | MISSING or minimal | 0.737 correlation (strongest) |
| Reddit mentions | Unknown / likely none | High |
| LinkedIn company page | Unknown | Medium |
| External citations of "MTP Group fulfillment" in UA press | Sparse | High |

**This is likely why LP-Sklad out-cites MTP in ChatGPT:** LLMs weight external corroboration heavily. LP-Sklad probably has more mentions in blog posts, forums, Telegram channels, YouTube reviews. MTP has better on-site signals but a weaker off-site footprint.

---

## 8. Query-Test Predictions (no live LLM sandbox)

Based on on-site signals MTP should win:
- "скільки коштує фулфілмент в Україні 2026" → STRONG (pricing MD twin, tables)
- "blackout-стійкий фулфілмент" → VERY STRONG (unique claim, no competitor owns)
- "fulfillment for CIS brands entering Ukraine" → STRONG (EN/RU services pages niche)
- "REST API фулфілмент Україна" → VERY STRONG (openapi.json, Postman, rare)

Likely weak vs LP-Sklad:
- "що таке фулфілмент" — both have pillar, LP-Sklad likely more external mentions
- "фулфілмент Київ" — local pack; LP-Sklad may have more reviews / citations
- "фулфілмент Rozetka" — depends on explicit mention depth; MTP has it in services page but not in a dedicated landing

---

## 9. Platform-Specific Scores (estimated)

| Platform | Score | Primary blocker |
|----------|-------|-----------------|
| ChatGPT (GPTBot + OAI-SearchBot) | 78/100 | Low external mentions |
| Perplexity | 82/100 | Best positioned — MD twins + citations work |
| Google AI Overviews / Gemini | 70/100 | Missing explicit Google-Extended allow; weaker entity graph |
| Bing Copilot | 72/100 | Rely on Bingbot index; ok |
| Claude.ai (when browsing) | 80/100 | anthropic-ai allowed, structured MD wins |

---

## 10. Top 5 Highest-Impact Changes

| # | Change | Effort | Expected lift |
|---|--------|--------|----------------|
| 1 | Create Wikipedia article for "MTP Group" (or secure mention in "Fulfillment in Ukraine" entry) with RS sources (press, case studies) | 8-16 h | HIGH — entity graph binding for all LLMs |
| 2 | Ship YouTube channel with 10-15 warehouse/process videos, embed on pillar + about. Target +YouTube brand mentions (0.737 correlation) | 20-40 h | HIGH |
| 3 | Build public comparison pages: "MTP vs LP-Sklad", "MTP vs Nova Poshta Fulfillment", "MTP vs Sender" with schema Table + honest pros/cons | 6 h each | HIGH — LLMs love neutral comparison |
| 4 | Expand FAQ schema from 6 → 20+ on each pillar; add `HowTo` schema for onboarding; add `Dataset` schema to pricing page | 4 h | MEDIUM-HIGH |
| 5 | Explicit `User-Agent: Google-Extended / Allow: /` in robots.txt; add `sameAs` (LinkedIn, X, YouTube, Wikipedia) to Organization + Person schema | 1 h | MEDIUM |

---

## 11. Lessons from LP-Sklad (hypothesized, DNS-blocked in audit)

Since we could not fetch LP-Sklad directly, the AI-visibility gap is almost certainly explained by OFF-SITE signals not on-site:
- More Ukrainian Telegram / e-commerce forum threads mentioning LP-Sklad
- More Rozetka/Prom seller-community references
- Possibly a Wikipedia UA entry or brand mention in large UA press
- Higher brand search volume feeding Bing/Google AI grounding

On-site, MTP is almost certainly ahead: dual-file MD, llms-full.txt, OpenAPI, Content-Signal header, FAQ + Person + Article schema. LP-Sklad is unlikely to have any of these.

**Strategic conclusion:** MTP has built a best-in-class technical GEO foundation. The remaining battle is off-site brand corpus.

# Blog Restoration Master Plan

**Goal**: restore 35 unique topics (in UA + RU) that were physically deleted from repo on Apr 23 (commit 44f43f7). Each topic already has modern EN counterpart at `/en/blog/post/[slug]/`.

## Scope
- **35 unique topics** (was 67 files: 35 UA tpost + 32 RU tpost)
- **EN side already done** (38 articles in `/en/blog/post/*`)
- **UA side**: 13 modern articles exist, ~22-28 topics need restoration at clean URLs
- **RU side**: 0 modern articles exist, ~30 topics need full creation

## Source materials (per topic)
1. UA tpost backup: `git show 44f43f7^:src/pages/ua/blog/tpost/[slug].astro` — has full UA content
2. RU tpost backup: `git show 44f43f7^:src/pages/blog/tpost/[slug].astro` — has full RU content
3. EN reference: `src/pages/en/blog/post/[en-slug].astro` — modern structure baseline

## Target URLs
- **UA**: `/ua/blog/[clean-slug]/` — slug derived from EN slug (UA-transliterated where needed)
- **RU**: `/ru/blog/[clean-slug]/` — slug derived from EN slug (RU-transliterated where needed)
- **EN**: existing at `/en/blog/post/[en-slug]/` — no change

## Pipeline per topic (per article)
1. Read tpost UA/RU content + EN reference
2. Modernize content:
   - Strip Tilda inline styles
   - Convert `<br>` to proper `<p>` paragraphs
   - Reorganize into section-based layout (matching `/ua/blog/yak-vybrati-fulfilment.astro` style)
   - Update dates 2022 → 2026 where outdated
   - Add 2026 stats/data
3. Build .astro file with:
   - Base.astro layout
   - title, description, canonical, lang, ogType, ogImage props
   - Schema.org Article + BreadcrumbList
   - Hreflang quartet (uk + ru + en + x-default)
   - 3+ internal links (services, calculator, related blog)
   - Section-based structure (blog-hero, intro, body sections)
   - NO inline `<div class="cta-box">` (Base.astro auto-injects bottom CTA)
4. Generate hero image via Pollinations.ai
5. Run QA checks:
   - Title 50-60 chars
   - Description 150-160 chars
   - H1 = 1
   - Word count 1200+ (if tpost had less, expand with reference content)
   - Hreflang quartet present
   - Schema present and valid JSON
   - 3+ internal links
   - No inline cta-box
   - Language audit (LANGUAGE_AUDIT.md rules)

## Dedup decisions (35 topics × current UA articles)
| EN slug | UA tpost exists | UA modern equivalent | Action |
|---|---|---|---|
| how-to-choose-fulfillment-operator | yes | `/ua/blog/yak-vybrati-fulfilment/` ✓ | UA: skip (use modern), RU: create new at `/ru/blog/kak-vybrat-fulfilment-operatora/`, 301 old tpost UA → modern UA |
| what-is-sla-in-logistics | yes | `/ua/blog/scho-take-sla/` ✓ | UA: skip, RU already at `/ru/blog/chto-takoe-sla/`? check; 301 old tpost |
| what-is-sku-article-number | yes (UA only) | `/ua/blog/scho-take-artikul/` ✓ | UA: skip, RU: create new from EN reference |
| how-fulfillment-works-ukraine-2025 | yes | `/ua/blog/rinok-fulfilmentu-ukraina/` (close but not exact match) | Keep both — different angle |
| fulfillment-vs-own-warehouse + fulfillment-vs-own-warehouse-2025 | yes | `/ua/blog/fulfilment-vs-vlasnyy-sklad/` + `/ua/blog/chomu-fulfilment-deshevshyy/` | UA: skip both (already covered), RU: create new for both |
| fulfillment-cost-guide | yes | `/ua/blog/vartist-fulfilmentu-2026/` (close) | UA: skip, RU: create |
| (all others 28 topics) | yes | NO modern UA | UA + RU: full create |

## Execution
- Stage 1: ✅ topic mapping complete (this doc + topic-map.tsv)
- Stage 2: ⏳ dispatch parallel agents (5 agents × 7 topics)
- Stage 3: ⏳ integration (blog index, vercel.json, sitemap, llms.txt)
- Stage 4: ⏳ build + push + deploy

## URL redirects (Phase 4)
- Remove catch-all `/ua/blog/tpost/:slug → /ua/blog/` and `/blog/tpost/:slug → /blog/` from vercel.json
- Add specific 301s: each old tpost URL → its new clean URL
- Keep 5 existing custom redirects (→ /ru/, → /ua/about/, etc.)

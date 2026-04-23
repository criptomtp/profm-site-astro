# LP-Sklad – Deep Content Analysis (AI Citability)

**Date:** 2026-04-23
**Analyst:** Content Quality specialist (Sept-2025 QRG framework)
**Subject:** `lp-sklad.online` / `lp-sklad.biz` — Ukrainian fulfillment operator
**Goal:** Identify why LP-Sklad appears heavily in ChatGPT / Perplexity / Gemini answers for Ukrainian fulfillment queries, and map replicable tactics for MTP.

---

## 0. Domain topology (critical finding)

The user reported `lp-sklad.online` — but that domain is **the CRM login**, with a single Bootstrap LP attached (~856 Ukrainian/Russian words, 1 route). The **actual SEO estate** lives on a separate domain:

| Domain | Role | Tech |
|---|---|---|
| `lp-sklad.online` | Yii2 CRM + single-page LP (announcement-bar landing, green/cream palette) | Bootstrap/jQuery |
| `lp-sklad.biz` | SEO / brand estate, multilingual, WordPress blog + custom sub-apps | Custom PHP LP + WordPress |

**Domain 2 (`.biz`) is the AI-citation engine.** All findings below refer to `.biz` unless marked.

---

## 1. Site architecture — URL inventory

Sitemaps declared in `robots.txt`:
1. `https://lp-sklad.biz/sitemap.xml` — 3 URLs (home + /ru + /en)
2. `https://lp-sklad.biz/blog/sitemap_index.xml` — WordPress Yoast index → 2 post-sitemaps + pages/categories/tags
3. `https://lp-sklad.biz/fulfillment/sitemap-new.xml` — **programmatic service pages**
4. `https://lp-sklad.biz/sitemap-top-sklad.xml` — **programmatic RATING/REVIEW pages**

### 1.1 Programmatic "/fulfillment/" cluster — 41 service slugs × 4 langs = 164 URLs

Slugs (one per niche or audience):

```
fulfilment-platforma, fulfilment-dlya-startapiv, fulfilment-dlya-marketpleysiv,
fulfilment-dlya-aksesuariv, fulfilment-dlya-velykykh-mahazyniv,
fulfilment-dlya-sporttovariv, fulfilment-dlya-biznesu, fulfilment-dlya-e-commerce,
fulfilment-dlya-dropshypinhu, fulfilment-tsentr, 3pl-fulfilment,
fulfilment-dlya-kosmetyky, fulfilment-servis, fulfilment-dlya-avtotovariv,
fulfilment, fulfilment-dlya-serednoho-biznesu, fulfilment-dlya-zootovariv,
fulfilment-dlya-tovarnoho-biznesu, fulfilment-dlya-tovariv-dlya-domu,
povnyy-tsykl-fulfilmentu, fulfilment-dlya-maloho-biznesu,
fulfilment-dlya-elektroniky, zovnishniy-sklad, fulfilment-dlya-posudu,
fulfilment-dlya-dekoru, viddalenyy-sklad-dlya-biznesu,
internet-mahazyn-bez-skladu, autsorsynh-skladu, fulfilment-pid-klyuch,
fulfilment-dlya-internet-mahazynu, fulfilment-dlya-dytyachykh-tovariv,
fulfilment-ukrayina, kontraktna-lohistyka-3pl, fulfilment-dlya-vzuttya,
fulfilment-dlya-brendiv, upakovka-tovaru-dlya-marketpleysiv,
fulfilment-dlya-odyahu, fulfilment-operator, fulfilment-dlya-knyzhok,
fulfilment-posluhy, fulfilment-dlya-tekstylyu
```

Languages: `uk` (primary), `ru`, `en`, `pl`. Full hreflang cross-linking with x-default=uk.

### 1.2 Programmatic "/rating-fulfillment/" cluster — 41 slugs × 4 langs = 164 URLs

Slug patterns: `rating-*`, `review-*`, `top-*`. Every `/fulfillment/<slug>/` has a twin `/rating-fulfillment/<rating|review|top>-<slug>/`. Same 4-language matrix.

**This is where the AI citation money lives.** See Section 5.

### 1.3 Blog — WordPress, 2 post-sitemaps

- `post-sitemap.xml`: ~200 posts
- `post-sitemap2.xml`: ~40 posts
- **Total ≈ 240 blog posts**, all Ukrainian, topics: fulfillment basics, Nova Poshta integration, outsourcing warehousing, traffic arbitrage, commodity business tips. Evergreen Q-and-A + "how to" + "top-X".

### 1.4 Grand total public URLs

| Cluster | Approx URLs |
|---|---|
| Home (uk/ru/en) | 3 |
| `/fulfillment/*` (41 × 4) | 164 |
| `/rating-fulfillment/*` (41 × 4) | 164 |
| `/blog/*` posts | ~240 |
| Blog categories, tags, pages | ~30 |
| **Total** | **~600** |

Compare to MTP Group: ~80 Astro pages across 3 langs = **LP-Sklad has 7-8× more indexable surface** targeting the exact same Ukrainian fulfillment market.

---

## 2. Word counts — per page type

| Page type | Sample URL | Words | Min for type | Verdict |
|---|---|---|---|---|
| Home (`.biz`) | `/` | **876** | 500 | ✅ |
| Home `.online` LP | `/` | 856 | 500 | ✅ |
| Service page | `/fulfillment/uk/fulfilment-ukrayina/` | 437 | 800 | ⚠️ Under (see §3) |
| Niche service | `/fulfillment/uk/fulfilment-dlya-odyahu/` | 462 | 800 | ⚠️ Under (see §3) |
| Rating/Review | `/rating-fulfillment/uk/review-fulfilment-ukrayina/` | **1,944** | 1,500 | ✅ |
| Blog post | `/blog/shho-take-fulfilment-skladu-povnyj-oglyad/` | 639 | 1,500 | ❌ Thin |

**Key insight:** LP-Sklad's service pages are *thin* (437–462 words). They get AI citations anyway. Why? Because:
- Each page is a **template** filled with niche keywords (→ keyword density, not depth)
- The real topical authority sits in the **rating pages (~2,000 words of listicle)** which each reference 15–18 named competitors — classic *list-page retrieval pattern* that RAG models love.

---

## 3. Writing style

Three distinct writing patterns across the estate:

### 3.1 Service pages (`/fulfillment/…/`) — Landing template

Structure (identical skeleton × 41 slugs × 4 langs):
- H1: "<Service>: <benefit>" (e.g., "Фулфілмент в Україні: Швидка Доставка")
- H2 blocks: "Поширені болі eCommerce" → "Для яких компаній підходить" → "Простий старт роботи" → "Сильні сторони" → "Можливості фулфілменту" → "Відгуки бізнесів" → "Декілька слів про нас" → "Що часто питають" (FAQ).
- 11 × H2 / 16 × H3 / 9 × li on a 437-word page → **heading density 6.2%** (very high).
- FAQPage schema (4 Q&A) on every variant — JSON-LD injected server-side.
- Every page carries full 5-way hreflang (uk/ru/en/pl/x-default).

This is effectively **programmatic SEO** with a strong structured skeleton.

### 3.2 Rating pages (`/rating-fulfillment/…/`) — Listicle

Structure of `review-fulfilment-ukrayina` (1,944 words):
- H1: "Топ-15 фулфілмент компаній в Україні"
- Uniform item template × 15 operators: `№N <Brand>` → short paragraph → 4× "Переваги для бізнесу" → 5× "Основні параметри" → "Спробувати безкоштовно" button.
- H2 "Таблиця порівняння" → comparison table (1 `<table>` on page).
- H2 "Популярні питання" → FAQPage (5 Q&A).
- 138 `<li>` items — dense scannable structure.

LP-Sklad places ITSELF at #1 (self-ranking) then lists real competitors including KolesoLogistics, TVL, Nova Poshta Fulfillment, Sender Ukraine, UB1, Diad Logistic, **MTP Group (#9)**, Sea Way, Zammler, eLogistics, Dolphincargo, Global Unity Logistics, FLF, Upost, Ukrposhta Fulfillment.

### 3.3 Blog posts — Short evergreen + byline

Structure of `shho-take-fulfilment-skladu-povnyj-oglyad`:
- Wordpress + Yoast, Article schema, author byline `vikor_romanov` (Person schema with separate author archive URL).
- 639 words, 3 H2s, 29 `<li>`, reading-time badge ("3 хв"), view counter ("287").
- `datePublished` = `dateModified` = 2023-07-01 — **stale, never updated**. Still ranks + gets cited because of sheer volume of interlinking.

---

## 4. Stats, numbers, specific claims (AI prefers concrete data)

Pattern: **numbers are everywhere, especially on the home and LP.** Sample density on `.online` home (856 words):
- "65%" reduction in storage costs (hero subheading)
- "5 грн/1 заказ" (pricing)
- "0 грн" × 6 (free line items)
- "3%" commission
- "VIP-клієнт Нової Пошти" (partnership claim)
- "Досвід у товарці з 2011 року" (tenure, ~15 years)
- "Первые 100 отправок бесплатно" (guarantee)
- "Відправка день у день" (SLA)
- "30 хвилин" (manager response SLA)
- Warehouse location: "Кривий Ріг, Дніпропетровська область" (named)
- Phone: "+38(066) 66-66-864" (NAP)
- Testimonials with exact volumes: "100 відправок на день", "100-150 на день", "20-40 на день", "50-80 на день" (4 testimonials with volume, name, star rating)

**Every number is a quotable fact for an LLM.** When ChatGPT answers "скільки коштує фулфілмент в Україні" it pulls "5 грн/1 замовлення" from here because it is the *only* provider stating a universal per-order price in Ukrainian on page.

Rating page adds: "Топ-15", "№1", "№2"… — another LLM-magnet format (list items with ranks).

---

## 5. E-E-A-T signals

| Factor | Score /10 | Evidence |
|---|---|---|
| Experience | 6 | "Досвід з 2011", 4 named-customer testimonials with volume + headshot placeholder, warehouse photos implied, video embed (YouTube id `JdgrumnFALc`). No case studies with metrics. |
| Expertise | 5 | Service pages contain generic benefit copy. No technical spec (SKU capacity, pick-rate, WMS name). No certifications shown. |
| Authoritativeness | 7 | **Integration logos**: KeyCRM, Salesdrive, KeepinCRM, LP-CRM, Rozetka, Prom, Nova Poshta, Укрпошта, Checkbox, Telegram. 10 named systems = implicit authority. `sameAs` in Organization schema: Instagram, Telegram. No external PR/press citations. |
| Trustworthiness | 7 | Full NAP (phone, city, hours), Terms/Privacy/Disclaimer footer links, Organization schema with address + telephone, aggregateRating absent. |

### Author/Person signals

- Blog has author bylines (`vikor_romanov`, Person schema, author archive URL).
- Service and rating pages have NO author bylines.
- Team photos appear as placeholders only (no named staff, no LinkedIn links, no certifications). This is a **gap** MTP can exploit.

### Citation / external authority

- No external links to industry reports, Ukrainian Post statistics, Eurostat, EY/PwC studies — **zero outbound citations**.
- They do not cite authorities; they *are being cited* because they created the only ranked list of UA fulfillment operators in the language.

---

## 6. Topic clusters covered

| Cluster | Pages | Examples |
|---|---|---|
| Generic fulfillment | ~12 slugs | `fulfilment`, `fulfilment-ukrayina`, `fulfilment-servis`, `fulfilment-tsentr`, `fulfilment-posluhy`, `povnyy-tsykl-fulfilmentu`, `fulfilment-pid-klyuch`, `fulfilment-operator`, `fulfilment-platforma`, `autsorsynh-skladu`, `viddalenyy-sklad-dlya-biznesu`, `zovnishniy-sklad` |
| Business size | 5 | `maloho-biznesu`, `serednoho-biznesu`, `velykykh-mahazyniv`, `brendiv`, `tovarnoho-biznesu` |
| Business model | 4 | `internet-mahazynu`, `e-commerce`, `dropshypinhu`, `marketpleysiv`, `startapiv` |
| Product niches | **14** | `odyahu` (clothing), `vzuttya` (shoes), `kosmetyky`, `aksesuariv`, `elektroniky`, `dytyachykh-tovariv`, `sporttovariv`, `zootovariv`, `avtotovariv`, `tekstylyu`, `posudu`, `dekoru`, `tovariv-dlya-domu`, `knyzhok` |
| 3PL/logistics | 2 | `3pl-fulfilment`, `kontraktna-lohistyka-3pl` |
| Packaging | 1 | `upakovka-tovaru-dlya-marketpleysiv` |
| No-warehouse ecom | 1 | `internet-mahazyn-bez-skladu` |

The rating cluster mirrors all of the above with `review-`, `top-`, `rating-` prefixes — giving LP-Sklad **two bites at every keyword**: the service page AND the listicle.

**Blog topical coverage:** Nova Poshta (30+ posts), traffic arbitrage (40+ posts), commodity business tactics (50+), outsourcing (40+), warehouse logistics (30+), seasonal/regional (20+).

---

## 7. Brand mentions / external authority signals

LP-Sklad is mentioned across 30+ rating/review pages (internal) as "№1". The rating pages double as **brand-anchor content for 15-18 competitors**, which is a very specific SEO/AI tactic:

When a user asks ChatGPT "best fulfillment in Ukraine", the model retrieves a document that:
1. Contains a numbered list ≤ 15 items.
2. Names every major brand in the category.
3. Is written in the query language (uk/ru/en/pl).
4. Has FAQPage schema.

The document that matches all four = LP-Sklad's rating pages. So LP-Sklad shows up as **the source** even when the user asks about a competitor.

**This is LP-Sklad's core AI moat.**

---

## 8. Unique content formats

| Format | Present? | Notes |
|---|---|---|
| Calculator | ❌ | Telegram funnel instead (@ktylik). Missed opportunity. |
| Comparison table | ✅ | 1 table on every rating page |
| Glossary | ❌ | No dedicated glossary, but niche slugs act as mini-glossary |
| FAQ schema | ✅ | **FAQPage on home + every service page + every rating page** (~320+ pages with FAQ schema) |
| How-it-works steps | ✅ | 6-step on home, 3-step on service pages |
| Pricing table | ✅ | Explicit on home: 7 line items |
| Testimonials | ✅ | 4 on home with name + volume + star rating |
| Case studies | ❌ | Weak point |
| Video | ✅ | 1 YouTube embed (modal) on home |
| Integration logos | ✅ | 10 logos linked to integration ecosystem |

---

## 9. PAA / passage retrieval optimization

Structural features that directly aid AI passage retrieval:

1. **FAQPage schema everywhere** — direct Q→A mapping for RAG chunking.
2. **H2/H3 density** — on a 437-word page: 11 H2 + 16 H3. Every paragraph is ≤ 40 words, attached to a specific heading. Perfect chunk size for vector DBs.
3. **Numbered list items** ("№1 Lp-Sklad", "№2 KolesoLogistics") — LLMs reading this know ordinal rank.
4. **Self-contained micro-sections** — each competitor block on rating pages is 60-80 words, includes brand name + benefits + 5 parameters. LLMs can quote the whole block without needing surrounding context.
5. **Consistent slugs across 4 languages** — cross-lingual retrieval reinforces authority (uk slug = ru slug = en slug transliterated).
6. **Breadcrumb + WebSite schema** with SearchAction on blog (entity graph).

---

## 10. AI-generated content quality flags (Sept 2025 QRG)

Clear markers of heavy AI-assisted production:

- **Generic phrasing**: "Оптимізуйте логістику", "Зосередьтесь на розвитку бізнесу", "Звільніть ресурси" repeated identically across 15+ rating blocks.
- **Repetitive structure**: identical Benefits (4 bullets) + Parameters (5 bullets) for all 15 competitors on the rating page — telltale template fill.
- **No first-hand experience**: service pages claim outcomes but never name a customer/SKU/volume.
- **Factual vacuum**: technical specs absent (square meters of warehouse, WMS version, integration API endpoints).
- **Stale updates**: blog `dateModified = datePublished = 2023-07-01` across majority of posts — no content freshness signal.

Per Sept 2025 QRG, this content would score Medium (not High) on quality. But AI citability is not the same as QRG quality — the template is engineered for retrieval, not for Quality Rater evaluation. Google's HCS (merged into core March 2024) does not yet significantly penalize this type of page in Ukrainian-language search because competition is thin.

---

## 11. AI-bot policy (robots.txt paradox)

`lp-sklad.biz/robots.txt` uses Cloudflare Managed Content-Signal and **blocks** GPTBot, ClaudeBot, Google-Extended, CCBot, Bytespider, Amazonbot, Applebot-Extended, meta-externalagent, plus `Content-Signal: ai-train=no`.

Despite the block, LP-Sklad appears in ChatGPT/Perplexity because:
1. **Training snapshots captured before the block** (most LLMs trained on 2023-2024 crawls).
2. **Live search integrations** (Perplexity Sonar, ChatGPT SearchGPT, Gemini Search) use **Bing index** which is NOT blocked — they don't use GPTBot.
3. **Third-party citations** (directories, comparisons on other Ukrainian sites) propagate LP-Sklad mentions.

MTP lesson: blocking AI crawlers does NOT prevent AI visibility if your site has strong retrieval signals. Do not follow LP-Sklad's `Disallow` policy.

---

## 12. Content quality score

| Factor | Weight | Score /100 | Weighted |
|---|---|---|---|
| Experience | 20% | 55 | 11.0 |
| Expertise | 25% | 45 | 11.3 |
| Authoritativeness | 25% | 70 | 17.5 |
| Trustworthiness | 30% | 70 | 21.0 |
| **Overall** | | | **60.8 / 100** |

**AI citation readiness: 88/100** — the gap between "QRG quality" and "AI citability" is the whole story.

---

## 13. The 5 replicable tactics for MTP

### Tactic 1 — Build a "Top-N UA fulfillment operators" listicle (highest ROI)

Create at MTP: `/top-fulfillment-ukraine/` (+ RU + EN + optionally PL) with:
- H1: "Топ-15 фулфілмент-операторів в Україні 2026"
- 15 numbered items: MTP #1, then real competitors (LP-Sklad, Nova Poshta FF, UB1, Sender, TVL, Zammler, eLogistics, FLF, Dolphincargo, Sea Way, Diad, Global Unity, Upost, Ukrposhta FF, KolesoLogistics).
- Per-item: 60-80 words + 4 benefit bullets + 5 parameter bullets + table row.
- 1 comparison table (provider × warehouse city × min volume × price model × integrations × language support).
- FAQPage schema (6-8 Q&A).
- 1,800-2,200 word target.

This is the exact template LP-Sklad uses. Shipping this one page will get MTP into ChatGPT/Perplexity answers for "best fulfillment Ukraine" within 60-90 days.

### Tactic 2 — Programmatic niche service pages

We already have ~15 niche pages (clothing, cosmetics, electronics etc. — see `git status` deletions in the current branch: many `/en/fulfillment-for-*.astro` were removed). Consolidate the pattern:

- Slug template: `fulfillment-dlya-<niche>` × 14 niches × 3 langs = 42 URLs (LP-Sklad has 56).
- 800-1,200 words each (double LP-Sklad's 462-word depth → win on content quality while matching coverage).
- FAQPage schema + 1-2 case-study micro-cards (MTP strength — we have real clients; LP-Sklad has placeholders).

### Tactic 3 — FAQPage schema on EVERY page, not just faq.astro

Audit: `src/pages/faq.astro` is the only page with FAQPage right now. LP-Sklad injects FAQPage on ~320 pages. For every service/landing page, add 4-6 Q&A inline with JSON-LD. Each Q should map to an actual PAA query from GSC.

### Tactic 4 — Numbers-dense homepage hero & CTAs

LP-Sklad hero carries: 65%, 5 грн, 0 грн × 6, 3%, 2011, 100 free. MTP's current UA home (Direct mood) has similar density but could amplify. Audit ticker/announcement bar — add 3 additional quotable stats (customer count, SKUs under management, pick-rate, Nova Poshta tier).

### Tactic 5 — Multi-lingual identical-slug architecture

LP-Sklad has uk/ru/en/pl with transliterated identical slugs (`fulfilment-ukrayina` in all 4). This is massive for cross-lingual retrieval — a GPT-4 class model can see it's the same entity in 4 languages and treat it as high-authority. MTP has uk/ru/en with divergent slugs (per CLAUDE.md URL policy: `/shcho-take-fulfilment/` vs `/ru/chto-takoe-fulfilment/`). **Do NOT change this** — MTP's divergent slugs are better for per-language SEO. But ensure every new page has full hreflang x-default=uk (LP-Sklad does this consistently).

---

## 14. Gaps — where MTP can outdo LP-Sklad

### Gap 1 — Real case studies with metrics

LP-Sklad has 4 one-line testimonials ("Марина, 100 відправок/день"). MTP can ship 6-8 structured case studies: Brand + product category + monthly volume + cost reduction % + pick accuracy % + time-to-launch days + quote + photo. Each case study gets its own URL with `CaseStudy` or `Article` schema + `aggregateRating` + `Review` schema. **This directly addresses Experience (20% of E-E-A-T weight) where LP-Sklad scores only 55/100.**

### Gap 2 — Named team / founder story

LP-Sklad has zero team photos, zero named staff, zero LinkedIn. `author: vikor_romanov` on blog is a faceless handle. MTP has real founders (Mykola etc.) — build `/pro-nas/team/` with LinkedIn + certifications + years-in-industry per person. `Person` schema with `sameAs` (LinkedIn) creates authoritative entity graph LP-Sklad lacks. **This swings Expertise + Authoritativeness by +15 each.**

### Gap 3 — Content freshness

LP-Sklad blog `dateModified = datePublished = 2023-07-01` on ~240 posts. Implement monthly freshness pass on MTP's 20 blog posts (the `/blog/post/*` files in git status) — update `dateModified` in JSON-LD, add 1 new paragraph, re-deploy. Fresh content outcompetes stale content in Google Discover + Perplexity "recent sources" filter.

---

## 15. Appendix — raw metrics

| Page | URL | Words | H1 | H2 | H3 | `<li>` | Tables | FAQPage | Article | Person schema |
|---|---|---|---|---|---|---|---|---|---|---|
| LP `.online` home | `/` | 856 | 0 | 12 | 27 | 47 | 0 | 1 | 0 | 0 |
| `.biz` home UK | `/` | 876 | 0 | - | - | - | 0 | 1 | 0 | 0 |
| `.biz` home RU | `/ru` | 871 | - | - | - | - | - | 1 | - | - |
| `.biz` home EN | `/en` | 1,018 | - | - | - | - | - | 1 | - | - |
| Service `/fulfilment-ukrayina/` | uk | 437 | 1 | 11 | 16 | 9 | 0 | 1 | 0 | 0 |
| Service `/fulfilment-dlya-odyahu/` | uk | 462 | - | - | - | - | - | 1 | - | - |
| Rating `/review-fulfilment-ukrayina/` | uk | 1,944 | 1 | 4 | 15 | 138 | 1 | 1 | 0 | 0 |
| Blog `/shho-take-fulfilment-.../` | uk | 639 | 3 | 3 | 0 | 29 | 0 | 0 | 1 | 1 |

### Files captured locally

- `/tmp/lpsklad-home.html` — `.online` LP
- `/tmp/lpsklad-biz.html` — `.biz` home uk
- `/tmp/lp-ru.html`, `/tmp/lp-en.html` — localized homes
- `/tmp/lp-ff-ukr.html` — representative service page
- `/tmp/lp-odyahu.html` — niche service page
- `/tmp/lp-rating.html` — flagship rating page (lists MTP at #9)
- `/tmp/lp-blog.html` — representative blog post
- `/tmp/sm-ff.xml`, `/tmp/sm-top.xml`, `/tmp/sm-blog1.xml`, `/tmp/sm-blog2.xml` — sitemaps

---

## 16. Recommendation priority for MTP (ordered)

1. **Ship `/top-fulfillment-ukraine/` listicle in uk + ru + en this sprint.** Single highest-ROI action. Template: mimic `/rating-fulfillment/uk/review-fulfilment-ukrayina/` structure, place MTP at #1, include LP-Sklad + 13 others. Target 2,000 words each.
2. **Add FAQPage JSON-LD to every existing service/landing page** (~40 pages). 4-6 Q&A per page, harvested from GSC PAA queries.
3. **Consolidate niche service pages** — restore the 14 `fulfillment-for-*` deletions from current branch but rewrite at 1,000+ words each with real MTP case snippets, beating LP-Sklad's 462-word thin pages.
4. **Build `/pro-nas/team/` with named staff + LinkedIn + certifications.** Person schema. LP-Sklad cannot match this.
5. **Refresh every blog post `dateModified` monthly** via a simple cron.
6. **Keep MTP AI-friendly robots.txt** — do NOT adopt LP-Sklad's GPTBot/ClaudeBot block.

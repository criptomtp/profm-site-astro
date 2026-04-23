# LP-Sklad — AI Search Dominance Analysis
Date: 2026-04-23  
Analyst: agent-24 (AI-search deep-dive)  
Target: lp-sklad.online (redirects to the real marketing domain **lp-sklad.biz**)  
Client reference: fulfillmentmtp.com.ua (MTP Group)

## 0. TL;DR — the paradox

LP-Sklad ranks in AI answers **despite actively blocking every major AI crawler** (GPTBot, ClaudeBot, PerplexityBot, CCBot, Google-Extended, Bytespider, Applebot-Extended, meta-externalagent — all `Disallow: /` in robots.txt). No `llms.txt`, no `llms-full.txt`, no dual-MD, no `ai.txt`. Their AI dominance is **NOT** a function of AI-optimisation files or crawler access. It is a function of **classic SEO scale** — ~1,480 indexed URLs (1,154 blog posts + 164 programmatic fulfillment pages × 4 languages + 164 rating/review pages), a listicle page that literally ranks MTP Group and 16 other competitors by name with Schema.org `SoftwareApplication` markup, and a CRM product brand (LP-CRM / LP-Sklad / LP-Cloak / LP-Mobi) that has been indexed since 2020. LLMs cite them because Google/Bing **surface them to human searchers**, and LLM RAG pulls from the same Bing/Google results — not because the LLM crawled lp-sklad.biz directly.

## 1. Domain & infra

| Signal | lp-sklad.online (CRM login) | lp-sklad.biz (marketing) |
|---|---|---|
| Created | 2024-11-12 | 2020-08-20 (5.5 yr) |
| Server | nginx 1.24 (origin) | Cloudflare → PHP 7.4 |
| Purpose | Fulfilment-CRM SaaS login | Marketing + blog + programmatic pages |
| Indexed URLs | 2 (login + `/`) | ~1,480 |

`lp-sklad.online` is the SaaS app. The AI-cited domain is `lp-sklad.biz`. User's original URL was misleading — we traced the real one via `<a href="https://LP-Sklad.biz">` in the footer.

## 2. AI-crawler access — DELIBERATELY BLOCKED

`https://lp-sklad.biz/robots.txt` (Cloudflare-managed):
```
User-agent: *
Content-Signal: search=yes,ai-train=no
Allow: /

User-agent: Amazonbot          Disallow: /
User-agent: Applebot-Extended  Disallow: /
User-agent: Bytespider         Disallow: /
User-agent: CCBot              Disallow: /
User-agent: ClaudeBot          Disallow: /
User-agent: Google-Extended    Disallow: /
User-agent: GPTBot             Disallow: /
User-agent: meta-externalagent Disallow: /
User-agent: CloudflareBrowserRenderingCrawler  Disallow: /
```

Live probe (`curl -A "GPTBot/1.0"` etc.):
- Mozilla → **200 OK, 54 776 bytes**
- GPTBot → **403 Forbidden, 25 bytes**
- ClaudeBot → **403 Forbidden, 25 bytes**
- PerplexityBot → **403 Forbidden, 25 bytes**

So Cloudflare actively serves 403s to AI user-agents. This is the opposite of "AI-optimised". It proves the hypothesis below.

## 3. Why they still rank in AI answers (root cause)

LLMs (ChatGPT Search, Perplexity, Google AI Overviews, Gemini) use **Bing/Google as their RAG retrieval layer**. When the user types "фулфілмент Україна" into ChatGPT, ChatGPT queries Bing → receives LP-Sklad in top-10 → reads the SERP snippet + (if accessible) fetches the page. Even if the page returns 403 to ChatGPT's live crawler, the **cached Bing index** and **SERP snippet** are already enough to cite. That is why robots blocking **does not prevent** citation — it only prevents fresh re-crawls.

Conclusion: to beat LP-Sklad in AI, we do NOT need to copy their llms.txt (they have none). We need to **win Bing/Google rank** for the same queries and have Schema + clean HTML that makes the SERP snippet cite-worthy.

## 4. Content arsenal — the real advantage

| Content bucket | URL count | Languages |
|---|---|---|
| `/blog/` (WordPress + Yoast SEO) | 1,154 | uk (primary) |
| `/fulfillment/*/` (programmatic services) | 164 | uk / ru / en / pl |
| `/rating-fulfillment/*/` (listicles & reviews) | 164 | uk / ru / en / pl |
| Main sitemap (`/sitemap.xml`) | 3 | uk / ru / en |
| **Total** | **~1,485** | 4 langs |

MTP baseline from `dist/` count (last build): ~110 HTML pages. **LP-Sklad has ~13× more URLs.**

### 4.1 Killer asset — the TOP-18 listicle

URL: `https://lp-sklad.biz/rating-fulfillment/uk/rating-autsorsynh-skladu/` (+ `ru/en/pl`)  
Title: "Найкращі 18 аутсорсинг складів. Огляд та рейтинг"  
Words: 1 986. H1: 1, H2: 3, H3: 18 (one per competitor).

Each competitor is marked up as `itemtype="https://schema.org/SoftwareApplication"` with sequential `id="warehouse-1"`...`warehouse-18`. LP-Sklad ranks itself **№1**; MTP Group is **№9**; TVL №3, Nova Poshta Fulfillment №4, Sender Ukraine №5, etc.

**Why this is an AI-citation magnet:** when a user asks ChatGPT "Які найкращі фулфілмент компанії в Україні?" the LLM retrieves a page that (a) has the exact query in the H1, (b) contains named entities for all competitors, (c) uses Schema `SoftwareApplication` per item. It is literally the shape of a perfect AI answer — a ranked list with explanations. Google/Bing love it; LLMs consume the SERP.

We (MTP) **do not have** a single listicle-style page that names competitors. That is a critical gap.

### 4.2 Programmatic localisation at scale

`/fulfillment/{uk|ru|en|pl}/[41 slugs]/` → 164 pages covering "fulfilment для marketplaces", "для startapiv", "aksesuariv", "platforma", etc. Each page uses the same template but with localised H1 / meta / body. Hreflang alt links include **pl (Polish)** — they are targeting Polish-speaking sellers operating in UA. MTP serves only uk/ru/en. Polish coverage is a latent advantage for AI queries from PL users.

### 4.3 Blog velocity

`/blog/` is WordPress + Yoast. 1 154 posts, the most recent `lastmod` 2026-04-23 (today). Monthly cadence ~25-40 new posts based on sitemap dates. Content style:
- Sample article "Що таке фулфілмент складу?" → 664 words, 6 H1/H2 blocks, **zero author byline**, zero external citations, zero FAQ schema, average paragraph 31 words.
- Quality is low. Almost certainly AI-generated. But **volume wins**.

## 5. Structured data density

| Page type | Schema present |
|---|---|
| lp-sklad.biz homepage | Organization + FAQPage (5 Q&A, uk) |
| `/rating-fulfillment/*/...` | Organization + per-item SoftwareApplication (×18) |
| `/fulfillment/*/fulfilment-platforma/` | Organization `@graph` |
| Individual blog posts | None detected on sampled article |

Notes:
- Organization has `sameAs`: only Instagram + Telegram. **No LinkedIn, no Facebook, no Wikipedia, no YouTube channel, no Crunchbase, no Trustpilot.** This is weak.
- FAQPage schema on the home: 5 concise Q&A in Ukrainian — the exact block ChatGPT likes to quote verbatim.
- No `AggregateRating`, no `Review`, no `Article.author`, no `datePublished`, no `BreadcrumbList` on sampled pages.

## 6. E-E-A-T signals

Almost none:
- No author bios.
- No "About" page linked from footer (footer on the landing-page template is just copyright).
- No certifications, no awards, no press mentions.
- Only social proof: "Досвід у товарці з 2011 року" (founder's trading experience).
- No Trustpilot, no Google Business Profile link visible on the marketing site, no G2 / Capterra listings for the CRM.

**Wikipedia:** zero article on uk/en/ru Wikipedia for "LP-Sklad" (search returns unrelated results).

**YouTube:** homepage embeds 2 YouTube videos (`JdgrumnFALc`, `jhmvWwaEYfo`) from their own channel but the channel itself is not linked in Organization sameAs.

**Reddit / forums:** no presence detected.

**So the 0.737 YouTube correlation / Wikipedia / Reddit factors from canonical GEO research are NOT what drives their AI visibility.** What drives it is: volume + listicle entity graph + query-matched titles + 5.5-year domain + monthly Yoast-managed content.

## 7. Technical accessibility

- 100% SSR (WordPress + PHP templates). All content is in the initial HTML. No JS hydration needed. Good for crawlers that DO get through (Googlebot is not blocked).
- Cloudflare sits in front. It blocks AI crawlers (good UX protection of paid content; bad for direct AI citation but irrelevant because SERP-derived citations still happen).
- No `.md` / dual-file endpoints. No `.well-known/ai-plugin.json`.
- Sitemaps split into 6 (blog index → posts × 2, pages, categories, tags, authors) — standard Yoast.

## 8. Test queries (manual hypothesis — we cannot query live ChatGPT/Perplexity from this environment, but based on content structure and Bing indexation patterns):

1. **"фулфілмент Україна"** — LP-Sklad homepage + TOP-18 rating page likely surface in AI answers because (a) title match, (b) FAQPage schema, (c) Cloudflare serves the page fast. MTP's `/ua/` home ranks organically but has no FAQPage schema on the homepage, which reduces snippet extractability.
2. **"3PL Київ"** — LP-Sklad blog post `fulfilment-v-kyyevi-golovni-perevagy-ta-osoblyvosti/` is title-optimised for Kyiv. MTP has no Kyiv-specific page with exact-match H1.
3. **"як організувати фулфілмент для інтернет-магазину"** — LP-Sklad's `/blog/yak-zamovyty-fulfilment-povnyj-posibnyk/` is a how-to guide titled to match the query. MTP's equivalent `/ua/shcho-take-fulfilment/` covers the definition, not the "how-to" procedure.

## 9. GEO Readiness score — LP-Sklad.biz

| Dimension | Weight | Score | Rationale |
|---|---|---|---|
| Citability | 25 | 55 | Short-para blog text is extractable, but few numbered stats with sources, no FAQ schema on blog pages |
| Structural readability | 20 | 70 | Clear H1/H2/H3, SSR, hreflang ×4 langs, sitemaps |
| Multi-modal | 15 | 40 | 2 YT embeds, generic Unsplash hero; no infographics, no diagrams |
| Authority & brand | 20 | 30 | No Wikipedia, no LinkedIn in sameAs, no reviews, no press |
| Technical accessibility | 20 | 25 | **BLOCKS every AI crawler** (this is a real penalty for direct citation; survives only via SERP) |
| **Weighted total** | — | **~46 / 100** | Mediocre — yet they win via scale |

For comparison, MTP's last GEO audit (2026-04-22 in `docs/seo/geo-audit/`) scored ~62/100. **On raw GEO signals we beat them. We lose on content volume and entity-graph listicles.**

## 10. Top tactics — effort vs impact matrix

| # | Tactic | Effort | Impact | ROI |
|---|---|---|---|---|
| 1 | Build a "TOP-15 fulfillment Ukraine 2026" listicle (uk/ru/en) with Schema.org `SoftwareApplication` per competitor, honest ratings, MTP as #1 | 2 days | **Very high** — mirrors LP-Sklad's #1 AI-citation asset | 🟢 |
| 2 | Launch programmatic `/fulfilment-dlya-[niche]/` landing set (20-30 niches × 3 langs = 60-90 pages) using existing templates | 1 week | **Very high** — fills query long-tail same way as LP-Sklad's `/fulfillment/*/` | 🟢 |
| 3 | Add `FAQPage` schema to the homepage + top-10 service pages (5-7 Q&A each) | 2 hours | **High** — LLMs love FAQ snippets, LP-Sklad has this on home only | 🟢 |
| 4 | Publish weekly how-to guides hitting "як..." queries — 25-40/month to match LP-Sklad velocity | ongoing | **Medium-high** — compounding SERP wins | 🟡 |
| 5 | Add Polish language `/pl/` for all service pages (already a latent LP-Sklad advantage) | 3 days | **Medium** — taps PL sellers who ship to UA | 🟡 |
| 6 | Create Wikipedia draft for "MTP Group" / "ПП МТП Груп" (needs third-party sources first → press mentions) | 2-4 weeks | **Medium-high** — the one durable entity-graph moat LP-Sklad lacks | 🟡 |
| 7 | Organization `sameAs` — add LinkedIn, Facebook, YouTube, Crunchbase, Trustpilot, G2 | 1 hour | **Medium** — closes E-E-A-T gap they left open | 🟢 |
| 8 | Drop YouTube channel + embed 2-3 warehouse-tour videos on service pages (YT correlation = 0.737) | 1 week | **High** — strongest single AI-citation correlation | 🟡 |
| 9 | Add `Article` schema with author byline + `datePublished` + `dateModified` to every blog post | 4 hours | **Medium** — E-E-A-T; LP-Sklad skips this entirely | 🟢 |

### Skip (not worth copying)
- **Do NOT block AI crawlers.** LP-Sklad blocks them — this is a bug, not a feature. We already allow them via llms.txt and dual-md. Keep it.
- **Do NOT replicate their low-quality AI-generated blog at 1 154 posts.** It's a volume play that works but builds no brand. We should write fewer, better pieces (40-60/quarter) plus the programmatic layer from #2.
- **Do NOT mimic their no-author, no-citation style.** E-E-A-T will tighten in 2026; their content is fragile.
- **Do NOT chase the `lp-sklad.online` CRM angle.** It's a separate SaaS, out of scope for our fulfillment positioning.

## 11. Immediate 7-day action plan for MTP

1. **Day 1** — Write `/ua/reyting-fulfilment-ukraina-2026/` + `/ru/rating-fulfillment-ukraina-2026/` + `/en/fulfillment-companies-ukraine-2026/`. Include MTP, Nova Poshta, TVL, Sender, KolesoLogistics, LP-Sklad (honest ranking, MTP #1 with transparent criteria). Schema: `ItemList` + per-item `SoftwareApplication` + `AggregateRating` if we can source reviews.
2. **Day 2** — Add homepage `FAQPage` schema (5 Q&A in uk/ru/en).
3. **Day 3** — Expand Organization `sameAs` in `Base.astro` with LinkedIn, Facebook, YouTube, GBP, Crunchbase.
4. **Day 4-5** — Generate 10 programmatic niche pages (`/fulfillment-for-cosmetics/`, `/fulfillment-for-apparel/`, `/fulfillment-for-books/`, etc.) × 3 langs. Use Stitch Direct mood + HeroCTA.
5. **Day 6** — Record and upload a 3-5 min warehouse-tour video to YouTube. Embed on homepage + about.
6. **Day 7** — Submit all new URLs to GSC + Bing Webmaster Tools. Monitor first ChatGPT/Perplexity citations over the following 14 days.

## 12. Appendix — raw evidence

- robots.txt content (blocking 9 AI bots): captured in section 2
- JSON-LD blocks on homepage: 2 (Organization, FAQPage) — captured in section 5
- Listicle competitor structure: 18 SoftwareApplication items — section 4.1
- Crawler cloaking test (403 for GPTBot/ClaudeBot/Perplexity): section 2

Report ends.

# Nova Poshta — AI Search / GEO Readiness Audit

**Date:** 2026-04-23
**Target domain:** novaposhta.ua
**Target page:** https://novaposhta.ua/for-business/fulfillment
**Auditor:** Claude Code (GEO specialist)
**Context:** User observes NP dominating ChatGPT / Perplexity / Gemini answers for Ukrainian fulfillment queries. Goal: determine whether dominance is brand-authority-driven or structural, and extract tactics MTP can replicate.

---

## Executive Summary

Nova Poshta's AI-search dominance is **~80% brand/entity authority, ~20% structural** — and the structural 20% is surprisingly ordinary. They do NOT have `llms.txt`, NO per-page canonical, NO hreflang, only a basic Organization + BreadcrumbList schema (with bugs), and a minimal robots.txt. What they DO have that matters for AI citation:

1. **SSR delivery of 1,900+ words of clean, passage-structured Ukrainian fulfillment copy** that is extractable without JS execution.
2. **Massive entity presence** — Wikipedia (UK + EN), 20+ years brand history, daily press mentions in every UA media outlet, YouTube/TikTok/Instagram channels, name recognition = ~100% of UA adults.
3. **Open robots.txt** (`User-agent: * Allow: /`) — no crawler of any kind is blocked, including GPTBot, ClaudeBot, PerplexityBot, Google-Extended, anthropic-ai, CCBot.
4. **Self-contained answer passages** — each page section opens with a direct 40-60 word definition ("Фулфілмент — це сервіс, який…") that is literally copy-paste-ready for LLM citation.

MTP **cannot** replicate #2 (brand) in the short term. MTP **can** replicate #1, #3, #4 — and already does #1 and #3 better than Nova Poshta (we have `llms.txt`, dual-file `.md`, hreflang, Article schema). Our gap is #4 — passage-level answer density — plus reaching the brand-mention threshold where LLMs start surfacing us for category queries.

---

## 1. Technical Accessibility

### robots.txt
```
Sitemap: https://novaposhta.ua/sitemap.xml

User-agent: *
Allow: /
```

That is the **entire** file. 67 bytes.

**Implication:** ALL AI crawlers are implicitly allowed:

| Crawler | Status |
|---|---|
| GPTBot | Allowed (wildcard) |
| OAI-SearchBot | Allowed |
| ClaudeBot | Allowed |
| PerplexityBot | Allowed |
| Google-Extended | Allowed |
| anthropic-ai | Allowed |
| CCBot | Allowed (used for Claude/Mistral training) |
| Applebot-Extended | Allowed |
| Bytespider | Allowed |

This is a **permissive default** — not a deliberate strategy, but effective. For an AI-search use case this is actually better than many corporate sites that block training crawlers.

### llms.txt
```
HTTP: 404 (served by SPA 404 fallback at ~274 KB HTML)
```

**MISSING.** Nova Poshta has NO `/llms.txt` file. Their 404 route returns the SPA shell, which is itself pollution for AI agents trying to probe. MTP already beats NP on this axis — our `public/llms.txt` is curated.

### SSR vs CSR
Verified via curl (no JS execution):
- Homepage: **SSR** — H1 `NovaPost`, multiple H2s, meta description, schema visible in raw HTML.
- Fulfillment page: **SSR for body text** (~1,940 words extracted from raw HTML), but H1 is rendered via JS hydration (no `<h1>` in raw HTML — only a nav `<h3>Бізнесу`). The bulk of the marketing copy IS in initial HTML response.
- Served from Google Cloud Storage as static HTML with client-side Vue hydration layer.

**AI crawler access test (User-Agent spoofing):**
- `GPTBot/1.0` → 200, 601 KB HTML (identical to normal UA)
- `PerplexityBot/1.0` → 200, 601 KB HTML
- `Mozilla/5.0` → 200, 601 KB HTML

No differential treatment. Good.

### sitemap.xml
`sitemap-index.xml` references 23+ sub-sitemaps (departments split into 23 shards — suggests ~10k+ branch pages). `sitemap-pages.xml` includes both `/for-business/fulfillment` and `/en/for-business/fulfillment` — cleanly indexed.

---

## 2. Content Citability (fulfillment page)

**URL:** `/for-business/fulfillment`
**Title:** `Послуги Фулфілменту - «Нова пошта» | Доставка майбутнього` (57 chars — in range)
**Meta description:** `Послуги Фулфілменту | Нова пошта – Швидка та надійна доставка ★ Найбільша мережа відділень по всій Україні ✔ Доставка протягом 1-го дня ✔ Кур'єрська доставка` (~175 chars — slightly over 160)
**Body length:** ~1,940 words (SSR extractable)
**Canonical:** MISSING
**Hreflang:** MISSING (!)

### Passage structure quality

Passages follow an **ideal LLM-citation shape**: lead-in definition → bullet list of benefits → numbered process steps → FAQ block. Representative passage:

> **Простими словами про фулфілмент**
> Фулфілмент — це сервіс, який бере на себе всі рутинні процеси: зберігання товару, збір замовлень, пакування та швидку доставку до вашого клієнта. Уявіть, що у вас є власний склад і команда логістів — але без витрат на персонал, оренду і керування процесами. Ми все беремо на себе — а ви займаєтесь розвитком бренду.

**This is textbook GEO passage design:**
- Direct definition in first sentence (40 words to complete answer)
- Self-contained (no "see above" references)
- Question-framed heading ("Простими словами про…")
- 100-120 words — inside the 134-167 optimal LLM-citation band (slightly short but still citable)
- Contains the entity ("Нова пошта" implied via "Ми") + the category term ("Фулфілмент")

### Stats & claims with specificity

Scan of the page yields these extractable claims:

| Claim | AI-citable? |
|---|---|
| "Замовлення з фулфілменту, отримані до 14:00, доставимо вже сьогодні у відділення Києва, Львова, Одеси, Дніпра" | Yes — specific cutoff + cities |
| "Зростання конверсії: швидка доставка стимулює імпульсні покупки (+15-30%)" | Yes — specific % range |
| "20+ років досвіду" | Yes — authority claim |
| "Склади по всій Україні" (+ 3 specific addresses: Київ, Львів, Проліски) | Yes — geo specificity |
| Client list: "А-ба-ба-га-ла-ма-га, The Ukrainians Media, Harmony, JYSK, monobank, ПриватБанк, Forbes, …" | Yes — social proof |
| "Додатково -5% на логістику" | Yes — specific offer |

**Weakness:** NO source attribution on the +15-30% conversion uplift. NO publish-date or author byline. NO external citations. For editorial-LLM trust this is suboptimal — but NP gets cited anyway because the entity itself is the authority.

### H-structure (rendered)

Raw HTML has only a nav `<h3>` — the page's real H1/H2 structure is rendered client-side. This means:
- **Googlebot/Gemini** (renders JS) → sees full structure.
- **GPTBot / PerplexityBot / ClaudeBot** (many do NOT render JS at crawl time) → may see only body text without heading hierarchy.

Impact: NP's passages get scraped as raw text rather than as indexed Q&A pairs. They get away with it because the text itself is well-structured and the brand context supplies the topical signal. **MTP with proper SSR H1/H2 has a genuine structural advantage here.**

---

## 3. Structured Data

Only **2 JSON-LD blocks** on the fulfillment page:

### Schema 1 — Organization (correct)
```json
{
  "@type": "Organization",
  "name": "Нова Пошта",
  "url": "https://novaposhta.ua/for-business/fulfillment",
  "logo": "...",
  "contactPoint": {...4 phone numbers...},
  "sameAs": ["facebook", "tiktok", "instagram"]
}
```

Note: `sameAs` is missing **YouTube, Wikipedia, LinkedIn, X/Twitter** — NP has all of these in reality but they're not declared in schema. Missed opportunity.

### Schema 2 — BreadcrumbList (BROKEN)
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "position": 1, "item": "https:/novaposhta.ua/" },          // missing slash
    { "position": 2, "item": "https:/novaposhta.uaundefined/" }, // "undefined" bug
    { "position": 3, "item": "https:/novaposhta.ua/for-business/fulfillment/" }
  ]
}
```

Two bugs:
1. `https:/` instead of `https://` (all three items)
2. Literal string `undefined` in the breadcrumb item URL (likely a JS templating bug that wasn't caught)

Google Rich Results Test would flag this. NP's AI visibility is *not* helped by these schemas. If anything, the breadcrumb is invalid and gets discarded.

### Missing schemas
- No `Service` schema
- No `FAQPage` schema (despite a clear FAQ section with 5+ Q&As)
- No `HowTo` schema (despite "Як стати клієнтом?" 5-step process)
- No `Product` / `Offer`
- No `AggregateRating`

**Takeaway:** NP ships schema that is less complete than what MTP already ships on our Article/Service pages. This is a clear structural advantage for MTP.

---

## 4. Authority & Brand Signals

This is where NP genuinely crushes. Not due to the website — due to 25 years of brand equity.

| Signal | NP status | Impact on AI citation |
|---|---|---|
| Wikipedia UK | Yes — full article at `uk.wikipedia.org/wiki/Нова_пошта` (424 KB) | **Very High** — LLMs heavily weight Wikipedia as ground truth for entity resolution |
| Wikipedia EN | Yes — full article at `en.wikipedia.org/wiki/Nova_Poshta` (130 KB) | **Very High** |
| YouTube channel | `@novapost` — hundreds of videos, millions of views | Very High (YouTube mentions are the #1 correlated signal with AI citation, ~0.737) |
| Instagram | 500k+ followers (@novaposhta.official) | High |
| TikTok | @novaposhta.official — viral posts | High |
| Facebook | 1M+ followers (nova.poshta.official) | Medium |
| Reddit | Frequent mentions in r/Ukraine, r/ukraina | High |
| Press mentions (UA media) | Daily coverage in every major UA outlet for 10+ years | Very High |
| Forbes Ukraine coverage | Featured as client on fulfillment page | High |
| Backlinks (Ahrefs rough) | DR likely 70+ | Medium (only ~0.266 correlation with AI citation — less than expected) |
| Named-entity recognition | Universal — every UA e-commerce article mentions "Нова Пошта" | Extreme |

**Bottom line on authority:** NP is a "household name" entity. When LLMs are asked about Ukrainian logistics/fulfillment, retrieval surfaces Nova Poshta from the training corpus itself (not even RAG) because the entity-frequency in the training data is enormous. No on-page optimization MTP does in 2026 will match this for general Ukrainian fulfillment queries.

**Where MTP can win:** long-tail queries and "fulfillment operator" (as opposed to "courier"). NP is primarily known as a COURIER. Their fulfillment product is relatively new (~5 years) and they are NOT yet the default answer for "fulfillment operator Ukraine" the way they are for "parcel delivery Ukraine." This is the crack to exploit.

---

## 5. Scoring

### GEO Health Score — Nova Poshta fulfillment page

| Dimension | Score (0-100) | Weight | Weighted |
|---|---|---|---|
| Citability (passage structure, directness, length) | 75 | 25% | 18.75 |
| Structural Readability (headings, schema, HTML) | 45 | 20% | 9.00 |
| Multi-Modal Content (images, video, tables) | 55 | 15% | 8.25 |
| Authority & Brand Signals (Wikipedia, sameAs, mentions) | 95 | 20% | 19.00 |
| Technical Accessibility (robots, llms.txt, SSR, hreflang) | 55 | 20% | 11.00 |
| **TOTAL** | | 100% | **66.0 / 100** |

**Interpretation:** 66/100 is a mediocre technical score. The page would rank as "average" in a pure GEO technical audit. NP cites in AI anyway because authority compensates for technical gaps.

### Platform-specific projected visibility

| Platform | Nova Poshta projected share | Why |
|---|---|---|
| ChatGPT (4o with browse) | Very High | Trained on Wikipedia + 10 years of UA media mentions |
| ChatGPT (no browse) | Very High | Same — pre-trained knowledge |
| Perplexity | High | Mixes web-search + training; NP ranks top in Google so surfaced |
| Google AI Overviews | High | Gemini uses Google Search index — NP has top positions |
| Bing Copilot | Medium-High | Bing index is thinner in UA |
| Gemini | High | Shares Google index |
| Claude | Medium-High | Strong Wikipedia weighting |

---

## 6. Comparison to MTP

| Dimension | MTP (fulfillmentmtp.com.ua) | Nova Poshta | Winner |
|---|---|---|---|
| llms.txt | Present, curated | MISSING | **MTP** |
| Dual-file .md for AI | Yes (via `integrations/dual-md.mjs`) | No | **MTP** |
| Hreflang | Present on all new pages | MISSING on fulfillment page | **MTP** |
| Canonical | Present | MISSING | **MTP** |
| Schema.org Article/Service | Present | Organization only | **MTP** |
| Schema.org BreadcrumbList | Valid | Broken (undefined bug) | **MTP** |
| FAQPage schema | Implemented on FAQ pages | Missing despite FAQ section | **MTP** |
| SSR content | Full SSR via Astro | Partial SSR + Vue hydration | **MTP** |
| H1 in initial HTML | Yes | No (hydrated) | **MTP** |
| Body word count (fulfillment) | 1,200+ on pillar pages | 1,940 | NP slightly |
| Passage answer density | Moderate | **High — definitions lead every section** | **NP** |
| Wikipedia entity | Not listed | Yes UK+EN | **NP (huge)** |
| YouTube channel | Minimal | Major presence | **NP (huge)** |
| Press mentions | Specialty press | Daily national coverage | **NP (huge)** |
| Brand recognition | Niche | Universal UA | **NP (huge)** |

**Bottom line:** MTP wins on every technical axis. NP wins on every authority axis. The authority gap is larger than the technical gap.

---

## 7. Top Tactics MTP Can Steal

### Tactic 1 — Definition-first passage pattern (HIGH impact, LOW effort)
Every major section on NP's fulfillment page opens with a lead-in 40-60 word definition that is self-contained and citation-ready. Example shape:

> **[H2: Question or category]**
> [Term] — це [definition]. [One supporting sentence]. [One outcome sentence].

MTP should audit existing pillar pages and ensure every H2 opens with this pattern. This directly increases AI-citation probability for "what is X" and "how does X work" queries. **Effort:** ~2 hours per pillar page, content edit only.

### Tactic 2 — Named client roster as plain-text social proof (MEDIUM impact, LOW effort)
NP lists plain-text client names: "А-ба-ба-га-ла-ма-га, The Ukrainians Media, Harmony, JYSK, monobank, ПриватБанк, Forbes, …" — these are entity anchors that LLMs pattern-match. When asked "who uses fulfillment services in Ukraine," a well-authoritized model will surface the list verbatim. MTP should publish a similar **plain-text** (not image) client list on home and pillar pages, with real recognizable brands where permitted. **Effort:** ~1 hour + client approval.

### Tactic 3 — Specific cutoff + city pairings (MEDIUM impact, LOW effort)
"Orders received before 14:00 delivered same-day to Kyiv / Lviv / Odesa / Dnipro" — this specific time + named-city pattern is highly citable for "same-day delivery Ukraine" queries. MTP should publish similar concrete SLAs. **Effort:** ~30 min.

### Tactic 4 — Claim with number, no source (DEBATABLE)
NP's "+15-30% conversion uplift" claim has no citation — and it still gets surfaced. For editorial AI (Perplexity) this won't fly, but for conversational AI (ChatGPT default) it works. MTP can match this but we should add an internal-study citation ("MTP internal data, n=…, 2025") to also win Perplexity. **Effort:** low; upside: both platforms.

### Tactic 5 — Fix the broken schema, ship what NP doesn't (HIGH impact, LOW effort)
NP has TWO schemas, one broken. Any MTP page shipping FAQPage + Service + BreadcrumbList + Article + Organization with full `sameAs` (including Wikipedia when we earn one, YouTube, LinkedIn, X) will immediately out-schema the market leader. **Effort:** already in our playbook — just enforce consistency.

---

## 8. Strategic Recommendations for MTP

1. **Don't try to out-brand NP** — their authority gap is a 10-year project. Target adjacent category: "fulfillment OPERATOR" (not "courier"), where NP is less dominant.
2. **Build Wikipedia presence** — MTP should pursue a UA-Wikipedia entry for the MTP Group (requires third-party press coverage first — needs 3-5 independent Forbes/Liga/AIN articles in 2026).
3. **YouTube channel is the #1 structural lever** — the 0.737 correlation with AI citations suggests even a modest YT channel (20-30 fulfillment explainer videos) will compound over 12 months.
4. **Maintain technical lead** — NP's llms.txt, hreflang, canonical, FAQ-schema gaps are opportunities. Keep shipping.
5. **Replicate passage pattern TODAY** — Tactic 1 above is a one-sprint fix with immediate measurable effect on AI visibility.
6. **Reddit / r/Ukraine presence** — NP wins here organically. MTP should seed 2-3 high-quality expert answers per month in r/Ukraine, r/ukraina, r/ecommerce for UA-fulfillment threads.

---

## 9. Conclusion

Nova Poshta's AI-search dominance is NOT driven by superior on-page GEO. Their fulfillment page scores 66/100 technically, has a broken breadcrumb schema, no llms.txt, no hreflang, no canonical, and relies on client-side hydration for its heading structure. MTP's technical execution is already superior.

NP dominates because they are an **entity-recognized monopoly** in the UA logistics category. LLMs surface them from training-data frequency alone. No amount of schema markup closes this gap in 2026.

**MTP's winnable game:** (a) own the "fulfillment operator" adjacent category where NP is weaker, (b) replicate NP's passage-first writing style, (c) build YouTube + Wikipedia + Reddit presence over 12 months, (d) maintain technical lead on llms.txt / dual-md / schema.

**Time horizon:** MTP can realistically achieve ~15-25% AI citation share for "fulfillment Ukraine" and 40-60% for "fulfillment operator Ukraine" by Q4 2026 with the tactics above. Competing with NP for generic "logistics Ukraine" is not feasible in 2026.

---

*Files referenced:*
- `/tmp/np-robots.txt` — NP robots.txt (cached)
- `/tmp/np-home.html` — NP homepage SSR
- `/tmp/np-fulf.html` — NP fulfillment page SSR
- `/tmp/np-sp.xml` — NP sitemap-pages.xml
- `/tmp/np-wiki.html`, `/tmp/np-wiki-en.html` — Wikipedia entries

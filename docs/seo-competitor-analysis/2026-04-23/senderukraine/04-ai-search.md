# AI Search / GEO Readiness Audit — senderukraine.com

**Auditor:** GEO Specialist (Claude)
**Date:** 2026-04-23
**Target:** https://senderukraine.com
**Context:** Ukrainian 3PL fulfillment — direct MTP competitor
**Purpose:** Determine AI-citation readiness for queries like "кращий фулфілмент Україна", "fulfillment operator Kyiv", etc.

---

## GEO Readiness Score: **38 / 100** (Below average)

| Dimension                 | Weight | Score | Weighted |
|---------------------------|--------|-------|----------|
| Citability                | 25%    | 45    | 11.25    |
| Structural Readability    | 20%    | 55    | 11.00    |
| Multi-Modal Content       | 15%    | 30    | 4.50     |
| Authority & Brand Signals | 20%    | 25    | 5.00     |
| Technical Accessibility   | 20%    | 30    | 6.00     |
| **Total**                 | 100%   |       | **37.75** |

**Platform-specific estimates**
| Platform            | Est. citation share | Reason |
|---------------------|---------------------|--------|
| Google AI Overviews | Low-Medium          | Strong FAQPage microdata, hreflang present, 3 langs |
| ChatGPT Search      | Very Low            | GPTBot + OAI-SearchBot both **403 at server level** |
| Perplexity          | Low-Medium          | PerplexityBot passes (200), but no llms.txt + weak brand signals |
| Bing Copilot        | Low                 | No dedicated Bingbot handling, but not blocked |
| Gemini / AIO        | Low                 | Google-Extended passes (200), but thin content |

---

## 1. llms.txt / llms-full.txt

- `https://senderukraine.com/llms.txt` → **404 (not present)**
- `https://senderukraine.com/llms-full.txt` → **404 (not present)**
- Note: the site does echo `?_url=/llms.txt` inside the language selector dropdown, meaning the request is rewritten to a locale (`/ru/llms.txt?_url=/llms.txt`) — still returns the generic 404 template. There is literally no file.

**Status:** MISSING. No AI-specific content map. Advantage: MTP already has one; gap widens.

---

## 2. robots.txt

```
User-agent: *
Disallow: /login
Disallow: /register
Disallow: /call-center
Disallow: /partnership
Disallow: /courier-shipping
Sitemap: https://senderukraine.com/sitemap.xml
```

- No AI-specific directives (no explicit Allow/Disallow for GPTBot, ClaudeBot, PerplexityBot, CCBot, Google-Extended, anthropic-ai, OAI-SearchBot).
- Default = allowed for all.
- **Critical finding:** server-level WAF/nginx blocks OpenAI crawlers independently of robots.txt.

**Live AI crawler probe (curl with UA header):**

| Crawler          | HTTP status | Interpretation |
|------------------|-------------|----------------|
| GPTBot           | **403**     | Hard block (server/WAF) — ChatGPT will rarely cite |
| OAI-SearchBot    | **403**     | Hard block — ChatGPT Search excluded |
| ClaudeBot        | 200         | Allowed |
| anthropic-ai     | 200         | Allowed |
| PerplexityBot    | 200         | Allowed |
| Google-Extended  | 200         | Allowed (Gemini/AIO OK) |
| CCBot            | 200         | Allowed (training corpus) |

**Implication:** Sender Ukraine is effectively invisible to ChatGPT Search. This is a big opportunity window for MTP if we keep our `robots.txt` GPTBot-allow posture (which we do).

---

## 3. Structured Data Quality

Reviewed:
- `/` (home)
- `/faq`
- `/prices`
- `/how-it-works`
- `/blog/shcho-take-fulfilment-perevahy-nedoliky-komu-pidiide` (blog post)

**Findings:**

| Page          | Schema type | Format | Quality |
|---------------|-------------|--------|---------|
| Home          | None visible in HTML | — | Missing Organization, Service, LocalBusiness |
| FAQ           | `FAQPage` (Question/Answer) | Microdata (`itemscope/itemprop`) | Valid, covers ~8 Q&A |
| Prices        | None visible | — | No `Product`/`Offer`/`PriceSpecification` |
| How-it-works  | None visible | — | No `Service` or `HowTo` |
| Blog post     | None visible | — | No `Article` / `BlogPosting` / author schema |

- **No JSON-LD anywhere** — they use legacy microdata.
- **No `Organization` schema** with `sameAs`, `logo`, `aggregateRating`, `address`, `telephone`.
- **No `AggregateRating`** found on any page — this is a huge GEO miss because AI engines weight rating presence.
- **No `BreadcrumbList`.**
- **No `Service` schema** despite the whole site being services.

**Implication:** MTP can out-schema them trivially. JSON-LD + `Organization` with `aggregateRating` + `Service` blocks on hub pages + `FAQPage` would dominate.

---

## 4. Passage-Level Citability

**Sample passage (home, "Описание-блок"):**
> "Фулфилмент - это комплексное решение для вашего интернет-магазина. Мы предоставляем услуги приёма, хранения, отправки товара по Украине вашим клиентам."
> Length: 34 words.

**Sample FAQ answer:**
> "Для начала работы достаточно просто зарегистрироваться на сайте. Вам предоставится доступ в личный кабинет..."
> Length: ~45 words.

**Blog post length:** `shcho-take-fulfilment-...` → **~1,206 words** (HTML body) — acceptable but thin.

**Citability signals:**
- Direct answers in first 40–60 words: partially — FAQ yes, home page no (too much prose).
- Question-based H2/H3 headings: YES on FAQ and blog.
- Specific statistics with attribution: **NONE found** (no "X% of merchants", no cited studies, no year-over-year numbers).
- Self-contained passages 134–167 words (optimal citation length): rare — most paragraphs are 30–80 words.
- Table data: NONE (prices page uses interactive slider calculator — not a static pricing table, so AI can't cite rates).
- Defined terms / glossary: absent.
- Author bios / entity markup for experts: absent.

**Score:** citability is mediocre. Short paragraphs + FAQ schema = some extractability, but lack of statistics and tables blocks them from being the go-to source for factual citations.

---

## 5. Structural Readability

- Only one H1 per page. Good.
- Hreflang: `ru-UA`, `uk-UA`, `en` declared on every page. No `x-default` (minor miss).
- Canonical: present.
- Language versions: UA (`/uk/`), RU (root), EN (`/en/`) — RU is treated as primary.
- Sitemap: **only 6 URLs** (`/`, `/how-it-works`, `/prices`, `/faq`, `/contacts`, `/blog`) — blog posts are NOT in sitemap. Critical indexability miss for AI crawlers that follow sitemap.
- `lastmod` on all sitemap entries is `2024-02-08` — stale by ~2 years, AI engines de-prioritize stale content.
- Navigation blocks are clear; tabs (`/how-it-works` "Заказы/Товарные остатки/...") are not progressively enhanced for crawlers — tab panels are in DOM but without clear semantic grouping.

---

## 6. Multi-Modal Content

- Video on home (Wistia `4hyr5uyduh`) — embedded but no `VideoObject` schema.
- Screenshots of CRM — good visuals, no `ImageObject` alt-text for AI semantic pickup.
- No YouTube channel linked from home page HTML (Facebook present: `facebook.com/sender.fulfillment/`).
- Mobile apps on App Store (`id6744337675`) + Google Play — no `MobileApplication` schema.
- No podcast, no webinar, no case-study PDFs.

---

## 7. Authority & Brand Signals

| Signal                  | Status | Note |
|-------------------------|--------|------|
| Wikipedia entity        | **Missing** | 404 on `/wiki/Sender_Ukraine` |
| Ukrainian tech media    | Not verified (WAF on SERP) | No direct hits on AIN/MC.today/Epravda via manual probes |
| Named authors on blog   | YES | "Андрій Слюсар" appears — but no author schema / bio page |
| Google Analytics id     | `UA-118367275-1` (legacy Universal Analytics, deprecated July 2023) |
| GTM id                  | `GTM-KXQLNPR` present |
| Backlink pool (inferred)| Likely weak — no DA signals suggested by corpus |
| Facebook                | Active (`sender.fulfillment/`) |
| YouTube                 | Not linked from site |
| LinkedIn                | Not linked from site |
| Reddit mentions         | Not detectable via public probe |
| G2 / Capterra / Trustpilot | No review aggregator schema linked |
| `sameAs` property       | Absent (no `Organization.sameAs`) |

**Interpretation:** Sender Ukraine has real traction inside Ukraine's ecom community but essentially zero structured authority signals that AI engines can pick up. Their brand is invisible to RAG models.

---

## 8. Technical Accessibility (SSR vs CSR)

- Laravel-rendered HTML (server-side). Content is in initial HTML. Good for AI crawlers.
- `app.css` + jQuery + FontAwesome loaded synchronously. Heavy but not blocking.
- Home HTML size: ~41 KB minified-ish. Readable for crawlers.
- No `<noscript>` fallbacks for JS-only components — not critical since content is SSR.
- Cookies set on homepage (`XSRF-TOKEN`, `laravel_session`) — this can annoy some crawlers but not block them.
- TLS + HSTS (`strict-transport-security: max-age=31536000; includeSubDomains; preload`). Clean.
- No `X-Robots-Tag` issues. No anti-bot challenge page for well-behaved UAs (except OpenAI family).

**Big miss:** they don't ship an auto-generated clean markdown version of each page (our `dual-md.mjs` advantage).

---

## Competitive Delta vs MTP (fulfillmentmtp.com.ua)

| Lever                          | Sender Ukraine | MTP       | Winner |
|--------------------------------|----------------|-----------|--------|
| llms.txt                       | 404            | Present   | MTP    |
| GPTBot access                  | 403            | 200       | MTP    |
| JSON-LD Organization           | No             | Yes       | MTP    |
| AggregateRating schema         | No             | ?         | Tied/MTP |
| FAQPage schema                 | Microdata      | JSON-LD   | MTP (modern format) |
| Blog post schema               | None           | Present   | MTP    |
| Dual-md (`.md` twin)           | No             | Yes       | MTP (unique moat) |
| Sitemap coverage               | 6 URLs, stale  | 100+ URLs, fresh | MTP |
| Hreflang completeness          | 3 (no x-default) | 4       | MTP    |
| Named authors                  | Yes (good)     | Varies    | Sender |
| Case studies / testimonials    | Present on site | Varies   | Sender |
| Mobile app (trust signal)      | Yes (iOS + Android) | No  | Sender |
| Facebook activity              | Active         | ?         | Sender |

**Net:** MTP wins on technical GEO. Sender wins on product depth signals (app, case studies, named authors).

---

## Top 5 Highest-Impact GEO Wins for MTP (from this audit)

1. **Publish `/llms.txt` + `/llms-full.txt` (effort: 0.5 day)** — Sender has none. Ship a curated map of our service pages, pricing, FAQ, and 10 flagship blog posts. Put it live before Sender does. Already planned per our `public/llms.txt`.
2. **Wrap `Organization` + `AggregateRating` JSON-LD on home + all service hubs (effort: 1 day)** — Sender has zero `AggregateRating`. Even self-declared ratings from our CRM (e.g. "4.8 based on 342 reviews") move the needle on AIO/Gemini. Link via `sameAs` to Google Business Profile, Facebook, LinkedIn, YouTube.
3. **Publish 3 data-driven statistics articles per quarter (effort: ongoing)** — Sender has no statistics. AI engines cite the site that says "37% of Ukrainian ecom stores lose 12% revenue on returns (MTP Group, 2026)". Own the numbers for: Ukrainian fulfillment market size, average return rate by category, cost-per-order breakdown, Nova Poshta vs Ukrposhta delivery times.
4. **Add static pricing tables (effort: 0.5 day)** — Sender uses a JS calculator that crawlers can't index. A static `<table>` on `/tsiny/` with example cost per SKU/month is instantly quotable. This alone can win "скільки коштує фулфілмент в Україні" queries.
5. **Named author bios with `Person` + `sameAs` schema (effort: 1 day)** — Sender has named authors but no structured entity. We should go one step further: author page per writer, linked to LinkedIn/Twitter via `sameAs`, plus `Article.author` JSON-LD on every post. This improves E-E-A-T and entity graph binding.

---

## What Sender Does Well (Steal These)

- **FAQPage microdata site-wide** — every FAQ is wrapped (8+ Q&A on `/faq`). We should ensure `FAQPage` is on every service page, not just the `/faq` hub.
- **Named authors on blog** — creates the illusion of expertise even without bios. Low effort, high AI-trust signal.
- **Mobile app as trust anchor** — "we have an iOS + Android app" signals maturity. Link it in `Organization.sameAs` + `MobileApplication` schema.
- **Clean Laravel SSR** — content is in initial HTML. No hydration delays. We already do this with Astro + SSG.
- **Integrations logo wall with `title` + `alt`** — 15+ integrations listed with labelled logos (Nova Poshta, Ukrposhta, Rozetka, Prom, Shopify, Horoshop, SalesDrive, KeyCRM, Sitnix, Checkbox, Turbo SMS, KeepinCRM, LP CRM, SMS-fly, Мій Дроп). AI engines scrape these as entity co-occurrences, strengthening the "Sender + <integration>" semantic link. **We should list ours the same way, with `itemprop` or JSON-LD `offers`/`subjectOf`.**

---

## Verdict

Sender Ukraine is **not meaningfully AI-cited today**. They have server-blocked the two most important ChatGPT-era crawlers (GPTBot, OAI-SearchBot), ship zero JSON-LD, have no `llms.txt`, no `AggregateRating`, no Wikipedia entity, and a stale 6-URL sitemap. They are discoverable only through Google AIO (Google-Extended passes) and Perplexity — and even there their lack of statistics and pricing tables makes them non-authoritative.

**MTP can lap them on GEO within 2 weeks of focused work.** The two fastest wins are (a) ship pricing tables and (b) ship Organization + AggregateRating JSON-LD. Everything else compounds from there.


# senderukraine.com — Content Audit (Sept 2025 QRG)

Date: 2026-04-23
Auditor: Content Quality specialist
Scope: Site architecture, word counts, E-E-A-T, topic clusters, language versions, thin content, AI citation readiness

---

## 1. Site Architecture

**Sitemap size:** 6 URLs total (sitemap.xml last updated 2024-02-08 — 2+ years stale).

| URL | Purpose | Priority |
|-----|---------|----------|
| `/` | Homepage | 1.0 |
| `/how-it-works` | Service/process | 0.5 |
| `/prices` | Pricing | 0.5 |
| `/faq` | FAQ | 0.4 |
| `/contacts` | Contact | 0.5 |
| `/blog` | Blog hub | 0.3 |

**Blog inventory:** 5 articles only, all Ukrainian slugs, all CRM/e-commerce tool roundups.
- `shcho-take-fulfilment-perevahy-nedoliky-komu-pidiide` (what is fulfillment)
- `top-5-krashchykh-servisiv-dlia-stvorennia-internet-mahazynu` (top e-shop builders)
- `CRM-systema-dlia-internet-mahazynu-kontrol...` (CRM for e-shops)
- `poiednannia-fulfilmentu-sender-z-sitniks-crm...` (Sitniks integration case)
- `avtomatyzatsiia-internet-mahazynu-top-3-ukrainski-crm-systemy` (top UA CRMs)

**Assessment:** This is a brochure-ware site, not a content hub. No service pages per vertical (cosmetics/fashion/food), no marketplace pages (Prom/Rozetka/Horoshop dedicated), no location pages, no calculator. Zero pillar content. Total indexable URLs ≈ 11 (6 sitemap + 5 blog posts).

vs MTP: MTP targets 120+ pages (per `MTP_SEMANTIC_CORE_FULL.md`). Sender is ~10x smaller.

---

## 2. Word Counts (key pages)

| Page | Words | Min per QRG | Verdict |
|------|-------|-------------|---------|
| Homepage (RU) | 1,051 | 500 | Passes floor, below comprehensive |
| Homepage (UK) | 1,040 | 500 | Passes floor |
| Homepage (EN) | 1,165 | 500 | Passes floor |
| `/how-it-works` (service) | 478 | 800 | **FAILS — 40% short** |
| `/prices` | 490 | 500-600 | **FAILS by ~10-20%** |
| `/faq` | 457 | 800 | **FAILS — 43% short** |
| `/contacts` | 130 | 500 | **Severely thin** |
| `/blog` (hub) | 348 | — | Listing only |
| Blog article (fulfillment guide) | 605 | 1,500 | **FAILS — 60% short** |

**Thin-content flag:** 5 of 6 primary pages are below topical-coverage floors. The 605-word cornerstone blog post ("What is fulfillment?") is less than half the 1,500-word blog minimum and has no TOC, no schema, no internal links to service pages beyond the homepage.

---

## 3. E-E-A-T Assessment

### Experience — 8/20
- Site claims "5+ years" in the meta description — vague, no founded-year, no shipment volume, no SKU count.
- Author byline on the one blog post: "Андрій Слюсар, 13.12.2022" — single author, no bio, no credentials, same author for all 5 posts.
- No case studies page. No named client stories. Has a photo gallery (`gallery/1-8.jpg`) with "Sender Fulfillment Team" alt text — photos yes, narrative no.
- Has a "Reviews" block on homepage but reviews are inline testimonials, not aggregated with schema/ratings.

### Expertise — 10/25
- Process page ("how-it-works") is a 3-step skeleton (478 words) — no depth on WMS, SLA, barcoding, returns, quality control, hazmat, temperature control, marketplace FBO specifics.
- No technical documentation beyond a help center subdomain (`senderfulfillment.crunch.help`) — opaque content.
- No vertical-specific expertise (cosmetics, apparel, supplements, electronics all absent).

### Authoritativeness — 7/25
- 20+ integration logos on homepage (Prom, Rozetka, Horoshop, Shopify, Nova Poshta, Ukrposhta, Checkbox, 6 CRMs, Telegram, SMS-fly) — strong ecosystem signal.
- No press mentions, no awards badges, no industry associations shown.
- Native mobile app (iOS + Android links present) — differentiator vs MTP.
- Backlink posture unknown (outside this audit scope).

### Trustworthiness — 14/30
- Phone visible in header (+380 63 595-32-32), email (info@senderukraine.com), physical contacts page exists.
- Privacy.pdf and Contract.pdf (UA + RU versions) linked in footer — good trust signal.
- HTTPS + HSTS preload enabled.
- No SSL business address, no legal entity name shown on homepage, no ЄДРПОУ/EDRPOU.
- No certifications (ISO, GDP, GMP) displayed.

**E-E-A-T total: 39/100** (weighted). Much weaker than a B2B fulfillment leader should be.

---

## 4. Topic Clusters / Verticals

**Verticals covered:** NONE.

Sender targets a single ICP implicitly: generic Ukrainian e-commerce store owners using Prom/Rozetka/Horoshop/Shopify with a CRM. Zero pages for:
- Cosmetics & beauty
- Apparel & footwear
- Food, supplements, BAD
- Electronics, gadgets
- Marketplace-specific (Rozetka FBR/FBS, Prom Market, Kasta, Allo, Epicentr, Amazon, eBay)
- Cross-border / Ukraine→EU / Ukraine→US
- B2B wholesale fulfillment
- Subscription boxes
- DTC brands

**Distribution partners shown:** Nova Poshta, Ukrposhta, Mist Express, Rozetka pickup, in-house courier Kyiv.

**Positioning axis:** "Fulfillment + 20 integrations + mobile app + transparent flat pricing". The comparison table on homepage explicitly positions them as *"different from other fulfillment companies"* on 8 features (all-carrier shipping, no-days-off, transparent tariffs, mobile app, CRM-replacement client portal, 20+ integrations, personal support, add-ons).

---

## 5. Unique Angles vs MTP

| Axis | Sender | MTP | Advantage |
|------|--------|-----|-----------|
| Native mobile app | iOS + Android published | Not shown | **Sender** |
| Integrations count | "20+" displayed on logo wall | Claims integrations, fewer logos shown | **Sender** |
| Client portal as "CRM replacement" | Headline feature | Not pitched this way | **Sender** |
| Vertical landing pages | 0 | 10+ planned | **MTP** |
| Blog depth | 5 thin posts, last major activity 2022-2024 | 20+ EN posts alone visible in current repo | **MTP** |
| Language versions | 3 (uk/ru/en) full | 3 (uk/ru/en) full | Tie |
| Word count average | ~500 on service pages | 1,200+ per URL policy | **MTP** |
| Schema.org | FAQPage detected on home | Article, Service, Breadcrumb, FAQ | **MTP** |
| Location pages | 0 | Planned (Kyiv, Dnipro, regional) | **MTP** |
| Calculator tool | 0 | `/calculator/` live in 3 langs | **MTP** |

---

## 6. Language Versions

Full trilingual stack, all hosted under single domain with path prefixes:
- `/uk` — Ukrainian
- `/` and `/ru` — Russian (default, `lang="ru"` on homepage — **SEO red flag** for Ukraine market post-2022)
- `/en` — English

Hreflang tags NOT detected in homepage head (`grep hreflang` returned empty on the rendered HTML). This is a **major SEO miss** — three language versions exist but without hreflang, Google may treat them as duplicates or pick the Russian as canonical internationally.

`/ua` returns 102-word stub (likely 404 or empty shell) — legacy URL not properly 301'd to `/uk`.

---

## 7. Thin Content Detection (Sept 2025 QRG flags)

**Pages flagged thin:**
1. `/contacts` — 130 words, basically just phone + email.
2. `/how-it-works` — 478 words, 3 steps, no depth.
3. `/faq` — 457 words total for entire FAQ (suggests <10 Q&A pairs).
4. `/blog` — 348 words, listing only.
5. Cornerstone blog "What is fulfillment?" — 605 words vs 1,500 floor.

**AI-content markers:** Not detected. Writing is human, Ukrainian/Russian idiomatic, no GPT-isms. But that also means content is SHORT-form, not AI-inflated.

**Sitemap freshness:** All 6 URLs stamped `lastmod: 2024-02-08`. Either CMS bug or the site hasn't been meaningfully updated in 14+ months. Google reads this as a stagnant site.

**AI citation readiness: 22/100.** No TOCs, no jump links, no structured data beyond FAQPage on home, no extractable stats (only "5+ years" and "20+ integrations" as quotable facts), no author entity markup, no last-updated visible timestamps.

---

## 8. Scoring Summary

| Metric | Score |
|--------|-------|
| Overall content quality | **34/100** |
| E-E-A-T | **39/100** |
| AI citation readiness | **22/100** |
| Word-count compliance | 2/9 pages pass |
| Topic cluster coverage | 0/10 verticals |
| Freshness signal | FAIL (stale sitemap, 2022 blog) |

---

## 9. Recommendations for MTP (where to attack)

1. **Vertical landing pages** — Sender has zero. MTP should own "fulfillment for cosmetics / apparel / supplements / electronics / marketplaces" before Sender notices.
2. **Long-form cornerstone content** — Sender's "What is fulfillment?" is 605 words. MTP's equivalent should be 3,000+ words with schema, TOC, author bio, last-updated stamp. Outrank on the definitional query.
3. **Location pages** — Sender has one contacts page, 130 words. MTP can publish Kyiv/Dnipro/Lviv/Odesa hub pages with warehouse specs and own local SERPs.
4. **Marketplace-specific guides** — Rozetka FBR, Prom Market, Kasta, Epicentr — Sender has zero. Publish 1,500-word operator guides per marketplace.
5. **Case studies with named clients + before/after metrics** — Sender shows team photos but no client stories. MTP should publish 5-10 named case studies with volume, SLA, cost-per-order deltas.
6. **Calculator SEO** — already live on MTP, Sender has none. Double down on `/calculator/` with expanded content around it.
7. **Author E-E-A-T** — Sender has one anonymous-ish author. MTP should publish ops-lead and warehouse-manager author pages with LinkedIn, years-in-role, bylines, and `Person` schema.
8. **Fix hreflang gap disclosure in comparison content** — if MTP publishes a "Sender vs MTP" comparison page, Sender's missing hreflang, stale 2024 sitemap, and 605-word cornerstone are legitimate content-depth talking points.

---

## 10. Raw Artifacts

Saved to `/tmp/`:
- `sender-home.html`, `sender-how-it-works.html`, `sender-prices.html`, `sender-faq.html`, `sender-blog.html`, `sender-contacts.html`, `sender-ru.html`, `sender-uk.html`, `sender-en.html`, `sender-blog-article.html`, `sender-sitemap.xml`

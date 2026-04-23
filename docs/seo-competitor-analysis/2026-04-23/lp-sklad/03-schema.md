# LP-Sklad — Schema.org Structured Data Audit

**Date:** 2026-04-23
**Auditor:** MTP schema specialist
**Hypothesis under test:** LP-Sklad's heavy citation in ChatGPT/Perplexity/Gemini for Ukrainian fulfillment queries is partly driven by richer/superior schema markup.

---

## 0. Critical domain clarification

The brief asked to audit `https://lp-sklad.online`. That host is **not** the marketing site — it is the authenticated SaaS portal (Yii-framework login for their warehouse management product). Every unknown path (`/about`, `/services`, `/faq`, etc.) resolves to the same 7.6 KB authorization page titled "Авторизация". **The `.online` host has zero structured data markup on any crawlable page.**

The real public marketing property is **`https://lp-sklad.biz`** (linked from the .online footer). All schema findings below come from `.biz`. `lp-sklad.biz` runs three distinct stacks:

| Section | Stack | URL shape |
| --- | --- | --- |
| Marketing home | Static HTML (hand-coded) | `/`, `/ru`, `/en` |
| Landing funnels | Static HTML (generated) | `/fulfillment/{uk\|ru\|en\|pl}/<slug>/`, `/rating-fulfillment/{locale}/<slug>/` |
| Blog | WordPress + Yoast SEO | `/blog/<slug>/` |

Also of note: their robots.txt is aggressively **AI-hostile** — it blocks `ClaudeBot`, `GPTBot`, `Google-Extended`, `Amazonbot`, `Applebot-Extended`, `Bytespider`, `CCBot`, and `meta-externalagent` at `Disallow: /`. **If lp-sklad is getting cited by ChatGPT/Perplexity/Gemini despite this, it is NOT happening through fresh crawls — it is historical training data or third-party citations. Schema is therefore unlikely to be the causal driver of their AI visibility.** The richness-hypothesis is weakened before we even look at the markup.

---

## 1. Schema inventory (every @type found across 4 sampled pages)

Sampled pages:
1. `lp-sklad.biz/` (marketing home, UK)
2. `lp-sklad.biz/fulfillment/uk/fulfilment-platforma/` (landing funnel)
3. `lp-sklad.biz/rating-fulfillment/uk/rating-autsorsynh-skladu/` (ratings/ToP-style page)
4. `lp-sklad.biz/blog/fulfilment-sklada-osnovni-proczesy-ta-vyklyky/` (WP blog post)

### Types observed

| @type | Where | Quality |
| --- | --- | --- |
| Organization | Home, landing, rating, blog | Thin on home (6 props + `sameAs` IG/Telegram); on landings `sameAs` self-references — broken |
| FAQPage | Home + every landing + every rating page | Present but small (4-5 Q&A), no `speakable`, no `dateModified` |
| Article | Every WP blog post | Yoast-generated, has `author`, `publisher`, `wordCount`, `articleSection`, `inLanguage`, `thumbnailUrl` |
| WebPage | Every WP blog post | Has `breadcrumb`, `primaryImageOfPage`, `potentialAction: ReadAction` |
| WebSite | Every WP blog post | Has `SearchAction` (sitelinks searchbox) |
| BreadcrumbList | Every WP blog post | 2-level (home → post). Absent on hand-coded landings |
| ImageObject | Blog posts | `contentUrl`, `width`, `height`, `caption` |
| Person | Blog posts | `author` entity: `name: vikor_romanov`, Gravatar URL, no `jobTitle`, no real `sameAs` |
| SearchAction | Blog `WebSite` node | Standard `?s={search_term_string}` |
| ReadAction | Blog `WebPage` node | Yoast default, little value |

### Types NOT found anywhere on lp-sklad.biz

- **Service** — critical miss for a service business
- **Offer / AggregateOffer** — no priced offers despite having "Тарифи" section
- **priceRange** — absent from Organization
- **LocalBusiness / Warehouse** — absent despite having a physical warehouse in Kryvyi Rih
- **AggregateRating** — absent despite the rating/top-18 pages
- **Review** — absent
- **Product** — absent
- **HowTo** (good — it is deprecated)
- **DefinedTerm / DefinedTermSet** — absent (no glossary markup)
- **VideoObject** — absent despite embedded YouTube reviews
- **ItemList** — absent on the "Top 18 fulfillment operators" rating page (they rank 18 providers with no `ItemList` schema — major miss)
- **JobPosting, Event, Course** — N/A

---

## 2. Per-page validation

### 2.1 `lp-sklad.biz/` (marketing home)

Two separate `<script type="application/ld+json">` blocks (not @graph-wrapped):

**Organization** — passes required fields:
- `@context` = `https://schema.org` OK
- `name` = "LP-Sklad" OK
- `url` = "http://lp-sklad.biz/" WARN — uses `http://`, not HTTPS
- `logo` = "http://lp-sklad.biz/img/logo.png" WARN — HTTP
- `description` OK
- `telephone` = "+380686686864" OK (E.164)
- `address` (PostalAddress): country UA, city Kryvyi Rih, region Dnipropetrovsk OK
- `contactPoint`: one entry, `customer support`, `areaServed: UA` OK
- `sameAs`: IG + Telegram only. **No LinkedIn, no Facebook, no YouTube, no Wikidata, no Ukrainian Companies Register, no Crunchbase.** This is weak — `sameAs` is one of the strongest entity-resolution signals for AI.

Missing recommended Organization props:
- `foundingDate`
- `numberOfEmployees`
- `legalName` (registered FOP/TOV name)
- `taxID` (ЄДРПОУ)
- `areaServed` at Organization level
- `brand`
- `award`
- `aggregateRating`

**FAQPage** — passes, but only 5 Q&A on home. All `Question`/`Answer` pairs valid. In UK language. No `inLanguage` property on the FAQPage itself (should be "uk"). No `dateModified`.

**Note on FAQPage Google policy**: LP-Sklad is a commercial SaaS, not government/healthcare — so per Google's August 2023 restriction they do not get rich results. They still benefit from AI consumption (ChatGPT/Perplexity do ingest `FAQPage` structured Q&A when the page is crawled). MTP has the same opportunity.

### 2.2 Landing funnels (`/fulfillment/uk/fulfilment-platforma/`)

Uses `@graph`-wrapped two-node graph:

```
@graph = [ Organization, FAQPage ]
```

Issues:
- Organization `name` mutates per page: "Готовий фулфілмент", "Фулфілмент e-комерції" — **different `name` on every landing**. This is schema abuse/spam — entity identity should be stable.
- `logo` is a relative path `./images/favicon.png` — invalid (schema requires absolute URL; Google will drop it)
- `sameAs: ["https://lp-sklad.biz/"]` — self-referencing, not a valid sameAs target
- FAQPage `inLanguage` present (good), `url` present
- No BreadcrumbList on these landings

### 2.3 Rating page (`/rating-fulfillment/uk/rating-autsorsynh-skladu/`)

Same two-node `@graph` (Organization + FAQPage) as landing funnels. Same issues (mutated Org name, relative logo, self-sameAs).

**Biggest miss**: this is a "Top 18 fulfillment operators" comparison page listing 18 ranked businesses. It should emit:
- `ItemList` with 18 `ListItem` entries
- Each `ListItem.item` as `Organization` (competitor name, URL, logo)
- Optional `Rating`/`AggregateRating` per item

Without this, the rich ranking content is invisible to structured-data consumers. MTP can win easily on ratings/comparison pages by doing this properly.

### 2.4 WordPress blog post

Yoast-generated `@graph` is the strongest schema on the site. Nodes: `Article`, `WebPage`, `ImageObject` (primaryImage), `BreadcrumbList`, `WebSite`, `Organization` (blog-scoped), `Person` (author).

Strengths:
- Proper @graph with cross-references (`@id` + `isPartOf`, `publisher`, `author` referenced by ID)
- `wordCount: 370` — helpful signal
- `articleSection: ["Фулфілмент"]` — topical classification
- `inLanguage: uk`
- `WebSite` has `SearchAction`
- BreadcrumbList present

Weaknesses:
- `author` is `vikor_romanov` (WP username, not human display name); no `jobTitle`, no bio, no real `sameAs` (just points back to the blog listing page)
- `Article` lacks `about` / `mentions` (topic entities)
- No `speakable` specification
- Blog `Organization` (separate from marketing-home Organization) has different @id `https://lp-sklad.biz/blog/#organization` — **two distinct Organization entities on same domain** (entity fragmentation; AI models may not connect them)
- Word count is only 370 — the schema is richer than the actual content
- No `citation` / no `author.knowsAbout` / no E-E-A-T signals

---

## 3. Organization deep-dive (vs the brief's focus areas)

| Question | Answer |
| --- | --- |
| `sameAs` → authority profiles? | Only IG + Telegram on home; self-reference on landings; IG only on blog. **Zero Wikipedia, Wikidata, LinkedIn, YouTube channel, Facebook, Crunchbase, government registries.** Weak entity graph. |
| `aggregateRating`? | Absent everywhere. |
| `award`? | Absent. |
| `foundingDate`? | Absent. |
| `numberOfEmployees`? | Absent. |
| `legalName` / `taxID`? | Absent. |

**Verdict: LP-Sklad's Organization schema is WEAKER than MTP's current implementation.** MTP already has `sameAs` pointing to Telegram and LinkedIn from Base.astro. If we add founder `Person` `sameAs` → Wikidata once we create an entry, add `foundingDate`, `numberOfEmployees`, and a genuine `aggregateRating` (driven by real testimonial inventory), we meaningfully leapfrog them.

---

## 4. Service schema (brief focus)

LP-Sklad emits **zero `Service` schema**. No `offers`, `priceRange`, `areaServed`, or `audience` anywhere on the site — despite having a `Тарифи` section with explicit pricing tiers and explicit target audience ("e-commerce in Ukraine"). **This is an enormous schema gap they could close but haven't.**

MTP should absolutely ship `Service` markup on every service page (`/fulfillment-dlya-*`), with nested `Offer`, `priceRange`, `areaServed: UA`, `audience: BusinessAudience`, `provider: Organization ref`, `serviceType`.

---

## 5. FAQPage usage

- Present on marketing home (UK version), on every `/fulfillment/{locale}/<slug>/` landing, and every `/rating-fulfillment/{locale}/<slug>/` rating page.
- 4–5 Q&A per page, short answers (1–2 sentences), no images or links in answers.
- No `speakable`, no `dateModified`, no `mainEntityOfPage`.
- Locale-specific FAQPage (inLanguage set) on landings.

**Google policy reminder**: FAQPage rich results restricted to government/healthcare since Aug 2023 — LP-Sklad is commercial, so they get no SERP rich result. They still benefit from AI models consuming the Q&A as clean structured pairs. MTP's existing FAQPage on `/ua/faq/` falls in the same bucket (info-priority, not critical; preserve for AI citation value).

---

## 6. DefinedTermSet (glossary markup — brief focus)

**LP-Sklad does not use DefinedTerm or DefinedTermSet anywhere.** If they do dominate AI citations for definitional queries ("що таке фулфілмент", "what is 3PL"), it is not thanks to glossary schema. This is a clear green-field opportunity for MTP: publish a glossary page (`/slovnyk-fulfillment/`) with `DefinedTermSet` containing 30–50 `DefinedTerm` entries (name, description, termCode, inDefinedTermSet, url). This markup is cited strongly by Perplexity for knowledge-panel style answers.

---

## 7. Article + author schema on blog posts

Yoast handles this with an @graph as shown above. It is competent but generic. Our MTP Base.astro auto-inserts `Article` with a better-quality `author` Person node (real display name, `jobTitle: Засновник MTP Group Fulfillment`, `sameAs: Telegram + LinkedIn`). **MTP's article schema is already stronger than LP-Sklad's.**

---

## 8. Uncommon / "AI-bait" types

| Type | LP-Sklad | Notes |
| --- | --- | --- |
| HowTo | No | Good — it was deprecated Sep 2023. Don't add to MTP. |
| BreadcrumbList | On blog only (Yoast). Missing on landings and rating page. | MTP should ensure BreadcrumbList on every URL (already on Base.astro — verify coverage). |
| LocalBusiness / Warehouse | No | Opportunity: MTP can add `Warehouse` (schema.org/Warehouse) with `openingHoursSpecification`, `geo`, `hasMap`, `photo` for our Kryvyi Rih + Kyiv locations. |
| WebSite + SearchAction | Blog only (Yoast default). Marketing home lacks it. | MTP should add this to Base.astro (sitelinks searchbox signal). |
| VideoObject | No (they embed YouTube testimonials without schema) | Easy win for MTP on any page with hero/testimonial video. |
| ItemList | No (even on their Top-18 ranking page!) | Huge opportunity for MTP's own comparison content. |
| DefinedTermSet | No | See section 6 — green-field. |
| BroadcastEvent / Clip | No | N/A unless MTP does live events. |

---

## 9. Overall schema quality scorecard

Scale: 0 (missing) → 5 (best in class)

| Dimension | LP-Sklad | MTP (current) | Gap |
| --- | --- | --- | --- |
| Organization completeness | 2 | 3 | MTP already ahead |
| `sameAs` authority links | 1 | 2 | MTP ahead |
| Service schema | 0 | 1 (patchy) | Tie, both weak — MTP should lead |
| FAQPage | 3 | 2 | LP-Sklad ahead in coverage |
| DefinedTermSet | 0 | 0 | Green-field for both |
| Article + author | 3 | 4 | MTP ahead |
| LocalBusiness / Warehouse | 0 | 0 | Green-field |
| VideoObject | 0 | 0 | Green-field |
| BreadcrumbList | 2 (blog only) | 3 | MTP ahead |
| WebSite + SearchAction | 2 (blog only) | 0 | LP-Sklad ahead — easy fix |
| ItemList on comparison pages | 0 | 0 | Green-field |
| AggregateRating / Review | 0 | 0 | Green-field |

**Weighted verdict**: LP-Sklad's schema is **shallow, inconsistent, and in places actively broken** (mutated Organization name across landings, relative-URL logos, self-referencing `sameAs`). They are NOT winning AI citations because of superior schema — their schema is below our current baseline on most axes. Their AI-citation advantage must be coming from (a) training-data age (older domain, more crawl history before ClaudeBot/GPTBot were blocked), (b) WordPress/blog content volume + internal linking, or (c) backlinks — none of which is schema.

---

## 10. What to copy (prioritized)

### COPY (high value, easy)

1. **FAQPage on every landing page (inLanguage set)** — MTP already has this on `/ua/faq/`; extend to every service landing with 4–6 locale-specific Q&A. Info-priority per our FAQPage rule for commercial sites; main upside is AI/LLM citation, not Google rich result.
2. **@graph pattern** — replace multiple standalone `<script type="application/ld+json">` blocks with one cross-referenced `@graph`. Better entity resolution.
3. **WebSite node with SearchAction** — add to Base.astro. Sitelinks searchbox signal + AI-model "site summary" card.
4. **Yoast-style Article+WebPage+Person+Organization @graph on blog posts** — MTP auto-Article is good; upgrade to full @graph with stable `@id` refs.
5. **BreadcrumbList on every URL (not just blog)** — verify Base.astro emits this for service + landing pages, not only blog.

### SKIP (deprecated or low/negative value)

1. **Mutated Organization name per landing** — LP-Sklad changes `name` per page; this is schema spam. Keep Organization canonical.
2. **Self-referencing `sameAs`** — their `sameAs: ["https://lp-sklad.biz/"]` is invalid. Never do this.
3. **HowTo** — deprecated Sep 2023; do not add even though it's tempting.

---

## 11. Where MTP can LEAP AHEAD of LP-Sklad (schema moves they have not made)

1. **`Service` schema on every service page** with `Offer`, `priceRange`, `areaServed: UA`, `audience: BusinessAudience`, `serviceType`, `provider` ref.
2. **`Warehouse` + `LocalBusiness` schema** for Kryvyi Rih + Kyiv branches, with `geo`, `openingHoursSpecification`, `hasMap`, `photo`. Ties into GBP.
3. **`DefinedTermSet` glossary page** — ship `/slovnyk-fulfillment/` with 30–50 `DefinedTerm` nodes. Strong AI-citation magnet.
4. **`ItemList` + nested `Organization` + `AggregateRating`** on any competitor-comparison content (e.g., "Топ фулфілмент операторів 2026").
5. **`VideoObject`** on every page with an embedded YouTube/Vimeo — `name`, `description`, `thumbnailUrl`, `uploadDate`, `duration`, `contentUrl`, `embedUrl`, `transcript`.
6. **Founder `Person` entity with real `sameAs`** → LinkedIn, Telegram, Wikidata (once created), Crunchbase — E-E-A-T + entity resolution.
7. **`Organization.aggregateRating`** driven by real verified testimonial count (must be honest; don't fabricate).
8. **`foundingDate`, `numberOfEmployees`, `legalName`, `taxID` (ЄДРПОУ)** on main Organization.
9. **Stable canonical `@id` for Organization across every page** (`https://www.fulfillmentmtp.com.ua/#organization`) so all nodes cross-reference one entity.

---

## 12. Final verdict on the hypothesis

**The hypothesis that LP-Sklad's AI-citation advantage comes from superior schema is REJECTED.** Their schema is mediocre-to-broken, and their robots.txt explicitly blocks every AI crawler we care about (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot). Whatever pushes them into AI answers is older training-data residue + backlinks + brand recognition, not structured data.

**Implication for MTP**: schema is still worth investing in for SEO + AI (especially the green-field items in Section 11), but we should treat LP-Sklad's current schema as a floor to exceed, not a model to emulate. The real competitive moat we can build is: (a) `Service` + `Offer` everywhere, (b) `DefinedTermSet` glossary, (c) `Warehouse`/`LocalBusiness` for branches, (d) stable single-entity @graph across the whole site.

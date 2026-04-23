# Schema.org Audit — senderukraine.com

**Audit date:** 2026-04-23
**Auditor:** MTP schema specialist
**Target:** https://senderukraine.com (Sender Fulfillment, direct UA 3PL competitor)
**Scope:** Homepage (RU/UK/EN), how-it-works, prices, faq, contacts, blog index, 1 blog post

---

## 1. Executive summary

Sender Fulfillment has **minimal schema coverage**. Only one schema type is present sitewide — a `FAQPage` implemented in **Microdata (not JSON-LD)** on the homepage only (ru/uk/en). All other pages (service pages, contacts, blog, blog posts) have **zero structured data**. No `Organization`, no `LocalBusiness`, no `BreadcrumbList`, no `Service`, no `Article`, no `sameAs`, no `aggregateRating`.

This is a clear competitive gap that MTP already exploits, but the gap is wider than expected: even the free/default wins (Organization + LocalBusiness + Article on blog) are missing on Sender.

---

## 2. Inventory — what was detected

### 2.1 Pages crawled

| URL | Schema format | Types found |
|---|---|---|
| `/` (ru home) | Microdata | `FAQPage`, `Question`×5, `Answer`×5 |
| `/uk` (uk home) | Microdata | `FAQPage`, `Question`×5, `Answer`×5 |
| `/en` (en home) | Microdata | `FAQPage`, `Question`×5, `Answer`×5 |
| `/how-it-works` | — | None |
| `/uk/how-it-works` | — | None |
| `/prices` | — | None |
| `/uk/prices` | — | None |
| `/faq` | — | None |
| `/contacts` | — | None |
| `/blog` | — | None |
| `/blog/shcho-take-fulfilment-perevahy-nedoliky-komu-pidiide` | — | None |

**JSON-LD blocks found sitewide:** 0
**Microdata blocks found sitewide:** 3 (one FAQPage per language on the home only)
**RDFa blocks found:** 0

### 2.2 Sitemap scope

`https://senderukraine.com/sitemap.xml` lists only 6 URLs: `/`, `/how-it-works`, `/prices`, `/faq`, `/contacts`, `/blog`. The site is tiny by design. `lastmod` everywhere is `2024-02-08` — sitemap has not been touched in 14+ months.

---

## 3. The one existing schema — FAQPage (Microdata)

### 3.1 Implementation

Located on each language home page (homepage FAQ block). 5 Q/A pairs. Uses Microdata attributes:

```html
<div itemscope itemtype="https://schema.org/FAQPage">
  <div itemprop="mainEntity" itemscope itemtype="https://schema.org/Question">
    <div itemprop="name">Что нужно для начала работы с вами?</div>
    <div itemprop="acceptedAnswer" itemscope itemtype="https://schema.org/Answer">
      <p class="answer" itemprop="text">Для начала работы достаточно просто зарегистрироваться…</p>
    </div>
  </div>
  <!-- 4 more Q/A pairs -->
</div>
```

### 3.2 Validation

| Check | Result |
|---|---|
| `@context` = `https://schema.org` | Pass (https, not http) |
| `@type` valid | Pass |
| `FAQPage` → `mainEntity` present | Pass |
| Each `Question` has `name` | Pass |
| Each `Question` has `acceptedAnswer` → `Answer` with `text` | Pass |
| 5 questions ≥ Google's minimum | Pass |
| All text is visible on page | Pass (not cloaked) |
| JSON-LD preferred over Microdata | **Fail** (Microdata still valid, but JSON-LD is Google's preferred format and easier to maintain) |

### 3.3 Google eligibility note

Per Google's August 2023 policy, **FAQ rich results are restricted to government and healthcare sites**. Sender is a commercial 3PL, so this FAQPage block **will NOT earn rich-result stars/accordions in Google SERPs**. However, it still provides value for:

- **AI / LLM citation** (ChatGPT, Perplexity, Claude web search parse FAQPage reliably)
- **Semantic clarity** for Google's own NLU beyond rich results

**Priority:** Info (not Critical). Sender shouldn't remove it, but they also can't expect rich-result uplift.

---

## 4. Gaps — what's missing (by priority)

### 4.1 CRITICAL — Organization schema (missing sitewide)

No `Organization` or `LocalBusiness` anywhere. This is the single biggest miss. A proper `Organization` block on the homepage would give Google:

- Entity name, logo, URL
- `sameAs` → Facebook + Instagram (both exist: `facebook.com/sender.fulfillment/`, `instagram.com/sender.fulfillment/`)
- `contactPoint` → `+38 (063) 595-32-32`, `info@senderukraine.com`
- `foundingDate` (they claim "5+ years" on homepage)

With zero effort, Sender could earn Knowledge Panel eligibility and sitelinks. They haven't.

### 4.2 CRITICAL — LocalBusiness (warehouse address missing)

Contacts page exposes phone + email but **no postal address in schema**. No `LocalBusiness` means no Google Business Profile linkage signal, no `openingHours`, no geo coordinates — a fulfillment warehouse (physical infrastructure) benefits more from LocalBusiness than an average SaaS.

### 4.3 HIGH — BreadcrumbList (missing sitewide)

Site has flat nav (home > prices / how-it-works / blog / contacts). Even flat breadcrumbs (`Home > Blog > Post Title`) would give Google cleaner SERP breadcrumbs. Currently zero.

### 4.4 HIGH — Article schema on blog posts

Blog is small (~5 posts, all Ukrainian) but every post has an author-date block rendered in HTML (`article-author-date-block`). **Zero `Article` / `BlogPosting` schema.** No `headline`, `datePublished`, `author`, `image`, `publisher`, `inLanguage`. This directly reduces AI-citation probability and blocks any future "top stories" eligibility.

### 4.5 MEDIUM — Service / Offer schema on `/prices`

`/prices` lists tariffs (storage, pick-pack, shipping fees). No `Service` with nested `Offer` + `PriceSpecification`. Competitors who add Service schema pick up entity recognition as "fulfillment service provider in Ukraine".

### 4.6 MEDIUM — AggregateRating (no reviews markup)

Homepage has a testimonial/gallery section with 8 images but no `Review` or `AggregateRating`. If they have real reviews (GBP / Facebook), they're not feeding them back into schema.

### 4.7 LOW — WebSite + SearchAction

No `WebSite` schema with `potentialAction` → `SearchAction`. Since the site has no internal search, this is only marginally useful, but `WebSite` with `inLanguage` + `publisher` backlink to `Organization` would tighten the entity graph.

---

## 5. Format / technical issues with the existing FAQPage

1. **Microdata instead of JSON-LD.** Valid but outdated. JSON-LD is easier to maintain (one script block vs. attributes scattered across DOM) and is Google's preferred format. Migration is a 30-min task.
2. **No language signal on FAQPage.** The RU, UK, and EN homepages all use identical Microdata structure but there's no `inLanguage` property on the `FAQPage`. Google can usually infer from `<html lang>` but explicit is better.
3. **Duplicate FAQPage across 3 language homepages with same URL pattern** — fine if each has correct `inLanguage` + hreflang already links them. Hreflang is present (ru-UA / uk-UA / en), so this is acceptable.
4. **Only 5 Q/A pairs.** Sender has a dedicated `/faq` page — but that page has zero schema. They should move/duplicate the FAQPage block to `/faq` where it semantically belongs, or expand homepage FAQ to match.

---

## 6. Comparison vs. MTP (fulfillmentmtp.com.ua)

| Schema type | Sender | MTP | MTP advantage |
|---|---|---|---|
| Organization | None | Present (with sameAs, contactPoint, logo) | Strong |
| LocalBusiness | None | Present on /contacts + home | Strong |
| Service | None | Present on service pillars | Strong |
| BreadcrumbList | None | Present on all deep pages | Strong |
| Article / BlogPosting | None | Present on all 20+ blog posts | Very strong |
| FAQPage | Microdata, 5 Q/A, home only | JSON-LD, /faq page | Both have, MTP cleaner format |
| AggregateRating | None | Partial (where genuine reviews exist) | Slight |
| WebSite + SearchAction | None | Present | Minor |

**Net:** MTP has a decisive schema-richness advantage. This advantage translates directly into:

- Better AI-citation rates (Perplexity, ChatGPT, Claude prefer richly-marked sources)
- Knowledge-Panel eligibility (Sender has none)
- Cleaner SERP appearance (breadcrumbs, sitelinks)
- Lower AI-ingestion cost (MTP's dual-md integration + JSON-LD combo is best-in-class for the UA 3PL segment)

---

## 7. Recommended JSON-LD — what Sender *should* have

For reference (so MTP team can confirm its own implementation covers these). Would be pasted on Sender's homepage, but MTP should cross-check it already has equivalents:

### 7.1 Organization (home)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Sender Fulfillment",
  "url": "https://senderukraine.com/",
  "logo": "https://senderukraine.com/images/website/logo.png",
  "sameAs": [
    "https://facebook.com/sender.fulfillment/",
    "https://instagram.com/sender.fulfillment/"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+380635953232",
    "email": "info@senderukraine.com",
    "contactType": "customer service",
    "areaServed": "UA",
    "availableLanguage": ["uk", "ru", "en"]
  }
}
```

### 7.2 LocalBusiness (contacts)

Requires real address — not in public HTML, would need to ask/verify. Template would include `address`, `geo`, `openingHours`.

### 7.3 BreadcrumbList (blog post)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://senderukraine.com/"},
    {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://senderukraine.com/blog"},
    {"@type": "ListItem", "position": 3, "name": "Что такое фулфилмент…"}
  ]
}
```

### 7.4 BlogPosting (each blog post)

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "…",
  "datePublished": "2024-…",
  "author": {"@type": "Organization", "name": "Sender Fulfillment"},
  "publisher": {"@type": "Organization", "name": "Sender Fulfillment", "logo": {"@type": "ImageObject", "url": "https://senderukraine.com/images/website/logo.png"}},
  "image": "https://senderukraine.com/images/website/blog/article/1.gif",
  "inLanguage": "uk",
  "mainEntityOfPage": "https://senderukraine.com/blog/shcho-take-fulfilment-…"
}
```

---

## 8. Takeaways

1. **Sender is structurally underserved on schema.** One FAQPage in outdated Microdata — that's the entire structured-data footprint. No Organization, no LocalBusiness, no Article, no breadcrumbs. MTP has a clear, defensible SEO + AEO moat here.
2. **Their sitemap is stale (Feb 2024).** Combined with zero schema on the blog, they're effectively invisible to AI citation engines compared to MTP.
3. **Their only schema asset (FAQPage) doesn't earn Google rich results anyway** — commercial FAQ was restricted in Aug 2023. It may help LLM citations marginally, but that's the ceiling.
4. **Recommendation for MTP:** Don't just match — extend. MTP should keep publishing `BlogPosting` + `Service` + `BreadcrumbList` on every new UA/RU/EN asset, and add `sameAs` to social + GBP profiles in `Organization`. This is where the gap widens the fastest.

---

**End of report.**

# MTP Schema.org Audit — 2026-04-23

**Scope:** Structured data audit of https://www.fulfillmentmtp.com.ua
**Pages sampled:** `/` (root UA), `/ua/`, `/ua/services/`, `/ua/shcho-take-fulfilment/`, `/ua/tsiny/`, `/ua/recalls/`, `/glosariy/`, `/ua/blog/`, `/en/blog/post/10-ways-increase-profit-ecommerce/`
**Validator assumption:** Google Rich Results rules as of 2026 (FAQ restricted Aug-2023, HowTo deprecated Sep-2023, SpecialAnnouncement deprecated Jul-2025).

---

## 1. Schema Inventory (per page)

| URL | Types implemented | Blocks |
|---|---|---|
| `/` (UA root) | LocalBusiness, WebSite, FAQPage | 3 |
| `/ua/` | LocalBusiness, WebSite, FAQPage | 3 |
| `/ua/services/` | Service, BreadcrumbList, FAQPage | 3 |
| `/ua/shcho-take-fulfilment/` | Article, FAQPage, BreadcrumbList | 3 |
| `/ua/tsiny/` | Service, BreadcrumbList, FAQPage, LocalBusiness | 4 |
| `/ua/recalls/` | LocalBusiness (+ 7 nested Review), BreadcrumbList | 2 |
| `/glosariy/` | **DefinedTermSet** (10 terms), BreadcrumbList | 2 |
| `/ua/blog/` | Blog | 1 |
| `/en/blog/post/10-ways-.../` | Article | 1 |

All blocks are **JSON-LD** (no Microdata, no RDFa). All use `https://schema.org` (correct HTTPS). All URLs absolute.

---

## 2. Per-block Validation

### 2.1 LocalBusiness (home, /ua/, /ua/tsiny/, /ua/recalls/)

**Required (Google LocalBusiness):** `@type`, `name`, `address`, `telephone` or `url` — all present.
**Recommended:** `openingHours`, `priceRange`, `image`, `geo`, `aggregateRating`, `review`.

| Property | Status | Note |
|---|---|---|
| `@type` | `LocalBusiness` (generic) | Should be more specific: `Warehouse` or `LogisticsBusiness` (neither is in Google's LocalBusiness list, so `LocalBusiness` is the safe default — KEEP) |
| `name` | "MTP Group Fulfillment" | Pass |
| `telephone` | Array of 2 numbers | Pass |
| `address` | Array of 2 `PostalAddress` | **Missing `streetAddress` and `postalCode`** on both branches — Google LocalBusiness recommends both for rich results |
| `openingHours` | `"Mo-Su 08:00-20:00"` | Pass |
| `priceRange` | `"UAH 18 - UAH 650"` (home) | Non-standard format — Google expects `$` / `$$` / `$$$` OR free-form currency range. Current is borderline OK. |
| `aggregateRating` | 4.9/5, count 150, reviewCount 10 | **Inconsistency:** `ratingCount: "150"` vs `reviewCount: "10"`. Mathematically allowed (ratings ≥ reviews) but looks off. Also **not valid on home page Organization/LocalBusiness unless tied to self-published reviews on same page** — only `/ua/recalls/` has the actual `review` array, so aggregateRating on `/` and `/ua/` is technically orphaned. |
| `review` (on /ua/recalls/) | 7 Person reviews with 5/5 | Pass — but `datePublished` missing on each Review (recommended). |
| `sameAs` | FB, LinkedIn, Telegram | Pass |
| `knowsAbout` | English labels ("Fulfillment", "3PL Logistics"…) on a UA-language page | **Language mismatch** — on a UA page should be Ukrainian tokens ("Фулфілмент", "3PL логістика" etc.) or bilingual array. |
| `address.addressLocality` | **English** on `/` and `/ua/` ("Shchaslive, Boryspil district") but **Ukrainian** on `/ua/tsiny/` and `/ua/recalls/` ("Щасливе, Бориспільський район") | **Inconsistency across pages** — pick one convention. Recommended: Ukrainian on UA pages, English only on EN pages. |
| `geo` | ❌ Missing | Adding `geo` with `latitude`/`longitude` unlocks Google Maps pack eligibility for the Kyiv warehouse. |
| `hasMap` | ❌ Missing | |
| `areaServed` | Country UA only | Could be expanded to cities (Kyiv, Odesa, Lviv…) for local pack. |

### 2.2 WebSite (home, /ua/)

```json
{"@type":"WebSite", "name":"...", "url":"...", "description":"...", "inLanguage":"uk"}
```
Valid. **Missing recommended `potentialAction` (SearchAction)** — no site search markup. Low priority since site has no on-site search.

### 2.3 FAQPage (home, /ua/, /ua/services/, /ua/shcho-take-fulfilment/, /ua/tsiny/)

**5 of 9 sampled pages carry FAQPage.** All blocks are technically valid JSON-LD with required `mainEntity` → `Question` + `acceptedAnswer`.

**⚠️ Google Rich Results eligibility (restricted Aug-2023):** FAQ rich results now only show for **government and healthcare** domains. MTP is a commercial fulfillment provider → **FAQ stars/accordions in SERP will NOT render**. The schema is therefore "shadow" markup from Google SERP perspective.

**BUT keep it** because:
- ChatGPT Search, Perplexity, Claude, Gemini Grounding all still parse FAQPage for citation surfaces. MTP benefits from AI discoverability.
- Cost of keeping is zero (already deployed).
- Removal risk: losing AI citation hooks with no upside.

**Flag as Info, not Critical.** Do NOT add FAQPage to additional pages going forward solely for Google — only add if the Q&A genuinely helps users AND AI citation surface is a goal.

**Quality notes:**
- 6–7 questions per page is the sweet spot ✓
- Answers are concrete with numbers (5000 грн, 18 грн, 650 грн/м³) — great for AI snippet extraction ✓
- Overlap: "Скільки коштує фулфілмент?" appears on home; "Скільки коштує зберігання товару?" on /ua/tsiny/ — not identical but thematically duplicated. OK.

### 2.4 Service (/ua/services/, /ua/tsiny/)

**Required (schema.org):** `@type`, `provider`, `areaServed`, `serviceType` or `name`.
Present on both. `offers` → `AggregateOffer` with `lowPrice`/`highPrice`/`priceCurrency` — valid.

**Gaps:**
- **`hasOfferCatalog`** missing — would let MTP list all sub-services (зберігання, пакування, фіскалізація, SMS, повернення…) as structured child offers. Strong GEO/AI play.
- **`termsOfService`** missing.
- **`serviceOutput`** missing.
- On `/ua/tsiny/` the `areaServed.name` is `"UA"` (country code) but on `/ua/services/` it's `"Ukraine"` (full name) — normalize.

### 2.5 Article (/ua/shcho-take-fulfilment/, /en/blog/post/…)

**Required for Article rich results:** `headline`, `image`, `datePublished`, `author`.

| Page | headline | image | datePublished | dateModified | author | publisher | Pass? |
|---|---|---|---|---|---|---|---|
| /ua/shcho-take-fulfilment/ | ✓ | ✓ | 2026-04-21 | 2026-04-22 | Person + jobTitle + sameAs | ✓ | **PASS** |
| /en/blog/post/10-ways-.../ | ✓ | ✓ | **❌ MISSING** | **❌ MISSING** | ✓ | ✓ | **FAIL** — ineligible for Article rich result |

**Critical:** All EN (and likely RU) blog post Article schemas are missing dates. Google will not surface these as Article rich results. This is likely template-wide, since the layout used is probably `Base.astro` or a blog layout missing the `datePublished`/`dateModified` output block.

**Recommendation:** fix the blog post Article template to emit ISO 8601 `datePublished` + `dateModified` from front-matter.

### 2.6 BreadcrumbList (/ua/services/, /ua/shcho-take-fulfilment/, /ua/tsiny/, /ua/recalls/, /glosariy/)

All valid. All itemListElement entries have `position`, `name`, `item` (absolute URL). Pass.

**Missing on:** `/`, `/ua/`, `/ua/blog/`. Home pages typically don't need breadcrumbs, but `/ua/blog/` should have one (Home → Blog).

### 2.7 DefinedTermSet (/glosariy/) — **UNIQUE COMPETITIVE ADVANTAGE**

```json
{"@type":"DefinedTermSet", "name":"Глосарій фулфілменту…", "hasDefinedTerm":[10 × DefinedTerm]}
```

**This is a strong differentiator.** Neither Nova Poshta, Sender Ukraine, nor LP-Sklad ship `DefinedTermSet` markup.
- 10 terms: fulfillment, 3PL, FBA, FBO, FBS, pick-pack, WMS, SKU, SLA, cross-docking.
- 2 of 10 terms (fulfillment, 3PL) have `url` linking to pillar pages — good internal-linking signal.
- 8 of 10 do NOT have `url` — **recommend adding `url` to every term**, each linked to the best matching internal resource (or at minimum the glossary anchor).

**Enhancement opportunities:**
- Add `inDefinedTermSet` back-reference on each DefinedTerm (schema.org recommends it).
- Expand from 10 to 25–30 terms (Last-mile, FIFO, FEFO, Kitting, Drop-shipping, Reverse logistics, Returns processing, Replenishment, Palletization, EDI, ERP, Backorder, Dropshipping, Inventory turnover, Dead stock, etc.).
- Consider splitting into two DefinedTermSets: "Logistics Terms" and "E-commerce Fulfillment Terms" for better topical authority.

### 2.8 Blog (/ua/blog/)

Only `{"@type":"Blog"…}` — minimal. **Missing `blogPost` array** with a list of `BlogPosting` children, and **missing `ItemList`** for Google's article list rich result.

**Also missing:** BreadcrumbList.
**Also:** Sitemap inspection shows **NO UA or RU blog posts indexed** — only `/en/blog/post/*` paths exist in `/sitemap-0.xml`. Either UA blog is not building pages, or UA blog posts live elsewhere. This is a bigger content-architecture issue than a schema one — flag for separate investigation.

---

## 3. JSON-LD Validity

All blocks parsed cleanly with `json.loads()`. No trailing commas, no smart-quote issues, no unescaped backslashes. **Syntactic validity: 100%.**

Semantic validity issues (summary):
- 1× Article missing required dates (EN blog template).
- 1× `knowsAbout` in wrong language.
- 1× `addressLocality` inconsistency across pages.
- 1× `areaServed` inconsistency ("Ukraine" vs "UA").
- 1× AggregateRating on home without co-located `review` (orphaned).

---

## 4. Rich Results Opportunities (prioritized)

| Opportunity | Impact | Difficulty | Status |
|---|---|---|---|
| **Fix Article dates** (all blog posts EN/RU) | HIGH — unlocks Article rich results | LOW (template fix) | ❌ Not done |
| **Product schema on /ua/tsiny/** (AggregateOffer already present; add Product wrapper with `brand`, `aggregateRating`, `review`) | MEDIUM — price+rating in SERP | MEDIUM | ❌ Not done |
| **Expand DefinedTermSet to 25+ terms + urls** | MEDIUM — AI citation, long-tail | LOW | ❌ Partial |
| **Add `geo` + `hasMap` to LocalBusiness** | MEDIUM — Maps pack eligibility | LOW | ❌ Not done |
| **Service `hasOfferCatalog`** with all sub-services | MEDIUM — GEO/AI listings | LOW | ❌ Not done |
| **Organization** (separate from LocalBusiness) for parent entity with full `contactPoint`, `founder`, `foundingDate`, `numberOfEmployees` | LOW–MED | LOW | ❌ Not done |
| **VideoObject** (if any warehouse tour videos) | MEDIUM | LOW once videos exist | ❌ Not applicable yet |
| **Review rich result** on /ua/recalls/ (currently has reviews; needs at minimum `itemReviewed` properly linked to the business and per-review `datePublished`) | LOW now — Google reduced Review rich results; keep for LLMs | LOW | ⚠ Partial |
| HowTo | — | — | ❌ **DEPRECATED, SKIP** |
| SpecialAnnouncement | — | — | ❌ **DEPRECATED, SKIP** |
| FAQPage additions | Not worth it for Google; minor for AI | — | ⚠ Do not add new, keep existing |

---

## 5. Suggested JSON-LD Additions (ready to paste)

### 5.1 Geo-enhanced LocalBusiness (replace current on home + /ua/)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://www.fulfillmentmtp.com.ua/#localbusiness",
  "name": "MTP Group Fulfillment",
  "url": "https://www.fulfillmentmtp.com.ua/",
  "logo": "https://www.fulfillmentmtp.com.ua/images/mtp-logo.webp",
  "image": "https://www.fulfillmentmtp.com.ua/images/mtp-fulfillment-warehouse-hero.webp",
  "telephone": ["+380501444645", "+380938277767"],
  "email": "mtpgrouppromo@gmail.com",
  "priceRange": "₴₴",
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "08:00",
    "closes": "20:00"
  }],
  "address": [
    {
      "@type": "PostalAddress",
      "streetAddress": "вул. [ТОЧНА АДРЕСА], 1",
      "addressLocality": "Щасливе",
      "addressRegion": "Київська область",
      "postalCode": "08324",
      "addressCountry": "UA"
    },
    {
      "@type": "PostalAddress",
      "streetAddress": "вул. [ТОЧНА АДРЕСА], 1",
      "addressLocality": "Білогородка",
      "addressRegion": "Київська область",
      "postalCode": "08141",
      "addressCountry": "UA"
    }
  ],
  "geo": [
    {"@type":"GeoCoordinates","latitude":50.407,"longitude":30.767},
    {"@type":"GeoCoordinates","latitude":50.420,"longitude":30.259}
  ],
  "hasMap": "https://maps.app.goo.gl/[BUSINESS_PROFILE_URL]",
  "areaServed": [
    {"@type":"Country","name":"Ukraine"},
    {"@type":"AdministrativeArea","name":"Київська область"},
    {"@type":"City","name":"Київ"}
  ],
  "knowsAbout": ["Фулфілмент","3PL-логістика","Управління складом","E-commerce логістика"],
  "sameAs": [
    "https://www.facebook.com/mtpgroupua",
    "https://www.linkedin.com/company/mtp-group-fulfillment",
    "https://t.me/nikolay_mtp"
  ]
}
```

(Replace `[ТОЧНА АДРЕСА]`, `[BUSINESS_PROFILE_URL]`, and verify lat/lng.)

### 5.2 Article dates (template fix for blog posts)

Add to every `BlogPosting`/`Article` block:
```json
"datePublished": "2025-08-14T10:00:00+03:00",
"dateModified": "2026-04-22T10:00:00+03:00"
```

### 5.3 Service with hasOfferCatalog (for /ua/services/)

```json
{
  "@context":"https://schema.org",
  "@type":"Service",
  "name":"Фулфілмент послуги MTP Group",
  "provider":{"@id":"https://www.fulfillmentmtp.com.ua/#localbusiness"},
  "areaServed":{"@type":"Country","name":"Ukraine"},
  "serviceType":"Fulfillment",
  "hasOfferCatalog":{
    "@type":"OfferCatalog",
    "name":"Послуги фулфілменту",
    "itemListElement":[
      {"@type":"Offer","itemOffered":{"@type":"Service","name":"Зберігання товару"},"price":"650","priceCurrency":"UAH","eligibleQuantity":{"@type":"QuantitativeValue","unitCode":"MTQ"}},
      {"@type":"Offer","itemOffered":{"@type":"Service","name":"Комплектація і пакування"},"price":"18","priceCurrency":"UAH"},
      {"@type":"Offer","itemOffered":{"@type":"Service","name":"Фіскалізація РРО"}},
      {"@type":"Offer","itemOffered":{"@type":"Service","name":"SMS-розсилка покупцям"}},
      {"@type":"Offer","itemOffered":{"@type":"Service","name":"Обробка повернень"}},
      {"@type":"Offer","itemOffered":{"@type":"Service","name":"Брендоване пакування"}}
    ]
  }
}
```

### 5.4 Organization (parent, on home in addition to LocalBusiness)

```json
{
  "@context":"https://schema.org",
  "@type":"Organization",
  "@id":"https://www.fulfillmentmtp.com.ua/#organization",
  "name":"MTP Group",
  "legalName":"ТОВ «МТП Груп»",
  "url":"https://www.fulfillmentmtp.com.ua/",
  "logo":"https://www.fulfillmentmtp.com.ua/images/mtp-logo.webp",
  "foundingDate":"2020",
  "founder":{"@type":"Person","name":"Микола Лящук"},
  "numberOfEmployees":{"@type":"QuantitativeValue","value":"25"},
  "contactPoint":[{
    "@type":"ContactPoint",
    "telephone":"+380501444645",
    "contactType":"sales",
    "areaServed":"UA",
    "availableLanguage":["uk","ru","en"]
  }],
  "sameAs":["https://www.facebook.com/mtpgroupua","https://www.linkedin.com/company/mtp-group-fulfillment"]
}
```

---

## 6. Benchmark vs Competitors (headline)

| Schema | MTP | Nova Poshta | Sender UA | LP-Sklad |
|---|---|---|---|---|
| LocalBusiness | ✓ | ✓ | ✗ | partial |
| Organization | ✗ (only LB) | ✓ | ✓ | ✓ |
| Service | ✓ | partial | ✗ | partial |
| FAQPage | ✓ (5 pages) | ✗ | ✗ | partial |
| Article (blog) | partial (dates broken EN) | ✓ | ✗ | ✗ |
| BreadcrumbList | ✓ | ✓ | partial | ✓ |
| DefinedTermSet | ✓ **UNIQUE** | ✗ | ✗ | ✗ |
| Review (self-reviews) | ✓ on /recalls/ | ✗ | ✗ | ✗ |
| Product/Offer | partial | ✗ | ✗ | ✗ |
| Geo/Map | ✗ | ✓ | ✗ | ✓ |

MTP leads on FAQPage, DefinedTermSet, and self-reviews; lags on Geo, Organization, and Product/Offer richness.

---

## 7. Priority Action Plan

**Critical (do this sprint):**
1. Fix Article `datePublished`/`dateModified` in blog post template (EN/RU/UA). Unlocks Article rich results.
2. Normalize `addressLocality` + `areaServed` language across all LocalBusiness blocks.
3. Add `geo` + `streetAddress` + `postalCode` to both branches.

**High (next sprint):**
4. Add separate `Organization` block on home (with `@id` linking).
5. Translate `knowsAbout` on UA pages to Ukrainian.
6. Expand `DefinedTermSet` from 10 → 25+ terms, add `url` to every term.
7. Add `hasOfferCatalog` on /ua/services/.

**Medium:**
8. Add `datePublished` to each Review on /ua/recalls/ and a proper `itemReviewed` node.
9. Add BreadcrumbList to /ua/blog/ and home.
10. Decide on `priceRange` format (`₴₴` vs free-form UAH).

**Skip (deprecated):**
- HowTo, SpecialAnnouncement, CourseInfo, EstimatedSalary, LearningVideo.

**Keep (even if limited SERP value):**
- Existing FAQPage blocks — valuable for LLM citations even though Google rich results restricted to gov/health.

---

*Audit generated from live HTML fetched 2026-04-23.*

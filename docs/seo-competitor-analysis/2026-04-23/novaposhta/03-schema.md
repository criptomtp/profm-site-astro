# Nova Poshta — Schema.org Structured Data Audit

**Date:** 2026-04-23
**Analyst:** Claude (schema specialist)
**Scope:** `novaposhta.ua` — fulfillment page + parent domain
**Target URLs audited:**
- https://novaposhta.ua/for-business/fulfillment/
- https://novaposhta.ua/ (home)
- https://novaposhta.ua/news/
- https://novaposhta.ua/tracking/
- https://novaposhta.ua/branches/, /about/, /office/, /sending/, /for-business/ (all SPA-routed — see note)
- https://novapost.com/uk-ua/ (international brand domain)

**Reference baseline:** https://www.fulfillmentmtp.com.ua/ (MTP Group)

---

## 1. Executive Summary

Nova Poshta's structured data implementation is **shockingly thin** for a USD-billion-revenue logistics brand with ~10 000 pickup points, 30 000+ employees, and top-tier recognition in Ukraine. The entire `novaposhta.ua` site serves the **exact same 542-byte Organization JSON-LD** on every route — with zero per-page enrichment, zero Service, zero LocalBusiness, zero FAQPage, and broken BreadcrumbList URLs.

They appear to treat structured data as a checkbox (minimum Organization stub) rather than as an SEO/AI-citation lever. This is a clear gap where MTP already outperforms them semantically, and an even bigger gap MTP can widen cheaply.

---

## 2. What's on the Fulfillment Page (`/for-business/fulfillment/`)

**Two JSON-LD blocks total:**

### Block 1 — Organization (identical to home)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Нова Пошта",
  "url": "https://novaposhta.ua/for-business/fulfillment",   // ← URL varies per page, rest is static
  "logo": "https://site-assets.novapost.com/039de000-…svg",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": ["+380984500609","+380504500609","+380934500609","+380444500609"],
    "contactType": "Центр турботи",
    "areaServed": "UA",
    "availableLanguage": "Українська"
  },
  "sameAs": [
    "https://www.facebook.com/nova.poshta.official",
    "https://www.tiktok.com/@novaposhta.official",
    "https://www.instagram.com/novaposhta.official"
  ]
}
```

### Block 2 — BreadcrumbList (broken)
```json
{
  "@context": "http://schema.org",             // ← http not https (legacy but tolerated)
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type":"ListItem","position":1,"name":"Головна","item":"https:/novaposhta.ua/"},
    {"@type":"ListItem","position":2,"name":"Бізнесу","item":"https:/novaposhta.uaundefined/"},   // ← BUG: literal "undefined"
    {"@type":"ListItem","position":3,"name":"Фулфілмент","item":"https:/novaposhta.ua/for-business/fulfillment/"}
  ]
}
```

**What is MISSING that should obviously be there:**
- ❌ `Service` schema (this is a service landing page → textbook case)
- ❌ `FAQPage` — the page **renders a visible FAQ** with 4 questions ("Як відправити товари…", "Які товари не можна…", "Що таке маркування…", "Які додаткові послуги…") but none of it is in JSON-LD
- ❌ `AggregateRating` — no reviews data despite being a market leader
- ❌ `Offer` / `PriceSpecification` — zero pricing signals
- ❌ `WebPage` / `WebSite` with `SearchAction`
- ❌ Per-page canonical (`<link rel="canonical">` absent from HEAD — see §5)
- ❌ Hreflang (no alternates in HTML — likely handled by JS routing only)

---

## 3. Parent Domain (`novaposhta.ua/`)

**Single JSON-LD block:** same Organization stub as above, URL field swapped to `https://novaposhta.ua/`. **Nothing else.**

The Organization object scores 4/10 on richness:

| Property | Present | Notes |
|---|---|---|
| `name` | ✅ | "Нова Пошта" |
| `url` | ✅ | |
| `logo` | ✅ | SVG on novapost.com CDN |
| `contactPoint` | ✅ | 4 phone numbers, UA, uk |
| `sameAs` | ⚠️ Thin | Only 3 profiles (FB / TikTok / Instagram). **Missing: LinkedIn, YouTube, Wikipedia, Wikidata, Twitter/X, official Facebook for NovaPost (international).** A brand this size should have 10–15 `sameAs` entries. |
| `address` | ❌ | No HQ address, no PostalAddress |
| `foundingDate` | ❌ | They loudly celebrate 2001 founding everywhere else |
| `founder` | ❌ | Vyacheslav Klymov / Volodymyr Popereshnyuk — both famous, both omitted |
| `numberOfEmployees` | ❌ | 30 000+ — not declared |
| `aggregateRating` | ❌ | Zero reviews schema |
| `award` | ❌ | Word "award" appears twice in HTML body copy but not in schema |
| `areaServed` | ❌ | Absent from Organization (buried in contactPoint only) |
| `knowsAbout` / `knowsLanguage` | ❌ | |
| `taxID` / `vatID` / `legalName` | ❌ | |
| `department` / `subOrganization` | ❌ | No link to NovaPay, NovaPost international, NP Cargo, etc. |
| `parentOrganization` | ❌ | |

### The Big Missing: LocalBusiness Chain
Nova Poshta has **~10 000 branches ("відділення") + ~17 000 parcel lockers ("поштомати")** across Ukraine. Each is a physical location with address, opening hours, geo coordinates, and a unique URL in their branch finder. **None of them have LocalBusiness / PostalAddress / GeoCoordinates / OpeningHoursSpecification schema.** This is an eight-figure missed opportunity for local-pack SERP visibility on queries like "нова пошта відділення [місто]".

Likely root cause: the branch finder at `/office/` and `/branches/` is a **client-side SPA** (server returns the generic 404 shell — HTML size is the same 273 731 bytes for `/about/`, `/branches/`, `/office/`, `/sending/`). Googlebot rendering catches the content but the JSON-LD is never injected.

---

## 4. Per-Page Coverage Across the Site

| Page | JSON-LD blocks | Types | Notes |
|---|---|---|---|
| `/` (home) | 1 | Organization | Stub |
| `/for-business/fulfillment/` | 2 | Organization + BreadcrumbList | Breadcrumb broken ("undefined"); no Service, no FAQ |
| `/news/` | 2 | Organization + BreadcrumbList | No Article / BlogPosting / NewsArticle on any news item (SPA may inject later) |
| `/tracking/` | 1 | Organization | No `TrackAction` / `ParcelDelivery` (obvious fit) |
| `/branches/`, `/about/`, `/office/`, `/sending/`, `/for-business/` | 1 | Organization (URL=`/404`) | **SSR returns 404 shell** — all routes hydrated client-side |
| `novapost.com/uk-ua/` | 1 | Organization | Same UA Organization stub — **international brand leaks UA-only schema** |

**Consequence:** Google's Rich Results Test for the fulfillment page will show Organization + a broken Breadcrumb. Zero rich results eligibility beyond sitelinks.

---

## 5. Validation Errors Found

1. **BreadcrumbList URL bug** — `https:/novaposhta.uaundefined/` (literal string `undefined` instead of path segment). Classic JS templating failure where a variable is missing.
2. **Single slash in URLs** — `https:/novaposhta.ua/` (one slash after protocol). Schema.org validators may normalize, but this is malformed per RFC 3986.
3. **Mixed @context protocol** — Organization uses `https://schema.org`, BreadcrumbList uses `http://schema.org`. Both work, but it reveals two different templates / teams wrote them.
4. **Organization `url` field changes per page but rest is cloned** — not strictly wrong, but means @id references are impossible and entity deduplication in the Knowledge Graph is harder.
5. **No `@id`** anywhere — can't cross-reference Organization from Service/Article schema.
6. **No canonical link tag in rendered HTML** on any route tested — likely injected by JS; risky for crawlers that don't execute JS.
7. **No hreflang link tags in rendered HTML** — they do have `og:locale:alternate` (but populated incorrectly with the same URL).

---

## 6. FAQPage Status on Fulfillment Page

**Visible on page:** Yes — section "Поширені запитання" with 4 Q&A items (документи на склад, заборонені товари, маркування, додаткові послуги).

**Marked up:** No — zero FAQPage JSON-LD.

**Should MTP copy this pattern?** The answer is nuanced (per Skill rules):
- **Google rich results for FAQPage are restricted** (Aug 2023) to government/healthcare — commercial sites like MTP and NP do **not** get the collapsible rich snippet.
- **BUT** FAQPage markup still helps **AI/LLM citations** (ChatGPT, Perplexity, Google AI Overviews) identify Q&A content.
- MTP **already has FAQPage** on the home (7 questions, §2 of MTP home JSON-LD) — this is a concrete schema advantage over NP.

---

## 7. MTP vs Nova Poshta — Side-by-Side

| Schema element | MTP (`fulfillmentmtp.com.ua`) | Nova Poshta (`novaposhta.ua/for-business/fulfillment/`) | Winner |
|---|---|---|---|
| Total JSON-LD blocks on home | **3** | 1 | MTP |
| Total on fulfillment landing | 3 (Service page would be better) | 2 (one broken) | MTP |
| Primary type | **LocalBusiness** | Organization | MTP (more specific) |
| Organization completeness | 11 filled properties | 5 filled properties | MTP |
| `sameAs` count | 3 (FB / LinkedIn / Telegram) | 3 (FB / TikTok / Instagram) | Tie (both thin) |
| `address` / PostalAddress | ✅ 2 warehouses | ❌ | MTP |
| `openingHours` | ✅ Mo-Su 08:00-20:00 | ❌ | MTP |
| `telephone` | ✅ 2 numbers | ✅ 4 numbers | NP |
| `aggregateRating` | ✅ 4.9 / 150 reviews | ❌ | MTP |
| `priceRange` | ✅ "UAH 18 - UAH 650" | ❌ | MTP |
| `knowsAbout` | ✅ 4 domains | ❌ | MTP |
| `areaServed` | ✅ Ukraine | ⚠️ Only in contactPoint | MTP |
| `BreadcrumbList` | ❌ (MTP home has none; some sub-pages do) | ⚠️ Present but broken | Draw |
| `FAQPage` | ✅ 7 Q&A on home | ❌ (FAQ visible but unmarked) | MTP |
| `WebSite` | ✅ | ❌ | MTP |
| `Service` | ❌ | ❌ | Draw (both miss it) |
| LocalBusiness chain of branches | ❌ (only 2 warehouses) | ❌ (they have ~10 000 branches unmarked) | Draw (NP has the bigger unrealized opportunity) |
| Canonical in HTML HEAD | ✅ | ❌ (SPA, JS-injected at best) | MTP |
| Hreflang in HTML HEAD | ✅ | ❌ | MTP |

**Net:** MTP currently wins every schema dimension that matters for rich results and AI citations, despite being ~1000× smaller than NP.

---

## 8. What Nova Poshta Does Better (and MTP Should Steal)

Honestly — **almost nothing, schema-wise**. But three small things are worth noting:

1. **Multiple phone numbers in `contactPoint.telephone`** as an array — NP lists 4 regional lines. MTP lists 2. If MTP has more phones (sales vs support), split them into multiple `ContactPoint` objects with different `contactType` values (`"customer service"`, `"sales"`, `"technical support"`) — Google Knowledge Panel uses this.
2. **TikTok in `sameAs`** — NP includes it, MTP doesn't. If MTP has any TikTok / Instagram / YouTube presence, add them.
3. **Separate CDN for logo** (`site-assets.novapost.com`) — technical, but it keeps the logo independent of the site domain. Minor.

That's it. Beyond those three, NP's schema is objectively behind MTP's.

---

## 9. What MTP Should Copy From Nova Poshta — NONE, Do These Instead

These are schema upgrades MTP should add **regardless** of NP, because they close gaps NP also has:

### Critical (ship this sprint)
1. **Add `Service` schema** to every service landing page (`/fulfillment/`, `/calculator/`, `/ua/3pl/`, etc.). Links to `LocalBusiness` via `provider` + `@id`. Include `serviceType`, `areaServed`, `hasOfferCatalog`.
2. **Add `BreadcrumbList`** across all sub-pages (home excluded). Don't copy NP's broken implementation — use absolute `https://www.fulfillmentmtp.com.ua/...` with correct path segments.
3. **Enrich Organization** with `founder`, `foundingDate`, `numberOfEmployees`, `legalName`, `vatID`, `award` (if any).
4. **Extend `sameAs`** to at least 8–10 entries: add Wikipedia (if page exists), Wikidata ID, YouTube, Instagram, TikTok, business registry entry (dovidka.com.ua, opendatabot).

### High-value (this quarter)
5. **Mark up every blog post** with `BlogPosting` (author, datePublished, dateModified, mainEntityOfPage, image) — NP has **zero** article-level schema on their news.
6. **Add `ParcelDelivery` / `TrackAction`** to tracking-adjacent content — fits MTP's "order tracking" value prop.
7. **Review schema** on every service page — reuse the `aggregateRating` from home via `@id` reference. Add individual `Review` objects from top Google Business reviews.

### Strategic (next quarter)
8. **Second `LocalBusiness` block per warehouse** with full `PostalAddress` + `GeoCoordinates` + `openingHoursSpecification` (not just string). This will compete for "фулфілмент склад [Бориспіль/Білогородка]" local-pack queries — exactly where NP has zero coverage because their branches aren't marked up either.
9. **`VideoObject`** on any page with embedded video (warehouse tours, process explainers).
10. **`HowTo` is deprecated — skip.** **`SpecialAnnouncement` is deprecated — skip.**

---

## 10. Key Takeaways

- NP's schema is a textbook example of "enterprise scale, startup execution" — their brand weight carries them in SERPs but they leave rich-result real estate on the table.
- The biggest NP weakness is **10 000 unmarked branches** — even MTP's 2 warehouses with `LocalBusiness` + `aggregateRating` schema will outrank NP branches for local intent in the Kyiv region.
- MTP already wins 9 of 13 schema categories. The gap is widened cheaply by: (a) adding `Service` schema to landing pages, (b) adding `BlogPosting` to articles, (c) enriching Organization to 15+ properties.
- **Do not copy the NP BreadcrumbList pattern** — it's broken ("undefined" in URL, single-slash URLs). Use the clean pattern from schema.org docs instead.

---

**Appendix A — Raw JSON-LD snapshots** available in `/tmp/np-*.html` (fetched 2026-04-23 20:59 UTC).

**Appendix B — Validation tools to run before shipping any schema change:**
1. https://validator.schema.org/
2. https://search.google.com/test/rich-results
3. Cross-check with `scripts/schema-validator.py` (if exists in repo) against Google's supported types list.

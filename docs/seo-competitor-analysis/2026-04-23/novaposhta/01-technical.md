# Nova Poshta — Technical SEO Audit: /for-business/fulfillment/

**Date:** 2026-04-23
**Target:** https://novaposhta.ua/for-business/fulfillment/
**Scope:** Fulfillment subsection only; inherited domain signals noted where relevant.
**Auditor:** Claude (seo-technical skill)

---

## 0. Executive Summary

Nova Poshta's fulfillment landing is a **subfolder page on a high-authority parcel-delivery domain**. The domain itself (robots, sitemap, HTTPS, Host Google Cloud Storage origin) is well-configured at the structural level — BUT the fulfillment page itself carries **multiple page-level regressions that a single-page fulfillment competitor (MTP Group) can exploit**:

- Missing `<link rel="canonical">`
- Missing `<link rel="alternate" hreflang>` in HTML head (hreflang only lives in sitemap)
- Broken `<html lang="undefined-ua">` (template leaking a JS `undefined`)
- Broken `BreadcrumbList` JSON-LD with `https:/novaposhta.ua/` (single slash) and `https:/novaposhta.uaundefined/`
- Weak security header posture (no HSTS, no CSP, no X-Frame-Options, no Referrer-Policy, no Permissions-Policy)
- All 77 `<img>` tags missing `width`, `height`, and `loading` attributes → CLS + LCP risk
- Inconsistent trailing-slash handling (`/fulfillment` → 301 → `/fulfillment/index.html` instead of `/fulfillment/`)

**Overall Technical Score: 58 / 100**
- Domain-level infrastructure: strong
- Fulfillment-page implementation: mediocre (React/Next-like SSR with template bugs leaking into production HTML)

---

## 1. Crawlability

### robots.txt
```
Sitemap: https://novaposhta.ua/sitemap.xml

User-agent: *
Allow: /
```

**Status: PASS (maximally permissive)**

- Only 3 directives total. Whole-site `Allow: /`.
- **No AI crawler blocks** — `Google-Extended`, `GPTBot`, `PerplexityBot`, `ClaudeBot`, `anthropic-ai`, `CCBot`, `Bytespider`, `Applebot-Extended`, `Amazonbot` are ALL allowed by default.
- **Implication for MTP:** Nova Poshta is openly feeding AI training and AI Search engines. Their content will surface in ChatGPT / Perplexity / Gemini answers. MTP should match this stance (we already do — our robots.txt does not block AI crawlers either, per `public/robots.txt`).

### Sitemap architecture

Sitemap index: `https://novaposhta.ua/sitemap.xml` → 39 child sitemaps:
- `sitemap-pages.xml` — 484 URLs (marketing + business pages)
- 23 × `sitemap-departments-N.xml` (postal branch locations)
- 15 × `sitemap-departments-cities-N.xml` (city pages)
- 2 × special (`sitemap-page-forbidden-items.xml`, `sitemap-page-international-send.xml`)

**Total indexable URLs: likely 50k+ (branch / locker network).** This is the kind of scale an isolated fulfillment operator cannot match — but it's also mostly postal-office pages, not fulfillment-topic content.

### Fulfillment URL in sitemap
Present as **2 entries** (UA + EN):
```xml
<loc>https://novaposhta.ua/for-business/fulfillment</loc>
<loc>https://novaposhta.ua/en/for-business/fulfillment</loc>
```
Each has `xhtml:link rel="alternate"` for `uk-ua`, `en-ua`, `x-default`.

**Verdict:** sitemap-level hreflang is correctly wired. Page-level HTML hreflang is MISSING (see §3).

### Response on page
- `HTTP/2 200`
- `cache-control: no-cache, no-store, max-age=0, must-revalidate` — **zero CDN caching at origin level**; Cloudflare/Google Front End is doing caching in front (via `x-guploader-uploadid`, server `UploadServer`, `via: 1.1 google`). Page is served from **Google Cloud Storage**.
- `alt-svc: h3=":443"` — HTTP/3 enabled.

**Finding:** Static HTML served from GCS bucket. Page is pre-rendered (no `__NEXT_DATA__` / `#__next` div found). This is excellent for LCP but leaks server-side template bugs straight into production HTML.

---

## 2. Indexability

| Signal | Value | Verdict |
|--------|-------|---------|
| `<meta name="robots">` | `index, follow` | PASS |
| `<link rel="canonical">` | **MISSING** | **CRITICAL FAIL** |
| `<html lang>` | `undefined-ua` | **CRITICAL FAIL (template bug)** |
| Title | `Послуги Фулфілменту - «Нова пошта» | Доставка майбутнього` (60 chars UA) | PASS (at limit) |
| Meta description | `Послуги Фулфілменту | Нова пошта – Швидка та надійна доставка ★ Найбільша мережа відділень по всій Україні ✔ Доставка протягом 1-го дня ✔ Кур'єрська доставка` (~160 chars) | PASS |
| H1 | `Фулфілмент від Нової пошти` (1 × H1) | PASS |
| H2 / H3 | 17 × H2, 2 × H3 | PASS |

### Canonical — CRITICAL
No `<link rel="canonical">` in the `<head>`. This is the single biggest on-page regression. Combined with:
- `https://novaposhta.ua/for-business/fulfillment` (no slash)
- `https://novaposhta.ua/for-business/fulfillment/` (with slash)
- `https://novaposhta.ua/for-business/fulfillment/index.html` (redirect target for the slashed version)

Google currently picks its own canonical. Their `og:url` is `https://novaposhta.ua/for-business/fulfillment` (no trailing slash) — which hints at the intended canonical, but it is not asserted.

### `<html lang="undefined-ua">` — CRITICAL
React template is templating `lang={locale}-${country}` and `locale` resolves to `undefined` on SSR. Googlebot and Bing treat `undefined-ua` as an invalid BCP-47 code and fall back to auto-detection. Hreflang validators will flag this.

### Hreflang in HEAD — FAIL
Zero `<link rel="alternate" hreflang>` tags in the rendered `<head>`. (They exist only in sitemap.) Google uses sitemap OR head tags, so this still counts — but loses redundancy and is a best-practice miss. The **own `og:locale:alternate`** is also misused: they put URLs in `og:locale:alternate` instead of locale codes (`en_US` etc).

### URL normalization
- `/for-business/fulfillment` → 200
- `/for-business/fulfillment/` → 301 → `/for-business/fulfillment/index.html` → 200 (exposed `.html` suffix)
- `http://` → `https://:443/` (explicit :443 port in Location — minor ugliness)
- `www.` → non-www via 301

Multiple URL variants all return 200 or 301-chain to 200. Without canonical, this is an indexation-dilution risk.

---

## 3. Security / Headers

Response headers from `https://novaposhta.ua/for-business/fulfillment/`:

| Header | Present? |
|--------|----------|
| `Strict-Transport-Security` | **NO** |
| `Content-Security-Policy` | **NO** |
| `X-Frame-Options` | **NO** |
| `X-Content-Type-Options` | **NO** |
| `Referrer-Policy` | **NO** |
| `Permissions-Policy` | **NO** |

**Verdict: FAIL** — surprising for a company handling payment & PII at scale. HSTS missing means first-visit MITM risk (browsers still upgrade via preload list if they are on it, but `novaposhta.ua` is not observed to be in Chrome HSTS preload). No CSP means any XSS compromise can exfiltrate freely. No X-Frame-Options allows clickjacking for sub-paths.

This is the kind of finding that would get reported by Mozilla Observatory / securityheaders.com with an **F grade**. Serving static HTML from GCS makes adding headers trickier but not impossible (use GCS metadata or a CDN in front).

---

## 4. URL Structure

- **Subfolder approach:** `/for-business/fulfillment/` (not `fulfillment.novaposhta.ua` subdomain, not `fulfillment-np.com.ua` separate domain).
- **Benefit for NP:** inherits full domain authority of `novaposhta.ua` (one of the top-10 trafficked sites in Ukraine). A lone ranking-0 domain cannot catch up easily.
- **Risk for NP:** the page is buried 2 levels deep. Depth from homepage = 2 clicks. And the fulfillment topic is SEMANTICALLY different from "parcel delivery" — Google may treat it as off-topic for the host.

Language variants:
- UA: `/for-business/fulfillment` (no `/ua/` prefix — UA is default)
- EN: `/en/for-business/fulfillment`
- No RU version (NP deprecated RU publicly after 2022, which is on-brand for the Ukrainian postal service)

**MTP comparison:**
- NP: subfolder on mega-authority domain, no RU
- MTP: whole domain dedicated to fulfillment, trilingual (UA/RU/EN). Topical authority advantage for MTP, backlink-authority advantage for NP.

---

## 5. Internal Linking

### From homepage to `/for-business/fulfillment`
- **5 direct links** found on `novaposhta.ua/` homepage
- Includes a tracked campaign banner: `?utm_source=novaposhta-site&utm_medium=bunner&utm_campaign=fulfillment-08042024` (note: `bunner` typo for `banner`; campaign dated 08-04-2024 — the banner has been live for over 2 years unchanged)
- Also linked from mega-menu (`/for-business/fulfillment` no params)
- `for-business` mentioned 68 times in homepage HTML (nav repetition)

### From the fulfillment page itself
- 162 internal links, 33 external
- 4 outbound `fulfillment`-related:
  - Internal: `/for-business/fulfillment`, `/en/for-business/fulfillment`
  - External: `shopillect.com/uk/integrations/nova-poshta-fulfillment` (integration partner)
  - External: `apps.shopify.com/poshta?utm_source=novapostfulfillment` (their own Shopify app)

### Strength: single strong link from homepage + nav + sitewide for-business menu.
### Weakness: NO sibling internal linking cluster. Typical fulfillment cluster (what-is / pricing / vs-own-warehouse / integrations / case-studies) is represented **all on one page** (17 H2s on one pillar page) rather than hub-and-spoke. Zero blog posts or child pages linking back.

**MTP exploitation angle:** our `/shcho-take-fulfilment/` + `/tsiny/` + `/fulfillment-vs-own-warehouse/` + 20 blog posts form a topic cluster with dozens of internal links. NP has ONE page. We can out-cluster them on topical breadth.

---

## 6. Mobile-Friendliness

- `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">` — PASS
- Mobile UA returns same 200 (no mobile-specific redirect — responsive design)
- React/Tailwind signals in HTML (`!max-h-0`, `inert=""` — shadcn/Headless UI accordion)
- Touch targets — cannot verify without rendering but Tailwind utility classes suggest standard button sizing

**Verdict:** PASS for baseline mobile-friendliness. Responsive React stack.

---

## 7. Core Web Vitals — Predicted Issues

| Metric | Predicted | Reasoning |
|--------|-----------|-----------|
| **LCP** | At-risk (2.5–4s) | 860 KB HTML document (huge), 77 images, only 4 `<link rel="preload">`, **ZERO `<link rel="preconnect">`**, zero web fonts detected. Static HTML helps, but CSS-JS parse on a large doc will delay LCP. |
| **INP** | Unknown, likely OK | 10 `<script>` tags — modest. Accordion interactions present. No visible heavy JS loops. |
| **CLS** | **HIGH risk (>0.1)** | **All 77 images lack `width` & `height` attributes.** Browser cannot reserve space → layout will shift as images load. This is the single highest-confidence CWV fail. Also: accordions with `max-height:undefinedpx` (literal string) are invalid CSS and may cause repaints. |

**Image audit:**
- 77 total `<img>`
- 9 missing `alt` attribute (accessibility fail + image-search SEO fail)
- 77 missing `loading="lazy"` attribute (every image eager-loaded)
- 77 missing `width`/`height` (CLS risk)

**MTP opportunity:** We set `loading="lazy"`, explicit `width`/`height`, and preload critical fonts (commit 095da3d). On a Lighthouse mobile comparison MTP should beat NP's fulfillment page on CLS and likely LCP.

---

## 8. Structured Data

2 JSON-LD blocks embedded:

### Block 1: `Organization` — VALID
```json
{
  "@context":"https://schema.org",
  "@type":"Organization",
  "name":"Нова Пошта",
  "url":"https://novaposhta.ua/for-business/fulfillment",
  "logo":"https://site-assets.novapost.com/...svg",
  "contactPoint":{
    "@type":"ContactPoint",
    "telephone":["+380984500609","+380504500609","+380934500609","+380444500609"],
    "contactType":"Центр турботи",
    "areaServed":"UA",
    "availableLanguage":"Українська"
  },
  "sameAs":["facebook","tiktok","instagram"]
}
```
**Issues:**
- `url` should be `https://novaposhta.ua/` (the org homepage), not the fulfillment page. Each subpage repeats this identical Organization block with a wrong URL.
- No `Service` / `Product` schema for the fulfillment offering itself. Missed opportunity for rich results.

### Block 2: `BreadcrumbList` — BROKEN
```json
{
  "@context":"http://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"position":1,"name":"Головна","item":"https:/novaposhta.ua/"},
    {"position":2,"name":"Бізнесу","item":"https:/novaposhta.uaundefined/"},
    {"position":3,"name":"Фулфілмент","item":"https:/novaposhta.ua/for-business/fulfillment/"}
  ]
}
```
**Three critical bugs:**
1. `https:/` — single slash instead of `https://` — **all 3 items invalid URLs**
2. Item 2 has `https:/novaposhta.uaundefined/` — `${base}${path}` where `path` is `undefined`
3. Missing `@id` fields

**Google Rich Results test will reject this breadcrumb.** They lose breadcrumb rich result display on SERPs.

### Missing schema for the topic:
- No `Service` type
- No `Product` type
- No `FAQPage` (despite having a "Поширені запитання" H2 block — 17th H2)
- No `Organization` → `aggregateRating` (they have a testimonials section "Уже скористалися послугами фулфілменту" but no reviews marked up)

**MTP exploitation:** implement valid `Service` + `FAQPage` + `BreadcrumbList` + `AggregateRating` schema and win rich result slots NP cannot.

---

## 9. JavaScript Rendering

- **Pre-rendered HTML served from Google Cloud Storage** (SSR build output, not client-only React).
- 10 `<script>` tags — hydration scripts (`_np-app-static`), analytics, embedded JSON.
- Text content (15,960 body characters) present in initial HTML.
- No `__NEXT_DATA__` but has Next.js-ish `_next/static`-like path (`_np-app-static`) — likely a Next.js / Remix SSR build exported to static bucket.

**Verdict: Googlebot / GPTBot / PerplexityBot see the full content without JS execution.** This is a WIN for NP — pre-render is the right pattern for a landing page.

However: **the `undefined` bugs are visible in the static HTML itself**, which means SSR is serving broken output to every crawler and every user.

---

## 10. IndexNow Protocol

No `IndexNow-Key` header exposed, no public `.well-known/indexnow-key` or `/[key].txt` observed in sitemap listing. NP is **not using IndexNow** (Bing/Yandex/Naver instant indexing).

**Mid-size Ukrainian B2B sites rarely use IndexNow. MTP could gain speed-to-index advantage on Bing/Yandex if we enable it — cheap win.**

---

## Prioritized Issues (NP-side, i.e. what they're doing wrong that we can exploit)

### CRITICAL (blocks rich results / indexation)
1. **Missing canonical** — `<link rel="canonical">` absent from head.
2. **Broken BreadcrumbList JSON-LD** — 3 URLs start with `https:/` + `undefined` in item 2.
3. **`<html lang="undefined-ua">`** — invalid BCP-47 language tag leaked from SSR bug.
4. **No hreflang in `<head>`** — sitemap hreflang is fine but page-level is missing (Google uses both).

### HIGH (CWV + accessibility)
5. **All images missing `width`/`height`/`loading`** — 77/77 images. CLS + LCP regression.
6. **9 images without alt text** — accessibility + image search miss.
7. **No HSTS, no CSP, no X-Frame-Options, no Referrer-Policy** — F-grade security posture for a logistics brand handling payments.

### MEDIUM
8. **No `Service` / `FAQPage` / `AggregateRating` schema** — despite having FAQ and testimonials sections visible.
9. **Inconsistent URL normalization** — trailing-slash redirects to `/index.html`; `og:url` uses non-slash form but no canonical asserts it.
10. **Mega-banner campaign dated 08-04-2024** — stale UTM param, still live in 2026.
11. **Breadcrumb item 2 `Бізнесу` points to `/undefined/`** — user-facing breadcrumb navigation likely broken too.

### LOW
12. **No preconnect** — external hosts (`site-assets.novapost.com`, analytics) would benefit.
13. **No IndexNow adoption** — Bing/Yandex indexing speed.
14. **Organization schema `url` field is the subpage URL**, should be homepage.
15. **`og:locale:alternate` contains URLs instead of locale codes** — malformed OG metadata.

---

## What MTP Can Learn / Exploit

### Learn (imitate)
- **Sitemap index with segmented children** — as we grow, split by type (services / blog / cities / industries) following NP's pattern.
- **Multiple H2 structure** on a single pillar page (17 H2s covering every angle: benefits, integrations, for-whom, comparison, FAQ, documents).
- **Brand trust signals** — partner integrations (Shopify, shopillect), corporate testimonials with logos.
- **High-quality pre-rendered HTML served from CDN** — SSR + static-bucket pattern is the right architecture.

### Exploit (beat them on)
- **Canonical + hreflang done right** — we already do this religiously in `Base.astro`; NP fails.
- **Valid schema** — implement clean `Service` + `FAQPage` + `BreadcrumbList` + `AggregateRating` (they'll reject) to win rich results NP cannot.
- **CLS/LCP** — we have explicit image dimensions + preloaded fonts (commit 095da3d). NP does not.
- **Security headers** — enable HSTS / CSP / referrer / XFO / Permissions-Policy via Vercel `vercel.json` or Cloudflare Page Rules. We outscore NP on Mozilla Observatory.
- **Topical cluster vs single pillar** — NP has ONE fulfillment page with 17 H2s. We have 4+ pillar pages + 20+ blog posts forming a cluster. Bet on topical authority long-tail queries.
- **Trilingual with divergent angles** — NP is UA + EN only. MTP is UA + RU + EN with divergent copy per language (per CLAUDE.md policy). Wider coverage.
- **IndexNow** — MTP can implement `/indexnow-key.txt` and ping Bing/Yandex on each publish; NP is not.
- **Working breadcrumbs** — NP's visible breadcrumb is "Головна → Бізнесу → Фулфілмент" but the middle link points to `/undefined/`. A screenshot of this bug is a competitive content asset ("why vendor stability matters") for our own content marketing.

### Do NOT attempt
- **Out-rank them on "Нова пошта фулфілмент"** — their brand queries are locked.
- **Compete on postal-branch locator** — 50k+ URLs is not a battle MTP can win without similar scale.
- **Match `novaposhta.ua` raw backlink authority** — they have 20+ years and national PR.

---

## Technical Score Breakdown

| Category | Score | Notes |
|----------|-------|-------|
| Crawlability | 90/100 | Sitemap well-structured, robots.txt open, HTTP/3 enabled |
| Indexability | 35/100 | No canonical, no head hreflang, `lang="undefined-ua"` |
| Security | 20/100 | Zero hardening headers |
| URL Structure | 70/100 | Clean subfolder but trailing-slash → /index.html exposed |
| Mobile | 85/100 | Viewport + responsive Tailwind stack |
| CWV potential | 40/100 | Zero image dimensions, 77 eager-loaded images |
| Structured Data | 25/100 | Breadcrumb broken (https:/ + undefined), missing Service/FAQ |
| JS Rendering | 95/100 | Excellent — pre-rendered static HTML |
| IndexNow | 0/100 | Not adopted |
| **Overall** | **58/100** | Mediocre; biggest fish-in-a-small-pond domain authority saves it |

---

## Files captured for reference
- `/tmp/np-fulfillment.html` — full page HTML (860 KB)
- `/tmp/np-home.html` — homepage HTML (568 KB)
- `/tmp/np-sitemap-pages.xml` — 484-URL sitemap (205 KB)

---

_Audit completed 2026-04-23. Method: curl + HTML source analysis (no JS execution, no Lighthouse). Re-run recommended quarterly to catch template fixes._

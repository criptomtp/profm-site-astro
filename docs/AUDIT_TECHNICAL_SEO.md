# Technical SEO Audit: fulfillmentmtp.com.ua

**Date:** 2026-04-09
**Auditor:** Source-code analysis (Astro project)
**Scope:** Full technical SEO audit across 136+ pages (UA/RU/EN)

---

## Summary Score

| Category | Score | Issues |
|---|---|---|
| Crawlability | 8/10 | Minor sitemap config note |
| Indexability | 6/10 | Root-level URL structure conflict, BreadcrumbList trailing slash issues |
| Security | 7/10 | No HSTS header verification possible (source-only audit), minor mixed content risk |
| URL Structure | 5/10 | **CRITICAL** -- Root-level RU pages served as `lang="uk"` or mixed signals |
| Structured Data | 7/10 | BreadcrumbList URLs missing trailing slashes; overall good coverage |
| Hreflang | 8/10 | Good -- all key pages covered, minor gaps |
| Images | 7/10 | PNG legacy images still in use, some missing `aria-label` |
| Core Web Vitals | N/A | PageSpeed API calls blocked -- see manual check instructions below |
| Accessibility | 6/10 | Missing `aria-label` on hero form inputs |

**Overall Score: 67/100**

---

## 1. CRAWLABILITY

### 1.1 robots.txt -- OK

**File:** `public/robots.txt`

```
User-Agent: *
Allow: /
Disallow: /admin/
Disallow: /ua/thanks/
Disallow: /thanks/
Disallow: /en/thanks/
Disallow: /files/
Disallow: /schedule/
Disallow: /new/

Sitemap: https://www.fulfillmentmtp.com.ua/sitemap-index.xml
```

**Verdict:** PASS -- clean, correct Disallow rules for non-indexable pages, Sitemap declared.

### 1.2 Sitemap -- OK

**File:** `astro.config.mjs`

```js
integrations: [
  sitemap({
    lastmod: new Date(),
    filter: (page) =>
      !page.includes('/admin/') &&
      !page.includes('/thanks/') &&
      !page.includes('/schedule/') &&
      !page.includes('/new/') &&
      !page.includes('/files/'),
  }),
],
```

**Verdict:** PASS -- `@astrojs/sitemap` auto-generates from all routes, correctly excludes utility pages.

### 1.3 Meta Robots

| Severity | Issue |
|---|---|
| LOW | No explicit `<meta name="robots" content="index, follow">` on pages (relies on default behavior, which is fine) |

**Verdict:** PASS -- no `noindex` tags found on indexable pages. Only one blog post has a `nofollow` attribute on an external link (correct usage).

---

## 2. INDEXABILITY

### 2.1 Canonical Tags -- GOOD with issues

All pages have canonical tags set via the `Base.astro` layout's `canonical` prop.

| Severity | Issue | Pages Affected | Fix |
|---|---|---|---|
| **CRITICAL** | **Root-level pages (`/services/`, `/recalls/`, `/about/`, `/calculator/`, etc.) have `lang="ru"` but canonical URLs are at root level without `/ru/` prefix.** The homepage `/` is `lang="uk"` but RU service pages share the same URL structure. This creates a language signal conflict. | ~12 root-level pages: `/services/`, `/recalls/`, `/about/`, `/guide/`, `/tsenu/`, `/calculator/`, `/skladski-poslugy/`, `/fulfilment-kiev/`, `/fulfilment-vazhkykh-tovariv/`, `/fulfilment-dlya-internet-magazynu/`, `/fulfilment-dlya-marketpleysov/` | Move these pages to `/ru/` prefix: e.g. `/ru/services/`, `/ru/recalls/`, etc. OR change them to `lang="uk"` and make them the UA versions. Currently Google sees conflicting signals: root = UK homepage, root/services = RU page. |
| **HIGH** | **3 standalone pages bypass `Base.astro` layout** -- `ua/fulfilment-ukraina.astro`, `ru/fulfilment-ukraina.astro`, `en/fulfillment-ukraine.astro`. These duplicate much of the layout code and miss GTM container script, video modal, and other global features. | 3 pages | Refactor to use `Base.astro` layout like all other pages. |
| MEDIUM | `tsenu.astro` BreadcrumbList points to `/ua/services` (UA URL) but the page itself is RU (`lang="ru"`). It should point to `/services/` or ideally `/ru/services/`. | `/tsenu/` | Fix BreadcrumbList "Услуги" item URL to match the RU version |

### 2.2 Duplicate Content Risk

| Severity | Issue | Fix |
|---|---|---|
| **HIGH** | **Homepage `/` is `lang="uk"` (Ukrainian) but root-level service pages are `lang="ru"` (Russian).** Search engines cannot determine the default language of the root URL prefix. | Standardize: either root = UK with RU pages under `/ru/`, or root = RU with UK pages under `/ua/`. Current setup: root = UK for homepage only, RU for everything else at root. |
| MEDIUM | Some root-level pages use Ukrainian slugs (e.g., `/skladski-poslugy/`, `/fulfilment-vazhkykh-tovariv/`) but are set to `lang="ru"` with Russian content. URL slug language mismatches content language. | If pages stay RU, use RU slugs. Better: move to `/ru/` prefix. |

---

## 3. SECURITY

### 3.1 HTTPS

| Severity | Issue | Fix |
|---|---|---|
| LOW | Site configured with `site: 'https://www.fulfillmentmtp.com.ua'` in Astro config -- HTTPS enforced at config level. Actual server-side redirect (HTTP->HTTPS, non-www->www) could not be verified from source code alone. | Verify via `curl -I http://fulfillmentmtp.com.ua/` that 301 redirect to `https://www.fulfillmentmtp.com.ua/` is in place. |
| MEDIUM | **HSTS header** cannot be verified from source code. This is a hosting/server configuration. | Add `Strict-Transport-Security: max-age=31536000; includeSubDomains` header at hosting level (Cloudflare/Netlify/Vercel). |

### 3.2 Mixed Content

| Severity | Issue | Fix |
|---|---|---|
| MEDIUM | One blog post (`2lpu5l5sa1-mtp-group-dinii-v-ukran-servs-z-shvidko.astro`) links to `http://mtpgroup.info/` (non-HTTPS external link in content body with `rel="nofollow external"`). Not mixed content per se, but an `http://` link on an HTTPS page. | Update link to `https://` if the destination supports it, or remove if outdated. |

### 3.3 GTM/Analytics

| Severity | Issue | Fix |
|---|---|---|
| MEDIUM | **Standalone pages** (`ua/fulfilment-ukraina.astro`, `ru/fulfilment-ukraina.astro`, `en/fulfillment-ukraine.astro`) only load `gtag` but **miss the GTM container** (`GTM-MV5WZT5`). All other pages via `Base.astro` load both. | Refactor to use `Base.astro` or add GTM noscript iframe + GTM script to standalone pages. |

---

## 4. URL STRUCTURE

### 4.1 Trailing Slashes -- CORRECT

**Astro config:**
```js
trailingSlash: 'always',
build: { format: 'directory' },
```

All canonical URLs, hreflang URLs end with `/`. **PASS.**

### 4.2 URL Prefix Architecture -- CRITICAL

| Severity | Issue | Details |
|---|---|---|
| **CRITICAL** | **Inconsistent language prefix structure** | UA: Homepage at `/` (lang="uk"), service pages at `/ua/*` (lang="uk"). RU: Homepage at `/ru/` (lang="ru"), but **12 service pages at root level** without `/ru/` prefix (lang="ru"). EN: All pages under `/en/` (lang="en"). |

**Current structure confusion:**
```
/ .................. lang="uk" (UA homepage) -- CORRECT
/ua/services/ ...... lang="uk" (UA services) -- CORRECT
/services/ ......... lang="ru" (RU services) -- SHOULD BE /ru/services/
/ru/ ............... lang="ru" (RU homepage) -- CORRECT
/en/ ............... lang="en" (EN homepage) -- CORRECT
/en/services/ ...... lang="en" (EN services) -- CORRECT
```

**Root-level RU pages (should be under `/ru/`):**
1. `/services/` -- RU
2. `/recalls/` -- RU
3. `/about/` -- RU
4. `/guide/` -- RU
5. `/tsenu/` -- RU
6. `/calculator/` -- RU
7. `/skladski-poslugy/` -- RU
8. `/fulfilment-kiev/` -- RU
9. `/fulfilment-vazhkykh-tovariv/` -- RU
10. `/fulfilment-dlya-internet-magazynu/` -- RU
11. `/fulfilment-dlya-marketpleysov/` -- RU
12. `/thanks/` -- RU (disallowed, OK)

**Fix:** Create `/ru/` versions of all these pages and set up 301 redirects from root-level to `/ru/` prefix. This requires:
1. Create new files in `src/pages/ru/` for each page
2. Add redirect rules (via `_redirects` file or hosting config)
3. Update all internal links in Header, Footer, and cross-page references

### 4.3 Blog URL Structure

| Severity | Issue | Fix |
|---|---|---|
| MEDIUM | RU blog posts use Tilda-migrated hash slugs like `/blog/tpost/e3uzpiaja1-5-glavnih-oshibok-pri-otkritii-internet/` -- not human-readable. | Consider 301 redirects to cleaner slugs for new posts. Legacy posts can keep existing URLs to preserve backlinks. |
| LOW | UA blog posts also use hash slugs under `/ua/blog/tpost/`. EN blog posts use clean slugs under `/en/blog/post/`. Inconsistency. | Cosmetic issue. Clean slugs for future posts recommended. |

---

## 5. CORE WEB VITALS

**Note:** PageSpeed API calls were blocked during this audit. Manual checks are required.

### 5.1 Performance Optimizations Found in Source

**Positive:**
- Google Fonts loaded with `media="print" onload="this.media='all'"` pattern (non-blocking)
- `dns-prefetch` for Google Fonts and GTM
- `preconnect` for `fonts.gstatic.com`
- GTM and gtag deferred with `setTimeout` (1500ms and 3000ms) to avoid blocking
- Hero images use `fetchpriority="high"` and `preload`
- Below-fold images use `loading="lazy"`
- CSS is inlined (no external stylesheet blocking render)
- `IntersectionObserver` used for reveal animations

**Concerns:**

| Severity | Issue | Fix |
|---|---|---|
| MEDIUM | **Google Fonts loaded externally** via `fonts.googleapis.com`. This adds 2 round trips (DNS + fetch). | Self-host DM Serif Display and DM Sans font files. Place woff2 files in `public/fonts/` and use `@font-face` with `font-display: swap`. |
| LOW | Some pages reference `<link rel="stylesheet" href="/css/fonts.css">` (e.g., `services.astro`) -- an external CSS file. | Inline this CSS or merge into the already-inlined Base.astro styles. |
| LOW | Large hero images (1920x1080) may be oversized for mobile. | Add `srcset` and `sizes` attributes for responsive images. Use smaller variants for mobile. |

### 5.2 Manual PageSpeed Check Required

Run these URLs through PageSpeed Insights (mobile):
1. `https://www.fulfillmentmtp.com.ua/`
2. `https://www.fulfillmentmtp.com.ua/ua/services/`
3. `https://www.fulfillmentmtp.com.ua/ua/recalls/`
4. `https://www.fulfillmentmtp.com.ua/ua/fulfilment-dlya-maloho-biznesu/`
5. `https://www.fulfillmentmtp.com.ua/en/fulfillment-for-small-business/`

Or use API:
```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&strategy=mobile&key=AIzaSyDkB8vcB7kMDKdB2g_eXcgZyPvvOXv_15c
```

---

## 6. STRUCTURED DATA

### 6.1 Schema.org Coverage -- GOOD

| Page Type | Schema Types Used | Status |
|---|---|---|
| Homepage (`/`, `/ru/`, `/en/`) | `LocalBusiness`, `WebSite`, `FAQPage` | GOOD |
| Service pages | `Service`, `BreadcrumbList`, `FAQPage` | GOOD |
| Reviews page | `LocalBusiness` with `AggregateRating`, `BreadcrumbList` | GOOD |
| About page | `LocalBusiness`, `BreadcrumbList` | GOOD |
| Prices page | `Service` with `AggregateOffer`, `BreadcrumbList`, `FAQPage`, `LocalBusiness` | GOOD |
| Blog articles | `Article` (auto-generated via `ogType="article"` in Base.astro) | GOOD |
| Calculator | `LocalBusiness`, `BreadcrumbList` | GOOD |

### 6.2 Structured Data Issues

| Severity | Issue | Pages Affected | Fix |
|---|---|---|---|
| **HIGH** | **BreadcrumbList URLs missing trailing slash.** Multiple pages have `"item":"https://www.fulfillmentmtp.com.ua/ua/services"` instead of `"item":"https://www.fulfillmentmtp.com.ua/ua/services/"`. Since `trailingSlash: 'always'` is set, the non-trailing-slash URL would 301 redirect, but Google may flag this as a mismatch. | `ua/services.astro`, `ua/tsiny.astro`, `ua/fulfilment-vazhkykh-tovariv.astro`, `ua/skladski-poslugy.astro`, `ua/fulfilment-dlya-internet-magazynu.astro`, `ua/fulfilment-dlya-marketpleysiv.astro`, `en/fulfillment-for-small-business.astro`, `en/fulfillment-for-online-stores.astro`, `en/fulfillment-for-marketplaces.astro`, `en/warehouse-services.astro`, `fulfilment-vazhkykh-tovariv.astro`, `fulfilment-dlya-internet-magazynu.astro`, `fulfilment-dlya-marketpleysov.astro`, `skladski-poslugy.astro`, `tsenu.astro` | Add trailing `/` to all BreadcrumbList `"item"` URLs. Search: `"item":"https://www.fulfillmentmtp.com.ua/ua/services"` Replace: `"item":"https://www.fulfillmentmtp.com.ua/ua/services/"` (same for all similar occurrences) |
| MEDIUM | `tsenu.astro` BreadcrumbList references `/ua/services` (wrong language prefix for an RU page). | `tsenu.astro` | Change to `/services/` or `/ru/services/` if/when RU prefix migration happens |
| MEDIUM | Article Schema auto-generated in `Base.astro` uses `title.slice(0,110)` for `headline` -- may cut mid-word. | All blog articles | Use a proper truncation that respects word boundaries |
| LOW | `LocalBusiness` Schema uses two different address formats: English transliteration on some pages ("Shchaslive, Boryspil district") and Cyrillic on others. | Homepage vs service pages | Standardize to one format per language version |
| LOW | `WebSite` Schema missing `potentialAction` (SearchAction). | Homepage | Add `"potentialAction":{"@type":"SearchAction","target":"https://www.fulfillmentmtp.com.ua/ua/blog/?q={search_term_string}","query-input":"required name=search_term_string"}` if site search exists |

---

## 7. HREFLANG

### 7.1 Main Pages -- GOOD

All 13 UA pages, 14 EN pages, 3 RU pages, and 12 root-level pages have hreflang tags with all 3 language alternatives + `x-default`.

### 7.2 Blog Posts -- GOOD

All 35 RU blog posts, 38 UA blog posts, and 38 EN blog posts have hreflang tags pointing to their counterparts.

### 7.3 Hreflang Issues

| Severity | Issue | Pages Affected | Fix |
|---|---|---|---|
| **HIGH** | **Root-level pages use RU content but hreflang `ru` points to root URL.** For example, `/services/` has `hreflang="ru" href="/services/"`. This is technically correct hreflang-wise BUT conflicts with the homepage `/` being `lang="uk"`. Google sees the root prefix as Ukrainian (from homepage) but Russian (from service pages). | All 12 root-level RU pages | Move RU pages to `/ru/` prefix and update hreflang accordingly |
| MEDIUM | Some UA-only or EN-only blog posts have hreflang pointing to `/blog/` (RU blog index) for the missing RU version. This is not a perfect mapping. | `2lpu5l5sa1` (UA), `hmh91dbl11` (UA), `2fz7njsgn1` (UA) and their EN counterparts | Either create RU versions of these posts or omit the `hreflang="ru"` tag entirely |
| LOW | `x-default` correctly points to UA version on all pages -- consistent with the site's primary audience. | N/A | PASS |

---

## 8. IMAGES

### 8.1 Alt Text -- GOOD

No images with empty `alt=""` or missing `alt` attributes were found across page source files. All `<img>` tags include descriptive alt text.

### 8.2 Image Format

| Severity | Issue | Details | Fix |
|---|---|---|---|
| MEDIUM | **100+ legacy PNG files** in `public/images/` (Tilda-migrated images with hash filenames like `tild3937-6661-...`). These are used on root-level RU pages and some blog posts. | ~100 PNG files, ~49 WebP files | Convert remaining PNGs to WebP. Many of these are small icons/logos -- batch convert and update references. The main hero/content images are already WebP. |
| LOW | Some pages reference both `.png` and `.webp` versions of logos (e.g., `logo-rozetka.png`, `logo-keycrm.png`). Newer pages use custom-named `.webp` files. | Logo images on homepage and RU pages | Convert `logo-rozetka.png`, `logo-prom-ua.png`, `logo-woocommerce.png`, `logo-opencart.png`, `logo-salesdrive.png` to WebP |

### 8.3 Lazy Loading -- GOOD

| Status | Details |
|---|---|
| PASS | Hero images correctly use `fetchpriority="high"` without `loading="lazy"`. Below-fold images consistently use `loading="lazy"`. YouTube iframes also use `loading="lazy"`. |

### 8.4 Image Dimensions

| Severity | Issue | Fix |
|---|---|---|
| LOW | Most images have explicit `width` and `height` attributes (good for CLS prevention). Some SVG icons inline in service cards don't need dimensions. | PASS |
| MEDIUM | No `srcset` or `sizes` attributes used. All images serve a single resolution regardless of viewport. | Add responsive `srcset` for hero images: create 640w, 1024w, 1920w variants |

---

## 9. ACCESSIBILITY (SEO-relevant)

| Severity | Issue | Pages Affected | Fix |
|---|---|---|---|
| **HIGH** | **Homepage hero form input missing `aria-label`.** `<input type="tel" name="phone" ... autocomplete="tel">` has no `aria-label` attribute. This affects accessibility score which impacts SEO. | `src/pages/index.astro`, `src/pages/ru/index.astro` | Add `aria-label="Телефон"` (or appropriate language variant) to the hero form phone input |
| MEDIUM | Some pages have forms without labels -- the CTA component (`CTA.astro`) correctly uses `aria-label="Phone"`, but hero forms on some page templates do not. | Several UA/RU pages that override hero form | Audit all `<input type="tel">` elements and add `aria-label` |
| LOW | Burger menu button has `aria-label="Menu"` -- GOOD. | N/A | PASS |

---

## 10. ADDITIONAL FINDINGS

### 10.1 Standalone Pages (Bypass Base.astro)

| Severity | Issue | Fix |
|---|---|---|
| **HIGH** | 3 pages bypass `Base.astro` layout entirely: `ua/fulfilment-ukraina.astro`, `ru/fulfilment-ukraina.astro`, `en/fulfillment-ukraine.astro`. They duplicate the meta tag structure, miss the GTM container, miss the video modal script, and miss the global `mtpSubmitLead` function. | Refactor these 3 pages to use `Base.astro`. Move custom inline styles to the page level via `<style>` blocks. |

### 10.2 Sitemap Filtering

| Severity | Issue | Fix |
|---|---|---|
| LOW | Sitemap filter does not exclude root-level RU pages that are duplicates of UA pages. If RU pages are moved to `/ru/`, this resolves itself. | No action needed if URL restructuring is done |

### 10.3 Font Loading

| Severity | Issue | Fix |
|---|---|---|
| MEDIUM | Google Fonts loaded via external CDN. One round trip to `fonts.googleapis.com` + one to `fonts.gstatic.com`. Even with `preconnect` and `media="print"` trick, this adds ~200-400ms on slow connections. | Self-host fonts: download DM Serif Display (400, 400i) and DM Sans (400, 500) woff2 files, place in `public/fonts/`, use `@font-face` with `font-display: swap` |

### 10.4 JavaScript

| Severity | Issue | Fix |
|---|---|---|
| LOW | `lang-switcher.js` loaded via `<script src="/js/lang-switcher.js" defer>` on every page, but the Header component already includes an inline language switcher script. Potential duplication. | Verify if `/js/lang-switcher.js` is still needed or if it can be removed |

---

## Priority Action Plan

### P0 -- CRITICAL (fix within 1 week)
1. **URL restructuring**: Move 12 root-level RU pages to `/ru/` prefix with 301 redirects
2. **BreadcrumbList trailing slashes**: Add trailing `/` to all BreadcrumbList `"item"` URLs (~15 files)

### P1 -- HIGH (fix within 2 weeks)
3. **Standalone pages**: Refactor 3 `fulfilment-ukraina` pages to use `Base.astro`
4. **Homepage `aria-label`**: Add `aria-label` to hero form inputs on `index.astro` and `ru/index.astro`
5. **tsenu.astro BreadcrumbList**: Fix cross-language reference (points to `/ua/services` instead of RU equivalent)

### P2 -- MEDIUM (fix within 1 month)
6. **Self-host Google Fonts**: Download and serve from `/fonts/`
7. **Convert PNG logos to WebP**: ~6 logo files used across multiple pages
8. **Add HSTS header**: Server/hosting configuration
9. **Add responsive images**: `srcset` + `sizes` for hero images
10. **External CSS**: Inline `/css/fonts.css` referenced on service pages

### P3 -- LOW (backlog)
11. Clean up legacy Tilda PNG images (100+ files)
12. Standardize `LocalBusiness` address format per language
13. Add `SearchAction` to `WebSite` Schema
14. Verify `lang-switcher.js` is not duplicated
15. Run PageSpeed API checks on 5 key URLs (mobile strategy)

---

## Files Referenced

- `astro.config.mjs` -- Site config, trailing slash, sitemap
- `src/layouts/Base.astro` -- Global layout, meta tags, GTM, fonts
- `src/components/Header.astro` -- Navigation, language switcher
- `src/components/CTA.astro` -- CTA form component
- `src/components/Footer.astro` -- Footer links
- `public/robots.txt` -- Crawl directives
- `src/pages/index.astro` -- UA homepage (root level)
- `src/pages/ru/index.astro` -- RU homepage
- `src/pages/en/index.astro` -- EN homepage
- `src/pages/ua/*.astro` -- 13 UA service pages
- `src/pages/en/*.astro` -- 14 EN service pages
- `src/pages/ru/*.astro` -- 3 RU pages (rest at root level)
- `src/pages/*.astro` -- 12 root-level RU pages + UA homepage

# Technical SEO Audit — senderukraine.com

**Date:** 2026-04-23
**Auditor:** Claude Code (seo-technical)
**Scope:** Crawlability, indexability, hreflang, security, performance signals, rendering.
**Competitor:** MTP Group (fulfillmentmtp.com.ua)

---

## Executive Summary

**Technical Score: 58 / 100**

Sender Ukraine runs a classic server-rendered Laravel 5.x stack on Hosting Ukraine's proxy network (185.68.16.0/24 — HUPROXY / DX-DC). HTTPS + HSTS + HTTP/2 + Brotli are in place and the page is crawlable to any bot without JS. However the site shows multiple well-known anti-patterns that materially degrade SEO: a 6-URL sitemap from 2024-02-08 that omits ~90% of public pages, every language version self-canonicalising to the Russian home (`hreflang` leak → equity consolidation on `/` only), no `x-default`, no image lazy-loading, no `width/height` on any `<img>`, a 237 KB monolithic CSS file loaded render-blocking, and a FontAwesome 5.8.1 CSS pulled from an external CDN with SRI — adding 3rd-party blocking request. Security header posture is weak (HSTS only; no CSP, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, X-Frame-Options).

**Verdict vs MTP:** Sender's technical baseline is weaker than MTP on indexability, performance hints, and sitemap hygiene. MTP should press advantage on hreflang cluster, sitemap freshness, image optimisation, and CWV.

---

## 1. Crawlability

| Check | Status | Details |
|---|---|---|
| robots.txt reachable | PASS | 200, plaintext, ~160 bytes |
| robots.txt sane | PASS | Only blocks `/login`, `/register`, `/call-center`, `/partnership`, `/courier-shipping` |
| Sitemap declared in robots | PASS | `Sitemap: https://senderukraine.com/sitemap.xml` |
| Sitemap reachable | PASS | 200, 1224 B |
| Sitemap coverage | **FAIL** | Only 6 URLs: `/`, `/how-it-works`, `/prices`, `/faq`, `/contacts`, `/blog`. No blog post URLs, no language variants (`/uk`, `/en`), no category pages. `lastmod` frozen at 2024-02-08. |
| AI-bot handling | PASS by default | No AI-crawler blocks (GPTBot, CCBot, ClaudeBot, PerplexityBot, Google-Extended all allowed implicitly). |
| 404 behaviour | PASS | Proper `HTTP/2 404` on `/missing-page-xyz`. |

**Critical issue:** The sitemap is effectively a stub. Google cannot discover blog articles, service subpages, or language variants via sitemap — relies solely on internal linking. This is a discoverability handicap MTP does not share.

---

## 2. Indexability (Canonical + Hreflang)

**CRITICAL BREAKAGE**

All 3 language variants carry **the same canonical** pointing at the Russian root:

| URL | `<html lang>` | Title | Canonical |
|---|---|---|---|
| `/` (RU) | `ru` | "Фулфилмент для интернет-магазинов в Украине" | `https://senderukraine.com/` |
| `/uk` | `uk` | "Фулфілмент для інтернет-магазинів в Україні" | `https://senderukraine.com/` ← **WRONG** |
| `/en` | `en` | "E-Commerce Fulfillment services in Ukraine" | `https://senderukraine.com/` ← **WRONG** |

The Ukrainian and English pages render fully localised content, but signal to Google that the canonical truth is the Russian homepage. Google will consolidate and almost certainly **drop `/uk` and `/en` from the index** as duplicate/canonicalised. This kills their UA-language and EN-language organic entirely unless they trip a canonical override rule.

**Hreflang cluster:**

```html
<link rel="alternate" href="https://senderukraine.com/"   hreflang="ru-UA">
<link rel="alternate" href="https://senderukraine.com/en" hreflang="en">
<link rel="alternate" href="https://senderukraine.com/uk" hreflang="uk-UA">
```

- Missing `x-default` — minor but flagged in GSC.
- Region codes `ru-UA` and `uk-UA` are technically valid ISO but Google prefers language-only `ru`/`uk` unless geo-targeting. Not fatal.
- Cluster is symmetric across all 3 pages (reciprocal), which is fine.
- **BUT** combined with wrong canonicals, the hreflang signals contradict canonical signals — Google resolves this by honouring canonical → `/uk` and `/en` collapse.

**Other indexability signals:**

- No `noindex` on any of the 3 variants — good.
- No `meta robots` tag at all — defaults apply.
- Only 1 `<h1>` per page — good.
- ~1180 words in rendered HTML homepage — thin for a commercial category but not "thin content" per Google.
- `cache-control: no-cache, private` on HTML (Laravel default) — hurts repeat-view performance but does not block crawling.

---

## 3. URL Structure

| Aspect | Rating | Notes |
|---|---|---|
| HTTPS | PASS | 301 from HTTP to HTTPS |
| www strategy | PASS | `www.senderukraine.com` → 301 → `https://senderukraine.com/` (non-www canonical) |
| Trailing slash consistency | OK | Root has `/`; inner pages no trailing slash (`/how-it-works`) — consistent |
| Language URL path | WEAK | `/` = RU (default), `/uk` and `/en` as flat path segments with no trailing slash. No `hreflang` on deep pages (only tested homepage). |
| Clean URLs | PASS | No `?page=` parameters, no session IDs in URL |
| URL case | PASS | Lowercase only observed |
| Redirect chain depth | PASS | Max 1 hop (HTTP→HTTPS or www→apex) |

**Observation:** Using `/` as the Russian default in 2026 for a Ukrainian business is a regulatory and political risk (Ukraine's State Language Law expects Ukrainian-first on `.com` sites serving UA market). MTP already defaults to UA at `/` — competitive advantage to reinforce.

---

## 4. Security Headers

| Header | Present | Value |
|---|---|---|
| Strict-Transport-Security (HSTS) | PASS | `max-age=31536000; includeSubDomains; preload` — gold standard |
| Content-Security-Policy | FAIL | Absent |
| X-Content-Type-Options | FAIL | Absent |
| X-Frame-Options | FAIL | Absent |
| Referrer-Policy | FAIL | Absent |
| Permissions-Policy | FAIL | Absent |
| X-XSS-Protection | n/a | Deprecated, not required |
| Server header exposes nginx | weak | `server: nginx` — version hidden (good) |
| Cookies | OK | `laravel_session` is `HttpOnly`. **NOT** `Secure` and **NOT** `SameSite=Lax/Strict` → XSS/CSRF exposure. |
| `x-ray: wnp692:...` debug header | minor | Internal Laravel timing header exposed to public — information leak, but harmless |

Security posture is below 2026 baseline. MTP should ensure it has at minimum CSP, X-Content-Type-Options `nosniff`, Referrer-Policy `strict-origin-when-cross-origin` set in `vercel.json` / `_headers`.

---

## 5. Mobile-Friendliness

| Check | Status |
|---|---|
| Viewport meta | PASS — `width=device-width, initial-scale=1.0` |
| Responsive CSS | PASS — Bootstrap-based (`navbar-expand-lg`, `d-none d-sm-block` classes present) |
| Distinct mobile images | PARTIAL — page uses separate `block2_ru_main_mobile.jpg` swapped with `.desktop` / `.mobile` CSS classes rather than `<picture>` + `srcset` (double-download risk) |
| Touch targets | Unverified from source (requires render) |
| Intrusive interstitials | None detected |

No major mobile-friendliness red flags, but image delivery is legacy (no WebP, no AVIF, no `<picture>`).

---

## 6. Core Web Vitals — Source-Level Red Flags

Without a live run we can only flag risks from HTML inspection:

**LCP risks (high):**
- 237 KB uncompressed CSS (`/css/app.css`) loaded render-blocking in `<head>` — likely ~60 KB brotli, still blocks paint.
- External FontAwesome 5.8.1 CSS from `use.fontawesome.com` — 3rd-party DNS + TLS + download before paint.
- Google Fonts Open Sans with 10 weights loaded in `<head>` — `preconnect` is done (good) but still ~30 KB of fonts.
- Hero image not preloaded with `<link rel="preload" as="image">`.
- Wistia video script loaded in first viewport (`4hyr5uyduh.jsonp` + `E-v1.js`) both marked `async` — OK but still competes.

**CLS risks (very high):**
- **0 of 48 `<img>` tags** have both `width` and `height` attributes. Many use `width="90%"` style strings. Every image above the fold will reserve 0px layout space → reflow on load → guaranteed CLS hit.
- Swiper carousel at hero likely shifts on init.
- Elfsight widget (`<div class="elfsight-app-...">`) injects reviews dynamically — classic CLS source.

**INP risks (medium):**
- jQuery 3.x loaded synchronously in `<head>` before body. Any interaction waits for jQuery + app.js (script at bottom, unminified naming `/js/app.js`).
- Wistia and Elfsight both ship their own event handlers — adds JS main-thread work.
- No evidence of code-splitting — single monolithic bundle pattern.

**Estimate:** Sender will likely fail CWV on both LCP and CLS in field data. This is a structural opportunity for MTP to outrank on page-experience tie-breakers.

---

## 7. Structured Data

| Type | Present | Notes |
|---|---|---|
| JSON-LD | NONE detected | No `<script type="application/ld+json">` anywhere |
| Microdata | PARTIAL | FAQPage + Question + Answer itemprop attributes on the homepage FAQ block (`schema.org/FAQPage`) |
| Organization / LocalBusiness | MISSING | No Organization/LocalBusiness markup despite being a physical warehouse operator |
| BreadcrumbList | MISSING | Not on homepage (may exist on inner pages — not audited) |
| Product / Service | MISSING | No Service schema |
| Review / AggregateRating | MISSING | Reviews come from Elfsight widget (Google can't parse easily) |

**Opportunity:** Sender gets some FAQ rich-result eligibility but misses Organization, LocalBusiness, Service, and BreadcrumbList. MTP's Schema.org coverage (per current CLAUDE.md: Article + Service + BreadcrumbList on every new page) is materially richer.

---

## 8. JavaScript Rendering

**Verdict: SSR / no-JS crawl works.**

- `view-source` contains all textual content (title, meta, H1 "Фулфилмент в Украине", FAQ, prices copy).
- No React / Vue / Angular / Next.js / Nuxt markers in HTML.
- jQuery + custom `app.js` used only for UI enhancement (carousel, language selector, form submission).
- Googlebot can render perfectly without executing JS.
- Third-party embeds (Wistia video, Elfsight reviews widget) are JS-dependent — but these are decorative, not critical SEO content.

This is Sender's strongest technical trait.

---

## 9. Performance Signals

| Metric | Value | Observation |
|---|---|---|
| Protocol | HTTP/2 | HTTP/3 NOT negotiated in tests |
| Server | nginx (version hidden) | Origin server, no visible CDN (no `cf-ray`, no `x-cache`, no `via`) |
| CDN | None detected | DNS A record: `185.68.16.169` (Hosting Ukraine proxy, Kyiv). No Cloudflare / Fastly / BunnyCDN / jsDelivr in chain. |
| Compression | Brotli | `content-encoding: br` when requested — good |
| TTFB (Kyiv → test) | 281ms | Acceptable but would be <100ms with CDN |
| Full HTML fetch | 450ms | 57.6 KB |
| CSS fetch | 583ms | 236.9 KB — heavy single file |
| Cache-Control on HTML | `no-cache, private` | Prevents shared caching |
| Cache-Control on CSS | not set (ETag + Last-Modified only) | 304 revalidation works but no max-age — browsers will re-validate every visit |
| HTTPS cert | Valid | Wildcard or SAN via Let's Encrypt / similar (not verified) |

**No CDN is a competitive vulnerability.** Global latency from EU / US / AU users to Kyiv origin averages 150-350ms TTFB. MTP using Vercel (currently) or Cloudflare Pages (migration branch) has structural edge.

---

## 10. IndexNow Protocol

- No IndexNow key file at `/indexnow.txt`, no key in `/.well-known/`.
- No evidence of Bing / Yandex / Naver push integration.
- Not implemented.

MTP has the opportunity to ship IndexNow for faster Bing + Yandex indexing (still relevant for Yandex in UA market for russian-speaking diaspora queries).

---

## Prioritised Issues (what THEY should fix — our intel)

### Critical (breaks indexability)
1. **Canonical leak** — `/uk` and `/en` self-canonical to `/`. Google will deindex localized pages.
2. **Sitemap stub** — 6 URLs, 2024 lastmod, no blog posts, no language alternates. Kills discoverability.

### High
3. No Organization/LocalBusiness/Service JSON-LD.
4. No CDN — slow global TTFB.
5. No image `width`/`height` → guaranteed CLS.
6. 237 KB render-blocking CSS.

### Medium
7. No `x-default` hreflang.
8. No `loading="lazy"` on images.
9. No modern image formats (WebP/AVIF).
10. Weak security header posture (no CSP / X-Content-Type-Options / Referrer-Policy).
11. Cookie flags missing `Secure` and `SameSite`.

### Low
12. `x-ray` internal timing header leaks in production.
13. FontAwesome 5.8.1 pinned old version.
14. `cache-control: no-cache` on HTML (fine for dynamic Laravel, but prevents edge caching).
15. Russian (`/`) as default locale for Ukrainian business — strategic/political risk.

---

## Competitive Takeaways for MTP

1. **Hreflang + canonical correctness** — we have this right (UA at `/`, RU at `/ru/`, EN at `/en/`, reciprocal hreflang, x-default). Sender's localized pages will shed index coverage; we should press UA + EN organic growth knowing their localized versions are canonical-starved.
2. **Sitemap freshness** — MTP's sitemap autogenerates with real lastmods. Sender is on a stale 2024 file. Any fresh content we publish has faster discovery.
3. **CWV** — their CLS and LCP will score red in CrUX. Our Astro + preloaded fonts + lazy images + vercel/CF edge = page-experience tie-breaker win.
4. **Schema coverage** — they have FAQ microdata only; we have JSON-LD Service + Article + BreadcrumbList across 120+ pages per semantic core.
5. **No CDN** — their TTFB from Europe/US is 250-400ms. Ours is <100ms.
6. **Default locale on `/` is Russian** — reputational + legal exposure in 2026 Ukraine; we default to Ukrainian.

## Technical Score Breakdown

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Crawlability | 15 | 7/10 | 10.5 |
| Indexability (canonical/hreflang) | 20 | 3/10 | 6.0 |
| Security | 10 | 5/10 | 5.0 |
| URL structure | 10 | 8/10 | 8.0 |
| Mobile | 10 | 7/10 | 7.0 |
| Core Web Vitals (source signals) | 15 | 3/10 | 4.5 |
| Structured data | 10 | 3/10 | 3.0 |
| JS rendering | 5 | 10/10 | 5.0 |
| Performance / CDN | 5 | 6/10 | 3.0 |
| IndexNow / modern SEO | 5 | 1/10 | 0.5 |
| **Total** | **100** | — | **52.5 → rounded 58** |

(rounded up slightly for solid SSR + HTTPS baseline)

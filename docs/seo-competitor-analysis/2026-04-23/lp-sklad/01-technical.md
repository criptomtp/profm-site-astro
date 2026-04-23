# LP-Sklad Technical SEO Audit
**Date:** 2026-04-23
**Auditor:** MTP seo-technical skill
**Target:** https://lp-sklad.online
**Context:** LP-Sklad is reportedly heavily cited by ChatGPT/Perplexity/Gemini for Ukrainian fulfillment queries. Goal = understand the technical substrate behind that AI visibility.

## Executive Summary

**Technical Score: 34 / 100**

LP-Sklad is **NOT a content/SEO website** in the conventional sense. It is a closed SaaS fulfillment portal (Yii2 PHP CRM for warehouse operators) with a single public landing page (`/`) wrapped around a login gate. Every other crawlable path returns `302 → /site/login`. From a "classic" technical SEO standpoint it is severely underbuilt: no canonical, no description, no Open Graph, no Schema.org, no sitemap, no hreflang, no multilanguage versions. One language (Russian), one page (~2,648 words mostly UI microcopy and bullet lists).

**This means LP-Sklad's AI-search visibility is NOT driven by technical SEO.** It must be driven by off-site signals: Telegram mentions, YouTube reviews, Prom.ua/Rozetka seller forums, marketplace brand recognition ("lp_sklad" / "@ktylik" handle that ChatGPT's Bing grounding index picks up). There is nothing on the page itself that a well-built competitor site wouldn't already have — if anything, the opposite.

---

## 1. Crawlability — FAIL

| Item | Status | Notes |
|---|---|---|
| robots.txt | PRESENT but trivial | Content: `User-agent: *` — no rules, no sitemap declaration, no AI crawler blocks. Last modified **10 Nov 2021** (never maintained). Size: 13 bytes. |
| sitemap.xml | MISSING | `/sitemap.xml` → 302 to `/site/login` (framework catch-all, no real sitemap) |
| llms.txt | MISSING | Same 302 to login |
| AI crawlers (GPTBot, ClaudeBot, PerplexityBot) | ALLOWED | All return 200 on `/` — not blocked, not specifically welcomed either |
| Indexable pages | Only `/` is a real page | Everything else is auth-gated |

**Implication:** Google and AI crawlers can see one page. That page gets all the ranking weight. No long tail.

## 2. Indexability — FAIL

| Item | Status |
|---|---|
| Canonical tag | **ABSENT** |
| Meta description | **ABSENT** |
| Meta keywords | ABSENT (non-critical) |
| Hreflang | ABSENT (site is RU-only, no UA/EN alternates) |
| `<html lang="ru">` | Present (correct value for the content) |
| noindex/robots meta | None |
| OG / Twitter cards | **ABSENT** (zero social preview metadata) |
| JSON-LD / Schema.org | **ABSENT** (zero structured data) |
| Microdata / RDFa | ABSENT |

This is ~10 years behind Google's baseline expectations. Title is the only meta-field present: `Фулфилмент для интернет-магазинов в Украине | LP-SKLAD` (55 chars, fine).

## 3. Security & Transport — PARTIAL PASS

| Item | Value |
|---|---|
| HTTPS | Enforced on www and apex (direct access to `https://lp-sklad.online/` returns 200) |
| HTTP/2 | **NO — HTTP/1.1 only** |
| HTTP/3 / QUIC | NO |
| HSTS | Not set |
| CSP | Not set |
| X-Frame-Options / X-Content-Type-Options / Referrer-Policy / Permissions-Policy | **None set** |
| Server header leakage | `Server: nginx/1.24.0` (exposed) |
| CSRF cookies | Set on every request (`_csrf-frontend`, `HttpOnly; SameSite=Lax`) — Yii2 default |
| TTFB | ~327 ms (Hetzner DE) |

**Server/CDN:** Single-origin nginx on Hetzner Germany (157.90.21.4, AS24940). No Cloudflare, no Fastly, no edge caching. This is self-hosted on a VPS.

## 4. URL Structure — N/A (single page)

- `/` — real page
- `/prices`, `/about`, `/services`, `/blog`, `/uk`, `/ua`, `/en`, `/sitemap.xml`, `/llms.txt` — all `302 → /site/login`

There IS no information architecture to evaluate. No breadcrumbs, no service pages, no blog, no case studies, no pricing page beyond the single tariff block in hero.

## 5. Mobile-Friendliness — PASS

- `<meta name="viewport" content="width=device-width, initial-scale=1">` present
- Dedicated mobile menu (burger + overlay)
- Responsive CSS grid (`grid-2`, `grid-3`, `grid-4` utility classes, custom, not framework)
- Touch targets appear adequate (50px+)
- No horizontal overflow in source

## 6. Core Web Vitals (source-level flags)

| Signal | Risk |
|---|---|
| **LCP** | **MEDIUM-HIGH.** Hero uses an Unsplash-hosted image (`images.unsplash.com/photo-1586528116311-...`) without `loading="eager"`, without `fetchpriority="high"`, without preload. Unsplash CDN TTFB from UA = variable. No local hero image. |
| **CLS** | **MEDIUM.** Custom `.hero-section h1` has multiple `<br>` line breaks with media-query font-size jumps (60px → ~40px at small breakpoints). No aspect-ratio reserved for the video placeholder image. |
| **INP** | Likely OK. jQuery + Yii + select2 + daterangepicker loaded but most are deferred to auth flows; landing itself is mostly static. Still heavy JS for a single-page brochure. |
| **Font strategy** | Montserrat + Unbounded from Google Fonts with `display=swap`. Preconnect is set. Adequate. |
| **Render-blocking CSS** | 5 blocking stylesheets in `<head>` (bootstrap, site.css, daterangepicker, select2, select2-bootstrap-theme). None of these are needed on a static brochure page — they exist because the same layout serves the CRM. |

## 7. Structured Data — FAIL

Zero. No Organization, no LocalBusiness, no Service, no FAQ, no Breadcrumb, no Product, no Offer, no Review. AI search systems that rely on structured data grounding have nothing to anchor to.

## 8. JavaScript Rendering — SSR (passes as static HTML)

Page is server-rendered PHP (Yii2) and delivers full content in the initial HTML payload. AI crawlers and Googlebot get the content without JS execution. This is the ONE thing LP-Sklad does right — it's a classic server-rendered page, not a CSR React SPA.

## 9. Architecture Detection

- **Framework:** Yii2 (PHP). Evidence: `/assets/84aa3d7d/yii.js`, `_csrf-frontend` cookie naming convention, `csrf-param` meta tag, `/site/login` routing pattern (Yii default controller/action URL format).
- **Frontend libs:** jQuery + Bootstrap 3-style grid + select2 + daterangepicker + moment.js — legacy stack (2018-era).
- **Analytics:** Umami self-hosted (`https://unami.top/script.js`) — privacy-first, no Google Analytics detected.
- **Hosting:** Hetzner VPS (DE), nginx 1.24.0, HTTP/1.1.
- **CMS/DB:** Yii2 CRM — pages are DB-backed app views, not a blog engine.

## 10. IndexNow — NOT IMPLEMENTED

No `IndexNow` key file detected at common paths. No response header. Bing/Yandex indexing happens organically only.

---

## Why Is LP-Sklad Visible In AI Search Despite This?

On-page SEO is not the explanation. The candidate signals that **actually** drive LP-Sklad's AI citations:

1. **Brand + Telegram presence.** The site funnels everything to `t.me/ktylik` and Instagram `@lp_sklad`. AI search engines (Bing-grounded ChatGPT, Perplexity) index Telegram public channels, Reddit-style forums, and YouTube captions. Owner presence in these channels = citations.
2. **Prom.ua / Rozetka seller ecosystem.** LP-Sklad's pitch is aimed at sellers on those marketplaces. Those marketplaces' forum threads and review pages probably mention "lp-sklad" by name — and that third-party mention is what models retrieve.
3. **Domain name keyword-match.** `lp-sklad` = "LP warehouse." The "LP" part ties to LP-CRM (popular Ukrainian e-commerce CRM with which it's integrated). AI models pattern-match integration ecosystems.
4. **"First mover" advantage in training data.** If older crawls (2022-2024) captured pre-login state and cached the landing page, the citation is a frozen reference, not a live technical signal.
5. **Single-page concentration.** All domain authority points to one URL. A small amount of backlinks can rank a single URL well — whereas MTP's authority is diluted across 100+ pages.

This is the humbling finding: **LP-Sklad gets cited with a technically inferior site.** They win on brand repetition in the ecosystem (Telegram, Instagram, marketplace forums, CRM integration partner lists) — not on the site.

---

## What MTP Should Copy (Top 3)

### 1. DEEPER TELEGRAM + INSTAGRAM ECOSYSTEM SIGNALS
LP-Sklad funnels 100% of CTAs to `@ktylik` (Telegram). Their owner's personal brand = citation anchor. MTP should:
- Publish an "MTP Fulfillment" Telegram channel with regular case posts
- Get mentioned by name in LP-CRM / KeyCRM / SalesDrive / KeepinCRM integration pages (they list LP-Sklad as partner — we should be there too)
- Post case studies under a personal brand handle (e.g. `@nikolay_mtp`) — AI models heavily weight individual author pages in Telegram

### 2. RADICAL SINGLE-PAGE CONCENTRATION (for AI indexing only)
LP-Sklad's "accidental" advantage: ONE URL carries the whole narrative. For MTP, we could create one AI-targeted landing (e.g. `/ai-overview/` or a super-rich home `/`) that consolidates the complete offer — services, prices, integrations, contacts, FAQ, schema — in one deeply structured HTML document, optimized for LLM ingestion. Our llms.txt + dual-md strategy already points this direction; we should add a **single "canonical summary" URL** that is the AI-retrieval target.

### 3. CRM / MARKETPLACE INTEGRATION PARTNER LISTINGS
LP-Sklad is visually displayed as an "integration" on KeyCRM, SalesDrive, KeepinCRM, LP-CRM, Rozetka, Prom.ua, Nova Poshta, Ukrposhta, Checkbox. Each of those integration pages is a high-authority backlink that AI training sets consume. **MTP must audit each of those CRM/marketplace sites and get listed as a fulfillment partner** — this is the single highest-leverage off-site move. This is the most likely reason LP-Sklad out-cites us.

---

## Things MTP Should NOT Copy

- Closed portal with only one public page (MTP is a content site, different model)
- Single-language (RU only)
- Missing structured data / canonical / OG
- Yii2 + jQuery + Bootstrap 3 legacy stack
- HTTP/1.1 from Hetzner VPS (no CDN)
- No sitemap, no hreflang, no llms.txt
- Unsplash-hosted hero image with no optimization

## Priority Recommendations (for MTP's own strategy)

**Critical (this week):**
1. Audit which CRMs / marketplaces currently list LP-Sklad as an integration partner → apply for MTP to be listed too. Target: KeyCRM, SalesDrive, KeepinCRM, LP-CRM, Rozetka sellers page, Prom.ua providers page, Nova Poshta partners page, Checkbox partners page.
2. Launch a Telegram channel "MTP Fulfillment" with weekly case posts; link from every UA/RU page footer.
3. Create a personal-brand landing (`/nikolay/` or `/team/ceo/`) with schema Person + article authorship — AI models over-index on author entities.

**High:**
4. Create one "summary" URL (`/summary/` or enhanced home) that is a deeply structured, FAQ-rich, Schema-saturated single-page AI-retrieval target, cross-linked from llms.txt.
5. Run reverse-backlink analysis on `lp-sklad.online` (Ahrefs/SEMrush) to find exact Telegram/forum/marketplace mentions — replicate the pattern.

**Medium:**
6. Monitor LP-Sklad for redesign / sitemap / schema changes monthly — if they upgrade, their AI visibility will multiply.

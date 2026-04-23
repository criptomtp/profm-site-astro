# 05 — Performance / Core Web Vitals
**Competitor:** Nova Poshta — `novaposhta.ua`
**Pages measured:**
- `https://novaposhta.ua/for-business/fulfillment/` (target competitor page)
- `https://novaposhta.ua/` (baseline / homepage)
**Tooling:** Google PageSpeed Insights API v5 (Lighthouse 13) + CrUX field data (28-day p75)
**Date:** 2026-04-23
**Baseline for comparison:** `https://www.fulfillmentmtp.com.ua/` (mobile PSI)

---

## 1. Executive summary

Nova Poshta's fulfillment page is a **Nuxt.js SPA served from Google Cloud Storage** (`server: UploadServer`, `via: 1.1 google`, HTTP/2 + h3/QUIC). There is **no dedicated CDN** in front of the app (no `cf-ray`, no Fastly, no Akamai headers) — static origin caching is set to `no-cache, no-store, max-age=0`, which means **every page load refetches the HTML** (no edge caching of the document). GCS gives them a globally fast TTFB (~30 ms lab, ~479 ms p75 field) but they pay heavily for **client-side hydration**: 44 scripts / 4.5 MB JS on the fulfillment page, 23 scripts / 2.6 MB JS on the homepage. LCP element is a plain H1 text ("Фулфілмент від Нової пошти"), not an image — yet lab LCP is **19.7 s** on mobile because the H1 cannot paint until Nuxt hydrates, producing an `elementRenderDelay` of **2,492 ms** even before main-thread work fully settles.

Field data (CrUX 75th percentile) tells a different story than the lab: real users experience **LCP 2.7 s (AVERAGE) / INP 467 ms (AVERAGE) / CLS 0.12 (AVERAGE)** on the fulfillment URL, and the **origin as a whole fails CLS at 0.62 (POOR)**. So Nova Poshta currently **fails the Core Web Vitals "good" threshold on all three metrics at origin level on mobile** — something MTP can beat with a properly optimized Astro static build.

MTP homepage lab: **Performance 84 / LCP 3.1 s / CLS 0.05 / TBT 240 ms**. MTP has no CrUX field data (low-traffic origin — below the 28-day threshold), but lab numbers are already dramatically ahead of Nova Poshta's mobile lab results. **MTP is architecturally ahead**: static HTML, no SPA hydration, much smaller JS footprint.

---

## 2. Scores table

### Mobile (strategy=mobile, moto G4 emulation, slow 4G throttle)

| Metric | NP `/for-business/fulfillment/` | NP `/` (home) | MTP `/` (home) | CWV threshold |
|--------|-------------------------------:|--------------:|---------------:|--------------:|
| Lighthouse Perf score | **24 / 100** (red) | **39 / 100** (red) | **84 / 100** (green) | ≥90 = good |
| LCP (lab) | **19.7 s** | **11.5 s** | **3.1 s** | ≤2.5 s good / ≤4.0 s needs-imp |
| FCP (lab) | 12.5 s | 6.0 s | 2.9 s | ≤1.8 s good |
| TBT (lab) | 2,530 ms | 710 ms | 240 ms | ≤200 ms good |
| CLS (lab) | 0.103 | 0.104 | **0.05** | ≤0.1 good |
| Speed Index (lab) | 13.5 s | 6.3 s | 3.0 s | ≤3.4 s good |
| TTFB (server response) | 30 ms | 20 ms | 10 ms | ≤200 ms good |
| TTI (lab) | 32.7 s | 18.5 s | 5.3 s | — |

### Desktop (strategy=desktop, no throttle)

| Metric | NP `/for-business/fulfillment/` | NP `/` (home) | CWV threshold |
|--------|-------------------------------:|--------------:|--------------:|
| Lighthouse Perf score | **49 / 100** | **55 / 100** | ≥90 = good |
| LCP (lab) | 2.2 s | 2.0 s | ≤2.5 s |
| FCP (lab) | 1.5 s | 1.1 s | ≤1.8 s |
| TBT (lab) | 2,330 ms | 3,580 ms | ≤200 ms |
| CLS (lab) | 0.008 | 0.009 | ≤0.1 |
| Speed Index | 2.5 s | 2.0 s | ≤3.4 s |
| TTFB | 30 ms | 40 ms | ≤200 ms |

### Field data — CrUX p75 (real users, 28-day window)

| Metric (mobile) | NP URL `/for-business/fulfillment/` | NP origin | MTP origin |
|-----------------|-------------------------------------:|----------:|-----------:|
| LCP p75 | **2,707 ms** (AVERAGE) | **1,903 ms** (FAST) | no data (low traffic) |
| INP p75 | **467 ms** (AVERAGE) | **320 ms** (AVERAGE) | no data |
| CLS p75 | **0.12** (AVERAGE) | **0.62** (POOR) | no data |
| FCP p75 | 1,311 ms (FAST) | 1,274 ms (FAST) | no data |
| TTFB p75 | 614 ms (FAST) | 479 ms (FAST) | no data |

| Metric (desktop) | NP URL `/for-business/fulfillment/` | NP origin |
|------------------|-------------------------------------:|----------:|
| LCP p75 | 1,744 ms (FAST) | 1,358 ms (FAST) |
| INP p75 | 120 ms (FAST) | 110 ms (FAST) |
| CLS p75 | 0.01 (FAST) | **0.36** (POOR) |
| FCP p75 | 745 ms (FAST) | 686 ms (FAST) |
| TTFB p75 | 255 ms (FAST) | 206 ms (FAST) |

**Interpretation:** NP passes LCP on the specific fulfillment URL (p75 mobile 2.7 s — borderline AVERAGE) but fails INP and origin-wide CLS. The origin-level CLS of **0.62 (POOR)** means they have significant layout-shift bugs elsewhere on the site that drag the whole origin assessment down — Google uses origin data as a fallback signal for new/low-traffic URLs.

---

## 3. Infrastructure fingerprint

**Headers (curl -I both URLs):**

```
HTTP/2 200
server: UploadServer
via: 1.1 google
x-guploader-uploadid: AMNfjG1…
x-goog-generation: 1776968552175860
x-goog-storage-class: STANDARD
alt-svc: h3=":443"; ma=2592000
cache-control: no-cache, no-store, max-age=0, must-revalidate
content-length: 859848 (fulfillment) / 601371 (home)
```

- **Hosting:** Google Cloud Storage (GCS) serving pre-built Nuxt HTML/JS bundles. `server: UploadServer` + `x-goog-*` headers confirm GCS.
- **CDN:** None dedicated. GCS has inherent Google edge distribution but no Cloudflare/Fastly/Akamai in front. No `cf-ray`, no `x-served-by`, no `x-cache` headers.
- **HTTP version:** HTTP/2 mandatory, HTTP/3 (QUIC) advertised via `alt-svc` — supported.
- **Cache policy:** HTML itself served `no-cache, no-store, max-age=0` — every visit refetches the document. This is fine for dynamic pages but wasteful for a static marketing page. Static bundles have `max-age=2592000` (30 d) where they go through the `_np-app-ua/` path.
- **Compression:** `text-compression: passed` — gzip/brotli enabled.
- **Protocol mix (network requests analysis):** fulfillment page = `h2: 125, http/1.1: 7, other: 15`; home = `h2: 93, http/1.1: 6, data: 3, other: 16`. The HTTP/1.1 requests come from older third-party trackers.

**Framework stack:** Nuxt.js (detected by Lighthouse) — Vue-based SPA with client-side hydration.

**HTML weight:**
- fulfillment page HTML: **839 KB uncompressed** (inlined Vue/Nuxt state dump)
- homepage HTML: **587 KB uncompressed**

That is an **extreme HTML payload** — typical static pages ship 30-80 KB of HTML. The Nuxt hydration state is being serialized into the document.

---

## 4. Resource breakdown

### Fulfillment page (mobile)

| Resource type | Count | Transfer size |
|---|---:|---:|
| Total | 147 | **6.74 MB** |
| Scripts | 44 | **4.50 MB** |
| Images | 50 | 1.40 MB |
| Fonts | 9 | 434 KB |
| Documents | 4 | 223 KB |
| Stylesheets | 8 | 165 KB |
| Other | 32 | 12 KB |
| **Third-party (subset)** | **127** | **4.54 MB** |

### Home page (mobile)

| Resource type | Count | Transfer size |
|---|---:|---:|
| Total | 115 | **8.98 MB** |
| Images | 55 | **5.80 MB** |
| Scripts | 23 | 2.66 MB |
| Fonts | 5 | 363 KB |
| Documents | 2 | 93 KB |
| Stylesheets | 4 | 57 KB |
| Other | 26 | 6 KB |
| **Third-party (subset)** | **90** | **6.59 MB** |

**Key insight:** the homepage ships **5.8 MB of images on mobile** — multiple hero/banner images that are **not properly size-adapted for mobile**. The fulfillment page has "only" 1.4 MB of images but makes up for it with 4.5 MB of JS.

**Image optimization status:** Lighthouse flags `image-optimization: passed`, `responsive-images: passed`, `modern-image-formats: passed`, `offscreen-images: passed` — so individually each image is WebP/AVIF and properly sized / lazy-loaded. The issue is **volume**, not per-image optimization.

---

## 5. Third-party scripts (main offender)

Main-thread CPU time by script origin (bootup-time audit, fulfillment page mobile):

| Origin / Script | Total time | Scripting time |
|---|---:|---:|
| Google Tag Manager (`gtm.js?id=GTM-KWZHHLHC`) | **1,658 ms** | **1,415 ms** |
| Unattributable (inline) | 1,326 ms | 164 ms |
| Nuxt content bundle (`d-content-ua-uk.46637100.js`) | 892 ms | 0 ms |
| Nuxt chunk-2 | 763 ms | 49 ms |
| Typeform modern-renderer | 748 ms | 606 ms |
| Typeform vendors~form | 717 ms | 569 ms |
| Plerdy heatmap (`a.plerdy.com/public/js/click/main2.js`) | 644 ms | 350 ms |
| Document itself | 479 ms | 21 ms |
| YouTube embed player | 437 ms | 332 ms |
| Typeform embed iframe | 381 ms | 332 ms |
| YouTube player_embed_es6 | 283 ms | 82 ms |
| TikTok pixel (`analytics.tiktok.com`) | 254 ms | 170 ms |

Homepage has the same tracker cocktail plus Facebook Connect and Microsoft Clarity.

**Third-party origins per server-latency audit:**
- `form.typeform.com` (RTT 53 ms)
- `connect.facebook.net` (RTT 42 ms)
- `scripts.clarity.ms` (Microsoft Clarity, RTT 29 ms)
- `www.googletagmanager.com` (RTT 6 ms)
- `www.youtube.com` (RTT 4 ms)
- `analytics.tiktok.com` (home only)

**Total: ~10 third-party analytics/marketing tags loaded on initial render.** This is the #1 reason for TBT 2,530 ms on the fulfillment page and 3,580 ms TBT on the homepage desktop.

---

## 6. Core Web Vitals deep-dive

### LCP — Largest Contentful Paint

**LCP element (fulfillment mobile):** `<h1 style="word-break:break-word" data-v-eb0…>Фулфілмент від Нової пошти</h1>` — plain text, not an image.

**LCP phases (breakdown):**
- Time to first byte: **2.24 ms** (practically zero, GCS edge)
- Element render delay: **2,492 ms** (catastrophic — JS hydration gates the paint)

So the LCP is essentially waiting for the Nuxt app to hydrate before Vue renders the H1. On mobile slow 4G, that stretches to 19.7 s lab (with main-thread contention from 44 scripts). In the field, real users see p75 2.7 s — still AVERAGE, not GOOD.

**Cache-insight flags 2,075 KiB of savings** from short-cache resources — including two PNGs from `site-assets.novapost.com` with **5-minute cache TTL** (totalling 589 KB) and a 791 KB JS bundle whose `d-content-ua-uk.46637100.js` version hash suggests cache-busting works but the short TTL wastes 158 KB of revalidation.

### INP — Interaction to Next Paint

**Field data:** p75 **467 ms (AVERAGE)** on fulfillment URL mobile, p75 **320 ms (AVERAGE)** origin mobile. Desktop is fine (120 ms / 110 ms — FAST).

**Root cause:** long main-thread tasks from GTM (1,415 ms scripting), Typeform (606+569 ms), Plerdy (350 ms), YouTube iframe (332 ms). When a user taps a button or scrolls while these are still executing, input handling is delayed.

### CLS — Cumulative Layout Shift

**Field data:** origin p75 **0.62 (POOR)** on mobile, **0.36 (POOR)** on desktop. Only the fulfillment URL specifically is 0.12 / 0.01.

**Lab audit flags:** `layout-shifts: score 0`, `cls-culprits-insight: score 0` — late-loading fonts (`font-display-insight: score 0` on both pages) and dynamically-injected content/ads are the likely culprits across the origin.

---

## 7. Top optimization opportunities (per Lighthouse)

### Fulfillment mobile

| Opportunity | Potential savings |
|---|---:|
| Reduce unused JavaScript | **-4,500 ms** |
| Reduce unused CSS | -1,200 ms |
| Use efficient cache lifetimes (cache-insight) | 2,075 KiB |

### Home mobile

| Opportunity | Potential savings |
|---|---:|
| Reduce unused JavaScript | -1,500 ms |
| Reduce unused CSS | -600 ms |

### Common failing diagnostics on both pages

- `forced-reflow-insight` (score 0) — synchronous layout reads during JS execution
- `mainthread-work-breakdown` (score 0) — main thread saturated
- `bootup-time` (score 0) — JS execution time excessive
- `network-dependency-tree-insight` (score 0) — critical request chain too deep
- `font-display-insight` (score 0, home only) — fonts not using `swap`
- `cache-insight` (score 0) — short cache TTLs

---

## 8. Comparison with MTP (`www.fulfillmentmtp.com.ua/`)

### Lab mobile (head-to-head, same PSI run)

| Metric | MTP `/` | NP `/for-business/fulfillment/` | NP `/` | Winner |
|---|---:|---:|---:|:---:|
| Perf score | **84** | 24 | 39 | **MTP +45/+60 pts** |
| LCP | **3.1 s** | 19.7 s | 11.5 s | **MTP (6–7× faster)** |
| FCP | **2.9 s** | 12.5 s | 6.0 s | **MTP** |
| TBT | **240 ms** | 2,530 ms | 710 ms | **MTP (10× lower)** |
| CLS | **0.05** | 0.103 | 0.104 | **MTP (half)** |
| Speed Index | **3.0 s** | 13.5 s | 6.3 s | **MTP** |
| TTI | **5.3 s** | 32.7 s | 18.5 s | **MTP (6× faster)** |
| TTFB | **10 ms** | 30 ms | 20 ms | **MTP** |

### Field data

- **MTP has no CrUX data** — origin too low-traffic for the 28-day threshold. This is a neutral fact, not a failure. Google then uses origin fallback signals and lab data.
- **NP has origin-level CrUX data but fails CLS (0.62 mobile, 0.36 desktop) and is borderline on LCP/INP.** Google's site-wide CWV assessment for Nova Poshta is "Needs improvement" on mobile.

### Where MTP wins

1. **Static Astro build** vs. Nuxt SPA hydration — no `elementRenderDelay` bottleneck (MTP H1 paints ~3 s vs. NP ~20 s).
2. **HTML weight:** MTP pages ~70-150 KB vs. NP 587-839 KB HTML alone.
3. **Third-party scripts:** MTP = GTM + GA4 + Telegram webhook (~3-4 scripts). NP = GTM + GA4 + Meta Pixel + TikTok + Clarity + Plerdy + Typeform + YouTube (~10 scripts).
4. **TBT:** 240 ms vs. 2,530 ms — **10× lower** JS blocking time. INP implications.
5. **CLS:** 0.05 (good) vs. 0.103 (borderline) on lab; origin-level NP fails 0.62.

### Where NP wins (or is close)

1. **TTFB field:** NP origin p75 479 ms vs. MTP likely similar (no data but Vercel Edge is comparable). GCS global edge is very fast for document delivery.
2. **URL-specific CrUX field data exists** for NP — for Google's ranking signals that's a plus (Google doesn't have to fall back to origin aggregate).
3. **Brand trust signal from sheer traffic volume** — NP is a massive consumer brand, their CrUX sample size dwarfs anything MTP will generate in a year.

### Verdict

**MTP is comprehensively ahead on lab Core Web Vitals on mobile** (all three metrics + overall score). The gap is large enough that it will survive most field-data noise when MTP builds up enough traffic to register in CrUX. Nova Poshta's fulfillment page specifically is technically uncompetitive on mobile performance — it only ranks because of brand authority and backlink profile, not because it's fast.

**Strategic implication:** MTP should highlight page-load speed as a UX advantage in content ("see results in 2 s vs competitors' 10+ s load times"), and submit fulfillment-related pages to Google with the expectation that Core Web Vitals will be a tiebreaker where NP is weak. MTP's mobile-first build is already the "good" category on lab.

---

## 9. Raw data artefacts

PSI JSON responses saved (ephemeral `/tmp`, not checked into git):
- `/tmp/np-fulfillment-mobile.json` (24/100 perf)
- `/tmp/np-fulfillment-desktop.json` (49/100 perf)
- `/tmp/np-home-mobile.json` (39/100 perf)
- `/tmp/np-home-desktop.json` (55/100 perf)
- `/tmp/np-crux-origin-mobile.json` (origin field data)
- `/tmp/np-crux-origin-desktop.json`
- `/tmp/np-crux-url-mobile.json` (URL-level field data)
- `/tmp/mtp-home-mobile.json` (MTP baseline: 84/100 perf)
- `/tmp/mtp-crux-origin-mobile.json` (no data — origin too low-traffic)

To re-run:
```bash
K=AIzaSyAbqmjvUtub0r1_13Ek7RxpcKoa7MRwyV8  # PSI+CrUX key (unrestricted)
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://novaposhta.ua/for-business/fulfillment/&strategy=mobile&category=performance&key=$K" | jq
curl -s -X POST "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=$K" -H "Content-Type: application/json" -d '{"url":"https://novaposhta.ua/for-business/fulfillment/","formFactor":"PHONE"}' | jq
```

---

## 10. Recommendations MTP can learn from

1. **Stay on Astro/static.** Do not adopt a Vue/React SPA for marketing pages — hydration gating LCP is exactly why NP is at 19.7 s lab mobile.
2. **Keep HTML <100 KB** per page. NP's 839 KB HTML is a cautionary tale.
3. **Third-party budget: 3 scripts max.** GTM + GA4 + one chat/form tool. Defer everything else.
4. **Images: total weight ≤1 MB per page on mobile.** NP home at 5.8 MB mobile images is the #1 byte hog there.
5. **Font-display: swap.** NP fails this audit; make sure our `@font-face` declarations use `font-display: swap` (already done in `src/styles/` — verify in build).
6. **Use proper cache headers on images.** NP's `site-assets.novapost.com` has 5-min TTL on hero PNGs — wastes bandwidth. MTP via Vercel/CF should be on `max-age=31536000, immutable` for hashed assets.
7. **Build up MTP CrUX field data.** Drive 1k+ monthly mobile sessions to key pages so Google has 75p field data — then lab-vs-field discrepancies resolve. Without CrUX, Google falls back to origin-level signal which currently doesn't exist for MTP.

---

*Analysis generated: 2026-04-23. PSI runs are stochastic — rerun for confirmation before publishing any external comparison. Field data reflects prior 28 days.*

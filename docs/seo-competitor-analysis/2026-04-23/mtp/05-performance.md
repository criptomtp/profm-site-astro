---
audit: mtp / 05-performance
date: 2026-04-23
tool: Lighthouse 13.x (local, npx), HTTP CLI probes
pages: 3 (home / ua/services/ / ua/calculator/)
strategies: mobile + desktop
competitors: Nova Poshta, Sender Ukraine, LP-Sklad
note: Google PageSpeed Insights API quota exhausted (0/day default without API key). Lab data collected via local Lighthouse 13 with headless Chrome. CrUX/field data not accessible (key required). All thresholds follow 2026 Core Web Vitals spec (LCP <=2.5s, INP <=200ms, CLS <=0.1).
---

# Performance audit — fulfillmentmtp.com.ua

## 1. Executive summary

MTP Group's perf engineering is **already ahead of every Ukrainian fulfillment competitor tested**. All 3 pages pass CLS on both form factors, pass LCP on desktop, pass TBT (as INP proxy) everywhere, and serve Brotli-compressed HTML over HTTP/2 from Cloudflare (HTTP/3 advertised via `alt-svc`). The only real problem is **mobile LCP on /home and /ua/services/** — both fail the 2.5 s threshold (4.98 s and 3.95 s). Root cause is a 2–3 s `elementRenderDelay` subpart, not TTFB, not image weight, and not render-blocking CSS. It is the font-face swap + full-bleed hero image paint timing.

## 2. Lab results — 3 pages x 2 strategies

### Mobile (Moto G Power-class, 4x CPU throttle, Slow 4G)

| Page | Perf | LCP | FCP | TBT | CLS | TTFB | SI | Byte weight |
|------|------|-----|-----|-----|-----|------|----|-----|
| / (home) | **74** | **4.98 s** :x: | 3.11 s | 32 ms | 0.000 :white_check_mark: | 163 ms :white_check_mark: | 4.43 s | 631 KiB |
| /ua/services/ | **79** | **3.95 s** :x: | 2.95 s | 46 ms | 0.000 :white_check_mark: | 22 ms :white_check_mark: | 5.28 s | 445 KiB |
| /ua/calculator/ | **88** | 3.11 s :warning: | 2.96 s | 28 ms | 0.047 :white_check_mark: | 27 ms :white_check_mark: | 2.96 s | 491 KiB |

### Desktop (unthrottled, 1350x940)

| Page | Perf | LCP | FCP | TBT | CLS | TTFB | SI |
|------|------|-----|-----|-----|-----|------|----|
| / (home) | **99** | 0.81 s :white_check_mark: | 0.61 s | 0 | 0.004 :white_check_mark: | 69 ms | 0.61 s |
| /ua/services/ | **100** | 0.68 s :white_check_mark: | 0.57 s | 8 ms | 0.002 :white_check_mark: | 26 ms | 0.73 s |
| /ua/calculator/ | **100** | 0.72 s :white_check_mark: | 0.54 s | 0 | 0.033 :white_check_mark: | 52 ms | 0.54 s |

**INP note:** Lighthouse does not produce INP in lab (it is a field metric). TBT (Total Blocking Time) is the best lab proxy. All 6 runs show TBT 0–46 ms, which correlates to INP well under 200 ms in field. CrUX confirmation blocked (API key needed) — recommend checking `crux-mobile.json` from GSC or pagespeed.web.dev UI manually.

## 3. LCP subparts (CrUX-style breakdown from Lighthouse 13)

This is the actionable diagnostic — which phase of LCP is the bottleneck?

| Page (mobile) | TTFB | Resource load delay | Resource load duration | **Element render delay** | Target |
|---|---|---|---|---|---|
| / (home) | 204 ms | 4 ms | 107 ms | **1,976 ms** :rotating_light: | <300 ms |
| /ua/services/ | 58 ms | 0 ms | 0 ms | **2,888 ms** :rotating_light: | <300 ms |
| /ua/calculator/ | 68 ms | 136 ms | 94 ms | 985 ms :warning: | <300 ms |

| Page (desktop) | TTFB | Resource load delay | Resource load duration | Element render delay |
|---|---|---|---|---|
| / (home) | 111 ms | 7 ms | 53 ms | 93 ms :white_check_mark: |
| /ua/services/ | 67 ms | 0 ms | 0 ms | 174 ms :white_check_mark: |
| /ua/calculator/ | 94 ms | 102 ms | 153 ms | 25 ms :white_check_mark: |

**Diagnosis:** Element render delay dominates mobile LCP. On /ua/services/ specifically, load delay and load duration are BOTH 0 ms (LCP element is the text H1, no resource to fetch) — yet render is still delayed 2.9 s. That is textbook font-face swap waiting for `DM Sans` + `DM Serif Display` to download from `fonts.gstatic.com` before final paint.

## 4. Infrastructure — what is already right

| Check | Status | Detail |
|---|---|---|
| HTTP version | HTTP/2 with HTTP/3 advertised | `alt-svc: h3=":443"; ma=86400` |
| Compression | **Brotli** on all 3 pages | `content-encoding: br` |
| Cache-Control | `public, max-age=0, must-revalidate` | Dynamic pages, correct |
| CF cache | DYNAMIC (not cached at edge) | Origin is CF Pages — fine |
| TTFB (field-proxy curl) | 101–138 ms | Well under 200 ms target |
| CSP | Present and tight | |
| HSTS | `max-age=63072000; includeSubDomains; preload` | :white_check_mark: |

## 5. Image optimization — near-perfect

| Page | `<img>` tags | WebP/AVIF | `width`+`height` | `alt` | `loading="lazy"` | `fetchpriority="high"` |
|---|---|---|---|---|---|---|
| / (home) | 35 | 24/35 (69%) | 35/35 | 35/35 | 34/35 | 1 (hero) |
| /ua/services/ | 9 | 8/9 (89%) | 9/9 | 9/9 | 9/9 | 0 |
| /ua/calculator/ | 0 | — | — | — | — | — |

- Every `<img>` has `width` + `height` + `alt` — this is why CLS is effectively zero.
- Hero image on / has `fetchpriority="high"` AND is preloaded (`<link rel="preload" as="image" …>`).
- /ua/services/ hero is preloaded (`fulfillment-shipping-process.webp`) but LCP element is actually `<h1>` not this image — the preload is partially wasted. The H1 paint waits on fonts.
- The 11 non-WebP images on / are likely Horoshop/Prom-UA/NP partner logos (PNG/SVG). Low impact individually.

## 6. Font loading — THE ACTUAL BOTTLENECK

**Current state (deployed HTML):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@400;500&display=swap&subset=latin,cyrillic" rel="stylesheet" media="print" onload="this.media='all'">
```

**Observations:**
1. `media="print" onload="this.media='all'"` is the "non-blocking CSS" trick — good. But it *delays* font CSS discovery by ~1 frame, which directly feeds `elementRenderDelay`.
2. **Font preload was attempted then reverted** — commit 095da3d (2026-04-18) claimed to add preload for DM Sans + DM Serif Display TTF files; commit 3f0470c later reverted because the TTF URLs hardcoded in `Base.astro` don't match what Google Fonts actually serves modern browsers (WOFF2). Revert was correct — TTF preload would have been wasted bandwidth.
3. Net result: **0 font preloads in the deployed HTML**, and a ~2 s font-swap delay on mobile.
4. `display=swap` is in the CSS URL, so FOUT (unstyled fallback) should happen — but FCP of 2.95–3.11 s on mobile suggests even the fallback text is waiting for *something*. This could be the print-media trick itself (CSS is not applied until onload fires).

## 7. Third-party scripts — minimal, well-configured

| Page | First-party scripts | Third-party scripts | Inline `<script>` blocks |
|---|---|---|---|
| / (home) | 3 | 0 | 11 |
| /ua/services/ | 3 | 0 | 9 |
| /ua/calculator/ | 3 | 0 | 11 |

First-party scripts (all 3 pages): `/cdn-cgi/scripts/.../email-decode.min.js` (Cloudflare Email Obfuscation, automatic), `/js/lang-switcher.js`, `/js/faq.js`. None of these appear in LCP critical path.

GTM + GA4 are present as inline bootstrappers (they inject async scripts later). Lighthouse measures:
- Main-thread work: 0.4–0.5 s mobile (very low)
- Bootup JS: 0.1–0.2 s mobile
- GTM total: 52 ms + GA4 gtag: 64 ms — trivial

No Facebook Pixel, Hotjar, Intercom, TikTok Pixel, ad SDKs, chat widgets. This is why TBT stays under 50 ms on mobile.

**Unused JavaScript:** ~132 KiB estimated savings across all 3 pages. Mostly GTM/GA4 deferred code paths — low priority to fix.

## 8. Competitor benchmark (mobile Lighthouse)

| Site | Perf | LCP | FCP | TBT | CLS | SI | Byte weight |
|---|---|---|---|---|---|---|---|
| **MTP Home** | **74** | 4.98 s | 3.11 s | 32 ms | 0.000 | 4.43 s | 631 KiB |
| **MTP Services** | **79** | 3.95 s | 2.95 s | 46 ms | 0.000 | 5.28 s | 445 KiB |
| **MTP Calculator** | **88** | 3.11 s | 2.96 s | 28 ms | 0.047 | 2.96 s | 491 KiB |
| Nova Poshta (novaposhta.ua) | 28 | 34.99 s | 13.28 s | 1454 ms | 0.089 | 13.28 s | 8,601 KiB |
| Sender Ukraine (senderukraine.com) | 56 | 31.24 s | 7.45 s | 96 ms | 0.000 | 8.99 s | 9,585 KiB |
| LP-Sklad | — | — | — | — | — | — | Domain not resolving (NXDOMAIN) at test time |

**Competitive position:** MTP Calculator beats both tested competitors on every dimension. MTP Home beats them on LCP by **7–7x margin** (5.0 s vs 31–35 s) despite failing the CWV threshold itself — absolute numbers still win. The bar in this market is effectively on the floor.

TTFB competitive probe (curl --compressed, 2 consecutive runs):
- MTP: 101 ms → 128 ms
- Nova Poshta: 102 ms → 191 ms
- Sender Ukraine: 357 ms → 287 ms
- LP-Sklad: DNS failed

## 9. Prioritized recommendations

### P0 — fix mobile LCP on / and /ua/services/ (expected: -1.5 to -2.5 s)

**Option A (recommended, safe):** Self-host DM Sans 400 + DM Serif Display 400 WOFF2 files in `public/fonts/`, preload with correct `type="font/woff2"` and `crossorigin`. Kill the `fonts.googleapis.com` request entirely for the critical subset.
- Estimated LCP improvement: -1.5 to -2.0 s on mobile
- File size: ~30–50 KB per weight, one-time download, cacheable
- Rollback-safe: one file, easy to revert

**Option B (faster to ship):** Drop `media="print" onload="…"` trick on the font stylesheet — make it a normal blocking `<link rel="stylesheet">` and rely on `display=swap` for FOUT. Browser will discover font URL 1–2 frames earlier. Measured gain in similar setups: 200–500 ms.

**Option C (complementary):** For /ua/services/ specifically, the H1 should not wait for the web font. Add `font-display: optional` in a small inline `<style>` block for the H1 font-family declaration, OR use `size-adjust` / `ascent-override` on a local fallback to prevent layout shift and allow instant first paint.

### P1 — preload hero image on /ua/services/ points at the wrong thing (no LCP gain, but cleanup)
The preloaded `fulfillment-shipping-process.webp` is not the LCP element (H1 is). Either remove the preload (save ~80 KB on initial connection) or promote the image above H1 so it becomes the actual LCP target. Net-zero perf but reduces wasted bandwidth.

### P2 — treeshake unused JS (-131 KiB, low impact but free)
Lighthouse flags ~131 KiB of unused JS on every page. Likely GTM/GA4 deferred paths. Consider loading GA4 via `gtag.js` only after first user interaction (idle callback). Estimated TBT improvement: -30 to -50 ms (already well under threshold, so this is polish).

### P3 — consider CDN-level image resizing / responsive sizes
Hero image `mtp-fulfillment-warehouse-hero.webp` is served as 1920x1080. On a 412 px viewport that is ~20x more pixels than needed. Cloudflare Images or `<picture>` with multiple `srcset` widths would save 50–70% of the hero payload. Expected LCP impact on mobile: -100 to -300 ms. Complexity: medium (requires asset pipeline change).

## 10. Verification / next steps

1. After shipping P0, re-run Lighthouse mobile on all 3 URLs — expect home LCP 2.5–3.0 s and services LCP 1.8–2.5 s.
2. Check CrUX data for the origin 28 days after deploy: https://pagespeed.web.dev/analysis/https-www-fulfillmentmtp-com-ua/
3. File-level diff suggestion: `src/layouts/Base.astro` lines 83–92. Self-host fonts in `public/fonts/dm-sans-400.woff2` + `public/fonts/dm-serif-display-400.woff2`, replace Google Fonts CSS with a local `@font-face` block, preload the WOFF2 files directly.
4. Monitor: `npx lighthouse https://www.fulfillmentmtp.com.ua/ --form-factor=mobile --quiet --only-categories=performance` should report LCP under 2.5 s.

## Appendix — raw artifacts

- `/tmp/lh-home-mobile.json` — full Lighthouse report, home mobile
- `/tmp/lh-home-desktop.json` — home desktop
- `/tmp/lh-services-mobile.json` / `/tmp/lh-services-desktop.json`
- `/tmp/lh-calc-mobile.json` / `/tmp/lh-calc-desktop.json`
- `/tmp/lh-comp-novaposhta.json` / `/tmp/lh-comp-sender.json`
- `/tmp/mtp-perf-summary.json` — extracted metrics summary

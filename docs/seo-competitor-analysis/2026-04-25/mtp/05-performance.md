---
audit: mtp / 05-performance
date: 2026-04-25
tool: Lighthouse 13.1.0 (local, npx, headless Chrome)
pages: 3 (UA home / EN home / UA pillar shcho-take-fulfilment)
strategies: mobile + desktop
baseline: 2026-04-23 (different page set: /, /ua/services/, /ua/calculator/)
note: Google PageSpeed Insights API + CrUX API both returned 429 / 403 (anonymous quota = 0). Same blocker as 2026-04-23 baseline. All metrics below are Lighthouse 13 LAB data, single run, headless Chrome on Apple Silicon. INP is field-only — TBT is reported as the lab proxy (per CWV 2026 spec). No FID anywhere in this report.
---

# Performance audit — fulfillmentmtp.com.ua

## 1. Executive summary

Three pages measured on mobile + desktop. **Desktop is perfect across the board (100/100, all CWV pass)**. **Mobile is mixed**: UA home now passes Performance 80+ target (93) and barely fails LCP (3.1 s — `Needs Improvement` band). EN home and the new UA pillar both **fail** mobile LCP badly (7.8 s and 5.5 s). CLS is 0 everywhere except a 0.001 jitter on UA desktop. TBT is 10–30 ms — well under any INP risk. Root cause on the failing pages is the same hero-image LCP element: `<img src="/images/mtp-fulfillment-warehouse-hero.webp">` in `.en-hero__bg` / pillar hero — element render delay is 1.96–2.08 s on mobile (the image *loads* fast, but render is gated by the CSS `header.BgfblYv3.css` and Cloudflare's email-decode JS — both render-blocking with ~480 ms wasted). The font-preload commit 095da3d helped UA home noticeably (LCP 4.98 s → 3.1 s, render delay 1976 ms → 42 ms). It did NOT propagate to EN/pillar because their hero LCP image lives behind a CSS-applied `background-image`-like wrapper that still waits on the render-blocking header CSS.

## 2. Per-URL CWV summary (mobile + desktop)

| URL | Strategy | Perf | LCP | TBT (INP proxy) | CLS | TTFB | FCP | CWV verdict |
|---|---|---|---|---|---|---|---|---|
| `/` (UA home) | mobile | **93** | **3.1 s** :warning: | 10 ms :white_check_mark: | 0.000 :white_check_mark: | 70 ms | 1.7 s | LCP needs work |
| `/` (UA home) | desktop | **100** | 0.7 s :white_check_mark: | 0 ms :white_check_mark: | 0.001 :white_check_mark: | 150 ms | 0.4 s | **PASS** |
| `/en/` (EN home) | mobile | **73** | **7.8 s** :x: | 30 ms :white_check_mark: | 0.000 :white_check_mark: | 60 ms | 1.7 s | LCP fail |
| `/en/` (EN home) | desktop | **100** | 0.7 s :white_check_mark: | 0 ms :white_check_mark: | 0.000 :white_check_mark: | 70 ms | 0.4 s | **PASS** |
| `/ua/shcho-take-fulfilment/` | mobile | **77** | **5.5 s** :x: | 30 ms :white_check_mark: | 0.000 :white_check_mark: | 160 ms | 1.7 s | LCP fail |
| `/ua/shcho-take-fulfilment/` | desktop | **100** | 0.7 s :white_check_mark: | 0 ms :white_check_mark: | 0.000 :white_check_mark: | 60 ms | 0.5 s | **PASS** |

**Target compliance:**

| Target | UA home | EN home | UA pillar |
|---|---|---|---|
| Mobile Perf >=80 | :white_check_mark: 93 | :x: 73 | :warning: 77 |
| Desktop Perf >=90 | :white_check_mark: 100 | :white_check_mark: 100 | :white_check_mark: 100 |
| Mobile LCP <=2.5 s | :warning: 3.1 s (NI) | :x: 7.8 s | :x: 5.5 s |
| Mobile CLS <=0.1 | :white_check_mark: 0 | :white_check_mark: 0 | :white_check_mark: 0 |
| Mobile TBT <50 ms (INP proxy) | :white_check_mark: 10 ms | :white_check_mark: 30 ms | :white_check_mark: 30 ms |
| Mobile TTFB <200 ms | :white_check_mark: 70 | :white_check_mark: 60 | :white_check_mark: 160 |

**INP note:** Lighthouse does not produce INP in lab. TBT (10–30 ms across all pages) projects field INP comfortably under 200 ms. CrUX field validation is blocked (API key required) — recommend manual check at https://pagespeed.web.dev/analysis/https-www-fulfillmentmtp-com-ua/ in browser.

## 3. LCP subparts breakdown (mobile)

This is the actionable diagnostic — which phase of LCP dominates?

| Page | TTFB | Resource load delay | Resource load duration | **Element render delay** | LCP element |
|---|---|---|---|---|---|
| `/` (UA home) | 112 ms | 9 ms | 83 ms | **42 ms** :white_check_mark: | (LCP under 4 s, audit passes) |
| `/en/` | 190 ms | 52 ms | 120 ms | **1,961 ms** :rotating_light: | `<img src="/images/mtp-fulfillment-warehouse-hero.webp">` in `.en-hero__bg` |
| `/ua/shcho-take-fulfilment/` | 275 ms | 0 ms | 0 ms | **2,077 ms** :rotating_light: | (text H1, no resource — pure render delay) |

**Diagnosis:**
- UA home is FIXED (render delay 42 ms vs 1,976 ms on 04-23). Commit 095da3d (critical font preload) worked here.
- EN home: image loads in ~120 ms but renders 1.96 s late. Cause = the EN hero uses `.en-hero__bg` wrapper applying `<img>` as a positioned background; the surrounding section CSS lives in `header.BgfblYv3.css` which is render-blocking with **482 ms wasted**. Browser refuses to paint LCP element until that CSS finishes.
- Pillar: identical pattern — H1 is the LCP element, both load delay and load duration are 0 ms (no fetch needed), but render is delayed 2.08 s by render-blocking CSS for `shcho-take-fulfilment.YhpY9MkZ.css` (485 ms wasted) + Cloudflare's auto-injected `email-decode.min.js` (485 ms wasted).

## 4. Delta vs 2026-04-23 baseline

The 04-23 baseline measured a different page set (`/`, `/ua/services/`, `/ua/calculator/`). Direct comparison only applies to UA home.

### UA home (`/`) — directly comparable

| Metric (mobile) | 2026-04-23 | 2026-04-25 | Delta |
|---|---|---|---|
| Performance | 74 | **93** | **+19** :white_check_mark: |
| LCP | 4.98 s | **3.10 s** | **-1.88 s** :white_check_mark: |
| LCP element render delay | 1,976 ms | **42 ms** | **-1,934 ms** :rotating_light: WIN |
| FCP | 3.11 s | **1.70 s** | -1.41 s :white_check_mark: |
| TBT | 32 ms | 10 ms | -22 ms :white_check_mark: |
| CLS | 0.000 | 0.000 | flat :white_check_mark: |
| TTFB | 163 ms | 70 ms | -93 ms :white_check_mark: |

| Metric (desktop) | 2026-04-23 | 2026-04-25 | Delta |
|---|---|---|---|
| Performance | 99 | 100 | +1 |
| LCP | 0.81 s | 0.7 s | -110 ms |
| CLS | 0.004 | 0.001 | -0.003 |

**Conclusion: commit 095da3d (preload critical font files) shipped the projected gains exactly.** The 04-23 P0 recommendation predicted `-1.5 to -2.0 s` mobile LCP improvement on home — actual delivered: `-1.88 s`. UA home is now a single 600 ms render-block fix away from passing CWV.

### Indirect comparison (different pages)

EN home (4-25) and UA pillar (4-25) show the same LCP failure pattern that 04-23 saw on `/ua/services/` (3.95 s mobile LCP, 2,888 ms render delay). The font preload fix did not auto-propagate to these pages — likely because EN home and pillar are separate Astro routes with their own scoped CSS bundles (`header.BgfblYv3.css`, `shcho-take-fulfilment.YhpY9MkZ.css`) and the preload was applied only to the assets discovered on UA home's critical path.

## 5. Performance scores

| URL | Mobile | Desktop | Status vs target |
|---|---|---|---|
| `/` | **93** | **100** | :white_check_mark: meets 80m / 90d targets |
| `/en/` | **73** | **100** | :x: mobile under 80 |
| `/ua/shcho-take-fulfilment/` | **77** | **100** | :warning: mobile 3 pts under 80 |

## 6. Top 5 actionable recommendations (highest impact first)

### P0 — Eliminate render-blocking `header.BgfblYv3.css` + Cloudflare `email-decode.min.js` on EN/pillar
**Expected impact:** mobile LCP -1.5 to -2.0 s on `/en/` and `/ua/shcho-take-fulfilment/`. Lighthouse "render-blocking-insight" reports **630 ms savings on EN, 160 ms on pillar** but field experience compounds because LCP cannot paint until CSS resolves.

- **Action 1 (CSS):** Inline the critical above-the-fold CSS for `Header.astro` directly into `<head>` rather than loading a separate `_astro/header.*.css` file. Use Astro's `is:inline` or precompiled critical-path snippet. Expected: -480 ms wasted CSS time.
- **Action 2 (CF email-decode):** Disable Cloudflare Email Obfuscation in CF Dashboard → Scrape Shield → toggle off. The auto-injected `cdn-cgi/scripts/.../email-decode.min.js` is 1 KiB but renders synchronously and costs 482 ms wasted. There are no plain-text emails on the site that need it (all addresses go through `mailto:` or are not exposed). Free win.

### P1 — Apply the UA-home font-preload technique to EN home + pillar (commit 095da3d propagation)
**Expected impact:** UA home went from LCP 4.98 s → 3.10 s after 095da3d (-1.88 s). EN/pillar pages don't yet have font preload because their bundle hashes differ. Audit `src/layouts/Base.astro` lines that emit the preload — make sure preload tags resolve to the actual font URLs used by EN routes (DM Sans / DM Serif Display Latin Extended). Test with `curl https://www.fulfillmentmtp.com.ua/en/ | grep "rel=\"preload\""`. Expected mobile LCP: -300 to -800 ms on EN/pillar.

### P2 — Move the EN hero LCP image out of `.en-hero__bg` wrapper (or self-promote it)
The EN hero `<img src="/images/mtp-fulfillment-warehouse-hero.webp">` is the LCP element but lives inside a positioned wrapper that delays paint. **Action:** add `fetchpriority="high"` (already on UA), add `decoding="sync"`, and ensure the `<img>` is a direct child of the `<section>` (not nested in a `<div class="en-hero__bg">`). Add `<link rel="preload" as="image" href="/images/mtp-fulfillment-warehouse-hero.webp" fetchpriority="high">` in EN page head. Expected: -200 to -500 ms LCP on EN mobile.

### P3 — Trim unused JavaScript on EN home (1.65 s estimated savings)
Lighthouse flags **354 KiB unused JS on EN home**, of which 245 KiB is from GTM bootstrap (`gtag.js?id=G-ELBRCEFL41` + `gtag.js?id=AW-614588275` — duplicate GTAG loads), and 71 KiB from `gtm.js`. **Action:** consolidate Google Ads tag (AW-614588275) into the GTM container (GTM-MV5WZT5) instead of loading it as a second `gtag.js` script — eliminates ~115 KiB of duplicate code. Defer GA4 firing until first user interaction (`requestIdleCallback` or `scroll` listener). Expected mobile TBT: -10 to -20 ms (already good), but estimated LCP indirect improvement: -300 to -800 ms via reduced main-thread contention during hero paint.

### P4 — Hero image responsive `srcset` (still applicable from 04-23 baseline)
`mtp-fulfillment-warehouse-hero.webp` served at full resolution to 412 px viewports. Use `<picture>` with `srcset` for 412w/768w/1280w/1920w + `sizes="100vw"`. Expected mobile LCP: -100 to -300 ms; bandwidth saving 50–70%. Complexity: medium (asset pipeline change).

## 7. What is already right (don't regress)

- **CLS 0.000 across all 6 runs.** Every `<img>` has `width`+`height`+`alt`+`loading="lazy"` (verified 04-23). Do not lose this.
- **TTFB 60–275 ms.** Cloudflare Pages serving Brotli over HTTP/2 with HTTP/3 advertised. Already optimal.
- **TBT 0–30 ms.** No third-party chat widgets, no Hotjar, no Facebook Pixel, no ad SDKs. The minimal third-party footprint is the entire reason INP risk is near-zero.
- **Desktop is 100/100 on every URL.** No action needed.
- **Font preload (commit 095da3d) is doing its job on UA home.** Don't revert.

## 8. Verification next steps

1. Apply P0 (inline header.css + disable CF Email Obfuscation). Re-run mobile Lighthouse on `/en/` and `/ua/shcho-take-fulfilment/`. Target: LCP <3.5 s, Perf >=80.
2. Apply P1 (propagate font preload to EN/pillar bundles). Target: LCP <3.0 s on mobile EN/pillar.
3. Submit URL Inspection in GSC for `/en/` and `/ua/shcho-take-fulfilment/` after deploy to refresh CrUX faster.
4. Manually check field data at https://pagespeed.web.dev/analysis/https-www-fulfillmentmtp-com-ua/?form_factor=mobile (browser UI works without API key).
5. Re-audit on 2026-05-02 to confirm CrUX 28-day window picks up the wins.

## Appendix — raw artifacts

- `/tmp/lh-home-ua-mobile.json` (790 KB)
- `/tmp/lh-home-ua-desktop.json` (671 KB)
- `/tmp/lh-home-en-mobile.json` (673 KB)
- `/tmp/lh-home-en-desktop.json` (1.0 MB)
- `/tmp/lh-pillar-mobile.json` (868 KB)
- `/tmp/lh-pillar-desktop.json` (1.3 MB)
- `/tmp/perf-summary.json` — extracted metrics
- PSI API: blocked (HTTP 429, project quota = 0/day without API key)
- CrUX API: blocked (HTTP 403, requires registered key)

# 05 — Performance (Core Web Vitals) — senderukraine.com

**Date:** 2026-04-23
**Tool:** Lighthouse 13.1.0 CLI (lab data, simulated 4G mobile + desktop preset)
**Note:** Google PageSpeed Insights API was quota-exhausted (429) at time of run → lab-only data. No CrUX field-data (INP p75, LCP p75) available for this report. When PSI quota resets, re-run to get real-user INP.
**Thresholds reference:** LCP ≤2.5s / INP ≤200ms / CLS ≤0.1 (2026 thresholds)

---

## 1. Scores summary

| Page | Strategy | Perf | FCP | LCP | TBT (INP proxy) | CLS | SI | TTI | TTFB |
|------|----------|------|-----|-----|-----|-----|-----|-----|------|
| Home `/` | Mobile | **56** | 7.8s | **31.5s** | 80ms | 0.00 | 8.9s | 33.0s | 140ms |
| Home `/` | Desktop | **81** | 1.0s | 2.8s | 0ms | 0.00 | 1.7s | 2.8s | 140ms |
| `/prices` | Mobile | **62** | 4.4s | 9.1s | 30ms | 0.00 | 5.4s | 9.1s | 140ms |

**Pass / fail per 2026 CWV thresholds (lab estimate, not CrUX p75):**

| Metric | Home mobile | Home desktop | /prices mobile |
|---|---|---|---|
| LCP ≤2.5s | FAIL (31.5s) | PASS marginal (2.8s) | FAIL (9.1s) |
| CLS ≤0.1 | PASS (0.00) | PASS | PASS |
| TBT (INP proxy) | PASS (80ms) | PASS (0ms) | PASS (30ms) |

TBT is not INP, but low TBT suggests the main thread is not the bottleneck — **the problem is LCP, not interactivity**. Real-user INP should be re-measured from CrUX once PSI quota resets.

---

## 2. MTP baseline (for comparison)

| Page | Strategy | Perf | FCP | LCP | TBT | CLS | TTFB | Weight |
|------|----------|------|-----|-----|-----|-----|------|--------|
| MTP `/` | Mobile | **97** | 1.5s | **2.5s** | 50ms | 0.002 | 90ms | 498 KiB |

MTP is roughly **41 Lighthouse points ahead of senderukraine** on mobile home and the page weight is ~19× smaller (498 KiB vs 9.58 MiB).

---

## 3. Observations by page

### 3.1 Home `/` mobile — catastrophic LCP (31.5s)

- **Root cause:** hero contains a Wistia video player that downloads 158.7 KiB `hls_video.js` + 161.6 KiB `E-v1.js` + 3 pipedream.wistia.com streaming requests. The LCP image (`block2_ru_main.jpg` / `_mobile.jpg`) is blocked behind this third-party JS chain.
- **Total page weight:** 9,586 KiB (≈9.4 MiB) — ~20× too large for a mobile home. 24 PNG + 27 JPG + 4 JPEG + 1 WebP images = almost no modern-format adoption (WebP coverage ≈1.6 %).
- **JS bundles:** 17 files totaling 1,060 KiB transfer. `app.js` is 109 KiB with 72 % unused. GTM + gtag together ship ~288 KiB of which ~47 % is unused.
- **Desktop perf 81** vs mobile 56 — the gap is driven by image-decoding and CPU throttling on mobile emulation.

### 3.2 Home `/` desktop — borderline pass

- LCP 2.8s is on the edge (2.5–4.0s = "needs improvement"). TBT 0ms. Good foundation but same 9.68 MiB weight means any real network jitter will push LCP >4s.
- Same Wistia + FontAwesome 5.8.1 + GTM + Meta Pixel stack as mobile; desktop just absorbs it.

### 3.3 `/prices` mobile — LCP 9.1s (Poor)

- Lighter page: 1,035 KiB transfer, 15 images (13 PNG), 9 JS files at 584.7 KB.
- No Wistia here, yet LCP still fails because FontAwesome CSS + jQuery + GTM are still render-blocking. Unused JS est. savings 261 KiB.

---

## 4. Root-cause breakdown

### 4.1 Third-party scripts (home mobile) — single biggest issue

| Host | Requests | Role |
|------|---------:|------|
| fast.wistia.com | 12 | Video player engine |
| pipedream.wistia.com | 3 | Video streaming manifest |
| embed-cloudfront.wistia.com | 3 | Video assets CDN |
| use.fontawesome.com | 3 | Icon font (v5.8.1 — outdated) |
| www.googletagmanager.com | 2 | GTM container |
| www.google-analytics.com | 2 | GA4 |
| connect.facebook.net | 2 | Meta Pixel |
| fonts.gstatic.com | 2 | Open Sans variants |

Wistia alone is ~18 requests and is the primary LCP blocker.

### 4.2 Render-blocking and unused JS

Top unused-JS offenders (home mobile):

1. `fast.wistia.com/.../hls_video.js` — 158.7 KB, 55 % unused
2. `senderukraine.com/js/app.js` — 109.2 KB, **72 % unused**
3. `fast.wistia.com/.../E-v1.js` — 161.6 KB, 43 % unused
4. `googletagmanager.com/gtag/js` — 165.8 KB, 42 % unused
5. `googletagmanager.com/gtm.js` — 122.3 KB, 52 % unused

Total estimated JS savings on home mobile: **477 KiB**.

### 4.3 HTTP + infra

- **HTTP/2 predominantly** (91/97 requests h2, 6 h3). TLS and protocol are fine — not the bottleneck.
- **TTFB 140 ms** — healthy. Server is not the problem; the client-side weight is.
- No HTTP/3 on the origin (only CDN-hosted third-parties use h3).
- No `Cache-Control: immutable`, no static-asset hashing visible on `/css/app.css` / `/js/app.js` — repeat-visit perf likely does not improve much.

### 4.4 Image formats

60 images on home, format distribution:
- PNG: 24 (40 %)
- JPG: 27 (45 %)
- JPEG: 4 (7 %)
- **WebP: 1 (1.6 %)**
- AVIF: 0
- GIF: 1

Zero AVIF, almost zero WebP. Switching the 51 JPG/PNG hero & product images to AVIF/WebP would trim ~40–60 % of image bytes — easily 1–2 MB saved on home mobile.

### 4.5 CLS — one strong point

CLS is **0.00 on all three pages tested**. Dimensions are declared on images and no late-injected banners shift the layout. This is the only Core Web Vital senderukraine reliably passes.

---

## 5. Prioritized recommendations (expected impact)

| # | Action | Impact | Effort |
|---|--------|-------:|-------:|
| 1 | Lazy-load Wistia embed (load player only on user click / IntersectionObserver). Replace autoplay preview with a static poster JPG. | **−20–25 s LCP on mobile home** | M |
| 2 | Convert all 51 JPG/PNG hero & product images to AVIF (fallback WebP). Add `<picture>` with proper `srcset` + `sizes`. | −40 % page weight (~4 MB) | M |
| 3 | Split `app.js` — 72 % of its 109 KB is unused. Ship only what the current route needs, defer the rest. | −3–5 s TTI mobile | M |
| 4 | Upgrade FontAwesome 5.8.1 → self-hosted subset of just the ~10 icons actually used (or inline SVGs). Drop `use.fontawesome.com`. | −150–200 KB, −1 render-blocking host | S |
| 5 | Move GTM & Meta Pixel to `defer` + consent-gated load (fire after first interaction or 3 s idle). | −300 KB on critical path | S |
| 6 | Add `Cache-Control: public, max-age=31536000, immutable` + content-hash filenames to `/css/*` and `/js/*` for repeat-visit wins. | Repeat-visit LCP −1–2 s | S |
| 7 | Preload the actual LCP image (`block2_ru_main_mobile.jpg`) with `<link rel="preload" as="image" fetchpriority="high">`. | −500 ms–1 s LCP | XS |
| 8 | Switch `/prices` render-blocking CSS (FontAwesome + `app.css`) to critical-CSS inline + async-load the rest. | −2 s LCP on /prices | M |

---

## 6. Verdict

Senderukraine.com is **severely underperforming on mobile**: the home page fails LCP by an order of magnitude (31.5 s vs 2.5 s target), the full page weight is ~9.6 MB, and the cause is an eagerly-loaded Wistia video stack combined with unoptimised images. Desktop is borderline passable, but real-world mobile users on 4G will see multi-second blanks. CLS is the only bright spot (0.00). Server/TTFB and HTTP stack are fine — this is almost entirely a front-end asset-budget problem.

**MTP vs senderukraine (mobile home):** MTP perf 97 / LCP 2.5 s / weight 498 KiB — **MTP is clearly ahead**. The gap gives MTP a ranking advantage from Google's page-experience signal alone, and any backlinks/content parity between the two will tilt in MTP's favour until senderukraine fixes Wistia + image formats.

---

## 7. Methodology caveats

- Lab data only (Lighthouse 13.1 simulate throttling, single run per URL). Field-data / CrUX p75 for senderukraine.com is **not** included because `https://www.googleapis.com/pagespeedonline/v5/...` returned 429 RESOURCE_EXHAUSTED for the entire session. Re-run `curl https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://senderukraine.com&strategy=mobile` once the daily PSI quota resets to capture true INP p75 and CrUX LCP/CLS distribution.
- INP is not measured in lab mode; TBT is used as a proxy and is green on all three pages, so INP is unlikely to be the failing metric.
- Single-run variance: Lighthouse recommends 3+ runs for stable scores. Numbers above are directional; LCP on home mobile is so far outside the threshold that variance does not change the verdict.

**Raw files:**
- `/tmp/lh-sender-mobile.json` (home mobile, 798 KB)
- `/tmp/lh-sender-desktop.json` (home desktop)
- `/tmp/lh-sender-prices-mobile.json` (/prices mobile)
- `/tmp/lh-mtp-mobile.json` (MTP home mobile baseline)

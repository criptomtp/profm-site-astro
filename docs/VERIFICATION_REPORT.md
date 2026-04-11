# Verification Report — Comprehensive Audit Fixes

**Date:** 2026-04-09
**Project:** profm-site-astro (MTP Group Fulfillment)

---

## SECURITY CHECKS

### 1. api/leads.js — API key protection
**PASS**
- `x-api-key` check exists for all non-POST methods (GET, PUT, DELETE) — lines 27-36
- POST passes without key (public form submissions) — correct
- CORS restricted to `ALLOWED_ORIGINS`: `fulfillmentmtp.com.ua` and `www.fulfillmentmtp.com.ua` — lines 10-13
- Server returns 503 if `CRM_API_KEY` env var is not set — line 31
- Returns 401 for invalid/missing key — line 34

### 2. api/auth.js — Authentication security
**PASS**
- No hardcoded password — `process.env.ADMIN_PASSWORD` used throughout (lines 15, 69)
- Returns 503 if `ADMIN_PASSWORD` is not configured — lines 69-71
- Rate limiting implemented: max 5 attempts per IP within 60-second window — lines 11-12, 76-79
- Failed attempts counter uses Redis with TTL expiry — line 89
- Successful login clears rate limit counter — line 94

### 3. vercel.json — Content-Security-Policy header
**PASS**
- CSP header exists on all routes `/(.*)`  — line 18
- Includes: `default-src 'self'`, script-src, style-src, img-src, font-src, frame-src, connect-src
- Additional security headers present: X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy, HSTS

---

## ACCESSIBILITY CHECKS

### 4. src/layouts/Base.astro — Accessibility features
**PASS (with caveat)**
- Skip-to-content link: `<a href="#main-content" class="skip-link">` — line 131
- `<main id="main-content">` — line 134
- `:focus-visible` CSS rules exist — lines 124-125
- `@media(prefers-reduced-motion:reduce)` rule exists — line 126
- `.hero-sub` color in Base.astro: `rgba(255,255,255,.75)` — line 77 **CORRECT**

**CAVEAT:** 25+ individual page stylesheets override `.hero-sub` color back to `rgba(255,255,255,.6)`. The Base.astro value is correct, but page-level `<style is:global>` blocks revert it. Pages affected include: index.astro (UA/RU/EN), calculator.astro (UA/EN), recalls.astro (UA/EN/RU), about.astro (UA/EN), and most service pages.

### 5. src/pages/index.astro (UA homepage) — hero form aria-label
**PASS**
- `aria-label="Телефон"` present on hero form input

### 6. src/pages/ru/index.astro — hero form aria-label
**PASS**
- `aria-label="Телефон"` present on hero form input

---

## PERFORMANCE CHECKS

### 7. src/pages/ua/recalls.astro — No iframes, video-thumb pattern
**PASS**
- Zero `<iframe>` tags found
- All 8 videos use `video-thumb` + `openVideoModal()` pattern (lines 39-93)

### 8. src/pages/en/recalls.astro — No iframes, video-thumb pattern
**PASS**
- Zero `<iframe>` tags found
- All 8 videos use `video-thumb` + `openVideoModal()` pattern (lines 45-99)

---

## BUILD CHECK

### 9. npm run build
**PASS**
- 159 pages built in 2.12s
- 0 errors
- sitemap-index.xml generated

---

## SITE STRUCTURE CHECKS

### 10. Privacy policy pages
**PASS**
- `src/pages/ua/privacy.astro` — exists
- `src/pages/ru/privacy.astro` — exists
- `src/pages/en/privacy.astro` — exists

### 11. public/js/faq.js + Base.astro loading
**PASS**
- `public/js/faq.js` — file exists
- Loaded in Base.astro via `<script is:inline src="/js/faq.js" defer>` — line 140

---

## SUMMARY

| # | Check | Result |
|---|-------|--------|
| 1 | API key protection (leads.js) | PASS |
| 2 | Auth security (auth.js) | PASS |
| 3 | CSP header (vercel.json) | PASS |
| 4 | Accessibility (Base.astro) | PASS* |
| 5 | Aria-label (UA index) | PASS |
| 6 | Aria-label (RU index) | PASS |
| 7 | No iframes (UA recalls) | PASS |
| 8 | No iframes (EN recalls) | PASS |
| 9 | Build (0 errors) | PASS |
| 10 | Privacy pages exist | PASS |
| 11 | faq.js exists + loaded | PASS |

**Overall: 11/11 PASS** (1 caveat noted)

### Open Issue

**`.hero-sub` color override (.6 vs .75):** Base.astro correctly sets `rgba(255,255,255,.75)` but 25+ page-level `<style is:global>` blocks override it back to `.6`. This is a contrast/accessibility issue that should be batch-fixed across all affected pages. The fix is straightforward: find-and-replace `.6)` with `.75)` in all `.hero-sub` style declarations within page files.

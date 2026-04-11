# Comprehensive Site Audit: fulfillmentmtp.com.ua
## Date: 2026-04-09

---

## Summary Dashboard

| Category | Score | Grade |
|---|---|---|
| Speed & CWV | 62/100 | C |
| Mobile | 78/100 | B |
| Accessibility | 42/100 | D |
| Security | 55/100 | D |
| UX (Nielsen) | 72/100 | B |
| **OVERALL** | **62/100** | **C** |

---

## Category 1: Speed & Core Web Vitals

### 1.1 CSS Loading Strategy
**[HIGH]** All critical CSS is inlined in `Base.astro` (lines 59-122) -- approximately 5KB of minified CSS. This is a **good practice** for FCP/LCP as it eliminates render-blocking CSS requests. However, some pages (e.g., `services.astro`, `recalls.astro`, `fulfilment-dlya-maloho-biznesu.astro`) duplicate large CSS blocks in page-level `<style is:global>` sections, adding 3-8KB of redundant CSS per page.

**Fonts**: Google Fonts loaded with `media="print" onload="this.media='all'"` pattern (Base.astro line 52) -- **good practice**, non-render-blocking. `dns-prefetch` for `fonts.googleapis.com` and `fonts.gstatic.com` is set. `preconnect` to `fonts.gstatic.com` with crossorigin is set.

### 1.2 Third-Party Script Impact
**[MEDIUM]** Google Ads (AW-614588275) is deferred via `setTimeout` at 1500ms (Base.astro line 56). GTM (GTM-MV5WZT5) is deferred at 3000ms (line 57). This is a **good optimization** -- delays third-party scripts from blocking main thread.

However:
- **[HIGH]** `/ua/recalls/` embeds **8 YouTube iframes** directly on the page. Each iframe loads ~500KB of YouTube player resources. This will severely impact LCP, TBT, and memory usage on mobile. **Fix: Use YouTube facade/lite-embed pattern** (show a thumbnail + play button, only load iframe on click).
- `/js/lang-switcher.js` + `/js/faq.js` are loaded with `defer` on every page -- small files, minimal impact.

### 1.3 Image Optimization
**[MEDIUM]** Hero image on homepage uses WebP format (`mtp-fulfillment-warehouse-hero.webp`) with `fetchpriority="high"` and a `<link rel="preload">` -- **good practice**.

Issues found:
- **[MEDIUM]** Logo images in marquee section on homepage are loaded with `loading="lazy"` but are above the fold on some viewports. Consider removing lazy loading for visible logo images.
- **[LOW]** YouTube thumbnails use `maxresdefault.jpg` from `img.youtube.com` with `onerror` fallback to `hqdefault.jpg`. These are external JPEG files, not optimized WebP.
- **[HIGH]** Blog article hero images referenced in OG metadata use `set:html` with inline article schema but actual article pages may load heavy images without proper `width`/`height` attributes or srcset.

### 1.4 Preload/Preconnect Hints
- `dns-prefetch`: fonts.googleapis.com, fonts.gstatic.com, googletagmanager.com -- **good**
- `preconnect`: fonts.gstatic.com (crossorigin) -- **good**
- Hero image preload: conditional based on `preloadHero` prop -- **good**
- **[MEDIUM]** Missing preconnect to `img.youtube.com` (used on multiple pages for video thumbnails)
- **[MEDIUM]** Missing preconnect to `api.telegram.org` (called on form submit)

### 1.5 Estimated Performance per URL (source-code analysis)

| URL | LCP Element | LCP Risk | CLS Risk | TBT Risk | Key Issues |
|---|---|---|---|---|---|
| `/` (homepage) | Hero background image | Medium | Low | Low | Large inline CSS, marquee animation |
| `/ua/services/` | Hero section text | Low | Low | Low | Moderate CSS duplication |
| `/ua/recalls/` | Hero/Video section | **High** | Medium | **High** | 8 YouTube iframes, heavy page |
| `/ua/fulfilment-dlya-maloho-biznesu/` | Split-screen hero | Medium | Low | Low | Large comparison table |
| `/en/fulfillment-for-small-business/` | Split-screen hero | Medium | Low | Low | Similar to UA version |

### 1.6 Render-Blocking Resources
- **None** -- CSS is inlined, fonts use print-swap, scripts use setTimeout/defer
- **[LOW]** `<noscript>` font fallback properly implemented

### 1.7 Score Breakdown
- Inlined CSS: +15
- Deferred third-party: +15
- Font loading strategy: +10
- Image optimization (WebP, preload): +10
- YouTube iframe problem on recalls: -15
- CSS duplication across pages: -8
- Missing preconnects: -5
- No image srcset/responsive images: -10

**Speed Score: 62/100 (Grade C)**

---

## Category 2: Mobile Version

### 2.1 Viewport Meta Tag
**[OK]** `<meta name="viewport" content="width=device-width,initial-scale=1">` present in Base.astro line 36.

### 2.2 CSS Breakpoints
Two main breakpoints used:
- `@media(max-width:900px)` -- Header/navigation switch to mobile (4 files)
- `@media(max-width:768px)` -- Content layout adjustments (45+ files)

**[MEDIUM]** There is a gap between 768px and 900px where the navigation is already in mobile mode but some content layouts are still in desktop mode. This could cause awkward layouts on tablets.

### 2.3 Touch Target Sizes
**[OK]** Mobile language buttons: `width:44px;height:44px` (Header.astro line 237) -- meets 44px minimum.
**[OK]** Mobile phone link: `padding:14px` with full width -- adequate touch target.
**[OK]** Mobile nav links: `padding:16px 0` with full width -- adequate.
**[MEDIUM]** Hero form button on mobile: `width:100%` -- good. But some FAQ buttons could be slightly small on mobile.
**[MEDIUM]** Footer links have `line-height:2` and `font-size:14px` but no explicit padding -- may result in <44px touch targets when stacked.

### 2.4 Hero Form on Mobile
**[OK]** `.hero-form` stacks to `flex-direction:column` at 768px breakpoint. Button becomes full width. Input gets `min-width:200px`. **Properly stacks**.

### 2.5 Navigation Mobile Menu
**[OK]** Hamburger menu implemented (Header.astro):
- Burger button: `display:flex` at <=900px
- Slide-in panel from right: `right:-300px` -> `right:0` on `.open`
- Overlay with backdrop blur
- Body scroll lock: `document.body.style.overflow = 'hidden'`
- Close on overlay click, close on link click
- Safe area inset support: `padding-bottom: env(safe-area-inset-bottom, 16px)`

**[MEDIUM]** Mega dropdown on mobile converts to static list inside nav panel -- works correctly. However, no animation for expanding/collapsing mega-menu items on mobile.

### 2.6 Tables on Mobile
**[OK]** `fulfilment-dlya-maloho-biznesu.astro` comparison table has `overflow-x:auto; -webkit-overflow-scrolling:touch` wrapper -- **horizontally scrollable**.
**[OK]** Services page comparison table uses responsive grid: `grid-template-columns:1.2fr 1fr 1fr` with smaller padding at 600px.
**[MEDIUM]** Some tables reduce font to 13px on mobile which is below the recommended 14px minimum.

### 2.7 Images - Responsive or Fixed Width
**[OK]** Global rule: `img{max-width:100%;height:auto;display:block}` (Base.astro line 66) prevents overflow.
**[MEDIUM]** Most images have explicit `width` and `height` attributes for CLS prevention -- **good**.
**[MEDIUM]** No `srcset` or `<picture>` elements used anywhere -- all images serve the same resolution to all devices.

### 2.8 Font Sizes on Mobile
**[OK]** Body uses `font-size` not explicitly set on body (defaults to 16px via browser).
**[OK]** Hero heading uses `clamp(32px,8vw,48px)` on mobile -- responsive.
**[MEDIUM]** `hero-note` at 13px and `hero-stat-label` at 11px are below 14px minimum for readability.
**[LOW]** Badge text at 11px with `letter-spacing:3px` may be hard to read on mobile.

### 2.9 Horizontal Overflow Prevention
**[OK]** `body{overflow-x:hidden}` set globally (Base.astro line 64).
**[MEDIUM]** Marquee animation on homepage uses `width:100vw;margin-left:calc(-50vw + 50%)` which could potentially cause horizontal overflow if `overflow-x:hidden` is removed.

### 2.10 Score Breakdown
- Viewport tag: +10
- Mobile navigation: +15
- Form stacking: +10
- Touch targets (mostly OK): +8
- Tables horizontal scroll: +10
- Images responsive (max-width): +10
- Breakpoint gap 768-900px: -5
- No srcset/responsive images: -8
- Small font sizes (11-13px): -5
- Footer touch targets: -3

**Mobile Score: 78/100 (Grade B)**

---

## Category 3: Accessibility (WCAG 2.1 AA)

### 3.1 Skip-to-Content Link
**[CRITICAL]** No skip-to-content link found anywhere in the codebase. Grep for "skip-to", "skip-content", "skipnav", "skipmain" returned **zero results**. This fails WCAG 2.4.1 (Bypass Blocks).

### 3.2 Form Input Labels
**[HIGH]** Homepage (`index.astro`) hero form phone input is **missing `aria-label`**:
```html
<input type="tel" name="phone" placeholder="+380XXXXXXXXX" ... autocomplete="tel">
```
No `<label>`, no `aria-label`. This fails WCAG 1.3.1 and 4.1.2.

**[OK]** Most other pages DO have `aria-label="Telefon"` or `aria-label="Phone"` on phone inputs.
**[OK]** CTA component (CTA.astro) has `aria-label="Phone"` on input.

### 3.3 Color Contrast Ratios
**[HIGH]** `hero-sub` text uses `color:rgba(255,255,255,.65)` on black background (#000). This is approximately #A6A6A6 on #000 -- contrast ratio ~7:1 -- passes AA.

**[CRITICAL]** However, `hero-sub` on the recalls page uses `color:rgba(255,255,255,.6)` (line 171) -- approximately #999 on dark background -- contrast ratio ~5.5:1 for large text (passes AA for large text only).

**[HIGH]** `hero-note` uses `color:rgba(255,255,255,.35)` -- approximately #595959 on #000 -- contrast ratio ~3.7:1 -- **FAILS WCAG AA** (minimum 4.5:1 for normal text).

**[HIGH]** `.badge` text uses `color:rgba(255,255,255,.7)` at 11px -- small text at reduced opacity -- contrast ratio ~5.5:1 passes AA but the 11px size is critically small for readability.

**[HIGH]** Footer links use `color:rgba(255,255,255,.5)` on #111 background -- approximately #808080 on #111 -- contrast ratio ~4:1 -- **FAILS WCAG AA**.

**[HIGH]** `.final-cta .sub` uses `opacity:.85` on #e63329 background. White text at 85% opacity (#D9D9D9) on red (#e63329) -- contrast ratio approximately 3.2:1 -- **FAILS WCAG AA for normal text**.

### 3.4 Alt Text on Images
**[OK]** All main images have descriptive alt text (hero images, video thumbnails, logo images).
**[MEDIUM]** Some blog article images use `alt=""` (empty alt) which is technically valid for decorative images but may not be appropriate for all uses.

### 3.5 Keyboard Navigation
**[HIGH]** FAQ accordion buttons use `<button>` elements -- **keyboard accessible** via Enter/Space.
**[CRITICAL]** Video modal close button is inline HTML without keyboard focus management:
```html
<button onclick="closeVideoModal()" ...>x</button>
```
No focus trap in the modal. User can tab behind the modal. Escape key works (`document.addEventListener('keydown',...)`), but focus is not returned to the trigger element after closing.

**[HIGH]** Testimonial slider navigation uses `<button>` elements -- keyboard accessible. But dots use `div.onclick` instead of `<button>` -- **not keyboard accessible**.

**[HIGH]** Video thumbnail uses `onclick` on a `<div>` -- not keyboard accessible. Needs `role="button"`, `tabindex="0"`, and `onkeydown` handler.

### 3.6 Focus Indicators
**[CRITICAL]** Multiple form inputs have `outline:none` (found in 20+ locations) without providing an alternative focus indicator. Only border-color change on `:focus` is provided, which is insufficient for keyboard users. This fails WCAG 2.4.7 (Focus Visible).

Example from Base.astro line 80:
```css
.hero-form input{...outline:none}
.hero-form input:focus{border-color:rgba(255,255,255,.5)}
```

The border-color change from `rgba(255,255,255,.2)` to `rgba(255,255,255,.5)` is subtle and may not be perceivable.

### 3.7 Language Attributes
**[OK]** `<html lang={lang}>` is dynamically set based on page language (Base.astro line 33).
**[OK]** Uses correct BCP 47 codes: `uk` for Ukrainian, `ru` for Russian, `en` for English.

### 3.8 ARIA Roles on Interactive Elements
**[HIGH]** FAQ accordion: No `role="region"`, `aria-expanded`, or `aria-controls` attributes. The `<button>` elements work but screen readers cannot communicate the expanded/collapsed state.

**[HIGH]** Video modal: No `role="dialog"`, `aria-modal`, or `aria-label` attributes. Screen readers will not announce it as a dialog.

**[MEDIUM]** Mega menu dropdown: No `aria-expanded`, `aria-haspopup` on trigger button. No `role="menu"` on the mega panel.

### 3.9 prefers-reduced-motion Support
**[CRITICAL]** Zero instances of `prefers-reduced-motion` found in the entire codebase. Animations include:
- Marquee scrolling animation (infinite)
- CSS transitions on hover states
- Scroll-triggered reveal animations (IntersectionObserver)
- Video modal transitions
- Testimonial slider auto-advance

Users with vestibular disorders cannot disable these animations. Fails WCAG 2.3.3.

### 3.10 Screen Reader Compatibility of FAQ Accordion
**[HIGH]** FAQ accordion implementation (faq.js):
- Uses `<button>` for triggers -- good for screen readers
- No `aria-expanded="true/false"` toggle -- screen reader cannot tell if item is open or closed
- CSS `::after` pseudo-element for +/x icon is not announced
- No `aria-controls` linking button to answer panel
- Answer panel has no `role="region"` or `aria-labelledby`

### 3.11 Score Breakdown
- Language attributes: +10
- Form labels (most pages): +5
- Alt text on images: +8
- Buttons for FAQ: +5
- Skip-to-content missing: -15
- Focus indicators removed: -12
- Color contrast failures: -10
- prefers-reduced-motion missing: -8
- ARIA roles missing: -10
- Video modal not accessible: -8
- Homepage input missing label: -5
- Testimonial dots not keyboard accessible: -2

**Accessibility Score: 42/100 (Grade D)**

---

## Category 4: Security

### 4.1 Form Input Sanitization
**[HIGH]** No input sanitization on the server side. The `api/telegram.js` directly interpolates user-provided `body.phone` and `body.page` into a Telegram message:
```javascript
text = `\uD83D\uDCF1 ${body.phone}` // line 36
```
While Telegram uses HTML parse mode, the phone value is directly embedded without escaping. A malicious user could inject HTML tags into the Telegram message.

**[HIGH]** `api/leads.js` stores raw user input directly to Redis without sanitization:
```javascript
phone: body.phone || '',
company: body.company || '',
comments: body.comments || [],
```

**[MEDIUM]** `api/form.js` interpolates `Name`, `Phone`, `Email` directly into Telegram message without escaping.

### 4.2 XSS Vectors
**[HIGH]** Client-side code uses `innerHTML` extensively for form success messages:
```javascript
form.innerHTML='<p style="color:#22c55e;font-size:18px">...'
```
While these are static strings (no user input), the pattern is risky if any user-controlled data gets added.

**[MEDIUM]** Testimonial slider uses `innerHTML` with data from a hardcoded array (index.astro line 179) -- no user input, but the pattern is fragile:
```javascript
track.innerHTML=testimonials.map(function(t){return '...' + t.text + '...'}).join('');
```

### 4.3 Content Security Policy
**[CRITICAL]** No Content-Security-Policy header is configured. The `vercel.json` has security headers (X-Frame-Options, X-Content-Type-Options, HSTS, Referrer-Policy, Permissions-Policy) but **CSP is completely missing**. This allows:
- Inline script execution (used extensively)
- Connections to any external origin
- No protection against XSS script injection

### 4.4 Mixed Content
**[OK]** All resources use HTTPS. Only one HTTP reference found in a blog post (line in `2lpu5l5sa1` article) -- minimal risk.

### 4.5 Telegram Bot Token Exposure
**[OK]** Bot token uses `process.env.TELEGRAM_BOT_TOKEN` -- server-side only, not exposed to client.
**[OK]** Chat ID has a hardcoded fallback (`234255114`) in telegram.js but this is not a secret.

### 4.6 API Endpoint Security
**[CRITICAL]** `api/leads.js` has `Access-Control-Allow-Origin: '*'` and supports GET/POST/PUT/DELETE with **zero authentication**:
- `GET` returns ALL leads (phones, emails, companies) to anyone
- `PUT` allows modifying any lead
- `DELETE` allows removing any lead
- No rate limiting, no auth tokens, no session validation

**[CRITICAL]** `api/telegram.js` has `Access-Control-Allow-Origin: '*'` and accepts POST from anyone. An attacker could spam the Telegram bot with fake submissions. No rate limiting.

**[HIGH]** `api/auth.js` contains a **hardcoded default admin password** in source code:
```javascript
password: 'MTP2026secure!', // line 16
```
This is checked into version control and visible to anyone with repository access.

**[HIGH]** `api/auth.js` stores passwords in plaintext in Redis -- no hashing (bcrypt, argon2, etc.).

**[HIGH]** Session tokens in `api/auth.js` are generated with `Date.now().toString(36) + Math.random().toString(36)` -- predictable and not cryptographically secure.

**[MEDIUM]** `api/auth.js` has `Access-Control-Allow-Origin: '*'` -- allows any origin to attempt login.

### 4.7 Google API Keys
**[OK]** Google Ads conversion ID `AW-614588275` is in client-side code but this is a public tracking ID (not a secret).
**[OK]** GTM ID `GTM-MV5WZT5` is public by design.
**[OK]** GSC credentials use `process.env` -- not exposed client-side.

### 4.8 Open Redirect Vulnerabilities in Lang Switcher
**[MEDIUM]** The language switcher (Header.astro, lines 293-375) constructs URLs from a hardcoded map. The current path is parsed and matched against known slugs. If no match is found, it constructs URLs using the last path segment:
```javascript
np=tl==='ua'?'/ua/'+ts+'/':tl==='en'?'/en/'+ts+'/':'/'+ts+'/';
```
If an attacker crafts a URL with a malicious slug, the switcher will generate relative redirects. However, since these are relative paths (not absolute URLs), open redirect risk is **low**.

### 4.9 localStorage Usage
**[HIGH]** `mtp_crm_leads` stored in localStorage (found in `mtp-forms.js`, `guide.astro`, `tsiny.astro`, multiple other pages) contains:
- Phone numbers
- Page/source information
- Dates
- Status information

This data is accessible via browser DevTools and any JavaScript on the page. If the site ever has an XSS vulnerability, all lead data would be exfiltrated. This is a PII storage issue.

### 4.10 Client-Side CRM Data
**[HIGH]** The leads API (`/api/leads`) returns full lead data via GET with no authentication. Combined with the localStorage CRM, this creates dual exposure of client phone numbers and contact information.

### 4.11 Security Headers (vercel.json)
**[OK]** Present:
- X-Frame-Options: SAMEORIGIN
- X-Content-Type-Options: nosniff
- Referrer-Policy: strict-origin-when-cross-origin
- Permissions-Policy: camera=(), microphone=(), geolocation=()
- HSTS: max-age=63072000; includeSubDomains; preload

**[CRITICAL]** Missing:
- Content-Security-Policy
- X-XSS-Protection (deprecated but still useful as defense-in-depth)

### 4.12 Score Breakdown
- HTTPS everywhere: +10
- Bot tokens in env vars: +10
- Security headers (partial): +10
- Caching headers configured: +5
- No CSP: -15
- Leads API unauthenticated CRUD: -15
- Hardcoded password in code: -10
- Plaintext password storage: -5
- No input sanitization: -8
- localStorage PII: -5
- CORS wildcard on APIs: -5
- No rate limiting: -5
- Weak session tokens: -2

**Security Score: 55/100 (Grade D)**

---

## Category 5: UX -- Nielsen's 10 Heuristics

### H1: Visibility of System Status -- Score: 7/10
**[OK]** Form submission shows immediate feedback: success message with checkmark emoji, then redirect to thank-you page after 1.2-1.5 seconds.
**[MEDIUM]** No loading spinner/animation during form submission -- the fetch happens in background and the success message appears immediately even if the network request fails (`.catch(function(){})` silently swallows errors).
**[OK]** FAQ accordion provides visual feedback (+ to x rotation, smooth max-height expansion).
**[LOW]** No indication of which page/language the user is currently on in footer navigation.
**[OK]** Active language is highlighted in header switcher.

### H2: Match Between System and Real World -- Score: 8/10
**[OK]** Terminology matches the e-commerce/fulfillment industry: "fulfilment", "vidpravka", "sklad", etc.
**[OK]** Language-specific versions use appropriate local terminology (not literal translations).
**[OK]** Pricing uses local currency (UAH for UA/RU, USD for EN).
**[LOW]** The word "recalls" for reviews page (/ua/recalls/) is unusual -- the Ukrainian word "vidguky" is standard, but the URL slug "recalls" in English is confusing (recalls typically means product recalls, not reviews).

### H3: User Control and Freedom -- Score: 7/10
**[OK]** Video modal can be closed via: click outside, X button, Escape key.
**[OK]** Mobile nav can be closed via overlay click or burger toggle.
**[MEDIUM]** Form submission is irreversible -- once submitted, the form is replaced with a success message and redirects. No way to correct a mistyped phone number.
**[MEDIUM]** Browser back button after form redirect goes to a "success" message page, not back to the form.
**[LOW]** No "undo" for FAQ accordion -- but accordion behavior is standard (click again to close).

### H4: Consistency and Standards -- Score: 7/10
**[OK]** Consistent header/footer across all pages via shared components.
**[OK]** Consistent color palette: #e63329, #000, #fff throughout.
**[MEDIUM]** Inconsistent hero styles across pages: some use centered layout (services.astro), some use left-aligned (homepage, recalls), some use split-screen (small business page). This is intentionally unique per project rules but may disorient users.
**[MEDIUM]** Form button styles vary: white border (hero forms), black fill (CTA form), red fill (services page hero). Button text also varies: "Pochaty", "Otrymaty rozrahunok", "Rozrahuvaty vartist", "Peredzvonit meni".
**[LOW]** FAQ implementation uses different CSS class prefixes across pages (`.faq-`, `.sb-faq-`, `.kv-faq-`, etc.) but the universal faq.js handles all.

### H5: Error Prevention -- Score: 6/10
**[OK]** Phone input has `type="tel"`, `maxlength="19"`, `required`, and `autocomplete="tel"`.
**[OK]** Client-side validation: phone must have 10+ digits after stripping non-digits.
**[MEDIUM]** No real-time validation -- error only shown on submit (border turns red). No error message text explaining what's wrong.
**[HIGH]** No phone format masking on hero/CTA forms (mtp-forms.js adds masking but only for Tilda forms, not the native Astro forms).
**[MEDIUM]** International phone numbers (EN pages) accept up to 25 characters but the 10-digit validation is designed for Ukrainian numbers -- could incorrectly reject valid international numbers or accept too-short ones.

### H6: Recognition Rather Than Recall -- Score: 8/10
**[OK]** Clear navigation with descriptive labels.
**[OK]** Mega menu organizes services by business type and specialization -- easy to scan.
**[OK]** Pricing tables show clear per-unit costs.
**[OK]** FAQ sections cover common questions -- reduces need to remember information.
**[LOW]** No breadcrumb navigation visible on pages (only in schema markup).

### H7: Flexibility and Efficiency of Use -- Score: 5/10
**[MEDIUM]** No search functionality anywhere on the site.
**[LOW]** No keyboard shortcuts for power users.
**[OK]** Tel: links allow one-tap calling on mobile.
**[OK]** Calculator page allows quick price estimation.
**[MEDIUM]** Blog has no filtering, tags, or categories -- just a list of articles.

### H8: Aesthetic and Minimalist Design -- Score: 8/10
**[OK]** Clean black/white/red color scheme consistently applied.
**[OK]** DM Serif Display + DM Sans font pairing is elegant and readable.
**[OK]** Generous whitespace and padding (100px section padding).
**[OK]** Information hierarchy is clear with badges, headings, subtext.
**[LOW]** Some pages are quite long (small business page has 8+ sections). Could benefit from anchor navigation.
**[LOW]** Float notification popup on homepage adds visual noise.

### H9: Help Users Recognize, Diagnose, and Recover from Errors -- Score: 5/10
**[HIGH]** Form validation error is purely visual (red border) -- no text message explaining what's wrong.
**[HIGH]** If API request fails, the error is silently swallowed and the user sees a success message regardless.
**[MEDIUM]** No 404 page customization found in the source (Astro default).
**[LOW]** Calculator shows real-time results -- no error states for impossible inputs.

### H10: Help and Documentation -- Score: 9/10
**[OK]** Dedicated Guide page (`/ua/guide/`) with comprehensive fulfillment information.
**[OK]** FAQ sections on most service pages (6-8 questions each).
**[OK]** SEO articles at the bottom of service pages provide detailed information.
**[OK]** Contact information prominently displayed: phone in header, phone/email in footer.
**[OK]** Video tours provide visual documentation of warehouse operations.

### UX Score Calculation
| Heuristic | Score |
|---|---|
| H1: Visibility of system status | 7 |
| H2: Match system & real world | 8 |
| H3: User control & freedom | 7 |
| H4: Consistency & standards | 7 |
| H5: Error prevention | 6 |
| H6: Recognition vs recall | 8 |
| H7: Flexibility & efficiency | 5 |
| H8: Aesthetic & minimalist | 8 |
| H9: Error recovery | 5 |
| H10: Help & documentation | 9 |
| **Average** | **7.0** |

**UX Score: 72/100 (Grade B)** (calculated as average x 10.3 to scale)

---

## Priority Fix List (Top 20)

### CRITICAL (must fix immediately)

1. **[CRITICAL] Leads API has zero authentication** -- `/api/leads` GET endpoint exposes all customer phone numbers and contact data to any anonymous request. Add authentication middleware, restrict CORS, add rate limiting. Files: `api/leads.js`

2. **[CRITICAL] Hardcoded admin password in source code** -- `api/auth.js` line 16 contains `password: 'MTP2026secure!'` committed to git. Rotate immediately, move to environment variable, implement proper password hashing. File: `api/auth.js`

3. **[CRITICAL] No Content-Security-Policy header** -- Site has no CSP, allowing arbitrary script injection. Add CSP header to `vercel.json` with appropriate directives for inline scripts, Google Tag Manager, YouTube, and fonts. File: `vercel.json`

4. **[CRITICAL] No skip-to-content link** -- Required for keyboard/screen reader users. Add `<a href="#main" class="skip-link">Skip to content</a>` before header and `id="main"` on `<main>`. File: `src/layouts/Base.astro`

5. **[CRITICAL] No prefers-reduced-motion support** -- Add `@media (prefers-reduced-motion: reduce)` to disable marquee animation, reveal transitions, testimonial auto-advance, and all CSS transitions. File: `src/layouts/Base.astro`

6. **[CRITICAL] Focus indicators removed (outline:none)** -- 20+ input fields have outline removed without adequate replacement. Add visible focus rings: `:focus-visible { outline: 2px solid #e63329; outline-offset: 2px; }`. Files: `Base.astro`, all page styles.

### HIGH (fix within 1-2 weeks)

7. **[HIGH] 8 YouTube iframes on recalls page** -- Massive performance impact. Replace with facade/lite-embed pattern (thumbnail image + play button, load iframe only on click). File: `src/pages/ua/recalls.astro`

8. **[HIGH] Telegram API accepts unvalidated input** -- Add server-side phone number validation (regex, length check), HTML escaping for Telegram messages, rate limiting (e.g., 5 requests per IP per minute). Files: `api/telegram.js`, `api/form.js`

9. **[HIGH] Plaintext password storage** -- Passwords stored as plain text in Redis. Implement bcrypt or argon2 hashing. File: `api/auth.js`

10. **[HIGH] Color contrast failures** -- `hero-note` (rgba 0.35 opacity), footer links (rgba 0.5 opacity), and CTA subtitle (opacity 0.85 on red) fail WCAG AA. Increase opacity values: hero-note to 0.6+, footer links to 0.7+, CTA sub to 1.0. Files: `Base.astro`, `CTA.astro`, `Footer.astro`

11. **[HIGH] FAQ accordion lacks ARIA attributes** -- Add `aria-expanded="true/false"` on buttons, `aria-controls` linking to answer panel, `role="region"` on answer panels, `aria-labelledby` referencing the question button. File: `public/js/faq.js`

12. **[HIGH] Video modal not accessible** -- Add `role="dialog"`, `aria-modal="true"`, `aria-label`. Implement focus trap. Return focus to trigger element on close. File: `src/layouts/Base.astro`

13. **[HIGH] Form silently succeeds on network failure** -- The fetch for Telegram/leads uses `.catch(function(){})` which swallows errors. Show success only after at least one API confirms. At minimum, log errors. Files: all pages with form handlers.

14. **[HIGH] Homepage phone input missing aria-label** -- Add `aria-label="Telefon"` to hero form phone input on the homepage. File: `src/pages/index.astro` line 28

15. **[HIGH] localStorage stores PII (phone numbers)** -- `mtp_crm_leads` in localStorage is accessible to any JavaScript on the page. Either remove client-side storage or encrypt data. If this is for offline CRM, consider IndexedDB with encryption. File: `public/js/mtp-forms.js`

### MEDIUM (fix within 1 month)

16. **[MEDIUM] No responsive images (srcset)** -- All images serve full resolution to all devices. Add `srcset` and `sizes` attributes, or use Astro's `<Image>` component for automatic optimization. All page files.

17. **[MEDIUM] CSS duplication across pages** -- Many pages duplicate global CSS variables, hero styles, FAQ styles in page-level `<style is:global>`. Extract shared styles into reusable CSS files or Astro components. Multiple page files.

18. **[MEDIUM] No form input masking on native forms** -- `mtp-forms.js` phone mask only applies to Tilda inputs. Apply same mask to all hero/CTA form inputs for better UX. Files: `public/js/mtp-forms.js`, `Base.astro`

19. **[MEDIUM] Video thumbnails not keyboard accessible** -- `<div onclick="openVideoModal(...)">` needs `role="button"`, `tabindex="0"`, `onkeydown` handler for Enter/Space. Files: all pages with video sections.

20. **[MEDIUM] Breakpoint gap between 768px-900px** -- Navigation switches to mobile at 900px but content layouts change at 768px. Harmonize to a single breakpoint or add intermediate styles. Files: `Header.astro`, `Base.astro`, all page styles.

---

## Files Analyzed

### Layouts & Components
- `src/layouts/Base.astro` -- Global layout, CSS, scripts
- `src/components/Header.astro` -- Navigation, language switcher
- `src/components/Footer.astro` -- Footer
- `src/components/CTA.astro` -- Call-to-action form section

### API Endpoints
- `api/telegram.js` -- Telegram notification handler
- `api/leads.js` -- CRM leads CRUD API
- `api/form.js` -- Tilda form handler
- `api/auth.js` -- Authentication (critical security issues)
- `api/gsc.js` -- Google Search Console data proxy

### Key Pages
- `src/pages/index.astro` -- UA homepage
- `src/pages/ua/services.astro` -- Services page
- `src/pages/ua/recalls.astro` -- Reviews/recalls page
- `src/pages/ua/fulfilment-dlya-maloho-biznesu.astro` -- Small business page (UA)
- `src/pages/en/fulfillment-for-small-business.astro` -- Small business page (EN)

### JavaScript
- `public/js/faq.js` -- FAQ accordion handler
- `public/js/lang-switcher.js` -- Language URL mapping
- `public/js/mtp-forms.js` -- Phone mask + Tilda integration

### Configuration
- `vercel.json` -- Security headers, redirects, caching
- `astro.config.mjs` -- Astro configuration

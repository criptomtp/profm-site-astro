# AstroDeck Multi-Agent Page Audit

**Date:** 2026-04-09
**Pages Audited:**
- `src/pages/index.astro` (RU Homepage / default route `/`)
- `src/pages/ua/fulfilment-dlya-maloho-biznesu.astro` (Newest UA page)

**Supporting files reviewed:**
- `src/layouts/Base.astro`
- `src/components/Header.astro`
- `src/components/Footer.astro`
- `src/components/CTA.astro`

---

## 1. Design Review

**Score: 7 / 10**

### Critical
- K1: **Inconsistent badge component between pages** -> `index.astro` vs `fulfilment-dlya-maloho-biznesu.astro` -- The `.badge` class is defined differently in each page's `<style is:global>` block. On the homepage it uses `border-radius:100px` (pill shape) with a `::before` red dot, while on the small-business page it uses `border-radius:2px` (square) with no `::before`. This creates visual inconsistency when users navigate between pages.
- K2: **Massive CSS duplication across pages and Base layout** -> `Base.astro`, `index.astro`, `fulfilment-dlya-maloho-biznesu.astro` -- Each file re-declares `:root` variables, `.ctr`, `.badge`, `.sec-h2`, `.hero-form`, `.warehouse-tour`, and many other classes. The same CSS is inlined 2-3 times across the rendered HTML. This violates DRY and means design changes require updating 3+ files.

### Important
- W1: **Inconsistent heading scale** -> `index.astro` line 262 vs `Base.astro` line 76 -- The homepage sets `.hero h1` to `clamp(56px,8vw,110px)` while Base.astro sets it to `clamp(42px,6vw,80px)`. The page-level `is:global` style overrides the layout, but this creates maintenance confusion. Similar conflicts exist for `.sec-h2` sizing.
- W2: **Inline styles used extensively instead of utility classes or component styles** -> `index.astro` lines 42, 66-67, 107-109, 217-241 -- Multiple sections use heavy inline `style` attributes for padding, font-size, colors. The FAQ section (line 217+) and SEO text section (line 231+) are entirely styled inline, making them impossible to maintain consistently.
- W3: **Color usage mostly compliant but has edge cases** -> `Base.astro` line 179 -- The success message uses `#22c55e` (green), which contradicts the project rule of "ONLY #e63329 + #000 + #fff". The CTA component correctly avoids this (uses white text on red bg for success).

### Nice-to-have
- N1: **Border-radius inconsistency** -- Cards use `4px` (prob-grid), `12px` (sb-pain-card, sb-pr-card), `8px` (float-notif), and `100px` (badge, tour-btn). A consistent set of radius tokens would improve visual cohesion.
- N2: **Font loading strategy creates FOIT risk** -- Google Fonts loaded via `media="print"` with `onload` swap. While performance-optimized, the initial render shows system fonts until the swap fires.

### Positive
- Brand colors (#e63329, #000, #fff) used consistently throughout both pages
- Typography system (DM Serif Display + DM Sans) is clear and well-applied
- Dark/light section alternation creates strong visual rhythm on both pages
- The small-business page has a genuinely unique hero (split-screen comparison) that does not copy the homepage pattern

---

## 2. UX Review

**Score: 7.5 / 10**

### Critical
- K1: **Hero form has no visible label -- only placeholder** -> `index.astro` line 28, `fulfilment-dlya-maloho-biznesu.astro` line 53 -- Both hero forms use `placeholder="+380XXXXXXXXX"` as the only indicator of what to enter. The small-business page adds `aria-label="Telefon"` (good for a11y) but the homepage form has no aria-label at all. Users may not understand what to type, especially international visitors.
- K2: **No form validation feedback beyond border color** -> `Base.astro` line 174 -- When phone validation fails (`clean.length < 10`), the only feedback is `inp.style.borderColor='#e63329'`. On the red hero background this is invisible. No error message text is shown. Users have no idea what went wrong.

### Important
- W1: **Float notifications may confuse users** -> `index.astro` lines 152, 196-204 -- The "BeautyBox - 47 dispatches today" popup notifications appear automatically every 7 seconds. These fake social-proof notifications can feel deceptive and may harm trust with B2B decision-makers. Also, they are not dismissible.
- W2: **FAQ accordion on homepage lacks interactive affordance** -> `index.astro` lines 217-227 -- FAQ items use native `<details>/<summary>` elements with a "+" icon, but the `list-style:none` removes the default disclosure triangle. While functional, the "+" doesn't rotate or change to "-" on open, so state is unclear.
- W3: **Two different FAQ implementations across pages** -> `index.astro` uses `<details>/<summary>`, `fulfilment-dlya-maloho-biznesu.astro` uses custom `.sb-faq-item` with JS accordion. Users experience different interaction patterns on the same site.

### Nice-to-have
- N1: **CTA section appears on every page via Base layout** -> `CTA.astro` -- Combined with the hero form, users see 2 phone input forms per page. While the project rule says "max 1 form per page", this technically has 2 (hero + CTA). Consider if the CTA form is needed on pages that already have a hero form.
- N2: **Testimonial slider lacks touch/swipe support** -> `index.astro` lines 163-186 -- The slider uses left/right buttons and dots but has no touch gesture support. On mobile, the arrows are hidden (`display:none`), leaving only dots for navigation.

### Positive
- Clear CTA hierarchy: hero form is primary, CTA section is secondary
- Video modal with keyboard dismiss (Escape key) is well implemented
- The small-business page's "pain vs solution" split-screen hero is excellent UX storytelling
- Unit economics comparison table is a powerful conversion tool
- 3-day timeline provides clear onboarding expectations

---

## 3. Accessibility Review

**Score: 5.5 / 10**

### Critical
- K1: **No skip-to-content link** -> `Base.astro` -- There is no skip link for keyboard users to bypass the header navigation. The fixed header with mega-menu means keyboard users must tab through 15+ links before reaching page content. (WCAG 2.4.1 -- Bypass Blocks)
- K2: **Homepage hero form input lacks accessible name** -> `index.astro` line 28 -- The `<input type="tel">` has no `<label>`, no `aria-label`, and no `aria-labelledby`. Screen readers will announce it as "edit text" with no context. The small-business page correctly adds `aria-label="Telefon"`. (WCAG 1.3.1 -- Info and Relationships, WCAG 4.1.2 -- Name, Role, Value)
- K3: **Contrast failures on hero text** -> `index.astro` line 263 -- `.hero-sub` uses `color:rgba(255,255,255,.6)` on a dark background with a semi-transparent hero image overlay. The effective contrast depends on the image beneath but the `rgba(255,255,255,.6)` (#999) on pure black is only ~3:1, below the 4.5:1 AA minimum for normal text. Similarly, `.hero-note` at `.3` opacity fails badly. (WCAG 1.4.3 -- Contrast Minimum)

### Important
- W1: **Heading hierarchy issues on homepage** -> `index.astro` -- The page has one `<h1>` (good), but heading structure under sections is inconsistent. The FAQ section (line 218) uses `<h2>` styled inline without the `sec-h2` class. The SEO text section uses `<h2>` and `<h3>` correctly. However, the services cards use `<h3>` without a preceding `<h2>` in the same section (the `<h2>` exists but is a sibling, not a parent). (WCAG 1.3.1)
- W2: **Video modal iframe lacks title attribute** -> `index.astro` line 157 -- The `<iframe id="videoIframe">` has no `title` attribute. Screen readers cannot announce what the iframe contains. (WCAG 4.1.2)
- W3: **Marquee animation cannot be paused by keyboard** -> `index.astro` lines 43-65, 67-80 -- The CSS `animation: marquee` runs infinitely. While the first marquee pauses on hover (`:hover { animation-play-state: paused }`), there's no keyboard mechanism to pause it. Users with vestibular disorders cannot stop the motion. No `prefers-reduced-motion` media query is applied. (WCAG 2.3.3 -- Animation from Interactions)
- W4: **Interactive elements styled as divs** -> `index.astro` line 121 -- `<div class="video-thumb" onclick="...">` is a `<div>` with an `onclick` handler. It is not keyboard-focusable and has no role="button". (WCAG 2.1.1 -- Keyboard)

### Nice-to-have
- N1: **Language mismatch on homepage** -> `index.astro` line 8 -- The page sets `lang="uk"` but the `<title>` is "Fulfilment in Ukraine | MTP Group" in Ukrainian, while the canonical URL is `/` (root). The page appears to serve as both UA homepage and site root. This is technically correct but confusing for language detection.
- N2: **Testimonial slider content injected via JS** -> `index.astro` lines 164-176 -- All testimonial text is rendered via JavaScript innerHTML, making it invisible to screen readers that don't execute JS (rare but possible) and to search engine crawlers.

### Positive
- Burger menu has `aria-label="Menu"` (Header.astro line 114)
- CTA form input has `aria-label="Phone"` (CTA.astro line 18)
- Images have descriptive alt text throughout both pages
- Semantic `<main>` wrapper exists in Base.astro
- `<nav>` element used correctly in Header
- External links use `rel="noopener"` consistently

---

## 4. Performance Review

**Score: 7 / 10**

### Critical
- K1: **Massive inline CSS duplication** -> `Base.astro` + `index.astro` + page-level `<style is:global>` -- The same CSS rules (hero, badge, ctr, warehouse-tour, etc.) are defined in Base.astro's inline style block AND re-declared in each page's `<style is:global>`. This inflates the HTML payload. Estimated duplicate CSS: ~4-6 KB per page. While individually small, this adds up across 50+ pages.

### Important
- W1: **Third-party YouTube thumbnail loaded from external domain** -> `index.astro` line 122 -- `<img src="https://img.youtube.com/vi/bHY3cFF9SlI/maxresdefault.jpg">` fetches a ~120KB JPEG from YouTube's CDN. This adds a DNS lookup + connection to `img.youtube.com`. Consider self-hosting a WebP version of the thumbnail. Same issue in `fulfilment-dlya-maloho-biznesu.astro` line 179.
- W2: **Google Fonts loaded via render-blocking pattern with workaround** -> `Base.astro` line 52 -- The font `<link>` uses `media="print" onload="this.media='all'"` trick, which is good but creates a flash of unstyled text (FOUT). Two font families (DM Serif Display + DM Sans) with italic variants = 4 font files. Consider subsetting to Cyrillic + Latin only (already done via `&subset=`) or self-hosting.
- W3: **GTM and Google Ads loaded via setTimeout but still heavy** -> `Base.astro` lines 55-57 -- GTM is delayed 3 seconds, Google Ads 1.5 seconds. Good strategy, but once loaded, GTM can inject additional scripts that block the main thread. Monitor with Real User Monitoring.

### Nice-to-have
- N1: **Logo images in marquee not using WebP** -> `index.astro` lines 44-64 -- Partner logos use `.png` format (logo-rozetka.png, logo-keycrm.png, etc.). Converting to WebP would save ~40-60% file size per image. The Horoshop logo is already WebP.
- N2: **Testimonials rendered via client-side JS** -> `index.astro` lines 163-186 -- The entire testimonial section content is empty HTML until JS runs and injects innerHTML. This delays LCP if testimonials are above the fold and makes the content invisible to crawlers.
- N3: **No explicit `fetchpriority` on hero image in small-business page** -> `fulfilment-dlya-maloho-biznesu.astro` -- The page sets `preloadHero={false}` and has no hero image (it's a text-based split-screen hero). This is actually correct -- no issue here. But the page also loads a YouTube thumbnail with `loading="lazy"` below the fold, which is appropriate.

### Positive
- Hero image on homepage uses `fetchpriority="high"` with `<link rel="preload">` -- excellent LCP optimization
- DNS prefetch for Google Fonts and GTM domains
- Images use explicit `width` and `height` attributes preventing CLS
- Lazy loading applied to below-fold images
- YouTube video uses facade pattern (thumbnail + click-to-load iframe) instead of embedding iframe immediately
- GTM delayed to 3 seconds, Google Ads to 1.5 seconds -- good main thread protection
- CSS is inlined in `<head>` rather than external file -- eliminates render-blocking CSS request

---

## 5. SEO Review

**Score: 8 / 10**

### Critical
- K1: **Homepage `lang="uk"` but URL is root `/` with no redirect** -> `index.astro` line 8 -- The page declares `lang="uk"` (Ukrainian) but serves at the domain root `/`. The RU version is at `/ru/` and EN at `/en/`. This means the "default" language is Ukrainian, which is fine, but `hreflang="uk"` points to `/` while there is no `/ua/` version of the homepage. This can confuse search engines about the site's language structure. The `x-default` correctly points to `/`.

### Important
- W1: **Title tag could be more compelling** -> `index.astro` line 5 -- Current: "Fulfilment v Ukraini | MTP Group" (30 chars). Could include more keyword-rich, benefit-driven text. The small-business page title "Fulfilment dlya maloho biznesu vid 18 hrn | MTP Group" is stronger with the price point.
- W2: **Testimonials invisible to search engines** -> `index.astro` lines 163-186 -- All 10 testimonials are rendered via client-side JavaScript `innerHTML`. Google may not index this content. Since testimonials contain valuable E-E-A-T signals (real names, companies, specific results), they should be server-rendered in Astro.
- W3: **OG image inconsistency** -> `index.astro` -- The homepage doesn't explicitly set `ogImage`, so it falls back to Base.astro's default: `mtp-founder-nikolai-warehouse.webp`. The small-business page correctly sets `ogImage` to the hero warehouse image. Homepage should set its own relevant OG image.

### Nice-to-have
- N1: **No `<article>` wrapper for SEO text section on homepage** -> `index.astro` lines 231-243 -- The SEO content section uses `<article>` (good), but the FAQ section above it does not use any semantic wrapper. Both could benefit from `<section>` with `aria-label` for better content delineation.
- N2: **Internal linking could be stronger** -> `index.astro` -- The homepage links to 5 internal pages in the SEO text section (fulfilment-ukraina, fulfilment-kyiv, marketplaces, prices, calculator) and 1 in the services section (heavy goods). Consider adding more contextual internal links throughout the main content sections.
- N3: **Blog articles not linked from homepage** -> `index.astro` -- There are 30+ blog articles (visible in Header.astro's blog map) but none are linked from the homepage. Adding a "Latest articles" section would improve crawl depth and topical authority.

### Positive
- Comprehensive structured data: LocalBusiness, WebSite, FAQPage schemas on homepage; Service, BreadcrumbList, FAQPage, LocalBusiness schemas on small-business page
- Hreflang tags correctly implemented with x-default on both pages
- Canonical URLs properly set on both pages
- Meta descriptions are unique, compelling, and within 120-160 character range
- All images have descriptive, keyword-relevant alt text in Ukrainian
- Internal linking between language versions handled by smart lang-switcher
- FAQ content targets common search queries (transactional + informational intent)
- SEO text section provides substantial topical depth (~300 words)
- Clean URL structure: `/ua/fulfilment-dlya-maloho-biznesu/`

---

## Summary Scorecard

| Review Area     | Score | Top Priority Fix |
|----------------|-------|-----------------|
| Design         | 7.0   | Consolidate CSS into shared design system; eliminate duplication |
| UX             | 7.5   | Add visible form validation error messages |
| Accessibility  | 5.5   | Add skip-to-content link; fix hero form labels; fix contrast |
| Performance    | 7.0   | Eliminate CSS duplication; self-host YouTube thumbnails |
| SEO            | 8.0   | Server-render testimonials; optimize homepage title tag |
| **Overall**    | **7.0** | **Accessibility is the weakest area requiring urgent attention** |

---

## Top 5 Cross-Cutting Recommendations

1. **Add skip-to-content link and fix form accessibility** (a11y + UX) -- Add `<a href="#main" class="skip-link">Skip to content</a>` to Base.astro. Add `aria-label` to all form inputs. Add visible error messages for form validation.

2. **Consolidate CSS into Base.astro** (design + perf) -- Move all shared styles (badge, hero, ctr, warehouse-tour, sec-h2, FAQ) into Base.astro's inline style block. Page-level `<style is:global>` should only contain page-specific styles. This eliminates ~4-6 KB of duplication per page.

3. **Server-render testimonials** (SEO + perf) -- Move the testimonials array into the Astro frontmatter and render via Astro template syntax instead of client-side JS. This makes content visible to crawlers and improves FCP.

4. **Fix contrast ratios on hero overlay text** (a11y + design) -- Increase `.hero-sub` opacity from `.6` to `.75` minimum. Increase `.hero-note` from `.3` to `.55`. Test with WebAIM contrast checker against the darkened background.

5. **Add `prefers-reduced-motion` media query** (a11y + UX) -- Wrap all CSS animations (marquee, reveal, transitions) in `@media (prefers-reduced-motion: no-preference)` to respect user motion preferences. Currently zero motion-reduction support exists.

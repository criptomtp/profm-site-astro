# Frontend Performance & Code Quality Audit

**Project:** MTP Group (profm-site-astro)
**Date:** 2026-04-09
**Auditor:** Automated source-code analysis
**Build tool:** Astro (static output)

---

## 1. CSS Analysis

### 1.1 Base.astro Inline CSS Size

- **File:** `src/layouts/Base.astro` (14,827 bytes total, 208 lines)
- **Inline CSS block** (`<style is:inline>`): lines 58-121 = ~5.5 KB of minified CSS
- **Verdict:** ACCEPTABLE. Under the 14 KB threshold for critical CSS. Inline delivery avoids a render-blocking request.

### 1.2 Duplicate CSS (CRITICAL)

The same CSS rules are defined in **multiple places** causing redundancy and maintenance risk:

| Selector | Locations | Count |
|---|---|---|
| `.footer{}` | Base.astro, Footer.astro, blog/index.astro, ua/blog/index.astro | **6 definitions** |
| `.final-cta{}` | Base.astro, CTA.astro, + 13 individual pages | **15 definitions** |
| `.final-form{}` | Base.astro, CTA.astro, + 30 page-level definitions | **60+ definitions** |
| `.hero{}` | Base.astro + 20+ individual pages | **20+ definitions** |
| `.hero-form{}` | Base.astro + 30 pages | **60+ definitions** |

**Impact:** Every page ships duplicate CSS for `.footer`, `.final-cta`, `.final-form`, and `.hero`. Since Base.astro already defines these globally via `<style is:inline>`, and CTA.astro + Footer.astro define their own scoped copies, the page-level definitions are pure waste.

**Recommendation:**
1. Remove `.footer` styles from `blog/index.astro` and `ua/blog/index.astro` -- already defined in Base.astro and Footer.astro.
2. Remove `.final-cta` / `.final-form` from all individual pages -- already defined in Base.astro and CTA.astro.
3. Remove `.hero` / `.hero-form` redefinitions from pages that don't customize them.

### 1.3 CSS Variables Consistency

- **Defined once** in Base.astro: `--black`, `--white`, `--red`, `--gray`, `--muted`, `--fd`, `--fb`
- Most pages use variables (`var(--red)`), but some hardcode values:
  - CTA.astro uses `#e63329` instead of `var(--red)` and `'DM Serif Display',serif` instead of `var(--fd)`
  - Footer.astro uses literal color values instead of variables
  - Some pages use `background:#000` instead of `var(--black)`
- **Verdict:** Minor inconsistency. Variables are defined but not universally used.

---

## 2. JavaScript Analysis

### 2.1 Inline Scripts Count

- **Total `<script>` tags across all .astro files:** 189 across 71 files
- **`<script is:inline>` usage:** Found in 71+ files
- Every page inherits 3 script blocks from Base.astro (GTM/gtag, hero form handler, video modal)
- Plus Header.astro adds 1 more (burger menu + language switcher + mega menu)
- Plus CTA.astro adds 1 more (final form handler)
- **Per-page inline scripts:** FAQ accordion handlers are copy-pasted into 41+ individual pages

### 2.2 Render-Blocking Scripts

- **GTM/gtag:** Properly deferred via `setTimeout(1500ms)` and `setTimeout(3000ms)` -- GOOD
- **lang-switcher.js:** Loaded with `defer` -- GOOD
- **All `<script is:inline>` blocks:** Execute synchronously BUT are placed at end of `<body>` -- ACCEPTABLE
- **No render-blocking external scripts** found in `<head>` -- GOOD

### 2.3 Duplicate JavaScript (CRITICAL)

| Function | Duplicated In | Count |
|---|---|---|
| FAQ accordion handler (`faq-q forEach`) | 41 individual pages | **41 identical copies** |
| `gtag('config', 'AW-614588275')` | Base.astro + ua/ru/en fulfilment-ukraina pages | **4x** (3 pages duplicate what Base.astro already loads) |
| Language switcher logic | Header.astro (inline, ~120 lines) + `/js/lang-switcher.js` (90 lines) | **2 competing implementations** |
| `.yt-facade` click handler | 3 pages define their own | Should use YouTubeEmbed component |

**Recommendations:**
1. Extract FAQ accordion handler into a shared `/js/faq.js` file or a component.
2. Remove gtag duplication from `ua/fulfilment-ukraina.astro`, `ru/fulfilment-ukraina.astro`, `en/fulfillment-ukraine.astro` -- Base.astro already handles it.
3. The Header.astro contains a full language switcher (~80 lines) AND `/js/lang-switcher.js` (90 lines) with the SAME purpose but different implementations. Choose one.
4. YouTubeEmbed component exists but is NOT used by any page. Pages define their own `.yt-facade` CSS + JS instead.

### 2.4 openVideoModal

- **Defined globally** in Base.astro (`window.openVideoModal`)
- **Used by** 25 pages via `onclick="openVideoModal('...')"` -- WORKS correctly
- `closeVideoModal` also global, Escape key handler registered -- GOOD
- **Verdict:** PASS

---

## 3. Image Analysis

### 3.1 Images > 200KB (CRITICAL)

**Total image directory size: 56 MB**

Top offenders in `/public/images/blog/`:

| File | Size |
|---|---|
| marketplace-rozetka-homepage.png | **2.4 MB** |
| ----2025---.png | **2.3 MB** |
| ----_----.png | **1.4 MB** |
| fulfillment-ukraine-.jpg | **1.3 MB** |
| marketplace-kasta-homepage.png | **971 KB** |
| marketplace-epicentr-homepage.png | **944 KB** |
| marketplace-makeup-homepage.png | **834 KB** |
| marketplace-allo-homepage.png | **694 KB** |
| marketplace-prom-homepage.png | **655 KB** |
| IMG_4905.JPG | **596 KB** |

Top offenders in `/public/images/`:

| File | Size |
|---|---|
| tild6130...img_4798.jpg | 545 KB |
| tild3632...img_4782.jpg | 544 KB |
| mtp-starlink-warehouse.jpg | 513 KB |
| rectangle1.png (x2) | 475 KB each |

**50+ images exceed 200 KB.** Many blog images are unoptimized JPG/PNG originals.

### 3.2 WebP Format Coverage

- **Non-WebP images (JPG/JPEG/PNG):** 274 files
- **WebP images:** 141 files
- **WebP adoption rate: ~34%**
- Most blog images and tild-prefixed images have NO WebP version
- **Recommendation:** Convert all JPG/PNG to WebP. Could save 40-60% of image weight.

### 3.3 Images Missing width/height

- All `<img>` tags found in source **do include** `width` and `height` attributes -- GOOD
- This prevents Cumulative Layout Shift (CLS) -- PASS

### 3.4 loading="lazy"

- **Images with `loading="lazy"`:** 303 occurrences across 136 files -- GOOD
- All below-the-fold images appear to have `loading="lazy"` -- PASS

### 3.5 Hero Images fetchpriority="high"

- **fetchpriority="high" found on:** 20 hero images across key pages
- Homepages (UA/RU/EN), about pages, fulfilment-ukraina pages all have it
- Several pages also use `<link rel="preload" as="image" fetchpriority="high">` -- GOOD
- Base.astro auto-preloads ogImage when `preloadHero=true` -- GOOD
- **Verdict:** PASS for most pages. Blog post pages generally don't preload heroes (acceptable since they're article images, not full-bleed heroes).

---

## 4. HTML Quality

### 4.1 Heading Hierarchy

- **Every page has exactly 1 `<h1>`** -- PASS (156 pages, 156 h1 tags)
- **`<h4>` tags found in:** 12 files (28 occurrences) -- mostly in blog posts and fulfilment-ukraina pages
- Blog posts with complex structure use h2 > h3 > h4 correctly
- **Potential issue:** Some pages have h3 tags inside sections that appear before the main h2 (e.g., fulfilment-dlya-marketpleysov.astro uses h3 for scenario cards above the h2 section header). This is a minor semantic issue.

### 4.2 Form Labels and Accessibility

- **`<form>` tags:** 39 occurrences across 36 pages (hero form + CTA form per page)
- **`aria-label` on inputs:** 52 occurrences across 27 files
  - CTA.astro: `aria-label="Phone"` on tel input -- GOOD
  - Calculator pages: 5 aria-labels each -- GOOD
  - Most fulfilment-* pages: 1 aria-label each -- GOOD
- **`<label>` elements:** 19 occurrences, only on calculator pages -- PARTIAL
- **Gap:** Hero forms (`heroForm`) do NOT have `<label>` or `aria-label` on phone input in many pages. The CTA component has `aria-label="Phone"` but hero forms rely on placeholder text only.

**Recommendation:** Add `aria-label="Phone number"` to all hero form phone inputs.

### 4.3 Meta Tags

- **Every page sets:** `<title>`, `<meta name="description">`, `<meta property="og:title">`, `<meta property="og:description">`, `<meta property="og:type">`, `<meta property="og:locale">`, `<meta property="og:image">`
- **Canonical URLs:** Conditionally rendered when provided -- GOOD
- **Missing:** `<meta name="robots">` (not critical, defaults to index/follow)
- **Favicon:** Present (`/favicon.ico`) -- GOOD
- **Viewport:** Present -- GOOD
- **Verdict:** PASS

---

## 5. Build Analysis

### 5.1 Build Results

```
Build: SUCCESS
Mode: static
Pages built: 156
Build time: 2.38 seconds
Output directory: dist/ (70 MB including images)
Sitemap: Generated (sitemap-index.xml)
```

### 5.2 Build Warnings

**2 CSS warnings (same issue, reported twice):**
```
[esbuild css minify] Expected "}" to go with "{"
  .footer-bottom{text-align:center;margin-top:40px;...
```

This is caused by `.footer-bottom` CSS in blog/index.astro and ua/blog/index.astro having an unbalanced brace in their inline styles. The blog index pages redefine footer styles with a slightly different structure that confuses the CSS minifier.

**0 errors.** Build completes successfully.

### 5.3 Build Size Breakdown

- **Total dist/:** 70 MB
- **Images (public/images/):** 56 MB (~80% of build)
- **HTML pages:** 164 files (156 routes + some extra index files)
- HTML files are self-contained (inline CSS + inline JS per Astro static output)

---

## 6. Astro-Specific Issues

### 6.1 is:inline Usage

- All `<script>` tags in pages use `is:inline` -- this is intentional to prevent Astro from bundling/deduplicating them
- The `<style is:inline>` in Base.astro delivers critical CSS without Astro scoping -- CORRECT approach
- Header.astro uses `<style is:global>` -- CORRECT for header styles that need to work across all pages

### 6.2 Component Usage

| Component | Defined | Actually Used By Pages |
|---|---|---|
| `Header.astro` | Yes | All pages (via Base.astro) -- GOOD |
| `Footer.astro` | Yes | All pages (via Base.astro) -- GOOD |
| `CTA.astro` | Yes | All pages except thanks pages (via Base.astro) -- GOOD |
| `YouTubeEmbed.astro` | Yes | **0 pages** -- UNUSED |

**YouTubeEmbed.astro is orphaned.** The component exists with proper facade pattern implementation but no page imports or uses it. Pages that embed YouTube videos define their own inline versions instead.

### 6.3 Layout Inheritance

- **All 156 pages** import and use `Base.astro` as layout -- CONSISTENT
- Props used correctly: `title`, `description`, `canonical`, `lang`, `ogImage`, `ogType`, `schema`, `showCTA`, `preloadHero`
- `<Fragment slot="head">` used for per-page `<head>` additions (hreflang, schema, preloads)
- **Verdict:** PASS -- clean and consistent

### 6.4 CSS Scoping

- Base.astro uses `<style is:inline>` (global, no scoping) -- correct for design system
- Header.astro uses `<style is:global>` -- correct for fixed header that affects body layout
- Footer.astro and CTA.astro use `<style>` (scoped by default in Astro) BUT then pages redefine the same styles inline -- this causes the duplication noted in section 1.2
- **No scoping bugs found** (the `is:inline` fix mentioned in the task description appears to be already resolved)

---

## Summary: Priority Action Items

### P0 (Critical -- Performance Impact)

1. **Compress images:** 50+ images exceed 200KB. Blog marketplace screenshots are 1-2.4 MB each. Convert all to WebP and resize to max 1200px wide. **Potential savings: 30-40 MB.**
2. **Remove duplicate gtag script** from 3 fulfilment-ukraina pages (already loaded by Base.astro, causes double-tracking).

### P1 (High -- Code Quality)

3. **Extract FAQ accordion** into a shared file or component. Currently copy-pasted 41 times.
4. **Eliminate duplicate CSS:** Remove `.final-cta`, `.final-form`, `.hero-form`, `.footer` redefinitions from 30+ pages. These are already defined globally in Base.astro, CTA.astro, and Footer.astro.
5. **Fix CSS brace warning** in blog index pages (causes build warnings).
6. **Choose one language switcher:** Header.astro has 80 lines of inline switcher logic AND loads `/js/lang-switcher.js` (90 lines) -- these are redundant competing implementations.

### P2 (Medium -- Best Practice)

7. **Use YouTubeEmbed component:** It exists but is unused. Replace inline yt-facade implementations in 3+ pages with the component.
8. **Add aria-label to hero form inputs:** Most hero forms lack accessibility labels on phone inputs.
9. **CSS variable consistency:** CTA.astro and Footer.astro should use `var(--red)`, `var(--fd)` instead of hardcoded values.

### P3 (Low -- Nice to Have)

10. **Remove `/js/mtp-forms.js`** if Tilda is no longer used (it's a Tilda-specific form handler).
11. **Consider extracting** the ~75 lines of JS from Base.astro (lead submit, hero form, reveal animation, video modal) into an external deferred script.

---

## Scores

| Category | Score | Notes |
|---|---|---|
| Build Health | 9/10 | Builds clean, 2 minor CSS warnings |
| CSS Architecture | 5/10 | Massive duplication across pages |
| JavaScript Quality | 5/10 | FAQ handler x41, dual lang switcher |
| Image Optimization | 3/10 | 56 MB images, 34% WebP adoption |
| HTML/Accessibility | 7/10 | Good structure, missing some aria-labels |
| Astro Best Practices | 7/10 | Clean layout, unused component |
| **Overall** | **6/10** | Images and CSS/JS duplication are main issues |

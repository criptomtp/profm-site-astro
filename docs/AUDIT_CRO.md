# CRO Audit Report — MTP Group Fulfillment Website

**URL:** https://www.fulfillmentmtp.com.ua  
**Date:** 2026-04-09  
**Pages analyzed:** 7  
**Methodology:** Source code analysis of Astro components, layouts, forms, CTAs, trust signals, mobile responsiveness

---

## Executive Summary

The MTP Group website is well-structured with strong trust signals and clear value propositions. The site scores well on hero sections with visible CTAs and pricing transparency. Key conversion opportunities exist around form design, CTA placement consistency, the services page missing a lead form, and mobile tap target optimization.

**Estimated CRO Score: 72/100**

---

## 1. Homepage (`/` — index.astro)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear in 3s | YES | H1: "Fulfillment for online stores. From 18 UAH per shipment." — clear, specific, with price |
| Visible CTA | YES | Phone-only form + "Start ->" button in hero |
| Phone number visible | YES | `tel:+380501444645` in header (desktop + mobile) |
| Badge/context label | YES | "FULFILLMENT IN UKRAINE" badge above H1 |

### Trust Signals

| Signal | Present | Details |
|--------|---------|---------|
| Statistics in hero | YES | 60,000+ shipments/mo, 10 years, 150+ clients, 3,900 m2 |
| Integration logos | YES | Rozetka, Prom.ua, Horoshop, KeyCRM, WooCommerce, OpenCart, SalesDrive (marquee) |
| Media mentions | YES | Europa Plus, Groshi Plus, Top100 (marquee) |
| Video tour | YES | YouTube embed of warehouse tour (bHY3cFF9SlI) |
| Testimonials | YES | 10 text testimonials in slider with names + companies |
| FAQ | YES | 7 FAQ items with Schema.org FAQPage markup |
| LocalBusiness Schema | YES | Full structured data with addresses, phone numbers |

### Forms

| Form | Fields | Submit text | Placement |
|------|--------|-------------|-----------|
| Hero form | 1 (phone) | "Start ->" | Above the fold |
| CTA form (component) | 1 (phone) | "Call me back ->" | Before footer |

- Form submission: sends to `/api/telegram` + `/api/leads`, shows success message, redirects to `/ua/thanks/` after 1.5s
- Success message: Green checkmark + "Thank you! We'll call back."
- Total forms: 2 (hero + pre-footer CTA) -- GOOD, follows best practice

### Social Proof

| Element | Details |
|---------|---------|
| Live notifications | Floating notifications showing "BeautyBox - 47 shipments today", "OrnerUA - 123 shipments today" etc. |
| Client count | "150+ online stores trust us" |
| Named testimonials | 10 reviews: Oleksiy Ryabtsev, Pavlo Mokriyenko, Anton Borysenko, Iryna Savchenko (OrnerUA), Dmytro Koval (KRKR.com.ua), Mykhailo Honchar (FashionUA), Oleh Petrenko (EcoDrive), Viktoriya Lysenko, Serhiy Bondarenko (TechStore UA), Nataliya Moroz (Home & Decor) |
| Specific numbers | "From 100 to 800 shipments/day in 3 months", "Saved 25,000 UAH/month", "Freed 40 hours/month" |

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| No case study section | Medium | Homepage has testimonials but no structured case study with before/after metrics (those are on subpages) |
| No video testimonials on homepage | Low | Video exists only as warehouse tour; video reviews are on /ua/recalls/ |
| Pricing reference only | Low | Price mentioned in hero (from 18 UAH) but no pricing table on homepage; link to /ua/tsiny/ in SEO text only |

### Mobile UX

| Criteria | Status | Details |
|----------|--------|---------|
| Phone clickable (tel:) | YES | Header mobile phone: `<a href="tel:+380501444645">`, Footer phones: `tel:` links |
| Tap targets 44px+ | YES | Mobile burger button has 12px padding + 24px content; lang buttons are 44x44px; mobile phone link has 14px padding |
| Form usable on mobile | YES | Hero form stacks vertically on mobile (`flex-direction:column`), button becomes full-width |
| No horizontal scroll | YES | All sections use responsive grid with `grid-template-columns:1fr` on mobile |

---

## 2. Services Page (`/ua/services/` — services.astro)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear | PARTIAL | H1: "Fulfillment services for online stores" — generic, no price/differentiator |
| Visible CTA | NO | No CTA button or form in hero. Hero only has H1 + subtitle |
| Phone in header | YES | Via global Header component |

### Trust Signals

| Signal | Present | Details |
|--------|---------|---------|
| Integration logos | YES | 8 platform logos (OpenCart, Prom.ua, Rozetka, Horoshop, WooCommerce, KeyCRM, SalesDrive, LP CRM) |
| Pricing table | YES | Dynamic pricing: 0-5 orders = 26 UAH, 200+ = 18 UAH |
| Comparison table | YES | "MTP vs Own warehouse" — shows 49% savings at 50 orders/day |
| Video tour | YES | Warehouse tour section |
| FAQ | YES | 6 FAQ items with Schema.org markup |

### Forms

| Form | Fields | Submit text | Placement |
|------|--------|-------------|-----------|
| CTA form (component) | 1 (phone) | "Call me back ->" | Before footer |

**CRITICAL ISSUE:** No hero form. The hero section is text-only. Visitors must scroll significantly to find the CTA form before the footer.

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| No hero CTA or form | CRITICAL | Hero is purely informational — no way to convert above the fold |
| Hero subtitle weak | High | "Services that help you earn more" is vague, needs specificity |
| No testimonials | Medium | Services page has no social proof from clients |
| 10 service cards without hierarchy | Medium | All 10 services shown equally; user may not know where to start |
| Heavy goods CTA link buried | Low | Inline banner linking to heavy goods page below services grid |

---

## 3. Fulfillment for Online Stores (`/ua/fulfilment-dlya-internet-magazynu/`)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear | YES | H1: "Fulfillment for online stores" + "You sell -- we ship. From 18 UAH per shipment." |
| Visible CTA | YES | Hero form with phone input + "Get a quote ->" button |
| Phone in header | YES | Via global Header component |
| Stats in hero | YES | 6,000 shipments/day, 150+ active clients, 30-sec order assembly |

### Trust Signals

| Signal | Present | Details |
|--------|---------|---------|
| Case study | YES | "Online cosmetics store: from 80 to 400 orders/day" with real metrics (80->400, -70% costs, 2 days to connect) |
| Pricing table | YES | Full tariff grid from 0-49 orders (26 UAH) to 200+ (18 UAH) |
| Video tour | YES | Warehouse tour section |
| Benefits grid | YES | 6 benefits: 30-sec assembly, WMS 24/7, 8 hours/month, API in 2 hours, generators+Starlink, 99.5% accuracy |
| FAQ | YES | 7 FAQ items |
| SEO article | YES | Long-form content explaining fulfillment process |

### Forms

| Form | Fields | Submit text | Placement |
|------|--------|-------------|-----------|
| Hero form | 1 (phone) | "Get a quote ->" | Above the fold |
| CTA form (component) | 1 (phone) | "Call me back ->" | Before footer |

**ISSUE:** The pricing section has a CTA button "Calculate for my store ->" that tries to scroll to `#ctaSection` and focus the form. But the CTA section markup (`<section class="final-cta">`) is NOT present in the page HTML -- the CTA is rendered by the layout via the `<CTA>` component. The `id="ctaSection"` exists in the CTA component, so it should work. However, the `id="finalForm"` reference in the onclick handler is correct since CTA.astro uses that ID.

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| Case study lacks client name | Medium | Case study says "online cosmetics store" but no brand name or photo -- less credible |
| No video testimonials | Medium | Only warehouse tour, no client video reviews |
| Red line decoration before content | Low | `hero-content::before` creates a 3px red line that adds visual weight but no conversion value |

---

## 4. Fulfillment for Small Business (`/ua/fulfilment-dlya-maloho-biznesu/`)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear | YES | Split-screen "NOW vs WITH MTP GROUP" comparison, extremely effective. H1: "Fulfillment for small business" |
| Visible CTA | YES | Phone input + "Calculate cost ->" with red background button (stands out) |
| Price shown | YES | "from 18 UAH/shipment" in large font below H1 |
| Phone in header | YES | Via global Header component |

### Trust Signals

| Signal | Present | Details |
|--------|---------|---------|
| Unit economics table | YES | 4-tier comparison (10, 50, 100, 200 orders/day) -- own warehouse vs MTP |
| Pricing cards | YES | 3 tiers: Start (26 UAH), Growth (22 UAH, marked "POPULAR"), Scale (from 18 UAH) |
| Threshold scale | YES | Visual scale showing when to switch: 5-10, 30-50, 100+ orders/day |
| Pain-solution grid | YES | 5 pains with 5 solutions |
| Video tour | YES | Warehouse tour section |
| FAQ | YES | 8 FAQ items |
| Timeline | YES | 3-day onboarding: Day 1 (consultation), Day 2 (goods to warehouse), Day 3 (first shipment) |

### Forms

| Form | Fields | Submit text | Placement |
|------|--------|-------------|-----------|
| Hero form | 1 (phone) | "Calculate cost ->" | Center of hero |
| CTA form (component) | 1 (phone) | "Call me back ->" | Before footer |

This is one of the best-converting page structures on the site.

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| Broken internal link | High | "Calculate exact price ->" links to `/ua/kalkulyator-fulfillment/` which may not exist (correct URL is `/ua/calculator/`) |
| Broken internal link (2) | High | "Customer reviews ->" links to `/ua/vidhuky/` which may not exist (correct URL is `/ua/recalls/`) |
| No named case studies | Medium | No specific client success stories |
| 5-column pain grid on mobile | Low | `.sb-pains-grid` uses `grid-template-columns:repeat(5,1fr)` -- no mobile override found in visible styles, may cause horizontal scroll |

---

## 5. Reviews Page (`/ua/recalls/`)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear | YES | H1: "Reviews from satisfied MTP Group clients" + "Real stories from 150+ online stores" |
| Visible CTA | YES | Hero form with phone input + "Get a quote ->" |
| Phone in header | YES | Via global Header component |

### Trust Signals

| Signal | Present | Details |
|--------|---------|---------|
| Video testimonials | YES | 8 embedded YouTube videos with client interviews |
| Case studies with metrics | YES | 3 case cards: Carter's (5x growth, 14 UAH/shipment), I.Love.My.Cycle (3x, 90 hrs saved), EcoDrive (50+ kg, 0 damages) |
| Text reviews | YES | 10 text reviews with names, 5-star ratings, company names |
| Aggregate rating Schema | YES | 4.9/5 rating, 150 ratingCount, 10 reviewCount |
| SEO article | YES | Expert analysis of how to evaluate fulfillment partners |

### Forms

| Form | Fields | Submit text | Placement |
|------|--------|-------------|-----------|
| Hero form | 1 (phone) | "Get a quote ->" | Above the fold |
| CTA form (component) | 1 (phone) | "Call me back ->" | Before footer |

### Social Proof Assessment

This page is STRONG. 8 video testimonials + 3 case studies with real numbers + 10 named text reviews = comprehensive social proof.

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| All 8 iframes load at once | High | No lazy video loading strategy -- 8 YouTube iframes significantly impact page load time (each iframe ~500KB+ of resources). Should use lite-youtube-embed or click-to-load |
| No photos of reviewers | Medium | Text reviews have names but no profile photos/avatars |
| No CTA between sections | Medium | Between video grid, case studies, and text reviews -- no intermediate CTA to capture users already convinced |
| Duplicate form handler | Low | Page has its own inline form handler AND the global one from Base.astro -- may cause double submission |

---

## 6. Calculator Page (`/ua/calculator/`)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear | YES | H1: "Fulfillment cost calculator" + "Calculate in 30 seconds" |
| Visible CTA | YES | Hero form + phone input |
| Stats in hero | YES | "from 18 UAH/shipment", "650 UAH/m3 storage", "5,000 UAH minimum/month" |
| Phone in header | YES | Via global Header component |

### Calculator UX

| Feature | Status | Details |
|---------|--------|---------|
| Input fields | 4 | Orders/day (number), Weight category (select), Storage volume m3 (number), Items per order (number) |
| Results shown immediately | YES | JavaScript calculates in real-time on input change -- no form required |
| Contact info required for results | NO | Calculator shows full results without any gating |
| Own warehouse comparison | YES | Automatically calculates own warehouse costs side-by-side |
| Savings percentage | YES | Shows % savings vs own warehouse |
| Time savings | YES | Shows hours freed per month for marketing and product development |

### Pricing Transparency

This page is **EXCELLENT** for conversion. Full tariff table visible, real-time calculator, no gating, comparison with own warehouse built in.

### Forms

| Form | Fields | Submit text | Placement |
|------|--------|-------------|-----------|
| Hero form | 1 (phone) | "Get a quote ->" | Above the fold |
| CTA form (component) | 1 (phone) | "Call me back ->" | Before footer |

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| Calculator not linked to CTA | Medium | After seeing results, there is no "Get a custom quote with these numbers" CTA directly below the results. User must scroll past tariff table and additional services to find the CTA |
| No calculator results in form submission | Medium | When user submits the CTA form, their calculator inputs (orders/day, volume) are not sent along with the phone number -- sales team has no context |
| Hero form competes with calculator | Low | Hero has a phone form, but the real value of this page is the calculator below. Consider removing hero form or replacing with "Scroll to calculator ->" CTA |

---

## 7. EN: Fulfillment for Small Business (`/en/fulfillment-for-small-business/`)

### Above the Fold

| Criteria | Status | Details |
|----------|--------|---------|
| Value proposition clear | YES | Split-screen "Without fulfillment vs With MTP fulfillment" -- strong contrast |
| H1 | YES | "Fulfillment for Small Business in Ukraine" |
| Visible CTA | YES | Phone form + "Get a free quote ->" |
| Price shown | YES | "From $0.45 per shipment" |
| Stats bar | YES | 150+ active clients, 10 yrs, 60,000+ shipments/month, 99.5% accuracy |
| Phone in header | YES | Via global Header component |

### Trust Signals for International Audience

| Signal | Present | Details |
|--------|---------|---------|
| "Why Ukraine" section | YES | 4 cards: 60-70% lower costs, EU access, 44M consumers, tech workforce |
| ROI comparison table | YES | USD pricing, in-house vs MTP at 100 orders/day |
| War-resilient infrastructure | YES | Dedicated section: triple generators, Starlink, dual fiber, zero downtime |
| Blockquote proof | YES | "We shipped 6,000 orders on the day of the largest blackout" |
| Video tour | YES | Warehouse tour |
| USD/EUR pricing | YES | Invoicing in USD/EUR mentioned |

### Localization Quality

| Criteria | Status | Details |
|----------|--------|---------|
| English quality | GOOD | Professional, natural English. No grammar issues. Tone matches B2B international audience |
| No untranslated text | YES | All UI elements properly translated |
| Currency localized | YES | Prices in USD (from $0.45), EUR invoicing available |
| International focus | YES | Mentions Shopify, Magento, WooCommerce, PayPal, Wise -- platforms international clients use |

### Friction Points

| Issue | Severity | Details |
|-------|----------|---------|
| International phone format | GOOD | Placeholder says "+380 or international number", maxlength="25" -- accommodates international numbers |
| No WhatsApp/Telegram CTA | Medium | International users may prefer messaging apps over phone calls |
| Missing Calendly/booking | Medium | International clients would benefit from a "Book a call" with timezone selection rather than "we'll call back" |

---

## Cross-Site Issues

### Forms (All Pages)

| Finding | Severity | Pages Affected |
|---------|----------|---------------|
| Phone-only form field | EXCELLENT | All | Minimal friction, phone-only is perfect for Ukrainian B2B market |
| Form placement: hero + before footer | EXCELLENT | 6 of 7 pages | Services page is the exception -- MISSING hero form |
| Submit button text is actionable | GOOD | All | "Start ->", "Get a quote ->", "Calculate cost ->", "Call me back ->" |
| Success message + redirect | GOOD | All | Green checkmark + thank you message + redirect to /thanks/ after 1.5s |
| No form field validation feedback | Medium | All | Only borderColor change on invalid phone, no text message explaining what's wrong |
| No loading state on submit | Low | All | No spinner or "Sending..." state while API calls execute |

### Trust Signals (Cross-Site)

| Finding | Status |
|---------|--------|
| Consistent header with phone | YES -- all pages via Header.astro component |
| Footer with email + 2 phones + social | YES -- all pages via Footer.astro component |
| Schema.org structured data | YES -- LocalBusiness, Service, FAQPage, BreadcrumbList on every page |
| Integration logos | Present on homepage and services page |
| Client testimonials | Homepage (10 text), recalls page (8 video + 10 text + 3 case studies) |

### Mobile UX (Cross-Site)

| Finding | Severity | Details |
|---------|----------|---------|
| Phone is clickable tel: link | GOOD | Header (mobile and desktop) + Footer use `<a href="tel:...">` |
| Mobile nav is slide-in panel | GOOD | 300px panel from right, with close overlay, phone link at bottom |
| Mobile nav phone link 44px+ | GOOD | `.hdr-mobile-phone` has 14px padding, `.hdr-lang-btn` is 44x44px |
| Forms stack vertically on mobile | GOOD | All hero forms use `flex-direction:column` at `max-width:768px` |
| 5-column grid on small business page | HIGH | `.sb-pains-grid` has no mobile breakpoint for `repeat(5,1fr)` -- likely causes horizontal scroll on mobile |
| Reviews 8 iframes | HIGH | Loading 8 YouTube iframes on mobile is extremely slow |

---

## Prioritized Recommendations

### CRITICAL (Impact: Very High, Fix: Quick)

1. **Add hero CTA form to /ua/services/ page**
   - Currently the only page without a hero form
   - Add the same phone-only form used on other pages
   - Expected impact: +15-25% more leads from this high-intent page
   - File: `src/pages/ua/services.astro`, line 21-27

2. **Fix broken internal links on /ua/fulfilment-dlya-maloho-biznesu/**
   - `/ua/kalkulyator-fulfillment/` should be `/ua/calculator/`
   - `/ua/vidhuky/` should be `/ua/recalls/`
   - File: `src/pages/ua/fulfilment-dlya-maloho-biznesu.astro`, lines 252 and 293

### HIGH (Impact: High, Fix: Medium)

3. **Fix 5-column pain grid mobile overflow**
   - Add mobile breakpoint to `.sb-pains-grid` on `/ua/fulfilment-dlya-maloho-biznesu/`
   - Change to `grid-template-columns: 1fr` or `repeat(2, 1fr)` on mobile
   - Currently likely causes horizontal scroll on phones
   - File: `src/pages/ua/fulfilment-dlya-maloho-biznesu.astro`, style section

4. **Replace YouTube iframes with click-to-load on /ua/recalls/**
   - 8 simultaneous YouTube iframes devastate page load speed
   - Use thumbnail + play button pattern (like the warehouse tour section already does)
   - Expected impact: 3-5x faster page load, better Core Web Vitals
   - File: `src/pages/ua/recalls.astro`, lines 38-69

5. **Add intermediate CTA on /ua/recalls/ between sections**
   - Users who watch a video or read a case study are hot leads
   - Add a simple phone form between videos and case studies, and between case studies and text reviews
   - Expected impact: +10-15% more leads from this high-trust page

6. **Pass calculator data with form submission**
   - When user fills out the calculator and then submits the CTA form, include their calculator inputs (orders/day, volume, etc.) in the API payload
   - Sales team gets immediate context for the call
   - File: `src/pages/ua/calculator.astro` (modify CTA submit to include calc values)

7. **Add sticky "Get a quote" button on mobile**
   - On long pages (small business, calculator, reviews), add a fixed-bottom CTA bar on mobile
   - Eliminates the "how do I contact them" friction on every scroll position
   - Expected impact: +10-20% mobile conversions

### MEDIUM (Impact: Medium, Fix: Medium)

8. **Add WhatsApp/Telegram contact option for EN pages**
   - International users may prefer messaging over phone
   - Add Telegram bot link (already exists: `t.me/MTPGroupFulfillment_bot`) as alternative CTA
   - File: `src/pages/en/fulfillment-for-small-business.astro`

9. **Add Calendly/booking widget for EN pages**
   - International prospects need timezone-aware scheduling
   - "Book a call" with embedded Calendly is standard for B2B SaaS/logistics
   - Alternative to "we'll call back in 15 minutes" which doesn't work across timezones

10. **Add reviewer photos/avatars to testimonials**
    - Homepage testimonials and /ua/recalls/ text reviews have names but no photos
    - Even generic avatar icons increase perceived credibility
    - Expected impact: +5-10% trust signal improvement

11. **Add form validation messages**
    - Currently, invalid phone only gets a red border -- no text message
    - Add "Please enter a valid phone number (at least 10 digits)" message
    - Expected impact: reduces form abandonment from confused users

12. **Improve hero copy on /ua/services/**
    - Current: "Fulfillment services that help you earn more" -- vague
    - Proposed: "10 fulfillment services. Full cycle. From 18 UAH per shipment." -- specific, with price
    - File: `src/pages/ua/services.astro`, line 26

13. **Add case study client names and photos**
    - /ua/fulfilment-dlya-internet-magazynu/ case study says "online cosmetics store" -- anonymous
    - Named, real clients with permission are dramatically more credible
    - Compare with Carter's, I.Love.My.Cycle on /ua/recalls/ which are named

### LOW (Impact: Low, Fix: Quick)

14. **Add loading spinner on form submit**
    - Between click and success message, there's a brief period with no visual feedback
    - Add "Sending..." or a spinner to the button
    - Prevents double-clicks and confirms action is processing

15. **Deduplicate form handlers**
    - /ua/recalls/ has its own inline form handler AND inherits the global one from Base.astro
    - May cause double API calls on form submission
    - File: `src/pages/ua/recalls.astro`, lines 236-248 (remove page-level handler, let Base.astro handle it)

16. **Add "trusted by" counter near CTA forms**
    - Add "150+ businesses already work with us" near the pre-footer CTA form
    - Simple text addition to CTA.astro component
    - File: `src/components/CTA.astro`

17. **Float notification A/B test**
    - Homepage floating notifications ("BeautyBox - 47 shipments today") could be annoying or trust-building
    - Consider A/B testing with/without to measure impact on conversion
    - File: `src/pages/index.astro`, lines 196-206

---

## Summary by Page

| Page | CRO Score | Hero CTA | Forms | Trust Signals | Mobile | Key Fix |
|------|-----------|----------|-------|---------------|--------|---------|
| Homepage `/` | 82/100 | YES | 2 | Strong | Good | Add case study section |
| Services `/ua/services/` | 55/100 | NO | 1 | Good | Good | **Add hero form** |
| Internet shops `/ua/fulfilment-dlya-internet-magazynu/` | 78/100 | YES | 2 | Strong | Good | Name the case study client |
| Small business `/ua/fulfilment-dlya-maloho-biznesu/` | 85/100 | YES | 2 | Excellent | Fix needed | Fix broken links + mobile grid |
| Reviews `/ua/recalls/` | 75/100 | YES | 2 | Excellent | Slow | Replace iframes with thumbnails |
| Calculator `/ua/calculator/` | 80/100 | YES | 2 | Good | Good | Pass calc data to form |
| EN Small biz `/en/fulfillment-for-small-business/` | 82/100 | YES | 2 | Strong | Good | Add messaging CTA option |

---

## Quick Wins (Under 30 minutes each)

1. Add hero form to /ua/services/ (copy from any other page)
2. Fix 2 broken links on /ua/fulfilment-dlya-maloho-biznesu/
3. Add `@media(max-width:768px)` to `.sb-pains-grid` for single-column layout
4. Add "150+ businesses trust us" text to CTA.astro component
5. Remove duplicate form handler from /ua/recalls/

---

## Files Referenced

- `src/components/Header.astro` -- global header with phone, nav, language switcher
- `src/components/Footer.astro` -- global footer with email, 2 phones, social links
- `src/components/CTA.astro` -- pre-footer CTA form component (phone only)
- `src/layouts/Base.astro` -- global form handler, reveal animations, video modal
- `src/pages/index.astro` -- homepage
- `src/pages/ua/services.astro` -- services page (missing hero form)
- `src/pages/ua/fulfilment-dlya-internet-magazynu.astro` -- fulfillment for online stores
- `src/pages/ua/fulfilment-dlya-maloho-biznesu.astro` -- fulfillment for small business (broken links, mobile issue)
- `src/pages/ua/recalls.astro` -- reviews page (iframe performance issue)
- `src/pages/ua/calculator.astro` -- calculator page
- `src/pages/en/fulfillment-for-small-business.astro` -- EN small business page

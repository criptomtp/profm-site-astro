# Week 4 Quick-Start Execution Guide
**MTP-71 Phase: From Planning to Action | Monday Week 4**

---

## Start Here: Your Next 5 Days (Monday-Friday Week 4)

This guide shows **exactly what to do each day** to prepare for Week 5 outreach launch.

Total time commitment: **11-18 hours spread over 5 days** (2-4 hours/day)

---

## Monday: Measurement & Planning (1.5 hours)

### 9:00 AM - Establish Baseline Metrics (30 mins)

**Do this:**
```
1. Open: https://pagespeed.web.dev/
2. Enter URL: https://www.fulfillmentmtp.com.ua/en/guide/
3. Run analysis (takes 30-60 seconds)
4. Record in spreadsheet:
   ├─ LCP: _____ seconds (target: < 2.5s)
   ├─ INP: _____ milliseconds (target: < 200ms)
   ├─ CLS: _____ (target: < 0.1)
   ├─ Performance Score: _____/100 (target: > 85)
   └─ Date recorded: _____

5. Screenshot or save report for comparison on Friday
```

**Why:** Establishes baseline so you can measure improvement

---

### 10:00 AM - Check Google Search Console (30 mins)

**Do this:**
```
1. Go to: https://search.google.com/search-console/
2. Select your property (fulfillmentmtp.com.ua)
3. Check three things:

   COVERAGE:
   ├─ Total pages indexed: _____ (should be 298+)
   ├─ Any errors?: yes/no
   └─ Action: If errors, note for fixing

   CORE WEB VITALS:
   ├─ Good: _____ pages (target: 250+)
   ├─ Needs improvement: _____ pages
   └─ Poor: _____ pages
   
   PERFORMANCE:
   ├─ Top query: _______________ (position: ___)
   ├─ Organic impressions: _____
   └─ CTR: ___%

4. Screenshot metrics for comparison Friday
```

**Why:** Understand current search visibility before optimization

---

### 11:00 AM - Review Implementation Plan (30 mins)

**Do this:**
```
1. Open: IMPLEMENTATION_TEMPLATES.md
2. Skim all 6 sections:
   ├─ Internal Linking (most important)
   ├─ dateModified Schema
   ├─ Meta Descriptions
   ├─ Core Web Vitals
   ├─ Image Optimization
   └─ Week 4 Daily Schedule

3. Create simple checklist:
   [ ] Internal linking (4-6 hours needed)
   [ ] dateModified schema (1-2 hours needed)
   [ ] Meta descriptions (1-2 hours needed)
   [ ] Core Web Vitals (2-4 hours needed)
   [ ] Image optimization (2-3 hours if needed)
   
4. Decide priority order for Tue-Thu
   (Recommendation: Internal linking first)
```

**Why:** Gets you mentally prepared for implementation

---

## Tuesday: Internal Linking Phase 1 (2-3 hours)

### 9:00 AM - Cluster 1 Implementation (Foundations)

**Files to update:**
- `src/pages/en/guide/what-is-3pl.astro`
- `src/pages/en/guide/how-to-choose-fulfillment-operator.astro`
- `src/pages/en/guide/sla-agreements.astro`

**Do this:**

```astro
STEP 1: Open what-is-3pl.astro
STEP 2: Find this text (Ctrl+F):
  "definition" or "3PL definition"
STEP 3: Add this link naturally:
  "Once you understand what 3PL means, the next critical step is 
   <a href="/en/guide/how-to-choose-fulfillment-operator/">
   choosing the right 3PL partner</a> that aligns with your business..."

STEP 4: Find "benefits" section
STEP 5: Add link to SLA guide:
  "...make sure you understand 
   <a href="/en/guide/sla-agreements/">
   service level agreements and guarantees</a>—they protect..."

STEP 6: Save file (Ctrl+S)
STEP 7: Repeat for other two files in Cluster 1
```

**Validation:**
```bash
npm run build
# If error: Check closing </a> tags
# If success: Ready for next cluster
```

**Time estimate:** 45 mins - 1 hour for all 3 files

---

### 11:00 AM - Cluster 2 Implementation (Core Operations)

**Files to update:**
- `src/pages/en/guide/inventory-management.astro`
- `src/pages/en/guide/picking-packing.astro`
- `src/pages/en/guide/quality-control-accuracy.astro`
- `src/pages/en/guide/returns-management.astro`
- `src/pages/en/guide/customer-service.astro`

**Do this:**

```
STEP 1: Use IMPLEMENTATION_TEMPLATES.md as reference
STEP 2: Open Inventory Management guide
STEP 3: Find sections (use Ctrl+F):
  "ABC Analysis" → Add link to Picking guide
  "Accuracy" → Add link to Quality Control guide
  "Cost" → Add link to Pricing guide
STEP 4: Follow copy-paste template from document
STEP 5: Test each link in browser after saving
STEP 6: Repeat for other Cluster 2 guides
```

**Validation:**
```bash
npm run build
# Check for errors
```

**Time estimate:** 1.5 hours for 5 files

---

### 2:00 PM - Interim Save & Review

```
[ ] Commit changes to git (if using version control)
git add src/pages/en/guide/
git commit -m "Add internal links: Clusters 1-2"

[ ] Review links in browser:
  Open: https://localhost:3000/en/guide/what-is-3pl/
  Click internal links → Verify they work
  
[ ] Note any broken links for fixing later
```

---

## Wednesday: Internal Linking Phase 2 + Schema (2.5 hours)

### 9:00 AM - Clusters 3-4 Implementation (Technology & Strategy)

**Files to update:**
- Cluster 3: WMS, Shopify, Rozetka, Prom integration guides (4 files)
- Cluster 4: Scaling, Pricing, Risk Management, Staff Training (4 files)

**Do this:**

```
STEP 1: Use same process as Tuesday
STEP 2: Focus on high-value connections:
  ├─ WMS → All integration guides
  ├─ Scaling → Quality, Pricing, Risk, Staff Training
  ├─ Pricing → Scaling, Quality, Inventory
  └─ Risk → Pricing, Scaling, Operator selection

STEP 3: For each guide:
  [ ] Add 2-3 most relevant internal links
  [ ] Use anchor text from IMPLEMENTATION_TEMPLATES.md
  [ ] Test links work
  
STEP 4: Validate build
npm run build
```

**Time estimate:** 1 hour for 8 files

---

### 11:00 AM - dateModified Schema Update (1-1.5 hours)

**Files to update:** All 36 guide files (both /en/ and /ua/)

**Do this:**

```astro
STEP 1: Open any guide file
STEP 2: Find this section:
<Fragment slot="head">
  <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "...",
      "author": {...}
    }
  </script>
</Fragment>

STEP 3: Add two lines inside the script (after author):
      "datePublished": "2025-04-15",
      "dateModified": "2025-04-19",

STEP 4: Save file
STEP 5: Repeat for all 36 guides

STEP 6: After updating all:
npm run build
```

**Speed tip:** Use Find & Replace
```
Find: "author": {
Replace with: "datePublished": "2025-04-15",
              "dateModified": "2025-04-19",
              "author": {
```

**Time estimate:** 1-1.5 hours for all 36 (using Find & Replace)

---

### 2:00 PM - Build & Deploy

```bash
npm run build
# Wait for build to complete
# Should show: ✓ Built in XXs

# If errors: 
# - Check for syntax errors (missing quotes, brackets)
# - Review changes made in last step
# - Fix and rebuild
```

---

## Thursday: Meta Descriptions & Core Web Vitals (3-4 hours)

### 9:00 AM - Meta Description Audit (1 hour)

**Do this:**

```
STEP 1: Create spreadsheet with 3 columns:
  | Guide Name | Current Description | Optimized Description |
  
STEP 2: For each guide, use template:
  "[Primary Keyword]: [Specific Benefit]. [Data/Number]."
  
STEP 3: Examples:
  "Inventory Management: Cross-channel sync, ABC analysis, 
   and 25-50% cost reduction tactics for e-commerce."
   
  "Quality Control: Achieve 99.5% accuracy with 3-pillar 
   quality system and staff training framework."
   
  "Fulfillment Scaling: Scale from 100 to 6,000+ orders/day. 
   10 KPIs, bottleneck identification, playbook."

STEP 4: Ensure each is 155-160 characters
  (Most important for SERP appearance)
  
STEP 5: Save to spreadsheet for reference
```

**Time estimate:** 1 hour for 36 guides

---

### 10:30 AM - Core Web Vitals Optimization (2-3 hours)

**Check current state:**
```bash
npm run build
# This generates production build
# Images are optimized by Astro build process
```

**Optimize images if needed:**

```
IF images are > 50KB:

STEP 1: Go to https://squoosh.app/
STEP 2: Upload image
STEP 3: Set quality to 70-80%
STEP 4: Export as WebP
STEP 5: Replace in /src/images/
STEP 6: Update img tag with width/height:

<img 
  src="/images/guide-hero.webp" 
  alt="Descriptive text"
  width="720" 
  height="360"
/>
```

**Optimize fonts (if slowing LCP):**

```css
/* In CSS file */
@font-face {
  font-family: 'DM Serif Display';
  src: url('/fonts/dm-serif.woff2') format('woff2');
  font-display: swap;  /* ← Add this line */
}
```

**Test improvements:**

```
STEP 1: Run build: npm run build
STEP 2: Open: https://pagespeed.web.dev/
STEP 3: Enter: https://www.fulfillmentmtp.com.ua/en/guide/
STEP 4: Compare to Monday baseline:
  LCP: Monday ____ → Thursday ____
  INP: Monday ____ → Thursday ____
  CLS: Monday ____ → Thursday ____
  Score: Monday ____/100 → Thursday ____/100
STEP 5: Target: >20% improvement in each metric
```

**Time estimate:** 2-3 hours depending on optimization needed

---

## Friday: Final Verification & Go/No-Go (2-3 hours)

### 9:00 AM - Build Verification (30 mins)

```bash
npm run build
# Check: Build completes successfully
# Check: No warnings or errors
# Output should show: ✓ Built in XXs

# If errors:
# - Fix syntax errors (missing closing tags, quotes)
# - Rebuild
# - Do NOT proceed until clean build
```

---

### 10:00 AM - Link Testing (1 hour)

**Do this:**

```
STEP 1: Start local dev server:
npm run dev

STEP 2: Open: http://localhost:3000/en/guide/

STEP 3: Spot-check 5 guides:
[ ] What is 3PL
  ├─ Click links to operator selection & SLA
  ├─ Verify links work (no 404s)
  └─ Check anchor text is readable

[ ] Inventory Management
  ├─ Click links to picking, quality, pricing
  ├─ Verify navigation flow makes sense
  └─ Check no broken links

[ ] Scaling
[ ] Pricing
[ ] Quality Control

STEP 4: If any broken links:
  - Note which guide/link
  - Fix the href attribute
  - Test again
```

---

### 11:00 AM - Schema Validation (30 mins)

**Do this:**

```
STEP 1: Open guide in browser
STEP 2: Right-click → View Page Source
STEP 3: Press Ctrl+F, search for "dateModified"
  Result: Should find it in every guide
  
STEP 4: Verify format:
  "dateModified": "2025-04-19"  ← Correct
  (Not: "dateModified": "2025-04-19,")  ← Wrong

STEP 5: If any errors:
  - Fix JSON syntax
  - Rebuild
  - Verify again
```

---

### 12:00 PM - Core Web Vitals Final Check (30 mins)

```
STEP 1: Run PageSpeed Insights again:
https://pagespeed.web.dev/

STEP 2: Compare Friday vs Monday:
Metric          Monday    Friday    Improvement
LCP            ______    ______    ________
INP            ______    ______    ________
CLS            ______    ______    ________
Score          ____/100  ____/100  ________

STEP 3: Check target achievement:
✅ LCP < 2.5s?
✅ INP < 200ms?
✅ CLS < 0.1?
✅ Score > 85/100?

STEP 4: If targets met:
  Ready for Week 5 launch ✅
  
STEP 5: If targets missed:
  Identify issue and quick fix:
  ├─ LCP slow? → Compress images more
  ├─ CLS high? → Add width/height to images
  ├─ INP slow? → Check for JavaScript issues
  └─ Score low? → Review audit recommendations
```

---

### 1:00 PM - Go/No-Go Decision

**Checklist before Week 5 outreach:**

```
CRITICAL ITEMS (Must complete):
✅ [ ] Build clean (no errors)
✅ [ ] Internal links implemented (all 5 clusters)
✅ [ ] dateModified schema added (all 36 guides)
✅ [ ] Core Web Vitals measured and optimized
      └─ LCP < 2.5s: YES/NO
      └─ INP < 200ms: YES/NO
      └─ CLS < 0.1: YES/NO
✅ [ ] PageSpeed score > 85/100: YES/NO
✅ [ ] All guides link properly (spot check passed)
✅ [ ] No 404 errors

HIGH PRIORITY (Should complete):
✅ [ ] Meta descriptions audit completed
✅ [ ] Image alt text reviewed
✅ [ ] Google Search Console data recorded

DECISION:
  ✅ GO FOR WEEK 5 (all critical items complete)
  ⚠️ CONDITIONAL GO (minor items missing, can catch up Week 5)
  ❌ NO-GO (critical items incomplete, must fix before outreach)
```

---

## Weekend: Prep for Week 5 Launch

### Saturday/Sunday (1-2 hours optional)

**If you have time, prepare:**

```
OPTIONAL but helpful:

[ ] Open OUTREACH_BATCH_1.md
[ ] Review the 15 target sites
[ ] Gather contact information:
    ├─ Email addresses (if not in templates)
    ├─ Editor names
    └─ Recent articles they've published

[ ] Prepare tracking spreadsheet:
    | Company | Contact | Email Sent Date | Response | Status |
    
[ ] Test email account
    ├─ Send test email to yourself
    ├─ Verify it reaches inbox (not spam)
    └─ Note any delivery issues

[ ] Prepare email signature/template
    ├─ Ensure professional format
    ├─ Include contact info
    └─ Include link to profm.ua
```

---

## Emergency Troubleshooting

### "Build is failing - what do I do?"

```
STEP 1: Check error message
npm run build
# Look for: "✗ Error: [specific error]"

STEP 2: Common errors:
  ❌ Syntax error (missing quotes, brackets)
     Fix: Find the line, check quotes/brackets
     
  ❌ File not found error
     Fix: Verify file path is correct
     
  ❌ Astro syntax error
     Fix: Ensure proper Astro tag usage

STEP 3: If you can't fix:
  git checkout -- src/pages/
  # Reverts all changes (start over with one change at a time)
```

---

### "I don't understand how to add a link"

```
SIMPLE EXAMPLE:

Instead of:
<p>Learn about inventory management.</p>

Use:
<p>Learn about <a href="/en/guide/inventory-management/">
inventory management</a>.</p>

Key parts:
- <a href="..."> opens link
- URL format: /en/guide/topic-name/
- </a> closes link
- Text between tags is what users see
```

---

## Quick Reference: File Locations

```
Guide files to update:
src/pages/en/guide/*.astro        (English guides)
src/pages/ua/guide/*.astro        (Ukrainian guides)

Layout file (if needed):
src/layouts/Base.astro

Configuration:
astro.config.mjs
```

---

## Success Metrics After Week 4

### Friday EOD: You should have...

```
✅ Internal linking implemented across all 36 guides
✅ dateModified schema on all guides
✅ Core Web Vitals optimized (LCP, CLS, INP)
✅ Meta descriptions improved
✅ PageSpeed score > 85/100
✅ Clean build with no errors
✅ All links tested and working
✅ Baseline metrics recorded for comparison

READY FOR: Week 5 outreach launch
STATUS: ✅ PREPARED
```

---

## Monday Week 5: Launch Day Checklist

```
[ ] Deploy latest build to production
[ ] Verify guides live and working
[ ] Open OUTREACH_BATCH_1.md
[ ] Start sending Week 5 outreach emails
[ ] Track responses in spreadsheet
[ ] Monitor email deliverability

Monday goal: Send 3-5 emails to top-tier targets
```

---

## Need Help?

**If you get stuck:**

1. Check IMPLEMENTATION_TEMPLATES.md for your specific task
2. Review example code in that document
3. Compare your code to the template
4. Check for syntax errors (quotes, brackets, closing tags)
5. Run `npm run build` to verify

**Still stuck?**
- Revert changes: `git checkout -- src/pages/`
- Start with one guide at a time
- Test and verify before moving to next guide

---

## Timeline Summary

```
MONDAY:     1.5 hours - Measure baseline + plan
TUESDAY:    2-3 hours - Clusters 1-2 internal linking
WEDNESDAY:  2.5 hours - Clusters 3-4 + schema updates
THURSDAY:   3-4 hours - Meta descriptions + CWV optimization
FRIDAY:     2-3 hours - Final verification + go/no-go decision

TOTAL:      11-18 hours over 5 days
PACE:       2-4 hours/day (very manageable)

RESULT:     Site optimized for Week 5 outreach launch
```

---

**Ready to begin Monday? Start with the Monday checklist above.**

**Questions? Refer back to IMPLEMENTATION_TEMPLATES.md for detailed guidance.**

**Let's go.**


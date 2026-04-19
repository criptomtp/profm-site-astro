# Core Web Vitals Optimization Guide
**MTP-71 Phase: Pre-Outreach Performance | Priority: HIGH**

---

## Why Core Web Vitals Matter for Link Building

**Search ranking impact:**
- Google uses Core Web Vitals as ranking factor (since May 2021)
- Poor CWV = lower rankings despite backlinks
- Good CWV = backlinks have full impact

**User experience impact:**
- Slow sites: 50% higher bounce rate
- Fast sites: +25% higher click-through rate from search results
- Mobile experience: Critical for referral traffic quality

**Campaign impact:**
- Slow site receiving backlinks = wasted link juice
- Each slow page load = lower conversion on referral traffic
- Target: Optimize CWV BEFORE outreach begins (Week 4)

---

## Core Web Vitals Metrics

### 1. LCP (Largest Contentful Paint)
**What it measures:** How long until main content is visible  
**Target:** < 2.5 seconds (good) / < 4.0 seconds (acceptable)

**Common culprits (fulfillment guides likely affected by):**
- Large uncompressed images (hero images in guide sections)
- Custom fonts (DM Serif Display may be slow)
- Unoptimized Astro builds
- Server response time (TTFB)

**Impact on guides:**
- Hero image with guide title is probably LCP element
- If LCP > 3s, Google may penalize rankings
- Each 100ms improvement = 2-3% CTR improvement

### 2. INP (Interaction to Next Paint)
**What it measures:** Responsiveness to user clicks/input  
**Target:** < 200ms (good) / < 500ms (acceptable)  
**Replaces:** First Input Delay (FID) - retired March 2024

**Common culprits:**
- JavaScript execution blocking main thread
- Unoptimized event listeners
- Poor JavaScript bundle size
- Analytics/tracking scripts running on main thread

**Impact on guides:**
- Guide table of contents navigation should be snappy
- Internal links should feel responsive
- Guides with many interactive elements need optimization

### 3. CLS (Cumulative Layout Shift)
**What it measures:** Unexpected layout shifts during page load  
**Target:** < 0.1 (good) / < 0.25 (acceptable)

**Common culprits:**
- Images without width/height attributes (forces layout recalculation)
- Late-loading ads or embeds
- Font loading causing text reflow
- Dynamically injected content above fold

**Impact on guides:**
- If hero images shift during load = CLS issue
- If nav shifts = bad UX
- Usually easiest metric to fix

---

## Measurement (Week 4 - BEFORE Outreach)

### Option 1: Google PageSpeed Insights (Easiest)
```
Website: https://pagespeed.web.dev/
Steps:
1. Enter your guide URL
2. Run analysis (takes 30-60 seconds)
3. Record scores for:
   - LCP (seconds)
   - INP (milliseconds)
   - CLS (number)
4. Get field data (real user metrics) + lab data (simulated)
```

**What to look for:**
- Field data (real users): Most important
- Lab data (simulated): Helps with debugging
- Compare mobile vs desktop (mobile usually slower)

### Option 2: Core Web Vitals in Google Search Console (Most Accurate)
```
Website: https://search.google.com/search-console/
Steps:
1. Go to Enhancements → Core Web Vitals
2. View by page/URL
3. Check "Good", "Needs Improvement", "Poor" status
4. Identify problem pages

Note: This shows real user data only (100k+ monthly users)
If site is new, may not have data yet
```

### Option 3: Chrome DevTools (For Debugging)
```
Steps:
1. Open guide in Chrome
2. Right-click → Inspect → Lighthouse tab
3. Click "Analyze page load"
4. Gets detailed performance metrics
5. Identifies specific optimization opportunities
```

---

## Optimization Strategy (Quick Wins First)

### Phase 1: CLS Optimization (Easiest - 30 mins)

#### 1.1: Image Dimensions
**Impact:** 40-60% of CLS issues

```html
<!-- BEFORE (causes layout shift) -->
<img src="guide-hero.jpg" alt="Hero">

<!-- AFTER (prevents shift) -->
<img src="guide-hero.jpg" alt="Hero" width="720" height="360">
```

**Astro syntax:**
```astro
---
import Image from 'astro/components/Image.astro';
---

<Image 
  src={import('./guide-hero.jpg')} 
  alt="Hero"
  width={720}
  height={360}
/>
```

**Action:**
- [ ] Find all `<img>` tags in guide pages
- [ ] Add width/height attributes
- [ ] Calculate correct aspect ratio (width:height)
- [ ] Test in Chrome DevTools

#### 1.2: Font Loading
**Impact:** 20-30% of CLS issues

**Current: DM Serif Display (custom font)**

```css
/* BEFORE: Causes FOIT (Flash of Invisible Text) */
@font-face {
  font-family: 'DM Serif Display';
  src: url('/fonts/dm-serif.woff2') format('woff2');
}

/* AFTER: Prevents shift with fallback */
@font-face {
  font-family: 'DM Serif Display';
  src: url('/fonts/dm-serif.woff2') format('woff2');
  font-display: swap; /* Show fallback immediately */
}
```

**Action:**
- [ ] Add `font-display: swap;` to custom fonts
- [ ] Consider system fonts as fallback (faster)
- [ ] Limit to 1-2 custom fonts maximum

#### 1.3: Preload Critical Resources
```html
<!-- In <head> of Base layout -->
<link rel="preload" as="image" href="/images/guide-hero.jpg">
<link rel="preload" as="font" href="/fonts/dm-serif.woff2" type="font/woff2">
```

**Action:**
- [ ] Preload hero images
- [ ] Preload custom fonts
- [ ] Limit to 2-3 preload directives (too many = performance hit)

---

### Phase 2: LCP Optimization (Medium Difficulty - 2-4 hours)

#### 2.1: Image Optimization
**Impact:** 50-70% of LCP issues

```bash
# Convert images to modern format (WebP)
npx imagemin src/images/*.jpg --plugin=webp --out-dir=src/images/webp

# Or use online tool: https://squoosh.app/
# Compress: 60-70% quality = imperceptible difference + 50-60% file size reduction

# Verify file sizes (target: <50KB for hero images)
ls -lh src/images/guide-hero.jpg
# Should be < 50KB after compression
```

**Astro implementation:**
```astro
<picture>
  <source srcset="/images/webp/guide-hero.webp" type="image/webp">
  <source srcset="/images/guide-hero.jpg" type="image/jpeg">
  <img 
    src="/images/guide-hero.jpg" 
    alt="Hero"
    width="720" 
    height="360"
    loading="eager"
  />
</picture>
```

**Action:**
- [ ] Audit all guide images (size, format, optimization)
- [ ] Convert large images to WebP
- [ ] Compress images to 60-70% quality
- [ ] Target hero images first (biggest impact)

#### 2.2: Server Response Time (TTFB)
**Impact:** 20-30% of LCP issues (Time to First Byte)

**Check current TTFB:**
```
PageSpeed Insights → Metrics → Time to First Byte
Target: < 600ms
```

**If TTFB > 1s:** Likely server/hosting issue
- Check if host is in same region as users
- May require CDN (Cloudflare, etc.)

**If TTFB < 600ms:** Good; move to other optimizations

**Action:**
- [ ] Check current TTFB in PageSpeed Insights
- [ ] If acceptable (< 600ms), skip this
- [ ] If poor (> 1s), consider CDN or server upgrade

#### 2.3: Remove Render-Blocking Resources
**Impact:** 10-20% of LCP issues

```astro
<!-- BEFORE: Blocks page render -->
<script src="/lib/heavy-library.js"></script>
<link rel="stylesheet" href="/styles/non-critical.css">

<!-- AFTER: Doesn't block render -->
<script src="/lib/heavy-library.js" defer></script>
<link rel="preload" href="/styles/non-critical.css" as="style">
<noscript><link rel="stylesheet" href="/styles/non-critical.css"></noscript>

<!-- Or: Load after page ready -->
<script>
  window.addEventListener('load', () => {
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = '/styles/non-critical.css';
    document.head.appendChild(link);
  });
</script>
```

**Action:**
- [ ] Audit scripts in Base layout (what's actually needed on page load?)
- [ ] Add `defer` to non-critical JavaScript
- [ ] Move non-critical CSS to lazy-load
- [ ] Test that page still functions properly

---

### Phase 3: INP Optimization (Complex - 4-6 hours)

#### 3.1: Optimize JavaScript Execution
**Impact:** 40-60% of INP issues

```astro
--- 
// BEFORE: Heavy computation on click
function handleClick() {
  let result = 0;
  for (let i = 0; i < 1000000; i++) {
    result += Math.sqrt(i);
  }
  console.log(result);
}

// AFTER: Break into smaller chunks (using requestIdleCallback)
function handleClickOptimized() {
  const work = () => {
    // Do small chunk of work
    let result = 0;
    for (let i = 0; i < 10000; i++) {
      result += Math.sqrt(i);
    }
    return result;
  };
  
  if ('requestIdleCallback' in window) {
    requestIdleCallback(work);
  } else {
    setTimeout(work, 1);
  }
}
---
```

**Common issues in guides:**
- Table of contents navigation
- Internal link click handlers
- Any click listeners should finish in < 100ms

**Action:**
- [ ] Identify slow interactions (DevTools → Performance tab)
- [ ] Break into smaller tasks
- [ ] Use requestIdleCallback for non-critical work

#### 3.2: Optimize Event Listeners
```astro
<!-- BEFORE: Many listeners -->
<button onclick="handleClick1()">Link 1</button>
<button onclick="handleClick2()">Link 2</button>
<button onclick="handleClick3()">Link 3</button>

<!-- AFTER: Event delegation (single listener) -->
<div id="toc" class="toc-container">
  <button data-target="/guide/topic-1">Link 1</button>
  <button data-target="/guide/topic-2">Link 2</button>
  <button data-target="/guide/topic-3">Link 3</button>
</div>

<script>
  const tocContainer = document.getElementById('toc');
  tocContainer.addEventListener('click', (e) => {
    if (e.target.tagName === 'BUTTON') {
      window.location.href = e.target.dataset.target;
    }
  });
</script>
```

**Action:**
- [ ] Audit Table of Contents (if interactive)
- [ ] Use event delegation instead of individual listeners
- [ ] Test responsiveness with DevTools

---

## Implementation Timeline

### Week 4 Priority Order (Before Outreach)

```
Monday:    Measure baseline (PageSpeed Insights, GSC)
Tuesday:   CLS optimization (images, fonts) - 1-2 hours
Wednesday: LCP optimization (images, TTFB check) - 2-4 hours
Thursday:  INP optimization (if needed) - 2-4 hours
Friday:    Verify improvements + prepare for outreach
```

---

## Measurement & Verification

### Before vs After Comparison
```
Record baseline (Week 4):
├─ LCP: ___ seconds
├─ INP: ___ milliseconds  
├─ CLS: ___
└─ Overall score: ___/100

Target after optimization (Week 4 end):
├─ LCP: < 2.5 seconds (improvement: > 20%)
├─ INP: < 200 milliseconds (improvement: > 10%)
├─ CLS: < 0.1 (improvement: > 30%)
└─ Overall score: > 85/100
```

### Ongoing Monitoring
```
Weekly tracking (during campaign):
├─ Monday: Check PageSpeed Insights (pick 3 top guides)
├─ Wednesday: Check Google Search Console CWV report
├─ Friday: Note any regressions + fix immediately
```

---

## Expected ROI

### Ranking Impact
```
Before optimization:  Position 12-15 for target keywords
After optimization:   Position 10-12 for target keywords
→ +2-3 position improvement = +20-30% CTR increase
```

### Traffic Impact
```
Baseline: 2,000 organic sessions/month
CWV improvement: +15-25% CTR improvement
Estimated gain: +300-500 sessions/month
+ backlinks during campaign: +500-1,000 additional sessions

Total expected: 2,800-3,500 sessions/month (vs 2,000 baseline)
```

### Backlink Value Multiplier
```
Poorly optimized site: Each backlink worth ~$5-10
Well-optimized site: Each backlink worth ~$8-15
Multiplier: 1.6-3x ROI improvement from CWV optimization
```

---

## Common Gotchas

### Issue: Optimization breaks responsive design
**Solution:** Test on mobile device (not just desktop)
**Why:** Mobile LCP usually slower than desktop

### Issue: Images blur after optimization
**Solution:** Increase quality setting (80-85% instead of 60-70%)
**Why:** 60% quality too aggressive for large images

### Issue: Font still causing CLS
**Solution:** Increase font preload priority or use system font fallback
**Why:** Font loading is often bottleneck for custom fonts

### Issue: INP still slow after optimization
**Solution:** Profile with DevTools to find actual bottleneck
**Why:** Might be rendering, not JavaScript execution

---

## Tools & Resources

### Testing Tools (All Free)
- **PageSpeed Insights:** https://pagespeed.web.dev/
- **Google Search Console:** https://search.google.com/search-console/
- **WebPageTest:** https://www.webpagetest.org/
- **Chrome DevTools:** Open in browser (F12)

### Image Optimization Tools
- **TinyPNG:** https://tinypng.com/ (simplest)
- **Squoosh:** https://squoosh.app/ (more control)
- **ImageOptim:** https://imageoptim.com/ (batch processing)

### Learning Resources
- **Google CWV Guide:** https://web.dev/vitals/
- **Google PageSpeed Guide:** https://developers.google.com/speed/docs/insights/v5/about
- **Web.dev Optimization Guide:** https://web.dev/performance/

---

## Success Checklist

```
[ ] Baseline metrics recorded (PageSpeed Insights)
[ ] All images optimized + width/height attributes added
[ ] Custom fonts have font-display: swap
[ ] Hero images preloaded
[ ] Render-blocking resources identified + removed/deferred
[ ] LCP verified < 2.5 seconds (lab test)
[ ] INP verified < 200ms (if slow in baseline)
[ ] CLS verified < 0.1
[ ] Mobile performance verified (priority: matches desktop improvements)
[ ] PageSpeed Insights score > 85/100
[ ] Google Search Console CWV report shows improvement
[ ] Ready for outreach campaign (Week 5)
```

---

## Maintenance

### Weekly (During Campaign)
- Check PageSpeed Insights on top 3 guides (5 mins)
- Monitor Google Search Console CWV report
- Fix any regressions immediately

### Monthly
- Run full PageSpeed audit (15 mins)
- Compare to baseline
- Document improvements
- Plan next optimization wave

### Per New Guide
- Test each new guide before publishing
- Ensure LCP < 3s, INP < 300ms, CLS < 0.15
- Add to monitoring dashboard

---

## Timeline Integration with Campaign

```
Week 4: CWV Optimization (Before Outreach)
  ├─ Monday-Thursday: Implement optimizations
  ├─ Friday: Verify improvements
  └─ Ready for Week 5 outreach

Week 5-12: Monitor & Maintain
  ├─ Weekly: Quick PageSpeed check
  ├─ If regression: Fix immediately
  └─ Priority: Keep CWV stable during high-traffic period (from backlinks)
```

---

**Status: READY TO IMPLEMENT**  
**Timeline: Complete by Friday of Week 4 (before outreach begins)**  
**Expected impact: +20-30% CTR improvement + +2-3 ranking positions for top keywords**


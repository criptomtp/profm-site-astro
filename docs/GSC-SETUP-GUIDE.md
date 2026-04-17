# Google Search Console Setup Guide (MTP-67)

**Last Updated:** April 17, 2026  
**Status:** Ready for GSC deployment  
**Site:** https://www.fulfillmentmtp.com.ua

---

## Pre-Launch Checklist ✅

### 1. Vercel Deployment Status
- [x] Site deployed to Vercel
- [x] Production domain: fulfillmentmtp.com.ua
- [x] SSL certificate: Valid
- [x] Sitemap generated: `/dist/sitemap-index.xml`

### 2. Sitemap Verification
- [x] Sitemap-index.xml includes lastmod dates
- [x] 251 pages indexed in sitemap
- [x] Freshness signal: Updated on 2026-04-17
- [x] No noindex pages included
- [x] Proper sitemap format (XML)

**Sitemap URLs:**
- Main: `https://www.fulfillmentmtp.com.ua/sitemap-index.xml`
- Sitemap-0: `https://www.fulfillmentmtp.com.ua/sitemap-0.xml`

### 3. Meta Tags Verification
- [x] Meta descriptions: Optimized (155 chars max)
- [x] Title tags: Keyword-focused
- [x] Hreflang tags: 4 variants per page (uk/en/ru/x-default)
- [x] Canonical tags: Self-referencing
- [x] Schema.org markup: Present (LocalBusiness, FAQPage, BreadcrumbList)

### 4. Core SEO Elements
- [x] robots.txt: Configured correctly
- [x] Security headers: HSTS, CSP, X-Frame-Options
- [x] Mobile responsive: Verified
- [x] SSL/HTTPS: Enforced
- [x] Load speed: Optimized (Astro)

---

## Google Search Console Setup (Week 1)

### Step 1: Add Property to GSC

1. Go to [Google Search Console](https://search.google.com/search-console/)
2. Click **"Add property"**
3. Select **"URL prefix"** (not Domain)
4. Enter: `https://www.fulfillmentmtp.com.ua`
5. Click **Continue**

### Step 2: Verify Ownership (Choose One)

**Option A: HTML File (Recommended for Vercel)**
1. Download HTML verification file from GSC
2. Place in `/public/` folder in your Astro project
3. Deploy to Vercel
4. Return to GSC and click **Verify**

**Option B: DNS TXT Record**
1. Copy the TXT record from GSC
2. Go to your domain registrar (GoDaddy, Namecheap, etc.)
3. Add the TXT record to your DNS settings
4. Wait 5-15 minutes for propagation
5. Return to GSC and click **Verify**

**Option C: Meta Tag**
1. Copy the meta tag from GSC
2. Add to `src/layouts/Base.astro` in the `<head>` section
3. Deploy to Vercel
4. Return to GSC and click **Verify**

### Step 3: Submit Sitemaps

1. In GSC, go to **Sitemaps** (left sidebar)
2. In the "Add a new sitemap" box, enter:
   ```
   sitemap-index.xml
   ```
3. Click **Submit**
4. Wait a few seconds—you should see:
   - Status: ✅ Success
   - Index count: 251 pages

### Step 4: Monitor Coverage

1. Go to **Coverage** (left sidebar)
2. You should see:
   - Valid: 251 pages (may take 24-48 hours to appear)
   - Excluded: 0-5 pages (redirects, noindex)
3. Click on each status category to inspect:
   - **Valid** → Pages correctly indexed
   - **Excluded** → Pages with noindex, redirects
   - **Error** → Pages with issues (usually 0)

### Step 5: Enable Crawl Stats Monitoring

1. Go to **Crawl Stats** (left sidebar)
2. Record baseline metrics:
   - Requests per day
   - Kilobytes downloaded
   - Response time

3. Set a reminder to check weekly for:
   - Increased crawl frequency (sign of freshness signals)
   - Crawl efficiency improvements

---

## Expected Milestones (MTP-67 Monitoring)

### Week 1 (Days 1-7)
- ✅ GSC property verified
- ✅ Sitemaps submitted
- 📊 First indexing wave (50-100 pages)

### Week 2 (Days 8-14)
- 📈 Coverage report shows 200+ pages indexed
- 📊 Crawl stats increasing
- 🔍 First impressions in SERP (brand terms)

### Week 3 (Days 15-21)
- 📈 Most pages indexed (240+/251)
- 📊 Organic traffic visible in GA4
- 🎯 Brand term rankings (top 5)

### Week 4 (Days 22-28)
- ✅ Full indexing (251/251)
- 📈 Category term impressions appearing
- 💬 Zero-click query CTR monitoring

---

## Quality Score Improvement (Google Ads)

### Current Status
- Fulfillment RU Ad Group: QS 0 (no history)
- Impression Share: 64% (limited by budget/QS)

### Expected Improvements (3-5 days)
1. **Fresh content signal** from updated sitemap
2. **Faster indexing** of optimized pages
3. **Better Quality Score** (target: 5-8) due to:
   - Optimized landing page experience
   - Relevant meta descriptions
   - Mobile-responsive design
   - Fast page load times (Astro)

### Verification Steps
1. Google Ads → Ad Groups → "Fulfillment Services RU"
2. Check Quality Score column
3. Track changes daily (will update within 24 hours of GSC indexing)
4. Target: QS 0-3 → 5-8 (within 5 days)

---

## Organic Traffic Monitoring (GA4)

### Setup
1. GA4 is already configured (tracking ID: G-ELBRCEFL41)
2. No additional setup needed

### Metrics to Track
- **Organic users:** Target +5-10 per week
- **Organic sessions:** Should increase with indexing
- **Organic conversions:** Monitor contact form submissions
- **Top organic keywords:** Should include "фулфілмент", "складські послуги"

### Where to Check
1. GA4 → **Acquisition** → **User acquisition**
2. Filter by: **Organic Search**
3. Compare Week 1 vs Week 2-3

---

## Checklist for Manual GSC Work

- [ ] Create GSC account (if not exists)
- [ ] Add property: https://www.fulfillmentmtp.com.ua
- [ ] Verify ownership (HTML file recommended)
- [ ] Submit sitemap-index.xml
- [ ] Set preferred domain (www vs non-www)
- [ ] Set crawl rate if needed (usually "Let Google decide")
- [ ] Enable coverage monitoring
- [ ] Set up search appearance settings
- [ ] Link GA4 account
- [ ] Daily monitoring for 7 days

---

## Post-Launch Monitoring (Recurring)

### Daily (First Week)
- Check GSC Coverage for new indexed pages
- Monitor QS in Google Ads
- Verify no indexing errors

### Weekly (Ongoing)
- Review GSC Coverage report
- Check Crawl Stats
- Monitor organic traffic in GA4
- Track rankings for target keywords

### Monthly (Ongoing)
- Full performance report
- Content update recommendations
- Link building opportunities
- SEO roadmap adjustments

---

## Important URLs

| Resource | URL |
|----------|-----|
| **Site** | https://www.fulfillmentmtp.com.ua |
| **Sitemap Index** | https://www.fulfillmentmtp.com.ua/sitemap-index.xml |
| **Robots.txt** | https://www.fulfillmentmtp.com.ua/robots.txt |
| **llms.txt** | https://www.fulfillmentmtp.com.ua/llms.txt |
| **GSC** | https://search.google.com/search-console/ |
| **Google Ads** | https://ads.google.com/ |
| **GA4** | https://analytics.google.com/ |

---

## Troubleshooting

### "Sitemap could not be found"
- Verify URL is accessible in browser
- Check sitemap-index.xml exists and is valid
- Ensure trailing slash: `.../sitemap-index.xml/` ❌ → `.../sitemap-index.xml` ✅

### "Property verification failed"
- For HTML file: Check file exists in `/public/` and deployed to Vercel
- For DNS: Wait 15 minutes for propagation, then try again
- For meta tag: Clear browser cache and try again

### "Pages not indexing after 3 days"
- Check GSC Coverage for errors (click "Error" tab)
- Verify pages are not blocked by robots.txt
- Check for noindex meta tags
- Request indexing manually (click "Request indexing")

---

**Next Step:** Follow this guide to set up GSC and submit sitemaps. Then monitor Week 1-3 metrics above.

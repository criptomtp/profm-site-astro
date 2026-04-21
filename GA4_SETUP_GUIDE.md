# GA4 Setup Guide for profm.ua
**Objective:** Configure Google Analytics 4 for weekly campaign tracking  
**Timeline:** 30-45 minutes  
**Difficulty:** Beginner-friendly (no coding)

---

## Part 1: Initial GA4 Property Setup

### Step 1: Create GA4 Property (if not exists)
1. Go to [analytics.google.com](https://analytics.google.com)
2. Click **Admin** (gear icon, bottom left)
3. Select your **Account** (MTP Group or similar)
4. Under **Property**, click **Create Property**
5. Fill in:
   - **Property name:** `profm.ua - SEO Campaign`
   - **Industry category:** `Business & Professional Services`
   - **Reporting timezone:** `Europe/Kyiv` (or your local)
   - **Currency:** `UAH`
6. Accept terms → **Create**

### Step 2: Add Data Stream
1. In new GA4 property, go to **Data collection & modification** → **Data streams**
2. Click **Add stream** → **Web**
3. Fill in:
   - **Website URL:** `https://profm.ua` (without trailing slash)
   - **Stream name:** `profm.ua - All Traffic`
4. Click **Create stream**
5. **Copy your Measurement ID** (starts with `G-`). You'll need this.

### Step 3: Install GA4 Tag in Astro Site

In your Astro project, add GA4 tracking code:

**File:** `src/layouts/BaseLayout.astro` (or your main layout)

```astro
---
// Add near top of component script
const GA_ID = 'G-YOUR_MEASUREMENT_ID'; // Replace with your ID
---

<head>
  <!-- Google Analytics -->
  <script is:inline async src=`https://www.googletagmanager.com/gtag/js?id=${GA_ID}`></script>
  <script is:inline define:vars={{GA_ID}}>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', GA_ID);
  </script>
  <!-- End Google Analytics -->
</head>
```

**Verify installation:**
1. Deploy your changes
2. Open [analytics.google.com](https://analytics.google.com) → Your property
3. Go to **Real-time** → **Overview**
4. Visit your site in a new browser tab
5. You should see **1 Active user** within 5 seconds ✅

---

## Part 2: Campaign-Specific Configuration

### Step 4: Create Custom Events (for Outreach Tracking)

**Why:** Track when backlinks drive referral traffic to your guides

**Setup:**

1. Go to **Data collection & modification** → **Events**
2. Click **Create event**
3. **Event name:** `backlink_referral`
4. **Matching conditions:** Add parameter
   - Parameter: `utm_source`
   - Operator: `matches regex`
   - Value: `(shiprob|flexport|3plcenter|logistics)` (update with your actual domains)
5. Click **Create**

Repeat for Batch 2, Batch 3 batches (create separate events or use broad match).

### Step 5: Set Up UTM Tracking for Email Outreach

**Why:** Every outreach email links to a guide with UTM parameters so you can track which outreach batch drives traffic

**Instructions for Outreach Coordinator:**

When sending outreach emails, use this URL format:

```
https://profm.ua/en/guide/[GUIDE-SLUG]?utm_source=[COMPANY]&utm_medium=backlink&utm_campaign=batch_1
```

**Example:**
```
https://profm.ua/en/guide/what-is-3pl/?utm_source=shiprob&utm_medium=backlink&utm_campaign=batch_1
```

**Batch campaigns:**
- **Batch 1:** `utm_campaign=batch_1_week5`
- **Batch 2:** `utm_campaign=batch_2_week6`
- **Batch 3:** `utm_campaign=batch_3_week7`
- **Batch 4:** `utm_campaign=batch_4_week8`

---

## Part 3: Dashboard Configuration

### Step 6: Create Campaign Dashboard

1. Go to **Home** (top left)
2. Click **+ Create** → **New report**
3. Name it: `MTP SEO Campaign - Week 5+`
4. Click **Create**

Now add these 4 cards:

**Card 1: Organic Sessions (Weekly)**
- **Report type:** Line chart
- **Dimensions:** Week
- **Metrics:** Sessions
- **Filter:** Traffic source = organic
- **Date range:** Last 12 weeks

**Card 2: Backlink Referral Traffic**
- **Report type:** Table
- **Dimensions:** Source, Medium
- **Metrics:** Sessions, Conversion rate
- **Filter:** Source contains (shiprob OR flexport OR 3plcenter...) [add your companies]
- **Date range:** Last 12 weeks

**Card 3: Top Performing Guides**
- **Report type:** Table
- **Dimensions:** Page path
- **Metrics:** Sessions, Engagement rate, Avg. session duration
- **Filter:** Page path contains `/en/guide/`
- **Date range:** Last 12 weeks
- **Sort by:** Sessions (descending)

**Card 4: Traffic by Campaign**
- **Report type:** Table
- **Dimensions:** Campaign
- **Metrics:** Sessions, Conversions
- **Filter:** Campaign contains `batch_`
- **Date range:** Last 12 weeks

### Step 7: Create Conversion Goals

1. Go to **Data collection & modification** → **Events**
2. Create custom events for key actions:

**Event 1: Contact Form Submit**
```
Event name: contact_form_submit
Trigger when: User completes contact form
Tracking code: (Add to your form component)
```

**Event 2: Demo Booking**
```
Event name: demo_booking_clicked
Trigger when: User clicks "Book Demo" CTA
```

3. Mark these as **Conversions:**
   - Go to **Data collection & modification** → **Conversions**
   - Toggle ON for `contact_form_submit`
   - Toggle ON for `demo_booking_clicked`

---

## Part 4: Weekly Measurement Routine

### Checklist for Analytics Owner (Fridays, 4:00 PM)

1. **Open GA4 Dashboard** → Your MTP campaign report
2. **Capture these 4 metrics:**
   - Total organic sessions (week-over-week change)
   - Backlink referral sessions (all sources)
   - Top 5 performing guides
   - Form submissions + demo bookings
3. **Fill in tracking spreadsheet** (see MEASUREMENT_DASHBOARD_TEMPLATE.csv)
4. **Screenshot dashboard** (for stakeholder reports)
5. **Check for anomalies:**
   - Session spike? → Investigate source in analytics
   - Traffic drop? → Check if site is indexed, Core Web Vitals stable
   - No backlink traffic? → Confirm UTM parameters in outreach emails

---

## Part 5: Troubleshooting

### "GA4 shows 0 sessions"
- Wait 24 hours after install (GA4 needs time to process)
- Check: Measurement ID is correct (matches in Astro code)
- Check: Site is live (not localhost or staging)
- Verify in **Real-time** → Active users should show immediately

### "Can't see backlink traffic"
- Confirm outreach emails use UTM parameters
- Check: `utm_source` values match your filter criteria
- Wait 24 hours for GA4 to process referral data
- In **Acquisition** → **Sources**, look for custom sources

### "Dashboard showing wrong data"
- Verify filters are correct (check spelling of source names)
- Check date range matches your measurement period
- Ensure events are marked as conversions (if tracking form submits)

---

## Part 6: Integration with Spreadsheet Tracking

**Each Friday, your Analytics Owner will:**

1. Export dashboard metrics from GA4
2. Enter into MEASUREMENT_DASHBOARD_TEMPLATE.csv
3. Calculate week-over-week change
4. Share with team for MEASUREMENT_FRAMEWORK.md monthly analysis

**GA4 Export Steps:**
1. Go to **Custom Reports** (your dashboard)
2. Click any chart → **More options** → **Download data**
3. Save as CSV
4. Paste key metrics into tracking spreadsheet

---

## Quick Links (Save These)

| Tool | URL | Purpose |
|------|-----|---------|
| GA4 Home | https://analytics.google.com | Main dashboard |
| Your Property | [Bookmark after login] | MTP SEO Campaign reports |
| Real-time | https://analytics.google.com → Real-time | Verify tracking working |
| Custom Reports | https://analytics.google.com → Reports | Your MTP campaign dashboard |

---

## Success Criteria

✅ GA4 property created  
✅ Measurement ID copied and installed in Astro  
✅ Real-time shows active users when site is visited  
✅ Campaign dashboard created with 4 cards  
✅ Backlink referral custom event configured  
✅ UTM tracking plan ready for outreach coordinator  
✅ Conversion events marked (contact form, demo booking)  

**Completion time:** 30-45 minutes for new GA4 property setup

**Next step:** Send Measurement ID to SEO Strategist so they can verify tracking before Week 5 outreach launch.

# Campaign Contingencies & Risk Response Playbook
**MTP-71 Organic Growth Campaign**  
**Proactive response strategies for 8 potential failure modes**

---

## Table of Contents
1. Low Outreach Response Rate
2. Slow Organic Traffic Growth
3. Core Web Vitals Regression
4. Link Disavowal or Penalty Risk
5. Team Member Unavailability
6. Internal Site Issues During Campaign
7. Budget Constraints
8. Competitive Pressure / Market Changes

---

## Contingency 1: Low Outreach Response Rate

### Trigger (When to activate)
- **Week 6 response rate <10%** (vs. target 20-30%)
- **Week 7 continuing <15%** (trend worse than expected)

### Root Causes to Investigate
1. **Email quality issue** → Pitches too generic, not compelling
2. **Contact accuracy issue** → Wrong contacts or invalid emails
3. **Timing issue** → Sending at wrong time/day
4. **Subject line weakness** → Not creating curiosity/interest
5. **Outreach velocity** → Sending too many at once (flagged as spam)

### Response Actions (Do This Immediately)

**Day 1: Diagnosis**
- Audit 5 recent non-responses (Gmail → check if opened)
- Review email templates for generic language
- Verify contact names/emails in target list
- Check outreach velocity (are you sending >5 per day?)

**Day 2-3: Adjust & Test**
- **If emails aren't being opened:** Rewrite subject lines with curiosity angle
  - ❌ "Guest Post Opportunity at [Company]"
  - ✅ "Why [Company] readers need this shipping guide"
- **If opened but no response:** Simplify pitch, add credibility
  - Add 1-2 social proof elements ("We've helped 500+ companies...")
  - Reduce ask (offer 1 option instead of 3)
- **If contact is wrong:** Use LinkedIn to find decision-maker for 5 targets
- **If velocity is high:** Slow to 3-5 emails/day instead of 10+

**Day 4-5: Deploy Small Test Batch**
- Send 10 new emails with revised approach
- Monitor for opens/responses over 3 days
- If response rate hits 20%+: Roll out to remaining targets
- If still <10%: Schedule strategy call with manager

**Contingency Success Criteria**
- Week 7-8 response rate ≥15% (recovered from low)
- At least 3-5 responses from test batch of 10

**Fallback Options (If adjustment doesn't work)**

**Option A: Pivot to Community (Medium effort, 1-2 weeks)**
- Launch Reddit strategy: r/fulfillment, r/ecommerce, r/supply_chain
- Daily participation (answer 2-3 questions, share guides contextually)
- Expected: 3-5 links from community mentions
- Timeline: Weeks 8-10 focus
- Trade-off: Lower-quality links but higher volume

**Option B: Expand Unlinked Mention Recovery (Low effort)**
- Use Ahrefs/SEMrush to find 50+ unlinked mentions
- Follow up with OUTREACH_BATCH_4 strategy
- Expected: 5-8 links from mentions
- Timeline: Weeks 7-9
- Trade-off: Easier conversions but smaller audience

**Option C: Guest Post Acceleration (High effort)**
- Shift focus to writing 2-3 original guest posts
- Pitch as "original research" vs. backlink request
- Higher acceptance but more writing work
- Expected: 3-4 high-quality guest post links
- Timeline: Weeks 8-12
- Trade-off: Slower to execute but premium quality

---

## Contingency 2: Slow Organic Traffic Growth

### Trigger (When to activate)
- **Week 8: Only +100 organic sessions** (vs. target +400 by Week 8)
- **No backlink referral traffic visible** (despite links placed)
- **Organic traffic flat for 2+ weeks**

### Root Causes to Investigate
1. **Backlinks haven't passed equity yet** → Normal (lag 2-4 weeks)
2. **Links are low-quality or nofollowed** → Check GSC + Ahrefs
3. **Site isn't indexed** → Check GSC coverage
4. **Rankings haven't improved** → Check average position in GSC
5. **Click-through rate too low** → Meta descriptions or title issues

### Response Actions (Do This Immediately)

**Day 1: Verify Basics**
- [ ] Check GSC → Coverage: Are all guides indexed? (Should be 36/36)
- [ ] Check GSC → Performance: Are organic impressions increasing?
- [ ] Check GA4: Backlink referral traffic via UTM parameters
- [ ] Check Ahrefs/SEMrush: Are backlinks showing in their data? (Can take 1-2 weeks)

**Day 2-3: Investigate Lag**
- Backlinks typically take **7-14 days** to pass equity
- Organic ranking improvements take **2-4 weeks**
- If campaign just started Week 5-6: **This is normal, don't panic**
- Create timeline: "Links acquired Week 6 should boost traffic Week 7-8"

**Day 4-5: Optimize for Quick Wins**
- **Meta descriptions:** Improve CTR on existing rankings
  - Review top 10 keywords in GSC
  - Update descriptions to include keyword + benefit
  - Expected: +20-30% CTR improvement
  
- **Internal linking for featured snippets:** Add structured data to definitions
  - Find high-intent keywords in GSC
  - Add FAQ schema to answer sections
  - Expected: +5-10% impressions from featured snippets

- **Backlink audit:** Are acquired links nofollowed?
  - Check Ahrefs for each link: Dofollow vs. Nofollow
  - If >30% nofollowed: Address with Outreach Coordinator
  - Expected: Shift to only dofollow targets

**Contingency Success Criteria**
- By end of Week 8: 100+ organic sessions (catching up to pace)
- By Week 10: 200+ weekly sessions (on track)
- Backlink referral traffic visible (even if small, 10-20 sessions/week)

**Fallback Options (If traffic stays flat through Week 10)**

**Option A: Accelerate Batch 2-3 Deployment**
- Deploy remaining outreach batches 1 week earlier
- Risk: Might get more rejections (less time between batches)
- Reward: More links sooner = traffic spike sooner

**Option B: Double Down on High-Performers**
- Identify which 5 guides are getting traffic
- Create 2 companion pieces for each (expand cluster)
- Add 10+ internal links between expanded guides
- Expected: Capitalize on momentum in top guides

**Option C: Accelerate AI Visibility Track**
- Launch Medium/Dev.to syndication immediately (Week 8)
- Push Reddit/Quora strategy (Week 8-9)
- Expected: 50-100 AI referral sessions while waiting for SEO lag
- Trade-off: Shifts resources from outreach, but provides growth signal

---

## Contingency 3: Core Web Vitals Regression

### Trigger (When to activate)
- **Mobile PageSpeed drops below 80** (from baseline 85+)
- **LCP increases above 2.5s** (from baseline <2.0s)
- **INP or CLS cross yellow thresholds**

### Root Causes to Investigate
1. **New images added without optimization** → Check image file sizes
2. **JavaScript increased** → Check for render-blocking scripts
3. **Cache expiration** → CDN cache headers misconfigured
4. **Increased traffic** → Overloading server resources
5. **Browser update** → Edge case rendering issue

### Response Actions (Do This Immediately)

**Day 1: Diagnose**
- [ ] Run PageSpeed Insights audit (profm.ua)
- [ ] Check Lighthouse report in Chrome DevTools
- [ ] Compare to baseline metrics (should be saved in MEASUREMENT_DASHBOARD_TEMPLATE.csv)
- [ ] Identify which metric regressed (LCP? INP? CLS?)

**Day 2-3: Quick Fixes** (1-2 hours each)

**If LCP regressed:**
- Compress hero image to <50KB
- Preload critical font
- Defer render-blocking JavaScript
- Expected improvement: +0.5-1.0s faster

**If INP regressed:**
- Check for long JavaScript tasks
- Defer non-critical JavaScript
- Use Web Workers for heavy processing
- Expected improvement: 50-100ms faster response

**If CLS regressed:**
- Add explicit width/height to all images
- Reserve space for ads/dynamic content
- Avoid inserting content above fold
- Expected improvement: CLS <0.05

**Day 4-5: Verify & Monitor**
- Re-run PageSpeed after fixes
- Wait 24 hours for metric refresh
- Monitor weekly (add to Friday checklist)

**Contingency Success Criteria**
- PageSpeed back >85 within 48 hours
- Core Web Vitals all green within 1 week
- No further regression (monitor weekly)

**Fallback Options (If regression persists)**

**Option A: Cache Optimization**
- Increase browser cache expiration
- Implement service worker caching
- Expected: 0.3-0.7s improvement
- Effort: 2-4 hours

**Option B: Image CDN / Lazy Loading**
- Implement Cloudflare Image Optimization
- Lazy load all below-fold images
- Expected: 20-30% image size reduction
- Effort: 4-6 hours

**Option C: Accept Performance Trade-off**
- Add 1 new tracking script or CMS
- Expected impact: 0.2-0.5s LCP increase
- Mitigation: Other optimizations offset loss
- Decision: Manager approval required

---

## Contingency 4: Link Disavowal, Penalty, or Low-Quality Links

### Trigger (When to activate)
- **Google Search Console penalty notification** (manual action)
- **Rankings drop >50% in 1-2 days** (possible algorithm update or penalty)
- **Ahrefs detects toxic links** (comment spam, PBN networks)
- **More than 10% of links are nofollowed**

### Root Causes to Investigate
1. **Links from spammy/low-quality sources** → Outreach Coordinator acquired from wrong targets
2. **Unnatural link pattern** → Too many from same domain/IP range
3. **Over-optimized anchor text** → Too many exact-match keywords
4. **Paid links reported** → Someone flagged links as paid
5. **Site-wide links from temporary partner** → Partner site later penalized

### Response Actions (Do This Immediately)

**Day 1: Verify Penalty Status**
- [ ] Check Google Search Console → Manual actions (any messages?)
- [ ] Check Search Console → Overview (traffic dropped?)
- [ ] Run Ahrefs backlink audit (are new links indexed?)
- [ ] Check rank tracking for top 10 keywords (any drops?)

**If penalty confirmed:**
- [ ] Create "Disavow file" (list of bad links)
- [ ] Use Google Search Console → Disavow tool
- [ ] Upload file (format: one domain per line)
- [ ] Request reconsideration in GSC
- [ ] Monitor for manual action removal (usually 1-2 weeks)

**If no penalty but quality concern:**
- [ ] Audit all links acquired (check domain authority + relevance)
- [ ] Flag questionable links to Outreach Coordinator
- [ ] Disavow links with DA <15 or off-topic
- [ ] Request removal from 5-10 lowest quality sources
- [ ] Shift to only Tier 1-2 targets going forward

**Day 2-3: Preventative Actions**
- [ ] Review Outreach Batch 2-3-4 targets (are they legitimate?)
- [ ] Add quality screening to outreach process
- [ ] Verify no paid links in current pipeline
- [ ] Check competitor links in Ahrefs (are they similar quality?)

**Contingency Success Criteria**
- Manual action removed (if one existed)
- Zero toxic links going forward
- 90%+ of links from DA 20+ sources
- Links with natural/varied anchor text

**Fallback Options (If penalty severe and long-term)**

**Option A: Pivot to Guest Posts Only**
- Stop requesting backlinks from questionable sources
- Focus on high-quality guest post links only
- Expected: Slower growth but zero risk
- Timeline: Extended to 12+ weeks

**Option B: Brand Mention Strategy**
- Shift from direct link requests to brand mentions
- Get quality links naturally over time
- Supplement with podcast/video interviews (harder to penalize)
- Timeline: Slower (3-4 months) but safer

**Option C: Accept Reduced KPIs**
- Lower target from 35+ backlinks to 20+ backlinks
- Focus on quality over quantity
- Adjust revenue projections accordingly
- Manager approval required

---

## Contingency 5: Key Team Member Unavailable

### Trigger (When to activate)
- **Outreach Coordinator resigns/gets sick** → 2+ week absence
- **Technical Lead unavailable** → During Week 4 (critical timing)
- **Analytics Owner unavailable** → Can't measure campaign

### Response Actions (Do This Immediately)

**If Outreach Coordinator is unavailable:**
- [ ] Manager takes over outreach emails for week(s)
- [ ] Pause new outreach, focus on follow-ups
- [ ] Freelancer/agency hired within 48 hours (Upwork, Reddit r/forhire)
- [ ] Backup person briefed on TEAM_ONBOARDING_PACKETS.md
- **Expected delay:** 1-2 weeks, extends campaign by 1-2 weeks total

**If Technical Lead is unavailable (Week 4 especially critical):**
- [ ] Manager or external contractor implements changes immediately
- [ ] Use QUICK_START_EXECUTION_GUIDE.md for day-by-day tasks
- [ ] All code templates ready in IMPLEMENTATION_TEMPLATES.md (no thinking required)
- **Expected delay:** 1 week max, implement week 5 instead
- **Risk:** Week 4 optimizations critical → consider delaying campaign 1 week

**If Analytics Owner is unavailable:**
- [ ] Manager covers weekly metric collection (simpler task)
- [ ] Monthly reports delayed but tracked
- [ ] Outsource report writing to freelancer ($200-300/week)
- **Expected delay:** Reports 3-5 days late, doesn't impact execution

### Contingency Success Criteria
- Replacement hired within 48 hours (if permanent departure)
- No >2 week gaps in outreach (core campaign work)
- Weekly metrics collected consistently

---

## Contingency 6: Internal Site Issues During Campaign

### Trigger (When to activate)
- **Site goes down for >4 hours** (breaks campaign at critical moment)
- **Deployment breaks internal links** (regression after Week 4 work)
- **Indexing issue** (pages removed from index mid-campaign)
- **SSL/HTTPS issue** (site serves mixed content)

### Response Actions (Do This Immediately)

**If site down:**
- [ ] Rollback to last known good version
- [ ] Check uptime monitoring tool (UptimeRobot)
- [ ] Notify manager + stakeholders of downtime
- [ ] Pause outreach if down >4 hours (wait until recovery)
- [ ] Resume outreach once confirmed stable
- Expected impact: 12-24 hour delay, minimal KPI impact

**If internal links broken:**
- [ ] Use link checker tool to find all broken links
- [ ] Fix broken links within 24 hours
- [ ] Test after deployment
- [ ] Check GSC for crawl errors
- Expected impact: 1-2 days to fix, minimal KPI impact

**If indexing issue:**
- [ ] Check GSC → Coverage (how many pages indexed?)
- [ ] If <36 guides indexed: Request re-indexing in GSC
- [ ] Check for accidental noindex tags
- [ ] Verify sitemap correct
- [ ] Wait 5-7 days for Google to re-index
- Expected impact: 1-2 week delay in traffic from new links

**If SSL/HTTPS issue:**
- [ ] Check site with SSL checker tool
- [ ] Fix certificate or redirect issues
- [ ] Clear cache if needed
- [ ] Verify all links use HTTPS
- Expected impact: Minimal if fixed quickly (<24 hours)

### Contingency Success Criteria
- Site stable within 24 hours
- All pages properly indexed (36/36 in GSC)
- Zero SSL/HTTPS issues
- Links working (0 broken links)

---

## Contingency 7: Budget Constraints / Funding Cut

### Trigger (When to activate)
- **Budget reduced by 30%+** (from $10k-15k to $7k or less)
- **Tools cancelled** (SEMrush/Ahrefs subscription)
- **Team reduced** (can't afford full-time outreach coordinator)

### Response Actions (Do This Immediately)

**If total budget cut to $7k-9k:**
- Cut optional tools: Keep GA4 + GSC (free), cut SEMrush/Ahrefs
- Prioritize: Link building (highest ROI) over syndication
- Reduce team: 1 part-time coordinator instead of full-time
- Expected impact: Slower backlink acquisition, delayed timeline
- New target: 25-30 backlinks (vs. original 35+)

**If specific tools cancelled:**
- Replace SEMrush with free alternatives (Google Search Console, SERP tracking)
- Use free backlink tools (Backlink Checker, Free Backlink Tools)
- Loss of convenience but not capability
- Expected impact: +2-3 hours/week research time, same results

**If team scaled back to part-time:**
- Reduce outreach to 20 targets (Batch 1-2 only, drop Batch 3-4)
- Extend timeline to 14-16 weeks instead of 9 weeks
- Focus on highest-quality targets (higher conversion = fewer emails)
- Expected target: 20-25 backlinks, +1,500-2,500 sessions

**If campaign must pause entirely:**
- All documentation preserved (no work wasted)
- Restart when budget available (4-6 weeks or later)
- Targets remain valid (seasonality not major factor)
- Expected: 1-2 month delay, campaign effectiveness unchanged

### Contingency Success Criteria
- Campaign continues in some form (don't abandon)
- Adjusted KPIs communicated to stakeholders
- Modified timeline confirmed

---

## Contingency 8: Competitive Pressure / Market Changes

### Trigger (When to activate)
- **Competitor launches similar campaign** (targeting same links)
- **Market shifts** (economic downturn, industry change)
- **Algorithm update** (Google changes ranking factors)

### Response Actions (Do This Immediately)

**If competitor launches similar campaign:**
- [ ] Shift to targets they haven't contacted yet (Batch 3-4)
- [ ] Improve pitch quality to win head-to-head
- [ ] Prioritize highest-quality targets first
- [ ] Consider guest post strategy (less competitive)
- Expected impact: Slightly harder to win links, but achievable

**If market shifts negatively:**
- [ ] Adjust content to address new market conditions
- [ ] Refresh guides with updated information
- [ ] Highlight how MTP helps in new market reality
- [ ] Use in outreach as "timely expert resource"
- Expected impact: May increase interest (relevance boost)

**If algorithm update hurts rankings:**
- [ ] Audit guide content for E-E-A-T signals
- [ ] Add author credentials (Founder bio)
- [ ] Add more internal linking to establish topical authority
- [ ] Consider expanding to 40+ guides (vs. 36)
- Expected impact: Recovery takes 2-4 weeks, no campaign changes

### Contingency Success Criteria
- Continue steady progress toward targets
- Adapt messaging to market conditions
- Monitor competitive landscape weekly

---

## Decision Tree: When to Escalate

```
Is campaign on pace? (35+ backlinks by Week 12, +2,500 sessions by Month 3)

YES → Keep executing, monitor weekly
NO → Does one of 8 contingencies apply?

- Low response rate? → Contingency 1
- Slow traffic? → Contingency 2
- CWV regression? → Contingency 3
- Link quality issue? → Contingency 4
- Team unavailable? → Contingency 5
- Site issue? → Contingency 6
- Budget cut? → Contingency 7
- Competition/market? → Contingency 8

APPLY contingency response immediately
MONITOR for 7 days
ASSESS: Did adjustment work?

YES → Resume normal execution
NO → Escalate to manager, consider fallback option
```

---

## Red Flags Summary (Act Immediately)

| Red Flag | Action | Timeline |
|----------|--------|----------|
| Response rate <10% for 2 weeks | Test new pitch, adjust messaging | Days 1-3 |
| Traffic flat through Week 10 | Accelerate outreach, optimize for snippets | Days 1-5 |
| PageSpeed <80 | Fix images/JS, optimization | Days 1-3 |
| Google penalty | Disavow bad links, request reconsideration | Days 1-2 |
| Team member absent 2+ weeks | Hire replacement, pause if critical | Days 1-2 |
| Site down >4 hours | Investigate, fix, resume carefully | Days 1-1 |
| Budget cut 30%+ | Reduce scope, communicate new targets | Days 1-5 |
| Competitor wins your target | Shift to other targets, improve pitch | Days 1-3 |

---

## Key Principle

**No contingency is a campaign killer.** Every failure mode has a response strategy that either:
1. Gets campaign back on track, or
2. Reduces scope to achievable targets, or
3. Extends timeline but maintains ROI

**Manager approval is required for ANY major change** (budget reduction, timeline extension, KPI adjustment).

**Weekly monitoring catches problems early** → Response is faster and simpler.

# AI Crawler Strategy: MTP Group Fulfillment

## Current Policy: ALLOW ALL AI CRAWLERS ✅

**Decision:** Allow all known AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Bytespider, Google-Extended, etc.) to access MTP Group content for training and citation.

**Implementation:**
```
# robots.txt - Current (Allow All AI)
User-Agent: *
Allow: /
Disallow: /admin/
Disallow: /thanks/
# ... additional disallows
```

---

## Rationale: Why We Allow AI Crawlers

### Business Benefits

1. **Brand Awareness**
   - MTP Group mentioned in ChatGPT, Claude, Perplexity responses
   - Example: User asks "What's the best fulfillment provider for office supplies?"
   - MTP appears in AI-generated comparison/recommendation
   - Direct benefit: Referral traffic, brand mention volume

2. **Authority Building**
   - More AI citations → higher perceived authority in fulfillment category
   - AI systems preferentially cite recognized, cited sources
   - Positive feedback loop: more citations → higher rankings → more citations

3. **Market Position**
   - Niche B2B market (fulfillment is specialized)
   - AI systems often cite small number of authoritative sources per query
   - Being cited by OpenAI/Google/Anthropic validates industry leadership

4. **No Sensitive Data Risk**
   - Pricing is public (visible on website anyway)
   - No customer data on public pages (PII protected)
   - No proprietary business methods exposed
   - Standard B2B marketing content

### Comparison: Restrict vs. Allow

| Factor | Restrict AI | Allow AI |
|--------|------------|----------|
| Training citations | No | Yes ✓ |
| ChatGPT browsing | Still yes | Yes ✓ |
| ChatGPT/Claude training | Blocked | Allowed ✓ |
| Brand mentions in Copilot | Maybe fewer | More ✓ |
| Referral traffic from AI | Low | High ✓ |
| Adoption complexity | High (multi-crawler) | Low ✓ |
| Legal/compliance | Same | Same |

**Conclusion:** Allowing AI crawlers is net positive for MTP with zero downside.

---

## Known AI Crawlers (As of April 2026)

### Search + Training (Recommend: ALLOW)

| Crawler | Company | robots.txt token | Purpose | Status |
|---------|---------|------------------|---------|--------|
| GPTBot | OpenAI | `GPTBot` | ChatGPT training | ✅ Allowed |
| ChatGPT-User | OpenAI | `ChatGPT-User` | Real-time browsing | ✅ Allowed |
| ClaudeBot | Anthropic | `ClaudeBot` | Claude training | ✅ Allowed |
| PerplexityBot | Perplexity | `PerplexityBot` | Search + training | ✅ Allowed |
| Bytespider | ByteDance | `Bytespider` | Training | ✅ Allowed |
| Google-Extended | Google | `Google-Extended` | Gemini training* | ✅ Allowed |
| CCBot | Common Crawl | `CCBot` | Open dataset | ✅ Allowed |
| Googlebot | Google | `Googlebot` | Search indexing | ✅ Allowed (critical) |

*Note: Google-Extended does NOT affect Google Search or AI Overviews—that uses regular Googlebot.

---

## Alternative Strategies (If Needed)

### Option 1: Block Training, Allow Citation (Hybrid)

**Use case:** Protect training but benefit from citations.

```
# Block AI model training
User-Agent: GPTBot
Disallow: /

User-Agent: Google-Extended
Disallow: /

User-Agent: Bytespider
Disallow: /

# Allow citation crawlers
User-Agent: ChatGPT-User
Allow: /

User-Agent: *
Allow: /
```

**Result:**
- ❌ Won't be used for GPT training
- ✅ ChatGPT can still cite via browsing
- ⚠️ More complex, harder to maintain
- ⚠️ Google may reduce visibility (Google-Extended is separate from search)

### Option 2: Block ALL AI (Restrictive)

**Use case:** Maximum privacy, no AI usage.

```
User-Agent: GPTBot
Disallow: /

User-Agent: ChatGPT-User
Disallow: /

User-Agent: ClaudeBot
Disallow: /

User-Agent: PerplexityBot
Disallow: /

User-Agent: Bytespider
Disallow: /

User-Agent: Google-Extended
Disallow: /

User-Agent: *
Allow: /
```

**Result:**
- ❌ Zero AI visibility
- ❌ No ChatGPT citations possible
- ⚠️ Not recommended for B2B businesses
- ✅ Maximum control

---

## Monitoring AI Visibility

### Tools to Track AI Citations

1. **Google Search Console** (Free)
   - Monitor click-through from "Google AI Overviews"
   - Check appearance in AI Overviews results
   - Trend: Growing traffic source

2. **Perplexity Analytics** (Free, requires account)
   - Track mentions in Perplexity search results
   - See what queries pull your content
   - Referral traffic dashboard

3. **ChatGPT Web Crawler Analysis** (Manual)
   - Test queries in ChatGPT
   - See if MTP is cited for fulfillment queries
   - Screenshot for documentation

4. **Ahrefs/Semrush** (Paid)
   - Track "citations" vs traditional backlinks
   - Monitor AI visibility alongside organic rankings
   - Trend analysis over time

### Monthly Checklist

- [ ] Check GSC for AI Overview traffic (if applicable to your region)
- [ ] Test 5-10 fulfillment-related queries in ChatGPT
- [ ] Document any MTP mentions (screenshot for records)
- [ ] Check Perplexity search results for similar queries
- [ ] Note any new AI citation sources

---

## Decision Log

**Date:** April 17, 2026  
**Decision:** Allow all AI crawlers  
**Rationale:** B2B fulfillment niche benefits from AI visibility; no data sensitivity; positive ROI from brand mentions and referral traffic  
**Implementation:** No robots.txt changes needed (current = allow all)  
**Review date:** July 17, 2026 (quarterly review)

---

## Future Considerations

### What Might Change This Decision?

1. **Legal/Regulatory:**
   - EU AI regulations (currently no impact)
   - Copyright legislation (may require opt-in)
   - Would review if new regulations emerge

2. **Competitive:**
   - If major competitors block AI crawlers
   - If AI citations significantly reduce organic traffic (unlikely)
   - If AI platforms feature competitor vs MTP

3. **Market Shift:**
   - If fulfillment becomes commoditized
   - If price sensitivity increases
   - Would reconsider around 2027 once market matures

**Current decision: Maintain "allow all" through at least 2026 Q3**

---

## Implementation

**Current robots.txt: ✅ Correct**  
No changes needed. All AI crawlers are welcomed.

**If you want to make explicit (for clarity):**
```
# AI Crawler Policy: ALLOWED
# - GPTBot, ClaudeBot, PerplexityBot, Bytespider (allow training)
# - ChatGPT-User, Googlebot (allow search/citations)
# See docs/AI-CRAWLER-STRATEGY.md for rationale

User-Agent: *
Allow: /
```

---

## FAQ

**Q: Will blocking AI crawlers hurt my rankings?**  
A: No. Google Search uses `Googlebot`, not `Google-Extended`. Blocking Google-Extended only prevents Gemini training.

**Q: Can I block GPTBot but allow ChatGPT-User?**  
A: Yes, but hybrid approaches are complex. Our recommendation: allow both.

**Q: What if AI training uses my content without permission?**  
A: Standard behavior. They're citing sources in citations. Treat like traditional backlinks.

**Q: Should I use robots.txt or META noindex?**  
A: robots.txt. Cleaner, applies site-wide. META is page-level.

**Q: Can I block just one AI company (e.g., only GPTBot)?**  
A: Yes, but not recommended. Creates fragmentation. Better to allow all or block all.

---

## Resources

- [robots.txt documentation](https://developers.google.com/search/docs/beginner/robots-txt)
- [Google Search Central guidance](https://developers.google.com/search)
- [Schema.org for AI discoverability](https://schema.org/BreadcrumbList)
- [OpenAI crawler documentation](https://platform.openai.com/docs/guides/web-crawl)

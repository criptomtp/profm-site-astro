# Security debt remediation — 2026-05-03

Source: Cloudflare Security Insights export
(`Cloudflare_Criptomtp@gmail.com's Account_SecurityInsights_20260503_1202.csv`).

5 of 6 reported items remain (Security.txt was already fixed earlier today —
commit `~present at /public/.well-known/security.txt`).

All 5 are CF dashboard / DNS toggles. The CF API token in `.env.local` is
read-only for DNS, so these need to be done manually OR the token needs
Zone:DNS:Edit scope added.

Run `python3 scripts/security-verify.py` after each change to confirm.

---

## 1. DMARC record — add reporting URI [Low] [DNS]

**Current:** `v=DMARC1; p=none;` — minimal valid record, but no `rua=`
reporting URI means we receive zero DMARC feedback. Cloudflare flags this
as "DMARC Record Error" because it's blind monitoring.

**Recommended new value:**
```
v=DMARC1; p=none; rua=mailto:mtpgrouppromo@gmail.com; sp=none; aspf=r; adkim=r; fo=1; pct=100
```

What this does:
- `p=none` — keep monitor-only mode (no quarantine/reject yet — safe)
- `rua=mailto:...@gmail.com` — receive aggregate DMARC reports daily
- `sp=none` — explicit subdomain policy (matches main policy)
- `aspf=r adkim=r` — relaxed alignment (matches normal email behavior)
- `fo=1` — generate failure reports if any auth method fails (helpful diagnostics)
- `pct=100` — apply policy to 100% of mail

**Caveat on rua=mailto:gmail.com:** Per RFC 7489, the receiving domain
(gmail.com) should publish a `_report._dmarc.gmail.com` authorization
record for fulfillmentmtp.com.ua. Gmail does not publish this. In practice
most major ISPs (Microsoft, Mail.ru, Yahoo) ignore the cross-domain check
and send reports anyway. If reports don't arrive in 7 days, switch to
free service like dmarcian.com.

**Path to update (CF Dashboard):**
1. Cloudflare Dashboard → fulfillmentmtp.com.ua → DNS → Records
2. Find TXT record with name `_dmarc` (current content: `"v=DMARC1; p=none;"`)
3. Click Edit → paste new value above → Save
4. TTL: leave at Auto (1)

**Verify after save:**
```bash
dig +short TXT _dmarc.fulfillmentmtp.com.ua
# Should output the new full string within 60 seconds
```

**Migration roadmap (do later, only after 30 days of clean monitor data):**
- Day 30: switch to `p=quarantine; pct=10` (10% of failed mail goes to spam)
- Day 60: `p=quarantine; pct=50`
- Day 90: `p=quarantine; pct=100`
- Day 120: `p=reject; pct=100` (failed mail bounces — strongest protection
  but only do this after confirming 30+ days of zero legitimate failures)

---

## 2. Bot Fight Mode — enable [Moderate] [Dashboard toggle]

**Current:** Disabled. Bots and scrapers hit origin without challenge.

**What it does:** CF's free bot detection challenges suspected bots
(headless browsers, known bot signatures, datacenter IPs). Requests
challenged are labeled "Bot Fight Mode" in Security → Events.

**Risk:** Some legitimate automation (uptime monitors, crawler-driven
SEO tools, GA4 server-side, your own scripts) MAY get challenged. CF's
default rules are conservative. The fix if false positives appear: add
the IP/UA to a Page Rule allowlist.

**Path to enable (CF Dashboard):**
1. fulfillmentmtp.com.ua → Security → Bots
2. Toggle "Bot Fight Mode" to ON

**Verify:**
- Security → Events should start showing "Bot Fight Mode" labeled requests
  within 24 hours.
- Watch GSC Coverage report for 7 days — Googlebot is whitelisted by CF
  but verify no "Crawl errors" spike.

---

## 3. Block AI bots — enable [Moderate] [Dashboard toggle]

**Current:** AI training crawlers (GPTBot, ClaudeBot, Bytespider, etc.)
can scrape full site content for model training without restriction.

**What it does:** Blocks the well-known AI training crawlers at the edge.
Your content stops feeding into models like GPT-5, Claude, Gemini training
sets without compensation.

**Risk:** None for SEO — Googlebot, Bingbot, Yandex are NOT affected,
they're ranking crawlers not training crawlers. AI Overviews citations
may decrease over time as models stop seeing fresh content from us.

**Trade-off to think about:** Blocking AI training reduces our presence
in AI search responses (ChatGPT, Perplexity, Claude search) over the
long run. For an SEO/content business this is a real loss. Consider
NOT blocking if AI search is part of the strategy.

**Recommendation:** **Don't enable this one.** Per `docs/AI_VISIBILITY_OPTIMIZATION.md`
and the dual-md generation work we did, we're explicitly courting AI
crawlers for citation visibility. Blocking GPTBot/ClaudeBot would
contradict that strategy.

If you disagree and want to block: Security → Bots → "Block AI bots" toggle.

---

## 4. AI Labyrinth — enable [Low] [Dashboard toggle]

**Current:** Disabled. Unwanted AI bots that bypass robots.txt see real
content.

**What it does:** Serves AI scrapers a maze of AI-generated decoy pages
instead of your real content. Disrupts training data quality without
blocking outright.

**Recommendation:** Same as #3 — **don't enable** if AI search citation
is part of the strategy. AI Labyrinth doesn't distinguish between
"good" AI crawlers (citing us in answers) and "bad" ones (training
without attribution). Both get the maze.

---

## 5. Skip rules review [Moderate] [Dashboard]

**What's flagged:** CF security rules with action="skip" bypass other
security checks. Each skip rule is a potential hole in the security
posture.

**Path to review:** Security → WAF → Custom rules. Filter by
Action: Skip.

**For each skip rule, decide:**
- Is the source still trusted? (e.g. Vercel deploy webhook IPs from before
  the CF Pages migration — likely stale)
- Can we replace `skip` with a narrower action like `bypass specific check`
  rather than all checks?
- Can we delete the rule entirely?

Most likely candidates to remove (legacy from Vercel era):
- Any rule whitelisting Vercel build IPs
- Any rule whitelisting old CI/CD endpoints

---

## How to grant the CF token DNS Edit scope (optional)

If you want me to apply DMARC and future DNS changes via API:

1. Cloudflare Dashboard → My Profile → API Tokens
2. Find the existing token (likely "Cache Purge" or similar) → Edit
3. Under Permissions, add: `Zone — DNS — Edit` (scope: fulfillmentmtp.com.ua only)
4. Save

Then I can run DMARC/DNS updates with `bash scripts/cf-api/update-dmarc.sh`.

---

## Verification

After making the changes above, run:
```bash
python3 scripts/security-verify.py
```

Will check:
- DMARC record has rua= field
- SPF still present
- Live site responds 200
- Security.txt still served
- Headers expected from CF (cf-cache-status etc.)

Output: pass/fail per item with current values.

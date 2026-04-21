# GSC Coverage Drilldown — 2026-04-21 (drop #3)

**Issue type:** "Копія. Система Google вибрала іншу канонічну сторінку, ніж користувач"
(Duplicate — Google chose a different canonical than user)
**Count:** 4 URLs, snapshot date 2026-04-17
**Source:** `fulfillmentmtp.com.ua-Coverage-D2rilldown-2026-04-21.zip`

## What this status means

The page declares itself canonical (`<link rel="canonical" href="self">`). Google crawled it, compared it to siblings, and decided a DIFFERENT URL better represents this content — so the user-declared canonical is overruled. The RU page is still crawled but not ranked independently; Google serves the UA version for RU queries too.

This is a **content uniqueness** problem, not a technical hreflang problem.

## Affected URLs

| URL | Last scan | Status | Canonical | Root cause |
|---|---|---|---|---|
| `/ru/recalls/` | 2026-04-18 | 200 | self ✅ | RU too similar to UA |
| `/ru/about/` | 2026-04-15 | 200 | self ✅ | RU too similar to UA |
| `/ru/guide/` | 2026-04-15 | 200 | self ✅ | RU too similar to UA |
| `/ua/blog/tpost/lgl2mu2gb1-...` | 2026-04-10 | 301 | n/a | Tilda legacy, 301 → `/ua/blog/` |

## Technical check ✅

All 3 RU pages pass technical hygiene:
- HTTP 200, `<html lang="ru">`
- `<link rel="canonical" href="https://www.fulfillmentmtp.com.ua/ru/{slug}/">` — self-referential
- Hreflang cluster complete: `uk` → `/ua/{slug}/`, `ru` → `/ru/{slug}/` (self), `en` → `/en/{slug}/`, `x-default` → `/ua/{slug}/`
- All 9 siblings (3 slugs × 3 langs) return 200
- No redirect chain, no robots block

The technical setup is correct. Google is overruling on content similarity.

## Root cause — content is too close to UA

All 3 RU pages were likely produced as near-translations of the UA original:

| Page | UA words | RU words | Δ |
|---|---|---|---|
| `about` | 1519 | 2391 | +57% |
| `recalls` | 1575 | 2044 | +30% |
| `guide` | 1833 | 2226 | +21% |

Word count is different, but **semantic fingerprint** (entities, claims, sequence of ideas) is the same. Google's duplicate detection is semantic, not lexical. When RU is a reworded UA, Google picks one URL to represent the cluster — usually x-default (UA).

This contradicts the project's "three audiences" policy in `CLAUDE.md`:

> UA / RU / EN: різний кут атаки, різна структура, різні візуальні рішення — НЕ переклади

These 3 RU pages are translations, not divergent angles.

## The 4th URL — Tilda legacy

`/ua/blog/tpost/lgl2mu2gb1-yak-vibrati-fulflment-operatora-v-ukran/` returns 301 → `/ua/blog/` via `vercel.json` wildcard. Google still lists it because the sitemap (or old backlinks) references it. Will age out. No fix needed.

## Recommended fix

### Option A (recommended) — rewrite the 3 RU pages with a different angle

Per the "three audiences" policy. RU target audience = СНД бізнес (Казахстан, Молдова, Грузія, Грузія) + рускомовні України. Different entities, different concerns:

**`/ru/about/`** — reposition from "history of MTP" to "Why Ukraine fulfillment for CIS brands entering Ukrainian market":
- Lead with war-resilient operations (blackouts, generators, OTIF 99.8% in 2022)
- Case studies: CIS sellers expanding to Ukraine via MTP
- Different H2 sequence: not chronicle → but credential stack

**`/ru/recalls/`** — reposition from "owner video interviews" to "proof stack for CIS decision makers":
- Lead with OTIF metrics per client
- Add "Why Ukrainian fulfillment beats self-ops from Astana/Tbilisi"
- Keep videos, but change the framing around each

**`/ru/guide/`** — reposition from "should I switch to 3PL" (Ukrainian owner POV) to "How a CIS brand onboards with a Ukrainian 3PL":
- Different 7 steps: visa, customs, registration, language, CRM integration, pricing in local currency, first shipment
- Different red flags (currency risk, cross-border, sanctions compliance)
- This becomes genuinely unique content, not a translation

Target: change ≥40% of semantic content per page (new H2/H3 sequence, new entities, new claims). Word count can stay.

### Option B (heavy) — delete RU versions, redirect to UA

If we don't have bandwidth to rewrite with a CIS angle, delete these 3 RU pages and 301 → UA equivalents. Loses RU traffic, but stops fighting Google's dedup. Not recommended while RU traffic from СНД still has business value.

### Option C (wait) — do nothing

Google's decision is "UA is canonical for this cluster". RU pages still serve as hreflang signal. If we don't care about RU showing up in SERPs independently, leave as-is. RU users still see RU content via `html lang` and hreflang. They just can't land on RU via a direct search snippet.

## Recommendation

**Option A for `/ru/about/` first** — it's the highest-value page for СНД trust-building. Rewrite with CIS-entry angle over 2-3 days. Re-check in 14 days.
If Google accepts the rewrite as distinct, do `/ru/guide/` and `/ru/recalls/` next.
If Google still overrules, fall back to Option C for the other two.

## Deliverables

- [x] `docs/gsc/2026-04-21_coverage-duplicate-google-canonical.md` (this file)
- [ ] Rewrite `/ru/about/` with CIS-entry angle
- [ ] Re-check GSC in 14 days after rewrite
- [ ] Decide Option A vs C for `/ru/guide/` and `/ru/recalls/`

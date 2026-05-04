# Keyword Strategy Protocol — Pipeline Step 1.5

Reference document for `keyword-strategist` agent and downstream consumers (WRITER, DESIGN, KEYWORD-AUDIT).

Created 2026-05-04 to formalize the SEO-first discipline that earlier pipeline runs lacked.

---

## Why this step exists

Without explicit keyword targets, the pipeline produced pages with good topical content but no clear ranking goal. Pages would rank for unintended queries, miss intended ones, and downstream optimization became reactive rather than designed.

KEYWORD-STRATEGIST converts competitor research + semantic core + GSC data into a formal contract: which exact queries the page must rank for, how downstream steps must accommodate them.

---

## Output schema

`.claude-flow/research/[slug]-keywords.json`:

```json
{
  "slug": "<slug>",
  "topic": "<one-line description>",
  "keyword_strategy_date": "YYYY-MM-DD",
  "current_gsc_state": {
    "[topic]_related_impressions_90d": <number>,
    "note": "<context>"
  },
  "ua": {
    "url_slug": "<slug>",
    "primary": [
      {
        "q": "фулфілмент книги",
        "volume_est": "50-200",
        "intent": "commercial-head",
        "target_pos": 5,
        "target_60d": true,
        "must_appear_in": ["url", "title", "h1", "lede", "schema", "≥3 body"]
      }
    ],
    "secondary": [
      {"q": "ISBN облік склад", "target_pos": 25}
    ],
    "long_tail": ["скільки коштує фулфілмент для видавництва", ...],
    "negative": [
      {"q": "купити книги", "reason": "Consumer intent, Yakaboo terrain"}
    ]
  },
  "ru": { ... same shape ... },
  "en": { ... same shape ... },
  "cannibalization_check": {
    "potential_conflicts": [
      {
        "page": "/ua/fulfilment-dlya-internet-magazynu/",
        "conflict_q": "склад для інтернет-магазину",
        "resolution": "Differentiate by specificity..."
      }
    ],
    "internal_linking_strategy": {
      "links_to_create_from_other_pages_to_new": [
        {"from_page": "/", "anchor": "фулфілмент для книжок", "context": "у списку категорій"}
      ],
      "links_from_new_page_to_other_pages": [
        {"to_page": "/ua/tsiny/", "anchor": "детальні тарифи", "context": "у pricing section"}
      ]
    }
  },
  "serp_features": {
    "ua": {
      "featured_snippet_target": {
        "query": "як організована логістика для видавництва",
        "format": "step-list of 8 process steps",
        "page_section": "How It Works section з 8 numbered steps"
      },
      "ai_overview_target": {
        "query": "скільки коштує фулфілмент для видавництва",
        "format": "concise pricing answer with anchor numbers",
        "page_section": "Pricing section з conversational FAQ-style answer"
      },
      "people_also_ask": [
        "Що таке ISBN облік на складі",
        "Чи можна self-publish тираж від 50 примірників"
      ]
    },
    "ru": { ... },
    "en": { ... }
  },
  "downstream_constraint_rules": {
    "url_slug": "EXACT match for 1 primary keyword (highest volume)",
    "title_50_60_chars": "Primary keyword in first 30 chars + USP/hook",
    "meta_description_150_160": "Primary + 1-2 secondary + CTA",
    "h1": "Primary keyword (exact or close variant) + brand-hook twist",
    "h2_sections": "8-12 H2s, each with 1 primary or secondary keyword",
    "lede_first_paragraph": "Primary keyword in first 50 words",
    "schema_name_description": "Primary keyword present",
    "image_alt_text": "≥3 alt texts include secondary keywords",
    "internal_links": "≥5 internal links with secondary keywords as anchor text",
    "faq_questions": "≥3 FAQ items use long-tail keywords as question structure",
    "keyword_density": "primary 0.5-2.5%, secondary 0.3-1%",
    "negative_keywords": "MUST NOT appear in title/h1/h2/meta/schema. May appear in body only for contrast."
  },
  "post_deploy_tracking": {
    "scheduled_check_t_plus_14d": "YYYY-MM-DD",
    "scheduled_check_t_plus_30d": "YYYY-MM-DD",
    "scheduled_check_t_plus_60d": "YYYY-MM-DD",
    "metrics_to_pull": [
      "Position for each primary keyword",
      "Position for each secondary keyword",
      "Total impressions for the URL",
      "Total clicks for the URL",
      "Unexpected queries we ranked for (add to strategy if material)",
      "Negative queries we accidentally ranked for (assess intervention need)"
    ]
  }
}
```

---

## Tier definitions

| Tier | Count per lang | Target position | Target window | Must appear in |
|---|---:|---|---|---|
| Primary | 3-5 | top-10 (5-10 ideal) | 60 days | URL, title, H1, lede, schema, ≥3 body |
| Secondary | 8-12 | top-30 | 90 days | ≥1 H2, ≥2 body |
| Long-tail | 15-20 | top-50 | 90 days | ≥3 as FAQ questions |
| Negative | 3-5 | NOT ranking | — | NEVER in title/H1/H2/meta/schema |

---

## Downstream constraint enforcement

**WRITER step (4):**
- Each language gets keyword strategy as input
- H1, lede, H2 list designed around primary keywords FIRST, content fills around them
- 3 angles per language are different intent framings of same primary keyword set

**DESIGN step (6):**
- URL slug = exact match primary #1
- Title field uses primary keyword in first 30 chars
- Meta description = primary + 1-2 secondary + CTA
- All H2s mapped to either primary or secondary

**KEYWORD-AUDIT step (6.5):**
- Validates all rules above
- Hard gate: blocks commit if >2 primary fail required placements
- Negative keyword violations cause immediate FAIL

**POST-DEPLOY GSC TRACKING (12):**
- T+14, T+30, T+60 GSC pulls
- Compare actual ranking to target_pos
- Identify mis-targeting + under-targeting
- Feed back into strategy revision

---

## Sample sources for keyword volume estimates

Lacking direct keyword tool access (Ahrefs, SEMrush), estimate via:
1. Google Search autocomplete patterns
2. Google "People Also Ask" frequency
3. Existing GSC data for adjacent queries
4. Competitor content depth (high depth → high volume signal)
5. Reasonable bounds: 20-100 (niche), 100-500 (mid), 500-2000 (head), 2000+ (saturated)

Always express as range like "50-200" not single point estimate.

---

## Cannibalization check procedure

For each primary keyword:
1. Run `grep -rln '[keyword]' src/pages/` to find existing pages
2. For each match, classify:
   - **Adjacent** (different specificity, e.g. "склад для інтернет-магазину" vs "склад для книжкового магазину") → resolution: internal link with disambiguating anchor
   - **Conflicting** (same intent, same specificity) → resolution: choose ONE page to own the query, redirect or differentiate the other
   - **Brand mention** (page mentions keyword in passing, doesn't target) → no action

3. Document each in `cannibalization_check.potential_conflicts[]`

4. Define internal_linking_strategy:
   - 3-5 inbound links from authority pages to new page (with secondary keyword anchors)
   - 3-5 outbound links from new page to related pages

---

## SERP features priorities

For each language, identify:

**Featured snippet target** — ONE structured-answer query we can win
- Format: step list, table, or concise definition
- Map to specific H2 section in the page
- Use semantic markup (ordered list, table, definition list)

**AI Overview target** — ONE conversational pricing/explanation query
- Format: concise factual answer with concrete numbers
- Map to specific section, ideally FAQ or pricing
- Use FAQPage schema

**People Also Ask candidates** — 3-5 questions
- Each becomes an FAQ accordion item
- Phrase exactly as users type ("Як обрати X" not "Вибір X")

---

## Negative keyword guidance

Common negatives by category:
- **Consumer intent**: "купити X", "X онлайн", "X цена"
- **Competitor brands**: Yakaboo, КСД, Юніпост, ShipBob, Lulu
- **Off-topic shared terms**: e.g., "книги онлайн" if you target B2B fulfilment

Negatives prevent SEO budget waste on queries that won't convert. They're an active strategy choice, not just a list.

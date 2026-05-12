# CLICKWORK BRIEF — Manually create Wikidata entity for MTP Group Fulfillment

**Для:** Claude Computer Use / Anthropic Computer Use API / будь-який AI-агент який оперує браузером через скріншоти + кліки + клавіатуру (типу "ClickWord" Chrome extension).

**Тривалість:** ~10-15 хв (з вашою активною присутністю поряд щоб бачити прогрес).

**Кінцевий результат:** Wikidata entity Q[якесь_число] для MTP Group Fulfillment з 7 ключовими statements.

**Чому manual (не QuickStatements):** новий Wikidata акаунт (Mykola Liashchuk) **НЕ autoconfirmed** (потребує 4 дні + 50 правок). QuickStatements bulk-creation заблокований. Але **Special:NewItem звичайний UI працює без autoconfirmed**.

---

## 🤖 PROMPT — paste this verbatim into ClickWork / Computer Use

```
TASK: Create a Wikidata entity for "MTP Group Fulfillment" using the standard
Wikidata UI (Special:NewItem), then add 7 statements one by one. Capture the
resulting Q-number at the end.

CONTEXT:
- The Chrome browser is already open
- User is already logged in to wikidata.org as "Mykola Liashchuk"
- DO NOT use QuickStatements (it requires autoconfirmed status, which this
  account does not have yet). Use the regular Wikidata interface only.

═══════════════════════════════════════════════════════════════════════════
STEP 1 — Open the "create new item" page
═══════════════════════════════════════════════════════════════════════════

Navigate to: https://www.wikidata.org/wiki/Special:NewItem

You should see a form with three fields:
  - Label (the main name)
  - Description
  - Aliases (also known as)
And language tabs for switching between languages.

═══════════════════════════════════════════════════════════════════════════
STEP 2 — Fill English (en) tab first
═══════════════════════════════════════════════════════════════════════════

If the language tab is not English already, change interface language to English
or scroll to find the "en" language fields.

Fill:
  - Label:       MTP Group Fulfillment
  - Description: Ukrainian third-party logistics and order fulfillment company
  - Aliases:     MTP Group

Click "Create" button.

After clicking, the page should navigate to the newly created entity at URL
like: https://www.wikidata.org/wiki/Q123456789

CAPTURE this Q-number — you'll need it at the end. Make a note: "Q-number = Q____"

═══════════════════════════════════════════════════════════════════════════
STEP 3 — Add Ukrainian (uk) and Russian (ru) labels
═══════════════════════════════════════════════════════════════════════════

On the entity page, look for the language section (usually shows all languages).
Click "Add" or "+" next to the languages list to add a new language.

Add Ukrainian (uk):
  - Label:       МТП Груп Фулфілмент
  - Description: Український 3PL фулфілмент-оператор
  - Aliases:     MTP Group

Add Russian (ru):
  - Label:       МТП Груп Фулфилмент
  - Description: Украинский 3PL фулфилмент-оператор

═══════════════════════════════════════════════════════════════════════════
STEP 4 — Add 7 statements one by one
═══════════════════════════════════════════════════════════════════════════

Scroll down to the "Statements" section. For EACH statement below:

  a) Click "+ add statement" button
  b) In the Property field, type the property name (e.g., "instance of")
     and select the correct one from the autocomplete dropdown
  c) In the Value field, type the value or Q-number — select from autocomplete
  d) Click "publish" or check mark to save the statement
  e) Wait for green confirmation before adding next

═════ STATEMENT 1 ═════
  Property:  instance of (P31)
  Value:     business (Q4830453)
  Look for the option labeled "business" — the description should mention
  "organization undertaking commercial activity". DO NOT select MOSFET or
  any other Q4830453-looking value — verify the description matches.

═════ STATEMENT 2 ═════
  Property:  EDRPOU code (P3125)
  Value:     45315740
  (This is a number/string, not a Q-entity. Just type 45315740 and confirm.)

═════ STATEMENT 3 ═════
  Property:  country (P17)
  Value:     Ukraine (Q212)

═════ STATEMENT 4 ═════
  Property:  official website (P856)
  Value:     https://www.fulfillmentmtp.com.ua
  (Full URL string with https://)

═════ STATEMENT 5 ═════
  Property:  inception (P571)
  Value:     2014
  When you enter the date, set precision to "year" (not "day"). The displayed
  date should be just "2014" without any month or day.

═════ STATEMENT 6 ═════
  Property:  legal form (P1454)
  Value:     limited liability company (Q98834261)
  The description should say "type of legal entity in Ukraine". Make sure you
  pick THIS Q98834261 specifically, not a generic LLC entity from another
  country. The description must mention Ukraine.

═════ STATEMENT 7 ═════
  Property:  headquarters location (P159)
  Value:     Boryspil (Q158910)
  Description should say "town in Ukraine". This is Бориспіль city in Kyiv
  Oblast — verify before confirming.

═══════════════════════════════════════════════════════════════════════════
STEP 5 — Verify all statements appear
═══════════════════════════════════════════════════════════════════════════

Scroll through the entity page. Confirm you see ALL 7 statements listed under
the "Statements" section.

Confirm labels exist in 3 languages (en, uk, ru) by checking the top of the page
or the languages list.

═══════════════════════════════════════════════════════════════════════════
STEP 6 — Final report
═══════════════════════════════════════════════════════════════════════════

Output to the user:

✅ WIKIDATA ENTITY CREATED

Q-number: Q[the number you captured in Step 2]
Entity URL: https://www.wikidata.org/wiki/Q[number]

Labels added: en, uk, ru ✓
Statements added: 7/7 ✓
  - P31 instance of = business ✓
  - P3125 EDRPOU = 45315740 ✓
  - P17 country = Ukraine ✓
  - P856 website = https://www.fulfillmentmtp.com.ua ✓
  - P571 inception = 2014 ✓
  - P1454 legal form = LLC Ukraine ✓
  - P159 HQ = Boryspil ✓

═══════════════════════════════════════════════════════════════════════════
RECOVERY — if something goes wrong
═══════════════════════════════════════════════════════════════════════════

- If a property autocomplete shows multiple options — pick the one whose
  description matches what's listed in this brief. Verify Q-number if shown.
- If "Create" button is greyed out — ensure Label field is non-empty.
- If you accidentally selected wrong Q-value — click the statement to edit it,
  delete and re-add.
- If the page reloads unexpectedly — return to entity URL and continue from
  where you left off.
- If you can't find a property — try alternative names:
  * "instance of" or "is a"
  * "country" or "country (P17)"
  * "official website" or "website"
  * "inception" or "date of foundation" or "founded"
  * "legal form" or "form of business"
  * "headquarters location" or "headquarters" or "HQ"
  Always verify the P-number matches what's in this brief.

═══════════════════════════════════════════════════════════════════════════
WHAT NOT TO DO
═══════════════════════════════════════════════════════════════════════════

- DO NOT use https://quickstatements.toolforge.org/ — it requires
  autoconfirmed account status which we don't have yet
- DO NOT add any statements not in this brief (founder, employees, revenue
  etc.) — they need separate sources and entity creation
- DO NOT remove or modify any existing statements if they appear (shouldn't
  be any on a new entity)
- DO NOT post anything in the entity's discussion/talk page

═══════════════════════════════════════════════════════════════════════════
END OF BRIEF
═══════════════════════════════════════════════════════════════════════════
```

---

## After Computer Use agent finishes — give Q-number back to me

Once the agent reports the Q-number, give it to me in the terminal:

```
Q[number]
```

I'll then run the post-submit automation (sameAs patches on 4 files + build + push):

```bash
python3 scripts/wikidata-postsubmit.py Q[number]
```

(I'll create this companion script next so you don't need to re-do the Q-number entry through the interactive script.)

---

## Quick reference card — for visual verification

| Property | P-code | Value | Q-code (if any) | Verify description |
|---|---|---|---|---|
| instance of | P31 | business | Q4830453 | "organization undertaking commercial activity" |
| EDRPOU code | P3125 | 45315740 | — | (numeric string, not Q-entity) |
| country | P17 | Ukraine | Q212 | "country in Eastern Europe" |
| official website | P856 | https://www.fulfillmentmtp.com.ua | — | (URL string) |
| inception | P571 | 2014 | — | (year-precision date) |
| legal form | P1454 | limited liability company | Q98834261 | "type of legal entity in **Ukraine**" |
| headquarters location | P159 | Boryspil | Q158910 | "town in Ukraine" / "Бориспіль" |

---

## Якщо Computer Use агент недоступний

Те саме можна зробити вручну за 10-15 хв — просто follow брифу самостійно. Всі кроки явно прописані.

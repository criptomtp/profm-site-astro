# AUTOMATION BRIEF — Wikidata entity submission for MTP Group Fulfillment

**Target:** автоматизована відправка Wikidata entity через QuickStatements + apply post-submit patches на сайт.

**Кому це дати:** Claude Code session з доступом до Playwright MCP АБО будь-якому AI-агенту з browser automation. Це самодостатній brief — він має всі дані які треба.

**Час виконання:** ~15-20 хв (з urer-OAuth кроком ~5 хв чекати на ваш login).

**Що user мусить зробити сам (єдиний неавтоматизований крок):**
- Login на https://wikidata.org через свій browser (якщо ще не logged-in)
- Authorize QuickStatements OAuth handshake (one click)

Все інше — повністю автоматизується.

---

## PROMPT FOR REMOTE CLAUDE SESSION (paste this as your input)

```
TASK: Submit Wikidata entity for "MTP Group Fulfillment" using QuickStatements,
retrieve the assigned Q-number, then patch the resulting Q-number into 5 JSON-LD
Organization schemas across the website source tree.

CONTEXT:
- Repository: /Users/nikolaj/My vibecode aplications/profm-site-astro (current dir)
- All input data prepared at /docs/wikidata/quickstatements.txt
- All Q-codes and P-codes pre-verified — do NOT modify the batch file
- This is the SECOND submission attempt? Check /docs/wikidata/SUBMISSION-LOG.md
  first — if a successful Q-number is already recorded there, skip Step 1-3 and
  jump to Step 5 (patches).

PROCEED IN THIS ORDER:

STEP 1 — Pre-flight checks
1.1 Read /docs/wikidata/quickstatements.txt — verify it exists and has CREATE
    statement near top
1.2 Read /docs/wikidata/guide.md sections "Розбіжності resolve-ні" — confirm
    inception=2014 and HQ=Boryspil are in the batch
1.3 Check connectivity: curl -sI https://quickstatements.toolforge.org/ — must
    return 200. If it fails, abort and ask user about VPN/network.
1.4 Check that Playwright MCP is available — call browser_open with the
    QuickStatements URL. If browser MCP unavailable, abort and tell user.

STEP 2 — User OAuth handshake (~5 min, only manual step)
2.1 Open https://quickstatements.toolforge.org/#/batch in Playwright browser
2.2 If the page shows "Login required" or shows the login button — tell user:
    > "Будь ласка, у відкритому браузері натисніть 'Login via wikidata.org'
    > і авторизуйте QuickStatements. Скажіть 'authorized' коли побачите
    > форму batch input."
2.3 Wait for user confirmation. Re-check page state — must show a textarea
    for batch input.

STEP 3 — Submit batch
3.1 Read /docs/wikidata/quickstatements.txt content (strip comment lines starting
    with #, keep actual CREATE/LAST lines)
3.2 Click "V1 format" tab if present (not CSV)
3.3 Fill the textarea with the batch content
3.4 Click "Import V1 commands" button
3.5 On the preview screen, verify:
    - Shows "CREATE new item" instruction
    - Shows P31 statements with Q4830453 and Q43229
    - Shows P3125 statement with value "45315740"
3.6 If preview looks wrong, abort and show user the page state. Do NOT click Run.
3.7 If preview looks correct, click "Run" button
3.8 Wait for execution to complete (status bar 100%, "Last batch state: DONE")
3.9 If any individual statement fails with red error, log it but continue —
    most are non-blocking warnings

STEP 4 — Capture Q-number
4.1 In the QuickStatements log/output, look for pattern:
    "Created new item: Q\d+" or check Special:RecentChanges
4.2 Alternative: navigate to https://www.wikidata.org/wiki/Special:RecentChanges
    filtered by current logged-in username, find latest CREATE entry
4.3 Save the Q-number (e.g., "Q123456789") to memory
4.4 Write /docs/wikidata/SUBMISSION-LOG.md with:
    - Timestamp
    - Q-number
    - QuickStatements batch ID (if visible in URL)
    - Confirmation URL: https://www.wikidata.org/wiki/Q{number}

STEP 5 — Apply schema patches
5.1 Read /docs/wikidata/schema-sameAs-patch.txt for exact patches needed
5.2 For each of these files, find or add JSON-LD <script type="application/ld+json">
    with @type:"Organization", then ensure sameAs array contains the Wikidata URL:
    
    a) /src/pages/ua/about.astro
       — Add or update Organization schema in the schemaJson const
    b) /src/pages/poslugy.astro
       — Same
    c) /src/components/Base.astro
       — Check if there's a global Organization schema. If yes, update sameAs.
       — If no, do NOT add one here (avoid duplication).
    d) /public/llms.txt
       — Add or update "Verifiable identifiers" section near top
    e) /public/.well-known/api-catalog (if exists, JSON file)
       — Add wikidata Q-URL to organization metadata
    
5.3 For EACH file edit:
    - Read current content first
    - Find the Organization JSON-LD block (or schemaJson const if using Astro pattern)
    - Locate or create the "sameAs" array
    - Add "https://www.wikidata.org/wiki/Q{number}" as first element
    - Preserve any existing URLs (YouTube, Telegram, LinkedIn)
    - Use Edit tool, not Write — preserve surrounding content

5.4 Edge case: if a file has multiple Organization JSON-LD blocks
    (e.g., one per page, breadcrumbs included), update each separately.

STEP 6 — Build + verify
6.1 Run: npm run build
6.2 Check build output for errors. If errors, abort and report.
6.3 grep dist/ for "wikidata.org/wiki/Q" to verify patches landed in output HTML
6.4 If grep returns 0 matches, debug why (check that Organization schema is
    actually emitted in build, not just in source).

STEP 7 — Commit + deploy
7.1 git add -A
7.2 git commit -m "feat(seo): wire Wikidata Q{number} into Organization sameAs

    Q-number obtained via QuickStatements batch on {timestamp}.
    Patches applied to ua/about, poslugy, llms.txt per schema-sameAs-patch.txt.
    
    Verification: https://www.wikidata.org/wiki/Q{number}"
7.3 git push origin cf-pages-migration
7.4 Wait 90 seconds for CF Pages auto-deploy
7.5 Verify live: curl -s https://www.fulfillmentmtp.com.ua/ua/about/ | grep
    "wikidata.org/wiki/Q{number}" — must return at least 1 match

STEP 8 — Google Rich Results Test
8.1 Open https://search.google.com/test/rich-results?url=https%3A%2F%2Fwww.fulfillmentmtp.com.ua%2Fua%2Fabout%2F
8.2 Look for Organization schema in detected results
8.3 Verify sameAs property includes wikidata.org URL
8.4 If schema parse error, debug and re-deploy

STEP 9 — Final report
9.1 Output to user:

✅ WIKIDATA SUBMISSION COMPLETE

- Q-number: Q{number}
- Entity URL: https://www.wikidata.org/wiki/Q{number}
- Submission log: /docs/wikidata/SUBMISSION-LOG.md
- Schema patches applied: 4-5 files
- Site rebuild + deploy: commit {sha}
- Live verification: ✅ Organization.sameAs includes wikidata URL
- Google Rich Results: ✅ schema valid

⏭️ NEXT (1-7 days, async — patroller review):
- Monitor https://www.wikidata.org/wiki/Q{number} for community edits
- If delete-nominated: accumulate press coverage before re-submit
- After 30 days check Google Knowledge Graph (might pick up automatically)

ABORT CONDITIONS — stop and ask user:
- Playwright MCP not available
- QuickStatements returns 5xx error
- Batch preview shows different statements than expected
- Build fails after patches
- Live verification fails (sameAs not in HTML)
```

---

## SUPPORTING FILES (вже на репо)

| Шлях | Призначення |
|---|---|
| `docs/wikidata/quickstatements.txt` | V1 batch — input для QuickStatements |
| `docs/wikidata/guide.md` | Reference на Q-коди + розбіжності |
| `docs/wikidata/schema-sameAs-patch.txt` | Template patches |
| `docs/wikidata/AUTOMATION-BRIEF.md` | Цей файл — task для remote Claude |
| `docs/wikidata/SUBMISSION-LOG.md` | (буде створено remote-агентом після submit) |

---

## ЯК ВІДКРИТИ TASK У REMOTE CLAUDE SESSION

### Варіант 1 — Claude Code remote (claude.work / GitHub Actions / CI)

Створіть GitHub issue з body:

```
Title: Submit Wikidata entity for MTP Group Fulfillment

Body:
@claude please run /docs/wikidata/AUTOMATION-BRIEF.md task. 
The PROMPT FOR REMOTE CLAUDE SESSION section contains the full instructions.
You'll need browser access (Playwright MCP) and I'll authorize the Wikidata OAuth
when prompted.
```

Якщо ви маєте Claude Code GitHub App або claude.work configured — agent prokachivае task. Pause-точка на OAuth — він спитає, ви залогінитесь і скажете "authorized".

### Варіант 2 — Інша Claude Code session локально

```bash
cd "/Users/nikolaj/My vibecode aplications/profm-site-astro"
claude --browser playwright \
  --instruction "$(cat docs/wikidata/AUTOMATION-BRIEF.md)"
```

(Якщо у вас Claude Code installation з MCP Playwright — це запустить fresh session з готовим browser context.)

### Варіант 3 — Manual fallback (якщо automation не зайде)

Усі файли вже готові — можете виконати кроки 2-7 вручну за ~15 хв, дотримуючись `guide.md`. Patches templated у `schema-sameAs-patch.txt` — копіювати-вставити.

---

## SECURITY NOTES

- Remote Claude session отримає **ваш Wikidata OAuth-token у browser cookies** на час сесії. Це нормально для QuickStatements (його ж задача — submit on your behalf). Cookies автоматично прибираються коли browser session закривається.
- Remote session НЕ отримує доступу до production secrets — bot тільки робить git push на branch що auto-deploy-иться. Якщо хочете додаткову страховку — створіть feature-branch замість push прямо у `cf-pages-migration`.
- Wikidata patroller може delete-nominate entity (1-7 днів review). У такому разі remote agent **не може це виправити сам** — потрібен press coverage який ви накопичуєте окремо. Не вкладайте у remote-agent retry logic.

---

## TROUBLESHOOTING

**Q: "Browser session closed unexpectedly" посеред submit**
A: QuickStatements має fragile session-handling. Просто re-run AUTOMATION-BRIEF з кроку 2.2 — система детектить що submit-у не було і починає заново.

**Q: "Statement #X failed: 'P3125' not found"**
A: Wikidata schema-кеш міг застаріти. Це non-blocking warning, продовжуйте. Перевірте https://www.wikidata.org/wiki/Property:P3125 окремо у browser.

**Q: "Created Q-number not found in log"**
A: Подивіться у Special:Contributions/{your-username} — там буде створена entity навіть якщо лог не вивів Q-номер.

**Q: Schema patch не лендиться у dist/ після build**
A: Перевірте чи Organization schema взагалі рендериться у HTML output (не тільки в Astro source). Якщо ні — потрібно переробити схему через Base.astro layout slot.

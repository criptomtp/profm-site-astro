# Wikidata Submission Guide — MTP Group Fulfillment

**Generated:** 2026-05-12
**Estimated time:** 10-15 minutes for submission + 1-7 days for patroller review

---

## ⚠️ КРИТИЧНО — прочитати перед submit

Під час підготовки виявлено **5 неправильних Q-кодів** і **1 неправильний P-код** у початковому brief. Усі виправлені у `quickstatements.txt`. А також **2 фактичні розбіжності** які треба resolve-ити перед submit:

### Розбіжність 1: рік заснування

| Brief казав | YouControl + project memory кажуть |
|---|---|
| Founded 2014 | LLC registered **2023-10-02** |

YouControl + Clarity-project є офіційними реєстрами і показують реєстрацію 2023. Якщо "MTP Group" як business pre-existed before LLC registration (e.g., перший fulfillment-операційний партнер), Wikidata потребує **citable source** для більш ранньої дати (Forbes / AIN.UA / interview). Без джерела використовуй legal entity date = 2023-10-02. **У файлі вже 2023-10-02.**

### Розбіжність 2: HQ адреса

| Brief казав | YouControl каже |
|---|---|
| Boryspil (Kyiv Oblast) | Legal address: с. Стара Котельня, Житомирська обл. |
| | Operational: Шасливе, Бориспільський район, Київська обл. |

У файлі використано **operational HQ = Boryspil/Kyiv Oblast** бо це адреса складу де реально працює компанія. Wikidata convention дозволяє operational HQ. Якщо patroller спитає — джерело /ua/about/.

### Розбіжність 3: Сирий founder claim

Brief казав P112 = Mykola Liashchuk. У файлі **закоментовано** — Wikidata P112 потребує **Person entity** (окрема Q-сутність) для founder. Створювати Person entity для Liashchuk зараз НЕ рекомендовано (окремий notability бар + ризик delete). Можна додати після того як company entity успішно створиться.

### Розбіжність 4: Employees count

Brief казав 30. Закоментовано — Wikidata patrollers відкидають unsourced employee counts. Якщо у вас є publicly citable число (LinkedIn company page показує? інтерв'ю? річний звіт?) — додайте після створення entity з reference на джерело.

---

## ✅ Виправлення Q/P кодів (already applied)

| Brief казав | Це що насправді | Правильний код | Що означає |
|---|---|---|---|
| Q12047650 | Wikimedia disambig page (Pustý zámek) | **Q98834261** | ТОВ / LLC (Ukraine) |
| Q210793 | MOSFET (semiconductor) | **Q158910** | Boryspil (місто) |
| Q5193 | 404 не існує | **Q170036** | Kyiv Oblast |
| Q5508776 | "Function representation" (math concept) | **Q1473552** | Order fulfillment |
| Q187634 | Emulsion (chemistry) | (опущено — фокус на order fulfillment) | — |
| P3608 | EU VAT number (тільки для ЄС-компаній) | **P3125** | EDRPOU code (Ukraine) |

Q-коди що **залишились правильні**: Q4830453 (business), Q43229 (organization), Q212 (Ukraine), Q1454 (legal form property).

---

## 📋 Покроковий процес submit

### Step 1 — Wikidata account

1. Зайти на https://www.wikidata.org
2. Якщо акаунт немає — **Create account** у правому верхньому куті
3. Login

### Step 2 — QuickStatements авторизація

1. Відкрити https://quickstatements.toolforge.org/
2. Click **Login via wikidata.org** (OAuth handshake)
3. Authorize app permissions for batch operations

### Step 3 — Final review batch файлу

1. Відкрити `/docs/wikidata/quickstatements.txt` локально
2. **Resolve розбіжності** (див. секцію вище):
   - Year founded — залишити 2023-10-02 (default) АБО замінити якщо є джерело на 2014
   - HQ city — залишити Boryspil (operational) АБО замінити на legal address
3. Перевірити очима кожен рядок — особливо Q-номери і EDRPOU 45315740

### Step 4 — Submit batch

1. На сторінці QuickStatements обрати tab **V1** (не V2 / CSV)
2. Paste весь вміст `quickstatements.txt`
3. Click **Import V1 commands** → preview screen show parsed statements
4. Click **Run** (виконується автоматично, статусний бар прогресу)
5. Звичайно займає 30-60 секунд для ~15 statements

### Step 5 — Знайти Q-номер створеної entity

Після Run, у логу QuickStatements буде рядок:
```
CREATE → New entity created: Q[номер]
```

**Збережіть цей Q-номер** — він буде потрібен для:
- Schema sameAs patch (див. `schema-sameAs-patch.txt`)
- Future updates на цю entity

Або знайти через: https://www.wikidata.org/wiki/Special:RecentChanges → filter by your username

### Step 6 — Patroller review (1-7 днів)

Wikidata має community-moderation. Перші 24-72 години інша спільнота може:
- Approve як є → entity stays
- Suggest edits → коментар на сторінці entity
- Reject for notability → entity може бути deletion-nominated

**Notability bar для company entity** на Wikidata:
- ✅ Verifiable EDRPOU 45315740 (державний реєстр)
- ✅ Physical operational address
- ✅ Active commercial website
- ⚠️ Press coverage — слабке місце (нема Forbes / AIN.UA / Wired великих згадок)

Якщо delete-nominated — це сигнал почати накопичувати press coverage перед re-submit (статті у AIN.UA про логістику, інтерв'ю засновника, кейси з клієнтами).

---

## 🔧 Після успішного створення entity

### A. Додати sameAs на сайт

1. Відкрити `/docs/wikidata/schema-sameAs-patch.txt`
2. Замінити `Q________` на ваш отриманий Q-номер
3. Додати у JSON-LD Organization schema на:
   - `/src/pages/ua/about.astro`
   - `/src/pages/poslugy.astro`
   - `/src/components/Base.astro` (якщо там є шаблон Organization schema)

### B. Розширити entity (опційно, через тиждень-два після створення)

Через звичайний Wikidata UI можна додати:
- **P159 logo image** (якщо створити логотип у Commons)
- **P112 founder** = Liashchuk Mykola (потрібна окрема Person entity з notability)
- **P3320 board member** = Sventukh Oleksandr (директор; потрібна окрема Person entity)
- **P1128 number of employees** = коли матимете citable source
- **P1080 manufactured object** = логістичні послуги
- **P127 owned by** = посилання на parent group якщо є

---

## 🚫 Що НЕ робити

- ❌ Не submit-ити з incorrect Q-codes — patroller відхилить за inaccuracy
- ❌ Не вигадувати employee count, revenue, founder bio без джерела
- ❌ Не використовувати маркетингові заявки ("найкращий 3PL Україна") — Wikidata вимагає neutral POV
- ❌ Не submit-ити коли акаунт менше 7 днів старий — system може флагнути спам
- ❌ Не запускати batch повторно якщо перший раз створилась entity — отримаєте дубль

---

## 📚 Корисні посилання

- QuickStatements docs: https://www.wikidata.org/wiki/Help:QuickStatements
- Notability policy: https://www.wikidata.org/wiki/Wikidata:Notability
- Company entity examples (для inspiration):
  - Nova Post (Q12133863) — добре заповнена UA компанія
  - Rozetka (Q1985648) — bigger company, more statements
- Property browser: https://www.wikidata.org/wiki/Wikidata:List_of_properties

---

## 📞 Якщо виникнуть питання

- Wikidata project chat: https://www.wikidata.org/wiki/Wikidata:Project_chat
- IRC #wikidata на libera.chat
- Ukrainian Wikidata community: https://www.wikidata.org/wiki/Wikidata:Ukrainian

# Команда: /create-page

Створює нову сторінку або статтю блогу за повним 12-кроковим pipeline через `create-page-orchestrator` agent.

## Використання:
```
/create-page "Фулфілмент для книжок"
/create-page "Топ-10 маркетплейсів України" --type=blog
/create-page "/fulfilment-knyzhok/" --slug-fixed --type=pillar
```

---

## ⚡ ПЕРША ДІЯ при отриманні цієї команди:

**Ти НЕ виконуєш pipeline сам.** Ти **спавнишь `create-page-orchestrator` agent** через Task tool:

```
Task(
  subagent_type="create-page-orchestrator",
  description="Create new page",
  prompt="""
Create new pillar page for topic: [TOPIC FROM USER]

Slug suggestion: [DERIVE FROM TOPIC OR USER-SPECIFIED]
Type: [pillar / blog / landing — default pillar]

Run the full 12-step pipeline per .claude/commands/create-page.md and
.claude/commands/keyword-strategy-protocol.md. Hard stop at:
- Step 3 STITCH for user approval (show 3 concepts inline)
- Step 6.5 KEYWORD AUDIT for pass verification
- Step 8 QA for validate:pillar + humanizer pass

After deploy (step 11), output the full report per "DEPLOY + ФІНАЛЬНИЙ ЗВІТ"
section of create-page.md.

Do not skip steps. Do not write 3 translations. Do not commit without
Humanizer pass + Keyword Audit pass + Validate:pillar pass.
"""
)
```

Після спавну ти просто чекаєш на результат від orchestrator. Він повертає звіт коли все завершено АБО затримується на hard-stop gates чекаючи твою відповідь.

При hard stop — orchestrator поверне коротке повідомлення з конкретним питанням і ти переадресуй це user. Коли user відповість — передай відповідь назад в orchestrator через `SendMessage` (НЕ створюй новий agent).

---

## ⚠️ Якщо `create-page-orchestrator` agent недоступний:
Виконай pipeline сам, читаючи цей файл повністю + `.claude/commands/keyword-strategy-protocol.md`. Дотримуйся всіх 12 кроків і 3 hard gates без shortcuts.

---

## PIPELINE — 12 кроків (для довідки orchestrator-у і для fallback):

**Pipeline-діаграма:**
```
1. RESEARCHER          → competitors data .claude-flow/research/[slug].json
1.5. KEYWORD-STRATEGIST → keyword strategy .claude-flow/research/[slug]-keywords.json [NEW STEP]
2. ANALYZER + ARCHETYPE → ADR docs/design-system/pages/[slug].md
3. STITCH PREVIEW      → 3 concepts saved → docs/design-system/stitch-exports/[date]_[slug]/
   ⛔ HARD STOP — wait for user approval
4. WRITER              → 3 .astro files (NOT translations)
5. LANGUAGE AUDIT      → 0 русизмів, 0 українізмів, EN naturalness
6. DESIGN              → manual Astro implementation per Stitch ref
6.5. KEYWORD AUDIT     → primary/secondary/negative coverage in code [NEW STEP]
   ⛔ HARD STOP — blocks commit if >2 primary keywords fail
7. IMAGE-GEN           → Pollinations.ai → public/images/[slug]-hero.jpg
8. QA                  → npm run build + validate:pillar + humanizer-scan
   ⛔ HARD STOP — must PASS all 3
9. WIRE-UP             → Header.astro mega-menu + lang-switcher map +
                         llms.txt + MTP_SEMANTIC_CORE_FULL.md status update
10. DEPLOY             → git commit + push (CF Pages auto-deploy)
11. GSC REINDEX        → scripts/gsc-reindex.py 3 URLs
12. POST-DEPLOY GSC TRACKING → schedule T+14, T+30, T+60 GSC checks [NEW STEP]
```

---

## PIPELINE — детальна специфікація кроків (для fallback виконання):

### АГЕНТ 1 — RESEARCHER
1. WebSearch топ-5 конкурентів Google UA + топ-3 RU + топ-3 EN
2. Для кожного: URL, кількість слів, структура H2/H3, ключові тези
3. Факти і статистика з авторитетних джерел
4. docs/MTP_SEMANTIC_CORE_FULL.md — релевантні ключові слова
5. Перевір які сторінки вже є — не повторювати структуру
6. Збережи в .claude-flow/research/[slug].json

---

### АГЕНТ 2 — ANALYZER + ВИБІР АРХЕТИПУ
1. Середня довжина конкурентів, теми яких не розкривають
2. План: мін. +20% слів від середнього конкурента
3. Ключові слова і LSI
4. Перевір docs/LANGUAGE_AUDIT.md
5. **Обери архетип** з 3 варіантів (docs/design-system/archetypes/):
   - **Industrial** — service-hub, міжнародна аудиторія, data-driven (ref: /en/)
   - **Direct** — UA/RU home, calculator, contact, CRO landing (ref: /ua/ after redesign)
   - **Editorial** — FAQ, blog, about, legal (ref: /en/faq/)
6. Опиши: який archetype + чому + який WOW-елемент (1 шт) + які shared компоненти з src/components/stitch/

---

### АГЕНТ 2.5 — STITCH PREVIEW (НОВИЙ ЕТАП)

**Мета**: показати user ВІЗУАЛ перед написанням коду — approval з картинкою, не з текстом.

**🚨 КРИТИЧНЕ ПРАВИЛО — РІЗНОМАНІТТЯ ПРОМПТІВ (lessons learned 2026-05-12):**

Не використовуй ОДИН промпт-шаблон з мінорними правками для кожної сторінки. Stitch інтерпретує однакові promt-сигнали (Industrial, dark+red+white, photo+overlay, 1.4fr/1fr grid) як ОДИН design system → variants виходять як повернення того самого шаблону.

**Кожна нова сторінка ОБОВ'ЯЗКОВО** отримує:

1. **Унікальну візуальну метафору** для hero-фото (не просто "warehouse"):
   - Що саме у кадрі? closeup smartphone seal / aerial drone shot / picker scanning / palette stacks / hands holding box / ESD-зона з робочим у спецодязі / scanner display макро?
   - Який mood? Apple unboxing / Tesla factory / customs office / hospital sterile / craft workshop?
   - Якщо тема має sub-stories (наприклад "anti-grey-market" + "industrial scale" + "individual care") — кожна story = свій кадр.

2. **Унікальний WOW-механізм** (не повторюй timeline/grid з попередньої сторінки):
   - Used уже: 5-step timeline (electronics base), 2x2 stamp grid (electronics 3a), zones map (electronics 3b), B2B vs B2C dossier (b2b UA), flag flow diagram (b2b RU), cost matrix table (b2b EN), Stats Bar 4 cells (komplektatsiya).
   - Не повторюй ці механіки на наступних сторінках. Шукай новий: live ticker / certificate wall / process flowchart vertical / before-after pricing slider / decision tree / customer journey map / weight class diagram / time-elapsed comparison.

3. **3 ОКРЕМИХ ВІЗУАЛЬНИХ НАРАТИВИ для UA / RU / EN** — НЕ один base + variants. Кожна мова отримує власну візуальну ідентичність:
   - UA = primary visual concept (для основної аудиторії — українські підприємці)
   - RU = принципово ІНША композиція (для СНД-аудиторії — інший кут атаки, інший hero photo, інший WOW)
   - EN = третя ще-інша композиція (для міжнародної аудиторії — інший photo, інший WOW)
   - **Приклад b2b-fulfilment**: UA = Bold Red Industrial + B2B-vs-B2C Dossier, RU = Flag Flow Diagram (KZ/MD/GE/UZ/AZ/PL → Kyiv → UA), EN = Dark Savings + Cost Matrix vs US/EU 3PL. Три фундаментально різні візуальні мови.

**Анти-патерн (НЕ робити так)**: один промпт для UA → mirror layout для RU → split-screen для EN. Це не різноманіття, це поворот.

**Pipeline:**

1. На базі архетипу і концепції зроби **СВІЖИЙ промпт для Stitch** (для UA первинно):
   - **Визначи кадр hero-фото конкретно** — не "warehouse" а "extreme macro of holographic security seal on smartphone box, black velvet bg, side-lighting"
   - **Прив'яжи WOW-механізм до теми** — не використовуй timeline якщо тема не процес, не используй grid якщо тема не порівняння
   - Color palette: red #e63329, black #000, white #fff only
   - Archetype signals (uppercase labels, stats bar → Industrial; overlay hero + badge → Direct; big typography + category nav → Editorial)

2. `mcp__stitch__create_project` — створи проект з назвою сторінки

3. `mcp__stitch__generate_screen_from_text` — base screen (UA design)

4. `mcp__stitch__generate_variants` — 2 variants з **РІЗНИМИ ВІЗУАЛЬНИМИ МЕТАФОРАМИ** (не міняй position колонок — міняй що в фото і яка WOW-механіка):
   - Variant 1 = інший hero photo + інший WOW
   - Variant 2 = ще інший hero photo + ще інший WOW
   - Параметри: `variantCount: 2, creativeRange: "EXPLORE", aspects: ["IMAGES", "LAYOUT"]`

5. Окремо опиши TEXTOM (без додаткових Stitch-викликів) візуальні концепти для RU і EN — вони мають бути принципово ІНШИМИ ніж UA. Якщо хочеш — генеруй Stitch для RU/EN теж, але це опціонально.

6. Експортуй артефакти в `docs/design-system/stitch-exports/YYYY-MM-DD_[slug]/`:
   - `concept.md` — archetype, mood, WOW, **повний промпт що ти писав** (для майбутнього reference), rationale, RU/EN концепти текстом
   - `base-screenshot.png` — UA base
   - `variant-1-[mood].png`, `variant-2-[mood].png` — UA варіанти
   - (опціонально) `ru-[mood].png`, `en-[mood].png` якщо генерував окремо

7. Показати user всі скріншоти → чекати approval / зміну

8. Тільки після "approved" → АГЕНТ 3 (Writer)

**Перевірка перед запуском Stitch**: відкрий 2-3 останні `docs/design-system/stitch-exports/*/concept.md` і подивись які промпти/WOW-механіки вже використовувались. **Не повторюй.**

---

### АГЕНТ 3 — WRITER (три окремі продукти для трьох аудиторій)

**КРИТИЧНО: НЕ переклади. Три окремі сторінки з різними кутами атаки.**

**🇺🇦 UA** (`src/pages/[slug].astro` — БЕЗ `/ua/` префіксу, нова URL policy):
- URL: `https://www.fulfillmentmtp.com.ua/[slug]/` (не `/ua/[slug]/`)
- Аудиторія: українські підприємці, e-commerce в Україні
- Кут: практична користь — гривня, Нова Пошта, Rozetka, Prom.ua, реалії воєнного часу
- Тон: діловий але теплий
- SEO: українські запити, Google.com.ua
- Мін. 1200 слів, унікальна структура H2/H3
- Див. CLAUDE.md розділ "Структура Astro сторінок + URL Policy" для деталей

**🇷🇺 RU** (src/pages/ru/[slug].astro):
- Аудиторія: СНД бізнес (Казахстан, Молдова, Грузія) + рускомовні підприємці України
- Кут: міжнародна логістика, вихід на ринок України
- Тон: офіційніший, акцент на надійності
- Інші H2/H3 ніж UA — не копія

**🇬🇧 EN** (src/pages/en/[slug].astro):
- Аудиторія: іноземні компанії, міжнародний e-commerce
- Кут: Ukraine as opportunity, EU access, war-resilient logistics
- Тон: professional, data-driven
- Western business logic — ROI, case studies, metrics

**Для кожної версії:**
- Title до 60 символів з ключовим словом
- Description 150-160 символів
- H1 один на сторінці
- Schema.org розмітка
- Hreflang теги (ua/ru/en)
- Мінімум 3 внутрішні посилання

---

### АГЕНТ 4 — LANGUAGE AUDIT (ОБОВ'ЯЗКОВО після Writer)

Перевір кожну версію окремо:

**UA версія — заборонено:**
- Русизми: "співпраця" (замість "співпраця") ✓, "любий" (замість "будь-який"), 
  "на протязі" (замість "протягом"), "слідуючий" (замість "наступний"),
  "приймати участь" (замість "брати участь"), "відноситися" (замість "стосуватися"),
  "рахунок" в значенні "через" (замість "завдяки/через")
- Перевір повний список в docs/LANGUAGE_AUDIT.md
- Виправ всі знайдені порушення

**RU версія — заборонено:**
- Українізми і суржик
- Перевір docs/LANGUAGE_AUDIT.md
- Виправ всі знайдені порушення

**EN версія — заборонено:**
- Неприродні кальки з UA/RU
- Перевір читабельність для native speaker

Після перевірки: виведи список знайдених і виправлених порушень.

---

### АГЕНТ 5 — DESIGN (після "approved" на Stitch preview)

**Правила:**
- Astro код ВРУЧНУ — НЕ копіювати HTML зі Stitch export
- Використовуй shared компоненти з `src/components/stitch/`:
  - `<LabelChip text="..." variant="red|muted|ghost|dark" />`
  - `<StatsBar items={[...]} tone="light|muted|dark" />`
  - `<SplitHero headline="..." sub="..." imgSrc="..." imgAlt="..." bgSrc="...">...</SplitHero>`
  - `<DarkCTA title="..." sub="..." primary={...} secondary={...} />`
  - `<AccordionGroup items={[{q, a}, ...]} />`
- Токени і утиліти `.s-*` підключено через `public/css/stitch-tokens.css` (автоматично з Base.astro)
- Page-specific стилі — через `<style is:global>` в .astro з BEM префіксом (наприклад `ua-home__hero`)
- Колір: ТІЛЬКИ #e63329 + #000 + #fff (використовуй var(--mtp-red) тощо)
- Mobile-first, без важких бібліотек

**ОБОВ'ЯЗКОВО — КРОС-МОВНА ПЕРЕЛІНКОВКА (часто забуваю!):**
- Всі 3 версії (UA/RU/EN) створюються разом — не деплоїмо одну без інших двох
- Hreflang на всіх 3 сторінках (UA БЕЗ `/ua/` префіксу — нова URL policy):
  ```
  <link rel="alternate" hreflang="uk" href="https://www.fulfillmentmtp.com.ua/[slug]/">
  <link rel="alternate" hreflang="ru" href="https://www.fulfillmentmtp.com.ua/ru/[slug]/">
  <link rel="alternate" hreflang="en" href="https://www.fulfillmentmtp.com.ua/en/[slug]/">
  <link rel="alternate" hreflang="x-default" href="https://www.fulfillmentmtp.com.ua/[slug]/">
  ```
- Додати в language-switcher map в `src/components/Header.astro` (рядок ~310):
  - UA → `/[slug]/` (без `/ua/`)
  - RU → `/ru/[slug]/`
  - EN → `/en/[slug]/`
- Додати в навігацію (mega-menu в Header.astro) якщо це service/landing сторінка
- Breadcrumbs з посиланням на головну (локалізовано по мові)

**ADR:**
- Створи `docs/design-system/pages/[slug].md` — archetype, mood deviations, Stitch export link, approval date

---

### АГЕНТ 6 — IMAGE-GEN (Pollinations.ai — безкоштовно)

```bash
curl -o "public/images/[slug]-hero.jpg" \
  "https://image.pollinations.ai/prompt/professional+logistics+warehouse+Ukraine+fulfillment+red+accent?width=1200&height=630&nologo=true"

curl -o "public/images/[slug]-feature.jpg" \
  "https://image.pollinations.ai/prompt/modern+fulfillment+center+Ukraine+business+operations?width=800&height=600&nologo=true"
```

---

### АГЕНТ 7 — QA

#### ЕТАП 1 — ПЕРЕД ДЕПЛОЄМ (вихідний код)

```bash
npm run build 2>&1 | grep -E "error|warning"
```

Перевір у вихідному коді:
- [ ] Title до 60 символів (всі 3 мови)
- [ ] Description 150-160 символів (всі 3 мови)
- [ ] H1 один на сторінці
- [ ] Canonical URL коректний
- [ ] Hreflang: uk, ru, en, x-default — всі взаємопосилаються
- [ ] Schema.org: Service + FAQPage + BreadcrumbList + LocalBusiness
- [ ] Alt теги на всіх зображеннях
- [ ] width/height на всіх `<img>`
- [ ] loading="lazy" на всіх зображеннях (крім hero з fetchpriority="high")
- [ ] YouTube: facade (не iframe), loading тільки по кліку
- [ ] Render-blocking: скрипти мають async/defer
- [ ] Мінімум 3 внутрішні посилання
- [ ] FAQ секція присутня
- [ ] Перемикач мов: додано в lang-switcher map (Header.astro)
- [ ] Навігація: сторінка додана в mega-menu (Header.astro)
- [ ] Breadcrumbs присутні
- [ ] Нуль русизмів в UA (Language Audit: docs/LANGUAGE_AUDIT.md)
- [ ] Нуль українізмів в RU
- [ ] Три версії — три різні кути, НЕ переклади
- [ ] Унікальний дизайн — не схожий на інші сторінки

**DUAL-MD (автогенерація .md для AI агентів):**
- [ ] Сторінка використовує `Base.astro` (не standalone) — інакше `integrations/dual-md.mjs` не побачить її
- [ ] Після `npm run build` у виводі — `[dual-md] X written, ...` і X збільшилось на 3 (UA + RU + EN)
- [ ] Перевірити: `ls dist/ua/[slug]/index.md dist/ru/[slug]/index.md dist/en/[slug]/index.md` — всі три мусять існувати
- [ ] `head -10 dist/ua/[slug]/index.md` — має бути frontmatter (title, description, lang, canonical) + чистий контент без форм/footer/CTA
- [ ] Якщо якась декоративна секція (логотип marquee, дубльований візуал) потрапила в .md — додати `data-md-skip` на цей елемент у .astro

**ПЕРЕМИКАЧ МОВ:**
- [ ] UA→RU: перехід працює (не 404)
- [ ] RU→EN: перехід працює (не 404)
- [ ] EN→UA: перехід працює (не 404)
- [ ] Якщо RU сторінка в /ru/ — map значення має бути повний шлях `/ru/slug/`
- [ ] Якщо не працює — виправити map в Header.astro (рядок ~310)

**ФОРМИ CTA (ЗАЛІЗНЕ правило):**
- [ ] Hero — ТІЛЬКИ `<HeroCTA lang="uk|ru|en" theme="light|dark" button="..." microCopy="..." sourceTag="hero /слug/"/>`
  - Імпорт: `import HeroCTA from '../../components/HeroCTA.astro';`
  - НЕ писати кастомні `<form id="heroForm">` з inline submit handler — флагуються як небезпечні
  - НЕ використовувати `<CTA/>` у hero (його id `finalForm` вже використаний bottom-CTA у Base)
- [ ] Bottom — стандартний `<CTA/>` через Base.astro (showCTA=true, дефолт)
- [ ] Максимум 2 форми на сторінку (hero + footer), мінімум 3 секції контенту між ними
- [ ] Декоративний hero тільки з кнопками "Розрахувати"/"Зателефонувати" без поля телефону — НЕ допустимо
- [ ] **QA gate обов'язковий**: після деплою відправити тестовий номер з hero-форми → перевірити що лід прийшов у Telegram (@nikolay_mtp). Без цього сторінка НЕ готова.

**МОБІЛЬНА ВЕРСІЯ:**
- [ ] Viewport 375px: немає горизонтального скролу
- [ ] Перемикач мов видно і клікабельний (44px+ кнопки)
- [ ] Форми відображаються коректно (stack, не overflow)
- [ ] Кнопки мінімум 44px висота
- [ ] grid→stack на 768px

#### ЕТАП 2 — ПІСЛЯ ДЕПЛОЮ (live перевірка)

```bash
# git commit + push (Vercel auto-deploy)
git add . && git commit -m "feat: new page [slug]" && git push
```

Після деплою перевірити:

```bash
# PageSpeed — Performance, SEO, Accessibility
for strategy in mobile desktop; do
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://fulfillmentmtp.com.ua/ua/[slug]/&strategy=$strategy" \
  | python3 -c "
import sys,json; d=json.load(sys.stdin)
cats=d['lighthouseResult']['categories']
print(f'{strategy.upper()}:')
for k in ['performance','seo','accessibility']:
  print(f'  {k}: {cats[k][\"score\"]*100:.0f}')
lcp=d['lighthouseResult']['audits']['largest-contentful-paint']['numericValue']/1000
cls=d['lighthouseResult']['audits']['cumulative-layout-shift']['numericValue']
print(f'  LCP: {lcp:.1f}s (target <2.5s)')
print(f'  CLS: {cls:.3f} (target <0.1)')
"
done
```

Цільові показники:
- [ ] Performance Mobile: 80+
- [ ] Performance Desktop: 90+
- [ ] SEO: 100
- [ ] LCP < 2.5s
- [ ] CLS < 0.1
- [ ] gtag працює (перевірити на /thanks/ після submit)
- [ ] Форма відправляє в Telegram + CRM (/api/leads)

---

### АГЕНТ 8 — LINKEDIN DISTRIBUTION

Після успішного deploy (сторінка live, PageSpeed OK) — готую LinkedIn-пост для Company Page.

1. **Вибери мови для постингу:**
   - UA версія → завжди пост (основна аудиторія)
   - EN версія → пост якщо тема international-релевантна (cross-border, EU gateway, DTC)
   - RU версія → НЕ постити на LinkedIn (невідповідна оптика у воєнному контексті)

2. **Для кожної обраної мови створи файл** `docs/linkedin/queue/YYYY-MM-DD_[slug]-[lang].md`:
   - Перший рядок: hook-цифра/проблема (≤80 символів)
   - Другий: продовження гачка або тизер
   - 2-4 короткі абзаци по 1-3 речення
   - 3-5 буллетів через "→" з унікальною цінністю (не переклад H2 зі статті)
   - CTA + 🔗 url на окремому рядку
   - 4-5 хештегів у кінці
   - Довжина 1200-2000 символів (ідеал для LinkedIn engagement)
   - Тон: конкретика, цифри, провокаційно — без маркетингового fluff
   - НЕ переписуй intro статті дослівно — пост це окремий контент-кутик

3. **Опублікуй найпершу UA-версію відразу** (інші — розклади на +3 і +7 днів у назві файлу):
   ```bash
   python3 scripts/linkedin-post.py --from-file docs/linkedin/queue/YYYY-MM-DD_[slug]-ua.md
   ```

4. **Після успіху** — перенеси файл у `docs/linkedin/published/`:
   ```bash
   mv docs/linkedin/queue/YYYY-MM-DD_[slug]-ua.md docs/linkedin/published/
   ```

5. **Якщо скрипт повертає `AUTH_STALE`** — скажи user: "LinkedIn session прострочена, запусти `python3 scripts/linkedin-auth.py`", і залиш пост у `queue/` без публікації.

6. **Правило ритму:** не публікувати 2 пости підряд у той самий день. Якщо сьогодні вже публікувався — всі нові йдуть у queue/ з датою +2/+5 днів.

У фінальний звіт додати секцію **### LinkedIn:** — які файли створено, які опубліковано, які у черзі.

---

### DEPLOY + ФІНАЛЬНИЙ ЗВІТ

```
## ЗВІТ: [назва]

### Дослідження:
- Конкурентів: X UA + X RU + X EN
- Середня довжина конкурентів: X слів
- Наша стаття: X слів (+X% від середнього)
- Унікальні теми vs конкуренти: [список тем яких немає у конкурентів]
- Прогноз топ-5: 3-6 місяців

### Дизайн: [назва концепції]
- WOW-елемент: [опис]

### Сторінки:
UA: /[slug]/ — X слів | для українських підприємців (URL без /ua/ префіксу — нова policy)
RU: /ru/[slug]/ — X слів | для СНД бізнесу
EN: /en/[slug]/ — X слів | для міжнародного бізнесу

### Language Audit:
UA: знайдено X русизмів → виправлено / 0 русизмів
RU: знайдено X українізмів → виправлено / 0 українізмів
EN: без зауважень

### Технічна перевірка:
- Alt теги: X/X зображень мають alt
- loading="lazy": X/X зображень
- width/height: X/X зображень
- YouTube: facade (0 iframes при завантаженні)
- Перемикач мов: працює (UA↔RU↔EN)
- Навігація: додано в mega-menu
- Breadcrumbs: присутні

### PageSpeed:
| Метрика | Mobile | Desktop |
|---------|--------|---------|
| Performance | X/100 | X/100 |
| SEO | X/100 | X/100 |
| Accessibility | X/100 | X/100 |
| LCP | X.Xs | X.Xs |
| CLS | 0.XXX | 0.XXX |

### SEO:
- Title: X символів (до 60)
- Description: X символів (150-160)
- H1: 1 шт.
- Canonical: коректний
- Hreflang: uk, ru, en, x-default — взаємопосилання ок
- Schema.org: Service + FAQPage + BreadcrumbList + LocalBusiness
- Internal links: X шт.

### Деплой:
https://www.fulfillmentmtp.com.ua/[slug]/          ← UA (без /ua/)
https://www.fulfillmentmtp.com.ua/ru/[slug]/
https://www.fulfillmentmtp.com.ua/en/[slug]/

### LinkedIn:
- Створено у queue: [список файлів docs/linkedin/queue/]
- Опубліковано зараз: [ua-файл або "нічого (ритм-пауза)"]
- Відкладено: [коли наступний пост піде]
```

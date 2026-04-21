# MTP Group — profm-site-astro
# fulfillmentmtp.com.ua | Astro + Vercel

## ЧИТАЙ ЗАВЖДИ на початку кожної сесії:
Read ~/.claude/skills/mtp-knowledge/SKILL.md

---

## Skill routing:
- Нова сторінка/стаття → Read frontend-design + seo-page + copywriting-ua + seo-hreflang
- SEO аудит → Read seo + seo-technical + seo-audit + seo-universal
- Google Ads → Read google-ads-analysis + google-ads-write
- Контент → Read content-production + content-strategy + content-humanizer + copywriting-ua
- Дизайн компоненти → Read senior-frontend + frontend-design
- CRO аналіз → Read cro + cro-advisor
- SEO конкуренти → Read seo-competitor-pages + seo-competitor-ext
- Нові компоненти Astro → Read astro skill
- Аудит сторінки → astrodeck agents (Design + UX + A11y + Perf + SEO паралельно)

---

## АВТОНОМНИЙ РЕЖИМ (головне правило):
- Виконуй завдання ПОВНІСТЮ без зупинок і питань
- Не питай "чи продовжувати?" — продовжуй завжди
- Не зупиняйся після одного кроку — виконуй всі кроки до кінця
- Якщо щось незрозуміло — прийми рішення сам і вкажи у звіті
- В кінці ЗАВЖДИ давай звіт у форматі ✅/❌

## Вибір моделі (рекомендації для користувача):
Перед виконанням задачі оціни складність і порекомендуй модель:
- **Sonnet 4.6** (швидкий): рутинні фікси, CSS/HTML правки, додавання контенту, build+push, прості SEO зміни
- **Opus 4.6** (глибокий): архітектурні рішення, міграції (standalone→Base.astro), CRO дебати, створення нових сторінок з нуля, складний рефакторинг, multi-agent аналіз
Якщо задача потребує Opus а зараз Sonnet — скажи: "⚠️ Для цієї задачі рекомендую Opus (/model opus)"

---

## MULTI-AGENT PIPELINE для нових сторінок:
При отриманні завдання "створи сторінку" або "напиши статтю":
1. RESEARCHER — WebSearch + WebFetch конкурентів (топ-5 UA + топ-3 RU + топ-3 EN)
2. ANALYZER — аналіз структури, довжини, ключових слів конкурентів + вибір архетипу (Industrial/Direct/Editorial)
2.5. STITCH PREVIEW — generate_screen_from_text + 2-3 variants → експорт у docs/design-system/stitch-exports/[date]_[slug]/ → показати user → "approved"
3. WRITER — написання UA + RU + EN (не переклади — різні кути атаки)
4. IMAGE-GEN — генерація зображень через Pollinations.ai (безкоштовно)
5. DESIGN — Astro код ВРУЧНУ за Stitch-референсом, використовуючи src/components/stitch/ (StatsBar, LabelChip, SplitHero, DarkCTA, AccordionGroup)
6. QA — перевірка SEO + PageSpeed + mobile + build
7. DEPLOY — vercel --prod + фінальний звіт

Детальний опис pipeline: .claude/commands/create-page.md
Редизайн існуючих сторінок: .claude/commands/redesign-page.md

---

## STITCH + ДИЗАЙН-СИСТЕМА (критично):

**Source of truth**: `docs/design-system/`
- `docs/design-system/archetypes/` — 3 moods (industrial / direct / editorial)
- `docs/design-system/stitch-exports/` — Stitch артефакти (concept.md + screenshot.png)
- `docs/design-system/pages/` — ADR на кожну сторінку

**3 Moods — обовʼязково обирати один:**
- **Industrial** — EN home, service-hub, міжнародна аудиторія (split hero, uppercase labels, stats bar)
- **Direct** — UA home, RU home, calculator, contact, CRO landing (full-width hero з overlay, badge, hero form)
- **Editorial** — FAQ, blog, about, legal (велика типографіка, без hero image, category nav)

**Shared коду**:
- `src/styles/stitch-tokens.css` — токени + утиліти (підключено в Base.astro)
- `src/components/stitch/` — StatsBar, LabelChip, SplitHero, DarkCTA, AccordionGroup

**Правила Stitch:**
1. Stitch output = ВІЗУАЛЬНИЙ РЕФЕРЕНС, не код. HTML/CSS зі Stitch НЕ копіювати в .astro.
2. Кожен approved concept експортується в `docs/design-system/stitch-exports/YYYY-MM-DD_[slug]/` (concept.md + screenshot.png) ДО написання коду.
3. Per-page ADR у `docs/design-system/pages/[slug].md` — archetype, deviations, Stitch link, approval date.
4. Токени (#e63329/#000/#fff) — фіксовані в Stitch і в коді, не міняються.

**Редизайн priority Tier NOW:**
1. `/ua/` home (Direct mood)
2. `/ru/` home (Direct mood, інший акцент від UA)
3. `/en/calculator/`, `/ua/calculator/`, `/ru/calculator/` (Direct mood)

**Rollback trigger для редизайну**: CR -15% АБО positions -20% за 7 днів → git revert.

---

## Чеклист для кожної нової сторінки (виконувати автоматично):
- [ ] Дослідження конкурентів (топ-5 Google UA/RU/EN)
- [ ] Прочитати docs/MTP_SEMANTIC_CORE_FULL.md — релевантні ключові слова
- [ ] Прочитати docs/LANGUAGE_AUDIT.md — мовні правила
- [ ] Прочитати docs/design-system/archetypes/[mood].md — обраний mood
- [ ] ls public/images/ — перевірити доступні зображення
- [ ] Згенерувати hero + feature зображення (Pollinations.ai)
- [ ] Stitch Preview: generate_screen_from_text + variants → export у docs/design-system/stitch-exports/
- [ ] Створити UA: src/pages/ua/[slug].astro (мін. 1200 слів)
- [ ] Створити RU: src/pages/ru/[slug].astro (інший кут, не переклад)
- [ ] Створити EN: src/pages/en/[slug].astro (інший кут, не переклад)
- [ ] **КРОС-МОВНА ПЕРЕЛІНКОВКА (обовʼязково, часто забуваю):**
  - [ ] Всі 3 версії створені в одній задачі — не деплоїмо одну без інших двох
  - [ ] Hreflang на всіх 3 сторінках (uk/ru/en/x-default) — повне взаємопосилання
  - [ ] Додано в language-switcher map в src/components/Header.astro (рядок ~310) — всі 3 мови
  - [ ] Перевірка: UA→RU, RU→EN, EN→UA — жодного 404
  - [ ] Додано в навігацію (mega-menu в Header.astro) якщо це service/landing сторінка
- [ ] Title до 60 символів (всі 3 мови)
- [ ] Description 150-160 символів (всі 3 мови)
- [ ] H1 один на сторінці
- [ ] Schema.org розмітка
- [ ] Мінімум 3 внутрішні посилання
- [ ] Перевірка мови (LANGUAGE_AUDIT.md)
- [ ] ADR в docs/design-system/pages/[slug].md
- [ ] npm run build — без помилок
- [ ] PageSpeed перевірка (після деплою)
- [ ] npx vercel --prod

---

## SEO Правила (обов'язково):
1. Домен завжди www: https://www.fulfillmentmtp.com.ua/
2. Redirect non-www → www має бути 301 (permanent), НЕ 307
3. Кожна нова сторінка ОБОВ'ЯЗКОВО має:
   - canonical (абсолютний URL з www)
   - hreflang (uk, ru, en, x-default) — всі 4
   - title (50-60 символів)
   - description (150-160 символів)
   - Schema.org (мінімум Article або Service + BreadcrumbList)
   - H1 (рівно один)
   - Всі зображення: alt, width, height, loading="lazy"
   - Використовувати Base.astro (НЕ standalone)
4. Перед деплоєм нової сторінки перевірити:
   - `curl -sI "https://fulfillmentmtp.com.ua/ШЛЯХ/"` → має бути 301 → www
   - `curl -sI "https://www.fulfillmentmtp.com.ua/ШЛЯХ/"` → має бути 200
5. Після деплою — подати Request Indexing в GSC

---

## ЗАЛІЗНЕ ПРАВИЛО дизайну:
1. Спочатку опиши концепцію ТЕКСТОМ (назва стилю, палітра, унікальна фішка)
2. Чекай слово "approved" від користувача
3. ТІЛЬКИ після "approved" — пиши код

---

## ЗАЛІЗНЕ ПРАВИЛО CTA-форм (first-screen):
**Кожна нова сторінка на першому екрані (hero) МУСИТЬ мати нашу стандартну CTA форму з перевіреною доставкою в Telegram.**

- Стандартна форма = та, що рендериться `<CTA/>` (`src/components/CTA.astro`) — перевірена, надійно доставляє в Telegram через `window.mtpSubmitLead` → `/api/telegram` + `/api/leads`.
- Декоративний hero тільки з кнопками "Розрахувати" / "Зателефонувати" БЕЗ поля телефону — **НЕ допустимо** для нових сторінок.
- Якщо потрібна hero-версія форми — зробити окремий компонент `HeroCTA.astro` (дзеркало CTA.astro з унікальним id і власним submit handler), а не кастомний `<form id="heroForm">`.
- `<form id="heroForm">` через Base.astro auto-handler — **НЕ вважається безпечним дефолтом** (був випадок коли ліди не доходили до Telegram). Використовувати тільки з live-тестом.
- **QA gate**: не позначати сторінку готовою, поки не відправлено тестовий номер з hero-форми і не отримано повідомлення в Telegram (@nikolay_mtp). Це обов'язковий крок поряд з PageSpeed і Schema перевіркою.
- Внизу сторінки — стандартний `<CTA/>` через `Base.astro` (showCTA=true). Дві форми на сторінці (hero + bottom) — це норма, головне не три.

---

## Дизайн (КРИТИЧНО):
- Колір: ТІЛЬКИ #e63329 + #000 + #fff — ніякого зеленого, синього, фіолетового
- Кожна сторінка обирає ОДИН з 3 archetypes (Industrial / Direct / Editorial) — див. docs/design-system/archetypes/
- Hero і секції варіюються ВСЕРЕДИНІ archetype — без "10 різних стилів"
- UA / RU / EN: різний кут атаки, різна структура, різні візуальні рішення — НЕ переклади
- Shared: Base.astro, Header.astro, Footer.astro, stitch-tokens.css — єдині для всіх мов
- Divergent: hero, секції, тон, layout — перекладно з archetype, не з іншої мови

---

## Структура Astro сторінок:
- UA: src/pages/ua/[slug].astro
- RU: src/pages/ru/[slug].astro
- EN: src/pages/en/[slug].astro

---

## Зображення:
- Шлях: public/images/
- Завжди: ls public/images/ перед створенням сторінки
- Використовувати ТІЛЬКИ реальні файли з цієї папки
- Нові зображення генерувати через Pollinations.ai

## Генерація зображень (Pollinations.ai — безкоштовно):
```bash
curl -o "public/images/[slug]-hero.jpg" \
  "https://image.pollinations.ai/prompt/professional+logistics+warehouse+Ukraine+red+accent?width=1200&height=630&nologo=true"
```

---

## Заборонено:
- Зелений колір (#00c853 та подібні)
- Дублювати форму перед footer (максимум 1 форма на сторінку)
- Nova Poshta бонуси (ТОП-200, 17 днів безкоштовно)
- RU як переклад UA — різний кут атаки обов'язково
- Зупинятись і питати дозволу в процесі виконання
- Робити тільки одну мову якщо завдання не вказує інше
- Вигадувати факти — тільки перевірена інформація з research

---

## Довідкові документи (docs/):
- `docs/MTP_SEMANTIC_CORE_FULL.md` — семантичне ядро: 120+ сторінок. ОБОВ'ЯЗКОВО при нових SEO-сторінках.
- `docs/LANGUAGE_AUDIT.md` — мовний аудит: 35 порушень. Перевіряти при написанні.
- `docs/TITLES_TO_FIX.md` — тайтли >60 символів для виправлення.
- `docs/design-system/README.md` — архетипи, Stitch workflow, priority queue.
- `docs/design-system/archetypes/` — industrial.md, direct.md, editorial.md.
- `docs/design-system/stitch-exports/` — Stitch артефакти (concept + screenshot) на approved концепцію.
- `docs/design-system/pages/` — ADR + baseline на кожну створену/редизайнуту сторінку.

---

## Формат фінального звіту:
```
## ✅ ЗВІТ: [назва]
✅ UA: /ua/[slug]/ — X слів
✅ RU: /ru/[slug]/ — X слів
✅ EN: /en/[slug]/ — X слів
✅ Зображення: згенеровано X шт
✅ Build: без помилок
✅ PageSpeed Mobile: X/100
✅ Deploy: https://fulfillmentmtp.com.ua/ua/[slug]/
⚠️ Увага: [якщо є нюанси]
```

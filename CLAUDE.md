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

---

## MULTI-AGENT PIPELINE для нових сторінок:
При отриманні завдання "створи сторінку" або "напиши статтю":
1. RESEARCHER — WebSearch + WebFetch конкурентів (топ-5 UA + топ-3 RU + топ-3 EN)
2. ANALYZER — аналіз структури, довжини, ключових слів конкурентів
3. WRITER — написання UA + RU + EN (не переклади — різні кути атаки)
4. IMAGE-GEN — генерація зображень через Pollinations.ai (безкоштовно)
5. QA — перевірка SEO + PageSpeed + mobile + build
6. DEPLOY — vercel --prod + фінальний звіт

Детальний опис pipeline: .claude/commands/create-page.md

---

## Чеклист для кожної нової сторінки (виконувати автоматично):
- [ ] Дослідження конкурентів (топ-5 Google UA/RU/EN)
- [ ] Прочитати docs/MTP_SEMANTIC_CORE_FULL.md — релевантні ключові слова
- [ ] Прочитати docs/LANGUAGE_AUDIT.md — мовні правила
- [ ] ls public/images/ — перевірити доступні зображення
- [ ] Згенерувати hero + feature зображення (Pollinations.ai)
- [ ] Створити UA: src/pages/ua/[slug].astro (мін. 1200 слів)
- [ ] Створити RU: src/pages/ru/[slug].astro (інший кут, не переклад)
- [ ] Створити EN: src/pages/en/[slug].astro (інший кут, не переклад)
- [ ] Title до 60 символів (всі 3 мови)
- [ ] Description 150-160 символів (всі 3 мови)
- [ ] H1 один на сторінці
- [ ] Schema.org розмітка
- [ ] Hreflang теги (ua/ru/en)
- [ ] Мінімум 3 внутрішні посилання
- [ ] Перевірка мови (LANGUAGE_AUDIT.md)
- [ ] npm run build — без помилок
- [ ] PageSpeed перевірка (після деплою)
- [ ] npx vercel --prod

---

## ЗАЛІЗНЕ ПРАВИЛО дизайну:
1. Спочатку опиши концепцію ТЕКСТОМ (назва стилю, палітра, унікальна фішка)
2. Чекай слово "approved" від користувача
3. ТІЛЬКИ після "approved" — пиши код

---

## Дизайн (КРИТИЧНО):
- Колір: ТІЛЬКИ #e63329 + #000 + #fff — ніякого зеленого, синього, фіолетового
- Кожна сторінка: УНІКАЛЬНА структура і hero — не копіювати існуючі
- UA / RU / EN: різний кут атаки, різна структура — НЕ переклади

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

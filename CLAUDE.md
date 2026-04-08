# MTP Group — RuFlo Project Rules

## ЧИТАЙ ЗАВЖДИ на початку кожної сесії:
Read ~/.claude/skills/mtp-knowledge/SKILL.md

## Skill routing:
- Нова сторінка → Read frontend-design + seo-page + copywriting-ua + seo-hreflang
- SEO аудит → Read seo + seo-technical + seo-audit
- Google Ads → Read google-ads-analysis + google-ads-write
- Контент → Read copywriting-ua + tilda-content

## ЗАЛІЗНЕ ПРАВИЛО дизайну (порушення заборонено):
1. Спочатку опиши концепцію ТЕКСТОМ (назва стилю, палітра, унікальна фішка)
2. Чекай слово "approved" від користувача
3. ТІЛЬКИ після "approved" — пиши код

## Дизайн (КРИТИЧНО):
- Колір: ТІЛЬКИ #e63329 + #000 + #fff — ніякого зеленого, синього, фіолетового
- Кожна сторінка: УНІКАЛЬНА структура і hero — не копіювати існуючі
- UA / RU / EN: різний кут атаки, різна структура — НЕ переклади

## Зображення:
- Шлях: public/images/
- Завжди: ls public/images/ перед створенням сторінки
- Використовувати реальні файли з цієї папки

## Заборонено:
- Зелений колір (#00c853 та подібні)
- Дублювати форму перед footer (максимум 1 форма на сторінку)
- Nova Poshta бонуси (ТОП-200, 17 днів безкоштовно)
- RU як переклад UA

## Структура Astro сторінок:
- UA: src/pages/ua/[slug].astro
- RU: src/pages/ru/[slug].astro
- EN: src/pages/en/[slug].astro

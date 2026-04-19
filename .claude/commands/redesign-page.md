# Команда: /redesign-page

Редизайн існуючої сторінки через Stitch pipeline.
Повністю автономно, з baseline measurement і SEO-freeze.

## Використання:
```
/redesign-page /ua/
/redesign-page /ua/calculator/ --mood=direct
```

---

## PIPELINE — виконувати повністю без зупинок:

### КРОК 1 — BASELINE MEASUREMENT

Зняти і зберегти поточні метрики ПЕРЕД будь-яким редизайном.

1. Визначити slug і шлях до файлу (наприклад `src/pages/index.astro` для `/ua/`).
2. Зняти baseline через GSC + GA4 (використай доступні MCP або WebFetch для Search Console).
3. Зняти PageSpeed:

```bash
for strategy in mobile desktop; do
  curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.fulfillmentmtp.com.ua[URL]&strategy=$strategy" \
    | python3 -c "
import sys,json; d=json.load(sys.stdin)
cats=d['lighthouseResult']['categories']
print(f'{strategy.upper()}:')
for k in ['performance','seo','accessibility']:
  print(f'  {k}: {cats[k][\"score\"]*100:.0f}')
audits=d['lighthouseResult']['audits']
print(f'  LCP: {audits[\"largest-contentful-paint\"][\"numericValue\"]/1000:.1f}s')
print(f'  CLS: {audits[\"cumulative-layout-shift\"][\"numericValue\"]:.3f}')
print(f'  INP: {audits.get(\"interaction-to-next-paint\",{}).get(\"numericValue\",0):.0f}ms')
"
done
```

4. Зберегти у `docs/design-system/pages/[slug]-baseline.md` за шаблоном з `docs/design-system/pages/README.md`.

Якщо baseline не можна зняти (нова сторінка без трафіку) — пропусти цей крок, але позначь це в baseline.md як "no baseline — newly created".

---

### КРОК 2 — АРХЕТИП + STITCH PREVIEW

1. Прочитай `docs/design-system/README.md` і 3 архетипи в `docs/design-system/archetypes/`.
2. Обери mood для сторінки:
   - UA/RU home → Direct
   - Calculator / contact → Direct
   - FAQ / blog / about → Editorial
   - Service hub / EN landing → Industrial
3. Якщо mood очевидний з типу сторінки — не питай user. Якщо нестандартний — спитай.
4. Stitch pipeline:
   - `mcp__stitch__generate_screen_from_text` — base screen на основі mood
   - `mcp__stitch__generate_variants` — 2-3 варіанти
   - Експорт у `docs/design-system/stitch-exports/YYYY-MM-DD_[slug]/`:
     - `concept.md` — mood, WOW, prompt, rationale
     - `screenshot.png` — скрін base + variants
5. Показати user → чекати "approved" або "змінити".

---

### КРОК 3 — SEO-FREEZE PLAN

Перед тим як змінювати код — зафіксуй що ЗАЛИШАЄТЬСЯ незмінним:

1. Відкрий поточний файл сторінки і витягни в `docs/design-system/pages/[slug]-seo-freeze.md`:
   - URL (не міняти)
   - H1 текст (не міняти, зберігає primary keyword)
   - Title тег (не міняти)
   - Description (не міняти)
   - Schema.org JSON-LD блок (переносимо дослівно)
   - Canonical URL
   - Hreflang tags (всі 4)
   - Primary keywords у body (flag їх у новому layout — вони мають залишитись)

2. Screenshot старого SERP snippet (для контролю featured snippets).

---

### КРОК 4 — REDESIGN CODE

1. Зробити backup-гілку: `git checkout -b redesign/[slug]-YYYYMMDD`
2. Переписати `.astro` файл вручну, орієнтуючись на Stitch screen:
   - Використати shared компоненти з `src/components/stitch/`
   - Підключити стилі через `<style is:global>` з BEM префіксом
   - ПЕРЕНЕСТИ дослівно: title, description, canonical, hreflang, Schema.org, H1 текст
   - URL не міняти (шлях файлу той самий)
3. **КРОС-МОВНА СИНХРОНІЗАЦІЯ (обовʼязково, часто забуваю):**
   - Якщо редизайн /ua/ — ОДРАЗУ передбач редизайн /ru/ і /en/ або мінімум перевір що їх hreflang і Header switcher не поламані.
   - Перевір `src/components/Header.astro` ~рядок 310 — language-switcher map
   - Перевір навігацію mega-menu
4. `npm run build` — має пройти без помилок.

---

### КРОК 5 — QA (перед деплоєм)

- [ ] Title незмінний
- [ ] Description незмінний
- [ ] H1 незмінний
- [ ] Canonical URL той самий
- [ ] Hreflang 4 tags (uk/ru/en/x-default)
- [ ] Schema.org — весь JSON-LD блок на місці
- [ ] Usage Base.astro
- [ ] Всі зображення мають alt + width + height + loading
- [ ] Мінімум 3 внутрішні посилання
- [ ] Shared компоненти використані (StatsBar / LabelChip / SplitHero / DarkCTA / AccordionGroup за потребою)
- [ ] Мобільний viewport 375px — без горизонтального скролу
- [ ] Кнопки 44px+ висота
- [ ] Language switcher UA↔RU↔EN працює (не 404)
- [ ] `npm run build` без помилок

---

### КРОК 6 — DEPLOY

```bash
git add -A
git commit -m "redesign: [slug] to [mood] archetype

- Stitch export: docs/design-system/stitch-exports/[date]_[slug]/
- Baseline: docs/design-system/pages/[slug]-baseline.md
- Mood: [Industrial|Direct|Editorial]
- SEO-freeze: title/description/H1/schema preserved
"
git push
```

Vercel auto-deploy.

---

### КРОК 7 — POST-DEPLOY MONITORING (7-14 днів)

Відразу після деплою:

1. Зняти PageSpeed (новий) — порівняти з baseline. Має бути:
   - LCP < 2.5s, CLS < 0.1, INP < 200ms
   - Якщо гірше baseline на 20%+ → дослідити і зафіксити до моніторингу

2. Додати запис у `docs/design-system/pages/[slug].md`:
   - Archetype + mood
   - Stitch export link
   - Approval date
   - Deploy date
   - PageSpeed after

3. Моніторинг **7 днів** щоденно:
   - GSC: positions для primary keyword
   - GA4: form CR, bounce, scroll 75%
   - Якщо **CR -15%** АБО **positions -20%** → **ROLLBACK**

4. Rollback процедура (якщо тригер):
   ```bash
   git revert [commit-hash]
   git push
   ```
   Створити `docs/design-system/pages/[slug]-rollback.md` з аналізом що не спрацювало.

5. Через 28 днів без rollback-тригера — відмітити в ADR як "validated".

---

## ФІНАЛЬНИЙ ЗВІТ

```
## ✅ РЕДИЗАЙН ЗВІТ: [slug]

### Mood: [Industrial|Direct|Editorial]
### Stitch export: docs/design-system/stitch-exports/[date]_[slug]/

### SEO-freeze (всі незмінні):
✅ URL: [same]
✅ H1: [same text]
✅ Title: [X симв, same]
✅ Description: [X симв, same]
✅ Schema.org: перенесено
✅ Hreflang: uk/ru/en/x-default — взаємопосилання ок

### PageSpeed (before → after):
Mobile  Performance: X → X  | LCP: X.Xs → X.Xs | CLS: X → X | INP: Xms → Xms
Desktop Performance: X → X  | LCP: X.Xs → X.Xs | CLS: X → X | INP: Xms → Xms

### Перелінковка:
✅ Language switcher (UA↔RU↔EN): працює
✅ Mega-menu: присутня

### Моніторинг:
Baseline: docs/design-system/pages/[slug]-baseline.md
Rollback trigger: CR -15% АБО positions -20% за 7 днів
Next check: через 7 днів (автоматично нагадати)

### Deploy:
https://www.fulfillmentmtp.com.ua[URL]
```

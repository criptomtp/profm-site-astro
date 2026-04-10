# Команда: /create-page

Створює нову сторінку або статтю блогу повністю автономно.
Запускає Multi-Agent Pipeline без зупинок.

## Використання:
```
/create-page "Топ-10 маркетплейсів України"
/create-page "Фулфілмент для Rozetka" --type=blog
```

---

## PIPELINE — виконувати повністю без зупинок:

### АГЕНТ 1 — RESEARCHER
1. WebSearch топ-5 конкурентів Google UA + топ-3 RU + топ-3 EN
2. Для кожного: URL, кількість слів, структура H2/H3, ключові тези
3. Факти і статистика з авторитетних джерел
4. docs/MTP_SEMANTIC_CORE_FULL.md — релевантні ключові слова
5. Перевір які сторінки вже є — не повторювати структуру
6. Збережи в .claude-flow/research/[slug].json

---

### АГЕНТ 2 — ANALYZER + ДИЗАЙН КОНЦЕПЦІЯ
1. Середня довжина конкурентів, теми яких не розкривають
2. План: мін. +20% слів від середнього конкурента
3. Ключові слова і LSI
4. Перевір docs/LANGUAGE_AUDIT.md
5. **Придумай УНІКАЛЬНУ дизайн-концепцію:**
   - Назва стилю (напр. "Growth Ladder", "Split Hero")
   - Унікальна структура — не копіювати жодну існуючу сторінку сайту
   - Унікальний hero layout
   - 1 WOW-елемент (калькулятор, порівняльна таблиця, таймлайн, animated stats)
   - Опиши концепцію ТЕКСТОМ → чекай "approved"

---

### АГЕНТ 3 — WRITER (три окремі продукти для трьох аудиторій)

**КРИТИЧНО: НЕ переклади. Три окремі сторінки з різними кутами атаки.**

**🇺🇦 UA** (src/pages/ua/[slug].astro):
- Аудиторія: українські підприємці, e-commerce в Україні
- Кут: практична користь — гривня, Нова Пошта, Rozetka, Prom.ua, реалії воєнного часу
- Тон: діловий але теплий
- SEO: українські запити, Google.com.ua
- Мін. 1200 слів, унікальна структура H2/H3

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

### АГЕНТ 5 — DESIGN (після "approved" на концепцію)

**Правила унікального дизайну:**
- Подивись на всі існуючі сторінки — твоя ВІДРІЗНЯЄТЬСЯ від всіх
- Hero: інший layout ніж text+image
  Варіанти: split-screen, full-screen overlay, centered велика типографіка, animated counters
- Нові компоненти яких немає на сайті:
  Варіанти: timeline, comparison table, step-by-step, stats grid, FAQ accordion, flip cards
- Колір: ТІЛЬКИ #e63329 + #000 + #fff
- 1 WOW-елемент що запам'ятовується
- Mobile-first, без важких бібліотек

**ОБОВ'ЯЗКОВО додати на сторінку:**
- Перемикач мов (ua/ru/en) — посилання на всі три версії
- Додати сторінку в навігацію/хедер сайту (знайди компонент Header.astro або nav)
- Breadcrumbs з посиланням на головну

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
- [ ] Mobile: grid→stack на 768px, кнопки 44px+

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
UA: /ua/[slug]/ — X слів | для українських підприємців
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
https://fulfillmentmtp.com.ua/ua/[slug]/
https://fulfillmentmtp.com.ua/ru/[slug]/
https://fulfillmentmtp.com.ua/en/[slug]/
```

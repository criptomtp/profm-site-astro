# Pillar/Topic Page — Quality Gate Checklist

**Призначення.** 8-пунктний чек-ліст, що ловить 6 категорій повторюваних дефектів виявлених аудитом 2026-05-01 на 8+ нових pillar-сторінках поспіль (Rozetka, Prom, online-store, cosmetics, small-biz, marketplaces, clothing, /poslugy/).

**Коли застосовувати.** Будь-яка нова **pillar/topic-сторінка** (сервісна або індустріальна landing з SEO-метою). Запускати перед commit і після deploy.

**Коли НЕ застосовувати.** Блог-пости, FAQ, legal/privacy, redirect-сторінки. Для них окремі (м'якіші) правила.

**Автоматичний чек:**
```bash
./scripts/pillar-page-validate.sh URL_OR_FILE
./scripts/pillar-page-validate.sh --triplet UA_URL RU_URL EN_URL
```

Exit code 0 = pass, 1 = fail. Інтеграція в pre-commit hook або post-deploy перевірку.

---

## A. Schema parity — 9 обов'язкових `@type`

Кожна pillar-сторінка має містити в JSON-LD ВСІ 9 типів:

1. `Organization` — у `provider` поля Service
2. `LocalBusiness` — окремий `<script>` з даними MTP
3. `GeoCoordinates` — точні координати (latitude/longitude)
4. `PostalAddress` — адреси складів (Щасливе + Білогородка — масив з двох)
5. `BusinessAudience` — опис цільової аудиторії
6. `Service` — основний `@type` сторінки
7. `Offer` — ціна або діапазон цін
8. `FAQPage` — мінімум 5 Q/A
9. `Country` — у `areaServed`

**Pattern для LocalBusiness:** 2-warehouse (Щасливе 2,700 м² + Білогородка 1,000 м²) як на `maloho-biznesu`/`marketpleysiv`. **НЕ** старий single-Бориспіль pattern з `kosmetyky` — той містить лише 1 локацію.

---

## B. UA/RU/EN parity — однаковий рівень якості 3 мовами

❌ Помилка з аудиту: на cosmetics/online-store/small-biz/marketplaces EN був 3 000+ слів і 13+ schemas, а UA/RU — 1 200-1 700 слів і 9-11 schemas. Це cannibalization — Google ранжує EN на UA-запити.

**Правило для нової triplet:** UA + RU + EN мають бути на однаковому рівні **одночасно**:
- Words: ≥2 500 кожна
- Schemas: ≥9 must-have кожна
- H1: brand-hook кожна (а не "Фулфілмент для X")
- Унікальний контент per мова (memory rule — НЕ переклад)

Деплой по одній мові → відкат, доробити решту, потім merge всіх 3 разом.

---

## C. H1 — brand-hook, не generic

❌ Заборонено: іменникова конструкція без зачіпки.
- «Фулфілмент для одягу»
- «Послуги фулфілменту»
- «MTP Group — фулфілмент»
- «Что мы предлагаем»
- «Our services»

✅ Обов'язково: дієслово в наказовому або парадокс/twist через пунктуацію (кома, тире, em-dash).
- «Фулфілмент для одягу, де розмір М завжди М» — comma + paradox
- «One inventory pool. Five marketplaces. Zero duplicate stock.» — staccato + paradox
- «Stop guessing your batch dates. Start shipping cosmetics fresh.» — imperative
- «Гараж не масштабується. Ми — так.» — paradox

**Heuristic перевірка** (у скрипті):
- H1 has > 5 words AND
- H1 contains comma / em-dash / colon / period mid-text OR starts with imperative verb

Інакше — flag як generic.

---

## D. H1 whitespace bug

❌ Кейси з аудиту:
- `tsiny`: «фулфілментдля інтернет-магазинів»
- `about`: «фулфілментсклад MTP Group»
- `shcho-take-fulfilment`: «фулфілмент.Повний гід»
- `fulfilment-prom`: «Prom.uaне існує.До сьогодні»

Корінь: Astro-компонент конкатенує `{var1}{var2}` без пробілу. Скрипт ловить через regex:
```python
re.findall(r'\.[A-ZА-ЯҐЄІЇ]|[a-zа-яґєії][A-ZА-ЯҐЄІЇ]', h1_text)
```

Якщо знайдено хоч одне — fail. Глобальний фікс — у H1-шаблоні Astro-компонента додати space-padding між змінними.

---

## E. Language purity — не змішувати EN/UA/RU

❌ Кейс з аудиту: `/poslugy/` мав «Повний spectrum фулфілмент-послуг». Слово "spectrum" — EN.

**Правило:**
- В UA: заборонені звичайні англіцизми (spectrum, features, benefits, awesome, growth-hub, seamless, robust, world-class). Дозволені: бренди (MTP, Prom, Rozetka, Horoshop, Shopify), технічні терміни (API, FBO, FBS, WMS, 3PL, FEFO, SLA, ERP, CRM, KPI).
- В RU: те саме з тими ж дозволами.
- В EN: окрім брендів і назв українських міст (Boryspil, Schaslyve, Bilohorodka, Kyiv) — все англійською.

**Не використовувати auto-translate** для нонсенс-фраз типу «Масштабируй с точной силой логистики Precision». Краще написати з нуля російською.

---

## F. Hreflang quartet — 4 reciprocal alternates

Кожна pillar-сторінка має 4 hreflang-альтернативи:

```html
<link rel="alternate" hreflang="uk" href="https://www.fulfillmentmtp.com.ua/<UA-slug>/" />
<link rel="alternate" hreflang="ru" href="https://www.fulfillmentmtp.com.ua/ru/<RU-slug>/" />
<link rel="alternate" hreflang="en" href="https://www.fulfillmentmtp.com.ua/en/<EN-slug>/" />
<link rel="alternate" hreflang="x-default" href="https://www.fulfillmentmtp.com.ua/<UA-slug>/" />
```

**Reciprocal check** (через `--triplet` режим скрипта): усі 3 sibling-сторінки мають віддавати **ідентичну** множину 4-х URL.

Поломка: якщо UA вказує на `/ru/X/`, а `/ru/X/` вказує на `/ru/Y/` — Google не зможе зв'язати triplet, ранжуватиметься некоректно.

---

## G. Internal linking — 4 hub-посилання

Без internal links нова pillar-сторінка може застрягти у "Crawled — not indexed" (приклад з аудиту: `/fulfilment-prom/` × 3 застрягли).

**При створенні нової pillar обов'язково додати посилання з:**

1. `/ua/3pl-logistyka/` — у блок «Категорії послуг»
2. `/poslugy/` — у блок «За індустрією»
3. `/` (homepage UA) — у footer або категорії
4. **Найближча topic-сестра** — наприклад нова clothing → лінк на cosmetics (обидва — DTC fashion/beauty); нова furniture → лінк на marketplaces

Без 4-х hub-посилань — не deploy.

---

## H. Pre-commit checklist (TL;DR)

Перед `git commit` будь-якої нової pillar-triplet:

- [ ] **9 schemas** — `Organization, LocalBusiness, GeoCoordinates, PostalAddress, BusinessAudience, Service, Offer, FAQPage, Country` на КОЖНІЙ з 3 мов
- [ ] **2 500+ слів** на КОЖНУ мову
- [ ] **H1 brand-hook** — дієслово/парадокс, не «Фулфілмент для X», на КОЖНІЙ мові
- [ ] **H1 whitespace** — без `слово.Слово` конкатенації
- [ ] **EN/UA/RU не змішувати** — окрім брендів/тех-термінів
- [ ] **Hreflang quartet** — 4 alternates reciprocal між UA/RU/EN
- [ ] **Internal links** — додано з 4 hubs (3pl-logistyka, poslugy, home, sibling)
- [ ] **Запустити** `npm run validate:pillar -- --triplet UA_URL RU_URL EN_URL` → exit 0

Якщо хоч один пункт FAIL — НЕ деплоїмо, доробляємо.

---

## Інтеграція

**Локально:**
```bash
# Single page
./scripts/pillar-page-validate.sh https://www.fulfillmentmtp.com.ua/fulfilment-dlya-odyahu/

# Triplet (UA + RU + EN)
./scripts/pillar-page-validate.sh --triplet \
  https://www.fulfillmentmtp.com.ua/fulfilment-dlya-odyahu/ \
  https://www.fulfillmentmtp.com.ua/ru/fulfilment-dlya-odezhdy/ \
  https://www.fulfillmentmtp.com.ua/en/fulfilment-for-clothing/

# Or against built dist (faster, no deploy needed)
./scripts/pillar-page-validate.sh dist/fulfilment-dlya-odyahu/index.html
```

**Через npm:**
```bash
npm run validate:pillar -- URL_OR_FILE
npm run validate:pillar -- --triplet UA RU EN
```

**Майбутнє — CI:**
- GitHub Actions workflow на push → build → run validate:pillar для нових pillar-файлів → fail PR якщо exit ≠ 0.
- На цьому етапі тримаємо як manual-check + post-deploy перевірку. Інтеграція в CI — окрема задача.

---

## Maintenance

Ставити цей checklist живим:
- Нові AI-tells / banned words → додавати в скрипт + цей doc
- Нові pillars (наприклад furniture, electronics) → перевіряти на цьому ж скрипті
- Перегляд раз на квартал, після кожного site-аудиту

**Останнє оновлення:** 2026-05-01.

# GBP Upload Checklist

Все готове — залишилось `copy-paste` у UI. Час: ~45 хвилин на одну філію.

## 📁 Файли готові

Папка: `public/images/gbp/`
13 фото, конвертовані в JPG 90% quality, max 2000px.

Captions: `public/images/gbp/photo-queue.json` (UA + RU для кожної).

Copy для постів: `docs/gbp/gbp-posts-queue.md` (4 готових поста).

## 🚀 Execution (роби в цьому порядку)

### Крок 1: Rename обох філій (5 хв)

1. `business.google.com/` → група "MTP Group фулфилмент"
2. MTPFUL1 → "До свого профілю" → "Редагувати профіль" → Name
3. Змінити з `Фулфилмент MTP Group` на `MTP Group Fulfillment`
4. Зберегти (Google може відправити на review — ok)
5. Те саме для MTPFUL2

### Крок 2: Upload photos (25 хв на обидві філії)

**MTPFUL1 (Щасливе):** (пріоритетний порядок)
- [ ] `mtp-fulfillment-warehouse-hero.jpg` → Cover
- [ ] `warehouse-mtp-boryspil.jpg` → Exterior
- [ ] `mtp-warehouse-exterior.jpg` → Exterior
- [ ] `mtp-warehouse-interior.jpg` → Interior
- [ ] `warehouse-mtp-storage.jpg` → Interior
- [ ] `mtp-packing-process.jpg` → At work
- [ ] `warehouse-mtp-packing.jpg` → At work
- [ ] `mtp-warehouse-team-work.jpg` → Team at work
- [ ] `warehouse-mtp-team.jpg` → Team at work
- [ ] `mtp-team-ukraine.jpg` → Team
- [ ] `mtp-founder-nikolai-warehouse.jpg` → Owner
- [ ] `mtp-generator-backup.jpg` → Additional (blackout-proof)
- [ ] `mtp-starlink-warehouse.jpg` → Additional (connectivity)

**MTPFUL2 (Білогородка):** (без exterior і owner, ті тільки MTPFUL1)
- [ ] `mtp-fulfillment-warehouse-hero.jpg` → Cover
- [ ] `mtp-warehouse-interior.jpg` → Interior
- [ ] `warehouse-mtp-storage.jpg` → Interior
- [ ] `mtp-packing-process.jpg` → At work
- [ ] `warehouse-mtp-packing.jpg` → At work
- [ ] `mtp-warehouse-team-work.jpg` → Team at work
- [ ] `warehouse-mtp-team.jpg` → Team at work
- [ ] `mtp-team-ukraine.jpg` → Team
- [ ] `mtp-generator-backup.jpg` → Additional
- [ ] `mtp-starlink-warehouse.jpg` → Additional

**Режим upload**: по 2-3 фото на день, не батчом (виглядає natural для Google).

**Captions**: відкрий `public/images/gbp/photo-queue.json`, скопіюй `caption_uk` (або `caption_ru`) для кожного файлу.

### Крок 3: Fill description (5 хв)

1. MTPFUL1 → Редагувати → "Про компанію" → description
2. Скопіювати з `docs/gbp/optimization-plan.md` → Action 4.3 → MTPFUL1 block
3. Вставити → Зберегти
4. Повторити для MTPFUL2 (інший текст)

### Крок 4: Services (5 хв на філію)

1. У розділі "Редагування послуг" додати з списку (з plan, Action 4.4):
   - Приймання товару
   - Зберігання
   - Упаковка замовлень
   - Відправка
   - Обробка повернень
   - Автодозвон клієнтам
   - Штрихкодування
   - Фотофіксація товару
   - Прийом платежів
   - Доукомплектація

### Крок 5: Перший GBP Post (5 хв)

1. Відкрити `docs/gbp/gbp-posts-queue.md`
2. Скопіювати "Post 1" заголовок + body
3. MTPFUL1 → "Додати оновлення"
4. Вставити
5. Додати photo: `mtp-generator-backup.jpg`
6. CTA button: "Докладніше" → `https://www.fulfillmentmtp.com.ua/ua/tsiny/`
7. Опублікувати
8. MTPFUL2 — повторити з Post 2 (Ціни)

### Крок 6: Review request — MTPFUL2 пріоритет (15 хв)

1. MTPFUL2 → "Збирати відгуки" → "Поширити"
2. Скопіювати короткий URL (типу `g.page/r/xxx/review`)
3. Відкрити KeyCRM / email список останніх 20 клієнтів MTPFUL2
4. Написати кожному (персоналізовано):

```
Привіт, %NAME%!
Дякуємо що обрали MTP Group Fulfillment для свого бізнесу.
Якщо вам все сподобалось — залишите, будь ласка, короткий відгук
(30 секунд): [SHORT_URL]
Ваш відгук допомагає новим клієнтам обирати нас впевнено.
— Микола, MTP Group
```

Ціль: 5 відгуків за 7 днів.

### Крок 7: Google Ads paused campaign (5 хв)

1. Відкрити `ads.google.com/`
2. Знайти "ProfM | Фулфилмент"
3. Рішення:
   - **Restart**: якщо був robust performer до паузи → Enable + перевірити budget
   - **Archive**: якщо paused через non-performance → Archive
4. Або зв'язатися зі мною якщо треба аналіз historical data

---

## Summary

- Фото: 13 файлів готові в `public/images/gbp/`
- Captions: в `photo-queue.json`
- Post copy: 4 готових пости в `gbp-posts-queue.md`
- Описи філій: в `optimization-plan.md`
- Services list: в `optimization-plan.md`

Хвиля 1 (зробити сьогодні): rename + 3 фото на кожну + 1 post на кожну + 10 SMS for MTPFUL2 reviews.

Хвиля 2 (тиждень 1): ще 5 фото кожній + fill description + services.

Хвиля 3 (тиждень 2-4): поступове додавання постів і нових відгуків.

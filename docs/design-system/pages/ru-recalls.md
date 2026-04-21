---
page: /ru/recalls/
archetype: Editorial
stitch_project: 16366500142707399412
stitch_screen: 39207901ffb8479097100bf2240b05c1
approval_date: 2026-04-20
status: live
driver: GSC Coverage Drilldown 8 — "Копія. Система Google вибрала іншу канонічну" (RU page was near-identical translation of UA, Google chose UA as canonical)
---

# ADR — `/ru/recalls/` Editorial redesign

## Причина
У GSC Drilldown 8 (2026-04-20) сторінка `https://www.fulfillmentmtp.com.ua/ru/recalls/` позначена статусом "Копія. Google вибрав іншу канонічну". Попередня RU-версія була ~95% перекладом UA (та сама структура: video grid 6 плиток → text reviews → case grid), тому Google вибрав UA як канонічну і виключив RU з індексації.

Мета редизайну: нова структура, новий тон, унікальний контент, щоб Google бачив RU як самостійну сторінку.

## Archetype
**Editorial** — великі типографічні акценти (DM Serif Display), відсутність hero image, читабельність як головна задача. Відхилення від дефолтного Editorial (`src/pages/en/faq.astro`): у `/ru/recalls/` використовуємо інтегровані відеороліки всередині кейс-сток (не FAQ-accordion), оскільки сторінка — це довга форма кейс-стади з візуальним доказом.

## Візуальний референс
- Stitch project: `16366500142707399412` ("MTP Manifesto")
- Approved screen: `39207901ffb8479097100bf2240b05c1` ("v2-with-videos")
- Локальний експорт: `docs/design-system/stitch-exports/2026-04-20_ru-recalls/`
  - `concept.md` — ТЗ
  - `v1-data-only/` — перша ітерація без відео (rejected)
  - `v2-with-videos/` — фінальна схвалена версія

## Структура сторінки
1. Top rule + label `РАЗБОР · CLIENT CASE STUDIES`
2. Editorial hero — `150 клиентов. 10 лет. 60 000+ отправок в пик.` без зображення, без форми
3. **Case 1 Carter's** — split 7/5: video left + текст з drop cap + pull quote + метрики 4×
4. Data Wall — таблиця 8 клієнтів (ніша / старт / зараз / лет / задача)
5. **Case 2 Elemis** — flipped split 1/1: text left + video right + метрики 4×
6. **Case 3 ORNER** — центроване video 960px + full-width prose + pull quote
7. Sector breakdown на чорному тлі — horizontal bar chart, 6 сегментів
8. Archive strip — 6 відео-thumbnails (5 реальних YT ID + 1 "See all")
9. Methodology — OTIF 99.8% / Pick Accuracy 0.02% / Cycle 1.5 h
10. Dark CTA з формою (єдина форма на сторінці)

## Відмінність від `/ua/recalls/`

| Аспект | UA | RU (v2 Editorial) |
|---|---|---|
| Hero | Video grid 6 плиток | Editorial typography "150 клиентов. 10 лет." |
| Архітектура | Hero-grid-first | Hero → 3 deep cases з інтегрованими відео → data → chart → archive |
| Формат відео | 6 окремих плиток в grid | 3 великих у кейсах + 6 малих у архівній смузі |
| Клієнти показані | 6 коротких | 3 deep-dive (Carter's/Elemis/ORNER) + таблиця 8 + архів 5 |
| Тон | Емоційний | Аналітичний + видеодоказательство |
| Об'єм | ~600 слів | ~1500+ слів оригінального RU (не переклад) |
| H2/H3 | "Посмотрите что говорят" | "Данные вместо обещаний", "Три метрики, по которым мы отчитываемся" |

## Фіксовані токени
- Колір: `#e63329` (red, CTA + акценти) / `#000` / `#fff` + `#fafafa` (data wall бекграунд) + `#e5e5e5` (divider lines)
- Типографіка: `DM Serif Display` (H1/H2/pull quotes/metrics), `DM Sans` (body)
- Scope: усі CSS-класи мають префікс `.ed-` щоб не конфліктувати з глобальними `.hero`, `.cases` тощо

## Shared компоненти
- `Base.astro` (layout + Header/Footer + skip-link + глобальні токени `--fd/--fb/--red`)
- Header + Footer — автоматично з Base, нічого не змінено
- Відеомодал — вбудований inline script, embed через YouTube IFrame API

## Deviations from default Editorial archetype
- `src/pages/en/faq.astro` рекомендує StatsBar + AccordionGroup. Тут вони не використовуються, бо сторінка це не Q&A, а кейс-стади. Замість Accordion — 3 наративні кейси з drop cap.
- Дозволена форма в самому кінці (Dark CTA) — це фінальна конверсійна точка, не "форма над фолдом", яку забороняє архетип.
- Використано бар-чарт на чорному тлі (sector breakdown) — нетипово для Editorial, але необхідно щоб візуально відокремити data-секцію від наративної.

## Rollback criteria
- Якщо CR зі сторінки падає >15% протягом 7 днів після деплою → revert до попередньої версії (коміт перед цим редизайном).
- Якщо GSC Coverage через 30 днів все ще показує "Копія, Google вибрав іншу канонічну" → треба буде переглянути hreflang або об'єднати RU ↔ UA канонікли.

## Real YouTube IDs (використані) — оновлено 2026-04-20
**Тільки реальні відеоінтервʼю, контент згенерований з транскриптів:**
- Case 1: `k7ET02dWB7k` — **Павел Мокриенко**, власник інтернет-магазину БАДів, ~1 рік з MTP. Транскрипт `/tmp/yt_transcripts/k7ET02dWB7k.uk.vtt`. Ключова цитата: «Затратная часть снизилась раза в три. Время на отправки — ушло в ноль».
- Case 2: `mE4N4CHwG7o` — **Антон, Monkey Family**, товарний бізнес, ~8–9 місяців з MTP, тестував 3 інших фулфілменти до цього. Транскрипт `/tmp/yt_transcripts/mE4N4CHwG7o.ru.vtt`. 1С-інтеграція, пік 600 відправок/день.
- Case 3: `7t3z8weL8Pw` — **Антон (товарка Китай)**, 20 → 600 відправок/день, починав зі складу на балконі. Транскрипт `/tmp/yt_transcripts/7t3z8weL8Pw.ru.vtt`.
- Archive strip: `k7ET02dWB7k`, `bUMM8S91quo` (Влад Савицький), `K3KHxItl2nk` (Максим), `KhYY0MsjLmU` (Ігор Бакалов), `bHY3cFF9SlI` (Екскурсія по складу)
- "See all" → https://www.youtube.com/@mtpgroup

### ⚠️ Важливо: попередні кейси були фіктивні
До ітерації 2026-04-20 Cases 2/3 мали бренди «Elemis» / «ORNER» з довільно призначеними YouTube ID — **цього не повинно було бути**. User виявив фейк ("ти пишеш Елеміс, але по факту у нас немає відеовідгуку Елеміс"). Поточна версія — тільки реальні відеоінтервʼю, контент написаний з розшифровок через `yt-dlp --write-auto-sub` (UA/RU субтитри).

### Як відтворити транскрипти
```bash
for vid in k7ET02dWB7k mE4N4CHwG7o 7t3z8weL8Pw; do
  yt-dlp --skip-download --write-auto-sub --sub-format vtt \
    --sub-lang "ru,uk,en" \
    -o "/tmp/yt_transcripts/%(id)s.%(ext)s" \
    "https://www.youtube.com/watch?v=$vid"
  sleep 15  # rate-limit safety
done
```

## Next steps after deploy
1. GSC → Inspect URL `https://www.fulfillmentmtp.com.ua/ru/recalls/` → Request Indexing
2. GSC → Coverage → "Копія, Google вибрав іншу канонічну" → Validate Fix для `/ru/recalls/`
3. Monitor CR (Яндекс.Метрика / GA4 / Telegram) 7 днів
4. Повторити той самий workflow для `/ru/about/` (Drilldown 8, 2-й URL у списку)
5. Потім для `/ru/guide/` (3-й URL)

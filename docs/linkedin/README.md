# LinkedIn Company Page — контент-конвеєр

**Page:** https://www.linkedin.com/company/mtpgroupfulfillment/ (ID: 112973784)

## Папки

- `queue/` — готові пости у черзі на публікацію. Формат: `YYYY-MM-DD_slug.md`
- `published/` — архів опублікованих (переносити після `linkedin-post.py`)
- `post-template.md` — шаблон для нових постів

## Публікація

```bash
# подивитись чергу
ls docs/linkedin/queue/

# опублікувати
python3 scripts/linkedin-post.py --from-file docs/linkedin/queue/2026-04-25_pillar-ua.md

# після успіху — перенести в архів
mv docs/linkedin/queue/2026-04-25_pillar-ua.md docs/linkedin/published/
```

## Ритм

- **Макс 2-3 пости/тиждень** — LinkedIn детектить бот-ритм, треба варіювати час
- Оптимальні вікна для UA B2B: **вт-чт 9:00-11:00 або 14:00-16:00**
- Не постити 2 дні підряд у той самий час
- Уникати вихідних (субота/неділя — engagement низький для B2B)

## Формат поста

- **Перші 2 рядки** — критичні (preview у стрічці до кліку "see more")
- **Довжина** — 1 200-2 000 символів (LinkedIn bias на mid-length)
- **Абзаци короткі** — 1-2 рядки, багато пробілів
- **Хештеги** — 3-5 у кінці, не розкидати по тексту
- **Посилання** — у кінці, 1 штука на пост
- **Мова** — UA для українського ринку, EN для міжнародних кейсів. RU пропустити.

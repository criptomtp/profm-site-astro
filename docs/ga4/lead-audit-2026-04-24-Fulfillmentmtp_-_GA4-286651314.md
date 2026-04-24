# GA4 Lead Audit — Fulfillmentmtp - GA4

- Property ID: `286651314`
- Account: Fulfillmentmtp
- Time zone: Europe/Kiev · Currency: USD
- Period: last 14 days · generated 2026-04-24T11:08:04

## 1. Всі події за останні 14 днів (топ-25 за кількістю)

| Event Name | Events | Users |
|---|---:|---:|
| `page_view` | 185 | 37 |
| `user_engagement` | 137 | 19 |
| `session_start` | 66 | 39 |
| `scroll` | 34 | 4 |
| `first_visit` | 29 | 29 |

## 2. `form_submit` — деталі за 14 днів

- Всього `form_submit`: **0**
- Унікальних користувачів: **0**

🚨 **0 подій form_submit** — подія не долітає до GA4. Можливі причини:
  - Adblock/ITP блокує gtag
  - Race condition — форма відправлена раніше ніж gtag завантажився
  - Помилка у коді `mtpSubmitLead`
  - Події надходять у інший property ID

### 2a. По сторінках (topic: звідки йдуть ліди)

_(немає даних)_

### 2b. По джерелу трафіку

_(немає даних)_

### 2c. По днях (тренд за 14 днів)

_(немає даних)_

## 3. `generate_lead` за 14 днів

🚨 0 подій generate_lead

## 4. Key Events (Conversions) за 14 днів

🚨 Жодного Key Event не зафіксовано за період

## 5. Realtime (останні 30 хв)

❌ 400 Selected dimensions and metrics cannot be queried together.

### 2d. Детальний лог: останні form_submit з джерелом і landing page

_(жодного form_submit за період)_

## 7. Google Search Console — топ запити які приводять на сайт

_Organic keywords агреговано з GSC. Per-user keyword відсутній — Google шифрує "(not provided)" з 2011._

❌ GSC помилка: ('invalid_grant: Token has been expired or revoked.', {'error': 'invalid_grant', 'error_description': 'Token has been expired or revoked.'})

## 8. AI-пошук і реферали (Perplexity, ChatGPT, Bing Copilot, Gemini)

_(жодного візиту з AI-пошуку — або їх ще немає, або CSP блокував до 2026-04-24 10:40)_

## 9. Google Ads — ключові слова з реклами

_(жодного Google Ads keyword — або реклама не лила трафік за період, або auto-tagging GCLID вимкнено)_

Перевірка: Google Ads → Account Settings → Tracking → Auto-tagging має бути ON.

## 6. Діагностика і рекомендації

- **Якщо секція 2 показує >0 form_submit але секція 4 не містить їх** → подія є, але не марковано як Key Event. Admin → Events → toggle «Mark as key event».
- **Якщо секція 2 = 0** → події не долітають. Перевір DevTools → Network → filter `collect?` на `https://region1.google-analytics.com/g/collect`. Якщо там нічого під час submit — gtag не завантажений (adblock, slow network, race condition).
- **Якщо realtime (секція 5) працює, а історія (секція 1) — ні** → фільтр Internal Traffic чи DebugView режим виключає продакшн-трафік. Admin → Data Filters.
- **Перевірити стан на продакшн**: відкрити сайт у Chrome Incognito + DevTools Network, submit форму, очікувати POST на `g/collect?...en=form_submit` зі status 204/200.

# СЕМАНТИЧНЕ ЯДРО MTP GROUP — ПОВНА МАТРИЦЯ
## На основі аналізу ShipBob (USA), конкурентів UA, видачі Google та AI-пошуку
## Дата: 2026-03-27 (оновлено 2026-04-30)

---

## МЕТОДОЛОГІЯ

Кожне ключове слово = окрема посадкова сторінка (landing page).
Модель ShipBob: 200+ SEO-сторінок, кожна таргетує 1 кластер запитів.
Адаптація для MTP Group: 120+ сторінок UA + вибірково EN.

**Status legend** (додано 2026-04-30):
- ✅ Done — створено всі 3 мовні версії (UA + RU + EN), задеплоєно
- 🚧 In Progress — у роботі зараз
- 🟡 Partial — є тільки 1-2 мови або тільки як blog post
- (без іконки) — у backlog, пріоритет за кольором (🔴 high → 🔵 low)

---

## URL POLICY (оновлено 2026-04-22)

**Нові UA-сторінки** деплоюються в корінь без префіксу `/ua/`. Старі `/ua/*` сторінки **залишаються на місці** (grandfather clause).

| Мова | Шлях для нових сторінок | Приклад |
|---|---|---|
| UA (default) | `/[slug]/` | `/fulfilment-dlya-odyahu/` |
| RU | `/ru/[slug]/` | `/ru/fulfilment-dlya-odezhdy/` |
| EN | `/en/[slug]/` | `/en/fulfilment-for-clothing/` |

> ⚠️ Slug-колонка нижче зберігає історичні `/ua/*` префікси для довідки. При створенні нової сторінки **дроп префікс `/ua/`** і деплой у корінь.

---

## ВІСЬ 1: ЗА ТОВАРНОЮ КАТЕГОРІЄЮ (26 сторінок)

| # | Slug | Ключовий запит | LSI/довгий хвіст | Пріоритет |
|---|------|---------------|-------------------|-----------|
| 1 | /ua/fulfilment-dlya-kosmetyky/ | фулфілмент косметика Україна | зберігання косметики на складі, логістика б'юті товарів, фулфілмент крему, сироваток | ✅ |
| 2 | /fulfilment-dlya-odyahu/ | фулфілмент одяг взуття | UA + RU + EN deployed 2026-05-01, Direct mood, Stitch V1 | ✅ |
| 3 | /ua/fulfilment-dlya-elektroniky/ | фулфілмент електроніка | логістика гаджетів, зберігання техніки, фулфілмент смартфонів, аксесуарів | 🟠 |
| 4 | /ua/fulfilment-dlya-dytyachykh-tovariv/ | фулфілмент дитячі товари | логістика іграшок, зберігання дитячого одягу, фулфілмент для дитячих магазинів | 🟡 |
| 5 | /ua/fulfilment-dlya-sportu/ | фулфілмент спортивні товари | логістика спортивного обладнання, зберігання тренажерів, фулфілмент фітнес | 🟡 |
| 6 | /ua/fulfilment-dlya-domu/ | фулфілмент товари для дому | логістика домашнього декору, меблів, текстилю для дому | 🟡 |
| 7 | /ua/fulfilment-zootovariv/ | фулфілмент зоотовари | логістика кормів для тварин, зберігання зоотоварів | 🟡 |
| 8 | /ua/fulfilment-produktiv-kharchuvannya/ | фулфілмент продуктів харчування | логістика їжі, зберігання снеків, фулфілмент healthy food | 🔵 |
| 9 | /ua/fulfilment-knyzhok/ | фулфілмент книги | логістика книг, зберігання видань, фулфілмент для видавництв | 🔵 |
| 10 | /ua/fulfilment-avtozapchastyn/ | фулфілмент автозапчастини | логістика автодеталей, склад запчастин | 🔵 |
| 11 | /ua/fulfilment-sonyachni-paneli/ | фулфілмент сонячні панелі | логістика важких товарів, кейс EcoDrive | 🟠 |
| 12 | /ua/fulfilment-budmaterialiv/ | фулфілмент будівельних матеріалів | логістика будматеріалів, зберігання інструментів | 🔵 |
| 13 | /ua/fulfilment-medychnoho-obladnannya/ | фулфілмент медичне обладнання | логістика медтехніки, зберігання медтоварів | 🔵 |
| 14 | /ua/fulfilment-bijuteriyi/ | фулфілмент біжутерія аксесуари | логістика дрібних товарів, зберігання прикрас | 🔵 |
| 15 | /ua/fulfilment-parfumeriyi/ | фулфілмент парфуми | логістика ароматів, зберігання парфумерії | 🔵 |
| 16 | /ua/fulfilment-pobutovoi-khimiyi/ | фулфілмент побутова хімія | логістика мийних засобів | 🔵 |
| 17 | /ua/fulfilment-kantstovariv/ | фулфілмент канцтовари | логістика офісних товарів | 🔵 |
| 18 | /ua/fulfilment-handmade/ | фулфілмент хендмейд | логістика авторських товарів, крафтових виробів | 🔵 |
| 19 | /ua/fulfilment-dlya-kvitiv/ | фулфілмент квіти подарунки | логістика подарункових наборів, букетів | 🔵 |
| 20 | ~~/ua/fulfilment-dlya-vape/~~ | ~~фулфілмент вейп електронні сигарети~~ | ~~DROPPED 2026-04-30: ризикова ніша, виключено з ядра~~ | ⛔ |
| 21 | /ua/fulfilment-supplement/ | фулфілмент БАДів добавок | логістика спортивного харчування, вітамінів | 🟡 |
| 22 | /ua/fulfilment-mebliv/ | фулфілмент меблі | логістика великогабаритних товарів | 🔵 |
| 23 | /ua/fulfilment-posudu/ | фулфілмент посуд | логістика кухонних товарів, крихкого товару | 🔵 |
| 24 | /ua/fulfilment-tekstylyu/ | фулфілмент текстиль постільна білизна | логістика тканин, рушників | 🔵 |
| 25 | /ua/fulfilment-ihrashok/ | фулфілмент іграшки | логістика настільних ігор, дитячих товарів | 🔵 |
| 26 | /ua/fulfilment-vazhkykh-tovariv/ | фулфілмент важкі товари | ✅ ВЖЕ Є | ✅ |

---

## ВІСЬ 2: ЗА ТИПОМ БІЗНЕСУ (16 сторінок)

| # | Slug | Ключовий запит | LSI/довгий хвіст | Пріоритет |
|---|------|---------------|-------------------|-----------|
| 27 | /ua/fulfilment-dlya-internet-magazynu/ | фулфілмент для інтернет-магазину | логістика для e-commerce, склад для онлайн магазину | ✅ |
| 28 | /ua/fulfilment-dlya-marketpleysiv/ | фулфілмент для маркетплейсів | фулфілмент Rozetka, Prom, Kasta, OLX | ✅ |
| 29 | /ua/fulfilment-dlya-startapiv/ | фулфілмент для стартапів | логістика для початківців, мінімальний обсяг | 🟡 |
| 30 | /ua/b2b-fulfilment/ | B2B фулфілмент Україна | оптова логістика, фулфілмент для дистриб'юторів | 🟠 |
| 31 | /ua/fulfilment-dropshipping/ | фулфілмент для дропшипінгу | логістика без власного складу, дропшип Україна | 🟡 |
| 32 | /ua/fulfilment-dlya-vyrobnykiv/ | фулфілмент для виробників | логістика від виробництва до клієнта, D2C фулфілмент | 🟡 |
| 33 | /ua/fulfilment-dlya-brendiv/ | фулфілмент для брендів | преміум пакування, брендована логістика | 🟡 |
| 34 | /ua/fulfilment-dlya-fop/ | фулфілмент для ФОП | логістика для підприємців, мінімальні тарифи | 🟠 |
| 35 | /ua/fulfilment-dlya-optovykiv/ | фулфілмент для оптовиків | складське зберігання опту, B2B логістика | 🟡 |
| 36 | /ua/fulfilment-dlya-importeriv/ | фулфілмент для імпортерів | митне оформлення, зберігання імпортного товару | 🔵 |
| 37 | /ua/fulfilment-dlya-eksporteriv/ | фулфілмент для експорту | міжнародна логістика з України | 🔵 |
| 38 | /ua/fulfilment-dlya-podpysnykh-korobok/ | фулфілмент subscription box | логістика підписних коробок, бокси | 🔵 |
| 39 | /ua/fulfilment-dlya-sezonnykh-tovariv/ | фулфілмент сезонні товари | логістика на Чорну п'ятницю, піки продажів | 🔵 |
| 40 | /ua/fulfilment-dlya-crowdfunding/ | фулфілмент для краудфандингу | логістика Kickstarter, Indiegogo проєктів | 🔵 |
| 41 | /ua/fulfilment-dlya-sotsialnykh-proektiv/ | фулфілмент для благодійності | логістика гуманітарної допомоги | 🔵 |
| 42 | /ua/fulfilment-dlya-maloho-biznesu/ | фулфілмент для малого бізнесу | логістика без мінімального обсягу, доступний фулфілмент | ✅ |

---

## ВІСЬ 3: ЗА КАНАЛОМ ПРОДАЖУ / ПЛАТФОРМОЮ (12 сторінок)

| # | Slug | Ключовий запит | LSI/довгий хвіст | Пріоритет |
|---|------|---------------|-------------------|-----------|
| 43 | /fulfilment-rozetka/ | фулфілмент для Розетки | FBO Rozetka, логістика для селерів Rozetka (deployed at root, not /ua/) | ✅ |
| 44 | /fulfilment-prom/ | фулфілмент для Prom.ua | логістика для продавців Prom (deployed at root, not /ua/) | ✅ |
| 45 | /ua/fulfilment-shopify/ | фулфілмент Shopify Україна | інтеграція Shopify, 3PL для Shopify | 🟡 |
| 46 | /ua/fulfilment-woocommerce/ | фулфілмент WooCommerce | інтеграція WordPress, логістика WooCommerce | 🟡 |
| 47 | /ua/fulfilment-tiktok-shop/ | фулфілмент TikTok Shop | логістика для TikTok продавців | 🟡 |
| 48 | /ua/fulfilment-instagram-shop/ | фулфілмент Instagram Shop | логістика для Instagram продавців | 🟡 |
| 49 | /ua/fulfilment-hotline/ | фулфілмент для Hotline | логістика для Hotline продавців | 🔵 |
| 50 | /ua/fulfilment-kasta/ | фулфілмент для Kasta | логістика для Kasta | 🔵 |
| 51 | /ua/fulfilment-amazon/ | фулфілмент Amazon з України | FBA альтернатива, міжнародний фулфілмент | 🔵 |
| 52 | /ua/fulfilment-etsy/ | фулфілмент Etsy з України | логістика для Etsy продавців | 🔵 |
| 53 | /ua/fulfilment-olx/ | фулфілмент для OLX доставка | логістика для OLX продавців | 🔵 |
| 54 | /ua/fulfilment-opencart/ | фулфілмент OpenCart | інтеграція OpenCart | 🔵 |

---

## ВІСЬ 4: ЗА ПОСЛУГОЮ (17 сторінок)

| # | Slug | Ключовий запит | LSI/довгий хвіст | Пріоритет |
|---|------|---------------|-------------------|-----------|
| 55 | /ua/tsiny/ | ціна фулфілмент Україна | тарифи фулфілмент, вартість фулфілменту, скільки коштує | ✅ |
| 56 | /ua/calculator/ | калькулятор фулфілменту | ✅ ВЖЕ Є | ✅ |
| 57 | /ua/skladski-poslugy/ | складське зберігання Київ | оренда складу, відповідальне зберігання, зберігання палет (slug: skladski-poslugy) | ✅ |
| 58 | /ua/paletne-zberigannya/ | зберігання палет Київ Бориспіль | палетне зберігання, тарифи на палети (slug: paletne-zberigannya) | ✅ |
| 59 | /ua/komplektatsiya-zamovlen/ | комплектація замовлень | пікінг пакінг, збирання замовлень на складі | 🟠 |
| 60 | /ua/markuvannya-tovaru/ | маркування товару стікерування | етикетування, штрих-кодування, підготовка до маркетплейсу | 🟡 |
| 61 | /ua/povernennya-tovariv/ | повернення товарів reverse logistics | зворотна логістика, обробка повернень | 🟡 |
| 62 | /ua/avtodzvonok/ | автодзвінок підтвердження замовлень | кол-центр, підтвердження замовлень | 🟡 |
| 63 | /ua/intehratsii-api/ | інтеграції CRM API фулфілмент | API Нова Пошта, інтеграція з CRM, WMS | 🟡 |
| 64 | /ua/pakuvannya/ | пакування замовлень | брендоване пакування, коробки, наповнювачі | 🟡 |
| 65 | /ua/kros-doking/ | крос-докінг Київ | перевалка вантажів, транзит | 🔵 |
| 66 | /ua/kopaking/ | копакінг ко-пакінг | формування наборів, кітінг, бандлінг | 🟡 |
| 67 | /ua/pryom-tovaru/ | прийом товару на склад | вхідна логістика, перевірка якості | 🔵 |
| 68 | /ua/inventaryzatsiya/ | інвентаризація на складі | облік товарів, WMS система | 🔵 |
| 69 | /ua/dostavka-po-ukraini/ | доставка по Україні | логістика останньої милі, Нова Пошта, Укрпошта | 🟡 |
| 70 | /ua/mizhnarodna-dostavka/ | міжнародна доставка з України | експорт, cross-border e-commerce | 🔵 |
| 71 | /ua/obsluhovuvannya-zamovlen/ | обслуговування замовлень | обробка замовлень, SLA, швидкість | 🔵 |

---

## ВІСЬ 5: ЗА ГЕОГРАФІЄЮ (8 сторінок)

| # | Slug | Ключовий запит | LSI/довгий хвіст | Пріоритет |
|---|------|---------------|-------------------|-----------|
| 72 | /ua/fulfilment-kyiv/ | фулфілмент Київ | 3PL Київ, склад Київ, логістика Київ | ✅ |
| 73 | /ua/3pl-boryspil/ | 3PL Бориспіль | фулфілмент Бориспіль, склад біля аеропорту | 🟠 |
| 74 | /ua/fulfilment-bilohorodka/ | фулфілмент Білогородка | склад Білогородка, логістика Київська область | 🟡 |
| 75 | /ua/fulfilment-kyivska-oblast/ | фулфілмент Київська область | склад під Києвом, логістика передмістя | 🟡 |
| 76 | /ua/fulfilment-ukraina/ | фулфілмент Україна | 3PL оператор Україна, фулфілмент компанії України | ✅ |
| 77 | /ua/fulfilment-blyzko-do-aeroportu/ | фулфілмент біля аеропорту Бориспіль | швидка відправка, міжнародна логістика | 🔵 |
| 78 | /ua/fulfilment-lviv/ | фулфілмент Львів | (інформаційна: чому Київ краще для центральної логістики) | 🔵 |
| 79 | /ua/fulfilment-odesa/ | фулфілмент Одеса | (інформаційна: чому Київ краще) | 🔵 |

---

## ВІСЬ 6: ІНФОРМАЦІЙНІ ТА ПОРІВНЯЛЬНІ (24 сторінки)

| # | Slug | Ключовий запит | Формат | Пріоритет |
|---|------|---------------|--------|-----------|
| 80 | /ua/blog/scho-take-fulfilment/ | що таке фулфілмент | Гайд 2000+ слів (також pillar /ua/shcho-take-fulfilment/) | ✅ |
| 81 | /ua/blog/yak-vybrati-fulfilment/ | як вибрати фулфілмент оператора | Чеклист, критерії | ✅ |
| 82 | /ua/blog/fulfilment-vs-vlasnyy-sklad/ | фулфілмент або власний склад | Порівняння з калькулятором ROI | ✅ |
| 83 | /ua/blog/fulfilment-vs-dropshipping/ | фулфілмент vs дропшипінг | Порівняльна таблиця | 🟡 |
| 84 | /ua/blog/top-fulfilment-operatoriv-2026/ | ТОП фулфілмент компанії Україна | Рейтинг з об'єктивним аналізом (slug: top-fulfilment-operatoriv-2026) | ✅ |
| 85 | /ua/blog/vartist-fulfilmentu-2026/ | вартість фулфілменту 2026 | Огляд цін ринку, порівняння | ✅ |
| 86 | /ua/blog/mtp-vs-unipost/ | MTP Group vs Юніпост | Порівняння операторів | 🟡 |
| 87 | /ua/blog/mtp-vs-nova-poshta-fulfilment/ | MTP Group vs Нова Пошта фулфілмент | Порівняння з NP | 🟡 |
| 88 | /ua/blog/mtp-vs-flg/ | MTP Group vs Fast Lane Group | Порівняння операторів | 🔵 |
| 89 | /ua/blog/yak-perejty-na-fulfilment/ | як перейти з власного складу на фулфілмент | How-to гайд | ✅ |
| 90 | /ua/blog/yak-pidklyuchytysia-do-fulfilmentu/ | як підключитися до фулфілменту | Покрокова інструкція, 5 кроків | ✅ |
| 91 | /ua/blog/pomylky-pry-vybori-fulfilmentu/ | помилки при виборі фулфілмент оператора | Антигайд, 10 помилок | 🟡 |
| 92 | /ua/blog/ekonomiya-na-fulfilmenti/ | як заощадити на фулфілменті | Лайфхаки, оптимізація витрат | 🟡 |
| 93 | /ua/blog/fulfilment-chorna-pyatnytsia/ | фулфілмент на Чорну п'ятницю | Підготовка до піків продажів | 🟡 |
| 94 | /ua/blog/wms-systema-dlya-skladu/ | WMS система для складу | Огляд систем управління складом | 🔵 |
| 95 | /ua/blog/kpi-fulfilmentu/ | KPI фулфілменту які метрики | Як оцінити ефективність 3PL | 🔵 |
| 96 | /ua/blog/dogovir-z-fulfilment-operatorom/ | договір з фулфілмент оператором | На що звертати увагу в договорі | 🔵 |
| 97 | /ua/blog/trendy-ecommerce-2026/ | тренди e-commerce Україна 2026 | Огляд ринку, статистика | 🟡 |
| 98 | /ua/blog/logistyka-dlya-pochatkivtsiv/ | логістика для початківців | Як побудувати логістику з нуля | 🟡 |
| 99 | /ua/blog/chomu-fulfilment-deshevshyy/ | чому фулфілмент дешевший за власний склад | Юніт-економіка, розрахунки (slug: chomu-fulfilment-deshevshyy) | ✅ |
| 100 | /ua/blog/case-ecodrive/ | кейс EcoDrive сонячні панелі | Кейс клієнта, цифри, ROI | ✅ |
| 101 | /ua/blog/case-kosmetyka/ | кейс фулфілмент косметика | Кейс клієнта | 🟡 |
| 102 | /ua/blog/rinok-fulfilmentu-ukraina/ | ринок фулфілменту в Україні | Аналітика, цифри, прогнози | ✅ |
| 103 | /ua/faq/ | FAQ фулфілмент питання відповіді | Збірник 30+ питань | ✅ |

---

## ВІСЬ 7: EN ВЕРСІЇ ДЛЯ МІЖНАРОДНОГО ТРАФІКУ (18 сторінок)

| # | Slug | Ключовий запит | Пріоритет |
|---|------|---------------|-----------|
| 104 | /en/fulfillment-ukraine/ | fulfillment services Ukraine | ✅ |
| 105 | /en/3pl-logistics/ | 3PL operator Ukraine (slug: 3pl-logistics) | ✅ |
| 106 | /en/fulfillment-kyiv/ | fulfillment center Kyiv | ✅ |
| 107 | /en/prices/ | fulfillment pricing Ukraine (slug: prices) | ✅ |
| 108 | /en/warehouse-services/ | warehouse storage Ukraine (slug: warehouse-services) | ✅ |
| 109 | /en/fulfilment-for-online-store/ | ecommerce fulfillment Ukraine (slug: fulfilment-for-online-store) | ✅ |
| 110 | /en/blog/ukraine-3pl-hub-europe/ | Ukraine 3PL hub for Europe | 🟠 |
| 111 | /en/blog/fulfillment-ukraine-wartime/ | fulfillment Ukraine wartime resilience | 🟡 |
| 112 | /en/blog/shipping-from-ukraine/ | shipping from Ukraine to EU | 🟡 |
| 113 | /en/blog/how-to-choose-fulfillment-ukraine/ | how to choose fulfillment Ukraine | 🟡 |
| 114 | /en/blog/cross-border-ecommerce-ukraine/ | cross-border ecommerce Ukraine | 🔵 |
| 115 | /en/blog/logistics-mistakes-ukraine/ | logistics mistakes international sellers Ukraine | 🔵 |
| 116 | /en/fulfilment-for-cosmetics/ | cosmetics fulfillment Ukraine | ✅ |
| 117 | /en/fulfillment-for-fashion/ | fashion fulfillment Ukraine | 🔵 |
| 118 | /en/fulfillment-for-electronics/ | electronics fulfillment Ukraine | 🔵 |
| 119 | /en/b2b-fulfillment-ukraine/ | B2B fulfillment Ukraine | 🔵 |
| 120 | /en/fulfillment-boryspil-airport/ | fulfillment near Boryspil airport Kyiv | 🔵 |
| 121 | /en/blog/post/top-fulfillment-operators-ukraine-2026/ | top fulfillment companies Ukraine 2026 | ✅ |

---

## ЗВЕДЕНА СТАТИСТИКА (оновлено 2026-04-30)

| Категорія | Всього | ✅ Done | 🚧 In Progress | ❌ Not done | Покриття |
|-----------|--------|---------|----------------|-------------|----------|
| За товаром (вісь 1) | 26 | 2 | 1 (odyahu) | 22 (-1 dropped vape) | 12% |
| За бізнесом (вісь 2) | 16 | 3 | 0 | 13 | 19% |
| За каналом (вісь 3) | 12 | 2 | 0 | 10 | 17% |
| За послугою (вісь 4) | 17 | 4 | 0 | 13 | 24% |
| За географією (вісь 5) | 8 | 2 | 0 | 6 | 25% |
| Інформаційні (вісь 6) | 24 | 11 | 0 | 13 | 46% |
| EN версії (вісь 7) | 18 | 8 | 0 | 10 | 44% |
| **ВСЬОГО** | **121** | **32** | **1** | **88** | **27%** |

> Примітка: рядок 20 (vape) виключено з ядра 2026-04-30 як ризикову нішу — фактично цільових 120.
> На сайті є додатково ~30+ blog-постів і службових сторінок поза ядром (`scho-take-artikul`, `scho-take-sla`, `prepare-store-valentines-day` etc.) — інформаційне покриття де-факто ширше.

---

## ПЛАН ВИКОНАННЯ

### Фаза 1: Тижні 1-2 (🔴 High — 3 сторінки + 🟠 топ-5)
1. /ua/tsiny/ — ціни та тарифи
2. /ua/fulfilment-dlya-internet-magazynu/ — для інтернет-магазинів
3. /ua/blog/scho-take-fulfilment/ — гайд "що таке фулфілмент"
4. /ua/fulfilment-dlya-marketpleysiv/ — для маркетплейсів
5. /ua/faq/ — збірник 30+ питань
6. /ua/blog/yak-vybrati-fulfilment/ — як вибрати оператора
7. /ua/blog/top-fulfilment-ukrainy/ — рейтинг компаній
8. /ua/blog/case-ecodrive/ — кейс EcoDrive

### Фаза 2: Тижні 3-6 (🟠 Medium — 23 сторінки)
Нішеві (косметика, одяг, електроніка, сонячні панелі) + послуги (зберігання, комплектація) + гео (Київ, Бориспіль) + блог (порівняння, how-to) + EN

### Фаза 3: Місяці 2-3 (🟡 Low — 33 сторінки)
Решта нішевих + канали + дропшипінг + Shopify + блог

### Фаза 4: Місяці 3-6 (🔵 Backlog — 55 сторінок)
Довгий хвіст, вузькі ніші, EN версії

---

## ПРОГРАМАТИЧНЕ SEO: ЯК МАСШТАБУВАТИ

Для створення 120+ сторінок ефективно, використовуємо шаблонний підхід:

1. **Створити 1 еталонну сторінку** (наприклад /ua/fulfilment-dlya-kosmetyky/)
2. **Зробити з неї шаблон** з placeholder-ами: {{CATEGORY}}, {{KEYWORD}}, {{BENEFITS}}, {{CASE_STUDY}}, {{FAQ}}
3. **Написати промпт для Claude Code** який генерує N сторінок з шаблону, підставляючи унікальний контент
4. **Кожна сторінка має мінімум 800 слів** унікального контенту (не переклад!)
5. **Автоматично додавати** в sitemap, nav dropdown, footer

Це дозволить створювати 5-10 сторінок за день замість 1.

---

## РЕКОМЕНДАЦІЇ — TIER 1 (наступні 30 днів) [додано 2026-04-30]

Топ-10 сторінок з найвищим ROI для негайного створення. Запускаються через `/create-page` pipeline (Stitch → Research → Writer → Design → Deploy).

| # | Сторінка (UA root, без /ua/) | Вісь | Чому пріоритет |
|---|------|-----|----------------|
| 1 | `/fulfilment-dlya-odyahu/` 🚧 | 1 | В роботі 2026-04-30. Гаряча ніша, high search volume, нема landing |
| 2 | `/fulfilment-dlya-elektroniky/` | 1 | Велика ніша, високий чек, конкуренція низька в UA |
| 3 | `/fulfilment-sonyachni-paneli/` | 1 | Готовий кейс EcoDrive, потрібен service landing під нього |
| 4 | `/b2b-fulfilment/` | 2 | Окрема аудиторія (оптовики, дистриб'ютори), інший buyer persona |
| 5 | `/fulfilment-dlya-fop/` | 2 | 70% UA e-commerce — це ФОП. Масовий запит без конкурентів |
| 6 | `/komplektatsiya-zamovlen/` | 4 | Базова послуга, дивно що нема окремої сторінки |
| 7 | `/3pl-boryspil/` | 5 | Гео + USP "склад біля аеропорту" = унікальний angle |
| 8 | `/fulfilment-dlya-startapiv/` | 2 | Lower funnel + ринок ростe |
| 9 | `/blog/case-kosmetyka/` | 6 | Дані є, тільки оформити → magnet для AI-цитат |
| 10 | `/en/blog/ukraine-3pl-hub-europe/` | 7 | Магніт для міжнародного трафіку, GEO для AI search |

**Ритм:** ~3 сторінки UA + 3 RU + 3 EN на тиждень = 9 публікацій. За 30 днів — 30 нових сторінок (10 нових слугів × 3 мови).

**Після Tier 1:** перегляд метрик (CR, positions, pageviews по нових landing) → план Tier 2 (15 сторінок 🟡 priority).

---

## AI-VISIBILITY ПРІОРИТЕТИ

Сторінки які найшвидше почнуть цитувати AI-чатботи:

1. /ua/blog/top-fulfilment-ukrainy/ — рейтинг (Perplexity, ChatGPT Search люблять рейтинги)
2. /ua/blog/vartist-fulfilmentu-2026/ — ціни з цифрами (AI цитує конкретні числа)
3. /ua/faq/ — FAQ (Perplexity активно цитує FAQ)
4. /ua/blog/scho-take-fulfilment/ — визначення (ChatGPT бере визначення)
5. /ua/blog/rinok-fulfilmentu-ukraina/ — ринкова аналітика (Gemini цитує дослідження)
6. /ua/tsiny/ — тарифи з таблицями (AI витягує структуровані дані)

### Технічні кроки для AI-visibility:
- Створити /llms.txt з переліком ключових сторінок
- FAQPage schema на всіх нових сторінках
- Перші 2 речення кожного абзацу — пряма відповідь на питання
- Включити конкретні цифри MTP Group (60 000 відправлень, 150+ клієнтів, 10 років)

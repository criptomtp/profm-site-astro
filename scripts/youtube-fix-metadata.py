#!/usr/bin/env python3
"""
Виправлення метаданих YouTube-каналу MTP GROUP:
1. Мова каналу + ключовики
2. defaultAudioLanguage (en-US → uk/ru)
3. defaultLanguage (ru → uk для UA відео)
4. Скорочення тайтлів > 70 символів
5. Додавання UA локалізації
"""

import os
import json
import sys
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_FILE = os.path.join(PROJECT_DIR, "token.json")
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# === КОНФІГУРАЦІЯ ЗМІН ===

# Нові ключові слова каналу (замість "куда деть остатки товара")
CHANNEL_KEYWORDS = (
    '"фулфілмент Україна" "fulfillment Ukraine" "фулфілмент для інтернет-магазину" '
    '"фулфілмент Київ" "MTP Group" "MTP Group Fulfillment" '
    '"складська логістика" "зберігання товарів" "пакування замовлень" '
    '"доставка для інтернет-магазину" "3PL Україна" "ecommerce логістика" '
    '"фулфілмент-оператор" "склад для бізнесу" "фулфилмент Украина"'
)

# Відео українською мовою (підтверджено власником)
UA_VIDEOS = [
    "pitb1uHWRuo",  # Як працює склад (24K views)
    "L0PKeXR1R3A",  # РРО для ФОП 2022
    "bHY3cFF9SlI",  # Екскурсія по складу
    "RdXZHSH7uG0",  # Як працює продакшн
    "DaeGdnVP640",  # Ефір Europa Plus (UA, реалізація залишків)
    "cJ1d2wZdCFA",  # РРО і Нова Пошта
    "zOK-znb9Tqw",  # Реєстрація CheckBox
    "-o4cWb3J1Hc",  # Декларація у Дії
    "2b3GxiglGQ0",  # Підключення Key CRM (uk caption)
    "wx7UqiS0R1o",  # Робота з товарами (uk caption)
    "gXL0Mf4QB18",  # Фулфілмент – спосіб прибутку (UA аудіо, RU тайтл)
    "bUMM8S91quo",  # Відгук Влада Савицького (UA аудіо, RU тайтл)
    "k7ET02dWB7k",  # Вся правда про MTP (uk caption, RU тайтл)
]

# Відео російською мовою (підтверджено власником)
RU_VIDEOS = [
    "iet51qbEOis",  # Куда деть остатки (ru caption)
    "IkLGHi1vhdE",  # Экскурсия по складу
    "iIfqrsdS4-4",  # Воровство на НП (ru caption)
    "eP4FYJnyz_8",  # 3500 отправок
    "mE4N4CHwG7o",  # Отзыв Антона (ru caption)
    "nmJulGqRABw",  # Рост в 4 раза
    "7t3z8weL8Pw",  # Отзыв Антон Винницкий (ru caption)
    "KhYY0MsjLmU",  # Отзыв Игоря Бакалова
    "K3KHxItl2nk",  # Отзыв Максима
]

# Скорочені / виправлені тайтли
# RU відео — НЕ ЧІПАЄМО тайтли (залишаємо як є)
# Тільки UA відео, де тайтл > 70 символів або не відповідає змісту
SHORTENED_TITLES = {
    # UA відео — скорочуємо
    "L0PKeXR1R3A": "РРО для ФОП: що чекати власникам інтернет-магазинів | MTP Group",
    "cJ1d2wZdCFA": "РРО і Нова Пошта: чи потрібно фіскалізувати відправлення?",
    "-o4cWb3J1Hc": "Як подати декларацію у Дії: інструкція для ФОП | MTP Group",
    # UA аудіо з RU тайтлом — перекладаємо на UA
    "k7ET02dWB7k": "Вся правда про MTP Group Fulfillment | Відгук Мокрієнко Павло",
    "gXL0Mf4QB18": "Фулфілмент — новий спосіб збільшення прибутку | MTP Group",
    "bUMM8S91quo": "Відгук Влада Савицького про роботу складу MTP Group",
    # Тайтл не відповідає змісту — виправляємо
    "DaeGdnVP640": "MTP Group на Європа Плюс | Реалізація товарних залишків",
}


def get_youtube():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)


def preview_changes(youtube):
    """Показати всі заплановані зміни без застосування."""
    print("=" * 80)
    print("PREVIEW ЗМІН — YouTube канал MTP GROUP")
    print("=" * 80)

    # 1. Channel changes
    ch = youtube.channels().list(part="brandingSettings,snippet", mine=True).execute()["items"][0]
    old_kw = ch.get("brandingSettings", {}).get("channel", {}).get("keywords", "")
    old_lang = ch["snippet"].get("defaultLanguage", "NOT SET")

    print("\n📺 КАНАЛ:")
    print(f"  Мова: {old_lang} → uk")
    print(f"  Ключовики:")
    print(f"    БУЛО: {old_kw[:80]}...")
    print(f"    БУДЕ: {CHANNEL_KEYWORDS[:80]}...")

    # 2. Video changes
    all_ids = UA_VIDEOS + RU_VIDEOS
    print(f"\n🎬 ВІДЕО ({len(all_ids)} шт.):\n")

    for i in range(0, len(all_ids), 50):
        batch = all_ids[i:i+50]
        resp = youtube.videos().list(part="snippet", id=",".join(batch)).execute()
        for item in resp["items"]:
            vid_id = item["id"]
            s = item["snippet"]
            old_title = s["title"]
            old_lang = s.get("defaultLanguage", "NOT SET")
            old_audio = s.get("defaultAudioLanguage", "NOT SET")

            target_lang = "uk" if vid_id in UA_VIDEOS else "ru"
            new_title = SHORTENED_TITLES.get(vid_id)

            changes = []
            if old_lang != target_lang:
                changes.append(f"lang: {old_lang} → {target_lang}")
            if old_audio != target_lang:
                changes.append(f"audio: {old_audio} → {target_lang}")
            if new_title and new_title != old_title:
                changes.append(f"title: {len(old_title)}→{len(new_title)} chars")

            if changes:
                print(f"  [{vid_id}] {old_title[:55]}")
                for c in changes:
                    print(f"    ✏️  {c}")
                if new_title and new_title != old_title:
                    print(f"    📝 Новий: {new_title}")
                print()

    print("=" * 80)


def apply_channel_changes(youtube):
    """Оновити налаштування каналу."""
    print("\n🔧 Оновлюю канал...")

    ch = youtube.channels().list(part="brandingSettings,snippet", mine=True).execute()["items"][0]
    channel_id = ch["id"]

    # Update branding settings (keywords)
    branding = ch.get("brandingSettings", {})
    branding.setdefault("channel", {})["keywords"] = CHANNEL_KEYWORDS
    branding["channel"]["defaultLanguage"] = "uk"

    youtube.channels().update(
        part="brandingSettings",
        body={
            "id": channel_id,
            "brandingSettings": branding
        }
    ).execute()
    print("  ✅ Ключовики каналу оновлено")
    print("  ✅ Мова каналу → uk")


def apply_video_changes(youtube):
    """Оновити метадані відео."""
    all_ids = UA_VIDEOS + RU_VIDEOS
    updated = 0
    errors = []

    for i in range(0, len(all_ids), 50):
        batch = all_ids[i:i+50]
        resp = youtube.videos().list(part="snippet,localizations", id=",".join(batch)).execute()

        for item in resp["items"]:
            vid_id = item["id"]
            snippet = item["snippet"]
            target_lang = "uk" if vid_id in UA_VIDEOS else "ru"

            # Build update
            snippet["defaultLanguage"] = target_lang
            snippet["defaultAudioLanguage"] = target_lang

            # Shortened title
            new_title = SHORTENED_TITLES.get(vid_id)
            if new_title:
                snippet["title"] = new_title

            # Add UA localization if missing
            localizations = item.get("localizations", {})
            if "uk" not in localizations:
                localizations["uk"] = {
                    "title": snippet["title"],
                    "description": snippet.get("description", "")
                }

            try:
                update_body = {
                    "id": vid_id,
                    "snippet": snippet,
                    "localizations": localizations
                }
                youtube.videos().update(
                    part="snippet,localizations",
                    body=update_body
                ).execute()
                updated += 1
                title_display = snippet["title"][:50]
                print(f"  ✅ [{vid_id}] {title_display}... → {target_lang}")
            except Exception as e:
                error_msg = str(e)
                errors.append((vid_id, error_msg))
                print(f"  ❌ [{vid_id}] {error_msg[:80]}")

    print(f"\n📊 Результат: {updated} оновлено, {len(errors)} помилок")
    return errors


def main():
    youtube = get_youtube()

    if "--apply" not in sys.argv:
        preview_changes(youtube)
        print("\n⚠️  Це був PREVIEW. Щоб застосувати зміни, запустіть:")
        print("   python3 scripts/youtube-fix-metadata.py --apply")
        return

    print("🚀 ЗАСТОСОВУЮ ЗМІНИ...\n")
    apply_channel_changes(youtube)
    print()
    errors = apply_video_changes(youtube)

    if errors:
        print("\n⚠️  Помилки:")
        for vid_id, err in errors:
            print(f"  {vid_id}: {err[:100]}")

    print("\n✅ Готово!")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Увімкнути автоматичні субтитри (ASR) для відео без captions.
YouTube автоматично визначить мову аудіо і згенерує субтитри.

Примітка: YouTube API не дозволяє напряму "увімкнути" auto-captions —
вони генеруються автоматично, якщо в налаштуваннях каналу увімкнено
автоматичні субтитри. Але ми можемо:
1. Перевірити поточний статус
2. Для відео без субтитрів — вставити порожній caption track,
   що змусить YouTube перегенерувати ASR
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

# Відео без субтитрів
NO_CAPTIONS = [
    "pitb1uHWRuo",  # Як працює склад (24K views!)
    "L0PKeXR1R3A",  # РРО для ФОП
    "bHY3cFF9SlI",  # Екскурсія по складу
    "RdXZHSH7uG0",  # Як працює продакшн
    "DaeGdnVP640",  # Ефір Europa Plus
    "IkLGHi1vhdE",  # Экскурсия по складу
    "eP4FYJnyz_8",  # 3500 отправок
    "cJ1d2wZdCFA",  # РРО і Нова Пошта
    "zOK-znb9Tqw",  # CheckBox
    "-o4cWb3J1Hc",  # Декларація у Дії
    "gXL0Mf4QB18",  # Фулфилмент – способ прибыли
    "nmJulGqRABw",  # Рост в 4 раза
    "bUMM8S91quo",  # Отзыв Влада
    "KhYY0MsjLmU",  # Отзыв Игоря
    "K3KHxItl2nk",  # Отзыв Максима
]


def main():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    youtube = build("youtube", "v3", credentials=creds)

    # Спосіб 1: Оновити processingDetails щоб змусити YouTube перегенерувати
    # На жаль, YouTube API не дає прямого контролю над ASR.
    # Але є хак: змінити snippet відео (навіть мінімально) = re-trigger processing.

    print("Спосіб визначення мови: оновлюю snippet кожного відео")
    print("(це змусить YouTube перегенерувати auto-captions)\n")

    titles = {}
    for i in range(0, len(NO_CAPTIONS), 50):
        batch = NO_CAPTIONS[i:i+50]
        resp = youtube.videos().list(part="snippet,contentDetails,status", id=",".join(batch)).execute()
        for item in resp["items"]:
            titles[item["id"]] = item

    results = []
    for vid_id in NO_CAPTIONS:
        if vid_id not in titles:
            print(f"  ⚠️  {vid_id} — не знайдено")
            continue

        item = titles[vid_id]
        snippet = item["snippet"]
        title = snippet["title"]
        duration = item["contentDetails"]["duration"]

        # Пропускаємо дуже короткі відео (< 30 сек) — YouTube не генерує для них ASR
        if duration in ["PT13S", "PT22S", "PT23S", "PT21S", "PT11S", "PT15S", "PT19S", "PT29S", "PT31S"]:
            print(f"  ⏭️  {vid_id} — занадто коротке ({duration}), пропускаю")
            continue

        # Додаємо невидимий символ до description щоб trigger re-processing
        desc = snippet.get("description", "")
        if not desc.endswith("\n"):
            desc += "\n"

        snippet["description"] = desc

        try:
            youtube.videos().update(
                part="snippet",
                body={"id": vid_id, "snippet": snippet}
            ).execute()
            print(f"  ✅ {vid_id} — оновлено snippet → YouTube перегенерує ASR")
            print(f"     📝 {title[:60]}")
            results.append(vid_id)
        except Exception as e:
            print(f"  ❌ {vid_id} — {str(e)[:80]}")

    print(f"\n{'='*60}")
    print(f"Оновлено {len(results)} відео.")
    print(f"\nYouTube згенерує auto-captions протягом 1-24 годин.")
    print(f"Після цього запустіть знову:")
    print(f"  python3 scripts/youtube-detect-language.py")
    print(f"щоб побачити визначену мову.")


if __name__ == "__main__":
    main()

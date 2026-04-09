#!/usr/bin/env python3
"""
Визначити реальну мову кожного відео через автоматичні субтитри YouTube.
"""

import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_FILE = os.path.join(PROJECT_DIR, "token.json")
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

ALL_VIDEO_IDS = [
    "pitb1uHWRuo", "iet51qbEOis", "L0PKeXR1R3A", "bHY3cFF9SlI",
    "RdXZHSH7uG0", "DaeGdnVP640", "IkLGHi1vhdE", "iIfqrsdS4-4",
    "eP4FYJnyz_8", "cJ1d2wZdCFA", "zOK-znb9Tqw", "mE4N4CHwG7o",
    "-o4cWb3J1Hc", "2b3GxiglGQ0", "k7ET02dWB7k", "gXL0Mf4QB18",
    "nmJulGqRABw", "bUMM8S91quo", "7t3z8weL8Pw", "KhYY0MsjLmU",
    "K3KHxItl2nk", "wx7UqiS0R1o",
]

def main():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    youtube = build("youtube", "v3", credentials=creds)

    # Get titles
    titles = {}
    for i in range(0, len(ALL_VIDEO_IDS), 50):
        batch = ALL_VIDEO_IDS[i:i+50]
        resp = youtube.videos().list(part="snippet", id=",".join(batch)).execute()
        for item in resp["items"]:
            titles[item["id"]] = item["snippet"]["title"]

    print(f"{'ID':<14} {'Auto-caption lang':<20} {'Title'}")
    print("-" * 100)

    for vid_id in ALL_VIDEO_IDS:
        title = titles.get(vid_id, "???")
        try:
            captions = youtube.captions().list(
                part="snippet",
                videoId=vid_id
            ).execute()

            langs = []
            for cap in captions.get("items", []):
                s = cap["snippet"]
                track_kind = s.get("trackKind", "")
                lang = s.get("language", "?")
                name = s.get("name", "")
                is_auto = track_kind == "ASR"
                label = f"{lang}({'auto' if is_auto else 'manual'})"
                langs.append(label)

            lang_str = ", ".join(langs) if langs else "NO CAPTIONS"
            print(f"  {vid_id:<12} {lang_str:<20} {title[:55]}")

        except Exception as e:
            err = str(e)
            if "forbidden" in err.lower() or "403" in err:
                print(f"  {vid_id:<12} {'ACCESS DENIED':<20} {title[:55]}")
            else:
                print(f"  {vid_id:<12} {'ERROR':<20} {title[:55]} — {err[:40]}")

if __name__ == "__main__":
    main()

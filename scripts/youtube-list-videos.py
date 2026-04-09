#!/usr/bin/env python3
"""
Отримати повний список відео з каналу MTP GROUP.
Зберігає результат у scripts/youtube-videos.json
"""

import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_FILE = os.path.join(PROJECT_DIR, "token.json")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "youtube-videos.json")

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_credentials():
    if not os.path.exists(TOKEN_FILE):
        print("Спочатку запустіть youtube-auth.py для авторизації!")
        exit(1)

    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return creds

def main():
    creds = get_credentials()
    youtube = build("youtube", "v3", credentials=creds)

    # 1. Отримати channel ID
    channels = youtube.channels().list(part="contentDetails,snippet,statistics", mine=True).execute()

    if not channels["items"]:
        print("Канал не знайдено!")
        return

    channel = channels["items"][0]
    channel_id = channel["id"]
    channel_title = channel["snippet"]["title"]
    uploads_playlist = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    sub_count = channel["statistics"].get("subscriberCount", "?")
    video_count = channel["statistics"].get("videoCount", "?")
    view_count = channel["statistics"].get("viewCount", "?")

    print(f"Канал: {channel_title}")
    print(f"ID: {channel_id}")
    print(f"Підписники: {sub_count} | Відео: {video_count} | Переглядів: {view_count}")
    print(f"Плейліст завантажень: {uploads_playlist}")
    print()

    # 2. Отримати всі відео з плейліста uploads
    videos = []
    next_page = None

    while True:
        playlist_req = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=next_page
        )
        playlist_resp = playlist_req.execute()

        for item in playlist_resp["items"]:
            video_id = item["contentDetails"]["videoId"]
            snippet = item["snippet"]
            videos.append({
                "id": video_id,
                "title": snippet["title"],
                "description": snippet.get("description", "")[:200],
                "published": snippet["publishedAt"],
                "thumbnail": snippet["thumbnails"].get("high", snippet["thumbnails"].get("default", {})).get("url", ""),
            })

        next_page = playlist_resp.get("nextPageToken")
        if not next_page:
            break

    # 3. Отримати статистику для кожного відео (батчами по 50)
    video_ids = [v["id"] for v in videos]
    stats = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        stats_resp = youtube.videos().list(
            part="statistics,contentDetails",
            id=",".join(batch)
        ).execute()
        for item in stats_resp["items"]:
            stats[item["id"]] = {
                "views": int(item["statistics"].get("viewCount", 0)),
                "likes": int(item["statistics"].get("likeCount", 0)),
                "comments": int(item["statistics"].get("commentCount", 0)),
                "duration": item["contentDetails"]["duration"],
            }

    for v in videos:
        s = stats.get(v["id"], {})
        v.update(s)

    # 4. Сортувати за переглядами (найпопулярніші першими)
    videos.sort(key=lambda x: x.get("views", 0), reverse=True)

    # 5. Зберегти результат
    result = {
        "channel": {
            "id": channel_id,
            "title": channel_title,
            "subscribers": sub_count,
            "total_videos": video_count,
            "total_views": view_count,
        },
        "videos": videos
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Знайдено {len(videos)} відео:")
    print("-" * 80)
    for i, v in enumerate(videos, 1):
        views = v.get("views", "?")
        duration = v.get("duration", "?")
        print(f"{i:2}. [{views:>6} views] {v['title']}")
        print(f"    ID: {v['id']} | {v['published'][:10]} | {duration}")
        print()

    print(f"Збережено у {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

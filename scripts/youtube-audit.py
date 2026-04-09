#!/usr/bin/env python3
"""
Повний аудит YouTube-каналу MTP GROUP:
- Теги, описи, метадані кожного відео
- SEO-аналіз
- Рекомендації
"""

import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_FILE = os.path.join(PROJECT_DIR, "token.json")
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "youtube-audit.json")

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def get_youtube():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)

def main():
    youtube = get_youtube()

    # Get channel info
    ch = youtube.channels().list(
        part="snippet,brandingSettings,contentDetails,statistics,topicDetails,status",
        mine=True
    ).execute()["items"][0]

    channel_info = {
        "id": ch["id"],
        "title": ch["snippet"]["title"],
        "description": ch["snippet"].get("description", ""),
        "customUrl": ch["snippet"].get("customUrl", ""),
        "country": ch["snippet"].get("country", "NOT SET"),
        "keywords": ch.get("brandingSettings", {}).get("channel", {}).get("keywords", "NOT SET"),
        "defaultLanguage": ch["snippet"].get("defaultLanguage", "NOT SET"),
        "subscribers": ch["statistics"].get("subscriberCount"),
        "totalViews": ch["statistics"].get("viewCount"),
        "videoCount": ch["statistics"].get("videoCount"),
        "topicCategories": ch.get("topicDetails", {}).get("topicCategories", []),
    }

    uploads_playlist = ch["contentDetails"]["relatedPlaylists"]["uploads"]

    # Get all video IDs
    video_ids = []
    next_page = None
    while True:
        pl = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=next_page
        ).execute()
        video_ids.extend([i["contentDetails"]["videoId"] for i in pl["items"]])
        next_page = pl.get("nextPageToken")
        if not next_page:
            break

    # Get full details for all videos
    videos = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        resp = youtube.videos().list(
            part="snippet,contentDetails,statistics,status,topicDetails,localizations",
            id=",".join(batch)
        ).execute()
        for item in resp["items"]:
            s = item["snippet"]
            st = item["statistics"]
            status = item["status"]

            tags = s.get("tags", [])
            desc = s.get("description", "")
            title = s.get("title", "")

            # SEO issues
            issues = []
            if not tags:
                issues.append("NO_TAGS")
            elif len(tags) < 5:
                issues.append(f"FEW_TAGS ({len(tags)})")
            if len(desc) < 50:
                issues.append(f"SHORT_DESC ({len(desc)} chars)")
            if len(title) > 70:
                issues.append(f"LONG_TITLE ({len(title)} chars)")
            if not s.get("defaultLanguage"):
                issues.append("NO_LANGUAGE")
            if not s.get("defaultAudioLanguage"):
                issues.append("NO_AUDIO_LANGUAGE")
            if "categoryId" in s and s["categoryId"] == "22":
                pass  # People & Blogs - ok but could be better
            localizations = item.get("localizations", {})
            if not localizations:
                issues.append("NO_LOCALIZATIONS")

            views = int(st.get("viewCount", 0))
            likes = int(st.get("likeCount", 0))
            comments = int(st.get("commentCount", 0))

            # Determine video type
            duration = item["contentDetails"]["duration"]
            vid_type = "content"
            if "куртк" in title.lower() or duration in ["PT13S", "PT22S", "PT23S", "PT21S", "PT11S", "PT15S", "PT19S", "PT29S"]:
                vid_type = "product_demo"
            elif "отзыв" in title.lower() or "відгук" in title.lower():
                vid_type = "testimonial"
            elif "екскурсі" in title.lower() or "экскурси" in title.lower():
                vid_type = "warehouse_tour"
            elif "як " in title.lower() and ("працю" in title.lower() or "зареєстру" in title.lower() or "подати" in title.lower() or "підключити" in title.lower()):
                vid_type = "tutorial"
            elif "ррo" in title.lower() or "рро" in title.lower():
                vid_type = "educational"
            elif "европа плюс" in title.lower() or "ефір" in title.lower() or "ефир" in title.lower():
                vid_type = "media_appearance"
            elif "звіт" in title.lower() or "отчет" in title.lower() or "прайс" in title.lower():
                vid_type = "internal"
            elif "трансляці" in title.lower() or "прямой" in title.lower() or "прямий" in title.lower():
                vid_type = "livestream"

            videos.append({
                "id": item["id"],
                "title": title,
                "description": desc,
                "tags": tags,
                "publishedAt": s["publishedAt"],
                "categoryId": s.get("categoryId"),
                "defaultLanguage": s.get("defaultLanguage", None),
                "defaultAudioLanguage": s.get("defaultAudioLanguage", None),
                "duration": duration,
                "views": views,
                "likes": likes,
                "comments": comments,
                "privacy": status.get("privacyStatus"),
                "embeddable": status.get("embeddable"),
                "madeForKids": status.get("madeForKids"),
                "localizations": list(localizations.keys()) if localizations else [],
                "topicCategories": item.get("topicDetails", {}).get("topicCategories", []),
                "thumbnails": {k: v.get("url") for k, v in s.get("thumbnails", {}).items()},
                "type": vid_type,
                "issues": issues,
            })

    videos.sort(key=lambda x: x["views"], reverse=True)

    # Get playlists
    playlists = []
    pl_resp = youtube.playlists().list(part="snippet,contentDetails", mine=True, maxResults=50).execute()
    for p in pl_resp.get("items", []):
        playlists.append({
            "id": p["id"],
            "title": p["snippet"]["title"],
            "description": p["snippet"].get("description", ""),
            "videoCount": p["contentDetails"]["itemCount"],
        })

    result = {
        "channel": channel_info,
        "playlists": playlists,
        "videos": videos,
        "summary": {
            "total": len(videos),
            "public": sum(1 for v in videos if v["privacy"] == "public"),
            "unlisted": sum(1 for v in videos if v["privacy"] == "unlisted"),
            "private": sum(1 for v in videos if v["privacy"] == "private"),
            "with_tags": sum(1 for v in videos if v["tags"]),
            "without_tags": sum(1 for v in videos if not v["tags"]),
            "with_localizations": sum(1 for v in videos if v["localizations"]),
            "embeddable": sum(1 for v in videos if v["embeddable"]),
            "types": {},
        }
    }

    for v in videos:
        t = v["type"]
        if t not in result["summary"]["types"]:
            result["summary"]["types"][t] = 0
        result["summary"]["types"][t] += 1

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Збережено повний аудит у {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

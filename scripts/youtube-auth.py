#!/usr/bin/env python3
"""
OAuth2 авторизація для YouTube Data API v3.
Відкриє браузер для авторизації, збереже токен у token.json.
"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENT_SECRET = os.path.join(PROJECT_DIR, "client_secret.json")
TOKEN_FILE = os.path.join(PROJECT_DIR, "token.json")

SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]

def main():
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Оновлюю токен...")
            creds.refresh(Request())
        else:
            print("Відкриваю браузер для авторизації...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=8080)

        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
        print(f"Токен збережено: {TOKEN_FILE}")
    else:
        print("Токен вже дійсний.")

    print("Авторизація успішна!")

if __name__ == "__main__":
    main()

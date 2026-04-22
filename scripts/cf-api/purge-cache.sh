#!/bin/bash
# Usage: ./scripts/cf-api/purge-cache.sh [url1 url2 ...]
# With no args — purges entire cache. With URLs — purges only those.

source "$(dirname "$0")/_env.sh"

if [[ $# -eq 0 ]]; then
  echo "⚠️  Purging ENTIRE cache for fulfillmentmtp.com.ua — Ctrl+C within 3s to abort"
  sleep 3
  BODY='{"purge_everything":true}'
else
  FILES_JSON=$(printf '"%s",' "$@" | sed 's/,$//')
  BODY="{\"files\":[${FILES_JSON}]}"
fi

curl -s -X POST "$CF_API/zones/$CF_ZONE_ID/purge_cache" \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d "$BODY" | python3 -m json.tool

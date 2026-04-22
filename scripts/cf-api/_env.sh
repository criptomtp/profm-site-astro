#!/bin/bash
# Load CF API credentials from .env.local. Source this at the top of every cf-api/*.sh script.
# Never echo $CLOUDFLARE_API_TOKEN — treat as secret.

ENV_FILE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/.env.local"

if [[ ! -f "$ENV_FILE" ]]; then
  echo "❌ .env.local not found at $ENV_FILE" >&2
  exit 1
fi

set -a
# shellcheck disable=SC1090
source "$ENV_FILE"
set +a

if [[ -z "$CLOUDFLARE_API_TOKEN" ]]; then
  echo "❌ CLOUDFLARE_API_TOKEN not set in .env.local" >&2
  exit 1
fi

# Hardcoded zone ID for fulfillmentmtp.com.ua — discovered via GET /zones?name=
export CF_ZONE_ID="be854562a1fdf626e5429921f0f1022c"
export CF_API="https://api.cloudflare.com/client/v4"
export CF_GRAPHQL="$CF_API/graphql"
export AUTH_HEADER="Authorization: Bearer $CLOUDFLARE_API_TOKEN"

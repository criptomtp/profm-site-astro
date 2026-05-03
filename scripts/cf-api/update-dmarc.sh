#!/bin/bash
# update-dmarc.sh — Update _dmarc TXT record via Cloudflare API.
#
# Requires the CLOUDFLARE_API_TOKEN in .env.local to have Zone:DNS:Edit scope.
# By default the existing token is read-only (works for GET DNS but not PATCH).
# To grant edit: CF Dashboard → My Profile → API Tokens → Edit token →
#   Permissions → Zone — DNS — Edit (scope: fulfillmentmtp.com.ua only).
#
# Usage: bash scripts/cf-api/update-dmarc.sh

set -euo pipefail

source "$(dirname "$0")/_env.sh"

DMARC_NAME="_dmarc.fulfillmentmtp.com.ua"
NEW_VALUE='v=DMARC1; p=none; rua=mailto:mtpgrouppromo@gmail.com; sp=none; aspf=r; adkim=r; fo=1; pct=100'

echo "Looking up existing DMARC record for $DMARC_NAME..."
LOOKUP=$(curl -s -H "$AUTH_HEADER" "$CF_API/zones/$CF_ZONE_ID/dns_records?type=TXT&name=$DMARC_NAME")
DMARC_ID=$(echo "$LOOKUP" | python3 -c "import json, sys; d=json.load(sys.stdin); print(d['result'][0]['id'] if d.get('success') and d.get('result') else '')")

if [[ -z "$DMARC_ID" ]]; then
  echo "❌ Could not find existing _dmarc TXT record. Lookup response:"
  echo "$LOOKUP" | python3 -m json.tool
  exit 1
fi

echo "Found record id=$DMARC_ID. Updating to:"
echo "  $NEW_VALUE"
echo

RESPONSE=$(curl -s -X PATCH \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  "$CF_API/zones/$CF_ZONE_ID/dns_records/$DMARC_ID" \
  -d "{\"content\":\"$NEW_VALUE\"}")

SUCCESS=$(echo "$RESPONSE" | python3 -c "import json, sys; print(json.load(sys.stdin).get('success', False))")

if [[ "$SUCCESS" == "True" ]]; then
  echo "✅ DMARC updated successfully."
  echo
  echo "Verifying with dig (may take 30-60s for cache)..."
  sleep 5
  dig +short TXT "$DMARC_NAME"
  echo
  echo "Run scripts/security-verify.py to confirm."
else
  echo "❌ Update failed. Response:"
  echo "$RESPONSE" | python3 -m json.tool
  echo
  echo "Most likely cause: token lacks Zone:DNS:Edit scope."
  echo "See docs/security-debt-2026-05.md section 'How to grant the CF token DNS Edit scope'."
  exit 1
fi

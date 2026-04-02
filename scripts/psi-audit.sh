#!/bin/bash
# PSI Audit — Автоматичний аналіз PageSpeed Insights
# Використання:
#   ./scripts/psi-audit.sh                    — без API ключа (лімітовано)
#   PSI_KEY=YOUR_KEY ./scripts/psi-audit.sh   — з API ключем (25K запитів/день)
#
# Як отримати ключ безкоштовно:
#   1. https://console.cloud.google.com/apis/credentials
#   2. Create Credentials → API Key
#   3. Enable "PageSpeed Insights API"

KEY="${PSI_KEY:-}"
BASE="https://www.fulfillmentmtp.com.ua"
STRATEGY="mobile"

# Сторінки для аналізу
PAGES=(
  "/"
  "/en/"
  "/ru/"
  "/ua/tsiny/"
  "/en/prices/"
  "/tsenu/"
  "/ua/services/"
  "/en/services/"
  "/services/"
)

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  PSI Audit — $BASE                          ║"
echo "║  Strategy: $STRATEGY                                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

printf "%-35s %5s %6s %6s %6s %4s %6s\n" "PAGE" "PERF" "FCP" "LCP" "TBT" "CLS" "SI"
printf "%-35s %5s %6s %6s %6s %4s %6s\n" "---" "----" "-----" "-----" "-----" "---" "-----"

for page in "${PAGES[@]}"; do
  URL="${BASE}${page}"
  API_URL="https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=${URL}&strategy=${STRATEGY}&category=performance"

  if [ -n "$KEY" ]; then
    API_URL="${API_URL}&key=${KEY}"
  fi

  RESULT=$(curl -s "$API_URL" 2>/dev/null)

  # Check for errors
  ERROR=$(echo "$RESULT" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('error',{}).get('message',''))" 2>/dev/null)

  if [ -n "$ERROR" ] && [ "$ERROR" != "" ]; then
    printf "%-35s %s\n" "$page" "ERROR: $ERROR"
    continue
  fi

  # Extract metrics
  METRICS=$(echo "$RESULT" | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    lr=d.get('lighthouseResult',{})
    a=lr.get('audits',{})
    perf=int(lr.get('categories',{}).get('performance',{}).get('score',0)*100)
    fcp=a.get('first-contentful-paint',{}).get('displayValue','?')
    lcp=a.get('largest-contentful-paint',{}).get('displayValue','?')
    tbt=a.get('total-blocking-time',{}).get('displayValue','?')
    cls=a.get('cumulative-layout-shift',{}).get('displayValue','?')
    si=a.get('speed-index',{}).get('displayValue','?')
    print(f'{perf}|{fcp}|{lcp}|{tbt}|{cls}|{si}')
except:
    print('ERR|?|?|?|?|?')
" 2>/dev/null)

  IFS='|' read -r PERF FCP LCP TBT CLS SI <<< "$METRICS"
  printf "%-35s %5s %6s %6s %6s %4s %6s\n" "$page" "$PERF" "$FCP" "$LCP" "$TBT" "$CLS" "$SI"

  # Delay to avoid rate limits
  sleep 2
done

echo ""
echo "Done! For detailed analysis, run with PSI_KEY for higher quota."

#!/bin/bash
# Usage: ./scripts/cf-api/errors-breakdown.sh [hours=23]
# Shows top URLs returning 4xx/5xx across all crawlers + user traffic.

source "$(dirname "$0")/_env.sh"

HOURS="${1:-23}"
SINCE=$(date -u -v-${HOURS}H +"%Y-%m-%dT%H:%M:%SZ")

echo "=== Status code distribution (last ${HOURS}h) ==="
curl -s "$CF_GRAPHQL" -H "$AUTH_HEADER" -H "Content-Type: application/json" -d @- <<EOF | python3 -c "
import sys, json
d = json.load(sys.stdin)
if 'errors' in d and d.get('errors'):
    print('ERROR:', d['errors']); sys.exit(1)
statuses = d['data']['viewer']['zones'][0]['httpRequests1dGroups'][0]['sum']['responseStatusMap']
total = sum(s['requests'] for s in statuses)
print(f'Total requests: {total}')
print()
print(f'{\"Status\":<8} {\"Count\":<8} {\"Pct\":<8}')
print('-' * 28)
for s in sorted(statuses, key=lambda x: -x['requests']):
    marker = ' ⚠️' if s['edgeResponseStatus'] >= 400 else ''
    print(f'{s[\"edgeResponseStatus\"]:<8} {s[\"requests\"]:<8} {s[\"requests\"]/total*100:>5.1f}%{marker}')
"
{"query":"query{viewer{zones(filter:{zoneTag:\"$CF_ZONE_ID\"}){httpRequests1dGroups(limit:1,filter:{date_geq:\"$(date -u -v-${HOURS}H +%Y-%m-%d)\"}){sum{responseStatusMap{edgeResponseStatus requests}}}}}}"}
EOF

echo ""
echo "=== Top error URLs (4xx/5xx, last ${HOURS}h) ==="
curl -s "$CF_GRAPHQL" -H "$AUTH_HEADER" -H "Content-Type: application/json" -d @- <<EOF | python3 -c "
import sys, json
d = json.load(sys.stdin)
if 'errors' in d and d.get('errors'):
    print('ERROR:', d['errors']); sys.exit(1)
groups = d['data']['viewer']['zones'][0]['httpRequestsAdaptiveGroups']
print(f'{\"Status\":<7} {\"Count\":<6} {\"Method\":<7} Path')
print('-' * 90)
for g in groups[:40]:
    dim = g['dimensions']
    print(f\"{dim['edgeResponseStatus']:<7} {g['count']:<6} {dim['clientRequestHTTPMethodName']:<7} {dim['clientRequestPath'][:80]}\")
"
{"query":"query{viewer{zones(filter:{zoneTag:\"$CF_ZONE_ID\"}){httpRequestsAdaptiveGroups(limit:50,filter:{datetime_geq:\"$SINCE\",edgeResponseStatus_in:[403,404,405,500,502,503,522]},orderBy:[count_DESC]){count dimensions{edgeResponseStatus clientRequestPath clientRequestHTTPMethodName}}}}}"}
EOF

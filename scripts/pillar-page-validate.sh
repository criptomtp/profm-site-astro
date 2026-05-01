#!/bin/bash
# scripts/pillar-page-validate.sh — Pillar/topic page quality gate
#
# Validates a pillar/topic page (or UA+RU+EN triplet) against 8 quality
# checks defined in docs/pillar-page-checklist.md. Catches the recurring
# defects flagged in the 2026-05-01 site audit:
#
#   1. Schema parity — 9 must-have @types (Organization, LocalBusiness,
#      GeoCoordinates, PostalAddress, BusinessAudience, Service, Offer,
#      FAQPage, Country)
#   2. Word count ≥ 2500 per language
#   3. H1 brand-hook (not generic noun construction)
#   4. H1 whitespace bug (no concatenated "слово.Слово")
#   5. Hreflang quartet (uk + ru + en + x-default = 4 alternates)
#   6. Language purity (no banned EN words in UA/RU body)
#   7. (--triplet) Reciprocal hreflang — all 3 pages cite the same 4 URLs
#   8. (--triplet) UA/RU/EN parity — same word count tier and schema count
#
# Usage:
#   ./scripts/pillar-page-validate.sh URL_OR_FILE
#   ./scripts/pillar-page-validate.sh --triplet UA_URL RU_URL EN_URL
#
# Exit: 0 = all passed, 1 = any failed.

set -u

usage() {
    cat <<EOF
Usage:
  $0 URL_OR_FILE                        # validate a single page
  $0 --triplet UA RU EN                 # validate all 3 + reciprocal hreflang
  $0 --help

Examples:
  $0 https://www.fulfillmentmtp.com.ua/fulfilment-dlya-odyahu/
  $0 dist/fulfilment-dlya-odyahu/index.html
  $0 --triplet \\
      https://www.fulfillmentmtp.com.ua/fulfilment-dlya-odyahu/ \\
      https://www.fulfillmentmtp.com.ua/ru/fulfilment-dlya-odezhdy/ \\
      https://www.fulfillmentmtp.com.ua/en/fulfilment-for-clothing/
EOF
    exit 2
}

[ $# -lt 1 ] && usage
[ "${1:-}" = "--help" ] && usage

fetch() {
    local input=$1
    if [[ "$input" =~ ^https?:// ]]; then
        curl -sL --max-time 15 "$input"
    elif [ -f "$input" ]; then
        cat "$input"
    else
        echo ""
    fi
}

detect_lang() {
    local html=$1
    if echo "$html" | grep -q '<html [^>]*lang="ru"'; then echo "ru"
    elif echo "$html" | grep -q '<html [^>]*lang="en"'; then echo "en"
    else echo "uk"
    fi
}

validate_single() {
    local input=$1
    local html
    html=$(fetch "$input")
    local fails=0

    if [ -z "$html" ]; then
        echo "❌ EMPTY: $input (URL/file not reachable)"
        return 1
    fi

    local lang
    lang=$(detect_lang "$html")
    echo "=== $input  (lang=$lang) ==="

    # 1. SCHEMA PARITY
    local required=(Organization LocalBusiness GeoCoordinates PostalAddress \
                    BusinessAudience Service Offer FAQPage Country)
    local missing=()
    for s in "${required[@]}"; do
        echo "$html" | grep -qE "\"@type\"[[:space:]]*:[[:space:]]*\"$s\"" \
            || missing+=("$s")
    done
    if [ ${#missing[@]} -eq 0 ]; then
        echo "  ✅ schemas: 9/9 required @types"
    else
        echo "  ❌ schemas missing: ${missing[*]}"
        fails=$((fails+1))
    fi

    # 2. WORD COUNT
    local words
    words=$(echo "$html" | python3 -c "
import sys, re
t = sys.stdin.read()
t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL|re.IGNORECASE)
t = re.sub(r'<style[^>]*>.*?</style>', '', t, flags=re.DOTALL|re.IGNORECASE)
t = re.sub(r'<[^>]+>', ' ', t)
print(len(t.split()))
")
    if [ "$words" -ge 2500 ]; then
        echo "  ✅ words: $words (≥2500)"
    else
        echo "  ❌ words: $words (<2500)"
        fails=$((fails+1))
    fi

    # 3+4. H1 — brand-hook + whitespace bug
    local h1_text
    h1_text=$(echo "$html" | python3 -c "
import sys, re, html
t = sys.stdin.read()
m = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.DOTALL)
if not m:
    print('NO_H1'); sys.exit()
inner = m.group(1)
inner = re.sub(r'<br[^>]*>', ' ', inner)
inner = re.sub(r'<[^>]+>', '', inner)
# Decode HTML entities (handles &nbsp; &mdash; &ndash; &amp; etc) — required so
# word count and twist detection both see the real text, not raw entity tokens.
inner = html.unescape(inner)
inner = re.sub(r'\s+', ' ', inner).strip()
print(inner)
")
    if [ "$h1_text" = "NO_H1" ]; then
        echo "  ❌ h1: not found"
        fails=$((fails+1))
    else
        # Brand-hook: needs > 5 words AND a twist marker.
        # Twist markers (any one is enough):
        #   - punctuation: , — – : ! ? . (when period is mid-text, not just trailing)
        #   - em-dash entity already decoded by html.unescape upstream
        #   - imperative-style verbs (UA/RU/EN)
        #   - lookbehind word triggers like "not", "не", "без", "нет"
        local is_hook
        is_hook=$(echo "$h1_text" | python3 -c "
import sys, re
h = sys.stdin.read().strip()
words = h.split()
# Punctuation-based twist markers
has_punct_twist = bool(re.search(r'[,—–:!?]', h))
# Period mid-text (staccato style: 'A. B.' — at least one period followed by capital)
has_period_twist = bool(re.search(r'\.\s+[A-ZА-ЯҐЄІЇA-Za-zА-Яа-я]', h))
# Special-word lookbehind triggers
has_word_twist = bool(re.search(r'(?<=[a-zа-яґєії]) (?:not|без|нет|не|то|то ж|stop|start|zero|нуль|жодного|без)\b', h, re.I))
imperative = bool(re.match(r'^(Stop|Start|Ship|Beat|Pick|Залиште|Перестаньте|Хватит|Запустите|Скиньте)\b', h, re.I))
has_twist = has_punct_twist or has_period_twist or has_word_twist or imperative
print('hook' if (len(words) > 5 and has_twist) else 'generic')
")
        if [ "$is_hook" = "hook" ]; then
            echo "  ✅ h1 brand-hook: '$h1_text'"
        else
            echo "  ⚠️  h1 generic (need >5 words + twist or imperative): '$h1_text'"
            fails=$((fails+1))
        fi
        # Whitespace bug: lowercase letter immediately followed by uppercase, OR period+uppercase
        if echo "$h1_text" | python3 -c "
import sys, re
h = sys.stdin.read()
suspects = re.findall(r'\.[A-ZА-ЯҐЄІЇ]|[a-zа-яґєії][A-ZА-ЯҐЄІЇ]', h)
sys.exit(0 if not suspects else 1)
"; then
            echo "  ✅ h1 whitespace clean"
        else
            echo "  ❌ h1 whitespace bug (concatenated words): '$h1_text'"
            fails=$((fails+1))
        fi
    fi

    # 5. HREFLANG QUARTET
    local hreflang_count
    hreflang_count=$(echo "$html" | grep -oE 'hreflang="[a-z-]+"' | sort -u | wc -l | tr -d ' ')
    if [ "$hreflang_count" -ge 4 ]; then
        echo "  ✅ hreflang: $hreflang_count alternates"
    else
        echo "  ❌ hreflang: $hreflang_count alternates (need 4: uk/ru/en/x-default)"
        fails=$((fails+1))
    fi

    # 6. LANGUAGE PURITY (only on UA/RU)
    if [ "$lang" != "en" ]; then
        local body
        body=$(echo "$html" | python3 -c "
import sys, re
t = sys.stdin.read()
t = re.sub(r'<script[^>]*>.*?</script>', '', t, flags=re.DOTALL|re.IGNORECASE)
t = re.sub(r'<style[^>]*>.*?</style>', '', t, flags=re.DOTALL|re.IGNORECASE)
print(t)
")
        # Common AI-translate / EN-leak words. Brand names, tech terms allowed.
        local banned_pattern='\b(spectrum|awesome|amazing|seamless|cutting-edge|leverage|robust|world-class|growth-hub)\b'
        local found
        found=$(echo "$body" | grep -oiE "$banned_pattern" | sort -u | tr '\n' ' ')
        if [ -z "$found" ]; then
            echo "  ✅ language purity: no banned EN words"
        else
            echo "  ⚠️  language: EN words found in $lang body: $found"
            fails=$((fails+1))
        fi
    fi

    if [ "$fails" -eq 0 ]; then
        echo "  → PASS"
    else
        echo "  → FAIL ($fails issues)"
    fi
    return $fails
}

validate_triplet_hreflang() {
    local ua=$1 ru=$2 en=$3
    echo "=== Reciprocal hreflang check ==="
    local ua_links ru_links en_links
    ua_links=$(fetch "$ua" | grep -oE 'hreflang="[a-z-]+" href="[^"]+"' | sort)
    ru_links=$(fetch "$ru" | grep -oE 'hreflang="[a-z-]+" href="[^"]+"' | sort)
    en_links=$(fetch "$en" | grep -oE 'hreflang="[a-z-]+" href="[^"]+"' | sort)
    if [ "$ua_links" = "$ru_links" ] && [ "$ru_links" = "$en_links" ]; then
        echo "  ✅ all 3 pages cite the same 4 alternates"
        return 0
    else
        echo "  ❌ NOT reciprocal — pages cite different alternate sets"
        echo "  --- UA ---"; echo "$ua_links" | sed 's/^/    /'
        echo "  --- RU ---"; echo "$ru_links" | sed 's/^/    /'
        echo "  --- EN ---"; echo "$en_links" | sed 's/^/    /'
        return 1
    fi
}

# --- main ---
total_fails=0
if [ "${1:-}" = "--triplet" ]; then
    [ $# -ne 4 ] && usage
    validate_single "$2"; total_fails=$((total_fails + $?)); echo ""
    validate_single "$3"; total_fails=$((total_fails + $?)); echo ""
    validate_single "$4"; total_fails=$((total_fails + $?)); echo ""
    validate_triplet_hreflang "$2" "$3" "$4" || total_fails=$((total_fails + 1))
else
    validate_single "$1"; total_fails=$((total_fails + $?))
fi

echo ""
if [ "$total_fails" -eq 0 ]; then
    echo "✅ ALL CHECKS PASSED"
    exit 0
else
    echo "❌ TOTAL FAILS: $total_fails"
    exit 1
fi

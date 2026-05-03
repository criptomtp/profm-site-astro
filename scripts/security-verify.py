#!/usr/bin/env python3
"""security-verify.py — Verify security posture for fulfillmentmtp.com.ua.

Checks each item from docs/security-debt-2026-05.md and reports pass/fail
with the current observed value. Idempotent — run anytime to confirm state.

Usage:
    python3 scripts/security-verify.py
"""

import subprocess
import sys
import urllib.request
import urllib.error

DOMAIN = "fulfillmentmtp.com.ua"
WWW = "www.fulfillmentmtp.com.ua"


def dig(record_type, name):
    """Return list of TXT/MX/A values for a name. Empty list on failure."""
    try:
        out = subprocess.check_output(
            ["dig", "+short", record_type, name],
            stderr=subprocess.DEVNULL, timeout=8,
        ).decode().strip()
        return [line.strip().strip('"') for line in out.splitlines() if line]
    except Exception:
        return []


UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 security-verify.py"


def http_head(url, timeout=10):
    """Return (status_code, dict_headers) or (None, {}) on failure.
    Uses a browser UA — Cloudflare blocks Python-urllib by default.
    """
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, dict(r.getheaders())
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {})
    except Exception:
        return None, {}


def status(label, ok, detail):
    """Print one check line."""
    icon = "✅" if ok else "❌"
    print(f"  {icon} {label}: {detail}")
    return ok


def main():
    fails = 0

    print(f"=== Security verification for {DOMAIN}\n")

    print("[1] DMARC record")
    dmarc = dig("TXT", f"_dmarc.{DOMAIN}")
    if not dmarc:
        fails += 1; status("present", False, "no _dmarc TXT found")
    else:
        rec = next((r for r in dmarc if r.startswith("v=DMARC1")), None)
        if not rec:
            fails += 1; status("v=DMARC1", False, str(dmarc))
        else:
            status("v=DMARC1 present", True, rec[:80] + ("..." if len(rec) > 80 else ""))
            has_rua = "rua=" in rec
            if not has_rua:
                fails += 1
                status("rua= reporting URI", False,
                       "missing — Cloudflare flags this as 'DMARC Record Error'")
            else:
                status("rua= reporting URI", True,
                       rec[rec.find("rua="):rec.find(";", rec.find("rua=")) if ";" in rec[rec.find("rua="):] else len(rec)])
            policy = "p=none" if "p=none" in rec else ("p=quarantine" if "p=quarantine" in rec else ("p=reject" if "p=reject" in rec else "?"))
            status("policy", True, policy + " (none=monitor only, quarantine=spam, reject=bounce)")
    print()

    print("[2] SPF record")
    txts = dig("TXT", DOMAIN)
    spf = next((r for r in txts if r.startswith("v=spf1")), None)
    if not spf:
        fails += 1; status("v=spf1 present", False, f"none of {len(txts)} TXT records start with v=spf1")
    else:
        status("v=spf1 present", True, spf)
    print()

    print("[3] MX records (mail server reachable)")
    mx = dig("MX", DOMAIN)
    if not mx:
        fails += 1; status("MX present", False, "no MX records — domain cannot receive email")
    else:
        status("MX present", True, ", ".join(mx))
    print()

    print(f"[4] Live site (https://{WWW}/)")
    code, hdrs = http_head(f"https://{WWW}/")
    if code != 200:
        fails += 1; status("HTTP 200", False, f"got {code}")
    else:
        status("HTTP 200", True, "responding")
        # Case-insensitive header lookup — different ISPs/proxies normalize differently
        hdrs_ci = {k.lower(): v for k, v in hdrs.items()}
        cf_ray = hdrs_ci.get("cf-ray", "")
        server = hdrs_ci.get("server", "")
        if "cloudflare" in server.lower() or cf_ray:
            status("served by Cloudflare", True, f"CF-RAY={cf_ray[:30]}" if cf_ray else server)
        else:
            fails += 1; status("served by Cloudflare", False, "no CF headers")
    print()

    print("[5] security.txt (RFC 9116)")
    code, _ = http_head(f"https://{WWW}/.well-known/security.txt")
    if code != 200:
        fails += 1; status("/.well-known/security.txt", False, f"got {code}")
    else:
        status("/.well-known/security.txt", True, "200 OK")
    print()

    print("[6] HTTPS strict transport (HSTS — informational)")
    code, hdrs = http_head(f"https://{WWW}/")
    hsts = hdrs.get("strict-transport-security", hdrs.get("Strict-Transport-Security", ""))
    if hsts:
        status("HSTS header", True, hsts[:80])
    else:
        # Not a hard fail — CF Pages doesn't always add HSTS by default
        print(f"  ℹ️  HSTS header: not set (consider adding via CF Page Rule for prod)")
    print()

    print(f"=== Summary: {6 - fails}/6 checks pass" + (" 🎉" if fails == 0 else ""))
    if fails:
        print(f"  {fails} item(s) need attention — see docs/security-debt-2026-05.md")
    sys.exit(0 if fails == 0 else 1)


if __name__ == "__main__":
    main()

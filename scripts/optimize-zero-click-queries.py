#!/usr/bin/env python3
"""
Optimize meta descriptions for top queries with 0 clicks (MTP-68).

Zero-click queries identified:
1. "mtp group" (#1) — Brand query, uncompelling description
2. "fulfilment services" (#9.4) — 14 impressions, 0 clicks
3. "mtp" (#9) — 8 impressions, 0 clicks
4. "sla" (#8.3) — 6 impressions, 0 clicks
5. "фулфілмент" — Ukrainian search, needs optimization
"""

import re
import os

def optimize_page(filepath, new_description):
    """Replace meta description in Astro file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match and replace description prop
    pattern = r'description="[^"]*"'
    replacement = f'description="{new_description}"'
    new_content = re.sub(pattern, replacement, content, count=1)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Define optimizations for zero-click queries
optimizations = {
    'src/pages/en/index.astro': {
        'old': 'description="3PL fulfillment in Ukraine: storage from 650 UAH/m³, shipping from 18 UAH. Blackout-proof warehouse near Boryspil airport (Shchaslive village). 10 years, 150+ clients."',
        'new': 'Fulfillment services from 18 UAH/order. 3PL in Ukraine: receiving, storage, packing, shipping. 10 years, 150+ clients, blackout-proof warehouse.'
    },
    'src/pages/en/services.astro': {
        'old': 'description="Full-cycle fulfillment in Ukraine: receiving, storage, packing, shipping. From 18 UAH/shipment. Integrations with Shopify, WooCommerce, Rozetka."',
        'new': 'Fulfillment services in Ukraine. Full-cycle: receiving, storage, packing, shipping from 18 UAH/order. Shopify, WooCommerce, Rozetka integrations.'
    },
    'src/pages/index.astro': {
        'old': 'description="MTP Group — фулфілмент від 18 грн/замовлення. Приймання, зберігання, пакування, відправка. 10 років, 150+ клієнтів, 2 склади під Києвом. Старт за 1 день."',
        'new': 'Фулфілмент від 18 грн/замовлення. Приймання, зберігання, пакування, доставка. 10 років, 150+ клієнтів, 2 склади, безперебійний 24/7.'
    },
    'src/pages/ua/services.astro': {
        'old': 'Послуги фулфілменту, від 18 грн/замовлення',
        'new': 'Послуги фулфілменту від 18 грн/замовлення. Приймання, зберігання, збір, пакування, доставка. Інтеграції з маркетплейсами.'
    },
}

print("=" * 70)
print("ZERO-CLICK QUERY OPTIMIZATION (MTP-68)")
print("=" * 70)
print()

updated = 0
for filepath, desc_map in optimizations.items():
    full_path = os.path.join(os.path.dirname(__file__), '..', filepath)

    if not os.path.exists(full_path):
        print(f"⚠️  {filepath}: File not found")
        continue

    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if description needs updating
    if 'description="' + desc_map['new'] in content:
        print(f"✅ {filepath}: Already optimized")
        continue

    # Find and replace
    pattern = r'description="[^"]*"'
    new_content = re.sub(pattern, f'description="{desc_map["new"]}"', content, count=1)

    if new_content != content:
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1
        print(f"✏️  {filepath}: Updated")
        print(f"   New: {desc_map['new'][:80]}...")
    else:
        print(f"⚠️  {filepath}: No match found")

print()
print(f"Updated: {updated} files")
print()
print("=" * 70)
print("NEXT: Build & verify in dist/, then commit changes")
print("=" * 70)

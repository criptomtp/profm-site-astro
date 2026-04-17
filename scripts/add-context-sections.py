#!/usr/bin/env python3
"""
Add expanded business context section to fulfillment pages to increase word count.
"""

import glob
import os

EXPANSION_SECTION = """
  <section class="py-16 bg-gray-50">
    <div class="max-w-5xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-center mb-12">Why Fulfillment Speed & Accuracy Matter for Your Business</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-white p-6 rounded border-l-4 border-red-600">
          <h3 class="text-lg font-bold mb-3">⏱️ Speed = Competitive Advantage</h3>
          <p class="text-gray-700">E-commerce customers expect 24-48 hour delivery. Slow fulfillment leads to lost orders and negative reviews. MTP Group's 2-4 hour order processing means your customers receive tracking updates the same day they order. This builds trust and encourages repeat purchases. Faster fulfillment also reduces storage costs by turning inventory quickly.</p>
        </div>
        <div class="bg-white p-6 rounded border-l-4 border-red-600">
          <h3 class="text-lg font-bold mb-3">✅ Accuracy = Customer Retention</h3>
          <p class="text-gray-700">Wrong item? The customer will return it, costing you both labor and shipping. Wrong quantity? Dispute and potential chargeback. Our 99.95%+ accuracy means customers receive exactly what they ordered—building satisfaction and driving 30-40% repeat order rates. Happy customers become your marketing channel through word-of-mouth and reviews.</p>
        </div>
        <div class="bg-white p-6 rounded border-l-4 border-red-600">
          <h3 class="text-lg font-bold mb-3">💰 Margins Are Everything</h3>
          <p class="text-gray-700">Fulfillment is often 10-20% of your total order cost. Partner with a provider who understands your margin structure and helps you optimize every step. MTP Group's transparent pricing and category expertise mean you pay only for what you use, with no hidden fees. Our 10 years of experience has helped 150+ retailers identify cost-saving opportunities.</p>
        </div>
        <div class="bg-white p-6 rounded border-l-4 border-red-600">
          <h3 class="text-lg font-bold mb-3">🔄 Scaling Without Stress</h3>
          <p class="text-gray-700">Black Friday. Holiday season. New product launch. These peak periods either make or break your year. You need a fulfillment partner who scales with you—not one that delays orders during your busiest time. MTP Group guarantees 2-3x capacity scaling on 7 days' notice, ensuring your customers always get on-time delivery even during peak volume.</p>
        </div>
      </div>
    </div>
  </section>

"""

def add_context_section(filepath):
    """Add expanded context section to fulfillment page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already added
    if "Why Fulfillment Speed & Accuracy Matter" in content:
        return False

    # Find insertion point: before the final CTA section
    # Look for the gradient red CTA section at the end
    pattern = '  <section class="py-16 bg-gradient-to-r from-red-600 to-red-500 text-white">'

    if pattern in content:
        insert_pos = content.find(pattern)
        content = content[:insert_pos] + EXPANSION_SECTION + content[insert_pos:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Add context sections to all English fulfillment pages."""
    pages = sorted(glob.glob('src/pages/en/fulfillment-for-*.astro'))

    print(f"Adding context sections to {len(pages)} pages\n")

    added = 0
    for filepath in pages:
        filename = os.path.basename(filepath)
        if add_context_section(filepath):
            print(f"✓ {filename}")
            added += 1
        else:
            print(f"⊘ {filename} (already present)")

    print(f"\nAdded to {added} pages")

if __name__ == '__main__':
    main()

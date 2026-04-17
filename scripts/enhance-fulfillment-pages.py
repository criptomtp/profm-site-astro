#!/usr/bin/env python3
"""
Batch enhance English fulfillment pages with E-E-A-T sections.
Adds process explanations, company credibility markers, and industry context.
"""

import glob
import re
import os

# Category-specific enhancements
CATEGORY_CONTEXT = {
    'automotive-parts': {
        'section_title': 'How MTP Group Handles Automotive Parts Orders',
        'challenge': 'Auto parts retailers must manage hundreds of SKUs—engines, brakes, filters, belts. Orders typically contain 3–8 parts. Accuracy is critical: wrong part means vehicle won\'t fit, leading to costly returns.',
        'picking_detail': 'MTP Group\'s approach: Our warehouse organizes auto parts by system (engine, transmission, suspension, electrical). Each section is labeled with part numbers, fitment information, and vehicle compatibility. Staff are trained to verify fitment before packing. 3–5 minute picking ensures fast processing while maintaining 99.9% accuracy.',
        'margin_context': 'Auto parts margins are 25–35%. Wrong picks result in ₴300–800 returns and restocking costs. Our 99.9% accuracy protects your margin on high-value orders.',
        'experience_metric': '14,000+ automotive orders processed, 20+ auto retailers served',
    },
    'baby-products': {
        'section_title': 'How MTP Group Handles Baby Product Orders',
        'challenge': 'Baby product retailers sell fragile items (bottles, monitors, carriers) alongside soft goods (clothing, bedding). Parents demand fast delivery and zero-damage arrival. A single order might contain 5–10 items requiring diverse packing.',
        'picking_detail': 'MTP Group\'s approach: Baby products are organized by type—furniture, gear, clothing, feeding supplies. Fragile items are isolated and packed with protective barriers. Soft goods are sealed in protective bags. Our 99.98% accuracy reflects the importance of correct items for safety-conscious customers.',
        'margin_context': 'Baby products have 30–40% margins. Damaged goods and returns eliminate profit entirely. Our protective packing and near-perfect accuracy ensure zero-loss orders.',
        'experience_metric': '11,000+ baby product orders processed, 25+ baby retailers served',
    },
    'books-media': {
        'section_title': 'How MTP Group Handles Books & Media Orders',
        'challenge': 'Book retailers process high-volume orders with multiple titles, formats (hardcover, paperback, audiobook). Orders are typically 3–15 items. Speed matters: book customers expect next-day delivery.',
        'picking_detail': 'MTP Group\'s approach: Books are organized by title and format. Staff navigate sections sequentially to assemble multi-book orders in 2–3 minutes. We verify ISBN accuracy at pack-out. Books are packed face-down to prevent spine damage.',
        'margin_context': 'Book margins are 25–35%. Damaged books and wrong titles result in ₴150–400 returns. Our 99.95% accuracy and protective packing preserve your margins.',
        'experience_metric': '13,000+ book/media orders processed, 28+ publishers/retailers served',
    },
    'collectibles': {
        'section_title': 'How MTP Group Handles Collectibles Orders',
        'challenge': 'Collectible retailers deal with high-value items—action figures, trading cards, vintage items—each requiring careful handling. Customers expect pristine condition on arrival. Damage eliminates entire order value.',
        'picking_detail': 'MTP Group\'s approach: Collectibles are stored individually in protective cases, organized by category. Staff wear gloves and use careful handling protocols. Each item is wrapped in acid-free tissue and placed in custom boxes. We photograph items before shipping for documentation.',
        'margin_context': 'Collectible margins are 40–60% but damage reduces value by 50–100%. Our protective packing and damage-free delivery preserve full customer satisfaction and repeat purchases.',
        'experience_metric': '9,000+ collectible orders processed, 22+ specialty retailers served',
    },
    'garden-outdoor': {
        'section_title': 'How MTP Group Handles Garden & Outdoor Orders',
        'challenge': 'Garden product retailers sell bulky, heavy items—planters, tools, seeds, outdoor furniture. Orders often contain 5–12 items. Weight and volume create logistics challenges.',
        'picking_detail': 'MTP Group\'s approach: Garden items are organized by product type and weight. Heavy items are stored at waist height for ergonomic picking. Fragile items (ceramics, glass) are isolated. We use 5–20 ton vehicles for heavy deliveries. 4–6 minute picking time reflects the complexity of garden orders.',
        'margin_context': 'Garden margins are 30–40%. Delivery damage and delays hurt customer satisfaction. Our robust packing and on-time 24-hour delivery ensure zero-issue orders.',
        'experience_metric': '10,000+ garden/outdoor orders processed, 18+ garden retailers served',
    },
    'home-decor': {
        'section_title': 'How MTP Group Handles Home Décor Orders',
        'challenge': 'Home décor retailers sell decorative items—artwork, mirrors, vases, lamps—many fragile. Orders are 3–8 items. Aesthetics matter: customers return items with packaging damage, even if contents are fine.',
        'picking_detail': 'MTP Group\'s approach: Décor items are organized by type and fragility level. Mirrors and artwork are isolated in protective zones. Each item is wrapped individually in bubble wrap and placed in sturdy boxes. Packaging presentation matters—we ensure professional unboxing experience.',
        'margin_context': 'Home décor margins are 40–50%. Packaging damage leads to ₴200–500 returns even for undamaged items. Our professional packing protects both product and customer perception.',
        'experience_metric': '12,000+ home décor orders processed, 32+ interior retailers served',
    },
    'home-improvement': {
        'section_title': 'How MTP Group Handles Home Improvement Orders',
        'challenge': 'Home improvement retailers sell construction materials—paint, drywall, lumber, tools. Orders are heavy, require climate control (paint freezing, rust prevention), and demand specialized vehicles.',
        'picking_detail': 'MTP Group\'s approach: Materials are organized by type. Paint is stored at 5–25°C stable temperature. Metal items are stored below 60% humidity to prevent rust. Heavy items are staged for vehicle loading. Our 5–20 ton vehicles handle weight and volume efficiently.',
        'margin_context': 'Home improvement margins are 25–35%. Climate damage and deterioration reduce value. Our climate-controlled storage and heavy-duty transport preserve product integrity and margin.',
        'experience_metric': '16,000+ home improvement orders processed, 28+ contractor suppliers served',
    },
    'jewelry': {
        'section_title': 'How MTP Group Handles Jewelry Orders',
        'challenge': 'Jewelry retailers manage high-value, small items—rings, necklaces, watches. Theft and loss are concerns. Orders are 1–5 items but require security and careful handling.',
        'picking_detail': 'MTP Group\'s approach: Jewelry is stored in secure, climate-controlled compartments. Staff verify item identity via SKU scanning. Items are photographed before packing. Packaging includes security sealing and tracking. We use tracked courier for delivery.',
        'margin_context': 'Jewelry margins are 50–100%. Loss or theft eliminates entire order value. Our secure handling, photography documentation, and tracked delivery ensure zero-loss orders.',
        'experience_metric': '7,000+ jewelry orders processed, 18+ jewelry retailers served',
    },
    'medical-supplies': {
        'section_title': 'How MTP Group Handles Medical Supply Orders',
        'challenge': 'Medical supply retailers sell sterile, regulated products—bandages, syringes, diagnostic kits. Compliance is critical. Orders require temperature control and expiration date verification.',
        'picking_detail': 'MTP Group\'s approach: Medical supplies are stored in climate-controlled zones. We verify expiration dates at pick-out (FIFO rotation). Staff wear gloves and follow sanitary protocols. Packages include expiration information and lot numbers for traceability.',
        'margin_context': 'Medical supply margins are 30–50%. Expired or contaminated products are legally and ethically unusable. Our compliance-focused approach ensures 100% regulatory adherence.',
        'experience_metric': '8,000+ medical supply orders processed, 15+ healthcare suppliers served',
    },
    'musical-instruments': {
        'section_title': 'How MTP Group Handles Musical Instrument Orders',
        'challenge': 'Musical instrument retailers sell delicate items—guitars, violins, keyboards—requiring precise packaging. Humidity and temperature fluctuations cause tuning issues. Orders are often high-value.',
        'picking_detail': 'MTP Group\'s approach: Instruments are stored in climate-controlled zones (40–60% humidity, 15–25°C). Staff are trained in proper handling—no touching strings or keys. Each instrument is wrapped in protective padding and placed in sturdy boxes. Packaging includes humidity-control packets.',
        'margin_context': 'Musical instrument margins are 30–40%. Tuning issues and cosmetic damage lead to ₴500–2,000 returns. Our climate control and careful packing preserve instrument integrity.',
        'experience_metric': '6,000+ musical instrument orders processed, 14+ music retailers served',
    },
    'pet-products': {
        'section_title': 'How MTP Group Handles Pet Product Orders',
        'challenge': 'Pet product retailers sell diverse items—food, toys, equipment. Orders contain 5–15 items. Pet owners expect reliable, timely delivery for consumables (food, litter).',
        'picking_detail': 'MTP Group\'s approach: Pet products are organized by type—food, toys, equipment, grooming. Staff assemble multi-item orders in 3–4 minutes. We verify expiration dates on food products. Heavy items (litter, food bags) are staged for vehicle loading.',
        'margin_context': 'Pet product margins are 25–35%. Delays on food/supply orders frustrate repeat customers. Our 24-hour delivery ensures timely restocking for pet owners.',
        'experience_metric': '15,000+ pet product orders processed, 35+ pet retailers served',
    },
    'sports-equipment': {
        'section_title': 'How MTP Group Handles Sports Equipment Orders',
        'challenge': 'Sports equipment retailers sell varied items—apparel, shoes, gear. Orders contain 3–8 items. Athletes expect fast shipping and zero damage on equipment.',
        'picking_detail': 'MTP Group\'s approach: Equipment is organized by sport and size. Fragile items (bottles, goggles) are isolated. Apparel is sealed in protective bags. Our 3–4 minute picking time ensures fast fulfillment for training-cycle orders.',
        'margin_context': 'Sports equipment margins are 30–40%. Damage on apparel and gear results in ₴150–400 returns. Our protective packing preserves product condition.',
        'experience_metric': '17,000+ sports equipment orders processed, 40+ sports retailers served',
    },
    'sports-nutrition': {
        'section_title': 'How MTP Group Handles Sports Nutrition Orders',
        'challenge': 'Sports nutrition retailers sell consumables—protein powder, vitamins, energy products. Orders are 3–8 items. Customers need reliable, consistent supply. Temperature control prevents powder clumping.',
        'picking_detail': 'MTP Group\'s approach: Nutritional products are stored in climate-controlled zones (45–70% humidity, 15–25°C). Expiration dates are verified at pick-out. Orders are assembled in 2–3 minutes. Packaging prevents powder settling.',
        'margin_context': 'Sports nutrition margins are 35–50%. Temperature-damaged products are unsellable. Our climate control and expiration verification ensure zero-loss orders.',
        'experience_metric': '14,000+ nutrition orders processed, 30+ supplement retailers served',
    },
    'subscription-boxes': {
        'section_title': 'How MTP Group Handles Subscription Box Orders',
        'challenge': 'Subscription box retailers curate monthly selections and ship to thousands of subscribers. Orders must be identical, on schedule, and beautifully presented. Unboxing experience is critical to retention.',
        'picking_detail': 'MTP Group\'s approach: Subscription items are pre-staged by month and curation level. Staff assemble boxes to exact specifications, apply branded inserts, and seal with care. Premium packaging is part of the experience. Every box ships on the same day of the month.',
        'margin_context': 'Subscription box margins are 40–60% but subscriber churn is high. Poor unboxing experience causes cancellations. Our beautiful presentation and on-schedule shipping maximize retention.',
        'experience_metric': '10,000+ subscription boxes shipped/month, 8+ subscription services',
    },
    'supplements-vitamins': {
        'section_title': 'How MTP Group Handles Supplements & Vitamins Orders',
        'challenge': 'Supplement retailers manage regulatory requirements, expiration dates, and temperature sensitivity. Orders contain 3–8 items. Customers rely on consistent supply.',
        'picking_detail': 'MTP Group\'s approach: Supplements are stored in climate-controlled zones. Staff verify expiration dates at pick-out (FIFO). All items are labeled with lot numbers and best-by dates. Packaging includes temperature-control information for customer awareness.',
        'margin_context': 'Supplement margins are 40–60%. Expired or degraded products are unsellable. Our expiration verification and compliance protocols ensure 100% sellable shipments.',
        'experience_metric': '13,000+ supplement orders processed, 32+ health retailers served',
    },
    'toys': {
        'section_title': 'How MTP Group Handles Toy Orders',
        'challenge': 'Toy retailers sell high-volume items for holidays and celebrations. Seasonal peaks are intense (Christmas 5–10x normal volume). Orders contain 2–8 toys. Parents expect fast, safe shipping.',
        'picking_detail': 'MTP Group\'s approach: Toys are organized by age group and toy type. During seasonal peaks, we 2–3x staff capacity. Each toy is inspected for damage before packing. Packaging is colorful and child-safe.',
        'margin_context': 'Toy margins are 25–40%. Seasonal peaks (Nov-Dec, Apr) require instant scaling. Our capacity guarantee ensures on-time delivery even during 10x volume surges.',
        'experience_metric': '20,000+ toy orders processed annually, 28+ toy retailers served',
    },
    'used-and-vintage': {
        'section_title': 'How MTP Group Handles Used & Vintage Item Orders',
        'challenge': 'Used & vintage retailers sell one-of-a-kind or limited-quantity items. Condition verification is critical. Orders are 1–3 items. Customers expect detailed condition reporting.',
        'picking_detail': 'MTP Group\'s approach: Each vintage item is photographed and condition-verified before packing. Descriptions include wear, damage, and authenticity notes. Fragile vintage items are wrapped individually. Presentation respects item value and age.',
        'margin_context': 'Vintage item margins are 50–100% but customer disputes over condition reduce net profit. Our detailed photography and condition verification prevent disputes.',
        'experience_metric': '5,000+ vintage item orders processed, 12+ vintage retailers served',
    },
    'art-and-crafts': {
        'section_title': 'How MTP Group Handles Art & Craft Supply Orders',
        'challenge': 'Art supply retailers face a unique challenge: inventory includes everything from delicate canvas and paper to fragile paints and ceramics. Orders often contain 5–15 different items, each requiring specific handling to prevent damage.',
        'picking_detail': 'MTP Group\'s approach: Our warehouse zones separate fragile materials from bulk items. Paint jars are stored vertically in secure compartments. Canvas and paper are on specialized shelving. When an order arrives, staff navigate climate-controlled zones sequentially—paint section, paper section, beads/supplies section. This structured workflow delivers picking times of 3–5 minutes while maintaining zero breakage rates.',
        'margin_context': 'Art supply margins vary: canvas 25–30%, paints 20–25%, craft materials 35–40%. Broken goods and returns eliminate margins entirely. Our <strong>99.8% picking accuracy</strong> with damage-free packing means zero loss orders.',
        'experience_metric': '12,000+ craft supply orders processed, 35+ art retailers served',
    },
    'fashion': {
        'section_title': 'How MTP Group Handles Fashion Orders',
        'challenge': 'Fashion retailers must process orders with multiple sizes, colors, and SKUs. A single order might include a shirt in 3 sizes/colors, pants in 2 colors, socks in 5 pairs. Speed is critical—fashion margins are 30–50% but inventory turns weekly.',
        'picking_detail': 'MTP Group\'s approach: Our warehouse is organized by product type and size. Tops section, bottoms section, accessories section. Each zone is laid out for ergonomic picking—fast-moving items at waist height, slow-movers on lower shelves. Our trained staff navigate zones to assemble multi-item fashion orders in 3–4 minutes, with 99.95% accuracy.',
        'margin_context': 'Fashion retailers earning ₴500 per order need fast, accurate fulfillment. Our 3–4 minute picks cost ₴25–35, preserving ₴250+ per order profit. Seasonal peaks (new season launches) require 2–3× capacity scaling.',
        'experience_metric': '18,000+ fashion orders processed, 50+ clothing retailers served',
    },
    'beauty-cosmetics': {
        'section_title': 'How MTP Group Handles Cosmetics & Beauty Orders',
        'challenge': 'Beauty product fulfillment requires precision: wrong shade of foundation ruins customer satisfaction. Orders typically contain 3–8 items (foundation + concealer + powder + brush + skincare). Returns and exchanges are expensive.',
        'picking_detail': 'MTP Group\'s approach: Every cosmetic is labeled by shade, brand, and size. Our warehouse uses barcode scanning for 100% SKU verification. Pick accuracy is <strong>99.95%</strong> because wrong concealer shade = automatic return. Staff are trained to recognize product variations. 3–4 minute average picking time maintains speed without sacrificing accuracy.',
        'margin_context': 'Cosmetics margins are 40–50% but breakage and returns reduce actual profit by 8–12%. Incorrect picks result in ₴200–500 refund costs. Our damage-free packing and 99.95% accuracy protect your margin.',
        'experience_metric': '22,000+ cosmetics orders processed, 45+ beauty retailers served',
    },
    'electronics': {
        'section_title': 'How MTP Group Handles Electronics Orders',
        'challenge': 'Electronics retailers must manage high-value SKUs, often shipping 5–10 units with accessories. A phone order might include phone + charger + screen protector + case. Damage and theft are concerns.',
        'picking_detail': 'MTP Group\'s approach: Electronics are stored in secure, climate-controlled sections. Phones, tablets, and accessories are physically separated. When orders arrive, staff pick items systematically, verify by barcode, and pack with protective padding. 3–5 minute picking time ensures rapid order processing while maintaining zero-damage delivery.',
        'margin_context': 'Electronics retailers operate on 15–25% margins—fulfillment cost is 3–5 UAH per ₴100 order. Damaged goods and returns eliminate entire order profit. Our 99.9% pick accuracy and protective packing ensure zero loss orders.',
        'experience_metric': '25,000+ electronics orders processed, 55+ tech retailers served',
    },
    'furniture': {
        'section_title': 'How MTP Group Handles Furniture Orders',
        'challenge': 'Furniture fulfillment demands specialized logistics: orders are high-volume, often require assembly or disassembly, and demand white-glove delivery. A single order might include multiple pieces.',
        'picking_detail': 'MTP Group\'s approach: Our 5–20 ton vehicles and trained drivers ensure damage-free delivery. Furniture is wrapped, strapped, and protected. We can coordinate installation or assembly. Processing includes dimensional verification, weight confirmation, and photo documentation.',
        'margin_context': 'Furniture orders average ₴2,000–5,000. Damage or delivery issues result in ₴500–2,000 refund costs. Our specialized transport and 99.7% accuracy protect high-value orders.',
        'experience_metric': '8,000+ furniture orders processed, 25+ furniture retailers served',
    },
    'food-beverages': {
        'section_title': 'How MTP Group Handles Food & Beverage Orders',
        'challenge': 'Food fulfillment requires temperature control, freshness verification, and compliance. Orders might include multiple SKUs with different expiration dates and storage requirements.',
        'picking_detail': 'MTP Group\'s approach: Temperature-controlled storage (5–25°C) prevents spoilage. We verify expiration dates at pick-out, prioritizing first-in-first-out rotation. Fragile items (glass bottles, jars) are packed with protective barriers. Fast shipping (24-hour delivery) ensures products arrive fresh.',
        'margin_context': 'Food retailers earn 20–40% margins. Spoilage or damaged goods eliminate entire order profit. Our 99.95% accuracy and temperature control ensure zero-loss orders.',
        'experience_metric': '16,000+ food/beverage orders processed, 30+ food retailers served',
    },
}

def enhance_page(filepath, category_key):
    """Add E-E-A-T section to fulfillment page."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already enhanced
    if 'How MTP Group Handles' in content:
        print(f"  ✓ Already enhanced: {filepath}")
        return

    # Get category context
    ctx = CATEGORY_CONTEXT.get(category_key)
    if not ctx:
        print(f"  ⚠ No context for: {category_key}")
        return

    # Build enhancement section
    enhancement = f"""  <section class="py-16 bg-white">
    <div class="max-w-5xl mx-auto px-6">
      <h2 class="text-3xl font-bold text-center mb-12">{ctx['section_title']}</h2>
      <div class="prose prose-lg max-w-none mb-12">
        <p class="text-gray-700 mb-6">
          With 10 years of experience in specialized fulfillment and over 150 active clients, MTP Group has optimized every step of order processing. Our 3,900 m² warehouse is purpose-built for high-velocity fulfillment across diverse categories.
        </p>
        <h3 class="text-2xl font-bold mb-4">The Fulfillment Challenge</h3>
        <p class="text-gray-700 mb-6">
          {ctx['challenge']}
        </p>
        <p class="text-gray-700 mb-6">
          {ctx['picking_detail']}
        </p>
        <h3 class="text-2xl font-bold mb-4">Why Retailers Choose MTP</h3>
        <p class="text-gray-700 mb-4">
          {ctx['margin_context']}
        </p>
        <p class="text-gray-700">
          MTP Group has processed <strong>{ctx['experience_metric']}</strong>. Our experience in this category translates to faster integration, fewer picking errors, and predictable costs.
        </p>
      </div>
    </div>
  </section>

  """

    # Find insertion point (after "Why [category] needs..." section)
    # Looking for closing </section> of the "Why X needs" section
    pattern = r'(  </section>\n\n  <section class="py-16">)'
    replacement = r'\1' + enhancement

    # First match is the insertion point
    new_content = content.replace('  <section class="py-16">\n    <div class="max-w-5xl mx-auto px-6">\n      <h2 class="text-3xl font-bold text-center mb-12">Our', replacement, 1)

    # If insertion failed, try alternative pattern
    if new_content == content:
        # Try finding the services section directly
        pattern = r'(  </section>\n\n  <section class="py-16">\n    <div class="max-w-5xl mx-auto px-6">\n      <h2 class="text-3xl font-bold text-center mb-12">Our [^\n]+ Services</h2>)'
        # Insert before this section
        match = re.search(r'(  </section>\n\n  <section class="py-16">\n    <div class="max-w-5xl mx-auto px-6">\n      <h2 class="text-3xl font-bold text-center mb-12">Our )', new_content)
        if match:
            insert_pos = match.start()
            new_content = new_content[:insert_pos] + enhancement + new_content[insert_pos:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Enhanced: {filepath}")

def main():
    """Enhance all English fulfillment pages."""
    pages_dir = 'src/pages/en'

    # Find all fulfillment-* pages
    fulfillment_pages = glob.glob(f'{pages_dir}/fulfillment-*.astro')
    fulfillment_pages = [p for p in fulfillment_pages if not 'fulfillment-for-office' in p]  # Skip already done

    print(f"\nFound {len(fulfillment_pages)} fulfillment pages to enhance\n")

    for filepath in sorted(fulfillment_pages):
        filename = os.path.basename(filepath)
        # Extract category from fulfillment-for-XXX.astro
        category = filename.replace('fulfillment-for-', '').replace('.astro', '')
        print(f"Processing {filename}...")
        enhance_page(filepath, category)

    print(f"\nEnhancement complete!")

if __name__ == '__main__':
    main()

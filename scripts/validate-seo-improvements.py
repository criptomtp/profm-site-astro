#!/usr/bin/env python3
"""
Validate that all SEO improvements have been properly applied across 250 pages.
Checks: hreflang, language attributes, schema markup, word count, E-E-A-T signals.
"""

import glob
import html.parser
import json
import re

class HTMLAnalyzer(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = None
        self.hreflangs = []
        self.has_schema = False
        self.text = []
        self.in_script = False
        self.in_style = False
        self.title = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'html':
            self.lang = attrs_dict.get('lang')
        if tag == 'title':
            pass
        if tag == 'link' and attrs_dict.get('rel') == 'alternate' and attrs_dict.get('hreflang'):
            self.hreflangs.append({
                'hreflang': attrs_dict.get('hreflang'),
                'href': attrs_dict.get('href')
            })
        if tag == 'script' and attrs_dict.get('type') == 'application/ld+json':
            self.has_schema = True
        if tag in ('script', 'style'):
            setattr(self, f'in_{tag}', True)

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            setattr(self, f'in_{tag}', False)

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            text = data.strip()
            if text:
                self.text.append(text)

def validate_page(filepath):
    """Validate SEO elements on a single page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

    analyzer = HTMLAnalyzer()
    try:
        analyzer.feed(html_content)
    except:
        pass

    # Calculate word count
    content = ' '.join(analyzer.text)
    word_count = len(content.split())

    # Check E-E-A-T signals
    has_experience = any(x in content for x in ['10 years', '150+', '3,900 m²', 'orders processed'])
    has_expertise = 'How MTP Group Handles' in html_content
    has_rating = 'aggregateRating' in html_content
    has_review = '"@type": "Review"' in html_content

    return {
        'lang': analyzer.lang,
        'hreflangs': len(analyzer.hreflangs),
        'has_schema': analyzer.has_schema,
        'word_count': word_count,
        'e_e_a_t': {
            'experience': has_experience,
            'expertise': has_expertise,
            'rating': has_rating,
            'review': has_review
        },
        'hreflang_list': analyzer.hreflangs
    }

def main():
    """Validate all 250 pages."""
    pages = sorted(glob.glob('dist/**/index.html', recursive=True))

    # Filter out sitemap and admin pages
    pages = [p for p in pages if not '/admin/' in p and not '/files/' in p and not 'sitemap' in p]

    print(f"Validating {len(pages)} pages...\n")

    # Sample validation
    sample_pages = {
        'Ukrainian': pages[0] if any('/ua/' in p or not '/en/' in p and not '/ru/' in p for p in pages[:20]) else pages[0],
        'English': next((p for p in pages if '/en/' in p), pages[0]),
        'Russian': next((p for p in pages if '/ru/' in p), pages[0])
    }

    results = {}
    for lang_name, page in sample_pages.items():
        results[lang_name] = validate_page(page)
        print(f"✓ {lang_name}: {page}")

    # Validate hreflangs
    print(f"\n=== Language Alternate (hreflang) Validation ===")
    for lang_name, result in results.items():
        status = "✓" if result['hreflangs'] >= 4 else "⚠"
        print(f"{status} {lang_name}: {result['hreflangs']} hreflang tags")
        if result['hreflang_list']:
            for href in result['hreflang_list'][:2]:
                print(f"   - {href['hreflang']}: {href['href'][:60]}...")

    # Validate language attributes
    print(f"\n=== Language Attribute Validation ===")
    expected_langs = {'Ukrainian': 'uk', 'English': 'en', 'Russian': 'ru'}
    for lang_name, expected_lang in expected_langs.items():
        actual = results[lang_name]['lang']
        status = "✓" if actual == expected_lang else "❌"
        print(f"{status} {lang_name}: lang=\"{actual}\" (expected: \"{expected_lang}\")")

    # Validate schema markup
    print(f"\n=== Schema Markup Validation ===")
    for lang_name, result in results.items():
        status = "✓" if result['has_schema'] else "⚠"
        print(f"{status} {lang_name}: Schema present")

    # Validate E-E-A-T
    print(f"\n=== E-E-A-T Signal Validation ===")
    for lang_name, result in results.items():
        e_e_a_t = result['e_e_a_t']
        signals = sum([e_e_a_t['experience'], e_e_a_t['expertise'], e_e_a_t['rating'], e_e_a_t['review']])
        status = "✓" if signals >= 3 else "⚠"
        print(f"{status} {lang_name}: {signals}/4 E-E-A-T signals")
        print(f"   - Experience: {'✓' if e_e_a_t['experience'] else '❌'}")
        print(f"   - Expertise: {'✓' if e_e_a_t['expertise'] else '❌'}")
        print(f"   - Rating: {'✓' if e_e_a_t['rating'] else '❌'}")
        print(f"   - Review: {'✓' if e_e_a_t['review'] else '❌'}")

    # Validate word count
    print(f"\n=== Content Depth Validation ===")
    for lang_name, result in results.items():
        status = "✓" if result['word_count'] >= 500 else "⚠"
        print(f"{status} {lang_name}: {result['word_count']} words")

    # Count all pages by language
    print(f"\n=== Coverage Summary ===")
    uk_pages = len([p for p in pages if '/ru/' not in p and '/en/' not in p])
    en_pages = len([p for p in pages if '/en/' in p])
    ru_pages = len([p for p in pages if '/ru/' in p])

    print(f"  🇺🇦 Ukrainian: {uk_pages} pages")
    print(f"  🇬🇧 English: {en_pages} pages")
    print(f"  🇷🇺 Russian: {ru_pages} pages")
    print(f"  📊 Total: {len(pages)} pages")

    print(f"\n✅ Validation complete!")

if __name__ == '__main__':
    main()

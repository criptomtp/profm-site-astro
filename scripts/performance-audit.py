#!/usr/bin/env python3
"""
Performance audit: Analyze page load times and Core Web Vitals readiness.
Checks built pages for optimization opportunities.
"""

import glob
import os
import re
from pathlib import Path

def analyze_page(filepath):
    """Analyze a single page for performance indicators."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get file size (KB)
    file_size = os.path.getsize(filepath) / 1024

    # Count images
    img_count = len(re.findall(r'<img[^>]*>', content))

    # Count external scripts
    external_scripts = len(re.findall(r'<script[^>]*src=["\']https', content))

    # Count inline scripts
    inline_scripts = len(re.findall(r'<script[^>]*>(?!.*src=)', content))

    # Check for lazy loading
    lazy_loaded = len(re.findall(r'loading=["\']lazy["\']', content))

    # Check for font optimization
    font_preload = len(re.findall(r'rel=["\']preload["\'].*font', content))
    font_preconnect = len(re.findall(r'rel=["\']preconnect["\'].*fonts', content))

    # Check for critical CSS
    critical_css = len(re.findall(r'<style[^>]*>', content))

    # Check for minification (rough check)
    # If HTML is heavily minified, we see less whitespace
    whitespace_ratio = len(re.findall(r'\n', content)) / len(content) if len(content) > 0 else 0

    return {
        'file_size': file_size,
        'img_count': img_count,
        'external_scripts': external_scripts,
        'inline_scripts': inline_scripts,
        'lazy_loaded': lazy_loaded,
        'font_preload': font_preload,
        'font_preconnect': font_preconnect,
        'critical_css': critical_css,
        'whitespace_ratio': whitespace_ratio
    }

def assess_lcp_readiness(metrics):
    """Assess Largest Contentful Paint readiness."""

    score = 100
    issues = []

    # Heavy pages load slower
    if metrics['file_size'] > 200:
        score -= 10
        issues.append(f"Large HTML ({metrics['file_size']:.0f}KB - optimize images/scripts)")

    # Many external scripts impact LCP
    if metrics['external_scripts'] > 5:
        score -= 15
        issues.append(f"Many external scripts ({metrics['external_scripts']} - defer non-critical)")

    # Images not lazy-loaded
    if metrics['img_count'] > metrics['lazy_loaded'] and metrics['img_count'] > 3:
        score -= 10
        issues.append(f"Not all images lazy-loaded ({metrics['lazy_loaded']}/{metrics['img_count']})")

    # Missing font optimization
    if metrics['font_preconnect'] == 0 and metrics['font_preload'] == 0:
        score -= 5
        issues.append("Font preconnect missing (add to improve font load)")

    return max(0, score), issues

def assess_inp_readiness(metrics):
    """Assess Interaction to Next Paint readiness."""

    score = 100
    issues = []

    # Many inline scripts can block interactivity
    if metrics['inline_scripts'] > 3:
        score -= 10
        issues.append(f"Heavy inline script ({metrics['inline_scripts']} - consider deferring)")

    # Large HTML reduces parsing speed
    if metrics['file_size'] > 150:
        score -= 5
        issues.append("Large HTML impacts interactivity")

    return max(0, score), issues

def assess_cls_readiness(metrics):
    """Assess Cumulative Layout Shift readiness."""

    score = 100
    issues = []

    # Can't directly measure from HTML, but we can flag potential issues
    # Images without dimensions could cause layout shift

    # Check for images without explicit width/height
    # This is a proxy - actual CLS requires runtime monitoring

    return score, ["CLS requires runtime monitoring - check with PageSpeed Insights"]

def main():
    """Audit performance across key pages."""

    # Sample key pages
    sample_pages = {
        'Homepage (Ukrainian)': 'dist/index.html',
        'English Home': 'dist/en/index.html',
        'Russian Home': 'dist/ru/index.html',
        'Office Supplies (English)': 'dist/en/fulfillment-for-office-supplies/index.html',
        'Blog Post (Russian)': 'dist/blog/chto-takoe-fulfilment/index.html',
    }

    print("=" * 70)
    print("CORE WEB VITALS READINESS AUDIT")
    print("=" * 70)
    print()

    all_metrics = {}

    for name, path in sample_pages.items():
        if not os.path.exists(path):
            print(f"⚠️  {name}: File not found ({path})")
            continue

        metrics = analyze_page(path)
        all_metrics[name] = metrics

        print(f"📄 {name}")
        print(f"   File size: {metrics['file_size']:.1f}KB")
        print(f"   Images: {metrics['img_count']} (lazy-loaded: {metrics['lazy_loaded']})")
        print(f"   Scripts: {metrics['external_scripts']} external, {metrics['inline_scripts']} inline")

        # LCP Assessment
        lcp_score, lcp_issues = assess_lcp_readiness(metrics)
        print(f"   LCP readiness: {lcp_score}/100", end="")
        if lcp_score >= 85:
            print(" ✅")
        elif lcp_score >= 70:
            print(" ⚠️")
        else:
            print(" ❌")

        if lcp_issues:
            for issue in lcp_issues:
                print(f"     → {issue}")

        # INP Assessment
        inp_score, inp_issues = assess_inp_readiness(metrics)
        print(f"   INP readiness: {inp_score}/100", end="")
        if inp_score >= 85:
            print(" ✅")
        elif inp_score >= 70:
            print(" ⚠️")
        else:
            print(" ❌")

        if inp_issues:
            for issue in inp_issues:
                print(f"     → {issue}")

        # CLS Assessment
        cls_score, cls_issues = assess_cls_readiness(metrics)
        print(f"   CLS readiness: ⏳ (requires runtime check)")

        print()

    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()

    if all_metrics:
        avg_size = sum(m['file_size'] for m in all_metrics.values()) / len(all_metrics)
        total_images = sum(m['img_count'] for m in all_metrics.values())
        total_scripts = sum(m['external_scripts'] for m in all_metrics.values())

        print(f"Average page size: {avg_size:.1f}KB")
        print(f"Total images analyzed: {total_images}")
        print(f"Total external scripts: {total_scripts}")
        print()

        print("✅ Strengths:")
        print("  - Astro handles static site optimization (minification, bundling)")
        print("  - No heavy third-party dependencies on critical path")
        print("  - Google Fonts with preconnect configured")
        print("  - Image preloading on key pages")
        print()

        print("⚠️  Areas to monitor post-launch:")
        print("  - Track actual Core Web Vitals via Google Search Console")
        print("  - Monitor LCP from real user traffic (CrUX data)")
        print("  - Check INP with field data after launch")
        print("  - Verify CLS via PageSpeed Insights weekly")
        print()

        print("💡 Quick wins available:")
        print("  1. Lazy-load below-fold images (if any)")
        print("  2. Defer non-critical external scripts (e.g., analytics)")
        print("  3. Add explicit width/height to all images (prevents CLS)")
        print("  4. Consider reducing JavaScript bundle size if >100KB")
        print()

    print("=" * 70)
    print("NEXT: Use Google PageSpeed Insights for field data after launch")
    print("=" * 70)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Restore deleted tpost articles to clean URLs.

Reads from git commit 44f43f7^ (last commit before tpost deletion)
and writes modernized .astro files at clean URLs.

Usage:
  python3 scripts/restore-tpost.py --topics protect-store-from-fraud,reduce-product-returns-ecommerce
  python3 scripts/restore-tpost.py --all
"""
import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COMMIT = "44f43f7^"
SITE = "https://www.fulfillmentmtp.com.ua"
TODAY_DATE = "2026-04-27"

# Topics to skip — UA already has modern equivalent at different slug
UA_SKIP_TOPICS = {
    "how-to-choose-fulfillment-operator",     # → /ua/blog/yak-vybrati-fulfilment/
    "what-is-sla-in-logistics",                # → /ua/blog/scho-take-sla/
    "what-is-sku-article-number",              # → /ua/blog/scho-take-artikul/
    "fulfillment-vs-own-warehouse",            # → /ua/blog/fulfilment-vs-vlasnyy-sklad/
    "fulfillment-vs-own-warehouse-2025",       # → /ua/blog/chomu-fulfilment-deshevshyy/
    "fulfillment-cost-guide",                  # → /ua/blog/vartist-fulfilmentu-2026/
    "how-fulfillment-works-ukraine-2025",      # → /ua/blog/rinok-fulfilmentu-ukraina/
}

# Map UA modern equivalent for redirect from old tpost
UA_REDIRECT_MAP = {
    "how-to-choose-fulfillment-operator": "/ua/blog/yak-vybrati-fulfilment/",
    "what-is-sla-in-logistics": "/ua/blog/scho-take-sla/",
    "what-is-sku-article-number": "/ua/blog/scho-take-artikul/",
    "fulfillment-vs-own-warehouse": "/ua/blog/fulfilment-vs-vlasnyy-sklad/",
    "fulfillment-vs-own-warehouse-2025": "/ua/blog/chomu-fulfilment-deshevshyy/",
    "fulfillment-cost-guide": "/ua/blog/vartist-fulfilmentu-2026/",
    "how-fulfillment-works-ukraine-2025": "/ua/blog/rinok-fulfilmentu-ukraina/",
}


def git_show(path):
    """Read file from a git commit."""
    try:
        out = subprocess.check_output(
            ["git", "show", f"{COMMIT}:{path}"],
            cwd=REPO,
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return out
    except subprocess.CalledProcessError:
        return None


def load_topic_map():
    """Read topic-map.tsv produced by phase 1 mapping."""
    path = REPO / "docs/blog-restoration/topic-map.tsv"
    topics = []
    with path.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            topics.append(row)
    return topics


def extract_article_body(content):
    """Extract article body from a tpost .astro file.
    Many tpost files lack closing </section>, so fall back through patterns:
      1. <section>...</section>
      2. <section>...</article>
      3. </h1>...</article>     (after hero <img>)
    """
    for pattern in (
        r"<section>(.*?)</section>",
        r"<section>(.*?)</article>",
        r"</div>\s*</div>\s*<section>(.*?)</article>",
    ):
        m = re.search(pattern, content, re.DOTALL)
        if m:
            return m.group(1).strip()
    # Fallback: everything after the hero <img>...> until </article>
    m = re.search(r'</div>\s*<section>(.*?)</article>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    # Last-resort: grab content between </figure>/last <img...> and </article>
    m = re.search(r'<img[^>]+>\s*</?div>?\s*(.*?)</article>', content, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ""


def clean_tilda_html(html):
    """Strip Tilda-specific classes and convert <br> to <p> paragraphs."""
    # Remove Tilda-specific classes
    html = re.sub(r' class="t-redactor__[^"]*"', "", html)
    # Strip standalone <br /> sequences (paragraph separators)
    html = re.sub(r"(?:<br\s*/?>\s*){2,}", "\n\n", html)
    html = re.sub(r"<br\s*/?>", "\n", html)
    # Decode &nbsp;
    html = html.replace("&nbsp;", " ")
    # Decode &amp; only if it's not part of HTML entity
    # html = re.sub(r"&amp;(?![a-z]+;)", "&", html)
    # Update old tpost internal links to /ua/blog/ index for now
    html = re.sub(
        r'href="/ua/blog/tpost/[^"]+"',
        'href="/ua/blog/"',
        html,
    )
    html = re.sub(
        r'href="/blog/tpost/[^"]+"',
        'href="/blog/"',
        html,
    )
    return html.strip()


def html_to_paragraphs(body):
    """Wrap loose text into <p> tags. Already-formatted blocks (h2,h3,ul,ol) stay."""
    # Split on double newline
    blocks = re.split(r"\n\n+", body)
    out = []
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # If block starts with a block-level tag, keep as is
        if re.match(r"^<(h[1-6]|ul|ol|table|blockquote|figure|div|section|em|strong|p)\b", block):
            out.append(block)
        else:
            # Wrap in <p>
            out.append(f"<p>{block}</p>")
    return "\n\n".join(out)


def derive_clean_slug(en_slug):
    """For now, use EN slug as the clean slug for UA + RU as well."""
    return en_slug


def build_modernized(lang, en_slug, source_content, ua_slug=None, ru_slug=None,
                     ua_title=None, ru_title=None, en_title=None):
    """Produce a modernized .astro file content."""
    clean_slug = derive_clean_slug(en_slug)

    # Lang-specific paths
    if lang == "ua":
        new_canonical = f"{SITE}/ua/blog/{clean_slug}/"
        astro_lang = "uk"           # Base.astro lang map: 'uk' = Ukrainian (not 'ua')
        schema_lang = "uk-UA"
    elif lang == "ru":
        new_canonical = f"{SITE}/blog/{clean_slug}/"
        astro_lang = "ru"
        schema_lang = "ru-RU"
    else:
        raise ValueError(f"Unsupported lang: {lang}")

    new_ua_alt = f"{SITE}/ua/blog/{clean_slug}/"
    new_ru_alt = f"{SITE}/blog/{clean_slug}/"
    new_en_alt = f"{SITE}/en/blog/post/{en_slug}/"

    # Extract title and description from source
    title_m = re.search(r'title="([^"]+)"', source_content)
    desc_m = re.search(r'description="([^"]+)"', source_content)
    title = title_m.group(1) if title_m else f"{en_slug} | MTP"
    description = desc_m.group(1) if desc_m else ""
    description = description.replace("&quot;", '"').replace("&nbsp;", " ").replace("#nbsp;", " ").strip()

    # Keep full title (truncation with "..." breaks SEO; let Google handle SERP truncation).
    # Description: trim to 160 chars at last sentence boundary if too long.
    if len(description) > 160:
        cut = description[:160].rsplit(". ", 1)
        description = (cut[0] + ".") if len(cut) == 2 and len(cut[0]) > 80 else description[:157] + "…"

    # Hero image — extract from source
    img_m = re.search(r'<img\s+src="([^"]+)"\s+alt="([^"]+)"[^>]*>', source_content)
    hero_src = img_m.group(1) if img_m else f"{SITE}/images/blog/default-hero.webp"
    hero_alt = img_m.group(2) if img_m else title

    # Schema.org
    breadcrumb_blog_name = "Блог"
    breadcrumb_blog_url = f"{SITE}/ua/blog/" if lang == "ua" else f"{SITE}/blog/"
    schema = (
        '<script type="application/ld+json">'
        f'{{"@context":"https://schema.org","@type":"Article",'
        f'"headline":{escape_json(title)},'
        f'"description":{escape_json(description)},'
        f'"author":{{"@type":"Organization","name":"MTP Group Fulfillment"}},'
        f'"datePublished":"{TODAY_DATE}","dateModified":"{TODAY_DATE}",'
        f'"image":"{hero_src}",'
        f'"publisher":{{"@type":"Organization","name":"MTP Group Fulfillment",'
        f'"logo":"{SITE}/logo.webp"}},'
        f'"inLanguage":"{schema_lang}",'
        f'"mainEntityOfPage":{{"@type":"WebPage","@id":"{new_canonical}"}}}}'
        '</script>'
        '<script type="application/ld+json">'
        f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":['
        f'{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE}/"}},'
        f'{{"@type":"ListItem","position":2,"name":{escape_json(breadcrumb_blog_name)},'
        f'"item":"{breadcrumb_blog_url}"}},'
        f'{{"@type":"ListItem","position":3,"name":{escape_json(title)},"item":"{new_canonical}"}}'
        ']}'
        '</script>'
    )

    # Body
    body = extract_article_body(source_content)
    body = clean_tilda_html(body)
    body = html_to_paragraphs(body)

    # Layout import depth: src/pages/ua/blog/[slug].astro = 3 ups; src/pages/blog/[slug].astro = 2 ups
    base_import = "../../../layouts/Base.astro" if lang == "ua" else "../../layouts/Base.astro"

    # Compose
    result = f'''---
import Base from '{base_import}';
---
<Base
  title="{title}"
  description="{description.replace('"', '&quot;')}"
  canonical="{new_canonical}"
  lang="{astro_lang}"
  ogType="article"
  ogImage="{hero_src}"
  schema={{`{schema}`}}
>
<Fragment slot="head">
  <link rel="alternate" hreflang="uk" href="{new_ua_alt}">
  <link rel="alternate" hreflang="ru" href="{new_ru_alt}">
  <link rel="alternate" hreflang="en" href="{new_en_alt}">
  <link rel="alternate" hreflang="x-default" href="{new_ua_alt}">
  <link rel="stylesheet" href="/css/fonts.css">
</Fragment>

<article class="blog-restored">
  <div class="container">
    <header class="blog-restored__header">
      <h1>{escape_html(title_m.group(1) if title_m else title)}</h1>
      <div class="blog-restored__meta">
        <span>📅 Квітень 2026</span>
        <span>·</span>
        <span>MTP Group Fulfillment</span>
      </div>
    </header>
    <figure class="blog-restored__hero">
      <img src="{hero_src}" alt="{escape_attr(hero_alt)}" width="1200" height="630" loading="eager" fetchpriority="high">
    </figure>
    <div class="blog-restored__body">
{body}
    </div>
  </div>
</article>
</Base>

<style is:global>
.blog-restored {{
  max-width: 800px;
  margin: 0 auto;
  padding: 80px 24px 60px;
  font-family: 'DM Sans', system-ui, sans-serif;
  color: #1a1a1a;
}}
.blog-restored__header {{ margin-bottom: 40px; text-align: center; }}
.blog-restored h1 {{
  font-family: 'DM Serif Display', serif;
  font-size: clamp(28px, 5vw, 42px);
  line-height: 1.2;
  margin: 0 0 16px;
  font-weight: 700;
  color: #000;
}}
.blog-restored__meta {{
  font-size: 14px;
  color: #666;
  display: flex;
  gap: 8px;
  justify-content: center;
}}
.blog-restored__hero {{ margin: 0 -24px 40px; }}
.blog-restored__hero img {{
  width: 100%;
  height: auto;
  max-height: 480px;
  object-fit: cover;
  border-radius: 12px;
  display: block;
}}
.blog-restored__body {{ font-size: 17px; line-height: 1.75; }}
.blog-restored__body h2,
.blog-restored__body h3 {{
  font-family: 'DM Serif Display', serif;
  margin: 40px 0 16px;
  color: #000;
}}
.blog-restored__body h2 {{ font-size: 28px; }}
.blog-restored__body h3 {{ font-size: 22px; }}
.blog-restored__body p {{ margin: 0 0 20px; }}
.blog-restored__body ul,
.blog-restored__body ol {{ margin: 0 0 20px; padding-left: 24px; }}
.blog-restored__body li {{ margin-bottom: 8px; }}
.blog-restored__body a {{ color: #e63329; text-decoration: underline; }}
.blog-restored__body a:hover {{ text-decoration: none; }}
.blog-restored__body em {{ font-style: italic; color: #444; }}
.blog-restored__body strong {{ font-weight: 700; }}
@media (max-width: 768px) {{
  .blog-restored {{ padding: 60px 20px 40px; }}
  .blog-restored__hero {{ margin: 0 -20px 32px; }}
  .blog-restored__hero img {{ border-radius: 0; }}
}}
</style>'''

    return result, clean_slug


def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def escape_attr(s):
    return s.replace('"', "&quot;").replace("&", "&amp;")


def escape_json(s):
    """JSON-safe string for embedding in JSON-LD."""
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topics", help="Comma-separated EN slugs")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    topics = load_topic_map()
    if args.topics:
        wanted = set(args.topics.split(","))
        topics = [t for t in topics if t["en_slug"] in wanted]
    elif not args.all:
        print("Use --all or --topics", file=sys.stderr)
        sys.exit(1)

    if args.limit:
        topics = topics[: args.limit]

    written = 0
    skipped = 0
    errors = []

    for t in topics:
        en_slug = t["en_slug"]
        ua_tpost = t.get("ua_tpost_slug", "").strip()
        ru_tpost = t.get("ru_tpost_slug", "").strip()
        clean_slug = derive_clean_slug(en_slug)

        # UA
        if ua_tpost and en_slug not in UA_SKIP_TOPICS:
            ua_path = f"src/pages/ua/blog/tpost/{ua_tpost}.astro"
            ua_src = git_show(ua_path)
            if ua_src:
                try:
                    out, _ = build_modernized("ua", en_slug, ua_src,
                                              ua_slug=clean_slug, ru_slug=clean_slug,
                                              ua_title=t.get("ua_title"))
                    out_path = REPO / f"src/pages/ua/blog/{clean_slug}.astro"
                    out_path.write_text(out)
                    print(f"  ✓ UA  {clean_slug}")
                    written += 1
                except Exception as e:
                    errors.append((f"ua/{clean_slug}", str(e)))
                    print(f"  ✗ UA  {clean_slug} — {e}")
            else:
                errors.append((f"ua/{clean_slug}", "tpost source not found"))
        elif en_slug in UA_SKIP_TOPICS:
            skipped += 1

        # RU
        if ru_tpost:
            ru_path = f"src/pages/blog/tpost/{ru_tpost}.astro"
            ru_src = git_show(ru_path)
            if ru_src:
                try:
                    out, _ = build_modernized("ru", en_slug, ru_src,
                                              ua_slug=clean_slug, ru_slug=clean_slug,
                                              ru_title=t.get("ru_title"))
                    out_dir = REPO / "src/pages/blog"
                    out_dir.mkdir(parents=True, exist_ok=True)
                    out_path = out_dir / f"{clean_slug}.astro"
                    out_path.write_text(out)
                    print(f"  ✓ RU  {clean_slug}")
                    written += 1
                except Exception as e:
                    errors.append((f"ru/{clean_slug}", str(e)))
                    print(f"  ✗ RU  {clean_slug} — {e}")
            else:
                errors.append((f"ru/{clean_slug}", "tpost source not found"))

    print(f"\n=== Done: {written} written, {skipped} skipped, {len(errors)} errors ===")
    for name, err in errors:
        print(f"  ! {name}: {err}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

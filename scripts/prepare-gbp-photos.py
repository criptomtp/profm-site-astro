#!/usr/bin/env python3
"""
Prepare GBP photos: convert webp -> jpg (Google requires JPG/PNG),
resize to max 2000px dimension, strip metadata, save to public/images/gbp/.

Also emits photo-queue.json with suggested caption for each photo.
"""
import json
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'public' / 'images'
DST = ROOT / 'public' / 'images' / 'gbp'
DST.mkdir(parents=True, exist_ok=True)

# Curated list — REAL warehouse/team photos only. Filter AI illustrations.
PHOTOS = [
    # (src_filename, gbp_category, caption_uk, caption_ru, suggested_branch)
    ('mtp-warehouse-exterior.webp',    'EXTERIOR',
     'Фасад складу MTP Group у Київській області',
     'Фасад склада MTP Group в Киевской области', 'MTPFUL1'),
    ('warehouse-mtp-boryspil.webp',    'EXTERIOR',
     'Склад у Щасливому (Бориспільський район)',
     'Склад в Счастливом (Бориспольский район)', 'MTPFUL1'),
    ('mtp-warehouse-interior.webp',    'INTERIOR',
     'Інтер\'єр складу: адресне зберігання товарів',
     'Интерьер склада: адресное хранение товаров', 'BOTH'),
    ('warehouse-mtp-storage.webp',     'INTERIOR',
     'Зона зберігання — стелажі та ячейки',
     'Зона хранения — стеллажи и ячейки', 'BOTH'),
    ('mtp-packing-process.webp',       'PROCESS',
     'Упаковка замовлень для відправки',
     'Упаковка заказов для отправки', 'BOTH'),
    ('warehouse-mtp-packing.webp',     'PROCESS',
     'Пакувальна зона MTP Group',
     'Упаковочная зона MTP Group', 'BOTH'),
    ('mtp-warehouse-team-work.webp',   'TEAM_AT_WORK',
     'Команда MTP Group за роботою',
     'Команда MTP Group за работой', 'BOTH'),
    ('warehouse-mtp-team.webp',        'TEAM_AT_WORK',
     'Склад MTP: співробітники комплектують замовлення',
     'Склад MTP: сотрудники комплектуют заказы', 'BOTH'),
    ('mtp-team-ukraine.webp',          'TEAM',
     'Команда MTP Group Fulfillment — 10 років на ринку України',
     'Команда MTP Group Fulfillment — 10 лет на рынке Украины', 'BOTH'),
    ('mtp-founder-nikolai-warehouse.webp', 'OWNER',
     'Микола, засновник MTP Group, на складі',
     'Николай, основатель MTP Group, на складе', 'MTPFUL1'),
    ('mtp-generator-backup.webp',      'ADDITIONAL',
     'Резервне живлення: 3 генератори — склад працює під час блекаутів',
     'Резервное питание: 3 генератора — склад работает при блэкаутах', 'BOTH'),
    ('mtp-starlink-warehouse.webp',    'ADDITIONAL',
     'Starlink забезпечує безперервний зв\'язок 24/7',
     'Starlink обеспечивает непрерывную связь 24/7', 'BOTH'),
    ('mtp-fulfillment-warehouse-hero.webp', 'COVER',
     'MTP Group — фулфілмент для інтернет-магазинів України',
     'MTP Group — фулфилмент для интернет-магазинов Украины', 'BOTH'),
]


def convert(src_path: Path, dst_path: Path):
    img = Image.open(src_path)
    # Convert to RGB (drop alpha if present)
    if img.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', img.size, (255, 255, 255))
        bg.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        img = bg
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    # Strip metadata: don't call exif_transpose if no exif
    img = ImageOps.exif_transpose(img)
    # Resize max 2000px
    w, h = img.size
    m = max(w, h)
    if m > 2000:
        scale = 2000 / m
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    img.save(dst_path, 'JPEG', quality=90, optimize=True)
    return dst_path.stat().st_size, img.size


def main():
    queue = []
    skipped = []
    for src_name, cat, cap_uk, cap_ru, branch in PHOTOS:
        src = SRC / src_name
        if not src.exists():
            skipped.append(src_name)
            continue
        dst_name = src_name.replace('.webp', '.jpg').replace('.png', '.jpg')
        dst = DST / dst_name
        size, dims = convert(src, dst)
        queue.append({
            'file': f'public/images/gbp/{dst_name}',
            'source': f'public/images/{src_name}',
            'category': cat,
            'caption_uk': cap_uk,
            'caption_ru': cap_ru,
            'branch': branch,
            'size_bytes': size,
            'dimensions': f'{dims[0]}x{dims[1]}',
            'uploaded_mtpful1': False,
            'uploaded_mtpful2': False,
        })
    (DST / 'photo-queue.json').write_text(
        json.dumps({'photos': queue, 'skipped': skipped}, ensure_ascii=False, indent=2),
        encoding='utf-8')
    print(f'Converted: {len(queue)} files -> {DST}')
    print(f'Skipped: {skipped}')
    for q in queue:
        print(f'  {q["file"]} ({q["dimensions"]}, {q["size_bytes"]//1024}KB) [{q["category"]}] {q["branch"]}')


if __name__ == '__main__':
    main()

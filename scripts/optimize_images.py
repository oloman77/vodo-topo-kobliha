#!/usr/bin/env python3
"""Download approved third-party site imagery and replace it with local WebP.
No HTML is changed unless all images have downloaded and decoded successfully.
"""
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import re
import time

import requests
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets" / "optimized"
HTML = ROOT / "index.html"
HEADERS = ROOT / "_headers"
URLS = {
    "alfa": "https://cdn.prod.website-files.com/64d4cc36c686fbd7ff7b07e4/6509aadb1c72d6a2050db1b3_aaalfa.webp",
    "soho": "https://www.cresco.sk/uploads/tx_gallery/M12_8899.JPG",
    "dubicny": "https://i.ci.cz/developerske_projekty/1036/604239a0b6ee9c.jpg",
    "lihovar": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Lihovar_Sm%C3%ADchov_%2810%29.jpg?width=650",
    "lihovar-small": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Lihovar_Sm%C3%ADchov_%2810%29.jpg?width=480",
    "toptower": "https://commons.wikimedia.org/wiki/Special:Redirect/file/TOPTOWER_1.jpg?width=480",
    "footer": "https://images.unsplash.com/photo-1504917595217-d4dc5ebe6122?auto=format&fit=crop&w=1400&q=80",
}
SIZES = {
    "alfa": (400, 800), "soho": (400, 800), "dubicny": (400, 800),
    "lihovar": (400, 800), "toptower": (400,), "footer": (1400,)
}
RESPONSIVE = "(max-width: 520px) calc(100vw - 36px), (max-width: 880px) 50vw, 280px"


def download(session, key, url):
    variants = [url]
    if "commons.wikimedia.org/wiki/Special:Redirect/file/" in url:
        variants.append(url.replace("Special:Redirect/file/", "Special:FilePath/"))
    errors = []
    for variant in variants:
        for attempt in range(3):
            try:
                with session.get(variant, timeout=(15, 45), stream=True) as resp:
                    resp.raise_for_status()
                    data = bytearray()
                    for block in resp.iter_content(65536):
                        data.extend(block)
                        if len(data) > 20_000_000:
                            raise ValueError("Image source exceeds 20 MB")
                with Image.open(BytesIO(data)) as probe:
                    probe.verify()
                img = Image.open(BytesIO(data))
                img.load()
                img = ImageOps.exif_transpose(img)
                print(f"SOURCE {key} {img.width}x{img.height}: {len(data)} bytes", flush=True)
                return img
            except (requests.RequestException, OSError, ValueError) as exc:
                errors.append(f"{type(exc).__name__}: {str(exc)[:120]}")
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Cannot retrieve {key}: {errors[-4:]}")


def variant(key, img, maximum):
    width = min(maximum, img.width)
    height = round(img.height * width / img.width)
    resized = img.resize((width, height), Image.Resampling.LANCZOS) if width < img.width else img.copy()
    if resized.mode not in ("RGB", "RGBA"):
        resized = resized.convert("RGBA" if "A" in resized.getbands() else "RGB")
    stream = BytesIO()
    resized.save(stream, "WEBP", quality=79, method=6)
    data = stream.getvalue()
    name = f"{key}-{width}-{sha256(data).hexdigest()[:10]}.webp"
    (OUTPUT / name).write_bytes(data)
    print(f"LOCAL {name}: {len(data)} bytes", flush=True)
    return ("/assets/optimized/" + name, width)


def main():
    html = HTML.read_text(encoding="utf-8")
    if 'src="/assets/optimized/' in html:
        print("Images already migrated. No changes required.")
        return
    for k in ("alfa", "soho", "dubicny", "lihovar", "lihovar-small", "toptower"):
        if f'src="{URLS[k]}"' not in html:
            raise AssertionError(f"Unexpected index.html: missing remote image {k}")
    if f"url('{URLS['footer']}')" not in html:
        raise AssertionError("Unexpected footer background")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "VodoTopoKoblihaWebsite/1.0 (https://vodotopokobliha.cz/; company media localization)", "Accept": "image/webp,image/*,*/*;q=0.7"})
    local = {}
    for key in SIZES:
        source_image = download(session, key, URLS[key])
        local[key] = [variant(key, source_image, size) for size in SIZES[key]]
    updated = html
    for key in ("alfa", "soho", "dubicny", "lihovar"):
        target = local[key][-1][0]
        variants = ", ".join(f"{file} {width}w" for file, width in local[key])
        updated = updated.replace(f'src="{URLS[key]}"', f'src="{target}" srcset="{variants}" sizes="{RESPONSIVE}"')
    updated = updated.replace(f'src="{URLS["lihovar-small"]}"', f'src="{local["lihovar"][0][0]}"')
    updated = updated.replace(f'src="{URLS["toptower"]}"', f'src="{local["toptower"][0][0]}"')
    updated = updated.replace(f"url('{URLS['footer']}')", f"url('{local['footer'][0][0]}')")
    if updated == html or 'src="https://' in updated or "url('https://images.unsplash.com" in updated:
        raise AssertionError("External image reference remains; do not deploy")
    if len(re.findall(r"<img\b", html)) != len(re.findall(r"<img\b", updated)):
        raise AssertionError("Image tag count changed; do not deploy")
    HTML.write_text(updated, encoding="utf-8")
    rules = HEADERS.read_text(encoding="utf-8")
    if "/assets/optimized/*" not in rules:
        HEADERS.write_text(rules.rstrip() + "\n\n/assets/optimized/*\n  Cache-Control: public, max-age=31536000, immutable\n", encoding="utf-8")
    print("SUCCESS: all six reference cards and footer background now local; attribution links unchanged.", flush=True)


if __name__ == "__main__":
    main()

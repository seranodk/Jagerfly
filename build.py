#!/usr/bin/env python3
"""Builds the artifact page and the GitHub Pages bundle from src/game.html."""
import json, os, re
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ROOT, 'src/game.html'), encoding='utf-8').read()
VERSION = re.search(r"VERSION='(v[0-9.]+)'", src).group(1)  # single source: the game's VERSION constant
NAME = 'Jagerfly'
SLUG = 'jagerfly'

# --- artifact version: page body only (the artifact host adds the skeleton)
os.makedirs(os.path.join(ROOT, 'artifact'), exist_ok=True)
open(os.path.join(ROOT, f'artifact/{SLUG}.html'), 'w', encoding='utf-8').write(src)
open(os.path.join(ROOT, f'artifact/{SLUG}-{VERSION}.html'), 'w', encoding='utf-8').write(src)

# --- GitHub Pages version
head = f'''<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#0c1520">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{NAME}">
<meta name="description" content="{NAME} – flyv et F-35 og skyd med maskingevær eller missiler. Til mobil og browser ({VERSION})">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>:root{{padding:0}}body{{margin:0}}[hidden]{{display:none!important}}</style>
'''
body = src.replace(f'<title>{NAME}</title>', f'<title>{NAME} {VERSION}</title>', 1)
i = body.index('</style>') + len('</style>')
page = head + body[:i] + '\n</head>\n<body>\n' + body[i:] + '\n</body>\n</html>\n'
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
os.makedirs(os.path.join(ROOT, 'versions'), exist_ok=True)
open(os.path.join(ROOT, 'versions', f'{SLUG}-{VERSION}.html'), 'w', encoding='utf-8').write(page)

manifest = {
    "name": NAME, "short_name": NAME, "description": "F-35 skydespil til mobil og browser",
    "start_url": "./", "scope": "./", "display": "fullscreen", "orientation": "portrait",
    "background_color": "#0c1520", "theme_color": "#0c1520", "lang": "da",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}
json.dump(manifest, open(os.path.join(ROOT, 'manifest.webmanifest'), 'w'), indent=2)
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')

def icon(n):
    s = 4 * n
    im = Image.new('RGB', (s, s), '#1f6a96')
    d = ImageDraw.Draw(im)
    for k in range(7):
        y = s * (.1 + k * .14)
        d.arc([s * (.1 + (k % 2) * .4), y, s * (.3 + (k % 2) * .4), y + s * .06], 200, 340, fill='#7fb6d4', width=max(2, s // 120))
    u = s / 56  # jet drawn in a 56-unit box
    pts = [(0, -24), (2.6, -17), (4.6, -9), (6, -4), (21, 7), (21, 11), (8, 10), (8, 13), (15, 19), (15, 22), (4.5, 21),
           (3.5, 22), (-3.5, 22), (-4.5, 21), (-15, 22), (-15, 19), (-8, 13), (-8, 10), (-21, 11), (-21, 7), (-6, -4),
           (-4.6, -9), (-2.6, -17)]
    cx, cy = s / 2, s / 2
    d.polygon([(cx + x * u + 4 * u, cy + y * u + 5 * u) for x, y in pts], fill='#15496a')
    d.polygon([(cx + 4 * u * 0, cy + 23 * u), (cx - 3 * u, cy + 21 * u), (cx + 3 * u, cy + 21 * u)], fill='#ffb02e')
    d.polygon([(cx - 3.5 * u, cy + 21 * u), (cx, cy + 31 * u), (cx + 3.5 * u, cy + 21 * u)], fill='#ffb02e')
    d.polygon([(cx + x * u, cy + y * u) for x, y in pts], fill='#9aa6b1', outline='#3f4952')
    d.ellipse([cx - 2.8 * u, cy - 17 * u, cx + 2.8 * u, cy - 5 * u], fill='#d8ad4c')
    return im.resize((n, n), Image.LANCZOS)

icon(192).save(os.path.join(ROOT, 'icon-192.png'))
icon(512).save(os.path.join(ROOT, 'icon-512.png'))
icon(180).save(os.path.join(ROOT, 'apple-touch-icon.png'))
print('built', VERSION)

"""Contact sheets: original swatch vs. repeated tile (for checking extraction)."""
import json, sys, io, cairosvg, re
from PIL import Image, ImageDraw
def png(path, scale):
    return Image.open(io.BytesIO(cairosvg.svg2png(url=path, scale=scale, background_color="white"))).convert("RGB")
kind, root, out = sys.argv[1], sys.argv[2], sys.argv[3]
sel = sys.argv[4].split(",") if len(sys.argv) > 4 and sys.argv[4] else None
items = json.load(open(f"{root}/{'lines.json' if kind=='line' else 'ornaments.json'}"))
key = "id" if kind == "line" else "ref"
items = [i for i in items if not sel or any(s.lower() in i[key].lower() for s in sel)]
rows = []
for it in items:
    sw = png(f"{root}/swatch/{it[key]}.svg", 2.5)
    tl = png(f"{root}/tile/{it[key]}.svg", 2.5)
    if kind == "line":
        n = max(2, int(400 / max(tl.width, 1)) + 1)
        rep = Image.new("RGB", (tl.width * n, tl.height), "white")
        for k in range(n): rep.paste(tl, (k * tl.width, 0))
        rep = rep.crop((0, 0, min(rep.width, 520), rep.height))
        H = max(sw.height, rep.height) + 14
        row = Image.new("RGB", (sw.width + 540 + 10, H), "white")
        row.paste(sw, (0, 14)); row.paste(rep, (sw.width + 20, 14 + (sw.height - rep.height) // 2))
        ImageDraw.Draw(row).text((2, 1), f"{it['description'][:70]}  [{it.get('repeat_method')} p={it['period_pt']}]", fill="red")
        ImageDraw.Draw(row).line([(sw.width + 20 + k * tl.width, 14) for k in (1,)] + [(sw.width + 20 + tl.width, H)], fill=(255,150,150))
    else:
        W = 300; rep = Image.new("RGB", (W, W), "white")
        for x in range(0, W, max(tl.width,1)):
            for y in range(0, W, max(tl.height,1)): rep.paste(tl, (x, y))
        row = Image.new("RGB", (sw.width + W + 30, max(sw.height, W) + 14), "white")
        row.paste(sw, (0, 14)); row.paste(rep, (sw.width + 20, 14))
        ImageDraw.Draw(row).text((2, 1), f"{it['ref']} {it['description'][:40]} seamless={it['seamless']}", fill="red")
    rows.append(row)
cols = int(sys.argv[5]) if len(sys.argv) > 5 else 1
import math
per = math.ceil(len(rows) / cols)
colimgs = []
for c in range(cols):
    rs = rows[c*per:(c+1)*per]
    if not rs: continue
    im = Image.new("RGB", (max(r.width for r in rs), sum(r.height + 4 for r in rs)), (235,235,235)); y = 0
    for r in rs: im.paste(r, (0, y)); y += r.height + 4
    colimgs.append(im)
sheet = Image.new("RGB", (sum(i.width + 8 for i in colimgs), max(i.height for i in colimgs)), (200,200,200)); x = 0
for i in colimgs: sheet.paste(i, (x, 0)); x += i.width + 8
sheet.save(out); print(sheet.size)

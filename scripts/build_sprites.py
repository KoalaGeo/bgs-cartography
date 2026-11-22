"""Rasterise symbols, ornament tiles and line tiles into MapLibre sprite sheets (1x and 2x)."""
import json, sys, io, re, csv, cairosvg
from PIL import Image
root = sys.argv[1]
PX_PER_PT = 96 / 72
SYM_SCALE = 16 / (3 / 25.4 * 96)   # Alluvium body (3 mm in the SVG) -> 16 px at 1x

def render(svg, w, h):
    svg = re.sub(r'<svg ([^>]*?)width="[^"]+" height="[^"]+"',
                 lambda m: f'<svg {m.group(1)}width="{w}" height="{h}" preserveAspectRatio="none"', svg, count=1)
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert("RGBA")

def pack(images, maxw):
    items = sorted(images.items(), key=lambda kv: (-kv[1].height, kv[0]))
    x = y = rowh = 0; pos = {}
    for name, im in items:
        if x + im.width > maxw: x = 0; y += rowh + 2; rowh = 0
        pos[name] = (x, y); x += im.width + 2; rowh = max(rowh, im.height)
    return pos, y + rowh

syms = json.load(open(f"{root}/Symbols/symbols.json"))
orns = json.load(open(f"{root}/Area-Ornaments/ornaments.json"))
lines = json.load(open(f"{root}/Line-Styles/lines.json"))
for ratio in (1, 2):
    imgs = {}
    for s in syms:
        w = max(1, round(s["width_mm"] / 25.4 * 96 * SYM_SCALE * ratio)); h = max(1, round(s["height_mm"] / 25.4 * 96 * SYM_SCALE * ratio))
        imgs["sym-" + s["ref"]] = render(open(f"{root}/Symbols/svg/{s['ref']}.svg").read(), w, h)
        if ratio == 1: s["sprite_px"] = [w, h]
    for o in orns:
        w = max(2, round(o["tile_pt"][0] * PX_PER_PT)) * ratio; h = max(2, round(o["tile_pt"][1] * PX_PER_PT)) * ratio
        imgs["orn-" + o["ref"]] = render(open(f"{root}/Area-Ornaments/tile/{o['ref']}.svg").read(), w, h)
        if ratio == 1: o["sprite_px"] = [w, h]
    for l in lines:
        w = max(2, round(l["tile_pt"][0] * PX_PER_PT)) * ratio; h = max(2, round(l["tile_pt"][1] * PX_PER_PT))
        h = (h + (h % 2)) * ratio  # even height keeps the centre line on the geometry
        imgs["line-" + l["id"]] = render(open(f"{root}/Line-Styles/tile/{l['id']}.svg").read(), w, h)
        if ratio == 1: l["sprite_px"] = [w, h]
    pos, H = pack(imgs, 1024 * ratio)
    sheet = Image.new("RGBA", (1024 * ratio, H), (0, 0, 0, 0))
    index = {}
    for name, im in imgs.items():
        x, y = pos[name]; sheet.alpha_composite(im, (x, y))
        index[name] = dict(x=x, y=y, width=im.width, height=im.height, pixelRatio=ratio)
    suf = "" if ratio == 1 else "@2x"
    sheet.save(f"{root}/Sprites/bgs-symbology{suf}.png", optimize=True)
    json.dump(dict(sorted(index.items())), open(f"{root}/Sprites/bgs-symbology{suf}.json", "w"), indent=0)
    print(ratio, sheet.size, len(index))
# 4x PNG line tiles (QGIS "raster line" symbol layer takes raster images, not SVG)
import os
os.makedirs(f"{root}/Line-Styles/png", exist_ok=True)
for l in lines:
    w, h = l["sprite_px"]
    render(open(f"{root}/Line-Styles/tile/{l['id']}.svg").read(), w * 4, h * 4).save(f"{root}/Line-Styles/png/{l['id']}.png", optimize=True)
json.dump(syms, open(f"{root}/Symbols/symbols.json", "w"), indent=1, ensure_ascii=False)
json.dump(orns, open(f"{root}/Area-Ornaments/ornaments.json", "w"), indent=1)
json.dump(lines, open(f"{root}/Line-Styles/lines.json", "w"), indent=1)
# CSVs for ornaments and lines
with open(f"{root}/Area-Ornaments/ornaments.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ref", "description", "colours", "seamless", "tile_method", "tile_width_pt", "tile_height_pt", "swatch_svg", "tile_svg", "sprite_name"])
    for o in orns: w.writerow([o["ref"], o["description"], " ".join(o["colours"]), o["seamless"], o["tile_method"], *o["tile_pt"], f"swatch/{o['ref']}.svg", f"tile/{o['ref']}.svg", "orn-" + o["ref"]])
with open(f"{root}/Line-Styles/lines.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "description", "colours", "seamless", "repeat_method", "tile_width_pt", "tile_height_pt", "swatch_svg", "tile_svg", "sprite_name", "maplibre_line_width_px"])
    for l in lines: w.writerow([l["id"], l["description"], " ".join(l["colours"]), l["seamless"], l["repeat_method"], *l["tile_pt"], f"swatch/{l['id']}.svg", f"tile/{l['id']}.svg", "line-" + l["id"], l["sprite_px"][1]])

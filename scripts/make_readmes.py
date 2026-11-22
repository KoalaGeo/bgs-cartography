"""Write the per-folder README catalogues (image tables) from the JSON catalogues."""
import json, sys, html
from collections import OrderedDict
root = sys.argv[1]
e = lambda s: html.escape(str(s or ""), quote=False).replace("|", "\\|")

# ---------------------------------------------------------------- Symbols
syms = json.load(open(f"{root}/Symbols/symbols.json"))
groups = OrderedDict()
for s in syms:
    groups.setdefault((s["group"], s["classification"]), OrderedDict()).setdefault(s["subclassification"] or "", []).append(s)
out = ["# Symbols", "",
       f"{len(syms)} point symbols from section 2 of BGS Research Report RR/01/01 (*Cartographic standard geological symbol index*, version 3, 2002), "
       "grouped by the report's geological classification.", "",
       "Each symbol was extracted as vector outlines directly from the font glyphs embedded in the PDF, so the shapes are exact rather than traced.", "",
       "## Files", "",
       "| Path | Contents |", "|---|---|",
       "| `svg/{REF}.svg` | Symbol at **BGS standard size**: the Alluvium symbol body is 3 mm (1:25 000 and smaller scales). Scale by 4/3 for 1:10 000 (4 mm). |",
       "| `svg-24px/`, `svg-48px/` | Square icons, symbol fitted and centred (like the OS GeoDataViz icons). Not to a common scale. |",
       "| `symbols.csv`, `symbols.json` | Catalogue: reference name, description, alternative descriptions from the A–Z index (2.2), classification, size, source page/glyph. |",
       "| [`../Sprites/`](../Sprites) | MapLibre/Mapbox sprite: image name `sym-{REF}`. |", "",
       "Reference names (`REF`) are the MicroStation cell names used in the report, e.g. `ALV` for Alluvium. "
       "Prefixes: ALV alluvial, BRK brickearth, GFL glaciofluvial, GLA glaciolacustrine, GL glacial, IGL interglacial, LAC lacustrine, "
       "MA marine, RM raised marine, RS rock, RT river terrace, S structural, SG sand and gravel.", "",
       "Symbols are black. Structural symbols are normally rotated to strike; in MapLibre use `icon-rotate` with `icon-rotation-alignment: map`.", "",
       "## Source inconsistencies", ""] + [f"- `{s['ref']}` ({e(s['description'])}): {e(s['notes'])}" for s in syms if s.get("notes")] + ["",
       "## Contents", ""]
for (g, c) in groups: out.append(f"- [{c}](#{c.lower().replace(' ', '-').replace('/', '')})")
out.append("")
for (g, c), subs in groups.items():
    out += [f"## {c}", ""]
    for sub, items in subs.items():
        if sub: out += [f"### {sub}", ""]
        out += ["| Symbol | Reference | Description | Also indexed as |", "|:---:|---|---|---|"]
        for s in items:
            out.append(f"| <img src=\"svg/{s['ref']}.svg\" height=\"{max(14, round(s['height_mm'] * 6))}\" alt=\"{e(s['ref'])}\"> | `{s['ref']}` | {e(s['description'])} | {e('; '.join(s['alt_descriptions']))} |")
        out.append("")
open(f"{root}/Symbols/README.md", "w").write("\n".join(out))

# ---------------------------------------------------------------- Area ornaments
orns = json.load(open(f"{root}/Area-Ornaments/ornaments.json"))
n_exact = sum(1 for o in orns if o["tile_method"].startswith("exact"))
n_wrap = sum(1 for o in orns if o["tile_method"].startswith("wrapped"))
n_crop = len(orns) - n_exact - n_wrap
out = ["# Area ornaments", "",
       f"{len(orns)} area ornaments (fill patterns) from section 3 of BGS RR/01/01, extracted as vector SVG from the PDF drawing operators.", "",
       "## Files", "",
       "| Path | Contents |", "|---|---|",
       "| `swatch/{REF}.svg` | The swatch exactly as printed in the report. |",
       "| `tile/{REF}.svg` | A repeat tile for use as a fill pattern (transparent background, so a colour fill can sit underneath). |",
       "| `ornaments.csv`, `ornaments.json` | Catalogue: reference name, description, colours, tile size and how the tile was made. |",
       "| [`../Sprites/`](../Sprites) | MapLibre sprite: image name `orn-{REF}`, use with `fill-pattern`. |", "",
       "## How the repeat tiles were made", "",
       f"- **Exact repeat ({n_exact})**: the repeat period was measured from the swatch by autocorrelation, and the tile is one period cropped from the vector artwork. These tile seamlessly.",
       f"- **Wrapped marks ({n_wrap})**: the hand-placed, irregular patterns (sand, igneous, lava, breccia and so on) have no repeat. Each mark whose centre falls inside the tile is kept whole and copied across the opposite edge, so the tile is seamless but the marks near its edges are re-arranged relative to the printed swatch.",
       f"- **Cropped swatch ({n_crop})**: dense irregular tessellations (coursed rubble, random rubble, marble), where wrapping would make stones overlap. These show a faint seam every tile width.", "",
       "Black in the PDF is a rich black (`#231f20`); it has been output as pure black. *Marine overprint (white)* is printed black in the report and is reproduced as printed. Colour it white yourself if needed.", "",
       "## Catalogue", "",
       "| Swatch | Tile | Reference | Description | Tile |", "|:---:|:---:|---|---|---|"]
for o in orns:
    m = o["tile_method"].split(" (")[0]
    out.append(f"| <img src=\"swatch/{o['ref']}.svg\" height=\"72\" alt=\"{e(o['ref'])} swatch\"> | <img src=\"tile/{o['ref']}.svg\" height=\"40\" alt=\"{e(o['ref'])} tile\"> | `{o['ref']}` | {e(o['description'])} | {m} |")
open(f"{root}/Area-Ornaments/README.md", "w").write("\n".join(out) + "\n")

# ---------------------------------------------------------------- Line styles
lines = json.load(open(f"{root}/Line-Styles/lines.json"))
nf = sum(1 for l in lines if l["repeat_method"] == "full swatch")
out = ["# Line styles", "",
       f"{len(lines)} line styles from section 4 of BGS RR/01/01, extracted as vector SVG.", "",
       "The report gives line styles a description but **no reference name**, so the `id` here is a slug of the description (e.g. `fault_thrust_observed`). It is not an official BGS code.", "",
       "## Files", "",
       "| Path | Contents |", "|---|---|",
       "| `swatch/{id}.svg` | The swatch exactly as printed. |",
       "| `tile/{id}.svg` | One repeat of the style, vertically centred on the line, for use as a line pattern. |",
       "| `lines.csv`, `lines.json` | Catalogue: id, description, colours, tile size, repeat method, MapLibre `line-width`. |",
       "| [`../Sprites/`](../Sprites) | MapLibre sprite: image name `line-{id}`, use with `line-pattern`. |", "",
       "## Using the tiles in MapLibre", "",
       "MapLibre stretches a `line-pattern` image so its height equals `line-width`. To draw a style at its printed size, set `line-width` to the tile height in pixels (the `maplibre_line_width_px` column in `lines.csv`). Scale both with zoom if needed.", "",
       "## How the repeat was found", "",
       "- **autocorrelation**: the period of the whole style, measured from the swatch.",
       "- **decoration spacing**: for the major fold axial traces (symbol, dashes, symbol), the period is the spacing between the symbols.",
       f"- **full swatch ({nf})**: the style carries a one-off decoration (a label such as `RF`, `Pb`, `al`, a single downthrow tick, strike-slip arrows, or end markers). The whole printed swatch is used as one repeat, so the decoration recurs about every 130 pt (about 46 mm). "
       "The glacial meltwater channel centre line has an arrow at one end and a dot at the other; on a real map it is better drawn as a plain line with end markers.", "",
       "## Catalogue", "",
       "| Swatch | Description | id | Repeat |", "|:---:|---|---|---|"]
for l in lines:
    out.append(f"| <img src=\"swatch/{l['id']}.svg\" width=\"200\" alt=\"\"> | {e(l['description'])} | `{l['id']}` | {l['repeat_method']} |")
open(f"{root}/Line-Styles/README.md", "w").write("\n".join(out) + "\n")
print("READMEs written")

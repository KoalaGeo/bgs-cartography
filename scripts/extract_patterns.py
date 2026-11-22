"""Extract area ornaments (section 3) and line styles (section 4) from RR/01/01 as SVG swatches + repeat tiles."""
import pymupdf, sys, os, re, json, io, html
import numpy as np, cairosvg
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from vector import Fonts, region_svg_elems, is_grid, f2

pdf, outdir = sys.argv[1], sys.argv[2]
doc = pymupdf.open(pdf); fonts = Fonts(doc)
S = 10  # raster px per pt for analysis

def grid(page):
    xs, ys = [], []
    for d in page.get_drawings():
        if not is_grid(d.get("color")): continue
        for it in d["items"]:
            if it[0] == "l":
                p, q = it[1], it[2]
                if abs(p.x - q.x) < .5 and abs(p.y - q.y) > 20: xs.append(p.x)
                if abs(p.y - q.y) < .5 and abs(p.x - q.x) > 20: ys.append(p.y)
            elif it[0] == "re":
                r = it[1]; xs += [r.x0, r.x1]; ys += [r.y0, r.y1]
    def merge(v):
        v = sorted(v); out = []
        for a in v:
            if not out or a - out[-1][-1] > 1.5: out.append([a])
            else: out[-1].append(a)
        return [sum(g) / len(g) for g in out]
    return merge(xs), merge(ys)

def svg_doc(elems, w, h, vb=None, title=None, extra=""):
    vb = vb or (0, 0, w, h)
    t = f"  <title>{html.escape(title)}</title>\n" if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f2(w)}pt" height="{f2(h)}pt" viewBox="{" ".join(f2(v) for v in vb)}">\n{t}{extra}'
            + "\n".join("  " + e for e in elems) + "\n</svg>\n")

def raster(svg, scale=S):
    png = cairosvg.svg2png(bytestring=svg.encode(), scale=scale * 72 / 96, background_color="white")
    a = np.asarray(Image.open(io.BytesIO(png)).convert("L"), dtype=np.float32) / 255
    return a < 0.92

def mismatch(A, s, axis):
    if axis == 1: a, b = A[:, :-s], A[:, s:]
    else: a, b = A[:-s, :], A[s:, :]
    u = np.logical_or(a, b).sum()
    return np.logical_xor(a, b).sum() / u if u else 1.0

def informative(A, axis):
    """Drop rows (axis=1 search) / columns (axis=0 search) that are constant, e.g. solid rules."""
    cov = A.mean(axis=axis)
    keep = (cov > 0.002) & (cov < 0.97)
    if keep.sum() < 2: return A
    return A[keep, :] if axis == 1 else A[:, keep]

def best_period(A, axis, smin, smax, frac=0.6):
    A = informative(A, axis)
    n = A.shape[axis]
    smax = min(smax, int(n * frac))
    if smax <= smin: return None, 1.0
    ms = np.array([mismatch(A, s, axis) for s in range(smin, smax)])
    gmin = ms.min()
    if gmin > 0.2: return None, float(gmin)
    # smallest local minimum close to the global minimum = fundamental period
    for i in range(1, len(ms) - 1):
        if ms[i] <= ms[i-1] and ms[i] <= ms[i+1] and ms[i] <= gmin + 0.04:
            # sub-pixel refinement (parabola)
            y0, y1, y2 = ms[i-1], ms[i], ms[i+1]; den = y0 - 2*y1 + y2
            off = 0.5 * (y0 - y2) / den if den > 1e-9 else 0
            return (smin + i + off) / S, float(y1)
    return None, float(gmin)

def slug(t):
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", t.lower())).strip("_")

def text_in(page, rect):
    desc, refs = [], []
    for b in page.get_text("dict", clip=rect)["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                t = s["text"].strip()
                if not t or s["size"] < 7.5: continue
                (refs if "Helvetica" in s["font"] else desc).append(t)
    return re.sub(r"\s+", " ", " ".join(desc)).replace("- ", "-").strip(), " ".join(refs).strip()

# ---------------------------------------------------------------- area ornaments
orn = []
os.makedirs(f"{outdir}/Area-Ornaments/swatch", exist_ok=True); os.makedirs(f"{outdir}/Area-Ornaments/tile", exist_ok=True)
for pno in range(len(doc)):
    pg = doc[pno]; txt = pg.get_text()
    if "3  AREA ORNAMENTS" not in txt or "LISTED BY DESCRIPTION" not in txt: continue
    xs, ys = grid(pg); drawings = pg.get_drawings(); tt = pg.get_texttrace()
    cols = [xs[i:i+3] for i in range(0, len(xs) - 2, 3)]
    for c in cols:
        for r0, r1 in zip(ys[:-1], ys[1:]):
            desc, ref = text_in(pg, pymupdf.Rect(c[1], r0, c[2], r1))
            if not ref: continue
            sw = pymupdf.Rect(c[0] + 0.6, r0 + 0.6, c[1] - 0.6, r1 - 0.6)
            elems, cols_used = region_svg_elems(pg, fonts, sw, sw.x0, sw.y0, drawings, tt)
            clip = f'  <defs><clipPath id="c"><rect width="{f2(sw.width)}" height="{f2(sw.height)}"/></clipPath></defs>\n'
            full = svg_doc([f'<g clip-path="url(#c)">'] + elems + ["</g>"], sw.width, sw.height, title=f"{desc} ({ref})", extra=clip)
            open(f"{outdir}/Area-Ornaments/swatch/{ref}.svg", "w").write(full)
            A = raster(full)
            ink = np.argwhere(A)
            if len(ink) == 0: print("EMPTY", ref); continue
            (y0, x0), (y1, x1) = ink.min(0), ink.max(0)
            core = A[y0 + 2*S: y1 - 2*S, x0 + 2*S: x1 - 2*S]
            px, mx = best_period(core, 1, int(1.5*S), core.shape[1])
            py, my = best_period(core, 0, int(1.5*S), core.shape[0])
            # vertical-only stripes (no x structure) or horizontal-only
            colx = core.any(0).mean(); rowy = core.any(1).mean()
            if px is None and colx > 0.97 and mismatch(core, S, 1) < 0.05: px, mx = 1.0, 0.0
            if py is None and rowy > 0.97 and mismatch(core, S, 0) < 0.05: py, my = 1.0, 0.0
            seamless = px is not None and py is not None
            ink_box = (x0 / S, y0 / S, x1 / S, y1 / S)
            if seamless:
                # widen trivial (no-structure) axes to a sensible tile size
                if px == 1.0: px = 8.0
                if py == 1.0: py = 8.0
                px *= max(1, int(np.ceil(6.0 / px))); py *= max(1, int(np.ceil(6.0 / py)))
                cx = (ink_box[0] + ink_box[2]) / 2; cy = (ink_box[1] + ink_box[3]) / 2
                tb = (cx - px / 2, cy - py / 2, px, py)
            else:
                m = 1.5  # crop inside the drawn area, away from the swatch edge
                tb = (ink_box[0] + m, ink_box[1] + m, ink_box[2] - ink_box[0] - 2*m, ink_box[3] - ink_box[1] - 2*m)
            tile = svg_doc(elems, tb[2], tb[3], vb=tb, title=f"{desc} ({ref}) - repeat tile")
            open(f"{outdir}/Area-Ornaments/tile/{ref}.svg", "w").write(tile)
            orn.append(dict(ref=ref, description=desc, colours=sorted(cols_used), seamless=seamless,
                            tile_pt=[round(tb[2], 3), round(tb[3], 3)], period_pt=[px and round(px, 3), py and round(py, 3)],
                            mismatch=[round(mx, 3), round(my, 3)], swatch_pt=[round(sw.width, 2), round(sw.height, 2)],
                            source=dict(document="BGS RR/01/01 v3", pdf_page=pno + 1)))
            print(f"ORN {ref:10s} {desc[:38]:38s} seamless={seamless!s:5s} p=({px},{py}) m=({mx:.3f},{my:.3f}) cols={sorted(cols_used)}")
json.dump(orn, open(f"{outdir}/Area-Ornaments/ornaments.json", "w"), indent=1)

# ---------------------------------------------------------------- line styles
# Four descriptions carry a small inline symbol (drawn as a vector, a symbol-font glyph or tiny
# mirrored text) that the text filter above drops. Restore the printed wording; ids stay the slug
# of the text without the symbol.
DESC_PRINTED = {
    "limit_of_granite_pegmatite_vein_complex_within_area_of_veining":
        "Limit of granite / pegmatite vein complex, x \u03c0 within area of veining",
    "limit_of_migmatisation_towards_migmatites": "Limit of migmatisation, \u2227 towards migmatites",
    "limit_of_transgressive_pegmatite_veins_within_areas_of_veins":
        "Limit of transgressive pegmatite veins, \u03c0 within areas of veins",
    "metamorphic_aureole_towards_intrusion": "Metamorphic aureole, + towards intrusion",
}
lines = []
os.makedirs(f"{outdir}/Line-Styles/swatch", exist_ok=True); os.makedirs(f"{outdir}/Line-Styles/tile", exist_ok=True)
for pno in range(len(doc)):
    pg = doc[pno]; txt = pg.get_text()
    if "4  LINE STYLES" not in txt or "LISTED BY DESCRIPTION" not in txt: continue
    xs, ys = grid(pg); drawings = pg.get_drawings(); tt = pg.get_texttrace()
    L, M, R = xs[0], xs[1], xs[-1]
    for r0, r1 in zip(ys[:-1], ys[1:]):
        desc, _ = text_in(pg, pymupdf.Rect(M, r0, R, r1))
        if not desc: continue
        sid = slug(desc)
        desc = DESC_PRINTED.get(sid, desc)
        sw = pymupdf.Rect(L + 0.6, r0 + 0.6, M - 0.6, r1 - 0.6)
        elems, cols_used = region_svg_elems(pg, fonts, sw, sw.x0, sw.y0, drawings, tt)
        full = svg_doc(elems, sw.width, sw.height, title=desc)
        A = raster(full)
        ink = np.argwhere(A)
        if len(ink) == 0: print("EMPTY", desc); continue
        (y0, x0), (y1, x1) = ink.min(0), ink.max(0)
        band = A[y0:y1 + 1, x0:x1 + 1]
        # centre line: the row(s) with most ink
        cov = band.mean(1)
        order = np.argsort(-cov)
        top = order[0]; cyp = top
        for j in order[1:]:
            if abs(j - top) > 1.0 * S and cov[j] > 0.85 * cov[top]:
                cyp = (top + j) / 2; break
            if cov[j] < 0.85 * cov[top]: break
        cy = (y0 + cyp) / S
        half = max(cy - y0 / S, y1 / S - cy) + 0.8
        trim = band[:, int(0.5*S): band.shape[1] - int(0.5*S)]  # avoid ragged ends
        px, mx = best_period(trim, 1, int(1.0 * S), trim.shape[1])
        solid = trim.any(0).mean() > 0.99 and mismatch(trim, S, 1) < 0.03
        if solid and (px is None or mx < 0.03): px, mx = 4.0, 0.0
        x_start = x0 / S + 0.5 + 2.0
        method = "autocorrelation"
        off = band.copy(); c0 = int(cyp - 0.9 * S); c1 = int(cyp + 0.9 * S) + 1
        off[max(0, c0):c1, :] = False
        if px is not None and off.any() and mismatch(informative(off, 1), int(round(px * S)), 1) > 0.25:
            px, mx = None, 1.0   # decorations do not repeat at the base period
        if px is None or mx > 0.1:
            # repeat of the off-axis decorations (symbols, ticks) only
            if off.any():
                q, mq = best_period(off, 1, int(4 * S), off.shape[1], frac=0.8)
                if q is not None and mq < 0.25:
                    cols = np.where(off.any(0))[0]
                    px, mx, method = q, mq, "decoration spacing"
                    x_start = (x0 + cols[0]) / S - 1.0
        seamless = px is not None and mx <= 0.25
        if not seamless:  # use the full drawn length as one repeat
            x_start, px, method = x0 / S, (x1 - x0) / S, "full swatch"
        elif px < 6: px *= int(np.ceil(6 / px))
        tb = (x_start, cy - half, px, 2 * half)
        open(f"{outdir}/Line-Styles/swatch/{sid}.svg", "w").write(full)
        open(f"{outdir}/Line-Styles/tile/{sid}.svg", "w").write(svg_doc(elems, tb[2], tb[3], vb=tb, title=f"{desc} - repeat tile"))
        lines.append(dict(id=sid, description=desc, colours=sorted(cols_used), seamless=seamless, solid=bool(solid), repeat_method=method,
                          tile_pt=[round(tb[2], 3), round(tb[3], 3)], period_pt=round(px, 3), mismatch=round(mx, 3),
                          source=dict(document="BGS RR/01/01 v3", pdf_page=pno + 1)))
        print(f"LIN {method[:6]} {desc[:50]:50s} seamless={seamless!s:5s} p={px:.2f} m={mx:.3f} h={2*half:.1f} cols={sorted(cols_used)}")
json.dump(lines, open(f"{outdir}/Line-Styles/lines.json", "w"), indent=1)
print(len(orn), "ornaments,", len(lines), "line styles")

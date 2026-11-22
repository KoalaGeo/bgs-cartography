"""PDF vector drawings + text glyphs -> compact SVG fragments (PyMuPDF + fontTools)."""
import pymupdf, io, math
from fontTools.cffLib import CFFFontSet
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

GRID = (0.482, 0.788, 0.647)  # green table rules in RR/01/01

def is_grid(c):
    return c is not None and all(abs(a - b) < 0.01 for a, b in zip(c, GRID))

def hexc(c):
    return "#%02x%02x%02x" % tuple(round(max(0, min(1, v)) * 255) for v in c[:3])

def snap_black(c):
    # The PDF uses a rich black (0.137,0.122,0.125); output pure black for map use
    return (0, 0, 0) if c and max(c) < 0.2 and max(c) - min(c) < 0.05 else c

class Fonts:
    def __init__(self, doc):
        self.doc, self.cache = doc, {}
        self.byname = {}
        for pno in range(len(doc)):
            for f in doc[pno].get_fonts(full=True):
                base = f[3].split('+')[-1]
                if f[1] == "cff" or f[2] in ("Type1C",) or base.startswith("TT") or "Helvetica" in base:
                    self.byname.setdefault(base, f[0])
    def glyph_d(self, font, gid):
        key = (font, gid)
        if key not in self.cache:
            xref = self.byname[font]
            buf = self.doc.extract_font(xref)[3]
            cff = CFFFontSet(); cff.decompile(io.BytesIO(buf), None)
            td = cff[cff.fontNames[0]]
            sp = SVGPathPen(None)
            td.CharStrings[td.charset[gid]].draw(TransformPen(sp, (1, 0, 0, -1, 0, 0)))
            self.cache[key] = (sp.getCommands(), td.FontMatrix[0])
        return self.cache[key]

def f2(v): return f"{v:.2f}".rstrip("0").rstrip(".")

def path_d(items, ox, oy, close):
    out, cur = [], None
    P = lambda p: f"{f2(p.x-ox)} {f2(p.y-oy)}"
    for it in items:
        op = it[0]
        if op == "l":
            p, q = it[1], it[2]
            if cur is None or abs(cur.x - p.x) + abs(cur.y - p.y) > 1e-3: out.append("M" + P(p))
            out.append("L" + P(q)); cur = q
        elif op == "c":
            p, c1, c2, q = it[1:5]
            if cur is None or abs(cur.x - p.x) + abs(cur.y - p.y) > 1e-3: out.append("M" + P(p))
            out.append("C" + P(c1) + " " + P(c2) + " " + P(q)); cur = q
        elif op == "re":
            r = it[1]
            out.append(f"M{f2(r.x0-ox)} {f2(r.y0-oy)}h{f2(r.width)}v{f2(r.height)}h{f2(-r.width)}Z"); cur = None
        elif op == "qu":
            q = it[1]
            out.append("M" + P(q.ul) + "L" + P(q.ur) + "L" + P(q.lr) + "L" + P(q.ll) + "Z"); cur = None
    if close: out.append("Z")
    return "".join(out)

def region_svg_elems(page, fonts, rect, ox, oy, drawings=None, texttrace=None):
    """SVG elements for everything drawn inside rect (minus grid rules and tiny invisible text)."""
    elems, colours = [], set()
    drawings = drawings if drawings is not None else page.get_drawings()
    for d in drawings:
        if is_grid(d.get("color")) or is_grid(d.get("fill")): continue
        if not d["rect"].intersects(rect) and not (d["rect"].width == 0 or d["rect"].height == 0) : continue
        if (d["rect"].width == 0 or d["rect"].height == 0) and not (rect.x0 - 1 <= d["rect"].x0 <= rect.x1 + 1 and rect.y0 - 1 <= d["rect"].y0 <= rect.y1 + 1): continue
        a = [f'd="{path_d(d["items"], ox, oy, d.get("closePath"))}"']
        t = d["type"]
        if "f" in t and d.get("fill") is not None:
            c = hexc(snap_black(d["fill"])); colours.add(c); a.append(f'fill="{c}"')
            if d.get("even_odd"): a.append('fill-rule="evenodd"')
            if (d.get("fill_opacity") or 1) < 1: a.append(f'fill-opacity="{d["fill_opacity"]:.2f}"')
        else:
            a.append('fill="none"')
        if "s" in t and d.get("color") is not None:
            c = hexc(snap_black(d["color"])); colours.add(c)
            a.append(f'stroke="{c}" stroke-width="{f2(d.get("width") or 1)}"')
            cap = {0: "butt", 1: "round", 2: "square"}.get((d.get("lineCap") or (0,))[0], "butt")
            if cap != "butt": a.append(f'stroke-linecap="{cap}"')
            j = {0: "miter", 1: "round", 2: "bevel"}.get(int(d.get("lineJoin") or 0), "miter")
            if j != "miter": a.append(f'stroke-linejoin="{j}"')
            dash = (d.get("dashes") or "[] 0").strip()
            if not dash.startswith("[]"):
                arr = dash[dash.index("[")+1:dash.index("]")].split(); ph = dash.split("]")[1].strip()
                a.append(f'stroke-dasharray="{" ".join(arr)}"');
                if ph not in ("0", ""): a.append(f'stroke-dashoffset="{ph}"')
        elems.append("<path " + " ".join(a) + "/>")
    for s in (texttrace if texttrace is not None else page.get_texttrace()):
        if s["size"] < 1: continue
        if abs(s["dir"][0] - 1) > 1e-3: raise ValueError("rotated text in swatch")
        c = hexc(snap_black(s["color"]))
        for ch in s["chars"]:
            x, y = ch[2]
            if not (rect.x0 - 1 <= x <= rect.x1 + 1 and rect.y0 - 1 <= y <= rect.y1 + 1): continue
            dd, fm = fonts.glyph_d(s["font"], ch[1])
            if not dd: continue
            k = s["size"] * fm
            # The text matrix can be mirrored vertically: "dir" stays (1, 0) but the glyph box hangs
            # below the origin instead of standing on it. RR/01/01 draws the carets of "Limit of
            # migmatisation" as an upside-down "V" this way.
            b = ch[3]
            sc = f"{k:.5f} {-k:.5f}" if (b[3] - y) > (y - b[1]) else f"{k:.5f}"
            colours.add(c)
            elems.append(f'<path transform="translate({f2(x-ox)} {f2(y-oy)}) scale({sc})" fill="{c}" d="{dd}"/>')
    return elems, colours

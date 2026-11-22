"""Make seamless 'wrapped' tiles for irregular (non-periodic) ornaments.

Each mark (sub-path) whose centre falls inside the tile is drawn whole, plus copies shifted by one
tile width/height, so marks cut by one edge reappear on the opposite edge. Marks that span the
whole tile (long rules) are kept as-is. Axes with a detected period keep that period.
"""
import json, re, sys, math
root = sys.argv[1]
DENSE = {"CRSRB", "RNRBL", "MARBLE"}           # tessellations: wrapping would overlap stones
SNAP = {"LMST_S": ("LMST", 0)}                  # sandy limestone: snap width to limestone brick period

TOK = re.compile(r"[MLCQHVZhvz]|-?\d*\.?\d+(?:e-?\d+)?")
def subpaths(d):
    return [m for m in re.findall(r"M[^M]*", d)]
def bbox(d, tf=None):
    toks = TOK.findall(d); xs, ys = [], []; i = 0; cmd = None; cx = cy = 0
    while i < len(toks):
        t = toks[i]
        if t.isalpha(): cmd = t; i += 1; continue
        if cmd in ("M", "L"):
            cx, cy = float(toks[i]), float(toks[i+1]); xs.append(cx); ys.append(cy); i += 2
        elif cmd == "C":
            for k in range(3): xs.append(float(toks[i+2*k])); ys.append(float(toks[i+2*k+1]))
            cx, cy = xs[-1], ys[-1]; i += 6
        elif cmd == "Q":
            for k in range(2): xs.append(float(toks[i+2*k])); ys.append(float(toks[i+2*k+1]))
            cx, cy = xs[-1], ys[-1]; i += 4
        elif cmd == "h": cx += float(t); xs.append(cx); ys.append(cy); i += 1
        elif cmd == "v": cy += float(t); xs.append(cx); ys.append(cy); i += 1
        elif cmd == "H": cx = float(t); xs.append(cx); ys.append(cy); i += 1
        elif cmd == "V": cy = float(t); xs.append(cx); ys.append(cy); i += 1
        else: i += 1
    if not xs: return None
    b = [min(xs), min(ys), max(xs), max(ys)]
    if tf:
        tx, ty, kx, ky = tf
        xs2, ys2 = sorted((b[0]*kx, b[2]*kx)), sorted((b[1]*ky, b[3]*ky))
        b = [tx + xs2[0], ty + ys2[0], tx + xs2[1], ty + ys2[1]]
    return b

def elements(svg):
    out = []
    for m in re.finditer(r"<path ([^>]*?)/>", svg):
        attrs = m.group(1)
        d = re.search(r' ?d="([^"]+)"', " " + attrs).group(1)
        rest = re.sub(r' ?d="[^"]+"', "", " " + attrs).strip()
        tfm = re.search(r'transform="translate\(([-\d.]+) ([-\d.]+)\) scale\(([-\d.]+)(?: ([-\d.]+))?\)"', rest)
        if tfm:  # glyph: keep whole
            tx, ty, kx, ky = tfm.groups()
            tf = (float(tx), float(ty), float(kx), float(ky if ky is not None else kx))
            out.append((rest, d, bbox(d, tf), True)); continue
        filled = 'fill="none"' not in rest
        subs = subpaths(d)
        boxes = [bbox(s) for s in subs]
        # filled shapes: attach holes (sub-paths inside another) to their outer ring
        groups = []
        for s, b in sorted(zip(subs, boxes), key=lambda z: -((z[1][2]-z[1][0])*(z[1][3]-z[1][1]) if z[1] else 0)):
            if b is None: continue
            host = None
            if filled:
                for g in groups:
                    gb = g[1]
                    if gb[0] <= b[0] and gb[1] <= b[1] and b[2] <= gb[2] and b[3] <= gb[3]: host = g; break
            if host: host[0].append(s)
            else: groups.append([[s], b])
        for ss, b in groups: out.append((rest, "".join(ss), b, False))
    return out

def place(rest, d, dx, dy, glyph):
    if dx == 0 and dy == 0: return f'<path {rest} d="{d}"/>'
    return f'<g transform="translate({dx:.3f} {dy:.3f})"><path {rest} d="{d}"/></g>'

orn = json.load(open(f"{root}/ornaments.json"))
byref = {o["ref"]: o for o in orn}
for o in orn:
    if o["seamless"]:
        o["tile_method"] = "exact repeat (period detected)"; continue
    if o["ref"] in DENSE:
        o["tile_method"] = "cropped swatch (not seamless; irregular tessellation)"; continue
    svg = open(f"{root}/swatch/{o['ref']}.svg").read()
    sw, sh = o["swatch_pt"]
    els = [e for e in elements(svg) if e[2] and e[2][2] > 0 and e[2][3] > 0 and e[2][0] < sw and e[2][1] < sh]
    ux0 = min(e[2][0] for e in els); uy0 = min(e[2][1] for e in els)
    ux1 = max(e[2][2] for e in els); uy1 = max(e[2][3] for e in els)
    m = 2.0
    px, py = o["period_pt"]
    W = px if px else (ux1 - ux0 - 2*m)
    H = py if py else (uy1 - uy0 - 2*m)
    if o["ref"] in SNAP:
        base = byref[SNAP[o["ref"]][0]]["period_pt"][0]
        W = math.floor((ux1 - ux0 - 2*m) / base) * base; px_snap = True
    x0 = ux0 + m; y0 = uy0 + m
    wrapx, wrapy = px is None, py is None
    parts = []
    for rest, d, b, glyph in els:
        cx, cy = (b[0]+b[2])/2, (b[1]+b[3])/2
        spanx = (b[2]-b[0]) >= 0.8 * W; spany = (b[3]-b[1]) >= 0.8 * H
        if wrapx and not spanx:
            if not (x0 <= cx < x0 + W): continue
            dxs = [-W, 0, W]
        else: dxs = [0]
        if wrapy and not spany:
            if not (y0 <= cy < y0 + H): continue
            dys = [-H, 0, H]
        else: dys = [0]
        for dx in dxs:
            for dy in dys:
                if b[2]+dx < x0 or b[0]+dx > x0+W or b[3]+dy < y0 or b[1]+dy > y0+H: continue
                parts.append(place(rest, d, dx, dy, glyph))
    title = re.search(r"<title>(.*?)</title>", svg).group(1)
    f2 = lambda v: f"{v:.3f}".rstrip("0").rstrip(".")
    tile = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{f2(W)}pt" height="{f2(H)}pt" viewBox="{f2(x0)} {f2(y0)} {f2(W)} {f2(H)}">\n'
            f'  <title>{title} - repeat tile</title>\n' + "\n".join("  " + p for p in parts) + "\n</svg>\n")
    open(f"{root}/tile/{o['ref']}.svg", "w").write(tile)
    o["seamless"] = True; o["tile_pt"] = [round(W, 3), round(H, 3)]
    o["tile_method"] = "wrapped marks (seamless; irregular marks re-arranged at tile edges)" + (" with width snapped to LMST brick period" if o["ref"] in SNAP else "")
    print("wrapped", o["ref"], round(W,1), round(H,1), len(parts), "marks")
json.dump(orn, open(f"{root}/ornaments.json", "w"), indent=1)

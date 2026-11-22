"""Generate a made-up geological dataset ("Isle of Mawer", a fictional island in the Celtic Sea)
that uses every symbol, area ornament and line style. Deterministic (fixed seed)."""
import json, math, sys, os, random
import numpy as np
from shapely.geometry import Polygon, Point, LineString, mapping, box
from shapely.ops import unary_union
from scipy.spatial import Voronoi

root = sys.argv[1]
out = f"{root}/docs/data"; os.makedirs(out, exist_ok=True)
rng = random.Random(1997)        # version 1 of the symbol index: April 1997
np_rng = np.random.default_rng(1997)
LAT0, LON0 = 50.85, -7.2
KX = 111.32 * math.cos(math.radians(LAT0)); KY = 110.57
def ll(x, y): return (round(LON0 + x / KX, 6), round(LAT0 + y / KY, 6))
def to_ll(geom):
    g = mapping(geom)
    def conv(c):
        if isinstance(c[0], (float, int)): return ll(*c)
        return [conv(cc) for cc in c]
    g["coordinates"] = conv(g["coordinates"]); return g

syms = json.load(open(f"{root}/Symbols/symbols.json"))
orns = json.load(open(f"{root}/Area-Ornaments/ornaments.json"))
lines = json.load(open(f"{root}/Line-Styles/lines.json"))

# ---- island outline (km) ------------------------------------------------------------
R = 30.0
ph = [rng.uniform(0, 2 * math.pi) for _ in range(6)]
pts = []
for i in range(360):
    a = math.radians(i)
    r = R * (1 + 0.10 * math.sin(2 * a + ph[0]) + 0.07 * math.sin(3 * a + ph[1]) + 0.05 * math.sin(5 * a + ph[2])
               + 0.025 * math.sin(9 * a + ph[3]) + 0.012 * math.sin(17 * a + ph[4]))
    pts.append((r * math.cos(a) * 1.15, r * math.sin(a) * 0.9))
island = Polygon(pts).buffer(0)

# ---- geology polygons: one Voronoi cell per ornament (Lloyd-relaxed) ----------------------
minx, miny, maxx, maxy = island.bounds
P = []
while len(P) < len(orns):
    p = (rng.uniform(minx, maxx), rng.uniform(miny, maxy))
    if island.contains(Point(p)): P.append(p)
P = np.array(P)
frame = np.array([[minx - 200, miny - 200], [minx - 200, maxy + 200], [maxx + 200, miny - 200], [maxx + 200, maxy + 200]])
def cells(P):
    vor = Voronoi(np.vstack([P, frame]))
    res = []
    for i in range(len(P)):
        reg = vor.regions[vor.point_region[i]]
        poly = Polygon([vor.vertices[v] for v in reg]).intersection(island)
        res.append(poly)
    return res
for _ in range(4):
    cs = cells(P); P = np.array([[c.centroid.x, c.centroid.y] for c in cs])
cs = cells(P)
PALETTE = ["#f2e6c9", "#e9d8a6", "#d9e4c4", "#c9dcd2", "#e7c9b4", "#efd3d3", "#dcd0e6", "#cfdcea",
           "#f3edd9", "#e0e0cc", "#ead6bd", "#d6e2dc"]
# order cells west->east so similar ornaments cluster a little
order = sorted(range(len(cs)), key=lambda i: (round(cs[i].centroid.x / 9), cs[i].centroid.y))
geo = []
for k, i in enumerate(order):
    o = orns[k]
    geo.append(dict(type="Feature", properties=dict(ref=o["ref"], description=o["description"], kind="ornament",
                    fill=PALETTE[k % len(PALETTE)], pattern="orn-" + o["ref"], seamless=o["seamless"],
                    unit=f"{o['description']} (made-up unit {k+1:02d})"), geometry=to_ll(cs[i])))
json.dump(dict(type="FeatureCollection", features=geo), open(f"{out}/geology.geojson", "w"))
json.dump(dict(type="FeatureCollection", features=[dict(type="Feature", properties=dict(name="Isle of Mawer (fictional)"),
          geometry=to_ll(island))]), open(f"{out}/island.geojson", "w"))

# ---- line features: one gently curving line per style, on a grid --------------------------
def grid_inside(spacing, inset, jitter):
    g = []
    inner = island.buffer(-inset)
    y = miny
    while y <= maxy:
        x = minx
        while x <= maxx:
            p = Point(x + rng.uniform(-jitter, jitter), y + rng.uniform(-jitter, jitter))
            if inner.contains(p): g.append((p.x, p.y))
            x += spacing
        y += spacing
    return g
sp = 6.0
while True:
    G = grid_inside(sp, 3.0, 0.4)
    if len(G) >= len(lines): break
    sp *= 0.95
rng.shuffle(G)
lf = []
for l, (cx, cy) in zip(lines, G):
    ang = rng.uniform(0, math.pi); L = sp * 0.8; amp = rng.uniform(0.15, 0.5); k = rng.uniform(0.6, 1.4)
    pts = []
    for t in np.linspace(-0.5, 0.5, 40):
        u = t * L; v = amp * math.sin(k * math.pi * t * 2)
        pts.append((cx + u * math.cos(ang) - v * math.sin(ang), cy + u * math.sin(ang) + v * math.cos(ang)))
    lf.append(dict(type="Feature", properties=dict(id=l["id"], description=l["description"], kind="line",
                   pattern="line-" + l["id"], width=l["sprite_px"][1], seamless=l["seamless"]),
                   geometry=to_ll(LineString(pts))))
json.dump(dict(type="FeatureCollection", features=lf), open(f"{out}/lines.geojson", "w"))

# ---- point symbols: snake-ordered jittered grid so each group forms a band -----------------
sp = 3.0
while True:
    G = grid_inside(sp, 1.5, 0.3)
    if len(G) >= len(syms): break
    sp *= 0.97
cols = {}
for x, y in G: cols.setdefault(round((x - minx) / sp), []).append((x, y))
snake = []
for i, c in enumerate(sorted(cols)):
    snake += sorted(cols[c], key=lambda p: p[1], reverse=bool(i % 2))
step = len(snake) / len(syms)
GROUP_ORDER = {"Drift": 0, "Rock": 1, "Structural": 2, "Other": 3}
ordered = sorted(syms, key=lambda s: (GROUP_ORDER.get(s["group"], 9), s["order"]))
pf = []
for i, s in enumerate(ordered):
    x, y = snake[int(i * step)]
    rot = rng.randrange(0, 360, 5) if s["group"] == "Structural" else 0
    props = dict(ref=s["ref"], description=s["description"], kind="symbol", group=s["group"],
                 classification=s["classification"], subclassification=s["subclassification"] or "",
                 icon="sym-" + s["ref"], rotation=rot)
    if s["group"] == "Structural": props["made_up_dip"] = rng.randrange(5, 90, 5)
    pf.append(dict(type="Feature", properties=props, geometry=dict(type="Point", coordinates=ll(x, y))))
json.dump(dict(type="FeatureCollection", features=pf), open(f"{out}/symbols.geojson", "w"))

# ---- compact catalogue for the demo sidebar ------------------------------------------------
cat = dict(
    symbols=[dict(ref=s["ref"], d=s["description"], g=s["group"], c=s["classification"], s=s["subclassification"] or "") for s in syms],
    ornaments=[dict(ref=o["ref"], d=o["description"], seamless=o["seamless"]) for o in orns],
    lines=[dict(id=l["id"], d=l["description"], w=l["sprite_px"][1], seamless=l["seamless"]) for l in lines])
json.dump(cat, open(f"{out}/catalogue.json", "w"), separators=(",", ":"))
print(len(geo), "polygons,", len(lf), "lines,", len(pf), "points; grid spacing", round(sp, 2), "km")

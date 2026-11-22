"""Build Symbols/: catalogue + SVGs extracted from the embedded symbol fonts in RR/01/01."""
import json, sys, os, re, csv, collections, html
sys.path.insert(0, os.path.dirname(__file__))
from glyphs import FontBank

pdf, parsed, out = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(parsed))
fb = FontBank(pdf)

# ---- 1. merge wrapped description lines (2.1) ----------------------------------
import pymupdf
doc = pymupdf.open(pdf)
def desc_lines(pno, xmin, xmax):
    pg = doc[pno-1]; res = []
    for b in pg.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if s["text"].strip() and xmin < s["bbox"][0] and s["bbox"][2] <= xmax and "Bold" not in s["font"] and s["size"] > 9 and not s["font"].startswith("TT"):
                    res.append(((s["bbox"][1]+s["bbox"][3])/2, s["bbox"][0], s["text"].strip()))
    return res

def full_desc(rows, xmin, xmax):
    bypage = collections.defaultdict(list)
    for r in rows: bypage[r["page"]].append(r)
    for p, rs in bypage.items():
        for r in rs: r["_parts"] = []
        for y, x, t in desc_lines(p, xmin, xmax):
            if y < 100: continue
            best = min(rs, key=lambda r: abs(r["y"] - y))
            if abs(best["y"] - y) < 14: best["_parts"].append((y, x, t))
        for r in rs:
            r["description"] = re.sub(r"\s+", " ", " ".join(t for y, x, t in sorted(r["_parts"]))).strip()
            r["description"] = re.sub(r"\s+,", ",", r["description"]).rstrip(",").strip()
            del r["_parts"]

r21 = [r for r in d["s21"] if r["section"] == "2.1"]
heads = [r for r in d["s21"] if r["section"] == "head"]
full_desc(r21, 150, 415)
full_desc(d["s22"], 50, 375)

# ---- 2. classification from 2.1 headings ----------------------------------------
heads.sort(key=lambda h: (h["page"], h["y"]))
blocks = []
for h in heads:
    up = lambda t: t.split()[0].isupper() and len(t.split()[0]) > 1
    neutral = h["text"].lower().startswith("(continued")
    if blocks and blocks[-1]["page"] == h["page"] and 0 < h["y"] - blocks[-1]["y_last"] < 14 and (neutral or up(h["text"]) == blocks[-1]["up"]):
        blocks[-1]["text"] += " " + h["text"]; blocks[-1]["y_last"] = h["y"]
    else:
        blocks.append(dict(page=h["page"], y=h["y"], y_last=h["y"], text=h["text"], up=up(h["text"])))
GROUP = {"ARTIFICIAL DEPOSITS":"Drift","MASS- MOVEMENT":"Drift","AEOLIAN DEPOSITS":"Drift","ORGANIC DEPOSITS":"Drift",
         "CHEMICAL /ORGANIC DEPOSITS":"Drift","FLUVIAL DEPOSITS":"Drift","LACUSTRINE DEPOSITS":"Drift","MARINE DEPOSITS":"Drift",
         "RAISED MARINE DEPOSITS":"Drift","INTERGLACIAL":"Drift","GLACIAL DEPOSITS":"Drift","MISCELLANEOUS DRIFT":"Drift",
         "LANDFORM":"Drift","ROCK SYMBOLS":"Rock","STRUCTURAL SYMBOLS":"Structural","OTHER SYMBOLS":"Other"}
def clean(t):
    t = re.sub(r"\(continued\)", "", t, flags=re.I).strip()
    t = t.replace("D R I F T", "DRIFT").replace("MASS- MOVEMENT", "MASS-MOVEMENT").replace("CHEMICAL /ORGANIC", "CHEMICAL/ORGANIC")
    return re.sub(r"\s+", " ", t)
def title(t):
    return " ".join(w if w in ("/",) else w.capitalize() if w.isupper() else w for w in t.split()).replace("Chemical/organic","Chemical/Organic")
cls, sub, grp = None, None, None
events = sorted([("h", b["page"], b["y"], b) for b in blocks] + [("r", r["page"], r["y"], r) for r in r21], key=lambda e: (e[1], e[2], e[0] != "h"))
for kind, p, y, o in events:
    if kind == "h":
        raw = re.sub(r"\(continued\)", "", o["text"], flags=re.I).strip()
        raw = re.sub(r"\s+", " ", raw)
        if raw == "D R I F T": continue
        if raw.split()[0].isupper() and len(raw.split()[0]) > 1:
            key = raw if raw in GROUP else raw.replace("STRUCTURAL SYMBOLS", "STRUCTURAL SYMBOLS")
            grp = GROUP.get(raw, grp); cls = title(clean(raw)); sub = None
        else:
            sub = clean(raw).replace("Deposits", "deposits")
    else:
        o["group"], o["classification"], o["subclassification"] = grp, cls, sub

# ---- 3. alt descriptions from 2.2 -------------------------------------------------
alt = collections.defaultdict(list)
for r in d["s22"]:
    alt[r["ref"].upper()].append(r["description"])

# ---- 4. scale: BGS standard = Alluvium body 3 mm -----------------------------------
alv = next(r for r in r21 if r["ref"] == "ALV")["glyphs"][0]
alv_w = fb.glyph(alv["font"], alv["gid"])["bounds"][2] - fb.glyph(alv["font"], alv["gid"])["bounds"][0]
MM_PER_UNIT = 3.0 / alv_w
PAD = 30  # font units of padding around each glyph

os.makedirs(f"{out}/svg", exist_ok=True)
os.makedirs(f"{out}/svg-24px", exist_ok=True)
os.makedirs(f"{out}/svg-48px", exist_ok=True)
# Inconsistencies found in the source PDF (sections 2.1 and 2.2 disagree)
NOTES = {
    "RT_SH": "Source inconsistency: section 2.1 labels this symbol 'SH', the A-Z index (2.2) labels it 'SHG'. This file follows 2.1.",
    "S_DIP": "Source inconsistency: printed at 16 pt in section 2.1 but at the standard 10 pt in the A-Z index (2.2). Drawn here at the standard size.",
    "S_HFJ": "Source inconsistency: the report prints the same glyph for horizontal (S_HFJ) and inclined (S_IFJ) flow jointing.",
    "S_IFJ": "Source inconsistency: the report prints the same glyph for horizontal (S_HFJ) and inclined (S_IFJ) flow jointing.",
}
STANDARD_SIZE = {"S_DIP"}
cat = []
for i, r in enumerate(r21):
    g = r["glyphs"][0]
    gl = fb.glyph(g["font"], g["gid"])
    x0, y0, x1, y1 = gl["bounds"]
    # Every glyph is printed at 9.96 pt except S_DIP (16 pt in 2.1 only): scale by printed size, but draw S_DIP at standard size
    k = 1.0 if r["ref"] in STANDARD_SIZE else g["size"] / 9.9595
    vb = (x0 - PAD, -y1 - PAD, x1 - x0 + 2 * PAD, y1 - y0 + 2 * PAD)
    wmm, hmm = vb[2] * MM_PER_UNIT * k, vb[3] * MM_PER_UNIT * k
    ref = r["ref"]
    descs = [x for x in alt.get(ref.upper(), []) if x and x != r["description"]]
    title_ = r["description"] or (descs[0] if descs else ref)
    tf = f' transform="scale({k:.4f})"' if abs(k - 1) > 0.01 else ""
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{wmm:.3f}mm" height="{hmm:.3f}mm" '
           f'viewBox="{vb[0]*k:.1f} {vb[1]*k:.1f} {vb[2]*k:.1f} {vb[3]*k:.1f}">\n'
           f'  <title>{html.escape(title_)} ({ref})</title>\n  <path{tf} fill="#000000" d="{gl["d"]}"/>\n</svg>\n')
    open(f"{out}/svg/{ref}.svg", "w").write(svg)
    for px in (24, 48):
        side = max(vb[2], vb[3]) * k
        cx, cy = (x0 + x1) / 2 * k, -(y0 + y1) / 2 * k
        open(f"{out}/svg-{px}px/{ref}_{px}px.svg", "w").write(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" '
            f'viewBox="{cx-side/2:.1f} {cy-side/2:.1f} {side:.1f} {side:.1f}">\n'
            f'  <title>{html.escape(title_)} ({ref})</title>\n  <path{tf} fill="#000000" d="{gl["d"]}"/>\n</svg>\n')
    cat.append(dict(ref=ref, description=title_, alt_descriptions=descs,
                    group=r["group"], classification=r["classification"], subclassification=r["subclassification"],
                    width_mm=round(wmm, 3), height_mm=round(hmm, 3),
                    notes=NOTES.get(ref, ""),
                    source=dict(document="BGS RR/01/01 v3", pdf_page=r["page"], font=g["font"], glyph_id=g["gid"]),
                    order=i))
json.dump(cat, open(f"{out}/symbols.json", "w"), indent=1, ensure_ascii=False)
with open(f"{out}/symbols.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ref", "description", "alt_descriptions", "group", "classification", "subclassification", "width_mm", "height_mm", "svg", "notes"])
    for c in cat:
        w.writerow([c["ref"], c["description"], " | ".join(c["alt_descriptions"]), c["group"], c["classification"], c["subclassification"] or "", c["width_mm"], c["height_mm"], f"svg/{c['ref']}.svg", c["notes"]])
print(len(cat), "symbols; ALV width units", alv_w, "mm/unit", MM_PER_UNIT)
print(collections.Counter((c["group"], c["classification"]) for c in cat))
print("lower-case clash:", [k for k, v in collections.Counter(c["ref"].lower() for c in cat).items() if v > 1])

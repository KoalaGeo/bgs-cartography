"""Parse RR/01/01 section 2 tables into a symbol catalogue (JSON)."""
import pymupdf, json, sys, collections
doc = pymupdf.open(sys.argv[1])

def page_rows(pno):
    pg = doc[pno]
    d = pg.get_text("dict")
    spans = []
    for b in d["blocks"]:
        for l in b.get("lines", []):
            for s in l["spans"]:
                if s["text"].strip():
                    spans.append(s)
    glyphs = [s for s in pg.get_texttrace() if s["font"].startswith("TT")]
    return spans, glyphs

out21, out22, anomalies = [], [], []
for pno in range(len(doc)):
    spans, glyphs = page_rows(pno)
    header = " ".join(s["text"] for s in spans[:3])
    if "INDEX LISTED BY CLASSIFICATION" in " ".join(s["text"] for s in spans) and any(s["text"].strip()=="REF NAME" for s in spans):
        sec = "2.1"
    elif "INDEX LISTED BY DESCRIPTION" in " ".join(s["text"] for s in spans) and any(s["text"].strip()=="REF NAME" for s in spans):
        sec = "2.2"
    else:
        continue
    head_y = next(s["bbox"][3] for s in spans if s["text"].strip()=="REF NAME")
    refcol = [s for s in spans if s["size"] < 9 and 400 < s["bbox"][0] < 480 and s["bbox"][1] > head_y]
    # column x positions differ between 2.1 and 2.2: detect ref col from header
    hx = next(s["bbox"][0] for s in spans if s["text"].strip()=="REF NAME")
    sx = next(s["bbox"][0] for s in spans if s["text"].strip()=="SYMBOL")
    dx = next(s["bbox"][0] for s in spans if s["text"].strip()=="DESCRIPTION")
    refcol = [s for s in spans if hx-15 < s["bbox"][0] < sx-5 and s["bbox"][1] > head_y and not s["font"].startswith("TT")]
    for r in refcol:
        cy = (r["bbox"][1]+r["bbox"][3])/2
        # description: regular font spans left of ref col on same line
        desc = [s for s in spans if s["bbox"][2] <= hx and abs((s["bbox"][1]+s["bbox"][3])/2 - cy) < 5
                and "Bold" not in s["font"] and not s["font"].startswith("TT") and s["bbox"][0] > (150 if sec=="2.1" else 50)]
        g = [x for x in glyphs if abs((x["bbox"][1]+x["bbox"][3])/2 - cy) < 7 and x["bbox"][0] > sx-25]
        rec = dict(section=sec, page=pno+1, ref=r["text"].strip(), y=round(cy,1),
                   description=" ".join(s["text"].strip() for s in sorted(desc, key=lambda s:s["bbox"][0])),
                   glyphs=[dict(font=x["font"], gid=c[1], uni=c[0], origin=[round(c[2][0],2), round(c[2][1],2)],
                                size=round(x["size"],3), color=x["color"]) for x in g for c in x["chars"]])
        if len(rec["glyphs"]) != 1: anomalies.append(rec)
        (out21 if sec=="2.1" else out22).append(rec)
    if sec == "2.1":
        # classification headings: bold spans at left; subclass: regular spans at x<150
        heads = [s for s in spans if s["bbox"][0] < 150 and s["bbox"][1] > head_y]
        for s in heads:
            out21.append(dict(section="head", page=pno+1, y=round((s["bbox"][1]+s["bbox"][3])/2,1),
                              text=s["text"].strip(), bold="Bold" in s["font"]))
json.dump(dict(s21=out21, s22=out22, anomalies=anomalies), open(sys.argv[2], "w"), indent=1)
print(len([r for r in out21 if r["section"]=="2.1"]), "rows in 2.1;", len(out22), "rows in 2.2;", len(anomalies), "anomalies")
for a in anomalies[:30]: print("ANOM", a["section"], a["page"], a["ref"], a["description"], len(a["glyphs"]))

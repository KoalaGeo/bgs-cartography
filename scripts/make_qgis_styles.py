"""Build QGIS styles with the QGIS API itself (so they are valid for QGIS 3.x):

  Styles/QGIS/bgs-symbology-embedded.xml  symbol library, graphics embedded (works offline)
  Styles/QGIS/bgs-symbology-linked.xml    symbol library, graphics linked to the published URLs
  Styles/QGIS/bgs_symbols.qml             categorised layer style on the 'ref' attribute (embedded)
  Styles/QGIS/bgs_ornaments.qml           categorised on 'ref' (embedded)
  Styles/QGIS/bgs_line_styles.qml         categorised on 'id' (embedded)

Needs PyQGIS (run with the Python that QGIS was built for, e.g. /usr/bin/python3.12):
    QT_QPA_PLATFORM=offscreen python3.12 scripts/make_qgis_styles.py . [--base-url URL]
"""
import argparse, base64, json, os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from qgis.core import (QgsApplication, QgsStyle, QgsMarkerSymbol, QgsFillSymbol, QgsLineSymbol,
                       QgsSvgMarkerSymbolLayer, QgsSVGFillSymbolLayer, QgsRasterLineSymbolLayer,
                       QgsSimpleLineSymbolLayer, QgsSymbolLayer, QgsProperty, QgsUnitTypes,
                       QgsVectorLayer, QgsCategorizedSymbolRenderer, QgsRendererCategory)
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QColor

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--base-url", default="https://koalageo.github.io/bgs-cartography/v3")
ap.add_argument("--symbol-field", default="ref"); ap.add_argument("--rotation-field", default="rotation")
ap.add_argument("--ornament-field", default="ref"); ap.add_argument("--line-field", default="id")
a = ap.parse_args()
R, BASE = a.root, a.base_url.rstrip("/")
app = QgsApplication([], False); app.initQgis()
MM = QgsUnitTypes.RenderMillimeters
PT_MM = 25.4 / 72
ANGLE = getattr(QgsSymbolLayer, "PropertyAngle", None) or QgsSymbolLayer.Property.Angle

syms = json.load(open(f"{R}/Symbols/symbols.json"))
orns = json.load(open(f"{R}/Area-Ornaments/ornaments.json"))
lines = json.load(open(f"{R}/Line-Styles/lines.json"))
os.makedirs(f"{R}/Styles/QGIS", exist_ok=True)

def src(local, url, embed):
    return "base64:" + base64.b64encode(open(local, "rb").read()).decode() if embed else url

def symbol_marker(s, embed):
    lyr = QgsSvgMarkerSymbolLayer(src(f"{R}/Symbols/svg/{s['ref']}.svg", f"{BASE}/symbols/svg/{s['ref']}.svg", embed))
    lyr.setSize(s["width_mm"]); lyr.setSizeUnit(MM)          # BGS standard size (3 mm body)
    lyr.setFillColor(QColor(0, 0, 0)); lyr.setStrokeWidth(0)
    if s["group"] == "Structural":
        lyr.setDataDefinedProperty(ANGLE, QgsProperty.fromField(a.rotation_field))
    return QgsMarkerSymbol([lyr])

def ornament_fill(o, embed):
    lyr = QgsSVGFillSymbolLayer(src(f"{R}/Area-Ornaments/tile/{o['ref']}.svg", f"{BASE}/ornaments/tile/{o['ref']}.svg", embed),
                                o["tile_pt"][0] * PT_MM, 0)
    lyr.setPatternWidthUnit(MM)
    outline = QgsSimpleLineSymbolLayer(); outline.setPenStyle(Qt.NoPen)
    lyr.setSubSymbol(QgsLineSymbol([outline]))             # pattern only, no polygon outline
    return QgsFillSymbol([lyr])

def line_symbol(l, embed):
    lyr = QgsRasterLineSymbolLayer(src(f"{R}/Line-Styles/png/{l['id']}.png", f"{BASE}/lines/png/{l['id']}.png", embed))
    lyr.setWidth(l["sprite_px"][1] * 0.75 * PT_MM); lyr.setWidthUnit(MM)   # tile height at printed size
    lyr.setPenCapStyle(Qt.FlatCap); lyr.setPenJoinStyle(Qt.RoundJoin)
    return QgsLineSymbol([lyr])

# ---- symbol libraries ----
for embed in (True, False):
    st = QgsStyle(); st.createMemoryDatabase()
    for s in syms:
        n = f"BGS {s['ref']} - {s['description']}"
        st.addSymbol(n, symbol_marker(s, embed), True)
        st.tagSymbol(QgsStyle.SymbolEntity, n, ["BGS", "BGS symbols", s["classification"]] + ([s["subclassification"]] if s["subclassification"] else []))
    for o in orns:
        n = f"BGS ornament {o['ref']} - {o['description']}"
        st.addSymbol(n, ornament_fill(o, embed), True)
        st.tagSymbol(QgsStyle.SymbolEntity, n, ["BGS", "BGS ornaments"])
    for l in lines:
        n = f"BGS line - {l['description']}"
        st.addSymbol(n, line_symbol(l, embed), True)
        st.tagSymbol(QgsStyle.SymbolEntity, n, ["BGS", "BGS line styles"])
    f = f"{R}/Styles/QGIS/bgs-symbology-{'embedded' if embed else 'linked'}.xml"
    assert st.exportXml(f), f
    print("wrote", f, st.symbolCount(), "symbols")

# ---- categorised layer styles (QML, embedded) ----
def qml(geom, field, cats, path):
    vl = QgsVectorLayer(f"{geom}?field={field}:string", "tmp", "memory")
    r = QgsCategorizedSymbolRenderer(field, [QgsRendererCategory(v, sym, label) for v, sym, label in cats])
    vl.setRenderer(r)
    msg, ok = vl.saveNamedStyle(path)
    assert ok, msg
    print("wrote", path, len(cats), "categories")
qml("Point", a.symbol_field, [(s["ref"], symbol_marker(s, True), f"{s['ref']} {s['description']}") for s in syms], f"{R}/Styles/QGIS/bgs_symbols.qml")
qml("Polygon", a.ornament_field, [(o["ref"], ornament_fill(o, True), f"{o['ref']} {o['description']}") for o in orns], f"{R}/Styles/QGIS/bgs_ornaments.qml")
qml("LineString", a.line_field, [(l["id"], line_symbol(l, True), l["description"]) for l in lines], f"{R}/Styles/QGIS/bgs_line_styles.qml")
# Every file is written and closed by now. QgsApplication.exitQgis() can segfault in a headless
# PyQGIS (QGIS 3.34) while tearing down, which would stop build_all.sh, so skip the teardown.
import sys; sys.stdout.flush(); os._exit(0)

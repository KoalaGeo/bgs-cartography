"""Build QGIS styles with the QGIS API itself (so they are valid for QGIS 3.x):

  Styles/QGIS/bgs-symbology-embedded.xml  symbol library, graphics embedded (works offline)
  Styles/QGIS/bgs-symbology-linked.xml    symbol library, graphics linked to the published URLs
  Styles/QGIS/bgs_symbols.qml             categorised layer style on the 'ref' attribute (embedded)
  Styles/QGIS/bgs_ornaments.qml           categorised on 'ref' (embedded)
  Styles/QGIS/bgs_line_styles.qml         categorised on 'id' (embedded)

Needs PyQGIS (run with the Python that QGIS was built for, e.g. /usr/bin/python3.12):
    QT_QPA_PLATFORM=offscreen python3.12 scripts/make_qgis_styles.py . [--base-url URL]

The linked library's paths default to relative (../../symbols/svg/ALV.svg, i.e. relative to
v3/styles/qgis/ where it is published), so the committed file names no host. Publishing makes
them absolute with scripts/make_web_styles.py --base-url, which needs no QGIS.
"""
import argparse, base64, itertools, json, os, re, uuid
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
os.environ.setdefault("QT_HASH_SEED", "0")   # fixed XML attribute order, so rebuilds diff cleanly
from qgis.core import (QgsApplication, QgsStyle, QgsMarkerSymbol, QgsFillSymbol, QgsLineSymbol,
                       QgsSvgMarkerSymbolLayer, QgsSVGFillSymbolLayer, QgsRasterLineSymbolLayer,
                       QgsSimpleLineSymbolLayer, QgsSymbolLayer, QgsProperty, QgsUnitTypes,
                       QgsVectorLayer, QgsCategorizedSymbolRenderer, QgsRendererCategory, QgsMapLayer)
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QColor

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--base-url", default="../..", help="public URL of the v3 folder (default: relative paths)")
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
    outline.setColor(QColor(0, 0, 0))                       # otherwise QGIS picks a random colour
    lyr.setSubSymbol(QgsLineSymbol([outline]))             # pattern only, no polygon outline
    return QgsFillSymbol([lyr])

def line_symbol(l, embed):
    lyr = QgsRasterLineSymbolLayer(src(f"{R}/Line-Styles/png/{l['id']}.png", f"{BASE}/lines/png/{l['id']}.png", embed))
    lyr.setWidth(l["sprite_px"][1] * 0.75 * PT_MM); lyr.setWidthUnit(MM)   # tile height at printed size
    lyr.setPenCapStyle(Qt.FlatCap); lyr.setPenJoinStyle(Qt.RoundJoin)
    return QgsLineSymbol([lyr])

def stable_ids(path):
    """QGIS gives every symbol layer and renderer category a random UUID. Replace each distinct
    one with a name-based UUID (same original -> same replacement, so any cross-reference still
    matches), so that rebuilding gives byte-identical files."""
    xml = open(path, encoding="utf-8").read()
    new, n = {}, itertools.count()
    def sub(m):
        if m.group(2) not in new:
            new[m.group(2)] = str(uuid.uuid5(uuid.NAMESPACE_URL, f"bgs-symbology/{os.path.basename(path)}/{next(n)}"))
        return f'{m.group(1)}{{{new[m.group(2)]}}}"'
    xml = re.sub(r'(\b(?:id|uuid)=")\{([0-9a-f-]{36})\}"', sub, xml)
    open(path, "w", encoding="utf-8").write(xml)

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
    if not embed:   # QGIS may rewrite relative paths on export: put back exactly BASE/<folder>/<file>
        xml = open(f, encoding="utf-8").read()
        xml = re.sub(r'(\bvalue=")[^"]*?((?:symbols|ornaments|lines)/(?:svg|tile|png)/[^"/]+)"',
                     lambda m: f'{m.group(1)}{BASE}/{m.group(2)}"', xml)
        open(f, "w", encoding="utf-8").write(xml)
    stable_ids(f)
    print("wrote", f, st.symbolCount(), "symbols")

# ---- categorised layer styles (QML, embedded) ----
def qml(geom, field, cats, path):
    vl = QgsVectorLayer(f"{geom}?field={field}:string", "tmp", "memory")
    r = QgsCategorizedSymbolRenderer(field, [QgsRendererCategory(v, sym, label) for v, sym, label in cats])
    vl.setRenderer(r)
    # Symbology only: applying the style should not also reset the user's labels, scale limits etc.
    msg, ok = vl.saveNamedStyle(path, QgsMapLayer.Symbology)
    assert ok, msg
    stable_ids(path)
    print("wrote", path, len(cats), "categories")
qml("Point", a.symbol_field, [(s["ref"], symbol_marker(s, True), f"{s['ref']} {s['description']}") for s in syms], f"{R}/Styles/QGIS/bgs_symbols.qml")
qml("Polygon", a.ornament_field, [(o["ref"], ornament_fill(o, True), f"{o['ref']} {o['description']}") for o in orns], f"{R}/Styles/QGIS/bgs_ornaments.qml")
qml("LineString", a.line_field, [(l["id"], line_symbol(l, True), l["description"]) for l in lines], f"{R}/Styles/QGIS/bgs_line_styles.qml")
# Every file is written and closed by now. QgsApplication.exitQgis() can segfault in a headless
# PyQGIS (QGIS 3.34) while tearing down, which would stop build_all.sh, so skip the teardown.
import sys; sys.stdout.flush(); os._exit(0)

"""Render the demo data in QGIS with (a) the QML styles, (b) the GeoServer SLDs and
(c) symbols from both symbol libraries, as a check that QGIS reads them all.

    QT_QPA_PLATFORM=offscreen python3.12 scripts/check_qgis_styles.py <site_v3_dir_or_repo> <out_dir>

The SLD and 'linked' checks fetch graphics over HTTP from the URLs written into those files,
so serve the site first (see serve/README.md).
"""
import os, sys, time
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from qgis.core import (QgsApplication, QgsVectorLayer, QgsMapSettings, QgsMapRendererSequentialJob,
                       QgsStyle, QgsRectangle, QgsCoordinateReferenceSystem, QgsProject)
from qgis.PyQt.QtCore import QSize
from qgis.PyQt.QtGui import QColor, QImage, QPainter

R, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
app = QgsApplication([], False); app.initQgis()
data = f"{R}/docs/data" if os.path.isdir(f"{R}/docs") else f"{R}/data"
styles = f"{R}/Styles" if os.path.isdir(f"{R}/Styles") else None

def wait(sec):
    t = time.time()
    while time.time() - t < sec: app.processEvents(); time.sleep(0.05)

def layers(kind):
    out = []
    for name, sty in (("geology", "ornaments"), ("lines", "line_styles"), ("symbols", "symbols")):
        vl = QgsVectorLayer(f"{data}/{name}.geojson", name, "ogr"); assert vl.isValid(), name
        if kind == "qml":
            msg, ok = vl.loadNamedStyle(f"{styles}/QGIS/bgs_{sty}.qml"); assert ok, msg
        else:
            msg, ok = vl.loadSldStyle(f"{styles}/GeoServer/bgs_{sty}.sld"); assert ok, msg
        n = len(vl.renderer().categories()) if hasattr(vl.renderer(), "categories") else len(vl.renderer().rootRule().children())
        print(f"  {kind}: {name} renderer={vl.renderer().type()} classes={n}")
        out.append(vl)
    return out[::-1]   # symbols on top

def render(lyrs, extent, path, size=(1600, 1100)):
    ms = QgsMapSettings(); ms.setLayers(lyrs); ms.setBackgroundColor(QColor("#ffffff"))
    ms.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:27700")); ms.setOutputSize(QSize(*size)); ms.setOutputDpi(96)
    from qgis.core import QgsCoordinateTransform
    xf = QgsCoordinateTransform(QgsCoordinateReferenceSystem("EPSG:4326"), ms.destinationCrs(), QgsProject.instance())
    ms.setExtent(xf.transformBoundingBox(extent))
    # Headless rendering: load remote graphics synchronously (QGIS desktop instead refreshes when they arrive)
    ms.setFlag(QgsMapSettings.RenderBlocking, True)
    job = QgsMapRendererSequentialJob(ms); job.start(); job.waitForFinished()
    job.renderedImage().save(path); print("  ->", path)

zoom = QgsRectangle(-7.30, 50.80, -7.18, 50.87)
print("QML styles"); render(layers("qml"), zoom, f"{OUT}/qgis_qml.png")
print("SLD styles"); render(layers("sld"), zoom, f"{OUT}/qgis_sld.png")

for kind in ("embedded", "linked"):
    st = QgsStyle(); st.createMemoryDatabase()
    assert st.importXml(f"{styles}/QGIS/bgs-symbology-{kind}.xml")
    names = st.symbolNames(); print(f"library {kind}: {len(names)} symbols")
    pick = [n for n in names if n.startswith(("BGS ALV ", "BGS S_GDIP ", "BGS ornament LMST ", "BGS ornament ST_CYN ", "BGS line - Fault, thrust observed"))]
    for n in pick: st.symbol(n).asImage(QSize(160, 80))
    wait(10)                                                        # let remote graphics arrive
    sheet = QImage(180 * len(pick), 100, QImage.Format_ARGB32); sheet.fill(QColor("white")); p = QPainter(sheet)
    for i, n in enumerate(pick): p.drawImage(10 + 180 * i, 10, st.symbol(n).asImage(QSize(160, 80)))
    p.end(); sheet.save(f"{OUT}/qgis_library_{kind}.png"); print("  ->", f"{OUT}/qgis_library_{kind}.png", pick)
app.exitQgis()

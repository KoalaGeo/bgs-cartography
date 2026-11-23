# Styles

Ready-made styles for desktop GIS and map servers, all generated from the same catalogues.

## QGIS (`QGIS/`)

| File | What it is |
|---|---|
| `bgs-symbology-embedded.xml` | **Symbol library** with all 618 symbols (451 markers, 71 fills, 96 lines). The graphics are embedded, so it works offline and does not depend on any URL. **Style Manager → Import/Export → Import Items**. Tagged `BGS symbols`, `BGS ornaments`, `BGS line styles` and by classification. |
| `bgs-symbology-linked.xml` | The same library, with graphics referenced by URL from the published site. Smaller, but needs network access. Download it from the published site (`<site>/v3/styles/qgis/`): the copy in this folder has relative paths (see below). |
| `bgs_symbols.qml` | Categorised **layer style** for point layers with a `ref` attribute (e.g. `ALV`). Structural symbols rotate by the `rotation` attribute. |
| `bgs_ornaments.qml` | Categorised style for polygon layers with a `ref` attribute (e.g. `LMST`). Pattern only: add a coloured fill underneath (duplicate the layer, or add a simple fill symbol layer). |
| `bgs_line_styles.qml` | Categorised style for line layers with an `id` attribute (e.g. `fault_thrust_observed`). |

Sizes are in millimetres at the BGS standard (symbols 3 mm body, as for 1:25 000 and smaller). Line styles use QGIS's *raster line* symbol layer, which needs QGIS 3.24 or later. It repeats a 4× PNG tile along the line, which is the same approach MapLibre takes.

If your layer stores the code in a differently named attribute, load the `.qml` and then pick that attribute as the **Value** in Layer Properties → Symbology. The categories match on the codes, not the attribute name.

## GeoServer (`GeoServer/`)

| File | Symbolizer |
|---|---|
| `bgs_symbols.sld` | `PointSymbolizer` + `ExternalGraphic` (SVG), one rule per `ref`; `Rotation` from `rotation` for structural symbols |
| `bgs_ornaments.sld` | `PolygonSymbolizer` + `GraphicFill` with the seamless tile |
| `bgs_line_styles.sld` | `LineSymbolizer` + `GraphicStroke` with the line tile |

SLD 1.0. **The copies in this folder use paths relative to where they are published** (`../../symbols/svg/ALV.svg` from `v3/styles/geoserver/`), so the repository names no host and survives being transferred. The copies on the published site (`<site>/v3/styles/geoserver/`) have absolute URLs, written by the GitHub or GitLab Pages job; use those with GeoServer, which fetches and caches the graphics. To make absolute copies for another host, or SLDs keyed on other attribute names, run this in a throwaway copy of the repository: `python3 tools/make_web_styles.py . --base-url https://your.host/symbology/v3 [--symbol-field bgs_ref --line-field line_style]`. To keep GeoServer self-contained instead, copy the published `v3` tree into the GeoServer data directory and use the relative SLDs, which then find the SVGs next to them.

**Status:** QGIS 3.34 loads all three SLDs and renders the point and fill rules with graphics fetched over HTTP. QGIS's SLD importer does not support `GraphicStroke` with an external graphic, so it draws the line rules as plain lines. **These SLDs have not been tested in GeoServer itself.** Check them on a test layer before using them in production WMS.

## MapLibre

Use the sprite (see [`../Sprites`](../Sprites)). The demo page [`../docs/index.html`](../docs/index.html) is a complete working style.

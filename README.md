## BGS Cartographic Symbols

The BGS standard geological map symbology (point symbols, area ornaments and line styles) as reusable SVG files, catalogues, MapLibre sprites and GIS styles, hosted as static files for anyone to use. The layout follows the [OS GeoDataViz Toolkit](https://github.com/OrdnanceSurvey/GeoDataViz-Toolkit).

Everything here was extracted from:

> Mawer C H. 2002. *Cartographic standard geological symbol index. Version 3.* British Geological Survey Research Report RR/01/01. ISBN 0 85272 402 0. © NERC 2002.

**▶ Live MapLibre demo**: every symbol, ornament and line style drawn on a made-up island (*Isle of Mawer*, in the Celtic Sea). GitHub Pages publishes it at `https://<owner>.github.io/<repo>/v3/`. Open it from **Deployments → github-pages** in this repository's sidebar, which always points at the current address.

![MapLibre demo: BGS ornaments, line styles and symbols on a fictional island](img/demo.jpg)

| | Count | Folder | Formats |
|---|---:|---|---|
| Point symbols | 451 | [Symbols](Symbols) | SVG at BGS standard size, 24 px and 48 px SVG icons, CSV/JSON catalogue |
| Area ornaments | 71 | [Area-Ornaments](Area-Ornaments) | SVG swatch and seamless repeat tile, CSV/JSON |
| Line styles | 96 | [Line-Styles](Line-Styles) | SVG swatch, repeat tile and 4× PNG, CSV/JSON |
| MapLibre sprite | 618 images | [Sprites](Sprites) | `bgs-symbology[@2x].json/png` |
| GIS styles | | [Styles](Styles) | QGIS symbol libraries and layer styles, GeoServer SLD |

## Using the symbology

Everything is published as static files under one versioned URL, `<site>/v3/`, with a machine-readable manifest at `<site>/v3/index.json`:

```
<site>/v3/index.json                       manifest: every URL template, catalogue and style below
<site>/v3/sprites/bgs-symbology[@2x].json|png        MapLibre / Mapbox sprite
<site>/v3/symbols/svg/{REF}.svg            symbols at BGS standard size (also svg-24px/, svg-48px/)
<site>/v3/ornaments/tile/{REF}.svg         seamless fill tiles (swatch/ = as printed)
<site>/v3/lines/tile/{id}.svg              line repeat tiles (png/ = 4× PNG, swatch/ = as printed)
<site>/v3/{symbols,ornaments,lines}/*.json|csv       catalogues
<site>/v3/styles/geoserver/*.sld           GeoServer styles
<site>/v3/styles/qgis/*.xml|*.qml          QGIS symbol libraries and layer styles
<site>/v3/                                 the MapLibre demo
```

| Client | Use |
|---|---|
| MapLibre GL / Mapbox GL | `"sprite": "<site>/v3/sprites/bgs-symbology"`, image names `sym-{REF}`, `orn-{REF}`, `line-{id}`. See [Sprites](Sprites) for a minimal style and [`docs/index.html`](docs/index.html) for the demo. |
| OpenLayers | MapLibre styles via `ol-mapbox-style`, or `ol/style/Icon` with `symbols/svg/{REF}.svg` |
| Leaflet | `L.icon({ iconUrl: '<site>/v3/symbols/svg/ALV.svg' })` |
| QGIS | `styles/qgis/bgs-symbology-embedded.xml` (Style Manager → Import) or the `.qml` layer styles. See [Styles](Styles). |
| GeoServer (WMS/WMTS) | upload `styles/geoserver/*.sld`; GeoServer fetches the SVGs from the URLs inside |
| ArcGIS Pro | import the SVGs from `symbols/svg/` into a style (`.stylx`) |
| Anything else | read `index.json` and fill in the URL templates |

**Names and paths are stable.** Treat the REF codes, line style ids, sprite image names and file paths as an interface: they will not be renamed within `v3`. "v3" is the edition of the BGS standard. A future edition would be published alongside as `v4`, so existing maps keep working. The line style ids are slugs of the printed descriptions (the report gives line styles no codes); they are not official BGS codes.

The demo data (`docs/data/*.geojson`) is **entirely fictional**.

## Symbols

Point symbols are grouped as in the report: Drift (artificial, mass-movement, aeolian, organic, fluvial and river terraces, lacustrine, marine, raised marine, glacial, landform, and so on), Rock, Structural (bedding, cleavage, foliation, linear structures, igneous, folds, faults) and Other.

The report's symbols are glyphs in seven embedded symbol fonts. They were converted straight from the font outlines, so they are exact vectors, not traces. The BGS standard size is kept: the average symbol body is 3 mm at 1:25 000 and smaller scales, and 4 mm at 1:10 000.

_[Symbols catalogue →](Symbols)_

## Area ornaments

Fill patterns for lithologies and overprints (limestone, sandstone, made ground, stipples in five colours, and so on). Each comes as the printed swatch and as a **repeat tile** for fills. Where the pattern is regular, its period was measured and the tile repeats exactly. The irregular, hand-placed patterns have been made seamless by wrapping marks across the tile edges. Three dense rubble and marble textures are plain crops and show a faint seam (see the folder README).

_[Area ornaments catalogue →](Area-Ornaments)_

## Line styles

Boundaries, faults, fold axial traces, coal and marine bands, glacial and landform features. Each comes as the printed swatch and as a repeat tile for `line-pattern`.

_[Line styles catalogue →](Line-Styles)_

## Hosting

This repository publishes itself; no tile server or build step is needed beyond copying files:

- **GitHub Pages**: `.github/workflows/pages.yml` deploys on every push to `main`. Enable it once: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
- **GitLab Pages**: `.gitlab-ci.yml` deploys from the default branch of a GitLab copy or mirror.

**Nothing in the repository names its owner or host.** The SLDs, the QGIS linked library and `index.json` are committed with relative paths. On deploy, each job writes absolute URLs into the published copies only, using the site address its platform reports (`actions/configure-pages` on GitHub, `CI_PAGES_URL` on GitLab). So a transfer, a rename, a mirror or a custom domain needs no code change.

To host it anywhere else:

```bash
python3 tools/make_web_styles.py . --base-url https://your.host/symbology/v3   # in a throwaway copy: rewrites files in place
tools/assemble_site.sh /path/to/webroot/symbology                            # or preview: tools/assemble_site.sh && python3 -m http.server -d _site 8000
```

Any static host works if it provides:

- **CORS**: `Access-Control-Allow-Origin: *`. Browser map clients on other domains fetch the sprite and SVGs with `fetch()`, and fail without it. GitHub Pages sends this header.
- **Content types**: `image/svg+xml`, `application/json`, `application/geo+json`, `text/csv`. QGIS and browsers refuse SVG served as `text/plain` or `application/octet-stream`.
- **Stable URLs**: SLDs, QGIS linked libraries and other people's styles hard-code them.

## Caveats

- This reproduces a **2002** standard (version 3). Check it is still the current BGS standard before using it for production maps.
- Descriptions are as printed, including the report's spellings (e.g. "recumbant", "grandiorite").
- The report itself is inconsistent in a few places: two symbols disagree between its sections 2.1 and 2.2, and horizontal and inclined flow jointing share one glyph. These are listed in [Symbols](Symbols#source-inconsistencies).
- Pure black replaces the report's rich black (`#231f20`). Spot colours (cyan `#0091d6`, magenta `#ec008c`, orange `#f36f51`, yellow `#ffe800`, brown `#c38957`) are as printed in the PDF, which may not exactly match the original print specification.
- Repeat tiles are derived artwork. See the Area-Ornaments and Line-Styles READMEs for how each one was made and which are approximate.
- The GeoServer SLDs have been checked in QGIS but not yet in GeoServer itself.

The assets are generated from the report by a separate build pipeline. To report a problem with a symbol, open an issue here.

## Licence

**To be confirmed.** The symbology and source report are © NERC 2002 (now UKRI). See [LICENCE.md](LICENCE.md).

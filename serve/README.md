# Serving the symbology

Everything is static files. No tile server is needed. `scripts/assemble_site.sh` builds one tree, and both GitHub Pages and the container here publish it unchanged:

```
<base>/v3/index.json                       manifest: every URL template, catalogue and style below
<base>/v3/sprites/bgs-symbology[@2x].json|png        MapLibre / Mapbox sprite
<base>/v3/symbols/svg/{REF}.svg            symbols at BGS standard size (also svg-24px/, svg-48px/)
<base>/v3/ornaments/tile/{REF}.svg         seamless fill tiles (swatch/ = as printed)
<base>/v3/lines/tile/{id}.svg              line repeat tiles (png/ = 4x PNG, swatch/ = as printed)
<base>/v3/{symbols,ornaments,lines}/*.json|csv       catalogues
<base>/v3/styles/geoserver/*.sld           GeoServer styles (graphics referenced by URL)
<base>/v3/styles/qgis/*.xml|*.qml          QGIS symbol libraries and layer styles
<base>/v3/                                 MapLibre demo
```

`v3` is the edition of the BGS standard (RR/01/01 version 3). If BGS issues a new edition, publish it alongside as `v4` so existing maps and styles keep working.

## Which client uses what

| Client | Use |
|---|---|
| MapLibre GL / Mapbox GL | `"sprite": "<base>/v3/sprites/bgs-symbology"` and image names `sym-REF`, `orn-REF`, `line-id` |
| OpenLayers | MapLibre styles via `ol-mapbox-style`, or `ol/style/Icon` with `symbols/svg/{REF}.svg` |
| Leaflet | `L.icon({ iconUrl: '<base>/v3/symbols/svg/ALV.svg' })` |
| GeoServer (WMS/WMTS) | upload `styles/geoserver/*.sld`; GeoServer fetches the SVGs from the URLs inside |
| QGIS | `styles/qgis/bgs-symbology-embedded.xml` (Style Manager → Import) or the `.qml` layer styles |
| ArcGIS Pro | import the SVGs from `symbols/svg/` into a style (`.stylx`) |
| Anything else | read `index.json` and fill in the URL templates |

## Requirements for any host

- **CORS**: `Access-Control-Allow-Origin: *`. Browser map clients on other domains fetch the sprite JSON/PNG and SVGs with `fetch()`, and fail without it. GitHub Pages sends this header already.
- **Content types**: `image/svg+xml`, `application/json`, `application/geo+json`, `text/csv`. QGIS and browsers refuse SVG served as `text/plain` or `application/octet-stream`.
- **Stable versioned URLs**: SLDs, QGIS "linked" libraries and other people's styles hard-code these URLs.
- **Base URL**: the SLDs, `index.json` and the QGIS linked library contain absolute URLs. Regenerate them for your host:
  `python3 scripts/make_web_styles.py . --base-url https://your.host/symbology/v3`. The Docker build and the Pages workflow do this automatically.

## Option 1: GitHub Pages

`.github/workflows/pages.yml` publishes to `https://<owner>.github.io/<repo>/v3/` on every push to `main`. Enable it once under **Settings → Pages → Source: GitHub Actions**.

## Option 2: container (nginx)

`serve/Dockerfile` builds a small non-root nginx image (`nginxinc/nginx-unprivileged`, port 8080) that serves the tree under `/symbology/v3/` with the headers above, gzip and cache headers (images cached for 1 day, catalogues and JSON for 5 minutes, errors not cached), plus `/healthz`.

```bash
docker build -f serve/Dockerfile --build-arg BASE_URL=https://symbology.example.org/symbology/v3 -t bgs-symbology .
docker run --rm -p 8080:8080 bgs-symbology
open http://localhost:8080/symbology/v3/
```

`.github/workflows/image.yml` builds and pushes `ghcr.io/<owner>/<repo>` when you push a `v*` tag or run the workflow by hand (Actions → Build serving image → Run workflow). Set the repository variable `SYMBOLOGY_BASE_URL` to the public URL first.

### Kubernetes

`serve/k8s/` is a kustomize base: Deployment (2 replicas, read-only root filesystem, non-root, probes), Service and Ingress (path `/symbology`). Set the image, namespace and host, then:

```bash
kubectl apply -k serve/k8s
```

## Option 3: any existing web server or object storage

Copy the output of `scripts/assemble_site.sh` into place and apply the same headers. `nginx/default.conf` and `nginx/symbology-headers.conf` are the reference config.

## Do I need Martin?

Not for this. Martin is a tile server. It earns its place when you are also serving vector tiles (from PostGIS, PMTiles or MBTiles) and want sprites built on request from a folder of SVGs, or glyphs from TTF fonts. These sprites are prebuilt, and the demo style draws no text labels, so it needs no glyphs. If you add labels to a MapLibre style later, add a `"glyphs"` URL pointing at a set of PBF font ranges. Those are static files too.

## Testing what was checked

- `nginx -t` passes with this config. Headers, content types, gzip, redirects, CORS preflight and 404 caching were checked with curl. nginx 1.24 was run natively because no Docker daemon was available; the Docker build itself was not run.
- `scripts/check_qgis_styles.py` renders the demo data in QGIS 3.34 with the QML styles, the SLDs (graphics fetched from the local nginx) and both symbol libraries.
- The SLDs were **not** tested in GeoServer itself. QGIS parses them, but QGIS's SLD importer draws the `GraphicStroke` line styles as plain lines. Point and fill rules render correctly in QGIS.

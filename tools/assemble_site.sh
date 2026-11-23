#!/usr/bin/env bash
# Assemble the published static tree (used by the GitHub Pages and GitLab Pages jobs).
#
#   <out>/index.html          -> redirects to v3/
#   <out>/v3/                 MapLibre demo (index.html, data/) + index.json manifest
#   <out>/v3/sprites/         bgs-symbology[@2x].json/png
#   <out>/v3/symbols/         svg/, svg-24px/, svg-48px/, symbols.json, symbols.csv
#   <out>/v3/ornaments/       swatch/, tile/, ornaments.json, ornaments.csv
#   <out>/v3/lines/           swatch/, tile/, png/, lines.json, lines.csv
#   <out>/v3/styles/          geoserver/*.sld, qgis/*.xml|*.qml
#
# "v3" is the edition of the BGS standard (RR/01/01 version 3). A future edition would be
# published alongside as v4 so existing maps keep working.
#
# Usage: [REPO_URL=https://host/owner/repo] tools/assemble_site.sh [out_dir]      (default: _site)
# Preview: tools/assemble_site.sh && python3 -m http.server -d _site 8000
#
# REPO_URL (optional) is written to v3/site.json; the demo links to it as "Repository" (no link if unset). The CI
# jobs pass the URL of whichever repository they run in, so nothing here names an owner.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; OUT="${1:-_site}"; V="$OUT/v3"
rm -rf "$OUT"; mkdir -p "$V"/{sprites,symbols,ornaments,lines,styles}
cp -r "$ROOT/docs/." "$V/"
cp "$ROOT"/Sprites/bgs-symbology*.json "$ROOT"/Sprites/bgs-symbology*.png "$V/sprites/"
cp -r "$ROOT/Symbols/svg" "$ROOT/Symbols/svg-24px" "$ROOT/Symbols/svg-48px" "$ROOT"/Symbols/symbols.{json,csv} "$V/symbols/"
cp -r "$ROOT/Area-Ornaments/swatch" "$ROOT/Area-Ornaments/tile" "$ROOT"/Area-Ornaments/ornaments.{json,csv} "$V/ornaments/"
cp -r "$ROOT/Line-Styles/swatch" "$ROOT/Line-Styles/tile" "$ROOT/Line-Styles/png" "$ROOT"/Line-Styles/lines.{json,csv} "$V/lines/"
mkdir -p "$V/styles/geoserver" "$V/styles/qgis"
cp "$ROOT"/Styles/GeoServer/*.sld "$V/styles/geoserver/"
cp "$ROOT"/Styles/QGIS/*.xml "$ROOT"/Styles/QGIS/*.qml "$V/styles/qgis/"
cat > "$OUT/index.html" <<'HTML'
<!DOCTYPE html><meta charset="utf-8"><title>BGS Cartographic Symbols</title>
<meta http-equiv="refresh" content="0; url=v3/"><a href="v3/">BGS Cartographic Symbols (v3)</a>
HTML
python3 -c 'import json, sys; json.dump({"repository": sys.argv[1] or None}, open(sys.argv[2], "w"))' "${REPO_URL:-}" "$V/site.json"
touch "$OUT/.nojekyll"
echo "Site assembled in $OUT"

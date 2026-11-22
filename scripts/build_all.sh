#!/usr/bin/env bash
# Rebuild every asset in this repository from the source PDF.
# Usage: [BASE_URL=https://host/path/v3] scripts/build_all.sh [path/to/RR01001.pdf]
# Leave BASE_URL unset for the committed files (relative paths); publishing sets it.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; ROOT="$(dirname "$HERE")"
PDF="${1:-$ROOT/source/RR01001.pdf}"
TMP="$(mktemp -d)"
python3 -I "$HERE/parse_symbols.py" "$PDF" "$TMP/parsed.json"
rm -rf "$ROOT/Symbols/svg" "$ROOT/Symbols/svg-24px" "$ROOT/Symbols/svg-48px"
python3 -I "$HERE/build_symbols.py" "$PDF" "$TMP/parsed.json" "$ROOT/Symbols"
rm -rf "$ROOT/Area-Ornaments/swatch" "$ROOT/Area-Ornaments/tile" "$ROOT/Line-Styles/swatch" "$ROOT/Line-Styles/tile"
python3 -I "$HERE/extract_patterns.py" "$PDF" "$ROOT"
python3 -I "$HERE/wrap_tiles.py" "$ROOT/Area-Ornaments"
mkdir -p "$ROOT/Sprites"
python3 -I "$HERE/build_sprites.py" "$ROOT"
python3 -I "$HERE/make_demo_data.py" "$ROOT"
# QGIS styles need PyQGIS; set QGIS_PYTHON if it is not python3.12 (Ubuntu's python3-qgis)
QGIS_PYTHON="${QGIS_PYTHON:-python3.12}"
if QT_QPA_PLATFORM=offscreen "$QGIS_PYTHON" -c "import qgis.core" 2>/dev/null; then
  QT_QPA_PLATFORM=offscreen "$QGIS_PYTHON" "$HERE/make_qgis_styles.py" "$ROOT"
else
  echo "PyQGIS not found: keeping the committed Styles/QGIS files"
fi
# SLDs, index.json and the QGIS linked library: relative paths unless BASE_URL is set.
# Commit them relative, so nothing in the repository names its owner or host.
python3 -I "$HERE/make_web_styles.py" "$ROOT" ${BASE_URL:+--base-url "$BASE_URL"}
python3 -I "$HERE/make_readmes.py" "$ROOT"
rm -rf "$TMP"
echo "Done."

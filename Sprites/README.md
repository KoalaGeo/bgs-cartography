# Sprites

A single [MapLibre](https://maplibre.org/maplibre-style-spec/sprite/) (and Mapbox GL) sprite containing every symbol, ornament tile and line tile:

| File | |
|---|---|
| `bgs-symbology.json` / `.png` | 1× sprite |
| `bgs-symbology@2x.json` / `@2x.png` | 2× sprite for high-DPI screens |

## Image names

| Prefix | Use with | Example |
|---|---|---|
| `sym-{REF}` | `icon-image` | `sym-ALV` (Alluvium) |
| `orn-{REF}` | `fill-pattern` | `orn-LMST` (Limestone) |
| `line-{id}` | `line-pattern` | `line-fault_thrust_observed` |

## Sizes

- **Symbols**: drawn to a common scale where the Alluvium symbol body is 16 px wide at 1×, about BGS's 4 mm (1:10 000) at 96 dpi. Scale with `icon-size`.
- **Ornament tiles**: 1 pt in the report = 1.333 px at 1×. Tile sizes are rounded to whole pixels, a scaling of under 1%, so the repeat stays seamless.
- **Line tiles**: same scale. Tile height is even, so the centre line sits on the geometry. Set `line-width` to the tile height (the `maplibre_line_width_px` column in [`../Line-Styles/lines.csv`](../Line-Styles/lines.csv)) to draw at printed size.

## Minimal MapLibre style

```js
const style = {
  version: 8,
  sprite: 'https://koalageo.github.io/bgs-cartography/v3/sprites/bgs-symbology', // must be an absolute URL
  sources: { geo: { type: 'geojson', data: 'my-geology.geojson' } },
  layers: [
    // colour fill, then the ornament on top (tiles are transparent)
    { id: 'fill',    type: 'fill', source: 'geo', filter: ['==', ['geometry-type'], 'Polygon'], paint: { 'fill-color': ['get', 'colour'] } },
    { id: 'pattern', type: 'fill', source: 'geo', filter: ['==', ['geometry-type'], 'Polygon'], paint: { 'fill-pattern': ['concat', 'orn-', ['get', 'ornament']] } },
    { id: 'lines',   type: 'line', source: 'geo', filter: ['==', ['geometry-type'], 'LineString'],
      paint: { 'line-pattern': ['concat', 'line-', ['get', 'line_style']], 'line-width': ['get', 'line_width_px'] } },
    { id: 'points',  type: 'symbol', source: 'geo', filter: ['==', ['geometry-type'], 'Point'],
      layout: { 'icon-image': ['concat', 'sym-', ['get', 'ref']], 'icon-rotate': ['get', 'strike'],
                'icon-rotation-alignment': 'map', 'icon-allow-overlap': true } }
  ]
};
```

The full working example is in [`../docs/index.html`](../docs/index.html).

Rebuild with `scripts/build_sprites.py` (it is run by `scripts/build_all.sh`).

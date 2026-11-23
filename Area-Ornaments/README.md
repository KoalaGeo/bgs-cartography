# Area ornaments

71 area ornaments (fill patterns) from section 3 of BGS RR/01/01, extracted as vector SVG from the PDF drawing operators.

## Files

| Path | Contents |
|---|---|
| `swatch/{REF}.svg` | The swatch exactly as printed in the report. |
| `tile/{REF}.svg` | A repeat tile for use as a fill pattern (transparent background, so a colour fill can sit underneath). |
| `ornaments.csv`, `ornaments.json` | Catalogue: reference name, description, colours, tile size and how the tile was made. |
| [`../Sprites/`](../Sprites) | MapLibre sprite: image name `orn-{REF}`, use with `fill-pattern`. |

## How the repeat tiles were made

- **Exact repeat (55)**: the repeat period was measured from the swatch by autocorrelation, and the tile is one period cropped from the vector artwork. These tile seamlessly.
- **Wrapped marks (13)**: the hand-placed, irregular patterns (sand, igneous, lava, breccia and so on) have no repeat. Each mark whose centre falls inside the tile is kept whole and copied across the opposite edge, so the tile is seamless but the marks near its edges are re-arranged relative to the printed swatch.
- **Cropped swatch (3)**: dense irregular tessellations (coursed rubble, random rubble, marble), where wrapping would make stones overlap. These show a faint seam every tile width.

Black in the PDF is a rich black (`#231f20`); it has been output as pure black. *Marine overprint (white)* is printed black in the report and is reproduced as printed. Colour it white yourself if needed.

## Catalogue

| Swatch | Tile | Reference | Description | Tile |
|:---:|:---:|---|---|---|
| <img src="swatch/AGGLOM.svg" height="72" alt="AGGLOM swatch"> | <img src="tile/AGGLOM.svg" height="40" alt="AGGLOM tile"> | `AGGLOM` | Agglomerate | exact repeat |
| <img src="swatch/ANHY.svg" height="72" alt="ANHY swatch"> | <img src="tile/ANHY.svg" height="40" alt="ANHY tile"> | `ANHY` | Anhydrite | exact repeat |
| <img src="swatch/ARE_ST.svg" height="72" alt="ARE_ST swatch"> | <img src="tile/ARE_ST.svg" height="40" alt="ARE_ST tile"> | `ARE_ST` | Arenaceous seatearth | exact repeat |
| <img src="swatch/BLSND.svg" height="72" alt="BLSND swatch"> | <img src="tile/BLSND.svg" height="40" alt="BLSND tile"> | `BLSND` | Blown sand | exact repeat |
| <img src="swatch/BCLAY.svg" height="72" alt="BCLAY swatch"> | <img src="tile/BCLAY.svg" height="40" alt="BCLAY tile"> | `BCLAY` | Boulder clay | exact repeat |
| <img src="swatch/BREC.svg" height="72" alt="BREC swatch"> | <img src="tile/BREC.svg" height="40" alt="BREC tile"> | `BREC` | Breccia | wrapped marks |
| <img src="swatch/CALTUF.svg" height="72" alt="CALTUF swatch"> | <img src="tile/CALTUF.svg" height="40" alt="CALTUF tile"> | `CALTUF` | Calcareous tufa | exact repeat |
| <img src="swatch/CAT.svg" height="72" alt="CAT swatch"> | <img src="tile/CAT.svg" height="40" alt="CAT tile"> | `CAT` | Cataclastic rock | exact repeat |
| <img src="swatch/CHLK.svg" height="72" alt="CHLK swatch"> | <img src="tile/CHLK.svg" height="40" alt="CHLK tile"> | `CHLK` | Chalk | exact repeat |
| <img src="swatch/CLST.svg" height="72" alt="CLST swatch"> | <img src="tile/CLST.svg" height="40" alt="CLST tile"> | `CLST` | Claystone | wrapped marks |
| <img src="swatch/CONG.svg" height="72" alt="CONG swatch"> | <img src="tile/CONG.svg" height="40" alt="CONG tile"> | `CONG` | Conglomerate | exact repeat |
| <img src="swatch/CRSRB.svg" height="72" alt="CRSRB swatch"> | <img src="tile/CRSRB.svg" height="40" alt="CRSRB tile"> | `CRSRB` | Coursed rubble | cropped swatch |
| <img src="swatch/CR_RCK.svg" height="72" alt="CR_RCK swatch"> | <img src="tile/CR_RCK.svg" height="40" alt="CR_RCK tile"> | `CR_RCK` | Crushed rock | exact repeat |
| <img src="swatch/DIST.svg" height="72" alt="DIST swatch"> | <img src="tile/DIST.svg" height="40" alt="DIST tile"> | `DIST` | Disturbed ground | exact repeat |
| <img src="swatch/DOLOM.svg" height="72" alt="DOLOM swatch"> | <img src="tile/DOLOM.svg" height="40" alt="DOLOM tile"> | `DOLOM` | Dolomite | wrapped marks |
| <img src="swatch/FOUND.svg" height="72" alt="FOUND swatch"> | <img src="tile/FOUND.svg" height="40" alt="FOUND tile"> | `FOUND` | Foundered strata | exact repeat |
| <img src="swatch/STIPP.svg" height="72" alt="STIPP swatch"> | <img src="tile/STIPP.svg" height="40" alt="STIPP tile"> | `STIPP` | General overprint stipple | exact repeat |
| <img src="swatch/GNEISS.svg" height="72" alt="GNEISS swatch"> | <img src="tile/GNEISS.svg" height="40" alt="GNEISS tile"> | `GNEISS` | Gneiss | wrapped marks |
| <img src="swatch/GRAN.svg" height="72" alt="GRAN swatch"> | <img src="tile/GRAN.svg" height="40" alt="GRAN tile"> | `GRAN` | Granite | exact repeat |
| <img src="swatch/GRAN_V.svg" height="72" alt="GRAN_V swatch"> | <img src="tile/GRAN_V.svg" height="40" alt="GRAN_V tile"> | `GRAN_V` | Granite veining | wrapped marks |
| <img src="swatch/GR_SCH.svg" height="72" alt="GR_SCH swatch"> | <img src="tile/GR_SCH.svg" height="40" alt="GR_SCH tile"> | `GR_SCH` | Graphitic schist | exact repeat |
| <img src="swatch/GRAV.svg" height="72" alt="GRAV swatch"> | <img src="tile/GRAV.svg" height="40" alt="GRAV tile"> | `GRAV` | Gravel | exact repeat |
| <img src="swatch/GWACKE.svg" height="72" alt="GWACKE swatch"> | <img src="tile/GWACKE.svg" height="40" alt="GWACKE tile"> | `GWACKE` | Greywacke | wrapped marks |
| <img src="swatch/GYPS.svg" height="72" alt="GYPS swatch"> | <img src="tile/GYPS.svg" height="40" alt="GYPS tile"> | `GYPS` | Gypsum | exact repeat |
| <img src="swatch/IG.svg" height="72" alt="IG swatch"> | <img src="tile/IG.svg" height="40" alt="IG tile"> | `IG` | Igneous | wrapped marks |
| <img src="swatch/INFILL.svg" height="72" alt="INFILL swatch"> | <img src="tile/INFILL.svg" height="40" alt="INFILL tile"> | `INFILL` | Infilled ground | exact repeat |
| <img src="swatch/LASC.svg" height="72" alt="LASC swatch"> | <img src="tile/LASC.svg" height="40" alt="LASC tile"> | `LASC` | Landscaped ground | exact repeat |
| <img src="swatch/LAND.svg" height="72" alt="LAND swatch"> | <img src="tile/LAND.svg" height="40" alt="LAND tile"> | `LAND` | Landslip | exact repeat |
| <img src="swatch/LAVA.svg" height="72" alt="LAVA swatch"> | <img src="tile/LAVA.svg" height="40" alt="LAVA tile"> | `LAVA` | Lava | wrapped marks |
| <img src="swatch/LAV_TU.svg" height="72" alt="LAV_TU swatch"> | <img src="tile/LAV_TU.svg" height="40" alt="LAV_TU tile"> | `LAV_TU` | Lava and tuff | exact repeat |
| <img src="swatch/LMST.svg" height="72" alt="LMST swatch"> | <img src="tile/LMST.svg" height="40" alt="LMST tile"> | `LMST` | Limestone | exact repeat |
| <img src="swatch/LMST_D.svg" height="72" alt="LMST_D swatch"> | <img src="tile/LMST_D.svg" height="40" alt="LMST_D tile"> | `LMST_D` | Limestone bands | exact repeat |
| <img src="swatch/LMST_B.svg" height="72" alt="LMST_B swatch"> | <img src="tile/LMST_B.svg" height="40" alt="LMST_B tile"> | `LMST_B` | Limestone beds | exact repeat |
| <img src="swatch/LMST_T.svg" height="72" alt="LMST_T swatch"> | <img src="tile/LMST_T.svg" height="40" alt="LMST_T tile"> | `LMST_T` | Limestone thin bed partings | exact repeat |
| <img src="swatch/MADE.svg" height="72" alt="MADE swatch"> | <img src="tile/MADE.svg" height="40" alt="MADE tile"> | `MADE` | Made ground | exact repeat |
| <img src="swatch/MARBLE.svg" height="72" alt="MARBLE swatch"> | <img src="tile/MARBLE.svg" height="40" alt="MARBLE tile"> | `MARBLE` | Marble | cropped swatch |
| <img src="swatch/MARINE.svg" height="72" alt="MARINE swatch"> | <img src="tile/MARINE.svg" height="40" alt="MARINE tile"> | `MARINE` | Marine overprint (white) | exact repeat |
| <img src="swatch/LMST_M.svg" height="72" alt="LMST_M swatch"> | <img src="tile/LMST_M.svg" height="40" alt="LMST_M tile"> | `LMST_M` | Massive limestone | exact repeat |
| <img src="swatch/METASD.svg" height="72" alt="METASD swatch"> | <img src="tile/METASD.svg" height="40" alt="METASD tile"> | `METASD` | Metasediment | exact repeat |
| <img src="swatch/MIGM.svg" height="72" alt="MIGM swatch"> | <img src="tile/MIGM.svg" height="40" alt="MIGM tile"> | `MIGM` | Migmatisation | exact repeat |
| <img src="swatch/LMST_G.svg" height="72" alt="LMST_G swatch"> | <img src="tile/LMST_G.svg" height="40" alt="LMST_G tile"> | `LMST_G` | Mixed group with calc-schist/ limestone | exact repeat |
| <img src="swatch/MDST.svg" height="72" alt="MDST swatch"> | <img src="tile/MDST.svg" height="40" alt="MDST tile"> | `MDST` | Mudstone | exact repeat |
| <img src="swatch/LMST_O.svg" height="72" alt="LMST_O swatch"> | <img src="tile/LMST_O.svg" height="40" alt="LMST_O tile"> | `LMST_O` | Ooidal limestone | exact repeat |
| <img src="swatch/ST_BLK.svg" height="72" alt="ST_BLK swatch"> | <img src="tile/ST_BLK.svg" height="40" alt="ST_BLK tile"> | `ST_BLK` | Overprint stipple for various rock types Black | exact repeat |
| <img src="swatch/ST_CYN.svg" height="72" alt="ST_CYN swatch"> | <img src="tile/ST_CYN.svg" height="40" alt="ST_CYN tile"> | `ST_CYN` | Overprint stipple for various rock types Cyan | exact repeat |
| <img src="swatch/ST_MAG.svg" height="72" alt="ST_MAG swatch"> | <img src="tile/ST_MAG.svg" height="40" alt="ST_MAG tile"> | `ST_MAG` | Overprint stipple for various rock types Magenta | exact repeat |
| <img src="swatch/ST_OR.svg" height="72" alt="ST_OR swatch"> | <img src="tile/ST_OR.svg" height="40" alt="ST_OR tile"> | `ST_OR` | Overprint stipple for various rock types Orange | exact repeat |
| <img src="swatch/ST_YEL.svg" height="72" alt="ST_YEL swatch"> | <img src="tile/ST_YEL.svg" height="40" alt="ST_YEL tile"> | `ST_YEL` | Overprint stipple for various rock types Yellow | exact repeat |
| <img src="swatch/PEBBLE.svg" height="72" alt="PEBBLE swatch"> | <img src="tile/PEBBLE.svg" height="40" alt="PEBBLE tile"> | `PEBBLE` | Pebbles | exact repeat |
| <img src="swatch/PEG.svg" height="72" alt="PEG swatch"> | <img src="tile/PEG.svg" height="40" alt="PEG tile"> | `PEG` | Pegmatite or vein complexes | exact repeat |
| <img src="swatch/PELITE.svg" height="72" alt="PELITE swatch"> | <img src="tile/PELITE.svg" height="40" alt="PELITE tile"> | `PELITE` | Pelite | exact repeat |
| <img src="swatch/LMST_P.svg" height="72" alt="LMST_P swatch"> | <img src="tile/LMST_P.svg" height="40" alt="LMST_P tile"> | `LMST_P` | Pisoidal limestone | exact repeat |
| <img src="swatch/PSAMM.svg" height="72" alt="PSAMM swatch"> | <img src="tile/PSAMM.svg" height="40" alt="PSAMM tile"> | `PSAMM` | Psammite | wrapped marks |
| <img src="swatch/QUART.svg" height="72" alt="QUART swatch"> | <img src="tile/QUART.svg" height="40" alt="QUART tile"> | `QUART` | Quartzite | exact repeat |
| <img src="swatch/RNRBL.svg" height="72" alt="RNRBL swatch"> | <img src="tile/RNRBL.svg" height="40" alt="RNRBL tile"> | `RNRBL` | Random rubble | cropped swatch |
| <img src="swatch/RECL.svg" height="72" alt="RECL swatch"> | <img src="tile/RECL.svg" height="40" alt="RECL tile"> | `RECL` | Reclaimed ground | exact repeat |
| <img src="swatch/GNE_RW.svg" height="72" alt="GNE_RW swatch"> | <img src="tile/GNE_RW.svg" height="40" alt="GNE_RW tile"> | `GNE_RW` | Reworked gneisses | exact repeat |
| <img src="swatch/LMST_R.svg" height="72" alt="LMST_R swatch"> | <img src="tile/LMST_R.svg" height="40" alt="LMST_R tile"> | `LMST_R` | Rubbly limestone; poorly bedded | wrapped marks |
| <img src="swatch/SAND.svg" height="72" alt="SAND swatch"> | <img src="tile/SAND.svg" height="40" alt="SAND tile"> | `SAND` | Sand | wrapped marks |
| <img src="swatch/SNDST.svg" height="72" alt="SNDST swatch"> | <img src="tile/SNDST.svg" height="40" alt="SNDST tile"> | `SNDST` | Sandstone | exact repeat |
| <img src="swatch/LMST_S.svg" height="72" alt="LMST_S swatch"> | <img src="tile/LMST_S.svg" height="40" alt="LMST_S tile"> | `LMST_S` | Sandy limestone | wrapped marks |
| <img src="swatch/SHALE.svg" height="72" alt="SHALE swatch"> | <img src="tile/SHALE.svg" height="40" alt="SHALE tile"> | `SHALE` | Shale | exact repeat |
| <img src="swatch/SHMRL.svg" height="72" alt="SHMRL swatch"> | <img src="tile/SHMRL.svg" height="40" alt="SHMRL tile"> | `SHMRL` | Shell marl | exact repeat |
| <img src="swatch/SLTST.svg" height="72" alt="SLTST swatch"> | <img src="tile/SLTST.svg" height="40" alt="SLTST tile"> | `SLTST` | Siltstone | exact repeat |
| <img src="swatch/SLTMD.svg" height="72" alt="SLTMD swatch"> | <img src="tile/SLTMD.svg" height="40" alt="SLTMD tile"> | `SLTMD` | Silty mudstone | exact repeat |
| <img src="swatch/SLTSND.svg" height="72" alt="SLTSND swatch"> | <img src="tile/SLTSND.svg" height="40" alt="SLTSND tile"> | `SLTSND` | Silty sandstone | exact repeat |
| <img src="swatch/SALT.svg" height="72" alt="SALT swatch"> | <img src="tile/SALT.svg" height="40" alt="SALT tile"> | `SALT` | Sodium salt | exact repeat |
| <img src="swatch/TUFF.svg" height="72" alt="TUFF swatch"> | <img src="tile/TUFF.svg" height="40" alt="TUFF tile"> | `TUFF` | Tuff | exact repeat |
| <img src="swatch/TURB.svg" height="72" alt="TURB swatch"> | <img src="tile/TURB.svg" height="40" alt="TURB tile"> | `TURB` | Turbidite | wrapped marks |
| <img src="swatch/WORK.svg" height="72" alt="WORK swatch"> | <img src="tile/WORK.svg" height="40" alt="WORK tile"> | `WORK` | Worked ground | exact repeat |
| <img src="swatch/XENO.svg" height="72" alt="XENO swatch"> | <img src="tile/XENO.svg" height="40" alt="XENO tile"> | `XENO` | Xenoliths | exact repeat |

# Symbols

451 point symbols from section 2 of BGS Research Report RR/01/01 (*Cartographic standard geological symbol index*, version 3, 2002), grouped by the report's geological classification.

Each symbol was extracted as vector outlines directly from the font glyphs embedded in the PDF, so the shapes are exact rather than traced.

## Files

| Path | Contents |
|---|---|
| `svg/{REF}.svg` | Symbol at **BGS standard size**: the Alluvium symbol body is 3 mm (1:25 000 and smaller scales). Scale by 4/3 for 1:10 000 (4 mm). |
| `svg-24px/`, `svg-48px/` | Square icons, symbol fitted and centred (like the OS GeoDataViz icons). Not to a common scale. |
| `symbols.csv`, `symbols.json` | Catalogue: reference name, description, alternative descriptions from the A–Z index (2.2), classification, size, source page/glyph. |
| [`../Sprites/`](../Sprites) | MapLibre/Mapbox sprite: image name `sym-{REF}`. |

Reference names (`REF`) are the MicroStation cell names used in the report, e.g. `ALV` for Alluvium. Prefixes: ALV alluvial, BRK brickearth, GFL glaciofluvial, GLA glaciolacustrine, GL glacial, IGL interglacial, LAC lacustrine, MA marine, RM raised marine, RS rock, RT river terrace, S structural, SG sand and gravel.

Symbols are black. Structural symbols are normally rotated to strike; in MapLibre use `icon-rotate` with `icon-rotation-alignment: map`.

## Source inconsistencies

- `RT_SH` (Shepperton Gravel): Source inconsistency: section 2.1 labels this symbol 'SH', the A-Z index (2.2) labels it 'SHG'. This file follows 2.1.
- `S_HFJ` (Horizontal flow jointing): Source inconsistency: the report prints the same glyph for horizontal (S_HFJ) and inclined (S_IFJ) flow jointing.
- `S_IFJ` (Inclined flow jointing): Source inconsistency: the report prints the same glyph for horizontal (S_HFJ) and inclined (S_IFJ) flow jointing.
- `S_DIP` (Dip of igneous contact): Source inconsistency: printed at 16 pt in section 2.1 but at the standard 10 pt in the A-Z index (2.2). Drawn here at the standard size.

## Contents

- [Artificial Deposits](#artificial-deposits)
- [Mass-movement](#mass-movement)
- [Aeolian Deposits](#aeolian-deposits)
- [Organic Deposits](#organic-deposits)
- [Chemical/Organic Deposits](#chemicalorganic-deposits)
- [Fluvial Deposits](#fluvial-deposits)
- [Lacustrine Deposits](#lacustrine-deposits)
- [Marine Deposits](#marine-deposits)
- [Raised Marine Deposits](#raised-marine-deposits)
- [Interglacial](#interglacial)
- [Glacial Deposits](#glacial-deposits)
- [Miscellaneous Drift](#miscellaneous-drift)
- [Landform](#landform)
- [Rock Symbols](#rock-symbols)
- [Structural Symbols](#structural-symbols)
- [Other Symbols](#other-symbols)

## Artificial Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/ART_BP.svg" height="14" alt="ART_BP"> | `ART_BP` | Small area of made ground, backfilled pit | Made ground, backfilled pit, small area |
| <img src="svg/ART_AS.svg" height="14" alt="ART_AS"> | `ART_AS` | Small area of made ground, above surface | Made ground, above surface, small area |
| <img src="svg/ART_WG.svg" height="14" alt="ART_WG"> | `ART_WG` | Small area of worked ground | Worked ground, small area |
| <img src="svg/MSM_L.svg" height="14" alt="MSM_L"> | `MSM_L` | Small area of landslip | Landslip, small area |

## Mass-movement

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/BLOC.svg" height="14" alt="BLOC"> | `BLOC` | Blockfield |  |
| <img src="svg/COD.svg" height="17" alt="COD"> | `COD` | Coombe deposits | Coombe Deposits |
| <img src="svg/CWF.svg" height="18" alt="CWF"> | `CWF` | Clay-with-flints |  |
| <img src="svg/CWF_S.svg" height="18" alt="CWF_S"> | `CWF_S` | Sand in clay-with-flints |  |
| <img src="svg/DCON.svg" height="14" alt="DCON"> | `DCON` | Debris cone |  |
| <img src="svg/HEAD.svg" height="17" alt="HEAD"> | `HEAD` | Head or hillwash |  |
| <img src="svg/HEAD1.svg" height="17" alt="HEAD1"> | `HEAD1` | Head 1 |  |
| <img src="svg/HEAD2.svg" height="17" alt="HEAD2"> | `HEAD2` | Head 2 |  |
| <img src="svg/HEAD_R.svg" height="20" alt="HEAD_R"> | `HEAD_R` | Blanket head / regolith |  |
| <img src="svg/HEADBL.svg" height="25" alt="HEADBL"> | `HEADBL` | Head, Burton Lazars |  |
| <img src="svg/HEAD_C.svg" height="17" alt="HEAD_C"> | `HEAD_C` | Head, Colluvium |  |
| <img src="svg/HEAD_G.svg" height="17" alt="HEAD_G"> | `HEAD_G` | Gravelly head |  |
| <img src="svg/HEADLD.svg" height="26" alt="HEADLD"> | `HEADLD` | Head, Little Dalby |  |
| <img src="svg/HEADPH.svg" height="25" alt="HEADPH"> | `HEADPH` | Head, Pen Hill |  |
| <img src="svg/HEAD_S.svg" height="17" alt="HEAD_S"> | `HEAD_S` | Sandy head |  |
| <img src="svg/HEAD_V.svg" height="17" alt="HEAD_V"> | `HEAD_V` | Valley bottom head |  |
| <img src="svg/PBS.svg" height="14" alt="PBS"> | `PBS` | Pebbly clay and sand |  |
| <img src="svg/SCRE.svg" height="14" alt="SCRE"> | `SCRE` | Scree / talus | Talus / scree |
| <img src="svg/SCRE_I.svg" height="17" alt="SCRE_I"> | `SCRE_I` | Inactive scree / talus | Talus / inactive scree |

## Aeolian Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/BLS.svg" height="14" alt="BLS"> | `BLS` | Blown sand |  |
| <img src="svg/BLS_1.svg" height="16" alt="BLS_1"> | `BLS_1` | Blown sand, 1 |  |
| <img src="svg/BRK_.svg" height="14" alt="BRK_"> | `BRK_` | Brickearth |  |
| <img src="svg/BRK_DA.svg" height="19" alt="BRK_DA"> | `BRK_DA` | Brickearth, Dartford Silt | Dartford Silt (brickearth) |
| <img src="svg/BRK_ES.svg" height="19" alt="BRK_ES"> | `BRK_ES` | Brickearth, Enfield Silt | Enfield Silt (brickearth) |
| <img src="svg/BRK_IL.svg" height="19" alt="BRK_IL"> | `BRK_IL` | Brickearth, Ilford Silt | Ilford Silt (brickearth) |
| <img src="svg/BRK_LS.svg" height="19" alt="BRK_LS"> | `BRK_LS` | Brickearth, Langley Silt | Langley Silt (brickearth) |
| <img src="svg/BRK_WC.svg" height="19" alt="BRK_WC"> | `BRK_WC` | Brickearth, Wolston Clay | Wolston Clay (brickearth) |
| <img src="svg/LOESS.svg" height="16" alt="LOESS"> | `LOESS` | Loess |  |

## Organic Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/PEAT.svg" height="14" alt="PEAT"> | `PEAT` | Peat |  |
| <img src="svg/PEA_BA.svg" height="14" alt="PEA_BA"> | `PEA_BA` | Basin peat |  |
| <img src="svg/PEA_BL.svg" height="14" alt="PEA_BL"> | `PEA_BL` | Blanket peat |  |
| <img src="svg/PEA_FN.svg" height="14" alt="PEA_FN"> | `PEA_FN` | Fen peat |  |
| <img src="svg/PEA_H.svg" height="14" alt="PEA_H"> | `PEA_H` | Hill peat |  |
| <img src="svg/PEAT_N.svg" height="15" alt="PEAT_N"> | `PEAT_N` | Nordelph peat | Nordelph Peat |
| <img src="svg/PEAT_F.svg" height="14" alt="PEAT_F"> | `PEAT_F` | Peat flow |  |
| <img src="svg/PET_SF.svg" height="14" alt="PET_SF"> | `PET_SF` | Submerged forest |  |
| <img src="svg/DIAT.svg" height="14" alt="DIAT"> | `DIAT` | Diatomite |  |
| <img src="svg/DIAT_F.svg" height="14" alt="DIAT_F"> | `DIAT_F` | Diatomite, fluvial |  |
| <img src="svg/SLM.svg" height="14" alt="SLM"> | `SLM` | Shell marl |  |

## Chemical/Organic Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/ORE.svg" height="14" alt="ORE"> | `ORE` | Bog iron ore |  |
| <img src="svg/TUFA_C.svg" height="14" alt="TUFA_C"> | `TUFA_C` | Calcareous tufa |  |
| <img src="svg/TUFA.svg" height="14" alt="TUFA"> | `TUFA` | Tufa |  |

## Fluvial Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/ALV_FN.svg" height="14" alt="ALV_FN"> | `ALV_FN` | Alluvial fan deposits |  |
| <img src="svg/ALV_FG.svg" height="14" alt="ALV_FG"> | `ALV_FG` | Alluvial fan deposits, gravel |  |
| <img src="svg/ALV.svg" height="14" alt="ALV"> | `ALV` | Alluvium |  |
| <img src="svg/ALV_1.svg" height="14" alt="ALV_1"> | `ALV_1` | Alluvium, 1 |  |
| <img src="svg/ALV_C.svg" height="14" alt="ALV_C"> | `ALV_C` | Alluvium, clay |  |
| <img src="svg/ALV_SG.svg" height="14" alt="ALV_SG"> | `ALV_SG` | Alluvium, sand and gravel |  |
| <img src="svg/RT_A1.svg" height="14" alt="RT_A1"> | `RT_A1` | Arun Terrace Deposits, 1st |  |

### River Terraces

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/RT_A2.svg" height="14" alt="RT_A2"> | `RT_A2` | Arun Terrace Deposits, 2nd |  |
| <img src="svg/RT_A3.svg" height="14" alt="RT_A3"> | `RT_A3` | Arun Terrace Deposits, 3rd |  |
| <img src="svg/RT_A4.svg" height="14" alt="RT_A4"> | `RT_A4` | Arun Terrace Deposits, 4th |  |
| <img src="svg/RT_A5.svg" height="14" alt="RT_A5"> | `RT_A5` | Arun Terrace Deposits, 5th |  |
| <img src="svg/RT_A6.svg" height="14" alt="RT_A6"> | `RT_A6` | Arun Terrace Deposits, 6th |  |
| <img src="svg/RT_A7.svg" height="14" alt="RT_A7"> | `RT_A7` | Arun Terrace Deposits, 7th |  |
| <img src="svg/RT_BDN.svg" height="14" alt="RT_BDN"> | `RT_BDN` | Balderton Sand and Gravel |  |
| <img src="svg/RT_B.svg" height="14" alt="RT_B"> | `RT_B` | Bank Farm Terrace |  |
| <img src="svg/RT_BS.svg" height="15" alt="RT_BS"> | `RT_BS` | Bassingfield Sand and Gravel |  |
| <img src="svg/RT_BC9.svg" height="14" alt="RT_BC9"> | `RT_BC9` | Beaconsfield Gravel |  |
| <img src="svg/RT_BG2.svg" height="14" alt="RT_BG2"> | `RT_BG2` | Beenham Grange Gravel |  |
| <img src="svg/RT_BS7.svg" height="14" alt="RT_BS7"> | `RT_BS7` | Beenham Stocks Gravel |  |
| <img src="svg/RT_BEE.svg" height="14" alt="RT_BEE"> | `RT_BEE` | Beeston Sand and Gravel |  |
| <img src="svg/RT_BEL.svg" height="14" alt="RT_BEL"> | `RT_BEL` | Belton Sand and Gravel |  |
| <img src="svg/RT_BIR.svg" height="14" alt="RT_BIR"> | `RT_BIR` | Birstall Sand and Gravel |  |
| <img src="svg/RT_BPG.svg" height="14" alt="RT_BPG"> | `RT_BPG` | Black Park Gravel |  |
| <img src="svg/RT_B3.svg" height="14" alt="RT_B3"> | `RT_B3` | Blackwater Terrace Deposits, 3rd |  |
| <img src="svg/RT_B4.svg" height="14" alt="RT_B4"> | `RT_B4` | Blackwater Terrace Deposits, 4th |  |
| <img src="svg/RT_BH.svg" height="14" alt="RT_BH"> | `RT_BH` | Boyn Hill Gravel |  |
| <img src="svg/RT_BW2.svg" height="14" alt="RT_BW2"> | `RT_BW2` | Bramley Wey Terrace Deposits, 2nd |  |
| <img src="svg/RT_BK8.svg" height="14" alt="RT_BK8"> | `RT_BK8` | Bucklebury Gravel |  |
| <img src="svg/RT_BKY.svg" height="14" alt="RT_BKY"> | `RT_BKY` | Brooksby Sand and Gravel |  |
| <img src="svg/RT_BN.svg" height="15" alt="RT_BN"> | `RT_BN` | Bunny Sand and Gravel |  |
| <img src="svg/RT_BTH.svg" height="14" alt="RT_BTH"> | `RT_BTH` | Bytham Sand and Gravel |  |
| <img src="svg/RT_CCG.svg" height="14" alt="RT_CCG"> | `RT_CCG` | Caesar's Camp Gravel |  |
| <img src="svg/ALV_CH.svg" height="21" alt="ALV_CH"> | `ALV_CH` | Cheltenham Sand and Gravel |  |
| <img src="svg/RT_CM.svg" height="14" alt="RT_CM"> | `RT_CM` | Combe Member | Combe Member (river terrace) |
| <img src="svg/RT_CY.svg" height="14" alt="RT_CY"> | `RT_CY` | Corbets Tey Gravel |  |
| <img src="svg/RT_DM1.svg" height="14" alt="RT_DM1"> | `RT_DM1` | Daylesford Member, 1st | Daylesford Member, 1st river terrace |
| <img src="svg/RT_DH.svg" height="14" alt="RT_DH"> | `RT_DH` | Dollis Hill Gravel |  |
| <img src="svg/ALV_DV.svg" height="14" alt="ALV_DV"> | `ALV_DV` | Dry valley deposits |  |
| <img src="svg/RT_EM.svg" height="14" alt="RT_EM"> | `RT_EM` | Eagle Moor Sand and Gravel |  |
| <img src="svg/RT_EC.svg" height="14" alt="RT_EC"> | `RT_EC` | Eggington Common Sand and Gravel |  |
| <img src="svg/RT_ET.svg" height="14" alt="RT_ET"> | `RT_ET` | Etwall Sand and Gravel |  |
| <img src="svg/RT_FG.svg" height="14" alt="RT_FG"> | `RT_FG` | Fen Sand and Gravel | Fen sand and gravel |
| <img src="svg/RT_FIN.svg" height="14" alt="RT_FIN"> | `RT_FIN` | Finsbury Gravel |  |
| <img src="svg/RT_FSG.svg" height="14" alt="RT_FSG"> | `RT_FSG` | Fluvial Sand and Gravel | Fluvial sand and gravel |
| <img src="svg/RT_FR.svg" height="14" alt="RT_FR"> | `RT_FR` | Freeland Member | Freeland Member river terrace |
| <img src="svg/RT_FUL.svg" height="14" alt="RT_FUL"> | `RT_FUL` | Fulbeck Sand and Gravel |  |
| <img src="svg/RT_GC.svg" height="14" alt="RT_GC"> | `RT_GC` | Gerrards Cross Gravel |  |
| <img src="svg/RT_GW1.svg" height="14" alt="RT_GW1"> | `RT_GW1` | Godalming Wey Deposits, 1st | Godalming Wey Deposits, 1st river terrace deposit |
| <img src="svg/RT_G1A.svg" height="14" alt="RT_G1A"> | `RT_G1A` | Godalming Wey Deposits, 1a | Godalming Wey Deposits, 1a river terrace deposit |
| <img src="svg/RT_G1B.svg" height="14" alt="RT_G1B"> | `RT_G1B` | Godalming Wey Deposits, 1b | Godalming Wey Deposits, 1b river terrace deposit |
| <img src="svg/RT_GW2.svg" height="14" alt="RT_GW2"> | `RT_GW2` | Godalming Wey Deposits, 2nd | Godalming Wey Deposits, 2nd river terrace deposit |
| <img src="svg/RT_GW3.svg" height="14" alt="RT_GW3"> | `RT_GW3` | Godalming Wey Deposits, 3rd | Godalming Wey Deposits, 3rd river terrace deposit |
| <img src="svg/RT_HA.svg" height="14" alt="RT_HA"> | `RT_HA` | Hackney Gravel |  |
| <img src="svg/RT_H4.svg" height="14" alt="RT_H4"> | `RT_H4` | Hanborough Member | Hanborough Member river terrace |
| <img src="svg/RT_HP.svg" height="14" alt="RT_HP"> | `RT_HP` | Holme Pierrepont Sand and Gravel |  |
| <img src="svg/RT_KP.svg" height="14" alt="RT_KP"> | `RT_KP` | Kempton Park Gravel |  |
| <img src="svg/RT_KN.svg" height="15" alt="RT_KN"> | `RT_KN` | Knighton Sand and Gravel |  |
| <img src="svg/RT_LG.svg" height="14" alt="RT_LG"> | `RT_LG` | Leaves Green Gravel |  |
| <img src="svg/RT_LN.svg" height="14" alt="RT_LN"> | `RT_LN` | Leen Sand and Gravel |  |
| <img src="svg/RT_H.svg" height="14" alt="RT_H"> | `RT_H` | Little Hereford River Terrace | Little Hereford river terrace |
| <img src="svg/RT_LH.svg" height="14" alt="RT_LH"> | `RT_LH` | Lynch Hill Gravel |  |
| <img src="svg/RT_N1.svg" height="14" alt="RT_N1"> | `RT_N1` | Northmoor Member | Northmoor Member river terrace |
| <img src="svg/RT_OcK.svg" height="14" alt="RT_OcK"> | `RT_OcK` | Ockbrook Sand and Gravel |  |
| <img src="svg/RT_RM1.svg" height="14" alt="RT_RM1"> | `RT_RM1` | Rissington Member | Rissington Member river terrace |
| <img src="svg/RT_AV1.svg" height="14" alt="RT_AV1"> | `RT_AV1` | River Avon Deposits, 1st | River Avon Deposits, 1st river terrace |
| <img src="svg/RT_AV2.svg" height="14" alt="RT_AV2"> | `RT_AV2` | River Avon Deposits, 2nd | River Avon Deposits, 2nd river terrace |
| <img src="svg/RT_S1.svg" height="14" alt="RT_S1"> | `RT_S1` | River Severn Deposits, 1st | River Severn Deposits, 1st river terrace |
| <img src="svg/RT_S2.svg" height="14" alt="RT_S2"> | `RT_S2` | River Severn Deposits, 2nd | River Severn Deposits, 2nd river terrace |
| <img src="svg/RT_S3.svg" height="14" alt="RT_S3"> | `RT_S3` | River Severn Deposits, 3rd | River Severn Deposits, 3rd river terrace |
| <img src="svg/RT01.svg" height="14" alt="RT01"> | `RT01` | River terrace deposits, 1st |  |
| <img src="svg/RT01A.svg" height="14" alt="RT01A"> | `RT01A` | River terrace deposits,1a |  |
| <img src="svg/RT01B.svg" height="14" alt="RT01B"> | `RT01B` | River terrace deposits,1b |  |
| <img src="svg/RT01C.svg" height="14" alt="RT01C"> | `RT01C` | River terrace deposits,1c |  |
| <img src="svg/RT01-2.svg" height="14" alt="RT01-2"> | `RT01-2` | River terrace deposits, 1st - 2nd |  |
| <img src="svg/RT02.svg" height="14" alt="RT02"> | `RT02` | River terrace deposits, 2nd |  |
| <img src="svg/RT02-3.svg" height="14" alt="RT02-3"> | `RT02-3` | River terrace deposits, 2nd - 3rd |  |
| <img src="svg/RT03.svg" height="14" alt="RT03"> | `RT03` | River terrace deposits, 3rd |  |
| <img src="svg/RT04.svg" height="14" alt="RT04"> | `RT04` | River terrace deposits, 4th |  |
| <img src="svg/RT05.svg" height="14" alt="RT05"> | `RT05` | River terrace deposits, 5th |  |
| <img src="svg/RT05-6.svg" height="14" alt="RT05-6"> | `RT05-6` | River terrace deposits, 5th - 6th |  |
| <img src="svg/RT06.svg" height="14" alt="RT06"> | `RT06` | River terrace deposits, 6th |  |
| <img src="svg/RT07.svg" height="14" alt="RT07"> | `RT07` | River terrace deposits, 7th |  |
| <img src="svg/RT08.svg" height="14" alt="RT08"> | `RT08` | River terrace deposits, 8th |  |
| <img src="svg/RT09.svg" height="14" alt="RT09"> | `RT09` | River terrace deposits, 9th |  |
| <img src="svg/RT10.svg" height="14" alt="RT10"> | `RT10` | River terrace deposits 10th | River terrace deposits, 10th |
| <img src="svg/RT11.svg" height="14" alt="RT11"> | `RT11` | River terrace deposits, 11th |  |
| <img src="svg/RT12.svg" height="14" alt="RT12"> | `RT12` | River terrace deposits, 12th |  |
| <img src="svg/RT13.svg" height="14" alt="RT13"> | `RT13` | River terrace deposits, 13th |  |
| <img src="svg/RT14.svg" height="14" alt="RT14"> | `RT14` | River terrace deposits, 14th |  |
| <img src="svg/RT15.svg" height="14" alt="RT15"> | `RT15` | River terrace deposits, 15th |  |
| <img src="svg/RT_U.svg" height="14" alt="RT_U"> | `RT_U` | River terrace deposits, undifferentiated |  |
| <img src="svg/RT_WF.svg" height="14" alt="RT_WF"> | `RT_WF` | River Worfe Deposits, undifferentiated |  |
| <img src="svg/RT_WF1.svg" height="14" alt="RT_WF1"> | `RT_WF1` | River Worfe Terrace Deposits, 1st |  |
| <img src="svg/RT_WF2.svg" height="14" alt="RT_WF2"> | `RT_WF2` | River Worfe Terrace Deposits, 2nd |  |
| <img src="svg/RT_WY1.svg" height="14" alt="RT_WY1"> | `RT_WY1` | River Wye Terrace Deposits, 1st |  |
| <img src="svg/RT_WY2.svg" height="14" alt="RT_WY2"> | `RT_WY2` | River Wye Terrace Deposits, 2nd |  |
| <img src="svg/RT_RO1.svg" height="14" alt="RT_RO1"> | `RT_RO1` | Rother Terrace Deposits, 1st |  |
| <img src="svg/RT_RO2.svg" height="14" alt="RT_RO2"> | `RT_RO2` | Rother Terrace Deposits, 2nd |  |
| <img src="svg/RT_RO3.svg" height="14" alt="RT_RO3"> | `RT_RO3` | Rother Terrace Deposits, 3rd |  |
| <img src="svg/RT_RO4.svg" height="14" alt="RT_RO4"> | `RT_RO4` | Rother Terrace Deposits, 4th |  |
| <img src="svg/RT_RO5.svg" height="14" alt="RT_RO5"> | `RT_RO5` | Rother Terrace Deposits, 5th |  |
| <img src="svg/RT_ROU.svg" height="14" alt="RT_ROU"> | `RT_ROU` | Rother Terrace Deposits, undifferentiated |  |
| <img src="svg/RT_S.svg" height="14" alt="RT_S"> | `RT_S` | Shakenhurst Terrace |  |
| <img src="svg/RT_SH.svg" height="14" alt="RT_SH"> | `RT_SH` | Shepperton Gravel |  |
| <img src="svg/RT_SM1.svg" height="14" alt="RT_SM1"> | `RT_SM1` | Sherborne Member, 1st terrace |  |
| <img src="svg/RT_SM2.svg" height="14" alt="RT_SM2"> | `RT_SM2` | Sherborne Member, 2nd terrace |  |
| <img src="svg/RT_SL6.svg" height="14" alt="RT_SL6"> | `RT_SL6` | Silchester Gravel |  |
| <img src="svg/RT_SR2.svg" height="14" alt="RT_SR2"> | `RT_SR2` | Summertown Radley Member, 2nd terrace |  |
| <img src="svg/RT_SHG.svg" height="14" alt="RT_SHG"> | `RT_SHG` | Surrey Hill Gravel |  |
| <img src="svg/RT_SYS.svg" height="15" alt="RT_SYS"> | `RT_SYS` | Syston Sand and Gravel |  |
| <img src="svg/RT_TAP.svg" height="14" alt="RT_TAP"> | `RT_TAP` | Taplow Gravel |  |
| <img src="svg/RT_TH3.svg" height="14" alt="RT_TH3"> | `RT_TH3` | Thatcham Gravel |  |
| <img src="svg/RT_WAN.svg" height="14" alt="RT_WAN"> | `RT_WAN` | Wanlip Sand and Gravel |  |
| <img src="svg/ALV_W.svg" height="14" alt="ALV_W"> | `ALV_W` | Warp |  |
| <img src="svg/RT_WG.svg" height="14" alt="RT_WG"> | `RT_WG` | Westland Green Gravel |  |
| <img src="svg/RT_WM.svg" height="14" alt="RT_WM"> | `RT_WM` | Westmill Lower Gravel |  |
| <img src="svg/RT_WH.svg" height="14" alt="RT_WH"> | `RT_WH` | Whatton Sand and Gravel |  |
| <img src="svg/RT_WH7.svg" height="14" alt="RT_WH7"> | `RT_WH7` | Winter Hill Gravel |  |
| <img src="svg/RT_WO3.svg" height="14" alt="RT_WO3"> | `RT_WO3` | Wolvercote Member | Wolvercote Member river terrace |
| <img src="svg/RT_WD.svg" height="14" alt="RT_WD"> | `RT_WD` | Woodford Gravel |  |

## Lacustrine Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/LAC.svg" height="14" alt="LAC"> | `LAC` | Lacustrine deposits |  |
| <img src="svg/LAC1.svg" height="14" alt="LAC1"> | `LAC1` | Lacustrine deposits 1 |  |
| <img src="svg/LAC2.svg" height="15" alt="LAC2"> | `LAC2` | Lacustrine deposits 2 |  |
| <img src="svg/LAC3.svg" height="14" alt="LAC3"> | `LAC3` | Lacustrine deposits 3 |  |
| <img src="svg/LAC_D.svg" height="14" alt="LAC_D"> | `LAC_D` | Lacustrine delta deposits |  |
| <img src="svg/LAC_SB.svg" height="14" alt="LAC_SB"> | `LAC_SB` | Lacustrine shoreface and beach deposits |  |
| <img src="svg/LAC_S5.svg" height="14" alt="LAC_S5"> | `LAC_S5` | Lacustrine shoreface and beach deposits 5 |  |

## Marine Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/MA_B.svg" height="14" alt="MA_B"> | `MA_B` | Bank deposits |  |
| <img src="svg/MA_BS.svg" height="14" alt="MA_BS"> | `MA_BS` | Bank deposits, sand |  |
| <img src="svg/MA_BDB.svg" height="15" alt="MA_BDB"> | `MA_BDB` | Barroway Drove Beds | Barroway Drove Beds, marine deposit |
| <img src="svg/MA_CH.svg" height="14" alt="MA_CH"> | `MA_CH` | Chenier deposits |  |
| <img src="svg/MA_NET.svg" height="14" alt="MA_NET"> | `MA_NET` | Netley Heath Deposits | Netley Heath marine deposits |
| <img src="svg/MA_CB.svg" height="14" alt="MA_CB"> | `MA_CB` | Coastal barrier deposits |  |
| <img src="svg/MA_SGC.svg" height="14" alt="MA_SGC"> | `MA_SGC` | Coastal barrier, sand and gravel |  |
| <img src="svg/MA_CZ.svg" height="14" alt="MA_CZ"> | `MA_CZ` | Coastal zone deposits, undifferentiated |  |
| <img src="svg/MA_I.svg" height="14" alt="MA_I"> | `MA_I` | Intertidal deposits, undifferentiated |  |
| <img src="svg/MA_MB.svg" height="14" alt="MA_MB"> | `MA_MB` | Marine band |  |
| <img src="svg/MA_BE.svg" height="14" alt="MA_BE"> | `MA_BE` | Marine beach deposits |  |
| <img src="svg/MA_MA.svg" height="14" alt="MA_MA"> | `MA_MA` | Marine deposits, undifferentiated |  |
| <img src="svg/MA_SG.svg" height="14" alt="MA_SG"> | `MA_SG` | Marine deposits, sand and gravel |  |
| <img src="svg/MA_M.svg" height="14" alt="MA_M"> | `MA_M` | Mud deposits |  |
| <img src="svg/MA_SM.svg" height="14" alt="MA_SM"> | `MA_SM` | Saltmarsh deposits |  |
| <img src="svg/MA_SSI.svg" height="14" alt="MA_SSI"> | `MA_SSI` | Sand and silt deposits |  |
| <img src="svg/MA_S.svg" height="14" alt="MA_S"> | `MA_S` | Sand deposits |  |
| <img src="svg/MA_SST.svg" height="14" alt="MA_SST"> | `MA_SST` | Sand, tabular or sheet deposits |  |
| <img src="svg/MA_SHB.svg" height="14" alt="MA_SHB"> | `MA_SHB` | Shell bank (mussel band) |  |
| <img src="svg/MA_SF.svg" height="14" alt="MA_SF"> | `MA_SF` | Shoreface deposits |  |
| <img src="svg/MA_SFS.svg" height="14" alt="MA_SFS"> | `MA_SFS` | Shoreface deposits, sand |  |
| <img src="svg/MA_SSG.svg" height="14" alt="MA_SSG"> | `MA_SSG` | Shoreface deposits, sand and gravel |  |
| <img src="svg/MA_SI.svg" height="14" alt="MA_SI"> | `MA_SI` | Silt deposits |  |
| <img src="svg/MA_SB.svg" height="14" alt="MA_SB"> | `MA_SB` | Storm beach deposits |  |
| <img src="svg/MA_SB1.svg" height="15" alt="MA_SB1"> | `MA_SB1` | Storm beach deposits, 1 |  |
| <img src="svg/MA_SBG.svg" height="14" alt="MA_SBG"> | `MA_SBG` | Storm beach deposits, gravel |  |
| <img src="svg/MA_SU.svg" height="14" alt="MA_SU"> | `MA_SU` | Supratidal deposits undifferentiated |  |
| <img src="svg/MA_ST.svg" height="14" alt="MA_ST"> | `MA_ST` | Tabular or sheet deposits |  |
| <img src="svg/MA_TF.svg" height="14" alt="MA_TF"> | `MA_TF` | Tidal flat deposits |  |
| <img src="svg/MA_TF1.svg" height="15" alt="MA_TF1"> | `MA_TF1` | Tidal flat deposits, 1 |  |
| <img src="svg/MA_TR.svg" height="14" alt="MA_TR"> | `MA_TR` | Tidal, river or creek deposits |  |
| <img src="svg/MA_TRM.svg" height="14" alt="MA_TRM"> | `MA_TRM` | Tidal, river or creek deposits, mud |  |
| <img src="svg/MA_TMG.svg" height="14" alt="MA_TMG"> | `MA_TMG` | Tidal, river or creek deposits, mud and gravel |  |
| <img src="svg/MA_WO.svg" height="14" alt="MA_WO"> | `MA_WO` | Washover deposits |  |

## Raised Marine Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/RM_SB2.svg" height="14" alt="RM_SB2"> | `RM_SB2` | Beach deposits | Beach deposits, raised marine deposits |
| <img src="svg/RM_BL.svg" height="15" alt="RM_BL"> | `RM_BL` | Brackish lagoon |  |
| <img src="svg/RM_DS.svg" height="14" alt="RM_DS"> | `RM_DS` | Delta deposits, sand and gravel | Delta deposits, sand and gravel, raised marine |
| <img src="svg/RM_FL.svg" height="14" alt="RM_FL"> | `RM_FL` | Flandrian deposits |  |
| <img src="svg/RM_IN.svg" height="14" alt="RM_IN"> | `RM_IN` | Intertidal |  |
| <img src="svg/RM_LG.svg" height="14" alt="RM_LG"> | `RM_LG` | Late glacial | Late Glacial, raised marine deposits |
| <img src="svg/RM_PG.svg" height="14" alt="RM_PG"> | `RM_PG` | Post glacial | Postglacial, raised marine deposits |
| <img src="svg/RM_D.svg" height="14" alt="RM_D"> | `RM_D` | Raised marine delta deposits |  |
| <img src="svg/RM.svg" height="14" alt="RM"> | `RM` | Raised marine deposits |  |
| <img src="svg/RM_C.svg" height="14" alt="RM_C"> | `RM_C` | Raised marine deposits, clay |  |
| <img src="svg/RM_2.svg" height="14" alt="RM_2"> | `RM_2` | Raised marine deposits, high | High raised marine deposits |
| <img src="svg/RM_3.svg" height="14" alt="RM_3"> | `RM_3` | Raised marine deposits, highest | Highest raised marine deposits |
| <img src="svg/RM_1.svg" height="14" alt="RM_1"> | `RM_1` | Raised marine deposits, low | Low raised marine deposits |
| <img src="svg/RM_MG.svg" height="14" alt="RM_MG"> | `RM_MG` | Raised marine deposits, March Gravels | March gravels, raised marine deposits |
| <img src="svg/RM_M.svg" height="14" alt="RM_M"> | `RM_M` | Raised marine deposits, mud |  |
| <img src="svg/RM_NV.svg" height="14" alt="RM_NV"> | `RM_NV` | Raised marine deposits, Nor Valley Clay | Nor Valley Clay, raised marine deposits |
| <img src="svg/RM_SG.svg" height="14" alt="RM_SG"> | `RM_SG` | Raised marine deposits, sand and gravel | Sand and gravel, raised marine deposits |
| <img src="svg/RM_SC.svg" height="16" alt="RM_SC"> | `RM_SC` | Raised marine deposits, silt and clay | Silt and clay, raised marine deposits |
| <img src="svg/RM_TB.svg" height="14" alt="RM_TB"> | `RM_TB` | Raised marine deposits, Terrington Beds | Terrington Beds, raised marine deposits |
| <img src="svg/RM_TO.svg" height="14" alt="RM_TO"> | `RM_TO` | Raised marine deposits, Tottenhill Gravels | Tottenhill Gravels, raised marine deposits |
| <img src="svg/RM_TF.svg" height="14" alt="RM_TF"> | `RM_TF` | Raised marine, tidal, river or creek deposits | Tidal, river or creek deposits, raised marine deposits |
| <img src="svg/RM_TRF.svg" height="15" alt="RM_TRF"> | `RM_TRF` | Raised tidal flat deposits of Flandrian age |  |
| <img src="svg/RM_SBF.svg" height="15" alt="RM_SBF"> | `RM_SBF` | Shore beach deposits of Flandrian age |  |
| <img src="svg/RM_SU.svg" height="14" alt="RM_SU"> | `RM_SU` | Subtidal | Subtidal, raised marine deposits |

## Interglacial

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/IGL_LA.svg" height="15" alt="IGL_LA"> | `IGL_LA` | Interglacial lacustrine deposits |  |
| <img src="svg/IGL.svg" height="14" alt="IGL"> | `IGL` | Interglacial deposits, undifferentiated |  |
| <img src="svg/IGL_FL.svg" height="14" alt="IGL_FL"> | `IGL_FL` | Interglacial fluvial deposits |  |
| <img src="svg/IGL_MA.svg" height="15" alt="IGL_MA"> | `IGL_MA` | Interglacial marine deposits, undifferentiated |  |
| <img src="svg/IGL_MS.svg" height="15" alt="IGL_MS"> | `IGL_MS` | Interglacial marine shore beach deposits |  |

## Glacial Deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/DM.svg" height="14" alt="DM"> | `DM` | Diamicton |  |
| <img src="svg/GL.svg" height="14" alt="GL"> | `GL` | Glacial deposits |  |
| <img src="svg/GL_CG.svg" height="14" alt="GL_CG"> | `GL_CG` | Crag with tail |  |
| <img src="svg/GL_HMC.svg" height="14" alt="GL_HMC"> | `GL_HMC` | Hummocky glacial and morainic deposits |  |
| <img src="svg/GL_MSG.svg" height="18" alt="GL_MSG"> | `GL_MSG` | Muddy sand and gravel | Muddy sand and gravel, glacial deposits |
| <img src="svg/GFL.svg" height="14" alt="GFL"> | `GFL` | Glaciofluvial deposits, undifferentiated |  |
| <img src="svg/GFL_IT.svg" height="21" alt="GFL_IT"> | `GFL_IT` | Irish Sea Ice Sheet (sheet deposits) | Irish Sea Ice Sheet, (sheet deposits) glaciofluvial deposits |

### Glaciofluvial deposits

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/GFL_B.svg" height="22" alt="GFL_B"> | `GFL_B` | Baginton Sand and Gravel | Baginton Sand and Gravel, glaciofluvial deposits |
| <img src="svg/GFL_BU.svg" height="22" alt="GFL_BU"> | `GFL_BU` | Burtle Beds | Burtle Beds, glaciofluvial deposits |
| <img src="svg/GFL_CO.svg" height="23" alt="GFL_CO"> | `GFL_CO` | Corton Formation | Corton Formation, glaciofluvial deposits |
| <img src="svg/GFL_D.svg" height="14" alt="GFL_D"> | `GFL_D` | Deltaic and / or fan deposits | Fan deposits and / or deltaic |
| <img src="svg/GFL_EG.svg" height="22" alt="GFL_EG"> | `GFL_EG` | Lochton Sand and Gravel Formation (East Grampian Drift Group) |  |
| <img src="svg/GFL_EM.svg" height="22" alt="GFL_EM"> | `GFL_EM` | Eagle Moor Sand and Gravel | Eagle Moor Sand and Gravel, glaciofluvial deposits |
| <img src="svg/GFL_HO.svg" height="22" alt="GFL_HO"> | `GFL_HO` | Holderness Formation | Holderness Formation, glaciofluvial deposits |
| <img src="svg/GFL_IC.svg" height="14" alt="GFL_IC"> | `GFL_IC` | Ice-contact | Ice-contact, glaciofluvial deposits |
| <img src="svg/GFL_I.svg" height="21" alt="GFL_I"> | `GFL_I` | Irish Sea Ice Sheet, undifferentiated | Irish Sea Ice Sheet, undifferentiated, glaciofluvial deposits |
| <img src="svg/GFL_L.svg" height="22" alt="GFL_L"> | `GFL_L` | Lowestoft Formation | Lowestoft Formation, glaciofluvial deposits |
| <img src="svg/GFL_MD.svg" height="21" alt="GFL_MD"> | `GFL_MD` | Drumlithie Sand and Gravel (Mearns Drift Group) | Drumlithie Sand and Gravel (Mearns Drift Group), glaciofluvial deposits |
| <img src="svg/GFL_MT.svg" height="21" alt="GFL_MT"> | `GFL_MT` | Moreton Member | Moreton Member, glaciofluvial deposits |
| <img src="svg/GFL_O.svg" height="22" alt="GFL_O"> | `GFL_O` | Overstrand Formation | Overstrand Formation, glaciofluvial deposits |
| <img src="svg/GFL_OD.svg" height="22" alt="GFL_OD"> | `GFL_OD` | Oadby Member | Oadby Member, glaciofluvial deposits |
| <img src="svg/GFL_PD.svg" height="22" alt="GFL_PD"> | `GFL_PD` | Pre-Devensian |  |
| <img src="svg/GFL_S1.svg" height="22" alt="GFL_S1"> | `GFL_S1` | Sheet deposits, 1st | Sheet deposits, 1st, glaciofluvial deposits |
| <img src="svg/GFL_S2.svg" height="22" alt="GFL_S2"> | `GFL_S2` | Sheet deposits, 2nd | Sheet deposits, 2nd, glaciofluvial deposits |
| <img src="svg/GFL_S3.svg" height="22" alt="GFL_S3"> | `GFL_S3` | Sheet deposits, 3rd | Sheet deposits, 3rd, glaciofluvial deposits |
| <img src="svg/GFL_SG.svg" height="14" alt="GFL_SG"> | `GFL_SG` | Sand and gravel | Sand and gravel, glaciofluvial deposits |
| <img src="svg/GFL_SH.svg" height="14" alt="GFL_SH"> | `GFL_SH` | Sheet deposits | Sheet deposits, glaciofluvial deposits |
| <img src="svg/GFL_WI.svg" height="21" alt="GFL_WI"> | `GFL_WI` | Wigston Sand and Gravel | Wigston Sand and Gravel, glaciofluvial deposits |
| <img src="svg/GFL_WL.svg" height="22" alt="GFL_WL"> | `GFL_WL` | Woolford Heath Member | Woolford Heath Member, glaciofluvial deposits |
| <img src="svg/GFL_WO.svg" height="22" alt="GFL_WO"> | `GFL_WO` | Wolston Sand and Gravel | Wolston Sand and Gravel, glaciofluvial deposits |
| <img src="svg/GLA.svg" height="14" alt="GLA"> | `GLA` | Glaciolacustrine deposits |  |

### Glaciolacustrine

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/GLA1.svg" height="15" alt="GLA1"> | `GLA1` | Glaciolacustrine deposits 1 |  |
| <img src="svg/GLA2.svg" height="16" alt="GLA2"> | `GLA2` | Glaciolacustrine deposits 2 |  |
| <img src="svg/GLA_C.svg" height="14" alt="GLA_C"> | `GLA_C` | Clay | Clay, glaciolacustrine deposits |
| <img src="svg/GLA_DG.svg" height="14" alt="GLA_DG"> | `GLA_DG` | Delta deposits, sand and gravel | Delta deposits, sand and gravel, glacial |
| <img src="svg/GLA_DL.svg" height="14" alt="GLA_DL"> | `GLA_DL` | Delta deposits |  |
| <img src="svg/GLA_DS.svg" height="14" alt="GLA_DS"> | `GLA_DS` | Delta deposits, sand |  |
| <img src="svg/GLA_EG.svg" height="21" alt="GLA_EG"> | `GLA_EG` | Glen Dye Silts Formation (East Grampian Drift Group) | Glen Dye Silts Formation (East Grampian Drift Group), glaciolacustrine deposits |
| <img src="svg/GLA_FC.svg" height="20" alt="GLA_FC"> | `GLA_FC` | Findern Clay |  |
| <img src="svg/GLA_M.svg" height="14" alt="GLA_M"> | `GLA_M` | Silt and clay | Silt and clay, glaciolacustrine deposits |

### Glaciomarine

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/GLA_MD.svg" height="20" alt="GLA_MD"> | `GLA_MD` | Ury Silts Formation (Mearns Drift Group) | Ury Silts Formation (Mearns Drift Group), glaciolacustrine deposits |
| <img src="svg/GLA_M1.svg" height="19" alt="GLA_M1"> | `GLA_M1` | Silt and clay, 1st | Silt and clay, 1st, glaciolacustrine deposits |
| <img src="svg/GLA_RO.svg" height="20" alt="GLA_RO"> | `GLA_RO` | Rotherby clay | Rotherby Clay, glaciolacustrine deposits |
| <img src="svg/GLA_S.svg" height="14" alt="GLA_S"> | `GLA_S` | Sand | Sand, glaciolacustrine deposits |
| <img src="svg/GLA_SG.svg" height="14" alt="GLA_SG"> | `GLA_SG` | Sand and gravel | Sand and gravel, glaciomarine deposits |
| <img src="svg/GLM.svg" height="14" alt="GLM"> | `GLM` | Glaciomarine deposits |  |
| <img src="svg/GLM_A.svg" height="23" alt="GLM_A"> | `GLM_A` | Ardersier Silts Formation | Ardersier Silts Formation, glaciomarine deposits |
| <img src="svg/TIL.svg" height="14" alt="TIL"> | `TIL` | Till or boulder clay |  |

### Till

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/TIL_BB.svg" height="19" alt="TIL_BB"> | `TIL_BB` | Benholm Clay Formation | Benholm Clay Formation, till |
| <img src="svg/TIL_C.svg" height="14" alt="TIL_C"> | `TIL_C` | Wragby, Calcethorpe &amp; Belmont | Wragby, Calcethorpe &amp; Belmont, till |
| <img src="svg/TIL_CO.svg" height="20" alt="TIL_CO"> | `TIL_CO` | Corton Formation | Corton Formation, till |
| <img src="svg/TIL_EG.svg" height="20" alt="TIL_EG"> | `TIL_EG` | Banchory Till Formation (east Grampian Drift Group) | Banchory Till Formation (east Grampian Drift Group), till |
| <img src="svg/TIL_HO.svg" height="19" alt="TIL_HO"> | `TIL_HO` | Holderness Formation | Holderness Formation, till |
| <img src="svg/TIL_I.svg" height="19" alt="TIL_I"> | `TIL_I` | Irish Sea Ice Sheet | Irish Sea Ice sheet, till |
| <img src="svg/TIL_L.svg" height="19" alt="TIL_L"> | `TIL_L` | Lowestoft Formation | Lowestoft Formation, till |
| <img src="svg/TIL_M.svg" height="19" alt="TIL_M"> | `TIL_M` | Marsh Till | Marsh till |
| <img src="svg/TIL_MD.svg" height="19" alt="TIL_MD"> | `TIL_MD` | Mill of Forest Formation (Mearns Drift Group) | Mill of Forest Formation (Mearns Drift Group), till |
| <img src="svg/TIL_MT.svg" height="21" alt="TIL_MT"> | `TIL_MT` | Moreton Member | Moreton Member, till |
| <img src="svg/TIL_O.svg" height="20" alt="TIL_O"> | `TIL_O` | Overstrand Formation | Overstrand Formation, till |
| <img src="svg/TIL_OD.svg" height="19" alt="TIL_OD"> | `TIL_OD` | Oadby Till |  |
| <img src="svg/TIL_OL.svg" height="20" alt="TIL_OL"> | `TIL_OL` | Oadby Till (Lias-rich) |  |
| <img src="svg/TIL_OT.svg" height="20" alt="TIL_OT"> | `TIL_OT` | Oadby Till (Trias-rich) |  |
| <img src="svg/TIL_RM.svg" height="19" alt="TIL_RM"> | `TIL_RM` | Ruddington Moor Till |  |
| <img src="svg/TIL_TH.svg" height="19" alt="TIL_TH"> | `TIL_TH` | Thrussington Till |  |

## Miscellaneous Drift

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/SG_A.svg" height="21" alt="SG_A"> | `SG_A` | Anker Sand and Gravel |  |
| <img src="svg/SG_CH.svg" height="19" alt="SG_CH"> | `SG_CH` | Chelsfield Gravel |  |
| <img src="svg/SG_DG.svg" height="21" alt="SG_DG"> | `SG_DG` | Dunsmore Gravel |  |
| <img src="svg/ERRAT.svg" height="14" alt="ERRAT"> | `ERRAT` | Erratic |  |
| <img src="svg/SG_HAT.svg" height="21" alt="SG_HAT"> | `SG_HAT` | Hathern Gravel |  |
| <img src="svg/SG_U.svg" height="14" alt="SG_U"> | `SG_U` | Sand and gravel, age uncertain |  |
| <img src="svg/SG_ST.svg" height="21" alt="SG_ST"> | `SG_ST` | Stanmore Gravel |  |
| <img src="svg/SG_UP.svg" height="21" alt="SG_UP"> | `SG_UP` | Upton Sand and Gravel |  |
| <img src="svg/SG_WH.svg" height="20" alt="SG_WH"> | `SG_WH` | Well Hill Gravel |  |

## Landform

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/GDC_FA.svg" height="14" alt="GDC_FA"> | `GDC_FA` | Fall of glacial drainage channel |  |
| <img src="svg/GDC_F.svg" height="21" alt="GDC_F"> | `GDC_F` | Glacial drainage channel, front |  |
| <img src="svg/GLST.svg" height="14" alt="GLST"> | `GLST` | Glacial striae |  |
| <img src="svg/GLSTI.svg" height="14" alt="GLSTI"> | `GLSTI` | Glacial striae direction of ice flow |  |
| <img src="svg/KH.svg" height="23" alt="KH"> | `KH` | Kettle hollow |  |
| <img src="svg/GL_RM.svg" height="14" alt="GL_RM"> | `GL_RM` | Roche moutonnée |  |
| <img src="svg/GL_RMS.svg" height="14" alt="GL_RMS"> | `GL_RMS` | Roche moutonnée with striae |  |
| <img src="svg/ROCK.svg" height="14" alt="ROCK"> | `ROCK` | Rockhead or bedrock |  |
| <img src="svg/GDC_S.svg" height="14" alt="GDC_S"> | `GDC_S` | Single sided glacial drainage channel |  |

## Rock Symbols

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/RS_ATF.svg" height="14" alt="RS_ATF"> | `RS_ATF` | Acid tuff |  |
| <img src="svg/RS_ATT.svg" height="15" alt="RS_ATT"> | `RS_ATT` | Acid tuffite |  |
| <img src="svg/RS_APL.svg" height="14" alt="RS_APL"> | `RS_APL` | Aplite |  |
| <img src="svg/RS_BTF.svg" height="14" alt="RS_BTF"> | `RS_BTF` | Basic tuff |  |
| <img src="svg/RS_BTT.svg" height="14" alt="RS_BTT"> | `RS_BTT` | Basic tuffite |  |
| <img src="svg/RS_BEM.svg" height="14" alt="RS_BEM"> | `RS_BEM` | Cataclastic (Metamorphic) | Cataclastic (metamorphic) |
| <img src="svg/RS_BET.svg" height="14" alt="RS_BET"> | `RS_BET` | Cataclastic rocks |  |
| <img src="svg/RS_FOL.svg" height="14" alt="RS_FOL"> | `RS_FOL` | Foliated |  |
| <img src="svg/RS_GRX.svg" height="14" alt="RS_GRX"> | `RS_GRX` | Grandiorite X |  |
| <img src="svg/RS_P.svg" height="14" alt="RS_P"> | `RS_P` | Microdiorite |  |
| <img src="svg/RS_FG.svg" height="15" alt="RS_FG"> | `RS_FG` | Microgranite |  |
| <img src="svg/RS_MU1.svg" height="14" alt="RS_MU1"> | `RS_MU1` | Mylonitic (metamorphic) |  |
| <img src="svg/RS_MU.svg" height="14" alt="RS_MU"> | `RS_MU` | Mylonitic rocks |  |
| <img src="svg/RS_PEG.svg" height="14" alt="RS_PEG"> | `RS_PEG` | Pegmatite |  |
| <img src="svg/RS_KAP.svg" height="14" alt="RS_KAP"> | `RS_KAP` | Pseudotachylitic |  |
| <img src="svg/RS_R.svg" height="15" alt="RS_R"> | `RS_R` | Rhyolite |  |
| <img src="svg/RS_SH.svg" height="14" alt="RS_SH"> | `RS_SH` | Sheared rock (igneous and metamorphic) |  |

## Structural Symbols

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_ISCL.svg" height="14" alt="S_ISCL"> | `S_ISCL` | Corrugated strata, low dip |  |
| <img src="svg/S_ISCF.svg" height="14" alt="S_ISCF"> | `S_ISCF` | Corrugated foliation |  |
| <img src="svg/S_IS2.svg" height="14" alt="S_IS2"> | `S_IS2` | Inclined strata 2 |  |
| <img src="svg/S_AMA.svg" height="14" alt="S_AMA"> | `S_AMA` | Axis of minor anticline |  |

### Bedding

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_CBF.svg" height="14" alt="S_CBF"> | `S_CBF` | Cross-bedding of foresets |  |
| <img src="svg/S_DY.svg" height="14" alt="S_DY"> | `S_DY` | Direction of younging |  |
| <img src="svg/S_DB.svg" height="14" alt="S_DB"> | `S_DB` | Dune-bedding |  |
| <img src="svg/S_GDIP.svg" height="14" alt="S_GDIP"> | `S_GDIP` | General dip | Dip, general |
| <img src="svg/S_GDUP.svg" height="15" alt="S_GDUP"> | `S_GDUP` | General dip, underground | Dip, general, underground |
| <img src="svg/S_GIS.svg" height="14" alt="S_GIS"> | `S_GIS` | Gently inclined strata | Inclined strata (gently) |
| <img src="svg/S_GUS.svg" height="15" alt="S_GUS"> | `S_GUS` | Gently undulating strata | Undulating strata (gently) |
| <img src="svg/S_ISH.svg" height="14" alt="S_ISH"> | `S_ISH` | Highly inclined strata | Inclined strata (highly) |
| <img src="svg/S_HOS.svg" height="17" alt="S_HOS"> | `S_HOS` | Horizontal overturned strata | Overturned (horizontal) strata |
| <img src="svg/S_HS.svg" height="14" alt="S_HS"> | `S_HS` | Horizontal strata |  |
| <img src="svg/S_IS1.svg" height="14" alt="S_IS1"> | `S_IS1` | Inclined strata 1 |  |
| <img src="svg/S_ISO.svg" height="14" alt="S_ISO"> | `S_ISO` | Inclined strata, overturned | Overturned inclined strata |
| <img src="svg/S_ISU.svg" height="14" alt="S_ISU"> | `S_ISU` | Inclined strata, uncertain |  |
| <img src="svg/S_ISUD.svg" height="14" alt="S_ISUD"> | `S_ISUD` | Inclined strata, underground |  |
| <img src="svg/S_STS.svg" height="14" alt="S_STS"> | `S_STS` | Strike of strata |  |
| <img src="svg/S_UIS.svg" height="14" alt="S_UIS"> | `S_UIS` | Undulating bed, inclined |  |
| <img src="svg/S_UVS.svg" height="14" alt="S_UVS"> | `S_UVS` | Undulating vertical strata | Vertical strata, undulating |
| <img src="svg/S_VS.svg" height="14" alt="S_VS"> | `S_VS` | Vertical strata |  |
| <img src="svg/S_HF.svg" height="14" alt="S_HF"> | `S_HF` | Horizontal foliation |  |

### Foliation or layering

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_IF.svg" height="14" alt="S_IF"> | `S_IF` | Inclined foliation |  |
| <img src="svg/S_STF.svg" height="14" alt="S_STF"> | `S_STF` | Strike of foliation |  |
| <img src="svg/S_UF.svg" height="17" alt="S_UF"> | `S_UF` | Undulating foliation |  |
| <img src="svg/S_VF.svg" height="14" alt="S_VF"> | `S_VF` | Vertical foliation |  |
| <img src="svg/S_VFC.svg" height="14" alt="S_VFC"> | `S_VFC` | Vertical foliation, general corrugated strike | Corrugated strike (general) vertical foliation |

### Cleavage / schistosity

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_DC.svg" height="14" alt="S_DC"> | `S_DC` | Direction of cleavage |  |
| <img src="svg/S_HC.svg" height="19" alt="S_HC"> | `S_HC` | Horizontal cleavage |  |
| <img src="svg/S_IC.svg" height="14" alt="S_IC"> | `S_IC` | Inclined cleavage |  |
| <img src="svg/S_ICS.svg" height="14" alt="S_ICS"> | `S_ICS` | Inclined cleavage, sandstone |  |
| <img src="svg/S_SR.svg" height="14" alt="S_SR"> | `S_SR` | Sheared rock |  |
| <img src="svg/S_STC.svg" height="14" alt="S_STC"> | `S_STC` | Strike of cleavage |  |
| <img src="svg/S_UCI.svg" height="14" alt="S_UCI"> | `S_UCI` | Undulating cleavage, inclined |  |
| <img src="svg/S_VC.svg" height="14" alt="S_VC"> | `S_VC` | Vertical cleavage |  |
| <img src="svg/S_VCS.svg" height="14" alt="S_VCS"> | `S_VCS` | Vertical cleavage in sandstone |  |
| <img src="svg/S_HJ.svg" height="18" alt="S_HJ"> | `S_HJ` | Horizontal joint |  |
| <img src="svg/S_IJ.svg" height="14" alt="S_IJ"> | `S_IJ` | Inclined joint |  |
| <img src="svg/S_VJ.svg" height="14" alt="S_VJ"> | `S_VJ` | Vertical joint |  |

### Linear structures

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_HLI.svg" height="14" alt="S_HLI"> | `S_HLI` | Horizontal lineation |  |
| <img src="svg/S_PLI.svg" height="14" alt="S_PLI"> | `S_PLI` | Plunging lineation |  |
| <img src="svg/S_VLI.svg" height="14" alt="S_VLI"> | `S_VLI` | Vertical lineation |  |
| <img src="svg/S_HFJ.svg" height="14" alt="S_HFJ"> | `S_HFJ` | Horizontal flow jointing |  |

### Igneous rocks

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_HPCA.svg" height="14" alt="S_HPCA"> | `S_HPCA` | Horizontal primary crystal alignment |  |
| <img src="svg/S_HPPF.svg" height="18" alt="S_HPPF"> | `S_HPPF` | Horizontal primary planar fabric in igneous rocks |  |
| <img src="svg/S_HR.svg" height="17" alt="S_HR"> | `S_HR` | Horizontal relict, planar fabric in plutonic rocks |  |
| <img src="svg/S_HWF.svg" height="18" alt="S_HWF"> | `S_HWF` | Horizontal welding foliation |  |
| <img src="svg/S_IFJ.svg" height="14" alt="S_IFJ"> | `S_IFJ` | Inclined flow jointing |  |
| <img src="svg/S_IPCA.svg" height="14" alt="S_IPCA"> | `S_IPCA` | Inclined primary crystal alignment |  |
| <img src="svg/S_IPP.svg" height="14" alt="S_IPP"> | `S_IPP` | Inclined primary planar fabric |  |
| <img src="svg/S_IPPO.svg" height="14" alt="S_IPPO"> | `S_IPPO` | Inclined primary planar fabric, overturned |  |
| <img src="svg/S_IR.svg" height="14" alt="S_IR"> | `S_IR` | Inclined relict, planar fabric in plutonic rocks |  |
| <img src="svg/S_IWF.svg" height="14" alt="S_IWF"> | `S_IWF` | Inclined welding foliation |  |
| <img src="svg/S_STPP.svg" height="14" alt="S_STPP"> | `S_STPP` | Strike of primary planar fabric |  |
| <img src="svg/S_STWF.svg" height="14" alt="S_STWF"> | `S_STWF` | Strike of welding foliation |  |
| <img src="svg/S_VFJ.svg" height="14" alt="S_VFJ"> | `S_VFJ` | Vertical flow jointing |  |
| <img src="svg/S_VPCA.svg" height="14" alt="S_VPCA"> | `S_VPCA` | Vertical primary crystal alignment |  |
| <img src="svg/S_VPP.svg" height="14" alt="S_VPP"> | `S_VPP` | Vertical primary planar fabric |  |
| <img src="svg/S_VR.svg" height="14" alt="S_VR"> | `S_VR` | Vertical relict, planar fabric in plutonic rocks |  |
| <img src="svg/S_VWF.svg" height="14" alt="S_VWF"> | `S_VWF` | Vertical welding foliation |  |
| <img src="svg/S_ACAP.svg" height="19" alt="S_ACAP"> | `S_ACAP` | Anticline axial plane |  |

### Major folds

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_SCAP.svg" height="18" alt="S_SCAP"> | `S_SCAP` | Synclinal axial plane |  |
| <img src="svg/S_SFAP.svg" height="17" alt="S_SFAP"> | `S_SFAP` | Synform axial plane |  |

### Minor folds

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_AMF.svg" height="14" alt="S_AMF"> | `S_AMF` | Axis of minor fold |  |
| <img src="svg/S_AMS.svg" height="14" alt="S_AMS"> | `S_AMS` | Axis of minor syncline |  |
| <img src="svg/S_HAPM.svg" height="14" alt="S_HAPM"> | `S_HAPM` | Horizontal axial plane of minor fold |  |
| <img src="svg/S_HAMA.svg" height="14" alt="S_HAMA"> | `S_HAMA` | Horizontal axis of minor anticline |  |
| <img src="svg/S_HAMF.svg" height="14" alt="S_HAMF"> | `S_HAMF` | Horizontal axis of minor fold |  |
| <img src="svg/S_HAM1.svg" height="14" alt="S_HAM1"> | `S_HAM1` | Horizontal axis of minor fold, phase 1 |  |
| <img src="svg/S_HAMM.svg" height="14" alt="S_HAMM"> | `S_HAMM` | Horizontal axis of minor monocline |  |
| <img src="svg/S_HAMS.svg" height="14" alt="S_HAMS"> | `S_HAMS` | Horizontal axis of minor syncline |  |
| <img src="svg/S_IAPM.svg" height="14" alt="S_IAPM"> | `S_IAPM` | Inclined axial plane of minor fold |  |
| <img src="svg/S_LOC.svg" height="14" alt="S_LOC"> | `S_LOC` | Locality with refolded minor folds |  |
| <img src="svg/S_MFLA.svg" height="14" alt="S_MFLA"> | `S_MFLA` | Minor fold, low angle of plunge |  |
| <img src="svg/S_ANO.svg" height="14" alt="S_ANO"> | `S_ANO` | Overturned anticline | Anticline, overturned |
| <img src="svg/S_SYNO.svg" height="14" alt="S_SYNO"> | `S_SYNO` | Overturned syncline | Syncline, overturned |
| <img src="svg/S_PMF.svg" height="14" alt="S_PMF"> | `S_PMF` | Plunge axis of minor fold |  |
| <img src="svg/S_STAM.svg" height="14" alt="S_STAM"> | `S_STAM` | Strike axial plane minor fold |  |
| <img src="svg/S_VAPM.svg" height="14" alt="S_VAPM"> | `S_VAPM` | Vertical axial plane of minor fold |  |
| <img src="svg/S_VAMF.svg" height="14" alt="S_VAMF"> | `S_VAMF` | Vertical axis of minor fold |  |

### Vergence

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/S_AMFV.svg" height="14" alt="S_AMFV"> | `S_AMFV` | Axis of minor fold showing direction of vergence |  |
| <img src="svg/S_DXVM.svg" height="14" alt="S_DXVM"> | `S_DXVM` | Dextral vergence of minor fold |  |
| <img src="svg/S_DVMF.svg" height="14" alt="S_DVMF"> | `S_DVMF` | Direction of vergence of minor fold |  |
| <img src="svg/S_NVMF.svg" height="14" alt="S_NVMF"> | `S_NVMF` | Neutral vergence of minor fold |  |
| <img src="svg/S_SVMF.svg" height="14" alt="S_SVMF"> | `S_SVMF` | Sinistral vergence of minor fold |  |

### Faults and related structures

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/FLT_MV.svg" height="14" alt="FLT_MV"> | `FLT_MV` | Fault movement |  |
| <img src="svg/FLT_TR.svg" height="14" alt="FLT_TR"> | `FLT_TR` | Fault terminator |  |
| <img src="svg/S_MVFD.svg" height="14" alt="S_MVFD"> | `S_MVFD` | Mineral vein dip | Dip, mineral vein |
| <img src="svg/FLT_S.svg" height="17" alt="FLT_S"> | `FLT_S` | Strike slip fault | Fault, strike slip |
| <img src="svg/TBARB.svg" height="14" alt="TBARB"> | `TBARB` | Thrust barb |  |

## Other Symbols

| Symbol | Reference | Description | Also indexed as |
|:---:|---|---|---|
| <img src="svg/ADIT.svg" height="14" alt="ADIT"> | `ADIT` | Adit |  |
| <img src="svg/ADIT_A.svg" height="14" alt="ADIT_A"> | `ADIT_A` | Adit, abandoned |  |
| <img src="svg/ADIT_U.svg" height="14" alt="ADIT_U"> | `ADIT_U` | Adit, unknown orientation |  |
| <img src="svg/BH.svg" height="14" alt="BH"> | `BH` | Borehole |  |
| <img src="svg/BH_UN.svg" height="14" alt="BH_UN"> | `BH_UN` | Borehole, uncertain |  |
| <img src="svg/BH_UD.svg" height="14" alt="BH_UD"> | `BH_UD` | Borehole, underground |  |
| <img src="svg/S_DIP.svg" height="14" alt="S_DIP"> | `S_DIP` | Dip of igneous contact |  |
| <img src="svg/FOSSL.svg" height="14" alt="FOSSL"> | `FOSSL` | Fossil locality |  |
| <img src="svg/S_IDY.svg" height="14" alt="S_IDY"> | `S_IDY` | Inclination of dyke |  |
| <img src="svg/SPNT.svg" height="18" alt="SPNT"> | `SPNT` | Location, with specific note | Location with specific note |
| <img src="svg/MLOC.svg" height="14" alt="MLOC"> | `MLOC` | Mineral locality |  |
| <img src="svg/PHOTO.svg" height="20" alt="PHOTO"> | `PHOTO` | Photo in BGS collection |  |
| <img src="svg/PIT.svg" height="14" alt="PIT"> | `PIT` | Pit or mine shaft |  |
| <img src="svg/PIT_A.svg" height="19" alt="PIT_A"> | `PIT_A` | Pit or mine shaft, abandoned, or denehole |  |
| <img src="svg/PIT_U.svg" height="22" alt="PIT_U"> | `PIT_U` | Pit or mine shaft, abandoned, site uncertain |  |
| <img src="svg/PIT_UD.svg" height="14" alt="PIT_UD"> | `PIT_UD` | Pit shaft, underground |  |
| <img src="svg/SLICE.svg" height="14" alt="SLICE"> | `SLICE` | Rock slice, petrographic |  |
| <img src="svg/SFM.svg" height="19" alt="SFM"> | `SFM` | Site of former mine |  |
| <img src="svg/EXP.svg" height="14" alt="EXP"> | `EXP` | Small isolated exposure |  |
| <img src="svg/SPRING.svg" height="14" alt="SPRING"> | `SPRING` | Spring or group of springs |  |
| <img src="svg/SURF_S.svg" height="14" alt="SURF_S"> | `SURF_S` | Surface section |  |
| <img src="svg/SWH.svg" height="20" alt="SWH"> | `SWH` | Swallow hole |  |
| <img src="svg/TRE.svg" height="14" alt="TRE"> | `TRE` | Trench |  |
| <img src="svg/UDSPOT.svg" height="14" alt="UDSPOT"> | `UDSPOT` | Underground spot level |  |
| <img src="svg/BH_WL.svg" height="14" alt="BH_WL"> | `BH_WL` | Well |  |

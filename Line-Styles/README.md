# Line styles

96 line styles from section 4 of BGS RR/01/01, extracted as vector SVG.

The report gives line styles a description but **no reference name**, so the `id` here is a slug of the description (e.g. `fault_thrust_observed`). It is not an official BGS code.

## Files

| Path | Contents |
|---|---|
| `swatch/{id}.svg` | The swatch exactly as printed. |
| `tile/{id}.svg` | One repeat of the style, vertically centred on the line, for use as a line pattern. |
| `lines.csv`, `lines.json` | Catalogue: id, description, colours, tile size, repeat method, MapLibre `line-width`. |
| [`../Sprites/`](../Sprites) | MapLibre sprite: image name `line-{id}`, use with `line-pattern`. |

## Using the tiles in MapLibre

MapLibre stretches a `line-pattern` image so its height equals `line-width`. To draw a style at its printed size, set `line-width` to the tile height in pixels (the `maplibre_line_width_px` column in `lines.csv`). Scale both with zoom if needed.

## How the repeat was found

- **autocorrelation**: the period of the whole style, measured from the swatch.
- **decoration spacing**: for the major fold axial traces (symbol, dashes, symbol), the period is the spacing between the symbols.
- **full swatch (13)**: the style carries a one-off decoration (a label such as `RF`, `Pb`, `al`, a single downthrow tick, strike-slip arrows, or end markers). The whole printed swatch is used as one repeat, so the decoration recurs about every 130 pt (about 46 mm). The glacial meltwater channel centre line has an arrow at one end and a dot at the other; on a real map it is better drawn as a plain line with end markers.

## Catalogue

| Swatch | Description | id | Repeat |
|:---:|---|---|---|
| <img src="swatch/aeromagnetic_bouguer_anomaly.svg" width="200" alt=""> | Aeromagnetic/Bouguer anomaly | `aeromagnetic_bouguer_anomaly` | autocorrelation |
| <img src="swatch/axial_plane_trace_of_major_anticline.svg" width="200" alt=""> | Axial plane trace of major anticline | `axial_plane_trace_of_major_anticline` | decoration spacing |
| <img src="swatch/axial_plane_traces_of_closely_spaced_anticline_syncline_pair.svg" width="200" alt=""> | Axial plane traces of closely spaced anticline/ syncline pair | `axial_plane_traces_of_closely_spaced_anticline_syncline_pair` | full swatch |
| <img src="swatch/axial_plane_trace_of_major_antiform.svg" width="200" alt=""> | Axial plane trace of major antiform | `axial_plane_trace_of_major_antiform` | decoration spacing |
| <img src="swatch/axial_plane_traces_of_closely_spaced_major_antiform_synform_pair.svg" width="200" alt=""> | Axial plane traces of closely spaced major antiform/ synform pair | `axial_plane_traces_of_closely_spaced_major_antiform_synform_pair` | full swatch |
| <img src="swatch/axial_plane_trace_of_major_reclined_or_vertical_fold.svg" width="200" alt=""> | Axial plane trace of major reclined or vertical fold | `axial_plane_trace_of_major_reclined_or_vertical_fold` | decoration spacing |
| <img src="swatch/axial_plane_trace_of_major_recumbant_fold.svg" width="200" alt=""> | Axial plane trace of major recumbant fold | `axial_plane_trace_of_major_recumbant_fold` | decoration spacing |
| <img src="swatch/axial_plane_trace_of_major_syncline.svg" width="200" alt=""> | Axial plane trace of major syncline | `axial_plane_trace_of_major_syncline` | decoration spacing |
| <img src="swatch/axial_plane_trace_of_major_synform.svg" width="200" alt=""> | Axial plane trace of major synform | `axial_plane_trace_of_major_synform` | decoration spacing |
| <img src="swatch/axis_of_large_scale_glacial_flute.svg" width="200" alt=""> | Axis of large-scale glacial flute | `axis_of_large_scale_glacial_flute` | autocorrelation |
| <img src="swatch/axis_of_large_scale_glacial_gouge.svg" width="200" alt=""> | Axis of large-scale glacial gouge | `axis_of_large_scale_glacial_gouge` | autocorrelation |
| <img src="swatch/backfeature_marking_former_coastline_arrowheads_denote_uphill_side.svg" width="200" alt=""> | Backfeature marking former coastline, arrowheads denote uphill side | `backfeature_marking_former_coastline_arrowheads_denote_uphill_side` | full swatch |
| <img src="swatch/backfeature_marking_former_lake_margin_arrowheads_denote_uphill_side.svg" width="200" alt=""> | Backfeature marking former lake margin, arrowheads denote uphill side | `backfeature_marking_former_lake_margin_arrowheads_denote_uphill_side` | full swatch |
| <img src="swatch/backfeature_of_terrace_margin_arrowheads_denote_uphill_side.svg" width="200" alt=""> | Backfeature of terrace margin, arrowheads denote uphill side | `backfeature_of_terrace_margin_arrowheads_denote_uphill_side` | full swatch |
| <img src="swatch/base_of_lava_flow.svg" width="200" alt=""> | Base of lava flow | `base_of_lava_flow` | autocorrelation |
| <img src="swatch/buried_channel_or_valley_margin.svg" width="200" alt=""> | Buried channel or valley margin | `buried_channel_or_valley_margin` | autocorrelation |
| <img src="swatch/buried_cliffline_crossmarks_on_beach_side.svg" width="200" alt=""> | Buried cliffline, crossmarks on beach side | `buried_cliffline_crossmarks_on_beach_side` | autocorrelation |
| <img src="swatch/cliffline_crossmarks_on_beach_side.svg" width="200" alt=""> | Cliffline, crossmarks on beach side | `cliffline_crossmarks_on_beach_side` | autocorrelation |
| <img src="swatch/cementstone.svg" width="200" alt=""> | Cementstone | `cementstone` | autocorrelation |
| <img src="swatch/coal_inferred.svg" width="200" alt=""> | Coal, inferred | `coal_inferred` | autocorrelation |
| <img src="swatch/coal_observed.svg" width="200" alt=""> | Coal, observed | `coal_observed` | autocorrelation |
| <img src="swatch/coal_sub_triassic.svg" width="200" alt=""> | Coal, sub-Triassic | `coal_sub_triassic` | autocorrelation |
| <img src="swatch/coal_seam_contour.svg" width="200" alt=""> | Coal seam contour | `coal_seam_contour` | autocorrelation |
| <img src="swatch/coal_seam_washout.svg" width="200" alt=""> | Coal seam, washout | `coal_seam_washout` | autocorrelation |
| <img src="swatch/crestline_of_elongate_mound.svg" width="200" alt=""> | Crestline of elongate mound | `crestline_of_elongate_mound` | autocorrelation |
| <img src="swatch/crestline_of_esker_blue_orange_or_magenta.svg" width="200" alt=""> | Crestline of esker (blue, orange or magenta) | `crestline_of_esker_blue_orange_or_magenta` | autocorrelation |
| <img src="swatch/crestline_of_linear_feature.svg" width="200" alt=""> | Crestline of linear feature | `crestline_of_linear_feature` | autocorrelation |
| <img src="swatch/drumlin_or_dune_line_at_base_of_mound.svg" width="200" alt=""> | Drumlin or dune line at base of mound | `drumlin_or_dune_line_at_base_of_mound` | autocorrelation |
| <img src="swatch/fault_brecciation_zone_inferred.svg" width="200" alt=""> | Fault brecciation zone, inferred | `fault_brecciation_zone_inferred` | autocorrelation |
| <img src="swatch/fault_brecciation_zone_observed.svg" width="200" alt=""> | Fault brecciation zone, observed | `fault_brecciation_zone_observed` | autocorrelation |
| <img src="swatch/fault_thrust_conjectural.svg" width="200" alt=""> | Fault, thrust conjectural | `fault_thrust_conjectural` | autocorrelation |
| <img src="swatch/fault_thrust_observed.svg" width="200" alt=""> | Fault, thrust observed | `fault_thrust_observed` | autocorrelation |
| <img src="swatch/incrop_of_fault_at_unconformity_sub_triassic.svg" width="200" alt=""> | Incrop of fault at unconformity (sub-Triassic) | `incrop_of_fault_at_unconformity_sub_triassic` | full swatch |
| <img src="swatch/fault_normal_inferred.svg" width="200" alt=""> | Fault, normal inferred | `fault_normal_inferred` | full swatch |
| <img src="swatch/fault_normal_observed.svg" width="200" alt=""> | Fault, normal observed | `fault_normal_observed` | full swatch |
| <img src="swatch/fault_reverse.svg" width="200" alt=""> | Fault, reverse | `fault_reverse` | full swatch |
| <img src="swatch/fault_shearing_zone_inferred.svg" width="200" alt=""> | Fault shearing zone, inferred | `fault_shearing_zone_inferred` | autocorrelation |
| <img src="swatch/fault_shearing_zone_observed.svg" width="200" alt=""> | Fault shearing zone, observed | `fault_shearing_zone_observed` | autocorrelation |
| <img src="swatch/fault_strike_slip.svg" width="200" alt=""> | Fault, strike-slip | `fault_strike_slip` | full swatch |
| <img src="swatch/fault_thrust_or_slide_inferred.svg" width="200" alt=""> | Fault, thrust or slide, inferred | `fault_thrust_or_slide_inferred` | autocorrelation |
| <img src="swatch/fossil_horizon_algal_band.svg" width="200" alt=""> | Fossil horizon, algal band | `fossil_horizon_algal_band` | autocorrelation |
| <img src="swatch/fossil_horizon_brachiopod_band.svg" width="200" alt=""> | Fossil horizon, brachiopod band | `fossil_horizon_brachiopod_band` | decoration spacing |
| <img src="swatch/fossil_horizon_coral_band.svg" width="200" alt=""> | Fossil horizon, coral band | `fossil_horizon_coral_band` | autocorrelation |
| <img src="swatch/fossil_horizon_eustheria_band.svg" width="200" alt=""> | Fossil horizon, eustheria band | `fossil_horizon_eustheria_band` | autocorrelation |
| <img src="swatch/fossil_horizon_lingula_band.svg" width="200" alt=""> | Fossil horizon, lingula band | `fossil_horizon_lingula_band` | autocorrelation |
| <img src="swatch/fossil_horizon_planolites_band.svg" width="200" alt=""> | Fossil horizon, planolites band | `fossil_horizon_planolites_band` | autocorrelation |
| <img src="swatch/geological_boundary_artificial.svg" width="200" alt=""> | Geological boundary, artificial | `geological_boundary_artificial` | autocorrelation |
| <img src="swatch/geological_boundary_drift.svg" width="200" alt=""> | Geological boundary, drift | `geological_boundary_drift` | autocorrelation |
| <img src="swatch/geological_boundary_mass_movement.svg" width="200" alt=""> | Geological boundary, mass movement | `geological_boundary_mass_movement` | autocorrelation |
| <img src="swatch/geological_boundary_solid_inferred.svg" width="200" alt=""> | Geological boundary, solid inferred | `geological_boundary_solid_inferred` | autocorrelation |
| <img src="swatch/geological_boundary_solid_intrusive.svg" width="200" alt=""> | Geological boundary, solid intrusive | `geological_boundary_solid_intrusive` | autocorrelation |
| <img src="swatch/geological_boundary_solid_intrusive_observed.svg" width="200" alt=""> | Geological boundary, solid intrusive observed | `geological_boundary_solid_intrusive_observed` | autocorrelation |
| <img src="swatch/geological_boundary_solid_observed.svg" width="200" alt=""> | Geological boundary, solid observed | `geological_boundary_solid_observed` | autocorrelation |
| <img src="swatch/glacial_meltwater_or_overflow_channel_centre_line.svg" width="200" alt=""> | Glacial meltwater or overflow channel, centre line | `glacial_meltwater_or_overflow_channel_centre_line` | full swatch |
| <img src="swatch/glacial_meltwater_channel_margins.svg" width="200" alt=""> | Glacial meltwater channel margins | `glacial_meltwater_channel_margins` | autocorrelation |
| <img src="swatch/hydrothermal.svg" width="200" alt=""> | Hydrothermal | `hydrothermal` | autocorrelation |
| <img src="swatch/igneous_cutting_margin_crossmarks_on_side_of_younger_rock_inferred.svg" width="200" alt=""> | Igneous cutting margin, crossmarks on side of younger rock, inferred | `igneous_cutting_margin_crossmarks_on_side_of_younger_rock_inferred` | autocorrelation |
| <img src="swatch/igneous_cutting_margin_observed.svg" width="200" alt=""> | Igneous cutting margin, observed | `igneous_cutting_margin_observed` | autocorrelation |
| <img src="swatch/igneous_plutons.svg" width="200" alt=""> | Igneous plutons | `igneous_plutons` | autocorrelation |
| <img src="swatch/incrop_of_coal.svg" width="200" alt=""> | Incrop of coal | `incrop_of_coal` | autocorrelation |
| <img src="swatch/incrop_of_marine_band.svg" width="200" alt=""> | Incrop of marine band | `incrop_of_marine_band` | autocorrelation |
| <img src="swatch/ironstone_inferred.svg" width="200" alt=""> | Ironstone, inferred | `ironstone_inferred` | autocorrelation |
| <img src="swatch/ironstone_observed.svg" width="200" alt=""> | Ironstone, observed | `ironstone_observed` | autocorrelation |
| <img src="swatch/kettle_hole.svg" width="200" alt=""> | Kettle hole | `kettle_hole` | autocorrelation |
| <img src="swatch/limit_of_diorite_grandiorite.svg" width="200" alt=""> | Limit of diorite / grandiorite | `limit_of_diorite_grandiorite` | autocorrelation |
| <img src="swatch/limit_of_glacial_advance_gosforth_oscillation_limit.svg" width="200" alt=""> | Limit of glacial advance, Gosforth oscillation limit | `limit_of_glacial_advance_gosforth_oscillation_limit` | autocorrelation |
| <img src="swatch/limit_of_glacial_advance_scottish_readvance_limit.svg" width="200" alt=""> | Limit of glacial advance, Scottish readvance limit | `limit_of_glacial_advance_scottish_readvance_limit` | autocorrelation |
| <img src="swatch/limit_of_granite_pegmatite_vein_complex_within_area_of_veining.svg" width="200" alt=""> | Limit of granite / pegmatite vein complex, x π within area of veining | `limit_of_granite_pegmatite_vein_complex_within_area_of_veining` | autocorrelation |
| <img src="swatch/limit_of_granite_vein_complex.svg" width="200" alt=""> | Limit of granite vein complex | `limit_of_granite_vein_complex` | autocorrelation |
| <img src="swatch/limit_of_migmatisation_towards_migmatites.svg" width="200" alt=""> | Limit of migmatisation, ∧ towards migmatites | `limit_of_migmatisation_towards_migmatites` | autocorrelation |
| <img src="swatch/limit_of_transgressive_pegmatite_veins_within_areas_of_veins.svg" width="200" alt=""> | Limit of transgressive pegmatite veins, π within areas of veins | `limit_of_transgressive_pegmatite_veins_within_areas_of_veins` | autocorrelation |
| <img src="swatch/lineament_probably_fracture_related.svg" width="200" alt=""> | Lineament, probably fracture related | `lineament_probably_fracture_related` | autocorrelation |
| <img src="swatch/line_of_split_coal_seam_ornament_on_split_side.svg" width="200" alt=""> | Line of split coal seam, ornament on split side | `line_of_split_coal_seam_ornament_on_split_side` | autocorrelation |
| <img src="swatch/magnetic_layer_or_boundary.svg" width="200" alt=""> | Magnetic layer or boundary | `magnetic_layer_or_boundary` | autocorrelation |
| <img src="swatch/man_made_deposit_boundary.svg" width="200" alt=""> | Man made deposit boundary | `man_made_deposit_boundary` | autocorrelation |
| <img src="swatch/marine_band.svg" width="200" alt=""> | Marine band | `marine_band` | autocorrelation |
| <img src="swatch/marked_break_in_slope_arrowheads_denote_uphill_side.svg" width="200" alt=""> | Marked break in slope, arrowheads denote uphill side | `marked_break_in_slope_arrowheads_denote_uphill_side` | autocorrelation |
| <img src="swatch/mass_movement_boundary.svg" width="200" alt=""> | Mass Movement boundary | `mass_movement_boundary` | autocorrelation |
| <img src="swatch/metamorphic_aureole_towards_intrusion.svg" width="200" alt=""> | Metamorphic aureole, + towards intrusion | `metamorphic_aureole_towards_intrusion` | autocorrelation |
| <img src="swatch/metamorphic_zone_boundary_with_mineral_or_zone_number.svg" width="200" alt=""> | Metamorphic zone boundary with mineral or zone number | `metamorphic_zone_boundary_with_mineral_or_zone_number` | full swatch |
| <img src="swatch/mineral_vein_with_name_of_mineral.svg" width="200" alt=""> | Mineral vein, with name of mineral | `mineral_vein_with_name_of_mineral` | full swatch |
| <img src="swatch/mining_area_subsurface.svg" width="200" alt=""> | Mining area, subsurface | `mining_area_subsurface` | autocorrelation |
| <img src="swatch/mussel_band.svg" width="200" alt=""> | Mussel band | `mussel_band` | autocorrelation |
| <img src="swatch/oil_shale_inferred.svg" width="200" alt=""> | Oil-shale, inferred | `oil_shale_inferred` | autocorrelation |
| <img src="swatch/oil_shale_observed.svg" width="200" alt=""> | Oil-shale, observed | `oil_shale_observed` | autocorrelation |
| <img src="swatch/outer_edge_of_terrace.svg" width="200" alt=""> | Outer edge of terrace | `outer_edge_of_terrace` | autocorrelation |
| <img src="swatch/quarry.svg" width="200" alt=""> | Quarry | `quarry` | autocorrelation |
| <img src="swatch/sandstone_bed.svg" width="200" alt=""> | Sandstone bed | `sandstone_bed` | autocorrelation |
| <img src="swatch/subsidence_hollow_drift_not_corresponding.svg" width="200" alt=""> | Subsidence hollow, drift (not corresponding) | `subsidence_hollow_drift_not_corresponding` | autocorrelation |
| <img src="swatch/subsidence_hollow_corresponding_to_drift_boundary.svg" width="200" alt=""> | Subsidence hollow, corresponding to drift boundary | `subsidence_hollow_corresponding_to_drift_boundary` | autocorrelation |
| <img src="swatch/subsidence_hollow_solid_not_corresponding.svg" width="200" alt=""> | Subsidence hollow, solid (not corresponding) | `subsidence_hollow_solid_not_corresponding` | autocorrelation |
| <img src="swatch/subsidence_hollow_corresponding_to_solid_boundary.svg" width="200" alt=""> | Subsidence hollow, corresponding to solid boundary | `subsidence_hollow_corresponding_to_solid_boundary` | autocorrelation |
| <img src="swatch/tonstein.svg" width="200" alt=""> | Tonstein | `tonstein` | autocorrelation |
| <img src="swatch/trace_of_lower_hinge_of_major_monocline.svg" width="200" alt=""> | Trace of lower hinge of major monocline | `trace_of_lower_hinge_of_major_monocline` | autocorrelation |
| <img src="swatch/trace_of_upper_hinge_of_major_monocline.svg" width="200" alt=""> | Trace of upper hinge of major monocline | `trace_of_upper_hinge_of_major_monocline` | decoration spacing |
| <img src="swatch/unconformity_marginalia_only.svg" width="200" alt=""> | Unconformity ( marginalia only ) | `unconformity_marginalia_only` | autocorrelation |

# pylint: disable=line-too-long  # This is data, not code
PROFILE = {
    "include_profiles": ["opentype"],
    "sections": {
        "Superfamily Checks": [
            "superfamily/list",
            "superfamily/vertical_metrics",
        ],
        "UFO Sources": [
            "designspace_has_consistent_codepoints",
            "designspace_has_consistent_glyphset",
            "designspace_has_consistent_groups",
            "designspace_has_default_master",
            "designspace_has_sources",
            "ufolint",
            # "ufo_consistent_curve_type",  # FIXME (orphan check) https://github.com/fonttools/fontbakery/pull/4809
            "ufo_features_default_languagesystem",
            # "ufo_no_open_corners",  # FIXME (orphan check) https://github.com/fonttools/fontbakery/pull/4809
            "ufo_recommended_fields",
            "ufo_required_fields",
            "ufo_unnecessary_fields",
        ],
        "Universal Profile Checks": [
            "alt_caron",
            "arabic_high_hamza",
            "arabic_spacing_symbols",
            # "caps_vertically_centered",  # Disabled: issue #4274
            "case_mapping",
            "cjk_chws_feature",
            "cjk_not_enough_glyphs",
            "cmap/format_12",
            "color_cpal_brightness",
            "colorfont_tables",
            "contour_count",
            "empty_glyph_on_gid1_for_colrv0",
            "empty_letters",
            "family/control_chars",
            "family/single_directory",
            "family/vertical_metrics",
            "family/win_ascent_and_descent",
            "fvar_name_entries",
            "file_size",
            "fontbakery_version",
            "fontdata_namecheck",
            "freetype_rasterizer",
            "glyf_nested_components",
            "gpos7",
            "gsub/smallcaps_before_ligatures",
            "hinting_impact",
            "inconsistencies_between_fvar_stat",
            "integer_ppem_if_hinted",
            "interpolation_issues",
            "legacy_accents",
            "ligature_carets",
            "linegaps",
            "kerning_for_non_ligated_sequences",
            "mandatory_avar_table",
            "mandatory_glyphs",
            "math_signs_width",
            "missing_small_caps_glyphs",
            "name/ascii_only_entries",
            "name/family_and_style_max_length",
            "name/trailing_spaces",
            "no_debugging_tables",
            "no_mac_entries",
            "os2_metrics_match_hhea",
            "ots",
            "required_tables",
            "render_own_name",
            "rupee",
            "sfnt_version",
            "smart_dropout",
            "soft_hyphen",
            "STAT_in_statics",
            "STAT_strings",
            "stylisticset_description",
            "tabular_kerning",
            "transformed_components",
            "ttx_roundtrip",
            "typoascender_exceeds_Agrave",
            "typographic_family_name",
            "unique_glyphnames",
            "unreachable_glyphs",
            "unwanted_aat_tables",
            "unwanted_tables",
            "valid_glyphnames",
            "varfont/consistent_axes",
            "vtt_volt_data",  # very similar to vttclean, may be a good idea to merge them.
            "vttclean",
            "whitespace_glyphnames",
            "whitespace_glyphs",
            "whitespace_ink",
            "whitespace_widths",
        ],
    },
    "configuration_defaults": {
        "file_size": {
            "WARN_SIZE": 1 * 1024 * 1024,
            "FAIL_SIZE": 9 * 1024 * 1024,
        }
    },
}

PROFILE = {
    "include_profiles": ["opentype"],
    "sections": {
        "Superfamily Checks": [
            "com.google.fonts/check/superfamily/list",
            "com.google.fonts/check/superfamily/vertical_metrics",
        ],
        "UFO Sources": [
            # FIXME (orphan check): "com.daltonmaag/check/consistent_curve_type",
            #                       https://github.com/fonttools/fontbakery/pull/4809
            "com.google.fonts/check/designspace_has_sources",
            "com.google.fonts/check/designspace_has_default_master",
            "com.google.fonts/check/designspace_has_consistent_glyphset",
            "com.google.fonts/check/designspace_has_consistent_codepoints",
            "com.thetypefounders/check/features_default_languagesystem",
            # FIXME (orphan check): "com.daltonmaag/check/no_open_corners",
            "com.daltonmaag/check/ufolint",
            "com.daltonmaag/check/ufo_required_fields",
            "com.daltonmaag/check/ufo_recommended_fields",
            "com.daltonmaag/check/ufo_unnecessary_fields",
            "com.daltonmaag/check/designspace_has_consistent_groups",
        ],
        "Universal Profile Checks": [
            "com.google.fonts/check/aat",
            "com.google.fonts/check/alt_caron",
            "com.google.fonts/check/arabic_high_hamza",
            "com.google.fonts/check/arabic_spacing_symbols",
            # "com.google.fonts/check/caps_vertically_centered",  # Disabled: issue #4274
            "com.google.fonts/check/case_mapping",
            "com.google.fonts/check/cjk_chws_feature",
            "com.google.fonts/check/contour_count",
            "com.google.fonts/check/family/single_directory",
            "com.google.fonts/check/family/vertical_metrics",
            "com.google.fonts/check/family/win_ascent_and_descent",
            "com.google.fonts/check/fontbakery_version",
            "com.adobe.fonts/check/freetype_rasterizer",
            "com.google.fonts/check/gpos7",
            "com.google.fonts/check/gsub/smallcaps_before_ligatures",
            "com.google.fonts/check/interpolation_issues",
            "com.google.fonts/check/legacy_accents",
            "com.google.fonts/check/linegaps",
            "com.google.fonts/check/mandatory_glyphs",
            "com.google.fonts/check/math_signs_width",
            "com.google.fonts/check/name/trailing_spaces",
            "com.google.fonts/check/os2_metrics_match_hhea",
            "com.google.fonts/check/ots",
            "com.google.fonts/check/required_tables",
            "com.google.fonts/check/rupee",
            "com.adobe.fonts/check/sfnt_version",
            "com.google.fonts/check/soft_hyphen",
            "com.google.fonts/check/STAT_in_statics",
            "com.google.fonts/check/STAT_strings",
            "com.google.fonts/check/tabular_kerning",
            "com.google.fonts/check/transformed_components",
            "com.google.fonts/check/ttx_roundtrip",
            "com.arrowtype.fonts/check/typoascender_exceeds_Agrave",
            "com.google.fonts/check/unique_glyphnames",
            "com.google.fonts/check/unreachable_glyphs",
            "com.google.fonts/check/unwanted_tables",
            "com.google.fonts/check/valid_glyphnames",
            "com.google.fonts/check/whitespace_glyphnames",
            "com.google.fonts/check/whitespace_glyphs",
            "com.google.fonts/check/whitespace_ink",
            "com.google.fonts/check/whitespace_widths",
        ],
    },
}

# pylint: disable=line-too-long  # This is data, not code
PROFILE = {
    "include_profiles": ["universal"],
    "pending_review": [
        "cmap/format_12",
        "empty_letters",
        "inconsistencies_between_fvar_stat",
        "no_mac_entries",
        "typographic_family_name",
        "vtt_volt_data",  # very similar to vttclean, may be a good idea to merge them.
    ],
    "sections": {
        "Article Checks": [
            "googlefonts:article/images",
        ],
        "Metadata Checks": [
            "googlefonts:metadata/axisregistry_bounds",
            "googlefonts:metadata/axisregistry_valid_tags",
            "googlefonts:metadata/broken_links",
            "googlefonts:metadata/canonical_style_names",
            "googlefonts:metadata/canonical_weight_value",
            "googlefonts:metadata/can_render_samples",
            "googlefonts:metadata/category",
            "googlefonts:metadata/category_hints",
            "googlefonts:metadata/consistent_axis_enumeration",
            "googlefonts:metadata/consistent_repo_urls",
            "googlefonts:metadata/copyright",
            "googlefonts:metadata/date_added",
            "googlefonts:metadata/designer_profiles",
            "googlefonts:metadata/designer_values",
            "googlefonts:metadata/empty_designer",
            "googlefonts:metadata/escaped_strings",
            "googlefonts:metadata/family_directory_name",
            "googlefonts:metadata/familyname",
            "googlefonts:metadata/filenames",
            "googlefonts:metadata/has_regular",
            "googlefonts:metadata/includes_production_subsets",
            "googlefonts:metadata/license",
            "googlefonts:metadata/match_filename_postscript",
            "googlefonts:metadata/match_fullname_postscript",
            "googlefonts:metadata/match_name_familyname",
            "googlefonts:metadata/match_weight_postscript",
            "googlefonts:metadata/menu_and_latin",
            "googlefonts:metadata/minisite_url",
            "googlefonts:metadata/nameid/family_and_full_names",
            "googlefonts:metadata/nameid/font_name",
            "googlefonts:metadata/nameid/post_script_name",
            "googlefonts:metadata/os2_weightclass",
            "googlefonts:metadata/parses",
            "googlefonts:metadata/primary_script",
            "googlefonts:metadata/regular_is_400",
            "googlefonts:metadata/reserved_font_name",
            "googlefonts:metadata/single_cjk_subset",
            "googlefonts:metadata/subsets_order",
            "googlefonts:metadata/undeclared_fonts",
            "googlefonts:metadata/unique_full_name_values",
            "googlefonts:metadata/unique_weight_style_pairs",
            "googlefonts:metadata/unreachable_subsetting",
            "googlefonts:metadata/unsupported_subsets",
            "googlefonts:metadata/valid_filename_values",
            "googlefonts:metadata/valid_full_name_values",
            "googlefonts:metadata/valid_nameid25",
            "googlefonts:metadata/valid_post_script_name_values",
        ],
        "Glyphset Checks": [
            "googlefonts:glyphsets/shape_languages",
        ],
        "Description Checks": [
            "googlefonts:description/broken_links",
            "googlefonts:description/eof_linebreak",
            "googlefonts:description/family_update",
            "googlefonts:description/git_url",
            "googlefonts:description/has_article",
            "googlefonts:description/has_unsupported_elements",
            "googlefonts:description/min_length",
            "googlefonts:description/urls",
            "googlefonts:description/valid_html",
        ],
        "Family Checks": [
            "googlefonts:family/equal_codepoint_coverage",
            "googlefonts:family/has_license",
            "googlefonts:family/italics_have_roman_counterparts",
            "googlefonts:family/tnum_horizontal_metrics",
        ],
        "Name table checks": [
            "googlefonts:name/family_name_compliance",
            "googlefonts:name/license",
            "googlefonts:name/license_url",
            "googlefonts:name/line_breaks",
            "googlefonts:name/rfn",
            "googlefonts:name/unwanted_chars",
        ],
        "Repository Checks": [
            "googlefonts:license/OFL_body_text",
            "googlefonts:license/OFL_copyright",
            "googlefonts:repo/dirname_matches_nameid_1",
            "googlefonts:repo/fb_report",
            "googlefonts:repo/sample_image",
            "googlefonts:repo/upstream_yaml_has_required_fields",
            "googlefonts:repo/vf_has_static_fonts",
            "googlefonts:repo/zip_files",
        ],
        "Shaping Checks": [
            "dotted_circle",
            "shaping/collides",
            "shaping/forbidden",
            "shaping/regression",
            "soft_dotted",
        ],
        "Outline Checks": [
            "outline_alignment_miss",
            "outline_colinear_vectors",
            "outline_direction",
            "outline_jaggy_segments",
            "outline_semi_vertical",
            "outline_short_segments",
        ],
        "Font File Checks": [
            "googlefonts:axisregistry/fvar_axis_defaults",
            "googlefonts:canonical_filename",
            "googlefonts:cjk_vertical_metrics",
            "googlefonts:cjk_vertical_metrics_regressions",
            "googlefonts:epar",
            "googlefonts:font_copyright",
            "googlefonts:font_names",
            "googlefonts:fstype",
            "googlefonts:fvar_instances",
            "googlefonts:gasp",
            "googlefonts:glyph_coverage",
            "googlefonts:has_ttfautohint_params",
            "googlefonts:meta/script_lang_tags",
            "googlefonts:name/description_max_length",
            "googlefonts:name/familyname_first_char",
            "googlefonts:name/mandatory_entries",
            "googlefonts:name/version_format",
            "googlefonts:old_ttfautohint",
            "googlefonts:os2/use_typo_metrics",
            "googlefonts:production_glyphs_similarity",
            # "googlefonts:production_encoded_glyphs",  # DISABLED
            "googlefonts:STAT",
            "googlefonts:STAT/axis_order",
            "googlefonts:STAT/axisregistry",
            "googlefonts:unitsperem",
            "googlefonts:usweightclass",
            "googlefonts:varfont/bold_wght_coord",
            "googlefonts:varfont/duplicate_instance_names",
            "googlefonts:varfont/generate_static",
            "googlefonts:varfont/has_HVAR",
            "googlefonts:vendor_id",
            "googlefonts:version_bump",
            "googlefonts:vertical_metrics",
            "googlefonts:vertical_metrics_regressions",
            #
            "cjk_not_enough_glyphs",
            "color_cpal_brightness",
            "colorfont_tables",
            "empty_glyph_on_gid1_for_colrv0",
            "file_size",
            "integer_ppem_if_hinted",
            "ligature_carets",
            "name/ascii_only_entries",
            "varfont/duplexed_axis_reflow",
            "varfont/instances_in_order",
            "varfont/unsupported_axes",
        ],
    },
    "configuration_defaults": {
        "file_size": {
            "WARN_SIZE": 1 * 1024 * 1024,
            "FAIL_SIZE": 9 * 1024 * 1024,
        }
    },
    "overrides": {
        "linegaps": [
            {
                "code": "hhea",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs.",
            },
            {
                "code": "OS/2",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs.",
            },
        ],
        "opentype:italic_angle": [
            {
                "code": "positive",
                "status": "FAIL",
                "reason": "Google Fonts has different policies on checking for italic angle.",
            },
            {
                "code": "negative",
                "status": "FAIL",
                "reason": "Google Fonts has different policies on checking for italic angle.",
            },
            {
                "code": "over-30-degrees",
                "status": "FAIL",
                "reason": "Google Fonts has different policies on checking for italic angle.",
            },
        ],
        "opentype:italic_axis_in_stat_is_boolean": [
            {
                "code": "wrong-ital-axis-value",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs",
            },
            {
                "code": "wrong-ital-axis-flag",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs",
            },
            {
                "code": "wrong-ital-axis-linkedvalue",
                "status": "FAIL",
                "reason": "For Google Fonts, all messages from this check are considered FAILs",
            },
        ],
        "opentype:italic_axis_last": [
            {
                "code": "ital-axis-not-last",
                "status": "FAIL",
                "reason": "For Google Fonts, the 'ital' axis must be last in the axes order.",
            },
        ],
        "alt_caron": [
            {
                "code": "bad-mark",
                "status": "FAIL",
                "reason": "For Google Fonts, one of the comma-lookalikes is a FAIL",
            },
        ],
    },
}

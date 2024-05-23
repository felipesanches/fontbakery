## Summary April & May 2024
### Notes
  - Fixed race condition with `--auto-jobs` caused by the current working directory changing (issue #4700)
  - When multi-threading is enabled, we now ensure that the font objects are fully loaded before running the checks. This causes an initial delay but avoids some code concurrency issues. (issue #4638)
  - Add back the `--list-subcommands` option that had been removed by mistake on v0.12.0 (issue #4685)
  - Fix ordering of log-messages on reports to show FAILs at the top. (issue #4672)
  - Fixed bug where some checks would modify the font under test and make other checks fail (issue #4678)
  - 2024-Apr-17: Unpin `glyphsets` dependency and fix `fontbakery.com` (issue #4639)
  - 2024-Apr-15: Temporarily pin glyphsets dependency to version v0.6.17 until a failing assert is addressed (issue #4639)
  - 2024-Apr-15: **com.google.fonts/check/tabular_kerning** (Universal profile) will remain experimental for a bit longer (issue #4640)
  - Restablish ordering of results on github markdown reports, showing the more severe results (such as FAILs) at the top. (issue #4600)
  - Set exit code when called from `__main__.py`. (issue #4633)
  - Support setting `configuration` in input TOML for `update_shaping_tests`. (issue #4635)
  - Fix Github Markdown syntax. (issue #4627)
  - Documentation for profile and check writers has been rewritten.
  - Implement a basic tool to update regression test files. See https://github.com/fonttools/fontbakery/discussions/4589 for details. Run like `python -m fontbakery.update_shaping_tests input.toml output.json path/to/*.ttf`.


### New Profile
  - On the week of April 22nd, a new profile was added for Microsoft fonts. (PR #4657)

### Promotion of previously experimental checks
#### Made effective on the FontWerk profile
  - * **com.fontwerk/check/names_match_default_fvar** After being marked as **experimental** for 10 weeks since the v0.12.0a1 release (PRs #3604 / #3698)

### Promotion of previously experimental checks
  2024-Apr-12: After being marked as **experimental** for 9 weeks since the v0.11.1 release, these checks are now made effective.
  For more details, see their previous entries on the changelog.

#### Made effective on the Open Type profile
  - * **com.typenetwork/check/varfont/ital_range** (PR #4402)
  - * **com.google.fonts/check/varfont/family_axis_ranges** (issue #4554)

#### Made effective on the Universal profile
  - * **com.google.fonts/check/tabular_kerning** (issue #4440)
  - * **com.google.fonts/check/case_mapping** (issue #3230)


### New checks
#### Added to the Outline profile (included in GFonts profile)
  - **[com.google.fonts/check/outline_direction]:** Check that outermost contours of glyphs have a clockwise direction. (issue #2056)

#### Added to the Google Fonts profile
  - **EXPERIMENTAL - [com.google.fonts/check/article/images]:** Validate maximum filesize and resolution of images in the article/images directory. (issue #4594)
  - **EXPERIMENTAL - [com.google.fonts/check/varfont/instances_in_order]:** Ensure that the fvar table instances are in ascending order of weight. (issue #3334)
  - **EXPERIMENTAL - [com.google.fonts/check/metadata/date_added]:** Check that the date_added field is not empty or malformed. (issue #4729)


### Changes to existing checks
#### On the Universal profile (included in GFonts profile)
  - **[com.google.fonts/check/tabular_kerning]:** Fixed race condition / bug where the check would modify the cmap of the font being checked (issue #4697)
  - **[com.google.fonts/check/legacy_accents]:** Re-enabled check but dropped complaints about legacy accents as part of glyph compositions (issue #4567)
  - **[com.google.fonts/check/interpolation_issues]:** We had forgotten to display the glyph name (issue #4659)
  - **[com.google.fonts/check/tabular_kerning]:** Eliminated some false positives in Ubuntu Sans related to digraphs. (PR #4579)
  - **[com.google.fonts/check/ttx_roundtrip]:** Fix multithreading conflict when using `--auto-jobs` and running this check (issue #4481)
  - **[com.google.fonts/check/arabic_high_hamza]:** Fixed detection of glyphs by codepoint. And fixed a code-typo, to also check for high hamza glyph. (issue #4539)
  - **[com.google.fonts/check/interpolation_issues]:** Also detect kinks and contours becoming overweight or underweight. (issue #4388)
  - **[com.google.fonts/check/case_mapping]:** Only check letters. As per David Corbett's suggestion, we now check for unicode category = "L*". (issue #4733)


#### On the OpenType profile (included in GFonts profile)
  - **[com.google.fonts/check/monospace]:** Fix ERROR when accessing the 4th bit of panose (spacing) when family type is LATIN_HAND_WRITTEN or LATIN_SYMBOL. FontTools still calls it 'bProportion' even though the proper name should be 'bSpacing' (issue #2857)
  - **[com.microsoft/check/tnum_glyphs_equal_widths]:** Fix shaping error under certain conditions (PR #4689)
  - **[com.google.fonts/check/caret_slope]:** Downgrade "caretslope-mismatch" from FAIL to WARN. (issue #4679)


#### On the Outline profile (included in GFonts profile)
  - **[com.google.fonts/check/outline_direction]:** fixed float division by zero error, by bumping the `beziers` dependency to a version that includes the necessary fix. (issue #4699)
  - Checks now check unencoded glyphs as well as encoded glyphs. (issue #2056)
  - **[com.google.fonts/check/outline_direction]:** fixed an error where the outermost path was not correctly detected. (issue #4719)


#### On the Google Fonts profile
  - Checks which validate the description files now also validate article files (issue #4730)
  - **[com.google.font/check/description/unsupported_elements]:** Also checks for wellformedness of HTML video tags. (issue #4730)
  - **[com.google.font/check/description/has_article]:** yield INFO when a non-Noto font doesn' t have an article. Also, an empty description file is not needed anymore (issue #4702)
  - **[com.google.fonts/check/fvar_instances]:** Fix markdown table formatting. (issue #4675)
  - **[com.google.fonts/check/missing_small_caps_glyphs]:** Fix ERROR: Handle LookupType 2, which maps to more than a single glyph. (issue #4677)
  - **EXPERIMENTAL [com.google.fonts/check/varfont/instances_in_order]:** Fix an ERROR caused by a list IndexError (issue #4626)
  - [com.google.fonts/check/description/noto_has_article]:** This check has been renamed to `description/has_article` and also checks that fonts with article files have an empty description. (issue #4318)


#### On the Type Network profile
  - **[com.typenetwork/check/glyph_coverage]:** Added minus sign to min charset. (PR #4701)
  - **[com.typenetwork/check/usweightclass]:** Updated `tn_expected_os2_weight` condition. (issue #4694 / PR #4701)
  - **[com.google.fonts/check/outline_alignment_miss]:** Extended to work even when OS/2 version is < 2 (PR #4655)
  - **[com.google.fonts/check/glyphsets/shape_languages]:** Refactor shape_languages and avoid repetition of messages. (issue #4646)
  - **[com.google.fonts/check/kerning_for_non_ligated_sequences]:** Correctly generate the list of ligated sequences the test warns about and do not include unligated sequences in it. (issue #2227)

#### On the FontWerk profile
  - **[com.fontwerk/check/style_linking]:** (also included in the `Type Network` profile). Adjust the `is_bold` condition to check for bold-adjacent style names with spaces, such as "Semi Bold" and "Extra Bold", and not consider such styles as "Bold" in the RIBBI sense. (issue #4667)
  - **[com.typenetwork/check/usweightclass]:** Update `tn_expected_os2_weight` condition and FAIL/WARN results (PR #4643)
  - Also temporarily removed the FontVal check. (PR #4643)

#### On the Microsoft profile
  - Make it independent of Universal and OpenType profiles by explicitly listing all needed checks instead of including the Universal profile. (PR #4712)




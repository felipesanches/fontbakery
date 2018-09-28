#!/usr/bin/env python3
# Copyright 2016 The Fontbakery Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def pretty_print_list(values):
  if len(values) == 1:
    return str(values[0])
  else:
    return "{} or {}".format(", ".join(map(str, values[:-1])),
                             str(values[-1]))


def get_bounding_box(font):
    """ Returns max and min bbox of given truetype font """
    ymin = 0
    ymax = 0
    if font.sfntVersion == 'OTTO':
        ymin = font['head'].yMin
        ymax = font['head'].yMax
    else:
        for g in font['glyf'].glyphs:
            char = font['glyf'][g]
            if hasattr(char, 'yMin') and ymin > char.yMin:
                ymin = char.yMin
            if hasattr(char, 'yMax') and ymax < char.yMax:
                ymax = char.yMax
    return ymin, ymax


def get_name_entries(font,
                     nameID,
                     platformID=None,
                     encodingID=None,
                     langID=None):
  results = []
  for entry in font['name'].names:
    if entry.nameID == nameID and \
       (platformID is None or entry.platformID == platformID) and \
       (encodingID is None or entry.platEncID == encodingID) and \
       (langID is None or entry.langID == langID):
      results.append(entry)
  return results


def get_name_entry_strings(font,
                           nameID,
                           platformID=None,
                           encodingID=None,
                           langID=None):
  entries = get_name_entries(font, nameID, platformID, encodingID, langID)
  return list(map(lambda e: e.string.decode(e.getEncoding()), entries))


def get_name_entry_string(font,
                          nameID,
                          platformID=None,
                          encodingID=None,
                          langID=None):
  values = get_name_entry_strings(font, nameID, platformID, encodingID, langID)
  if values:
    return values[0]
    #TODO: There should be a fontbakery check that ensures all occurrences of
    #      a given name id have identical string contents, so that is safe
    #      for us to simply use the zeroeth occurence here.
    #      I believe that having different strings would be a problem in the font.


def name_entry_id(name):
  from fontbakery.constants import (NAMEID_STR,
                                    PLATID_STR)
  return "[{}({}):{}({})]".format(NAMEID_STR[name.nameID],
                                  name.nameID,
                                  PLATID_STR[name.platformID],
                                  name.platformID)


def get_glyph_name(font, codepoint):
  # type: (fontTools.ttLib.TTFont, int) -> Optional[str]
  next_best_cmap = font.getBestCmap()

  if codepoint in next_best_cmap:
    return next_best_cmap[codepoint]

  return None


def glyph_contour_count(font, name):
    """Contour count for specified glyph.
    This implementation will also return contour count for
    composite glyphs.
    """
    contour_count = 0
    items = [font['glyf'][name]]

    while items:
        g = items.pop(0)
        if g.isComposite():
            for comp in g.components:
                items.append(font['glyf'][comp.glyphName])
        if g.numberOfContours != -1:
            contour_count += g.numberOfContours
    return contour_count


def get_font_glyph_data(font):
    """Return information for each glyph in a font"""
    from fontbakery.constants import (PLATFORM_ID__WINDOWS,
                                      PLAT_ENC_ID__UCS2)
    font_data = []

    try:
        subtable = font['cmap'].getcmap(PLATFORM_ID__WINDOWS,
                                        PLAT_ENC_ID__UCS2)
        if not subtable:
          # Well... Give it a chance here...
          # It may be using a different Encoding_ID value
          subtable = font['cmap'].tables[0]

        cmap = subtable.cmap
    except:
        return None

    cmap_reversed = dict(zip(cmap.values(), cmap.keys()))

    for glyph_name in font.getGlyphSet().keys():
        if glyph_name in cmap_reversed:
            uni_glyph = cmap_reversed[glyph_name]
            contours = glyph_contour_count(font, glyph_name)
            font_data.append({
                'unicode': uni_glyph,
                'name': glyph_name,
                'contours': {contours}
            })
    return font_data


def get_FamilyProto_Message(path):
  from fontbakery.fonts_public_pb2 import FamilyProto
  from google.protobuf import text_format
  message = FamilyProto()
  text_data = open(path, "rb").read()
  text_format.Merge(text_data, message)
  return message


def check_bit_entry(ttFont, table, attr, expected, bitmask, bitname):
  from fontbakery.message import Message
  from fontbakery.checkrunner import (PASS, FAIL)
  value = getattr(ttFont[table], attr)
  name_str = f"{table} {attr} {bitname} bit"
  if bool(value & bitmask) == expected:
    return PASS, f"{name_str} is properly set."
  else:
    if expected:
      expected_str = "set"
    else:
      expected_str = "reset"
    return FAIL, Message(f"bad-{bitname}",
                         f"{name_str} should be {expected_str}.")


def download_file(url):
  from urllib.request import urlopen
  from io import BytesIO
  return BytesIO(urlopen(url).read())


def glyph_has_ink(font, name):
  # type: (TTFont, Text) -> bool
  """Checks if specified glyph has any ink.

  That is, that it has at least one defined contour associated.
  Composites are considered to have ink if any of their components have ink.
  Args:
      font:       the font
      glyph_name: The name of the glyph to check for ink.
  Returns:
      True if the font has at least one contour associated with it.
  """
  glyph = font['glyf'].glyphs[name]
  glyph.expand(font['glyf'])

  if not glyph.isComposite():
    if glyph.numberOfContours == 0:
      return False
    (coords, _, _) = glyph.getCoordinates(font['glyf'])
    # you need at least 3 points to draw
    return len(coords) > 2

  # Check for ink in each sub-component.
  for glyph_name in glyph.getComponentNames(glyph.components):
    if glyph_has_ink(font, glyph_name):
      return True

  return False


def assert_results_contain(check_results, expected_status, expected_msgcode=None):
  """
  This helper function is useful when we want to make sure that
  a certain log message is emited by a check but it can be in any
  order among other log messages.
  """
  found = False
  for status, message in check_results:
    if status == expected_status and message.code == expected_msgcode:
      found = True
      break
  assert(found)

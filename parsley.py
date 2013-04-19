# -*- coding: utf-8 -*-

"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re
"""

import re

def parse(query):
  amount = [ "einige", "etwas", "nach belieben", "eine", "ein", "zwei",
             "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun",
             "zehn", "elf" ]

  regex = r"""
          ^
          ((?P<prefix> etwas|ca\.|ca|je   )\s)?
          ((?P<fraction> \d/\d|[½⅓¼¾] )\s)?
          ((?P<amount> .?[\d-]+(,\d+)? )\s)?
          ((?P<extra>
            ganzer?
            |voller?
            |kleiner?
            |gro(ss|ß)er?
            |viertel
            |drittel
            |dreiviertel)
          \s)?
          ((?P<unit>
            becher
            |bund
            |dose(\(n\)|n|/n)?
            |e(ss)?l(\.|(oe|ö)ffel)?
            |t(ee)?l(\.|(oe|ö)ffel)?
            |gl(ae|ä|a)s(er)?
            |(c(enti)?|m(ill?i)?)?l(\.|iter)?
            |(K(ilo)?|M(ill?i)?)?g(ramm)?
            |k(ä|ae)stchen
            |messerspitze(\(n\)|n|/n)?
            |stiel(\(e\)|e|/e)?
            |staude(\(n\)|n|/n)?
            |schuss
            |tropfen
            |pr(\.|isen?)?
            |packung(en)?|p(ae|ä)ckchen|pck\.?
            |st(\.|(ü|ue)ck(\.|chen)?)?

          )\s)?
          (?P<ingredient>.+?)
          $
  """
  match = re.search(regex, query, re.UNICODE|re.IGNORECASE|re.VERBOSE)
  return match

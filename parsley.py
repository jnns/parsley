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
  """
  This function expects a query string consisting of one line of an ingredient
  list from a recipe (which itself might consist of an amount, a unit, the
  ingredient and surplus info).

  As this function is used on our site http://restegourmet.de, the main focus
  in parsing instructions is to get the correct ingredient out. That's what
  matters, and only because of that we interested in recognizing
  amount and units correctly--because it helps us recognize which part makes
  up the ingredient.

  The following is expected behaviour:

  >>> parse('100g Rinderhackfleisch')
  'Rinderhackfleisch'
  >>> parse('666gr. Mehl')
  'Mehl'
  >>> parse('1 1/4 L Gemüsebrühe')
  'Gemüsebrühe'
  >>> parse('½ Zucchini')
  'Zucchini'
  >>> parse('1 große Zitrone')
  'Zitrone'
  >>> parse('ein halber Apfel')
  'Apfel'
  >>> parse('ca. 50-60g Margarine (Alsan)')
  'Margarine (Alsan)
  >>> parse('1-2 EL Sojamilch')
  'Sojamilch'
  >>> parse('etwas Petersilie, Schnittlauch oder Selleriegrün')
  'Petersilie, Schnittlauch oder Selleriegrün'
  >>> parse('einige Minzblätter')
  'Minzblätter'
  >>> parse('1 TL Thymianblätter (getrocknet oder frisch)')
  'Thymianblätter'
  >>> parse('grobes Meersalz')
  'grobes Meersalz'
  >>> parse('4cl trockene Sherry')
  'trockener Sherry'
  >>> parse('2 Stück Zitrone unbehandelt')
  'Zitrone unbehandelt'
  >>> parse('4 Stk. Peperoni')
  'Peperoni'
  >>> parse('1 Rolle Blätterteig')
  'Blätterteig'
  >>> parse('1 Packung (270g) Blätterteig, fertig ausgerollt')
  'Blätterteig'
  """


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
            |mittlerer?
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
            |st(ä|ae)ngel
            |staude(\(n\)|n|/n)?
            |schuss
            |tassen?
            |tropfen
            |pr(\.|isen?)?
            |packung(en)?|p(ae|ä)ckchen|pck\.?
            |st(\.|(ü|ue)ck(\.|chen)?)?

          )\s)?
          (?P<ingredient>.+?)
          $
  """
  match = re.search(regex, query, re.UNICODE|re.IGNORECASE|re.VERBOSE)
  if match:
    return match.groupdict().get("ingredient")
  return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

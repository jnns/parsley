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
  matters, and only because of that we are interested in recognizing
  amount and units correctly--because it helps us recognize which part makes
  up the ingredient.

  The following is expected behaviour:

  >>> parse('100g Rinderhackfleisch')
  'Rinderhackfleisch'
  >>> parse('666gr. Mehl')
  'Mehl'
  >>> parse('1 1/4 L Gemuesebruehe')
  'Gemuesebruehe'
  >>> parse('½ Zucchini')
  'Zucchini'
  >>> parse('1 große Zitrone')
  'Zitrone'
  >>> parse('ein halber Apfel')
  'Apfel'
  >>> parse('ca. 50-60g Margarine (Alsan)')
  'Margarine'
  >>> parse('1-2 EL Sojamilch')
  'Sojamilch'
  >>> parse('etwas Petersilie, Schnittlauch oder Selleriegruen')
  'Petersilie, Schnittlauch oder Selleriegruen'
  >>> parse('einige Minzblaetter')
  'Minzblaetter'
  >>> parse('1 TL Thymianblaetter (getrocknet oder frisch)')
  'Thymianblaetter'
  >>> parse('grobes Meersalz')
  'grobes Meersalz'
  >>> parse('4cl trockener Sherry')
  'trockener Sherry'
  >>> parse('2 Stueck Zitrone unbehandelt')
  'Zitrone unbehandelt'
  >>> parse('4 Stk. Peperoni')
  'Peperoni'
  >>> parse('1 Rolle Blaetterteig')
  'Blaetterteig'
  >>> parse('1 Packung (270g) Blaetterteig, fertig ausgerollt')
  'Blaetterteig'
  """

  query = re.sub("\(.*?\)", "", query) # delete everything within parentheses

  regex = r"""
        ^
        ((?P<prefix> etwas
          |ca\.?
          |je
          |Saft
          |Schale
          |ev(entuell|tl\.?|\.)?
        )\s)?
        ((?P<amount> (.?[\d-]+(,\d+)?
          |etwas
          |(nach Belieben)
          |ein(ig)?(er?)?
          |zwei
          |drei
          |vier
          |f(ue|ü)nf
          |sechs
          |sieben
          |acht
          |neun
          |zehn
          |elf))
        \s?)?
        ((?P<fraction> \d/\d|[½⅓¼¾] )\s)?
        ((?P<extra>
          ganzer?
          |volle(n|r)?
          |kleine(n|r)?
          |mittlere(n|r)?
          |halbe(n|r)?
          |(mittel)?gro(ss|ß)e(n|r)?
          |viertel
          |drittel
          |dreiviertel
          |reife(n|r)?
        )\s)?
        ((?P<unit>
          becher
          |bund
          |dose(\(n\)|n|/n)?
          |e(ss)?l(\.|(oe|ö)ffel)?
          |t(ee)?l(\.|(oe|ö)ffel)?
          |gl(ae|ä|a)s(er)?
          |h(a|ae|ä)nde?\s?voll
          |(c(enti)?|m(ill?i)?)?l(\.|iter)?
          |(K(ilo)?|M(ill?i)?)?g(r?\.|ramm)?
          |k(ä|ae)stchen
          |messerspitze(\(n\)|n|/n)?
          |packung(en)?|p(ae|ä)ckchen|pck\.?
          |pr(\.|isen?)?
          |rollen?
          |stiel(\(e\)|e|/e)?
          |st(ä|ae)ngel
          |staude(\(n\)|n|/n)?
          |schuss
          |spritzer
          |st(k?\.|(ü|ue)ck(\.|chen)?)?
          |tassen?
          |tropfen
        )\s)?
        (?P<ingredient>.+?)
        $
  """
  match = re.search(regex, query, re.UNICODE|re.IGNORECASE|re.VERBOSE)
  if match:
    return match.groupdict().get("ingredient").strip()
  return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

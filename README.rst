Parsley
=======

An small and simple ingredient parser
-------------------------------------

A small utility to parse ingredients from German recipe instructions using
Regular Expressions. Once it enters a mature state, we will use it in our site *Restegourmet* (a search engine for recipes based on ingredients):

`Was soll ich kochen? – restegourmet.de <http://restegourmet.de>`_

**Feel free to fork and extend this!** Other languages are very welcome too, but as we only crawl German sites, we don't plan on adding those ourselves.

Installation
------------

   pip install git+git://github.com/jnns/parsley.git#egg=parsley


Tests are included
------------------

Docstrings are included to test for correct behaviour and give you an
impression about what this regex does.

    >>> parse('100g Rinderhackfleisch')
    'Rinderhackfleisch'
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

For more information just take a look at parsley.py_.

.. _parsley.py: http://github.com/jnns/parsley/blob/master/parsley.py

Alternatives
------------

If you're looking for an English version, have a look at Ian C. Anderson's Ingreedy_ library for Ruby.

.. _Ingreedy: https://github.com/iancanderson/ingreedy



Regarding the name
------------------

I didn't want to go with a generic *ingredient-parser* or
something similar (despite many other projects having this name) because I would be the first to be confused whether I should use an underscore, a hyphen or nothing at all. And this being a parser for *food*, Parsley fits just too well.



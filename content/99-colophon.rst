========
Colophon
========

Sources
=======

L'écrite du présent ouvrage a été réalisée en utilisant `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`__, un langage utilisé pour l'écriture de documentation et largement utilisé  dans la communauté Python. Ce langage s'intègre dans le projet Docutils qui s'inspire d'outils tels que Javadoc. La compilation des sources est réalisée sous Sphinx, un paquet Python permettant de générer une documentation HTML ainsi qu'un ouvrage PDF via LaTeX.

Conventions
===========

Symbole d'égalité
-----------------

Le signe d'égalité ``=`` peut aisément être confondu avec l'opérateur d'affectation ``=`` utilisé en C. Dans certains exemples ou l'on montre une égalité entre différentes écritures, le signe d'égalité triple  (:unicode:`U+2261`) est utilisé pour faire disparaître toute ambiguïté:

.. code-block::

    'a' ≡ 0b1100001 ≡ 97 ≡ 0x61 ≡ 00141

Types de données
----------------

Les convention C s'appliquent à la manière d'exprimer les grandeurs suivantes:

- ``0xABCD`` pour les valeurs hexadécimales (``/0x[0-9a-f]+/i``)
- ``00217`` pour les valeurs octales (``/0[0-7]+/``)
- ``'c'`` pour les caractères (``/'([^']|\\[nrftvba'])'/``)
- ``123`` pour les grandeurs entières (``/-?[1-9][0-9]*/``)
- ``12.`` pour les grandeurs réelles à virgule flottante

Encodage de caractère
---------------------

Il est souvent fait mention dans ce cours la notation du type :unicode:`U+01AE`, il s'agit d'une notation unicode qui ne dépend pas d'un quelconque encodage. Parler du caractère ASCII 234 est incorrect car cela dépend de la table d'encodage utilisée. La notation unicode est exacte.

Références
==========

Les références utilisées dans cet ouvrage sont:

- Programming languages C - ISO/IEC 9899:TC3
- Le guide complet du langage C - Claude Delanoy, 844 pages (ISBN-13 978-2212140125)
- Le Langage C 2e edition - K&R, 304 pages (ISBN-13 978-2100715770)
- die.net - https://www.die.net
- wikipedia - https://www.wikipedia.org
- stackoverflow - https://stackoverflow.com

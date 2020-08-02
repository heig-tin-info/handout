
========
Colophon
========

Sources
=======

L'écriture du présent ouvrage a été réalisée en utilisant `reStructuredText <https://en.wikipedia.org/wiki/ReStructuredText>`__, un langage couramment utilisé pour l'écriture de documentation et largement utilisé dans la communauté Python. Ce langage s'intègre dans le projet Docutils qui s'inspire d'outils tels que Javadoc. La compilation des sources est réalisée sous Sphinx, un paquet Python permettant de générer une documentation HTML ainsi qu'un ouvrage PDF via LaTeX.

Conventions
===========

Symbole d'égalité
-----------------

Le signe d'égalité ``=`` peut aisément être confondu avec l'opérateur d'affectation ``=`` utilisé en C. Dans certains exemples ou l'on montre une égalité entre différentes écritures, le signe d'égalité triple  (:unicode:`U+2261`) est utilisé pour faire disparaître toute ambiguïté :

.. code-block::

    'a' ≡ 0b1100001 ≡ 97 ≡ 0x61 ≡ 00141

Symbole de remplissage
----------------------

Dans les exemples donnés, on voit régulièrement ``while (condition) { 〰 }`` ou ``〰`` (:unicode:`U+3030`) indique une continuité logique d'opération. Le symbole exprime ainsi ``...`` (`points de suspension <https://fr.wikipedia.org/wiki/Points_de_suspension>`__ ou *ellipsis*). Or pour ne pas confondre avec le symbole C ``...`` utilisé dans les fonctions à arguments variables tels que ``printf``.

Types de données
----------------

Les conventions C s'appliquent à la manière d'exprimer les grandeurs suivantes :

- ``0xABCD`` pour les valeurs hexadécimales (``/0x[0-9a-f]+/i``)
- ``00217`` pour les valeurs octales (``/0[0-7]+/``)
- ``'c'`` pour les caractères (``/'([^']|\\[nrftvba'])'/``)
- ``123`` pour les grandeurs entières (``/-?[1-9][0-9]*/``)
- ``12.`` pour les grandeurs réelles en virgule flottante

Encodage de caractère
---------------------

Il est souvent fait mention dans ce cours la notation du type :unicode:`U+01AE`, il s'agit d'une notation unicode qui ne dépend pas d'un quelconque encodage. Parler du caractère ASCII 234 est incorrect car cela dépend de la table d'encodage utilisée; en revanche, la notation unicode est exacte.


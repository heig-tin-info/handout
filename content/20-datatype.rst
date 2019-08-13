================
Types de données
================

Typage
======

Inhérent au fonctionnement interne de l'ordinateur, un langage de programmation s'abstrait plus ou moins du mode de stockage interne des données telles qu'elles sont enregistrées dans la mémoire. De la même manière que dans la vie réelle, il n'est pas possible de rendre de la monnaie à un vendeur à moins d'un cinquième de centime près, il n'est pas possible pour un ordinateur de stocker des informations numériques avec une précision infinie.

Aussi, les langages de programmation sont dits **typés** lorsqu'ils confient au programmeur la responsabilité de choisir comment une information sera stockée en mémoire, et **non typés** lorsque ce choix est implicite. Chacun des langages à ses avantages et ses inconvénients et pour reprendre l'exemple du rendu de monnaie, il serait ennuyant d'autoriser d'enregistrer des informations financières avec une précision meilleure qu'une pièce de cinq centimes, car il serait alors impossible à un caissier de rendre la monnaie correctement. Dans cette situation on préférera les langages **typés** et heureusement C est un langage fortement typé.

Les types de données ne se bornent pas qu'aux informations numériques, il existe des types plus complexes qui permettent par exemple de traiter des caractères tels que ``A`` ou ``B``. Ce chapitre à pour objectif de familiariser le lecteur aux différents types de données disponibles en C.

.. note:: Standard ISO

   Les ingénieurs sont friands des standards et qui plus est lorsqu'ils sont internationaux. Ainsi afin d'éviter le crash malheureux d'une fusée causé par la mésentente de deux ingénieurs de différents pays, il existe la norme **ISO 80000-2** qui définit précisément ce qu'est un entier, s'il doit inclure ou non le zéro, que sont les nombres réels, etc. Bien entendu les compilateurs, s'ils sont bien faits, cherchent à respecter au mieux ces normes internationales, et vous ?

.. _storage:

Stockage et interprétation
==========================

Rappelez-vous qu'un ordinateur ne peut stocker l'information que sous forme binaire et qu'il n'est à même de manipuler ces informations que par paquets de bytes. Aussi un ordinateur 64-bits manipulera avec aisance des paquets de 64-bits, mais plus difficilement des paquets de 32-bits. Ajoutons qu'il existe encore des microcontrôleurs 8-bits utilisés dans des dispositifs à faible consommation et qui peinent à manipuler des types de plus grande taille. Stocker une température avec une trop grande précision et effectuer des opérations mathématiques sur toute la précision serait une erreur, car le microcontrôleur n'est simplement pas adapté à manipuler ce type d'information.

Considérons le paquet de 32-bit suivant, êtes-vous à même d'en donner une signification?

.. code-block:: text

    01000000 01001001 01001001 11011011

Il pourrait s'agir:

- de 4 caractères de 8-bits:
    - ``01000000`` ``@``
    - ``01001001`` ``I``
    - ``01001001`` ``\x0f``
    - ``11011011`` ``Û``
- ou de 4 nombres de 8-bits: ``64``, ``73``, ``15``, ``219``,
- ou de deux nombres de 16-bits ``18752`` et ``56079``,
- ou alors un seul nombre de 32-bit ``3675212096``.
- Peut-être est-ce le nombre ``-4.033e16`` lu en *little endian*,
- ou encore ``3.141592`` lu en *big endian*.

Qu'en pensez-vous ?

Lorsque l'on souhaite programmer à bas niveau, vous voyez que la notion de type de donnée est essentielle, car en dehors d'une interprétation subjective: "c'est forcément PI la bonne réponse", rien ne permet à l'ordinateur d'interpréter convenablement l'information enregistrée en mémoire.

Le typage permet de résoudre toute ambiguïté.

.. _endianess:

Boutisme
========

.. figure:: ../assets/images/endian.*

La hantise de l'ingénieur bas-niveau c'est le boutisme aussi appelé *endianess*. Ce terme étrange a été popularisé par l'informaticien Dany Cohen en référence aux Voyages de Gulliver de Jonathan Swift. Dans ce conte les habitants de Lilliput refusent d'obéir à un décret obligeant à manger les oeufs à la coque par le petit bout (petit boutisme/*little endian*), la répression incite les rebelles à manger leurs oeufs par le gros bout (gros boutisme/*big endian*).

Aujourd'hui encore, il existe des microprocesseurs qui fonctionnent en *big endian* alors que d'autres sont en *little endian*. C'est à dire que si une information est stockée en mémoire comme suit:

.. code-block:: text

    [0x40, 0x49, 0xf, 0xdb]

Faut-il la lire de gauche à droite ou de droite à gauche? Cela vous paraît trivial, mais si cet exemple était mentionné dans un livre rédigé en arabe, quelle serait alors votre réponse ?

Imaginons qu'un programme exécuté sur un microcontrôleur *big-endian* 8-bit envoie par Bluetooth la valeur ``1'111'704'645``, qui correspond au nombre de photons ayant frappé un détecteur optique. Il transmet donc les 4 octets suivants: ``0x42, 0x43, 0x44, 0x45``. L'ordinateur qui reçoit les informations décode ``1'162'101'570``. Les deux ordinateurs n'interprètent pas les données de la même façon, et c'est un problème que la plupart des ingénieurs électroniciens rencontrent un jour dans leur carrière.

Les nombres entiers
===================

Les nombres entiers sont des nombres sans virgule et incluant le zéro. Ils peuvent donc être négatifs, nuls ou positifs. Mathématiquement ils appartiennent à l'ensemble des `entiers relatifs <https://fr.wikipedia.org/wiki/Entier_relatif>`__.

Comme aucun ordinateur ne dispose d'un espace de stockage infini, ces nombres excluent les infinis positifs et négatifs, et sont donc bornés, cela va de soi.

Les entiers naturels
--------------------

En mathématiques, un `entier naturel <https://fr.wikipedia.org/wiki/Entier_naturel>`__ est un nombre positif ou nul. Chaque nombre à un successeur unique et peut s'écrire avec une suite finie de chiffres en notation décimale positionnelle, et donc sans signe et sans virgule. L'ensemble des entiers naturels est défini de la façon suivante:

.. math::

   \mathbb{N} = {0, 1, 2, 3, ...}

En informatique, ces nombres sont par conséquent **non signés**, et peuvent prendre des valeurs comprises entre :math:`0` et :math:`2^N-1` où :math:`N` correspond au nombre de bits avec lesquels la valeur numérique sera stockée en mémoire. Il faut naturellement que l'ordinateur sur lequel s'exécute le programme soit capable de supporter le nombre de bits demandé par le programmeur.

En C, on nomme ce type de donnée ``unsigned int``, ``int`` étant le dénominatif du latin *integer* signifiant "entier".

Voici quelques exemples des valeurs minimales et maximales possibles selon le nombre de bits utilisés pour coder l'information numérique:

+--------------+-----------+-------------------------------------------------+
| Profondeur   | Minimum   | Maximum                                         |
+==============+===========+=================================================+
| 8 bits       | 0         | 255 (:math:`2^8 - 1`)                           |
+--------------+-----------+-------------------------------------------------+
| 16 bits      | 0         | 65'535 (:math:`2^{16} - 1`)                     |
+--------------+-----------+-------------------------------------------------+
| 32 bits      | 0         | 4'294'967'295 (:math:`2^{32} - 1`)              |
+--------------+-----------+-------------------------------------------------+
| 64 bits      | 0         | 18'446'744'073'709'551'616 (:math:`2^{64} - 1`) |
+--------------+-----------+-------------------------------------------------+

Notez l'importance du :math:`-1` dans la définition du maximum, car la valeur minimum :math:`0` fait partie de l'information même si elle représente une quantité nulle. Il y a donc 256 valeurs possibles pour un nombre entier non signé 8-bits, bien que la valeur maximale ne soit que de 255.

Les entiers relatifs
--------------------

Mathématiquement un entier relatif appartient à l'ensemble :math:`\mathbb{Z}`:

.. math::

   \mathbb{Z} = {..., -3, -2, -1, 0, 1, 2, 3, ...}

Les entiers relatifs sont des nombres **signés** et donc ils peuvent être **négatifs**, **nuls** ou **positifs** et peuvent prendre des valeurs comprises entre :math:`-2^{N-1}` et :math:`+2^{N-1}-1` où :math:`N` correspond au nombre de bits avec lesquels la valeur numérique sera stockée en mémoire. Notez l'asymétrie entre la borne positive et négative.

En C on dit que ces nombres sont ``signed``. Il est par conséquent correct d'écrire ``signed int`` bien que le préfixe ``signed`` soit optionnel, car le standard définit qu'un entier est par défaut signé. La raison à cela relève plus du lourd historique de C qu'à des préceptes logiques et rationnels.

Voici quelques exemples de valeurs minimales et maximales selon le nombre de bits utilisés pour coder l'information:

+--------------+------------------+------------------+
| Profondeur   | Minimum          | Maximum          |
+==============+==================+==================+
| 8 bits       | -128             | +127             |
+--------------+------------------+------------------+
| 16 bits      | -32'768          | +32'767          |
+--------------+------------------+------------------+
| 32 bits      | -2'147'483'648   | +2'147'483'647   |
+--------------+------------------+------------------+

En mémoire ces nombres sont stockés en utilisant le :ref:`complément à deux <twos_complement>` qui fait l'objet d'une section à part entière.

Les entiers bornés
------------------

Comme nous l'avons vu, les degrés de liberté pour définir un entier sont:

- Signé ou non signé
- Nombre de bits avec lesquels l'information est stockée en mémoire

À l'origine le standard C restait flou quant au nombre de bits utilisés pour chacun des types et aucune réelle cohérence n'existait pour la construction d'un type. Le modificateur ``signed`` était optionnel, le préfix ``long`` ne pouvait s'appliquer qu'au type ``int`` et ``long`` et la confusion entre ``long`` (préfixe) et ``long`` (type) restait possible. En fait, la plupart des développeurs s'y perdaient et s'y perd toujours ce qui menait à des problèmes de compatibilités des programmes entre eux.

La construction d'un type entier C est la suivante:

.. figure:: ../assets/figures/datatype/ansi-integers.*
    :alt: Entiers standardisés **C89**
    :width: 100 %

Ce qu'il faut retenir c'est que chaque type de donnée offre une profondeur d'au moins :math:`N` bits, ce qui est l'information minimale essentielle pour le programmeur. La liste des types de données standards en C pour les entiers est donnée au :numref:`standard-integers`.

.. _standard-integers:
.. table:: Types entiers standards

    +-----------------------------------------------+----------+------------------+----------+
    | Type                                          | Signe    | Profondeur       | Format   |
    +===============================================+==========+==================+==========+
    | ``char``                                      | ?        | ``CHAR_BIT``     | ``%c``   |
    +-----------------------------------------------+----------+------------------+----------+
    | ``signed char``                               | signed   | au moins 8 bits  | ``%c``   |
    +-----------------------------------------------+----------+------------------+----------+
    | ``unsigned char``                             | unsigned | au moins 8 bits  | ``%c``   |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``short``                                   | signed   | au moins 16 bits | ``%hi``  |
    | | ``short int``                               |          |                  |          |
    | | ``signed short``                            |          |                  |          |
    | | ``signed short int``                        |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``unsigned short``                          | unsigned | au moins 16 bits | ``%hu``  |
    | | ``unsigned short int``                      |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``unsigned``                                | unsigned | au moins 32 bits | ``%u``   |
    | | ``unsigned int``                            |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``int``                                     | signed   | au moins 32 bits | ``%d``   |
    | | ``signed``                                  |          |                  |          |
    | | ``signed int``                              |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``unsigned``                                | unsigned | au moins 32 bits | ``%u``   |
    | | ``unsigned int``                            |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``long``                                    | signed   | au moins 32 bits | ``%li``  |
    | | ``long int``                                |          |                  |          |
    | | ``signed long``                             |          |                  |          |
    | | ``signed long int``                         |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``unsigned long``                           | unsigned | au moins 32 bits | ``%lu``  |
    | | ``unsigned long int``                       |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``long long``                               | signed   | au moins 64 bits | ``%lli`` |
    | | ``long long int``                           |          |                  |          |
    | | ``signed long long``                        |          |                  |          |
    | | ``signed long long int``                    |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+
    | | ``unsigned long long``                      | unsigned | au moins 64 bits | ``%llu`` |
    | | ``unsigned long long int``                  |          |                  |          |
    +-----------------------------------------------+----------+------------------+----------+

Avec l'avènement de **C99**, une meilleure cohésion des types a été proposée dans le fichier d'en-tête ``stdint.h``. Cette bibliothèque standard offre les types suivants:

.. figure:: ../assets/figures/datatype/c99-integers.*
    :alt: Entiers standardisés **C99**
    :width: 100 %


Voici les types standards qu'il est recommandé d'utiliser lorsque le nombre de bits de l'entier doit être maîtrisé.

.. _stdint:
.. table:: Entiers standard définis par ``stdint``

    +-----------------------------------------------+----------+------------------+----------+
    | Type                                          | Signe    | Profondeur       | Format   |
    +===============================================+==========+==================+==========+
    | ``uint8_t``                                   | unsigned | 8 bits           | ``%c``   |
    +-----------------------------------------------+----------+------------------+----------+
    | ``int8_t``                                    | signed   | 8 bits           | ``%c``   |
    +-----------------------------------------------+----------+------------------+----------+
    | ``uint16_t``                                  | unsigned | 16 bits          | ``%hu``  |
    +-----------------------------------------------+----------+------------------+----------+
    | ``int16_t``                                   | signed   | 16 bits          | ``%hi``  |
    +-----------------------------------------------+----------+------------------+----------+
    | ``uint32_t``                                  | unsigned | 32 bits          | ``%u``   |
    +-----------------------------------------------+----------+------------------+----------+
    | ``int32_t``                                   | signed   | 32 bits          | ``%d``   |
    +-----------------------------------------------+----------+------------------+----------+
    | ``uint64_t``                                  | unsigned | 64 bits          | ``%llu`` |
    +-----------------------------------------------+----------+------------------+----------+
    | ``int64_t``                                   | signed   | 64 bits          | ``%lli`` |
    +-----------------------------------------------+----------+------------------+----------+

À ces types s'ajoutent les types **rapides** (*fast*) et **minimums** (*least*). Un type nommé ``uint_least32_t`` garanti l'utilisation du type de donnée utilisant le moins de mémoire et garantissant une profondeur d'au minimum 32 bits. Il est strictement équivalent à ``unsigned int``.

Les types rapides, moins utilisés vont automatiquement choisir le type adapté le plus rapide à l'exécution. Par exemple si l'architecture matérielle permet un calcul natif sur 48-bits, elle sera privilégiée par rapport au type 32-bits.

Les nombres réels
=================

Mathématiquement, les `nombres réels <https://fr.wikipedia.org/wiki/Nombre_r%C3%A9el>`__ :math:`\mathbb{R}`, sont des nombres qui peuvent être représentés par une partie entière, et une liste finie ou infinie de décimales. En informatique, stocker une liste infinie de décimale demanderait une quantité infinie de mémoire et donc, la `précision arithmétique <https://fr.wikipedia.org/wiki/Pr%C3%A9cision_arithm%C3%A9tique>`__ est contrainte.

Au début de l'ère des ordinateurs, il n'était possible de stocker que des nombres entiers, mais
le besoin de pouvoir stocker des nombres réels s'est rapidement fait sentir. La transition s'est faite progressivement, d'abord par l'apparition de la `virgule fixe <https://fr.wikipedia.org/wiki/Virgule_fixe>`__, puis par la `virgule flottante <https://fr.wikipedia.org/wiki/Virgule_flottante>`__.

Le premier ordinateur avec une capacité de calcul en virgule flottante date de 1942 (ni vous ni moi n'étions probablement né) avec le `Zuse's Z4 <https://fr.wikipedia.org/wiki/Zuse_4>`__, du nom de son inventeur `Konrad Zuse <https://fr.wikipedia.org/wiki/Konrad_Zuse>`__.

Virgule fixe
------------

Prenons l'exemple d'un nombre entier exprimé sur 8-bits, on peut admettre facilement que bien qu'il s'agisse d'un nombre entier, une virgule pourrait être ajoutée au bit zéro sans en modifier sa signification.

.. code-block::

    ┌─┬─┬─┬─┬─┬─┬─┬─┐
    │0│1│0│1│0│0│1│1│ = 2^6 + 2^4 + 2^1 + 2^0 = 64 + 16 + 2 + 1 = 83
    └─┴─┴─┴─┴─┴─┴─┴─┘
                    , / 2^0     ----> 83 / 1 = 83

Imaginons à présent que nous déplacions cette virgule virtuelle de trois éléments sur la gauche. En admettant que deux ingénieurs se mettent d'accord pour considérer ce nombre ``0b01010011`` avec une virgule fixe positionnée au quatrième bit, l'interprétation de cette grandeur serait alors la valeur entière divisé par 8 (:math:`2^3`). On parviens alors à exprimer une grandeur réelle comportant une epartie décimale:

.. code-block::

    ┌─┬─┬─┬─┬─┬─┬─┬─┐
    │0│1│0│1│0│0│1│1│ = 2^6 + 2^4 + 2^1 + 2^0 = 64 + 16 + 2 + 1 = 83
    └─┴─┴─┴─┴─┴─┴─┴─┘
              ,       / 2^3     ----> 83 / 8 = 10.375

Cependant, il manque une information. Un ordinateur, sans yeux et sans bon sens, est incapable sans information additionnelle d'interpréter correctement la position de la virgule puisque sa position n'est encodée nulle part. Et puisque la position de cette virgule est dans l'intervalle ``[0..7]``, il serait possible d'utiliser trois bits supplémentaires à cette fin:

.. code-block::

    ┌─┬─┬─┬─┬─┬─┬─┬─┐
    │0│1│0│1│0│0│1│1│ = 2^6 + 2^4 + 2^1 + 2^0 = 64 + 16 + 2 + 1 = 83
    └─┴─┴─┴─┴─┴─┴─┴─┘
              ┌─┬─┬─┐
              │0│1│1│ / 2^3     ----> 83 / 8 = 10.375
              └─┴─┴─┘

Cette solution est élégante mais demande a présent 11-bits contre 8-bits initialement. Un ordinateur n'étant doué que pour manipuler des paquets de bits souvent supérieurs à 8, il faudrait ici soit étendre inutilement le nombre de bits utilisés pour la position de la virgule à 8, soit tenter d'intégrer cette information, dans les 8-biàs initiaux.

Virgule flottante
-----------------

Imaginons alors que l'on sacrifie 3 bits sur les 8 pour encoder l'information de la position de la virgule. Appelons l'espace réservé pour positionner la virgule l'`exposant <https://fr.wikipedia.org/wiki/Exposant_(math%C3%A9matiques)>`__ et le reste de l'information la `mantisse <https://fr.wikipedia.org/wiki/Mantisse>`__, qui en mathématique représente la partie décimale d'un logarithme (à ne pas confondre avec la `mantis shrimp <https://fr.wikipedia.org/wiki/Stomatopoda>`__, une quille ou crevette mante boxeuse aux couleurs particulièrement chatoyantes).

.. code-block::

      exp.  mantisse
    ┞─┬─┬─╀─┬─┬─┬─┬─┦
    │0│1│0│1│0│0│1│1│ = 2^4 + 2^1 + 2^0 = 16 + 2 + 1 = 19
    └─┴─┴─┴─┴─┴─┴─┴─┘
       └────────────> / 2^1 ----> 19 / 2 = 9.5

Notre construction nous permet toujours d'exprimer des grandeurs réelles mais avec ce sacrifice, il n'est maintenant plus possible d'exprimer que les grandeurs comprises entre :math:`1\cdot2^{7}=0.0078125` et :math:`63`. Ce problème peut être aisément résolu en augmentant la profondeur mémoire à 16 ou 32-bits. Ajoutons par ailleurs que cette solution n'est pas à même d'exprimer des grandeurs négatives.

Dernière itération, choisissons d'étendre notre espace de stockage à ,4 octets. Réservons un bit de signe pour exprimer les grandeurs négatives, 8 bits pour l'exposant et 23 bits pour la mantisse:

.. code-block::

     ┌ Signe 1 bit
     │        ┌ Exposant 8 bits
     │        │                             ┌ Mantisse 23 bits
     ┴ ───────┴──────── ────────────────────┴──────────────────────────
    ┞─╀─┬─┬─┬─┬─┬─┬─┐┌─╀─┬─┬─┬─┬─┬─┬─┐┌─┬─┬─┬─┬─┬─┬─┬─┐┌─┬─┬─┬─┬─┬─┬─┬─┦
    │0│0│0│1│0│0│0│0││0│1│0│0│1│0│0│0││1│1│0│1│1│1│1│1││0│1│0│0│0│0│0│1│
    └─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘

Peu à peu, nous nous rapprochons du *Standard for Floating-Point Arithmetic* (`IEEE 754 <https://fr.wikipedia.org/wiki/IEEE_754>`__). La formule de base est la suivante:

.. math::

    x = s\cdot b^e\sum_{k=1}^p f_k\cdot b^{-k},\; e_{\text{min}} \le e \le e_{\text{max}}

Avec:

:math:`s`
    Signe (:math:`\pm1`)
:math:`b`
    Base de l'exposant, un entier :math:`>1`.
:math:`e`
    Exposant, un entier entre :math:`e_\text{min}` et :math:`e_\text{max}`
:math:`p`
    Précision, nombre de digits en base :math:`b` de la mantisse
:math:`f_k`
    Entier non négatif plus petit que la base :math:`b`.

Etant donné que les ordinateurs sont plus à l'aise à la manipulation d'entrées binaire, la base est 2 et la norme IEEE nomme ces nombres ``binary16``, ``binary32`` ou ``binary64``, selon le nombre de bits utilisé pour coder l'information. Les termes de *Single precision* ou *Double precision* sont aussi couramment utilisés.

Les formats supporté par un ordinateur ou qu'un microcontrôleur équipé d'une unité de calcul en virgule flottante (`FPU <https://en.wikipedia.org/wiki/Floating-point_unit>`__ pour *Floating point unit*) sont les suivants:

+--------------+----------+----------+-------+
| IEEE-754     | Exposant | Mantisse | Signe |
+==============+==========+==========+=======+
| ``binary32`` | 8 bits   | 23 bits  | 1 bit |
+--------------+----------+----------+-------+
| ``binary64`` | 11 bits  | 52 bits  | 1 bit |
+--------------+----------+----------+-------+

Prenons le temps de faire quelques observations.

- Une valeur encodée en virgule flottante sera toujours une approximation d'une grandeur réelle.
- La précision est d'autant plus grande que le nombre de bits de la mantisse est grand.
- La base ayant été fixée à 2, il est possible d'exprimer :math:`1/1024` sans erreur de précision mais pas :math:`1/1000`.
- Un ordinateur qui n'est pas équipé d'une FPU sera beaucoup plus lent `(10 à 100x) <https://stackoverflow.com/a/15585448/2612235>`__ pour faire des calculs en virgule flottante.
- Bien que le standard **C99** définisse les types virgule flottante ``float``, ``double`` et ``long double``, ils ne definissent pas la précision avec lesquelles ces nombres sont exprimés car cela dépend de l'architecture du processeur utilisé.

Simple précision
----------------

Le type ``float`` aussi dit à précision simple utilise un espace de stockage de 32-bits organisé en 1 bit de signe, 8 bits pour l'exposant et 23 bits pour la mantisse. Les valeurs pouvant être exprimées sont de:

- :math:`\pm\inf` lorsque l'exposant vaut ``0xff``
- :math:`(-1)^{\text{sign}}\cdot2^{\text{exp} - 127}\cdot1.\text{significand}`
- :math:`0` lorsque la mantisse vaut ``0x00000``

La valeur de 1.0 est encodée:

.. math::

    0\:01111111\:00000000000000000000000_2 &= \text{3f80}\: \text{0000}_{16} \\
    &= (-1)^0 \cdot 2^{127-127} \cdot \frac{(2^{23} + 0)}{2^{23}} \\
    &= 2^{0} \cdot 1.0 = 1.0\\

La valeur maximale exprimable:

.. math::

    0\:11111110\:11111111aquelle111111_2 &= \text{7f7f}\:, \text{ffff}_{16} \\
    &= (-1)^0 \cdot 2^{254-127} \cdot \frac{(2^{23} + 838'607)}{2^{23}} \\
    &≈ 2^{127} \cdot 1.9999998807 \\
    &≈ 3.4028234664 \cdot 10^{38}


La valeur de :math:`-\pi` (pi) est:

.. math::

    1\:10000000\:10010010000111111011011_2 &= \text{4049}\: \text{0fdb}_{16} \\
    &= (-1)^1 \cdot 2^{128-127} \cdot \frac{(2^{23} + 4'788'187)}{2^{23}} \\
    &≈ -1 \cdot 2^{1} \cdot 1.5707963 \\
    &≈ -3.14159274101

Vient s'ajouter les valeurs particulières suivantes:

.. code-block::

    0 00000000 00000000000000000000000₂ ≡ 0000 0000₁₆ ≡ 0
    0 11111111 00000000000000000000000₂ ≡ 7f80 0000₁₆ ≡ inf
    1 11111111 00000000000000000000000₂ ≡ ff80 0000₁₆ ≡ −inf

Double précision
----------------

La double précision est similaire à la simple précision mais avec une mantisse à **52 bits** et **11 bits** d'exposants.

Les caractères
==============

Les caractères, ceux que vous voyez dans cet ouvrage, sont généralement représentés par des grandeurs exprimées sur 1 octet (8-bits):

.. code-block::

    97 ≡ 0b1100001 ≡ 'a'

Historiquement, alors que les informations dans un ordinateur ne sont que des 1 et des 0, il a fallu établir une correspondance entre une grandeur binaire et le caractère associé. Un standard a été proposé en 1963 par l'`ASA <https://fr.wikipedia.org/wiki/American_National_Standards_Institute>`__, l'*American Standards Association* aujourd'hui ANSI qui ne définissait alors que 63 caractères imprimables et comme la mémoire était en son temps très cher, un caractère n'était codé que sur 7 bits.

.. figure:: ../assets/figures/encoding/ascii-1963.*

    Table ASCII ASA X3.4 établie en 1963

Aujourd'hui la table ASCII de base défini 128 carac,tères qui n'incluent pas les caractères accentués.

.. figure:: ../assets/figures/encoding/ascii.*

    Table ANSI INCITS 4-1986 (standard actuel)

Chaque pays et chaque langue utilise ses propres caractères et il a fallu trouver un moyen de satisfaire tout le monde. Il a été alors convenu d'encoder les caractères sur 8-bits au lieu de 7 et de profiter des 128 nouvelles positions pour ajouter les caractères manquants tels que les caractères accentués, le signe euro, la livre sterling et d'autres.

Le standard **ISO/IEC 8859** aussi appelé standard *Latin* défini 16 tables d'extension selon les besoins des pays. Les plus courantes en Europe occidentale sont les tables **ISO-8859-1** ou (**latin1**) et **ISO-8859-15** (**latin9**):

.. figure:: ../assets/figures/encoding/latin1.*

    Table d'extension ISO-8859-1 (haut) et ISO-8859-15 (bas)

Ce standard a généré durant des décénies de grandes frustrations et de profondes incompréhensions chez les développeurs, et utilisateurs d'ordinateur. Ne vous est-il jamais arrivé d'ouvrir un fichier texte et de ne plus voir les accents convenablement ? C'est un problème typique d'encodage.

Pour tenter de remédier à ce standard incompatible entre les pays Microsoft à proposé un standard nommé `Windows-1252 <https://fr.wikipedia.org/wiki/Windows-1252>`__ s'inspirant de `ISO-8859-1 <https://fr.wikipedia.org/wiki/ISO/CEI_8859-1>`__. En voulant rassembler en proposant un standard plus général, Microsoft n'a contribué qu'à proposer un standard supplémentaire venant s'inscrire dans une liste très trop longue. Et l'histoire n'est pas terminée...

Avec l'arrivée d'internet et les échanges entre les arabes (عَرَب‎), les coréens (한국어), les chinois avec le chinois simplifé (官话) et le chinois traditionel (官話), les japonais qui possèdent deux alphabets ainsi que des caractères chinois (日本語), sans oublier l'ourdou (پاکِستان) pakistanais et tous ceux que l'on ne mentionnera pas, il a fallu bien plus que 256 caractères et quelques tables de correspondance. Ce présent ouvrage, ne pourrait d'ailleur par être écrit sans avoir pu résoudre, au préalable, ces problèmes d'encodage; la preuve étant, vous parvenez à voir ces caractères qui ne vous sont pas familiers.

Un consensus planétaire a été atteint en 2008 avec l'adoption majoritaire du standard **Unicode** (*Universal Coded Character Set*) plus précisément nommé **UTF-8**.

.. figure:: ../assets/figures/encoding/encoding-trends.*

    Tendances sur l'encodage des pages web en faveur de UTF-8 dès 2008

L'UTF-8 est capable d'encoder 11'112'064 caractères en utilisant de 1 à 4 octets. `Ken Thompson <https://fr.wikipedia.org/wiki/Ken_Thompson>`__, dont nous avons déjà parlé en :ref:`introduction <thompson>` est à l'origine de ce standard. Par exemple le *devanagari* caractère ``ह`` utilisé en Sanskrit possède la dénomination unicode :unicode:`U+0939` et s'encode sur 3 octets: ``0xE0 0xA4 0xB9``

En programmation C, un caractère ``char`` ne peut exprimer sans ambiguité que les 128 caractères de la table ASCII standard et selon les conventions locales, les 128 caractères d'extension.

Voici par exemple comment déclarer une variable contenant le caractère dollar:

.. code-block:: c

    char c = '$';

Attention donc au caractère ``'3'`` qui correspond à la grandeur hexadécimale ``0x33``:

.. raw:: html

    <iframe height="400px" width="100%" src="https://repl.it/@yveschevallier/ContentMidnightbluePaintprogram?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Chaîne de caractères
====================

Une chaîne de caractère est simplement la suite contigue de plusieurs caractère dans une zone mémoire donnée. Afin de savoir lorsque cette chaîne se termine, le standard impose que le dernier caractère d'une chaîne soit ``NUL`` ou ``\0``.

La chaîne de caractère ``Hello`` sera en mémoire stockée en utilisant les codes ASCII suivants.

.. code-block:: c

    char string[] = "Hello";


.. code-block::

      H   E   L   L   O  \0
    ┌───┬───┬───┬───┬───┬───┐
    │ 72│101│108│108│111│ 0 │
    └───┴───┴───┴───┴───┴───┘

     0x00 01001000
     0x01 01100101
     0x02 01101100
     0x03 01101100
     0x04 01101111
     0x05 00000000

.. _booleans:

Les booléens
============

Un `booléen <https://fr.wikipedia.org/wiki/Bool%C3%A9en>`__ est un type de donnée à deux états consensuellement nommés *vrai* (``true``) et *faux* (``false``) et destiné à représenter les états en logique booléenne (Nom venant de `George Boole <https://fr.wikipedia.org/wiki/George_Boole>`__ fondateur de l'algèbre eponyme).

La convention est d'utiliser ``1`` pour mémoriser un état vrai, et ``0`` pour un état faux, c'est d'ailleurs de cette manière que les booléens sont encodés en C.

Les booléens ont étés introduits formellement en C avec **C99** et nécessitent l'inclusion du fichier d'en-tête ``stdbool.h``. Avant cela le type boolean était ``_Bool`` et définir les états vrais et faux étaient à la charge du dévelopeur.

.. code-block:: c

    #include <stdbool.h>

    bool is_enabled = false;
    bool has_tail = true;


Afin de faciliter la lecture du code, il est courant de préfixer les variables booléenes avec les prefixes ``is_`` ou ``has_``.

A titre d'exemple, si l'on souhaite stocker le genre d'un individu (male, ou femelle), on pourrait utiliser la variable ``is_male``.

.. _void:

void
====

Le type ``void`` est particulier car c'est un type qui ne vaut rien. Il est utilisé comme type de retour pour les fonctions qui ne retournent rien:

.. code-block:: c

    void shout() {
        printf("Hey!\n");
    }

Il peut être également utilisé comme type générique comme la fonction de copie mémoire ``memcpy``

.. code-block:: c

    void *memcpy(void * restrict dest, const void * restrict src, size_t n);

Le mot clé ``void`` ne peut être utilisé que dans les contextes suivants:

- Comme paramètre unique d'une fonction, indiquant que cette fonction n'a pas de paramètres ``int main(void)``
- Comme type de retour pour une fonction indiquant que cette fonction ne retourne rien ``void display(char c)``
- Comme pointeur dont le type de destination n'est pas spécifié ``void* ptr``

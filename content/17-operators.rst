==========
Opérateurs
==========

Un opérateur applique une opération à une (opérateur unitaire), deux ou trois (ternaire) entrées.

.. figure:: ../assets/figures/dist/processor/alu.*

    Unité de calcul arithmétique (ALU) composées de deux entrées ``A`` et ``B``, d'une sortie ``C`` et d'un mode opératoire ``O``.

.. code-block:: c

    c = a + b;

Un opérateur possède plusieurs propriétés:

Une priorité
    La multiplication ``*`` est plus prioritaire que l'addition ``+``

Une associativité
    L'opérateur d'affectation possède une associativité à droite, c'est à dire que l'opérande à droite de l'opérateur sera évalué en premier

Un point de séquence
    Certains opérateurs comme ``&&``, ``||``, ``?`` ou ``,`` possèdent un point de séquence garantissant que l'exécution séquentielle du programme sera respectée avant et après ce point. Par exemple si dans l'expression ``i < 12 && j > 2`` la valeur de ``i`` est plus grande que 12, le test ``j > 2`` ne sera jamais effectué. L'opérateur ``&&`` garanti l'ordre des choses ce qui n'est pas le cas avec l'affectation ``=``.

Opérateurs relationnels
=======================

Les opérateurs relationnels permettent de comparer deux entités. Le résultat d'un opérateur relationnel est toujours un **boolean** c'est à dire que le résultat d'une comparaison est soit **vrai**, soit **faux**.

.. table::

    =========  =====================  ==================
    Opérateur  Description            Exemple vrai
    =========  =====================  ==================
    ``==``     Egal                   ``42 == 0x101010``
    ``>=``     Supérieur ou égal      ``9 >= 9``
    ``<=``     Inférieur ou égal      ``-8 <= 8``
    ``>``      Strictement supérieur  ``0x31 > '0'``
    ``<``      Inférieur              ``8 < 12.33``
    ``!=``     Différent              ``'a' != 'c'``
    =========  =====================  ==================

Opérateurs arithmétiques
========================

Aux 4 opérations de base, le C ajoute l'opération `modulo <https://fr.wikipedia.org/wiki/Modulo_(op%C3%A9ration)>`__, qui est le reste d'une division entière.

- ``+`` Addition
- ``-`` Soustraction
- ``*`` Multiplication
- ``/`` Division
- ``%`` Modulo

Opérateurs bit à bit
====================

Les opérations binaires agissent directement sur les bits d'une entrée:

- ``&`` ET arithmétique
- ``|`` OU arithmétique
- ``^`` XOR arithmétique
- ``<<`` Décalage à gauche
- ``>>`` Décalage à droite
- ``~`` Inversion binaire

Opérateurs d'affectation
========================

- ``=`` Affectation simple
- ``+=`` Affectation par addition
- ``-=`` Affectation par soustraction
- ``*=`` Affectation par multiplication
- ``/=`` Affectation par division
- ``%=`` Affectation par modulo
- ``&=`` Affectation par ET arithmétique
- ``|=`` Affectation par OU arithmétique
- ``^=`` Affectation par XOR arithmétique
- ``<<=`` Affectation par décalage à gauche
- ``>>=`` Affectation par décalage à droite

Opérateurs logiques
===================

- ``&&`` ET logique
- ``||`` OU logique

Opérateurs d'incrémentation
===========================

- ``()++`` Post-incrémentation
- ``++()`` Pré-incrémentation
- ``()--`` Post-décrémentation
- ``--()`` Pré-décrémentation

Opérateur ternaire
==================

- ``()?():()`` Opérateur ternaire

Cet opérateur permet sur une seule ligne d'évaluer une expression et de renvoyer une valeur ou une autre selon que l'expression est vraie ou fausse. **valeur = (condition ? valeur si condition vraie : valeur si condition fausse);**

Important : seule la valeur utilisée pour le résultat est évaluée.

.. code-block:: c

    val_max = (a > b ? a : b);  // retourne la valeur max entre a et b



Opérateur de transtypage
========================

- ``()()``

Opérateur séquentiel
====================

L'opérateur séquentiel (*comma operator*) permet l'exécution ordonné d'opérations, et retourne la dernière valeur. Son utilisation est courament limitée soit aux décalarations de variables, soit au boucles ``for``:

.. code-block:: c

    for (size_t i = 0, j = 10; i != j; i++, j--) { /* ... */ }

Dans le cas ci-dessus, il n'est pas possible de séparer les instructions ``i++`` et ``j--`` par un point virgule, l'opérateur virgule permet alors de combiner plusieurs instructions en une seule.

Une particularité de cet opérateur est que seule la dernière valeur est retournée:

.. code-block:: c

    assert(3 == (1, 2, 3))

L'opérateur agit également comme un :ref:`Point de séquence <sequence_point>`, c'est à dire que l'ordre des étapes sont respectés.

.. exercise:: Opérateur séquentiel

    Que sera-t-il affiché à l'écran ?

    .. code-block:: c

        int i = 0;
        printf("%d", (++i, i++, ++i));

Opérateur sizeof
================

- ``sizeof``

Les opérateurs logiques
=======================

Ils permettent de coupler des opérateurs de comparaison entre eux pour
effectuer des tests un peu plus complexe.

ET logique
----------

Ecriture :

.. code-block:: c

    resultat = condition1 && condition2;

Table de vérité

+--------------+--------------+------------+
| condition1   | condition2   | résultat   |
+==============+==============+============+
| 0            | 0            | 0          |
+--------------+--------------+------------+
| 0            | 1            | 0          |
+--------------+--------------+------------+
| 1            | 0            | 0          |
+--------------+--------------+------------+
| 1            | 1            | 1          |
+--------------+--------------+------------+

OU logique
----------

Ecriture :

.. code-block:: c

    resultat = condition1 || condition2;

Table de vérité

+--------------+--------------+------------+
| condition1   | condition2   | résultat   |
+==============+==============+============+
| 0            | 0            | 0          |
+--------------+--------------+------------+
| 0            | 1            | 1          |
+--------------+--------------+------------+
| 1            | 0            | 1          |
+--------------+--------------+------------+
| 1            | 1            | 1          |
+--------------+--------------+------------+

Inversion logique
-----------------

Ecriture :

.. code-block:: c

    resultat = !condition1;

Table de vérité

+--------------+------------+
| condition1   | résultat   |
+==============+============+
| 0            | 1          |
+--------------+------------+
| 1            | 0          |
+--------------+------------+

Les opérateurs bit-à-bit
========================

Ils permettent d'effectuer des opérations binaire bit à bit sur des
types entiers.

Inversion logique ou complément à 1
-----------------------------------

C'est un opérateur unaire dont l'écriture est :

.. code-block:: c

    uint8_t a=0x55; // 0101 0101 (binaire)
    uint8_t r=0x00;

    r = ~a; // résultat r=0xAA (1010 1010)

ET logique
----------

Ecriture :

.. code-block:: c

    uint8_t a=0x55; // 0101 0101 (binaire)
    uint8_t b=0x0F; // 0000 1111
    uint8_t r=0x00;

    r = a & b;  // résultat r=0x05 (0000 0101)

OU logique
----------

Ecriture :

.. code-block:: c

    uint8_t a=0x55; // 0101 0101 (binaire)
    uint8_t b=0x0F; // 0000 1111
    uint8_t r=0x00;

    r = a | b;  // résultat r=0x5F (0101 1111)

OU EXCLUSIF logique
-------------------

Ecriture :

.. code-block:: c

    uint8_t a=0x55; // 0101 0101 (binaire)
    uint8_t b=0x0F; // 0000 1111
    uint8_t r=0x00;

    r = a ^ b;  // résultat r=0x5A (0101 1010)

Décalage à droite
-----------------

Ecriture :

.. code-block:: c

    uint8_t a=0xAA; // 1010 1010 (binaire)
    uint8_t r=0x00;

    r = a >> 1  // résultat r=0x55 (0101 0101)

Pour le décalage à droite de valeurs signées, le signe est conservé.
Cette opération s'apparente à une division par 2.

Décalage à gauche
-----------------

Ecriture :

.. code-block:: c

    uint8_t a=0xAA; // 1010 1010 (binaire)
    uint8_t r=0x00;

    r = a << 1  // résultat r=0x54 (0101 0100)

Cette opération s'apparente à une multiplication par 2.

Les opérateurs d'incrémentation (++) et de décrémentation (--)
==============================================================

Ces opérateurs, qui ne s'appliquent que sur des nombres entiers,
permettent d'ajouter 1 ou de retrancher 1 à une variable, et ce de
manière optimisée pour le processeur qui exécute le programme.

Ils peuvent, en outre, être exécutés avant ou après l'évaluation de
l'opération. On parle alors de pré-incrémentation ou pré-décrémentation
et post-incrémentation ou post-décrémentation.

pré-incrémentation
------------------

Ecriture :

.. code-block:: c

    int32_t i=0, j=0;

    j = ++i;    // on obtient i=1 et j=1

post-incrémentation
-------------------

Ecriture :

.. code-block:: c

    int32_t i=0, j=0;

    j = i++;    // on obtient i=1 et j=0

pré-décrémentation
------------------

Ecriture :

.. code-block:: c

    int32_t i=0, j=0;

    j = --i;    // on obtient i=-1 et j=-1

post-décrémentation
-------------------

Ecriture :

.. code-block:: c

    int32_t i=0, j=0;

    j = i--;    // on obtient i=-1 et j=0


.. _precedence:

Priorité des opérateurs
=======================

La **précédence** est un anglicisme de *precedence* (priorité) qui concerne la priorité des opérateurs, où l'ordre dans lequel les opérateurs sont exécutés. Chacuns connaît la priorité des quatre opérateurs de base (``+``, ``-``, ``*``, ``/``) mais le C et ses nombreux opérateurs est bien plus complexe.

La table suivante indique les règles à suivre pour les précédences des opérateurs en C.
La précédence

+----------+-----------------------+--------------------------------------------+-----------------+
| Priorité | Opérateur             | Description                                | Associativité   |
+==========+=======================+============================================+=================+
| 1        | ``++``, ``--``        | Postfix incréments/décréments              | Gauche à Droite |
|          +-----------------------+--------------------------------------------+                 |
|          | ``()``                | Appel de fonction                          |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``[]``                | Indexage des tableaux                      |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``.``                 | Element d'une structure                    |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``->``                | Element d'une structure                    |                 |
+----------+-----------------------+--------------------------------------------+-----------------+
| 2        | ``++``, ``--``        | Préfix incréments/décréments               | Droite à Gauche |
|          +-----------------------+--------------------------------------------+                 |
|          | ``+``, ``-``          | Signe                                      |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``!``, ``~``          | NON logique et NON binaire                 |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``(type)``            | Cast (Transtypage)                         |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``*``                 | Indirection, déréfrencement                |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``&``                 | Adresse de...                              |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``sizeof``            | Taille de...                               |                 |
+----------+-----------------------+--------------------------------------------+-----------------+
| 3        | ``*``, ``/``, ``%``   | Multiplication, Division, Mod              | Gauche à Droite |
+----------+-----------------------+--------------------------------------------+                 |
| 4        | ``+``, ``-``          | Addition, soustraction                     |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 5        | ``<<``, ``>>``        | Décalages binaires                         |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 6        | ``<``, ``<=``         | Comparaison plus petit que                 |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``>``, ``>=``         | Comparaison plus grand que                 |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 7        | ``==``, ``!=``        | Egalité, non égalité                       |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 8        | ``&``                 | ET binaire                                 |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 9        | ``^``                 | OU exclusif binaire                        |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 10       | ``|``                 | OU inclusif binaire                        |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 11       | ``&&``                | ET logique                                 |                 |
+----------+-----------------------+--------------------------------------------+                 |
| 12       | ``||``                | OU logique                                 |                 |
+----------+-----------------------+--------------------------------------------+-----------------+
| 13       | ``?:``                | Opérateur ternaire                         | Droite à Gauche |
+----------+-----------------------+--------------------------------------------+                 |
| 14       | ``=``                 | Assignation simple                         |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``+=``, ``-=``        | Assignation par somme/diff                 |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``*=``, ``/=``, ``%=``| Assignation par produit/quotient/modulo    |                 |
|          +-----------------------+--------------------------------------------+                 |
|          | ``<<=``, ``>>=``      | Assignation par décalage binaire           |                 |
+----------+-----------------------+--------------------------------------------+-----------------+
| 15       | ``,``                 | Virgule                                    | Gauche à Droite |
+----------+-----------------------+--------------------------------------------+-----------------+

Considérons l'exemple suivant:

.. code-block:: c

    int i[2] = {10, 20};
    int y = 3;

    x = 5 + 23 + 34 / ++i[0] & 0xFF << y;

Selon la précédance de chaque opérateur ainsi que son associativité on a:

.. code-block:: text

    [ ] 1
    ++  2
    /   3
    +   4
    +   4
    <<  5
    &   8
    =   14

L'écriture en notation polonaise inversée, donnerait alors

.. code-block:: text

    34, i, 0, [], ++,  /, 5, 23, +, +, 0xFF, y, <<, &, x, =

Associativité
-------------

L'associativité des opérateurs (`operator associativity <https://en.wikipedia.org/wiki/Operator_associativity>`__) décrit la manière dont sont évaluées les expressions.

Une associativité à gauche pour l'opérateur `~` signifie que l'expression ``a ~ b ~ c`` sera évaluée ``((a) ~ b) ~ c`` alors qu'une associativité à droite sera ``a ~ (b ~ (c))``.

Il ne faut pas confondre l'associativité *évaluée de gauche à droite* qui est une associativité à *gauche*.

Représentation mémoire des types de données
-------------------------------------------

Nous avons vu au chapitre sur les types de données que les types C
définis par défaut sont représentés en mémoire sur 1, 2, 4 ou 8 octets.
On comprend aisément que plus cette taille est importante, plus on gagne
en précision ou en grandeur représentable. La promotion numérique régit
les conversions effectuées implicitement par le langage C lorsqu'on
convertit une donnée d'un type vers un autre. Cette promotion tend à
conserver le maximum de précision lorsqu'on effectue des calcul entre
types différents (ex : l'addition d'un *int* avec un *double* donne un
type *double*). **Règles de base :**

-  les opérateurs ne peuvent agir que sur des types identiques

-  quand les types sont différents, il y a conversion automatique vers
   le type ayant le plus grand pouvoir de représentation

-  les conversions ne sont faites qu'au fur et à mesure des besoins

La **promotion** est l'action de promouvoir un type de donnée en un autre type de donnée plus général. On parle de promotion implicite des entiers lorsqu'un type est promu en un type plus grand automatiquement par le compilateur.

Valeurs gauche
==============

Une valeur gauche (*lvalue*) est une particularité de certains langage de programmation qui définissent ce qui peut se trouver à gauche d'une affectation. Ainsi dans ``x = y``, ``x`` est une valeur gauche. Néanmoins, l'expression ``x = y`` est aussi une valeur gauche:

.. code-block:: c

    int x, y, z;

    x = y = z;    // (1)
    (x = y) = z;  // (2)

1. L'associativité de ``=`` est à droite donc cette expression est équivalente à ``x = (y = (z))`` qui évite toute ambiguïté.
2. En forcant l'associativité à gauche, on essaie d'assigner ``z`` à une *lvalue* et le compilateur s'en plaint:
    .. code-block:: text

        4:8: error: lvalue required as left operand of assignment
            (x = y) = z;
                    ^

Voici quelques exemples de valeurs gauche:

- ``x /= y``
- ``++x``
- ``(x ? y : z)``

Optimisation
============

Le compilateur est en règle général plus malin que le développeur. L'optimiseur de code (lorsque compilé avec ``-O2`` sous ``gcc``), va regrouper certaines instructions, modifier l'ordre de certaines déclarations pour réduire soit l'empreinte mémoire du code, soit accélérer son exécution.

Ainsi l'expression suivante, ne sera pas calculée à l'exécution, mais à la compilation:

.. code-block:: c

    int num = (4 + 7 * 10) >> 2;

De même que ce test n'effectura pas une division mais testera simplement le dernier bit de ``a``:

.. code-block:: c

    if (a % 2) {
        puts("Pair");
    } else {
        puts("Impair");
    }

----

.. exercise:: Masque binaire

    Soit les déclarations suivantes:

    .. code-block:: c

        char m, n = 2, d = 0x55, e = 0xAA;

    Représenter en binaire et en hexadécimal la valeur de tous les bits de la variable ``m`` après exécution de chacune des instructions suivantes:

    #. :code:`m = 1 << n;`
    #. :code:`m = ~1 << n;`
    #. :code:`m = ~(1 << n);`
    #. :code:`m = d | (1 << n);`
    #. :code:`m = e | (1 << n);`
    #. :code:`m = d ^ (1 << n);`
    #. :code:`m = e ^ (1 << n);`
    #. :code:`m = d & ~(1 << n);`
    #. :code:`m = e & ~(1 << n);`

.. exercise:: Registre système

    Pour programmer les registres 16-bits d'un composant électronique chargé de gérer des sorties tout ou rien, on doit être capable d'effectuer les opérations suivantes:

    - mettre à 1 le bit numéro ``n``, ``n`` étant un entier entre 0 et 15;
    - mettre à 0 le bit numéro ``n``, ``n`` étant un entier entre 0 et 15;
    - inverser le bit numéro ``n``, ``n`` étant un entier entre 0 et 15;

    Pour des questions d'efficacité, ces opérations ne doivent utiliser que les opérateurs bit à bit ou décalage. On appelle ``r0`` la vairable désignant le registre en mémoire et ``n`` la variable contenant le numéro du bit à modifier. Écriver les expressions permettant d'effectuer les opérations demandées.

.. exercise:: Recherche d'expressions

    Considérant les déclarations suivantes:

    .. code-block:: c

        float a, b;
        int m, n;

    Traduire en C les expressions mathématiques ci-dessous; pour chacune, proposer plusieurs écritures différentes lorsque c'est possible. Le symbole :math:`\leftarrow` signifie *assignation*

    #. :math:`n \leftarrow 8 \cdot n`
    #. :math:`a \leftarrow a + 2`
    #. :math:`n \leftarrow \left\{\begin{array}{lr}m & : m > 0\\ 0 & : \text{sinon}\end{array}\right.`
    #. :math:`a \leftarrow n`
    #. :math:`n \leftarrow \left\{\begin{array}{lr}0 & : m~\text{pair}\\ 1 & : m~\text{impair}\end{array}\right.`
    #. :math:`n \leftarrow \left\{\begin{array}{lr}1 & : m~\text{pair}\\ 0 & : m~\text{impair}\end{array}\right.`
    #. :math:`m \leftarrow 2\cdot m + 2\cdot n`
    #. :math:`n \leftarrow n + 1`
    #. :math:`a \leftarrow \left\{\begin{array}{lr}-a & : b < 0\\ a & : \text{sinon}\end{array}\right.`
    #. :math:`n \leftarrow \text{la valeur des 4 bits de poids faible de}~n`

.. exercise:: Nombres narcissiques

    Un nombre narcissique ou `nombre d'Amstrong <https://fr.wikipedia.org/wiki/Nombre_narcissique>`__ est  un entier naturel ``n`` non nul qui est égal à la somme des puissances ``p``-ièmes de ses chiffres en base dix, où ``p`` désigne le nombre de chiffres de ``n``:

        .. math::

            n=\sum_{k=0}^{p-1}x_k10^k=\sum_{k=0}^{p-1}(x_k)^p\quad\text{avec}\quad x_k\in\{0,\ldots,9\}\quad\text{et}\quad x_{p-1}\ne 0

    Par exemple:

    - ``9`` est un nombre narcissique car :math:`9 = 9^1 = 9`
    - ``153`` est un nombre narcissique car :math:`153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`
    - ``10`` n'est pas un nombre narcissique car :math:`10 \ne 1^2 + 0^2 = 1`

    Implanter un programme permettant de vérifier si un nombre d'entrée est narcissique ou non. L'exécution est la suivante:

    .. code-block::

        $ ./armstrong 153
        1

        $ ./armstrong 154
        0

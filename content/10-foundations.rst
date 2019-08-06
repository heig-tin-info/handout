======================
Généralités du langage
======================

Ce chapitre traite des éléments constitufs et fondamentaux du langage C. Il traite des généralités propre au langage mais aussi les notions élémentaires permettant d'interpréter du code source.

L'alphabet
==========

L'alphabet de C est composé des 52 caractères latins et de 10 chiffres:

.. code-block:: text

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    0 1 2 3 4 5 6 7 8 9

La séparation des symboles est assurée par `une espace <https://fr.wikipedia.org/wiki/Espace_(typographie)>`__, une tabulation horizontale, une tabulation verticale, et un caractère de retour à la ligne. Ces caractères ne sont pas imprimables, c'est à dire qu'ils ne sont pas directement visible ni à l'écran, ni à l'impression. Microsoft Word et d'autres éditeurs utilisent généralement le `pied-de-mouche <https://fr.wikipedia.org/wiki/Pied-de-mouche>`__ ``¶`` pour indiquer les fin de paragraphes qui sont également des caractères non-imprimables.

On nomme les caractères non-imprimables soit par leur acronyme ``LF`` pour *Line Feed* ou soit par leur convention C ``\n``:

.. code-block:: text

    LF    \n   Line feed (retour à la ligne)
    VT    \v   Vertical tab
    FF    \f   New page
    TAB   \t   Horizontal tab
    CR    \r   Carriage return (retour charriot)
    SPACE \040 Space

La ponctuation utilise les 29 symboles graphiques suivants:

.. code-block:: text

    ! # % ^ & * ( _ ) - + = ~ [ ] ' | \ ; : " { } , .
    < > / ?

Un fait historique intéressant est que les premiers ordinateurs ne disposaient pas d'un clavier ayant tous ces symboles et la comission responsable de standardiser C a intégré au standard les **trigraphes** et plus tard les **digraphes** qui sont des combinaisons de caractères de base qui remplacent les caractères impossibles à saisir directement. Ainsi ``<:`` est le digraphe de ``[`` et ``??<`` est le trigraphe de ``{``. Néanmoins vous conviendrez lecteur que ces alternatives ne devraient être utilisées que dans des cas extrêmes et justifiables.

Fin de lignes (EOL)
===================

Restons un moment dans l'histoire et mentionnons qu'instar des premières machines à écrire, les `téléscripteurs <https://fr.wikipedia.org/wiki/T%C3%A9l%C3%A9scripteur>`__ possédaient de nombreux caractères de déplacement qui sont depuis tombés en désuétude et prêtent aujourd'hui à confusion même plus aguéri des programmeur. Maintenant que les ordinateurs possèdent des écrans, la notion originale du terme `retour chariot <https://fr.wikipedia.org/wiki/Retour_chariot>`__ est compromise et comme il y a autant d'avis que d'ingénieurs, les premiers PC `IBM compatible <https://fr.wikipedia.org/wiki/Compatible_PC>`__ ont choisi qu'une nouvelle ligne devait toujours se composer de deux caractères: un retour chariot (``CR``) et une nouvelle ligne (``LF``) ou en C ``\r\n``. Les premiers `Macintosh <https://fr.wikipedia.org/wiki/Macintosh>`__ d'Apple jugaient inutile de gaspiller deux caractères pour chaque nouvelle ligne dans un fichier et ont décidé d'associer le retour chariot et la nouvelle ligne dans le caractère ``\r``. Enfin, les ordinateurs UNIX ont eu le même raisonnement mais ils ont choisi de ne garder que ``\n``.

Fort heureusement depuis que Apple a migré son système sur une base `BSD <https://en.wikipedia.org/wiki/Berkeley_Software_Distribution>`__ (UNIX), il n'existe aujourd'hui plus que deux standards de retour à la ligne:

- ``LF`` ou ``\n`` sur les ordinateurs POSIX comme Linux, Unix ou MacOS
- ``CRLF`` ou ``\r\n`` sur les ordinateurs Windows.

Il n'y a pas de consensus établi sur lesquels des deux types de fin de ligne (``EOL``: *End Of Line*) il faut utiliser, faite preuve de bon sens et surtout, soyez cohérent.

.. figure:: assets/crlf.svg

    Distinction de différents caractères non-imprimables

Mots clés
=========

Le langage de programmation C tel que défini par C11 comporte 33 mots clés.

.. code-block:: c

    auto        enum         restrict     unsigned
    break       extern       return       void
    case        float        short        volatile
    char        for          signed       while
    const       goto         sizeof       _Bool
    default     inline       struct       _imaginary
    do          int          switch
    double      long         typedef
    else        register     union

Dans ce cours d'introduction l'usage des mots clés suivants est découragé car leur usage peut preter à confusion ou mener à des inélégances d'écriture.

.. code-block:: c

    auto        restrict     short        inline
    _Bool       register     goto         _imaginary
    long

Notons que les mots clés ``true`` et ``false`` décrits à la :numref:`booleans` ne sont pas standardisés en C mais ils le sont en C++.

.. _identifiers:

Identificateurs
===============

Un identificateur est une séquence de caractères représentant une entité du programme et à laquelle il est possible de se référer. Un identificateur est défini par:

.. figure:: assets/identifier.svg

    Grammaire d'un identificateur C

En addition de ceci, voici quelques règles:

- Un identificateur ne peut pas être l'un des mots clés du langage.
- Les identificateurs sont sensible à la `casse <https://fr.wikipedia.org/wiki/Casse_(typographie)>`__.
- Le standard C99, se réserve l'usage de tous les identificateurs débutant par ``_`` suivi d'une lettre majuscule ou un autre *underscore* ``_``.
- Le standard `POSIX <https://fr.wikipedia.org/wiki/POSIX>`__, se réserve l'usage de tous les identificateurs finissant par ``_t``.

Variables
=========

Une variable est un symbole qui associe un nom **identificateur** à une **valeur**. Comme son nom l'indique, une variable peut voir son contenu varier au cours du temps.

Une variable est définie par:

- Son **nom** (*name*), c'est à dire l'identificateur associé au symbole.
- Son **type** (*type*), qui est la convention d'interprétation du contenu binaire en mémoire.
- Sa **valeur** (*value*), qui est le contenu interprêté connaissant son type.
- Son **adresse** (*address*) qui est l'emplacement mémoire ou la représentation binaire sera enregistrée
- Sa **portée** (*scope*) qui est la portion de code ou le symbole est défini et accessible.
- Sa **visibilité** (*visibility*) qui ne peut être que *public* en C.

Déclaration
-----------

Avant de pouvoir être utilisée, une variable doit être déclarée afin que le compilateur puisse réserver un emplacement en mémoire pour stocker sa valeur. Voici quelques déclarations valides en C:

.. code-block:: c

    char c = '€';
    int temperature = 37;
    float neptune_stone_height = 376.86;
    char message[] = "Jarvis, il faut parfois savoir courir avant de savoir marcher.";

Il n'est pas nécessaire d'associer une valeur initiale à une variable, une déclaration peut se faire sans initialisation comme montré dans l'exemple suivant dans lequel on réserver trois variables ``i``, ``j``, ``k``.

.. code-block:: c

    int i, j, k;

Convention de nommage
---------------------

Il existe autant de conventions de nommage qu'il y a de développeurs mais un consensus majoritaire, que l'on retrouve dans d'autres langages de programmation exprime que:

- La longueur du nom d'une variable est généralement proportionnelle à sa portée et donc il est d'autant plus court que l'utilisation d'une variable est localisée.
- Le nom doit être concis et précis et ne pas laisser place à une quelconque ambiguité.
- Le nom doit participer à l'auto-documentation du code et permettre à un lecteur de comprendre facilement le programme qu'il lit.

Selon les standards adoptés chaque société on trouve ceux qui préfèrent nommer les variables en utilisant un *underscore* (``_``) comme séparateur et ceux qui préfèrent nommer une variable en utilisant des majuscules comme séparateurs de mots.

+--------------+------------------+----------------------+
| Convention   | Nom français     | Exemple              |
+==============+==================+======================+
| *camelcase*  | Casse de chameau | ``userLoginCount``   |
+--------------+------------------+----------------------+
| *snakecase*  | Casse de serpent | ``user_login_count`` |
+--------------+------------------+----------------------+
| *pascalcase* | Casse Pascal     | ``UserLoginCount``   |
+--------------+------------------+----------------------+
| *kebabcase*  | Casse de kebab   | ``user-login-count`` |
+--------------+------------------+----------------------+

Les constantes
==============

Une constante par opposition à une variable voit son contenu fixe et immutable.

Formellement, une constante se déclare comme une variable mais préfixée du mot-clé ``const``.

.. code-block:: c

    const double scale_factor = 12.67;


.. note::

    Il ne faut pas confondre la **constante** qui est une variable immutable, stockée en mémoire et une **macro** qui appartient au pré-processeur. Le fichier d'en-tête ``math.h`` définit par exemple la constante ``M_PI`` sous forme de macro.

    .. code-block:: c

        #define M_PI 3.14159265358979323846


Operateur d'affectation
=======================

Dans les exemples ci-dessus on utilise l'opérateur d'affectation pour associer une valeur à une variable.

Historiquement, et fort malheureusement, le symbole choisi pour cet opérateur est le signe égal ``=`` or, l'égalité est une notion mathématique qui n'est en aucun cas reliée à l'affectation.

Pour mieux saisir la nuance, considérons le programme suivant:

.. code-block:: c

    a = 42;
    a = b;

Mathématiquement, la valeur de ``b`` devrait être égale à 42 ce qui n'est pas le cas en C où il faut lire, séquentiellement l'exécution du code car oui, C est un langage impératif (c.f. :numref:`paradigms`). Ainsi, dans l'ordre on lit:

#. J'assigne la valeur 42 à la variable symbolisée par ``a``
#. Puis, j'assigne la valeur de la variable ``b`` au contenu de ``a``.

Comme on ne connaît pas la valeur de ``b``, avec cet exemple, on ne peut pas connaître la valeur de ``a``.

Certaines langages de programmation ont été sensibilité à l'importance de cette distinction et dans les langages **F#**, **OCaml**, **R** ou **S**, l'opérateur d'affectation est ``<-`` et une affectation pourrait s'écrire par exemple: ``a <- 42`` ou ``42 -> a``.

En C, l'opérateur d'égalité que nous verrons plus loin s'écrit ``==`` (deux ``=`` concaténés).

Remarquez ici que l'opérateur d'affectation de C agit toujours de droite à gauche c'est à dire que la valeur à **droite** de l'opérateur est affectée à la variable située à **gauche** de l'opérateur.

S'agissant d'un opérateur il est possible de chaîner les opérations, comme on le ferait avec l'opérateur ``+`` et dans l'exemple suivant il faut lire que ``42`` est assigné à ``c``, que la valeur de ``c`` est ensuite assignée à ``b`` et enfin la valeur de ``b`` est assignée à ``a``.

.. code-block:: c

    a = b = c = 42;

Nous verrons :numref:`precedence` que l'associativité de chaque opérateur détermine s'il agit de gauche à droite ou de droite à gauche.

Commentaires
============

Comme en français et ainsi qu'illustré par la :numref:`proust`, il est possible d'annoter un programme avec des **commentaires**. Les commentaires n'ont pas d'incidence sur le fonctionnement d'un programme et ne peuvent être lu que par le développeur qui possède le code source.

.. _proust:
.. figure:: assets/proust.svg

    Les carafes dans la Vivonne

Il existe deux manière d'écrire un commentaire en C:

- Les commentaires de lignes (depuis C99)

  .. code-block:: c

    // This is a single line comment.

- Les commentaires de block

  .. code-block:: c

    /* This is a
       Multi-line comment */

Les commentaires sont parsé par le pré-processeur, aussi il n'influencent pas le fonctionnement d'un programme mais seulement sa lecture. Rappelons qu'un code est plus souvent lu qu'écrit, car on ne l'écrit qu'une seule fois mais comme tout développement doit être si possible **réutilisable**,
il est plus probable qu'il soit lu part d'autres développeurs.

En conséquence, il est important de clarifier toute zone d'ombre lorsque que l'on s'éloigne des consensus établis, ou lorsque le code seul n'est pas suffisant pour bien comprendre son fonctionnement.

D'une façon générale, les commentaires servent à expliquer **pourquoi** et non **comment**. Un bon programme devrait pouvoir se passer de commentaires mais un programme sans commentaires n'est pas
nécessairement un bon programme.

Notons que l'on ne commente jamais du code et ce pour plusieurs raisons:

1. Les outils de *refactoring* ne pourront pas accéder du code commenté
2. La syntaxe ne pourra plus être vérifiée par l'IDE
3. Les outils de gestion de configuration (e.g. Git) devraient être utilisés à cette fin

Si d'aventure vous souhaitez exclure temporairement du code de la compilation, utilisez la directive de pré-processeur suivante, et n'oubliez pas d'expliquer pourquoi vous avez souhaité
désactiver cette portion de code.

.. code-block:: c

    #if 0 // TODO: Check if divisor could still be null at this point.
    if (divisor == 0) {
        return -1; // Error
    }
    #endif

D'une manière générale l'utilisaton des commentaires ne devrait pas être utilisée pour:

- Désactiver temporairement une portion de code sans l'effacer.
- Expliquer le **comment** du fonctionnement du code.
- Faire dans le dythyrambique pompeux et notarial, des phrases à rallonge bien trop romanesques.
- Créer de jolies spéarations telles que ``/*************************/``.

Exemple d'entête de fichier:

.. code-block:: c

    /**
     * Short description of the translation unit.
     *
     * Author: John Doe <john@doe.com>
     *
     * Long description of the translation unit.
     *
     * NOTE: Important notes about this code
     */

Opérateurs
==========

Un opérateur applique une opération à une (opérateur unitaire), deux ou trois (ternaire) entrées.

.. figure:: assets/alu.svg

.. code-block:: c

    c = a + b;

Opérateurs relationnels
-----------------------

Les opérateurs relationnels permettent de comparer deux entités. Le résultat d'un opérateur relationnel est toujours un **boolean** c'est à dire que le résultat d'une comparaison est soit **vrai**, soit **faux**.

- ``==`` Egal
- ``>=`` Supérieur ou égal
- ``<=`` Inférieur ou égal
- ``>`` Supérieur
- ``<`` Inférieur
- ``!=`` Différent

Opérateurs arithmétiques
------------------------

Aux 4 opérations de base, le C ajoute l'opération `modulo <https://fr.wikipedia.org/wiki/Modulo_(op%C3%A9ration)>`__, qui est le reste d'une division entière.

- ``+`` Addition
- ``-`` Soustraction
- ``*`` Multiplication
- ``/`` Division
- ``%`` Modulo

Opérateurs bit à bit
--------------------

Les opérations binaires agissent directement sur les bits d'une entrée:

- ``&`` ET arithmétique
- ``|`` OU arithmétique
- ``^`` XOR arithmétique
- ``<<`` Décalage à gauche
- ``>>`` Décalage à droite

Opérateurs d'affectation
------------------------

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
-------------------
- ``&&`` ET logique
- ``||`` OU logique

Opérateurs d'incrémentation
---------------------------

- ``()++`` Post-incrémentation
- ``++()`` Pré-incrémentation
- ``()--`` Post-décrémentation
- ``--()`` Pré-décrémentation

Opérateur ternaire
------------------

- ``()?():()`` Opérateur ternaire

Opérateur de transtypage
------------------------

- ``()()``

Opérateur séquentiel
--------------------

- ``,``

Opérateur sizeof
----------------

- ``sizeof``

Les opérateurs logiques booléens
--------------------------------

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

Les opérateurs pour manipuler les données binaires
==================================================

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

Les opérateurs d'affectation élargis
====================================

Ces opérateurs permettent une optimisation de l'écriture et du code
généré. Syntaxe :

.. code-block:: c

    i+=5; // équivaut à i=i+5;

| Les opérateurs élargis suivants s'appliquent pour les entiers et les
  nombres à virgule :
| += addition ----- ---------------- -= soustraction \*= multiplication
  /= division

|
| Ces derniers sont eux réservés aux entiers :
| %= modulo (entiers seulement) ---------------
  ------------------------------- :math:`\ll`\ = décalage à gauche
  :math:`\gg`\ = décalage à droite &= ET logique bit à bit :math:`|`\ =
  OU logique bit à bit :math:`\wedge`\ = OU EXCLUSIF logique bit à bit

|
| ### Opérateur de séquence

L'opérateur séquence est symbolisé par une virgule (,) séparant des
instructions C. L'évaluation de la séquence vaut la valeur de
l'instruction la plus à droite.

Syntaxe :

.. code-block:: c

    int32_t i=0, j=3, k=-4;

    i=j=5,k=-2; // j=5, k=-2, i=5

Opérateur conditionnel
----------------------

| Cet opérateur permet sur une seule ligne d'évaluer une expression et
  de renvoyer une valeur ou une autre selon que l'expression est vraie
  ou fausse. **valeur = (condition ? valeur si condition vraie : valeur
  si condition fausse);**
| Important : seule la valeur utilisée pour le résultat est évaluée.

.. code-block:: c

    val_max = (a > b ? a : b);  // retourne la valeur max entre a et b


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
|          | ``(type)``            | Cast                                       |                 |
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

    i, 0, [], ++, 34, /, 5, 23, +, +, y, <<, 0xFF, &, x, =


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

Promotion implicite
===================

+---------+-----------------------+----------+
| char    | :math:`\Rightarrow`   | int      |
+---------+-----------------------+----------+
| short   | :math:`\Rightarrow`   | int      |
+---------+-----------------------+----------+
| int     | :math:`\Rightarrow`   | long     |
+---------+-----------------------+----------+
| long    | :math:`\Rightarrow`   | float    |
+---------+-----------------------+----------+
| float   | :math:`\Rightarrow`   | double   |
+---------+-----------------------+----------+

Notez qu'il n'y a pas de promotion numérique vers le type *short*. On
passe directement à un type *int*.

Effets du transtypage
---------------------

Le changement de type forcé (transtypage) entre des variables de
différents type engendre des effets de bord qu'il faut connaître. Lors
d'un changement de type vers un type dont le pouvoir de représentation
est plus important, il n'y a pas de problème. A l'inverse, on peut
rencontrer des erreurs sur la précision ou une modification radicale de
la valeur représentée !

Transtypage d'un entier en réel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La conversion d'un entier (signé ou non) en réel (*double* ou *float*)
n'a pas d'effet particulier. Le type

.. code-block:: c

    long l=3;
    double d=(double)l; // valeur : 3 => OK

A l'exécution, la valeur de :math:`d` sera la même que :math:`l`.

Transtypage d'un réel en entier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La conversion d'un nombre réel (*double* ou *float*) en entier (signé)
doit être étudié pour éviter tout problème. Le type entier doit être
capable de recevoir la valeur (attention aux valeurs maxi).

.. code-block:: c

    double d=3.9;
    long l=(long)d; // valeur : 3 => perte de précision

A l'exécution, la valeur de :math:`l` sera la partie entière de
:math:`d`. Il n'y a pas d'arrondi.

.. code-block:: c

    double d=0x12345678;
    short sh=(short)d; // valeur : 0x5678 => changement de valeur

La variable sh (*short* sur 16 bit) ne peut contenir la valeur réelle.
Lors du transtypage, il y a modification de la valeur ce qui conduit à
des erreurs de calculs par la suite.

.. code-block:: c

    double d=-123;
    unsigned short sh=(unsigned short)d; // valeur : 65413 => changement de valeur

L'utilisation d'un type non signé pour convertir un nombre réel conduit
également à une modification de la valeur numérique.

Transtypage d'un double en float
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La conversion d'un nombre réel de type *double* en réel de type *float*
pose un problème de précision de calcul.

.. code-block:: c

    double d=0.1111111111111111;
    float f=(float)d; // valeur : 0.1111111119389533 => perte de précision

A l'exécution, il y a une perte de précision lors de la conversion ce
qui peut, lors d'un calcul itératif induire des erreurs de calcul.

Optimisation
============

Le compilateur est en règle général plus malin que le développeur. L'optimiseur de code (lorsque compilé avec ``-O2`` sous ``gcc``), va regrouper certaines instructions, modifier l'ordre de certaines déclarations pour réduire soit l'emprunte mémoire du code, soit accélérer son exécution.

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



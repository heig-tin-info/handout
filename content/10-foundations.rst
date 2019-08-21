======================
Généralités du langage
======================

Ce chapitre traite des éléments constitufs et fondamentaux du langage C. Il traite des généralités propres au langage mais aussi des notions élémentaires permettant d'interpréter du code source.

Notons que ce chapitre est transveral, à la sa première lecture, le profane ne pourra tout comprendre sans savoir lu et maitrisé les chapitres suivants, néanmoins il retrouvera ici les aspects fondamentaux du langage.

L'alphabet
==========

Fort heureusement pour nous occidentaux, l'alphabet de C est composé des 52 caractères latins et de 10 `chiffres indo-arabes <https://fr.wikipedia.org/wiki/Chiffres_arabes>`__:

.. code-block:: text

    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    0 1 2 3 4 5 6 7 8 9

La séparation des symboles est assurée par `une espace <https://fr.wikipedia.org/wiki/Espace_(typographie)>`__, une tabulation horizontale, une tabulation verticale, et un caractère de retour à la ligne. Ces caractères ne sont pas imprimables, c'est à dire qu'ils ne sont pas directement visible ni à l'écran, ni à l'impression. Microsoft Word et d'autres éditeurs utilisent généralement le `pied-de-mouche <https://fr.wikipedia.org/wiki/Pied-de-mouche>`__ ``¶`` pour indiquer les fin de paragraphes qui sont également des caractères non-imprimables.

On nomme les caractères non-imprimables soit par leur acronyme ``LF`` pour *Line Feed* ou soit par leur convention C échappée par un *backslash* ``\n``:

.. code-block:: text

    LF    \n   Line feed (retour à la ligne)
    VT    \v   Vertical tab
    FF    \f   New page
    TAB   \t   Horizontal tab
    CR    \r   Carriage return (retour charriot)
    SPACE \040 Space

La ponctuation utilise les 29 symboles graphiques suivants:

.. code-block:: text

    ! # % ^ & * ( _ ) - + = ~ [ ] ' | \ ; : " { } , . < > / ?

Un fait historique intéressant est que les premiers ordinateurs ne disposaient pas d'un clavier ayant tous ces symboles et la comission responsable de standardiser C a intégré au standard les **trigraphes** et plus tard les **digraphes** qui sont des combinaisons de caractères de base qui remplacent les caractères impossibles à saisir directement. Ainsi ``<:`` est le digraphe de ``[`` et ``??<`` est le trigraphe de ``{``. Néanmoins vous conviendrez cher lecteur que ces alternatives ne devraient être utilisées que dans des cas extrêmes et justifiables.

Retenez que C peut être un langage extrèmement cryptique tant il est permissif sur sa syntaxe. Il existe d'ailleurs un concours international d'obfuscation, le `The International Obfuscated C Code Contest <https://www.ioccc.org/>`__ qui prime des codes les plus subtils et illisibles comme le code suivant écrit par `Chris Mills <https://www.ioccc.org/2015/mills2>`__. Il s'agit d'ailleurs d'un exemple qui compile parfaitement sur la plupart des compilateurs.

.. code-block:: c

        int I=256,l,c, o,O=3; void e(
    int L){ o=0; for( l=8; L>>++l&&
    16>l;			    o+=l
    <<l-			    1) ;
    o+=l		     *L-(l<<l-1); { ; }
    if (		    pread(3,&L,3,O+o/8)<
    2)/*		    */exit(0);	L>>=7&o;
    L%=1		     <<l; L>>8?256-L?e(
    L-1)			    ,c||
    (e(c			    =L),
    c=0)			    :( O
    +=(-I&7)*l+o+l>>3,I=L):putchar(
        L); }int main(int l,char**o){
                    for(
                /*	    ////      */
                open(1[o],0); ; e(I++
                ))		      ;}

Fin de lignes (EOL)
===================

À l'instar des premières machines à écrire, les `téléscripteurs <https://fr.wikipedia.org/wiki/T%C3%A9l%C3%A9scripteur>`__ possédaient de nombreux caractères de déplacement qui sont depuis tombés en désuétude et prêtent aujourd'hui à confusion même pour le plus aguerri des programmeurs. Maintenant que les ordinateurs possèdent des écrans, la notion originale du terme `retour chariot <https://fr.wikipedia.org/wiki/Retour_chariot>`__ est compromise et comme il y a autant d'avis que d'ingénieurs, les premiers PC `IBM compatibles <https://fr.wikipedia.org/wiki/Compatible_PC>`__ ont choisi qu'une nouvelle ligne devait toujours se composer de deux caractères: un retour chariot (``CR``) et une nouvelle ligne (``LF``) ou en C ``\r\n``. Les premiers `Macintosh <https://fr.wikipedia.org/wiki/Macintosh>`__ d'Apple jugaient inutile de gaspiller deux caractères pour chaque nouvelle ligne dans un fichier et ont décidé d'associer le retour chariot et la nouvelle ligne dans le caractère ``\r``. Enfin, les ordinateurs UNIX ont eu le même raisonnement mais ils ont choisi de ne garder que ``\n``.

Fort heureusement depuis que Apple a migré son système sur une base `BSD <https://en.wikipedia.org/wiki/Berkeley_Software_Distribution>`__ (UNIX), il n'existe aujourd'hui plus que deux standards de retour à la ligne:

- ``LF`` ou ``\n`` sur les ordinateurs POSIX comme Linux, Unix ou MacOS
- ``CRLF`` ou ``\r\n`` sur les ordinateurs Windows.

Il n'y a pas de consensus établi sur lesquels des deux types de fin de ligne (``EOL``: *End Of Line*) il faut utiliser, faite preuve de bon sens et surtout, soyez cohérent.

.. figure:: ../assets/figures/encoding/crlf.*

    Distinction de différents caractères non-imprimables

Mots clés
=========

Le langage de programmation C tel que défini par C11 comporte 33 mots clés.

.. code-block:: c

    auto        enum         restrict     unsigned      break       extern
    return      void         case         float         short       volatile
    char        for          signed       while         const       goto
    sizeof      _Bool        default      inline        struct      _imaginary
    do          int          switch       double        long        typedef
    else        register     union

Dans ce cours l'usage des mots clés suivants est découragé car leur utilisation pourrait prêter à confusion ou mener à des inélégances d'écriture.

.. code-block:: c

    auto        restrict     short        inline
    _Bool       register     goto         _imaginary
    long

Notons que les mots clés ``true`` et ``false`` décrits à la :numref:`booleans` ne sont pas standardisés en C mais ils le sont en C++.

.. _identifiers:

Identificateurs
===============

Un identificateur est une séquence de caractères représentant une entité du programme et à laquelle il est possible de se référer. Un identificateur est défini par:

.. figure:: ../assets/figures/grammar/identifier.*

    Grammaire d'un identificateur C

En addition de ceci, voici quelques règles:

- Un identificateur ne peut pas être l'un des mots clés du langage.
- Les identificateurs sont sensible à la `casse <https://fr.wikipedia.org/wiki/Casse_(typographie)>`__.
- Le standard C99, se réserve l'usage de tous les identificateurs débutant par ``_`` suivi d'une lettre majuscule ou un autre *underscore* ``_``.
- Le standard `POSIX <https://fr.wikipedia.org/wiki/POSIX>`__, se réserve l'usage de tous les identificateurs finissant par ``_t``.

.. hint:: Expression régulière

    Il est possible d'exprimer la syntaxe d'un identificateur à l'aide de l'expression régulière suivante:

    .. code-block:: text

        ^[a-zA-Z_][a-zA-Z0-9_]*$

.. exercise:: Validité des identificateurs

    Pour chacune des suites de caractères ci-dessous, indiquez s'il s'agit d'un identificateur valide et utilisable en C. Justifier votre réponse.

    #. ``2_pi``
    #. ``x_2``
    #. ``x___3``
    #. ``x 2``
    #. ``positionRobot``
    #. ``piece_presente``
    #. ``_commande_vanne``
    #. ``-courant_sortie``
    #. ``_alarme_``
    #. ``panne#2``
    #. ``int``
    #. ``défaillance``
    #. ``f'``
    #. ``INT``

    .. solution::

        Une excellente approche serait d'utiliser directement l'expression régulière fournie et d'utiliser l'outil en ligne `regex101.com <https://regex101.com/r/cmxaic/1>`__.

        #. ``2_pi`` **invalide** car commence par un chiffre
        #. ``x_2`` **valide**
        #. ``x___3`` **valide**
        #. ``x 2`` **invalide** car comporte un espace
        #. ``positionRobot`` **valide**, notation *camelCase*
        #. ``piece_presente`` **valide**, notation *snake_case*
        #. ``_commande_vanne`` **valide**
        #. ``-courant_sortie`` **invalide**, un identificateur ne peut pas commencer par le signe ``-``
        #. ``_alarme_`` **valide**
        #. ``panne#2`` **invalide**, le caractère ``#`` n'est pas autorisé
        #. ``int`` **invalide**, ``int`` est un mot réservé du langage
        #. ``défaillance`` **invalide**, uniquement les caractères imprimable ASCII sont autorisés
        #. ``f'`` **invalide** l'apostrophe n'est pas autorisée
        #. ``INT`` **valide**

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
    char message[] = "Jarvis, il faut parfois savoir "
        "courir avant de savoir marcher.";

Il n'est pas nécessaire d'associer une valeur initiale à une variable, une déclaration peut se faire sans initialisation comme montré dans l'exemple suivant dans lequel on réserver trois variables ``i``, ``j``, ``k``.

.. code-block:: c

    int i, j, k;

.. exercise:: Affectation de variables

    Considérons les déclarations suivantes:

    .. code-block:: c

        int a, b, c;
        float x;

    Notez après chaque affectation, le contenu des différentes variables:

    =====  ================  =====  =====  =====  =====
    Ligne  Instruction       ``a``  ``b``  ``c``  ``x``
    =====  ================  =====  =====  =====  =====
    1      ``a = 5;``
    2      ``b = c;``
    3      ``c = a;``
    4      ``a = a + 1;``
    5      ``x = a - ++c;``
    6      ``b = c = x;``
    7      ``x + 2. = 7.;``
    =====  ================  =====  =====  =====  =====

    .. solution::

        =====  ================  =====  =====  =====  =====
        Ligne  Instruction       ``a``  ``b``  ``c``  ``x``
        =====  ================  =====  =====  =====  =====
        1      ``a = 5;``            5      ?      ?      ?
        2      ``b = c;``            5      ?      ?      ?
        3      ``c = a;``            5      ?      5      ?
        4      ``a = a + 1;``        6      ?      5      ?
        5      ``x = a - ++c;``      6      ?      6     12
        6      ``b = c = x;``        6     12     12     12
        7      ``x + 2. = 7.;``      -      -      -      -
        =====  ================  =====  =====  =====  =====

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
| *pascalcase* | Casse de Pascal  | ``UserLoginCount``   |
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


Constantes littérales
=====================

Les constantes littérales représentent des grandeurs scalaires numériques ou de caractères et initialisées lors de la phase de compilation.

.. code-block:: c

    6      // Grandeur valant le nombre d'heures sur l'horloge du Palais du Quirinal à Rome
    12u    // Grandeur non signée
    6l     // Grandeur entière signée codée sur un entier long
    42ul   // Grandeur entière non signée codée sur un entier long
    010    // Grandeur octale valant 8 en décimal
    0xa    // Grandeur hexadécimale valant 10 en décimal
    0b111  // Grandeur binaire valant 7 en décimal
    33.    // Grandeur réelle exprimée en virgule flottante
    '0'    // Grandeur caractère vallant 48 en décimal

.. exercise:: Constances littérales

    Pour les entrées suivantes, indiquez lesquelles sont correctes.

    #. ``12.3``
    #. ``12E03``
    #. ``12u``
    #. ``12.0u``
    #. ``1L``
    #. ``1.0L``
    #. ``.9``
    #. ``9.``
    #. ``.``
    #. ``0x33``
    #. ``0xefg``
    #. ``0xef``
    #. ``0xeF``
    #. ``0x0.2``
    #. ``09``
    #. ``02``

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

Certaines langages de programmation ont été sensibilisé à l'importance de cette distinction et dans les langages **F#**, **OCaml**, **R** ou **S**, l'opérateur d'affectation est ``<-`` et une affectation pourrait s'écrire par exemple: ``a <- 42`` ou ``42 -> a``.

En C, l'opérateur d'égalité que nous verrons plus loin s'écrit ``==`` (deux ``=`` concaténés).

Remarquez ici que l'opérateur d'affectation de C agit toujours de droite à gauche c'est à dire que la valeur à **droite** de l'opérateur est affectée à la variable située à **gauche** de l'opérateur.

S'agissant d'un opérateur il est possible de chaîner les opérations, comme on le ferait avec l'opérateur ``+`` et dans l'exemple suivant il faut lire que ``42`` est assigné à ``c``, que la valeur de ``c`` est ensuite assignée à ``b`` et enfin la valeur de ``b`` est assignée à ``a``.

.. code-block:: c

    a = b = c = 42;

Nous verrons :numref:`precedence` que l'associativité de chaque opérateur détermine s'il agit de gauche à droite ou de droite à gauche.

.. exercise:: Affectations simples

    Donnez les valeurs de ``x``, ``n``, ``p`` après l'exécution des instructions ci-dessous:

    .. code-block:: c

        float x;
        int n, p;

        p = 2;
        x = 15 / p;
        n = x + 0.5;

    .. solution::

        .. code-block:: c

            p ≡ 2
            x ≡ 7
            n ≡ 7

.. exercise:: Trop d'égalités

    On considère les déclarations suivantes:

    .. code-block:: c

        int i, j, k;

    Donnez les valeurs des variabels ``i``, ``j`` et ``k`` après l'exécution de chacune des expressions ci-dessous. Qu'en pensez-vous ?

    .. code-block:: c

        /* 1 */ i = (k = 2) + (j = 3);
        /* 2 */ i = (k = 2) + (j = 2) + j * 3 + k * 4;
        /* 3 */ i = (i = 3) + (k = 2) + (j = i + 1) + (k = j + 2) + (j = k - 1);

    .. solution::

        Selon la table de priorité des opérateurs, on note:

        - ``()`` priorité 1 associativité à droite
        - ``*`` priorité 3 associativité à gauche
        - ``+`` priorité 4 associativité à droite
        - ``=`` priorité 14 associativité à gauche

        En revanche rien n'est dit sur les `point de séquences <https://en.wikipedia.org/wiki/Sequence_point>`__. L'opérateur d'affectation n'est pas un point de séquence, autrement dit le standard C99 (Annexe C) ne définit pas l'ordre dans lequel les assignations sont effectuées.

        Ainsi, seul le premier point possède une solution, les deux autres sont indéterminés

        #. ``i = (k = 2) + (j = 3)``
            - ``i = 5``
            - ``j = 3``
            - ``k = 2``
        #. ``i = (k = 2) + (j = 2) + j * 3 + k * 4``
            - Résultat indéterminé
        #. ``i = (i = 3) + (k = 2) + (j = i + 1) + (k = j + 2) + (j = k - 1)``
            - Résultat indéterminé


Commentaires
============

Comme en français et ainsi qu'illustré par la :numref:`proust`, il est possible d'annoter un programme avec des **commentaires**. Les commentaires n'ont pas d'incidence sur le fonctionnement d'un programme et ne peuvent être lu que par le développeur qui possède le code source.

.. _proust:
.. figure:: ../assets/images/proust.*

    Les carafes dans la Vivonne

Il existe deux manière d'écrire un commentaire en C:

- Les commentaires de lignes (depuis C99)

  .. code-block:: c

    // This is a single line comment.

- Les commentaires de block

  .. code-block:: c

    /* This is a
       Multi-line comment */

Les commentaires sont parsés par le pré-processeur, aussi ils n'influencent pas le fonctionnement d'un programme mais seulement sa lecture. Rappelons qu'un code est plus souvent lu qu'écrit, car on ne l'écrit qu'une seule fois mais comme tout développement doit être si possible **réutilisable**,
il est plus probable qu'il soit lu part d'autres développeurs.

En conséquence, il est important de clarifier toute zone d'ombre lorsque que l'on s'éloigne des consensus établis, ou lorsque le code seul n'est pas suffisant pour bien comprendre son fonctionnement.

D'une façon générale, les commentaires servent à expliquer **pourquoi** et non **comment**. Un bon programme devrait pouvoir se passer de commentaires mais un programme sans commentaires n'est pas
nécessairement un bon programme.

Notons que l'on ne commente jamais des portions de code et ce pour plusieurs raisons:

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
- Créer de jolies séparations telles que ``/*************************/``.

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

Le format des commentaires est par essence libre au développeur mais il est généralement souhaité que:

- Les commentaires soient concis et précis.
- Les commentaires soient écrits en anglais.

Opérateurs
==========

Un opérateur applique une opération à une (opérateur unitaire), deux ou trois (ternaire) entrées.

.. figure:: ../assets/figures/processor/alu.*

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
-----------------------

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
- ``~`` Inversion binaire

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
^^^^^^^^^^^^^

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

.. exercise:: Expressions mixtes

    Soit les instructions suivantes:

    .. code-block:: c

        int n = 10;
        int p = 7;
        float x = 2.5;

    Donnez le type et la valeur des expressions suivantes:

    #. ``x + n % p``
    #. ``x + p / n``
    #. ``(x + p) / n``
    #. ``.5 * n``
    #. ``.5 * (float)n``
    #. ``(int).5 * n``
    #. ``(n + 1) / n``
    #. ``(n + 1.0) / n``

.. exercise:: Promotion numérique

    Représentez les promotions numériques qui surviennent lors de l'évaluation des expressions ci-dessous:

    .. code-block:: c

        char c;
        short sh;
        int i;
        float f;
        double d;

    #. ``c * sh - f / i + d;``
    #. ``c * (sh – f) / i + d;``
    #. ``c * sh - f - i + d;``
    #. ``c + sh * f / i + d;``

Effets du transtypage
---------------------

Le changement de type forcé (transtypage) entre des variables de
différents types engendre des effets de bord qu'il faut connaître. Lors
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

.. exercise:: Conversion de types

    On considère les déclarations suivantes:

    .. code-block:: c

        float x;
        short i;
        unsigned short j;
        long k;
        unsigned long l;

    Identifiez les expressions ci-dessous dont le résultat n'est pas mathématiquement correct.

    .. code-block:: c

        x = 1e6;
        i = x;
        j = -20;
        k = x;
        l = k;
        k = -20;
        l = k;

    .. solution::

        .. code-block:: c

            x = 1e6;
            i = x;    // Incorrect, i peut-être limité à -32767..+32767 (C99 §5.2.4.2.1)
            j = -20;  // Incorrect, valeur signée dans un conteneur non signé
            k = x;
            l = k;
            k = -20;
            l = k;    // Incorrect, valeur signée dans un conteneur non signé

.. exercise:: Un casting explicite

    Que valent les valeurs de ``p``, ``x`` et ``n``:

    .. code-block:: c

        float x;
        int n, p;

        p = 2;
        x = (float)15 / p;
        n = x + 1.1;

    .. solution::

        p ≡ 2
        x = 7.5
        n = 8

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

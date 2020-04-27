================
Types composites
================

.. index:: struct

Tableaux
========

Les `tableaux <https://fr.wikipedia.org/wiki/Tableau_(structure_de_donn%C3%A9es)>`__ (*arrays*) représentent une séquence finie d'éléments d'un type donné que l'on peut accéder par leur position (indice) dans la séquence. Un tableau est par conséquent une liste indexée de variable du même type.

L'opérateur crochet ``[]`` est utilisé à la fois pour le déréférencement (accès à un indice du tableau) et pour l'assignation d'une taille à un tableau :

La déclaration d'un tableau d'entiers de dix éléments s'écrit de la façon suivante :

.. code-block:: c

    int array[10];

Par la suite il est possible d'accéder aux différents éléments ici l'élément 1 et 3 :

.. code-block:: c

    array[1];
    array[5 - 2];

L'opérateur ``sizeof`` permet d'obtenir la taille d'un tableau en mémoire, mais attention, c'est la taille du tableau et non le nombre d'éléments qui est retourné. Dans l'exemple suivant ``sizeof(array)`` retourne :math:`5\cdot4=20` tandis que ``sizeof(array[0])`` retourne la taille d'un seul élément :math:`4`; et donc, ``sizeof(array) / sizeof(array[0])`` est le nombre d'éléments de ce tableau, soit 5.

.. code-block:: c

    uint32_t array(5);
    size_t length = sizeof(array) / sizeof(array[0]);

.. hint::

    L'index d'un tableau commence toujours à **0** et par conséquent l'index maximum d'un tableau de 5 éléments sera 4. Il est donc fréquent dans une boucle d'utiliser ``<`` et non ``<=``:

    .. code-block:: c

        for(size_t i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
           /* ... */
        }

Une variable représentant un tableau est en réalité un pointeur sur ce tableau, c'est-à-dire la position mémoire à laquelle se trouvent les éléments du tableau. Nous verrons ceci plus en détail à la section :numref:`pointers`. Ce qu'il est important de retenir c'est que lorsqu'un tableau est passé à une fonction comme dans l'exemple suivant, l'entier du tableau n'est pas passé par copie, mais seul une **référence** sur ce tableau est passée.

La preuve étant que le contenu du tableau peut être modifié à distance :

.. code-block:: c

    void function(int i[5]) {
       i[2] = 12
    }

    int main(void) {
       int array[5] = {0};
       function(array);
       assert(array[2] == 5);
    }

Un fait remarquable est que l'opérateur ``[]`` est commutatif. En effet, l'opérateur *crochet* est un sucre syntaxique :

.. code-block::c

    a[b] == *(a + b)

Et cela fonctionne même avec les tableaux à plusieurs dimensions :

.. code-block::c

    a[1][2] == *(*(a + 1) + 2))

.. exercise:: Assignation

    Écrire un programme qui lit la taille d'un tableau de cinquante entiers de 8 bytes et assigne à chaque élément la valeur de son indice.

    .. solution::

        .. code-block:: c

            int64_t a;
            for (size_t i = 0; i < sizeof(a) / sizeof(a[0]; i++) {
                a[i] = i;
            }

.. exercise:: Première position

    Soit un tableau d'entiers, écrire une fonction retournant la position de la première occurence d'une valeur dans le tableau.

    Traitez les cas particuliers.

    .. code-block:: c

        int index_of(int *array, size_t size, int search);

    .. solution::

        .. code-block:: c

            int index_of(int *array, size_t size, int search) {
                int i = 0;
                while (i < size && array[i++] != search);
                return i == size ? -1 : i;
            }

.. exercise:: Déclarations de tableaux

    Considérant les déclarations suivantes :

    .. code-block:: c

        #define LIMIT 10
        const int twelve = 12;
        int i = 3;

    Indiquez si les déclarations suivantes (qui n'ont aucun lien entre elles), sont correcte ou non.

    .. code-block:: c

        int t(3);
        int k, t[3], l;
        int i[3], l = 2;
        int t[LIMITE];
        int t[i];
        int t[douze];
        int t[LIMITE + 3];
        float t[3, /* five */ 5];
        float t[3]        [5];

.. exercise:: Comparaisons

    Soit deux tableaux `char u[]` et `char v[]`, écrire une fonction comparant leur contenu et retournant :

    ``0``
        La somme des deux tableaux est égale.

    ``-1``
        La somme du tableau de gauche est plus petite que le tableau de droite

    ``1``
        La somme du tableau de droite est plus grande que le tableau de gauche

    Le prototype de la fonction à écrire est :

    .. code-block:: c

        int comp(char a[], char b[], size_t length);

    .. solution::

        .. code-block:: c

            int comp(char a[], char b[], size_t length) {
                int sum_a = 0, sum_b = 0;

                for (size_t i = 0; i < length; i++) {
                    sum_a += a[i];
                    sum_b += b[i];
                }

                return sum_b - sum_a;
            }

.. exercise:: Le plus grand et le plus petit

    Dans le canton de Genève, il existe une tradition ancestrale: l'`Escalade <https://fr.wikipedia.org/wiki/Escalade_(Gen%C3%A8ve)>`__. En comémoration de la victoire de la république protestante sur les troupes du duc de Savoie suite à l'attaque lancée contre Genève dans la nuit du 11 au 12 décembre 1602 (selon le calendrier julien), une traditionnelle marmite en chocolat est brisée par l'ainé et le cadet après la récitation de la phrase rituelle "Ainsi périrent les ennemis de la République !".

    Pour gagner du temps et puisque l'assemblée est grande, il vous est demandé d'écrire un programme pour identifier le doyen et le benjamin de l'assistance.

    Un fichier contenant les années de naissance de chacun vous est donné, il ressemble à ceci :

    .. code-block:: text

        1931
        1986
        1996
        1981
        1979
        1999
        2004
        1978
        1964

    Votre programme sera exécuté comme suit :

    .. code-block:: console

        $ cat years.txt | marmite
        2004
        1931

.. exercise:: L'index magique

    Un indice magique d'un tableau ``A[0..n-1]`` est défini tel que la valeur ``A[i] == i``. Compte tenu que le tableau est trié avec des entiers distincts (sans répétition), écrire une méthode pour trouver un indice magique s'il existe.

    Exemple :

    .. code-block:: text

          0   1   2   3   4   5   6   7   8   9   10
        ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
        │-90│-33│ -5│ 1 │ 2 │ 4 │ 5 │ 7 │ 10│ 12│ 14│
        └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                                      ^

    .. solution:: c

        Une solution triviale consite à itérer tous les éléments jusqu'à trouver l'indice magique :

        .. code-block:: c

            int magic_index(int[] array) {
                const size_t size = sizeof(array) / sizeof(array[0]);

                size_t i = 0;

                while (i < size && array[i] != i) i++;

                return i == size ? -1 : i;
            }

        La complexité de cet algorithme est :math:`O(n)` or, la donnée du problème indique que le tableau est trié. Cela veut dire que probablement, cette information n'est pas donnée par hasard.

        Pour mieux se représenter le problème prenons l'exemple d'un tableau :

        .. code-block:: text

              0   1   2   3   4   5   6   7   8   9   10
            ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
            │-90│-33│ -5│ 1 │ 2 │ 4 │ 5 │ 7 │ 10│ 12│ 14│
            └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
                                          ^

        La première valeur magique est ``7``. Est-ce qu'une approche dichotomique est possible ?

        Prenons le milieu du tableau ``A[5] = 4``. Est-ce qu'une valeur magique peut se trouver à gauche du tableau ? Dans le cas le plus favorable qui serait :

        .. code-block:: text

              0   1   2   3   4
            ┌───┬───┬───┬───┬───┐
            │ -1│ 0 │ 1 │ 2 │ 3 │
            └───┴───┴───┴───┴───┘

        On voit qu'il est impossible que la valeur se trouve à gauche car les valeurs dans le tableau sont distinctes et il n'y a pas de répétitions. La règle que l'on peut poser est ``A[mid] < mid`` où ``mid`` est la valeur mediane.

        Il est possible de répéter cette approche de façon dichotomique :

        .. code-block:: c

            int magic_index(int[] array) {
                return _magic_index(array, 0, sizeof(array) / sizeof(array[0]) - 1);
            }

            int _magic_index(int[] array, size_t start, size_t end) {
                if (end < start) return -1;
                int mid = (start + end) / 2;
                if (array[mid] == mid) {
                    return mid;
                } else if (array[mid] > mid) {
                    return _magic_index(array, start, mid - 1);
                } else {
                    return _magic_index(array, mid + 1, end);
                }
            }

Initialisation
--------------

Lors de la déclaration d'un tableau, le compilateur réserve un espace mémoire de la taille suffisante pour contenir tous les éléments du tableaux. La déclaration suivante :

.. code:: c

    int32_t even[6];

contient 6 entiers, chacuns d'une taille de 32-bits (4 bytes). L'espace mémoire réservé est donc de 24 bytes.

Compte tenu de cette déclaration, il n'est pas possible de connaître la valeur qu'il y a, par exemple, à l'indice 4 (``even[4]``), car ce tableau n'a pas été initialisé et le contenu mémoire est non prédictible puisqu'il peut contenir les vestiges d'un ancien programme ayant résidé dans cette région mémoire auparavant. Pour s'assurer d'un contenu il faut initialiser le tableau, soit affecter des valeurs pour chaque indice :

.. code:: c

    int32_t sequence[6];
    sequence[0] = 4;
    sequence[1] = 8;
    sequence[2] = 15;
    sequence[3] = 16;
    sequence[4] = 23;
    sequence[5] = 42;

Cette écriture n'est certainement pas la plus optimisée car l'initialisation du tableau n'est pas réalisée à la compilation, mais à l'exécution du programme ; et ce seront pas moins de six instructions qui seront nécessaires à initialiser ce tableau. L'initialisation d'un tableau utilise les accolades :

.. code:: c

   int32_t sequence[6] = {4, 8, 15, 16, 23, 42};

Dans cette dernière écriture, il existe une redondance d'information. La partie d'initialisation ``{4, 8, 15, 16, 23, 42}`` comporte six éléments et le tableau est déclaré avec six éléments ``[6]``. Pour éviter une double source de vérité, il est ici possible d'omettre la taille du tableau :

.. code:: c

   int32_t sequence[] = {4, 8, 15, 16, 23, 42};

Notons que dans premier de ces deux cas, si un nombre inférieur à 6 éléments est initialisé, les autrs éléments seront initializés à **zéro**

.. code:: c

   int32_t sequence[6] = {4, 8, 15, 16 /* le reste vaudra zéro */ };

Il est également possible d'initialiser un tableau de façon explicite en utilisant une notation plus spécifique :

.. code:: c

   int32_t sequence[6] = {[0]=4, [1]=8, [2]=15, [3]=16, [4]=23, [5]=42};

Et naturellement il est possible d'omettre certaines valeurs, lesquelles seront initialisées à zéro par défaut. Dans l'exemple suivant les valeurs aux indices 1 à 4 vaudront zéro.

.. code:: c

   int32_t sequence[6] = {[0]=4, [5]=42};

Notons que lorsque que la notation ``[]=`` est utilisée, les valeurs qui suivent seront positionnées aux indices suivants :

.. code:: c

   int32_t sequence[6] = {[0]=4, 8, [3]=16, 23, 42};

Dans l'exemple ci-dessus ``sequence[2]`` vaudra zéro.

Notons qu'un type composé tel qu'un tableau ne peut pas être initialisé après sa déclaration. L'exemple suivant ne fonctionne pas :

.. code-block:: c

    int array[10];

    // Erreur: l'initialisation tardive n'est pas autorisée.
    array = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

Initialisation à zéro
---------------------

Enfin, un sucre syntaxique ``{0}`` permet d'initialiser tout un tableau à zéro. En effet, la valeur 0 est inscrite à l'indice zéro, les autres valeurs sont par défaut initialisées à zéro si non mentionnées :

.. code:: c

   int32_t sequence[6] = {0};

Cette écriture est nécessaire pour les variables locales, car, nous verrons plus loin (c.f. :numref:`memory-management`) les variables globales sont placées dans le segment mémoire ``.bss`` et sont initialisées à zéro au démarrage du programme. Toute variable globale est donc initialisée à zéro par défaut.

Initialization à une valeur particulière
----------------------------------------

Cette écriture n'est pas normalisée **C99**, mais est généralement compatible avec la majorité des compilateurs.

.. code-block:: c

    int array[1024] = { [ 0 ... 1023 ] = -1 };

En **C99**, il n'est pas possible d'initialiser un type composé à une valeur unique. La manière traditionnelle reste la boucle itérative :

.. code-block:: c

    for (size_t i = 0; i < sizeof(array)/sizeof(array[0]); i++)
        array[i] = -1;

Tableaux non modifiables
------------------------

A présent que l'on sait initialiser un tableau, il peut être utile de définir un tableau avec un contenu qui n'est pas modifiable. Le mot clé ``const`` est utilisé a cette fin.

.. code:: c

   int32_t sequence[6] = {4, 8, 15, 16, 23, 42};
   sequence[2] = 12;

Dans l'exemple ci-dessus, la seconde ligne génèrera l'erreur suivante :

.. code:: text

   error: assignment of read-only location ‘sequence[2]’

Notons que lors de l'utilisation de pointeurs, il serait possible, de façon détournée, de modifier ce tableau malgré tout :

.. code:: c

   int *p = sequence;
   p[2] = 12;

Dans ce cas, ce n'est pas une erreur mais une alerte du compilateur qui survient :

.. code:: text

   warning: initialization discards ‘const’ qualifier from pointer
   target type [-Wdiscarded-qualifiers]

Tableaux multi-dimensionnels
----------------------------

Il est possible de déclarer un tableau à plusieurs dimensions. Si par exemple on souhaite définir une grille de jeu du *tic-tac-toe* ou morpion, il faudra une grille de 3x3.

Pour ce faire, il est possible de définir un tableau de 6 éléments comme vu auparavant, et utiliser un artifice pour adresser les lignes et les colonnes :

.. code:: c

    char game[6] = {0};
    int row = 1;
    int col = 2;
    game[row * 3 + col] = 'x';

Néanmoins, cette écriture n'est pas pratique et le langage C dispose du nécessaire pour alléger l'écriture. La grille de jeu sera simplement initialisée comme suit :

.. code:: c

    char game[3][3] = {0};

Jouer ``x`` au centre équivaut à écrire :

.. code:: c

    game[1][1] = 'x';

De la même façon il est possible de définir structure tri-dimensionnelles :

.. code:: c

    int volume[10][4][8];

L'initialisation des tableaux multi-dimensionnel est très similaire au tableaux standards mais il est possible d'utiliser plusieurs niveau d'accolades.

Ainsi le jeu de morpion suivant :

.. code:: text

     o | x | x
    ---+---+---
     x | o | o
    ---+---+---
     x | o | x

Peut s'initialiser comme suit :

.. code:: c

   char game[][3] = {{'o', 'x', 'x'}, {'x', 'o', 'o'}, {'x', 'o', 'x'}};

Notons que l'écriture suivante est similaire, car un tableau multidimensionnel est toujours représenté en mémoire de façon linéaire, comme un tableau à une dimension :

.. code:: c

   char game[][3] = {'o', 'x', 'x', 'x', 'o', 'o', 'x', 'o', 'x'};

.. exercise:: Détectives privés

    Voici les dépenses de service annuelles d'un célèbre bureau de détectives privés :

    =========  =======  ======   ======  ======
               Bosley   Sabrina  Jill    Kelly
    =========  =======  ======   ======  ======
    Janvier    414.38   222.72   99.17   153.81
    Février    403.41   390.61   174.39  18.11
    Mars       227.55   73.86    291.08  416.55
    Avril      220.20   342.25   139.45  86.98
    Mai         13.46   172.66   252.33  265.32
    Juin       259.37   378.72   173.02  208.43
    Juillet    327.06   16.53    391.05  266.84
    Août        50.82   3.37     201.71  170.84
    Septembre  450.78   9.33     111.63  337.07
    Octobre    434.45   77.80    459.46  479.17
    Novembre   420.13   474.69   343.64  273.28
    Décembre   147.76   250.73   201.47  9.75
    =========  =======  ======   ======  ======

    Afin de laisser plus de temps aux détectives à résoudres des affaires, vous êtes mandaté pour écrire une fonction qui reçois en paramètre le tableau de réels ci-dessus formaté comme suit :

    .. code-block:: c

        double accounts[][] = {
            {414.38, 222.72,  99.17, 153.81, 0},
            {403.41, 390.61, 174.39, 18.11,  0},
            {227.55,  73.86, 291.08, 416.55, 0},
            {220.20, 342.25, 139.45, 86.98,  0},
            {13.46 , 172.66, 252.33, 265.32, 0},
            {259.37, 378.72, 173.02, 208.43, 0},
            {327.06,  16.53, 391.05, 266.84, 0},
            {50.82 ,   3.37, 201.71, 170.84, 0},
            {450.78,   9.33, 111.63, 337.07, 0},
            {434.45,  77.80, 459.46, 479.17, 0},
            {420.13, 474.69, 343.64, 273.28, 0},
            {147.76, 250.73, 201.47, 9.75,   0},
            {  0,      0,      0,    0,      0}
        };

    Et laquelle complète les valeurs manquantes.

.. exercise:: Pot de peinture

    A l'instar de l'outil *pot de peinture* des éditeurs d'image, il vous est demandé d'implémenter une fonctionnalité similaire.

    L'image est représentée par un tableau bi-dimensionnel contenant des couleurs indexées :

    .. code-block::

        typedef enum { BLACK, RED, PURPLE, BLUE, GREEN YELLOW, WHITE } Color;

        #if 0 // Image declaration example
        Color image[100][100];
        #endif

        boolean paint(Color* image, size_t rows, size_t cols, Color fill_color);

    .. hint::

        Deux approches intéressantes sont possibles: **DFS** (Depth-First-Search) ou **BFS** (Breadth-First-Search), toutes deux récursives.

Chaînes de caractères
=====================

Une chaîne de caractères est représentée en mémoire comme une succession de bytes, chacuns représentant un caractère ASCII spécifique. La chaîne de caractère ``hello`` contient donc 5 caractères et sera stockée en mémoire sur 5 bytes. Une chaîne de caractère est donc équivalente à un tableau de ``char``.

En C, un artifice est utilisé pour faciliter les opérations sur les chaînes de caractères. Tous les caractères de 1 à 255 sont utilisables sauf le 0 qui est utilisé comme sentinelle. Lors de la déclaration d'une chaîne comme ceci :

.. code-block:: c

    char str[] = "hello, world!";

Le compilateur ajoutera automatiquement un caractère de terminaison ``'\0'`` à la fin de la chaîne. Pour comprendre l'utilité, imaginons une fonction qui permet de compter la longueur de la chaîne. Elle aurait comme prototype ceci :

.. code-block:: c

    size_t strlen(const char str[]);

On peut donc lui passer un tableau dont la taille n'est pas définie et par conséquent, il n'est pas possible de connaître la taille de la chaîne passée sans le bénéfice d'une sentinelle.

.. code-block:: c

    size_t strlen(const char str[]) {
        size_t len = 0,
        while (str[len++] != '\0') {}
        return len;
    }

Une chaîne de caractère est donc strictement identique à un tableau de ``char``.

Ainsi une chaîne de caractère est initialisée comme suit :

.. code-block:: c

    char str[] = "Pulp Fiction";

La taille de ce tableau sera donc de 12 caractères plus une sentinelle ``'\0'`` insérée automatiquement. Cette écriture est donc identique à :

.. code-block:: c

    char str[] = {
        'P', 'u', 'l', 'p', ' ', 'F', 'i', 'c', 't', 'i', 'o', 'n', '\0'
    };

Tableaux de chaînes de caractères
---------------------------------

Un tableau de chaîne de caractères est identique à un tableau multidimensionnel :

.. code-block:: c

    char conjunctions[][10] = {
        "mais", "ou", "est", "donc", "or", "ni", "car"
    };

Il est ici nécessaire de définir la taille de la seconde dimension, comme pour les tableaux. C'est à dire que la variable ``conjunctions`` aura une taille de 7x10 caractères et le contenu mémoire de ``conjunctions[1]`` sera équivalent à :

.. code-block:: c

    {'o', 'u', 0, 0, 0, 0, 0, 0, 0, 0}

D'ailleurs, ce tableau aurait pu être initialisé d'une tout autre façon :

.. code-block:: c

    char conjunctions[][10] = {
        'm', 'a', 'i', 's', 0, 0, 0, 0, 0, 0, 'o', 'u', 0, 0, 0,
        0, 0, 0, 0, 0, 'e', 's', 't', 0, 0, 0, 0, 0, 0 , 0, 'd',
        'o', 'n', 'c', 0, 0, 0, 0, 0 , 0, 'o', 'r', 0, 0, 0, 0,
        0, 0, 0, 0, 'n', 'i', 0, 0, 0, 0, 0, 0, 0, 0, 'c', 'a',
        'r', 0, 0, 0, 0, 0, 0, 0,
    };

Structures
==========

Les structures sont des déclarations spécifiques permettant de regrouper une liste de variables dans un même bloc mémoire et permettant de s'y référer à partir d'une référence commune. Historiquement le type ``struct`` a été dérivé de ``ALGOL 68``. Il est également utilisé en C++ et est similaire à une classe.

Il faut voir une structure comme un container à variables qu'il est possible de véhiculer comme un tout.

La structure suivante décrit un agrégat de trois grandeurs scalaires formant un point tridimensionnel :

.. code-block:: c

    struct {
        double x;
        double y;
        double z;
    };

Il ne faut pas confondre l'écriture ci-dessus avec ceci, dans lequel il y a un bloc de code avec trois variables locales déclarées :

.. code-block:: c

    {
        double x;
        double y;
        double z;
    };

En utilisant le mot-clé ``struct`` devant un bloc, les variables déclarées au sein de ce bloc ne seront pas réservées en mémoire. Autrement dit, il ne sera pas possible d'accéder à ``x`` puisqu'il n'existe pas de variable ``x``. En revanche, un nouveau container contenant trois variable est défini, mais pas encore déclaré.

La structure ainsi déclarée n'est pas très utile telle quelle, en revanche elle peut-être utilisée pour déclarer une variable de type ``struct`` :

.. code-block:: c

    struct {
        double x;
        double y;
        double z;
    } point;

A présent on a déclaré une variable ``point`` de type ``struct`` contenant trois éléments de type ``double``. L'affectaction d'une valeur à cette variable utilise l'opérateur ``.`` :

.. code-block:: c

    point.x = 3060426.957;
    point.y = 3192003.220;
    point.z = 4581359.381;

Comme ``point`` n'est pas une primitive standard mais un container à primitive, il n'est pas correct d'écrire ``point = 12``. Il est essentiel d'indiquer quel élément de ce container on souhaite accéder.

Ces coordonnées sont un clin d'oeil aux `Pierres du Niton <https://fr.wikipedia.org/wiki/Pierres_du_Niton>`__ qui sont deux blocs de roche erratiques déposés par le glacier du Rhône lors de son retrait après la dernière glaciation. Les coordonnées sont exprimées selon un repère géocentré ; l'origine étant le centre de la terre. Ces pierres sont donc situées à 4.5 km du centre de la terre, et donc un sacré défi pour `Axel Lidenbrock <https://fr.wikipedia.org/wiki/Voyage_au_centre_de_la_Terre>`__ et son fulmicoton.

Structures nommées
------------------

L'écriture que l'on a vu initialement ``struct { ... };`` est appelée structure annonyme, c'est à dire qu'elle n'a pas de nom. Telle quelle elle ne peut pas être utilisée et elle ne sert donc pas à grand chose. En revanche, il est possible de déclarer une variable de ce type en ajoutant un identificateur à la fin de la déclaration ``struct { ... } nom;``. Néanmoins la structure est toujours annonyme.

Le langage C prévoit la possibilté de nommer une structure pour une utilisation ultérieure en rajoutant un nom après le mot clé ``struct`` :

.. code-block:: c

    struct Point {
        double x;
        double y;
        double z;
    };

Pour ne pas confondre un nom de structure avec un nom de variable, on préférera un identificateur en capitales ou en écriture *camel-case*. Maintenant qu'elle est nommée, il est possible de déclarer plusieurs variables de ce type ailleurs dans le code :

.. code-block:: c

    struct Point foo;
    struct Point bar;

Dans cet exemple, on déclare deux variables ``foo`` et ``bar`` de type ``struct Point``. Il est donc possible d'accéder à ``foo.x`` ou ``bar.z``.

Rien n'empêche de déclarer une structure nommée et d'également déclarer une variable par la même occasion :

.. code-block:: c

    struct Point {
        double x;
        double y;
        double z;
    } foo;
    struct Point bar;

Notons que les noms de structures sont stockés dans un espace de noms différent de celui des variables. C'est à dire qu'il n'y a pas de collision possible et qu'un identifiant de fonction ou de variable ne pourra jamais être comparé à un identifiant de structure. Aussi, l'écriture suivante, bien que perturbante, est tout à fait possible :

.. code-block:: c

    struct point { double x; double y; double z; };
    struct point point;
    point.x = 42;

Initialisation
--------------

Une structure se comporte à peu de chose près comme un tableau sauf que les éléments de la structure ne s'accèdent pas avec l'opérateur crochet ``[]`` mais avec l'opérateur ``.``. Néanmoins une structure est représentée en mémoire comme un contenu linéaire. Notre structure ``struct Point`` serait identique à un tableau de trois ``double`` et par conséquent l'initialisation suivante est possible :

.. code-block:: c

    struct Point point = { 3060426.957, 3192003.220, 4581359.381 };

Néanmoins on préfèrera la notation suivante, équivalente :

.. code-block:: c

    struct Point point = { .x=3060426.957, .y=3192003.220, .z=4581359.381 };

Comme pour un tableau, les valeurs omises sont initialisées à zéro. Et de la même manière qu'un tableau, il est possible d'initialiser une structure à zéro avec ``= {0};``.

Il faut savoir que **C99** restreint l'ordre dans lequel les éléments peuvent être initialisés. Ce dernier doit être l'ordre dans lequel les variables sont déclarées dans la structure.

Notons que des stuctures comportant des types différents peuvent aussi être initialisée de la même manière :

.. code-block:: c

    struct Product {
        int weight; // Grams
        double price; // Swiss francs
        int category;
        char name[64];
    }

    struct Product apple = {321, 0.75, 24, "Pomme Golden"};

Tableaux de structures
----------------------

Une structure est un type comme un autre. Tout ce qui peut être fait avec ``char`` ou ``double`` peut donc être fait avec ``struct``. Et donc, il est aussi possibel de déclarer un tableau de structures. Ici donnons l'exemple d'un tableaux de points initialisés :

.. code-block:: c

    struct Point points[3] = {
        {.x=1, .y=2, .z=3},
        {.z=1, .x=2, .y=3},
        {.y=1}
    };

Assigner une nouvelle valeur à un point est facile :

.. code-block:: c

    point[2].x = 12;

Structures en paramètres
------------------------

L'intérêt d'une structure est de pouvoir passer ou retourner un ensemble de données à une fonction. On a vu qu'une fonction ne permet de retourner qu'une seule primitive. Une structure est ici considérée comme un seul container et l'écriture suivante est possible :

.. code-block:: c

    struct Point generate_point(void) {
        struct Point p = {
            .x = rand(),
            .y = rand(),
            .z = rand()
        };

        return p;
    }

Il est également possible de passer une structure en paramètre d'une fonction :

.. code-block:: c

    double norm(struct point p) {
        return sqrt(p.x * p.x + p.y * p.y + p.z + p.z);
    }

    int main(void) {
        struct Point p = { .x = 12.54, .y = -8.12, .z = 0.68 };

        double n = norm(p);
    }

Contrairement aux tableaux, les structures sont toujours passées par valeur, c'est à dire que l'entier du contenu de la structure sera copié sur la pile (*stack*) en cas d'appel à une fonction. En revanche, en cas de passage par pointeur, seul l'adresse de la structure est passée à la fonction appelée qui peut dès lors modifier le contenu :

.. code-block:: c

    struct Point {
        double x;
        double y;
    };

    void foo(struct Point m, struct Point *n) {
        m.x++;
        n->x++;
    }

    int main(void) {
        struct Point p = {0}, q = {0};
        foo(p, &q);
        printf("%g, %g\n", p.x, q.x);
    }

Le résultat affiché sera ``0.0, 1.0``. Seul la seconde valeur est modifiée.

.. hint::

    Lorsqu'un membre d'une structure est accédé, via son pointeur, on utilise la notation ``->`` au lieu de ``.`` car il est nécessaire de déréférencer le pointeur. Il s'agit d'un sucre syntaxique permettant d'écrire ``p->x`` au lieu de ``(*p).x``

Structures flexibles
--------------------

Introduit avec C99, les membres de structures flexibles ou *flexible array members* (§6.7.2.1) sont un membre de type tableau d'une structure défini sans dimension. Ces membres ne peuvent apparaître qu'à la fin d'une structure.

.. code-block:: c

    struct Vector {
        char name[16]; // name of the vector
        size_t len; // length of the vector
        double array[]; // flexible array member
    };

Cette écriture permet par exemple de réserver un espace mémoire plus grand que la structure de base, et d'utiliser le reste de l'espace domme tableau flexible.

.. code-block:: c

    struct Vector *vector = malloc(1024);
    strcpy(vector->name, "Mon vecteur");
    vector->len = 1024 - 16 - 4;
    for (int i = 0; i < vector->len; i++)
        vector->array[i] = ...

Ce type d'écriture est souvent utilisé pour des contenus ayant un en-tête fixe comme des images BMP ou des fichiers sons WAVE.

Structure de structures
-----------------------

On comprends aisément que l'avantage des structures et le regroupement de variables. Une structure peut être la composition d'autres types composites.

Nous déclarons ici une structure ``struct Line`` composée de ``struct Point`` :

.. code-block:: c

    struct Line {
        struct Point a;
        struct Point b;
    };

L'accès à ces différentes valeurs s'effectue de la façon suivante :

.. code-block:: c

    struct Line line = {.a.x = 23, .a.y = 12, .b.z = 33};
    printf("%g, %g", line.a.x, line.b.x);

Alignement mémoire
------------------

Une structure est agencée en mémoire dans l'ordre de sa déclaration. C'est donc un agencement linéaire en mémoire :

.. code-block:: c

    struct Line lines[2];

.. code-block:: text

    0x0000 line[0].a.x
    0x0004 line[0].a.y
    0x0008 line[0].a.z
    0x000C line[0].b.x
    0x0010 line[0].b.y
    0x0014 line[0].b.z
    0x0018 line[1].a.x
    0x001C line[1].a.y
    0x0020 line[1].a.z
    0x0024 line[1].b.x
    0x0028 line[1].b.y
    0x002C line[1].b.z

Néanmoins, le compilateur se réserve le droit d'optimiser l' `alignement mémoire <https://fr.wikipedia.org/wiki/Alignement_en_m%C3%A9moire>`__. Une architecture 32-bits aura plus de facilité à accéder à des grandeurs de 32 bits or, une structure composée de plusieurs entiers 8-bits demanderait au processeur un coût additionnel pour optimiser le stockage d'information.

Considérons la structure suivante :

.. code-block:: c

    struct NoAlign
    {
        int8_t c;
        int32_t d;
        int64_t i;
        int8_t a[3];
    };

Imaginons pour comprendre qu'un casier mémoire sur une architecture 32-bit est assez grand pour y stocker 4 bytes. Si l'on souhaite représenter la structure ci-dessus sans optimisation de la part du processeur, le casier 0 contiendra  ``c`` tandis que pour obtenir la valeur d il faudra accéder au casier 0 et au casier 1 :

.. code-block:: text

    0x0000 c    <-- data[0]
    0x0001 d0
    0x0002 d1
    0x0003 d2

    0x0004 d3   <-- data[1]
    0x0005 i7
    0x0006 i6
    0x0007 i5

    ...

Ainsi, le compilateur sera obligé de faire du zèle pour accéder à d. En admettant que notre structure peut être accédée comme un tableau on aura :

.. code-block:: c

    int32_t d = (data[0] << 8) | (data[1] & 0x0F);

Pour éviter ces manoeuvres, le compilateur selon l'architecture donnée, va insérer des éléments de rembourrage (*padding*) pour forcer l'alignement mémoire et ainsi optimiser les lectures. La même structure que ci-dessus sera fort probablement implémentée de la façon suivante :

.. code-block:: c

    struct Align
    {
        int8_t c;
        int8_t __pad1[3]; // Inséré par le compilateur
        int32_t d;
        int64_t i;
        int8_t a[3];
        int8_t __pad2; // Inséré par le compilateur
    };

De cette manière, l'accès à ``d`` est facilité au détriment d'une perte substentielle de l'espace de stockage.

Une solution optimale consiste à réagencer la structure initiale peut éviter la perte d'espace mémoire. La structure suivante ne sera pas modifiée par le compilateur car elle est alignée sur 32-bits :

.. code-block:: c

    struct Align
    {
        int32_t d;
        int64_t i;
        int8_t a[3];
        int8_t c;
    };

L'option ``-Wpadded`` de GCC permet lever une alerte lorsqu'une structure est alignée par le compilateur.

Il est néanmoins possible, pour certains compilateurs comme `gcc` ou Visual Studio, d'utiliser un artifice pour forcer l'alignement mémoire. L'utilisation de ``#pragma pack`` permet de forcer un type d'alignement pour une certaine structure. Considérons par exemple la structure suivante :

.. code-block:: c

    struct Test
    {
        char a;
        int b;
        char c;
    };

Elle pourrait être représentée en mémoire de la façon suivante :

.. code-block:: text

    |   1  |  2   |   3  |   4  |
    |------|------|------|------|
    | a(1) | pad............... |
    | b(1) | b(2) | b(3) | b(4) |
    | c(1) | pad............... |

En revance si elle est décrite comme suit :

.. code-block:: c

    #pragma pack(2)

    struct Test
    {
        char a;
        int b;
        char c;
    };

L'emprunte mémoire sera différente :

.. code-block:: text

    |   1  |   2  |
    |------|------|
    | a(1) | c(1) |
    | b(1) | b(2) |
    | b(3) | b(4) |

Enfin, avec ``#pragma pack(1)`` on aura l'alignement mémoire suivant :

.. code-block:: text

    |   1  |
    |------|
    | a(1) |
    | b(1) |
    | b(2) |
    | b(3) |
    | b(4) |
    | c(1) |

Champs de bits
==============

Les champs de bits sont des structures dont une information supplémentaire est ajoutée: le nombre de bits utilisés.

Prenons l'exemple du `module I2C <http://www.ti.com/lit/ug/sprug03b/sprug03b.pdf>`__ du microcontrôleur TMS320F28335. Le registre ``I2CMDR`` décrit à la page 23 est un registre 16-bits qu'il conviendrait de décrire avec un champ de bits :

.. code-block::

    struct I2CMDR {
        int  bc  :3;
        bool fdf :1;
        bool stb :1;
        bool irs :1;
        bool dlb :1;
        bool rm  :1;
        bool xa  :1;
        bool trx :1;
        bool mst :1;
        bool stp :1;
        bool _reserved :1;
        bool stt  :1;
        bool free :1;
        bool nackmod :1;
    };

Activer le bit ``stp`` (bit numéro 12) devient une opération triviale :

.. code-block:: c

    struct I2CMDR i2cmdr;

    i2cmdr.stp = true;

Alors qu'elle demanderait une manipulation de bit sinon :

.. code-block:: c

    int32_t i2cmdr;

    i2cmdr |= 1 << 12;

Notons que les champs de bits, ainsi que les structures seront déclarées différemment selon que l'architecture cible est *little-endian* ou *big-endian*.

Unions
======

Une `union <https://en.wikipedia.org/wiki/Union_type>`__ est une variable qui peut avoir plusieurs représentations d'un même contenu mémoire. Rappelez-vous, au :numref:`storage` nous nous demandions quelle était l'interprétation d'un contenu mémoire donné. Il est possible en C d'avoir toutes les interprétations à la fois :

.. code-block:: c

    #include <stdint.h>
    #include <stdio.h>

    union Mixed
    {
        int32_t signed32;
        uint32_t unsigned32;
        int8_t signed8[4];
        int16_t signed16[2];
        float float32;
    };

    int main(void) {
        union Mixed m = {
            .signed8 = {0b11011011, 0b0100100, 0b01001001, 0b01000000}
        };

        printf(
            "int32_t\t%d\n"
            "uint32_t\t%u\n"
            "char\t%c, %c, %c, %c\n"
            "short\t%hu, %hu\n"
            "float\t%f\n",
            m.signed32,
            m.unsigned32,
            m.signed8[0], m.signed8[1], m.signed8[2], m.signed8[3],
            m.signed16[0], m.signed16[1],
            m.float32
        );
    }

Les unions sont très utilisées en combinaison avec des champs de bits. Pour reprendre l'exemple du champ de bit évoqué plus haut, on peut souhaiter accéder au registre soit sous la forme d'un entier 16-bits soit via chacun de ses bits indépendamment.

.. code-block:: c

    union i2cmdr {
        struct {
            int  bc  :3;
            bool fdf :1;
            bool stb :1;
            bool irs :1;
            bool dlb :1;
            bool rm  :1;
            bool xa  :1;
            bool trx :1;
            bool mst :1;
            bool stp :1;
            bool _reserved :1;
            bool stt  :1;
            bool free :1;
            bool nackmod :1;
        } bits;
        uint16_t all;
    };

Création de type
================

Le mot clé ``typedef`` permet de déclarer un nouveau type. Il est particulièrement utilisé conjointement avec les structures et les unions afin de s'affranchir de la lourdeur d'écriture (préfixe ``struct``), et dans le but de cacher la complexité d'un type à l'utilisateur qui le manipule.

L'exemple suivant déclare un type ``Point`` et un prototype de fonction permettant l'addition de deux points.

.. code-block:: c

    typedef struct {
        double x;
        double y;
    } Point;

    Point add(Point a, Point b);

Compound Literals
=================

Naïvement traduit en *litéraux composés*, un *compound literal* est une méthode de création d'un type composé "à la volée" utilisé de la même façon que les transtypages.

Reprenons notre structure Point ``struct Point`` vue plus haut. Si l'on souhaite changer la valeur du point ``p`` il faudrait on pourrait écrire ceci :

.. code-block:: c

    struct Point p; // Déclaré plus haut

    // ...

    {
        struct Point q = {.x=1, .y=2, .z=3};
        p = q;
    }

Notons que passer par une variable intermédiaire ``q`` n'est pas très utile. Il serait préférable d'écrire ceci :

.. code-block:: c

    p = {.x=1, .y=2, .z=3};

Néanmoins cette écriture mènera à une erreur de compilation car le compilateur cherchera à déterminer le type de l'expression ``{.x=1, .y=2, .z=3}``. Il est alors essentiel d'utiliser la notation suivante :

.. code-block:: c

    p = (struct Point){.x=1, .y=2, .z=3};

Cette notation de litéraux composés peut également s'appliquer aux tableaux. L'exemple suivant montre l'initialisation d'un tableau à la volée passé à la fonction ``foo`` :

.. code-block:: c

    void foo(int array[3]) {
        for (int i = 0; i < 3; i++) printf("%d ", array[i]);
    }

    void main() {
        foo((int []){1,2,3});
    }

-----

.. exercise:: Mendeleïev

    Chaque élément du taleau périodique des éléments comporte les propriétés suivantes :

    - Un nom jusqu'à 20 lettres
    - Un symbole jusqu'à 2 lettres
    - Un numéro atomique de 1 à 118 (2019)
    - Le type de l'élément
        - Métaux
            - Alcalin
            - Alcalino-terreux
            - Lanthanides
            - Actinides
            - Métaux de transition
            - Métaux pauvres
        - Métalloïdes
        - Non métaux
            - Autres
            - Halogène
            - Gaz noble
    - La période: un entier de 1 à 7
    - Le groupe: un entier de 1 à 18

    Déclarer une structure de données permettant de stocker tous les éléments chimiques de tel facon qu'ils puissent être accédés comme :

    .. code-block:: c

        assert(strcmp(table.element[6].name, "Helium") == 0);
        assert(strcmp(table.element[54].type, "Gaz noble") == 0);
        assert(table.element[11].period == 3);

        Element *el = table.element[92];
        assert(el->atomic_weight == 92);

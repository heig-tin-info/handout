===============
Entrées Sorties
===============

Comme nous l'avons vu (c.f. :numref:`inputs_outputs`) un programme dispose de canaux d'entrées sorties ``stdin``, ``stdout`` et ``stderr``. Pour faciliter la vie du programmeur, les bibliothèques standard offrent toute une panoplie de fonctions pour formatter les sorties et interptèter les entrées.

La fonction phare est bien entendu ``printf`` pour le formattage de chaîne de caractère et ``scanf`` pour la lecture de chaînes de caractères. Ces dernières fonctions se déclinent en plusieurs variantes:

- depuis/vers les canaux standards ``printf``, ``scanf``
- depuis/vers un fichier quelconque ``fprintf``, ``fscanf``
- depuis/vers une chaîne de caractère ``sprintf``, ``sscanf``

La liste citée est non exaustive mais largement documentée ici: `<stdio.h> <http://man7.org/linux/man-pages/man3/stdio.3.html>`__.

Sorties non formatées
=====================

Si l'on souhaite simplement écrire du texte sur la sortie standard, deux fonctions sont disponibles:

``putchar(char c)``
    Pour imprimer un caractère unique: ``putchar('c')``

``puts(char[] str)``
    Pour imprimer une chaîne de caractère

.. exercise:: Mot du jour

    Écrire un programme qui retourne un mot parmi une liste de mot, de facon aléatoire.

    .. code-block:: c

        #include <time.h>
        #include <stdlib.h>

        char *words[] = {"Albédo", "Bigre", "Maringouin", "Pluripotent", "Entrechat", "Caracoler" "Palinodie", "Sémillante", "Atavisme", "Cyclothymie", "Idiosyncratique", "Entéléchie"};

        #if 0
            srand(time(NULL));   // Initialization, should only be called once.
            size_t r = rand() % sizeof(words) / sizeof(char*); // Generate random value
        #endif

    .. solution:: c

        .. code-block:: c

            #include <time.h>
            #include <stdlib.h>

            char *words[] = {"Albédo", "Bigre", "Maringouin", "Pluripotent", "Entrechat", "Caracoler" "Palinodie", "Sémillante", "Atavisme", "Cyclothymie", "Idiosyncratique", "Entéléchie"};

            int main(void)
            {
                srand(time(NULL));
                puts(words[rand() % (sizeof(words) / sizeof(char*))]);

                return 0;
            }

Sorties formatées
=================

Convertir un nombre en une chaîne de caractère n'est pas trivial. Prenons l'exemple de la valeur ``123``. Il faut pour cela diviser itérativement le nombre par 10 et calculer le reste:

.. code-block:: text

    Etape  Opération  Resultat  Reste
    1      123 / 10   12        3
    2      12 / 10    1         2
    3      1 / 10     0         1

Comme on ne sait pas à priori combien de caractères on aura, et que ces caractères sont fournis depuis chiffre le moins significatif, il faudra inverser la chaîne de caractère produite.

Voici un exemple possible d'implémentation:

.. code-block:: c
    :caption: iota.c
    :name: iota-c

    void swap(char* a, char* b)
    {
        char t = a;
        a = b;
        b = t;
    }

    void reverse(char str[], size_t length)
    {
        size_t start = 0;
        size_t end = length - 1;
        while (start < end)
        {
            swap(*(str + start), *(str + end));
            start++;
            end--;
        }
    }

    char* itoa(int num, char* str)
    {
        int i = 0;

        bool is_negative = false;

        if (num == 0) {
            str[i++] = '0';
            str[i] = '\0';
            return str;
        }

        if (num < 0) {
            is_negative = true;
            num = -num;
        }

        while (num != 0) {
            int rem = num % 10;
            str[i++] = rem + '0';
            num /= base;
        }

        if (is_negative)
            str[i++] = '-';

        str[i] = '\0';

        reverse(str, i);
        return str;
    }

Cette implémentation pourrait être utilsée de la façon suivante:

.. code-block:: c

    #include <stdlib.h>

    int main(void)
    {
        int num = 123;
        char buffer[10];

        itoa(num, buffer);
    }

printf
======

Vous conviendrez que devoir manuellement convertir chaque valeur n'est pas des plus pratique, c'est pourquoi ``printf`` rend l'opération bien plus aisée en utilsant des marques substitutives (*placeholder*). Ces specifieurs débutent par le caractère ``%`` suivi du formattage que l'on veut appliquer à une variable passée en paramètres. L'exemple suivant utilise ``%d`` pour formatter un entier non signé.

.. code-block:: c

    #include <stdio.h>

    int main()
    {
        int32_t earth_perimeter = 40075;
        printf("La circonférence de la terre vaut vaut %d km", earth_perimeter);
    }

Le standard **C99** défini le prototype de ``printf`` comme étant:

.. code-block:: c

    int printf(const char *restrict format, ...);

Il défini que la fonction ``printf`` prend en paramètre un format suivi de ``...``. La fonction ``printf`` comme toutes celles de la même catégorie sont dit `variadiques <https://fr.wikipedia.org/wiki/Fonction_variadique#C>`__, c'est à dire qu'elles peuvent prendre un nombre variable d'arguments. Il y aura autant d'arguments additionnels que de marqueurs utilisés dans le format. Ainsi le format ``"Mes nombres préférés sont %d et %d mais surtout %s"`` demandera trois paramètres additionnels:

La fonction retourne le nombre de caractères formatés ou ``-1`` en cas d'erreur.

La construction d'un marqueur est loin d'être simple mais heureusement on n'a pas besoin de tout connaitre et la page wikipedia `printf format string <https://en.wikipedia.org/wiki/Printf_format_string>`__ est d'une grande aide. Le format de construction est le suivant:

.. code-block:: c

    %[parameter][flags][width][.precision][length]type

``parameter`` (optionnel)
    Numéro de paramètre à utiliser

``flags`` (optionnel)
    Modificateurs: préfixe, signe plus, alignement à gauche, ...

``width`` (optionnel)
    Nombre **minimum** de caractères à utiliser pour l'affichage de la sortie.

``.precision`` (optionnel)
    Nombre **minimum** de caractères affichés à droite de la virgule. Essentiellement valide pour les nombre à virgule flottante.

``length`` (optionnel)
    Longueur en mémoire. Indique la longueur de la représentation binaire

``type``
    Type de formattage souhaité

.. figure:: ../assets/figures/string/formats.*

    Formattage d'un marqueur

Exemples
--------

+---------------------------------+-----------------+--------+
| Exemple                         | Sortie          | Taille |
+=================================+=================+========+
| ``printf("%c", 'c')``           | ``c``           | 1      |
+---------------------------------+-----------------+--------+
| ``printf("%d", 1242)``          | ``1242``        | 4      |
+---------------------------------+-----------------+--------+
| ``printf("%10d", 42)``          | ``'       42'`` | 10     |
+---------------------------------+-----------------+--------+
| ``printf("%07d", 42)``          | ``0000042``     | 7      |
+---------------------------------+-----------------+--------+
| ``printf("%+-5d", 23)``         | ``'+23   '``    | 6      |
+---------------------------------+-----------------+--------+
| ``printf("%5.3f", 314.)``       | ``314.100``     | 7      |
+---------------------------------+-----------------+--------+
| ``printf("%*.*f", 4, 2, 102.)`` | ``102.10``      | 7      |
+---------------------------------+-----------------+--------+
| ``printf("%8x", 3141592)``      | ``2fefd8``      | 6      |
+---------------------------------+-----------------+--------+
| ``printf("%s", "Hello")``       | ``Hello``       | 5      |
+---------------------------------+-----------------+--------+

Entrées formatées
=================

A l'instar de la sortie formatée, il est possible de lire les saisies au clavier ou *parser* une chaîne de caractère, c'est à dire faire un `analyse syntaxique <https://fr.wikipedia.org/wiki/Analyse_syntaxique>`__ de son contenu pour en extraire de l'information.

La fonction ``scanf`` est par exmple utilisée à cette fin:

.. code-block:: c

    #include <stdio.h>

    int main()
    {
        int favorite;

        printf("Quelle est votre nombre favori ? ");
        scanf("%d", &favorite);

        printf("Saviez-vous que votre nombre favori, %d, est %s ?\n",
            favorite,
            favorite % 2 ? "impair" : "pair");
    }

Cette fonction utilise l'entrée standard ``stdin``. Il est donc possible soit d'exécuter ce programme en mode interactif:

.. code-block:: console

    $ ./a.out
    Quelle est votre nombre favori ? 2
    Saviez-vous que votre nombre favori, 2, est pair ?

soit exécuter ce programme en fournissant le nécessaire à stdin:

.. code-block:: console

    $ echo "23" | ./a.out
    Quelle est votre nombre favori ? Saviez-vous que votre nombre favori, 23, est impair ?

On observe ici un comportement différent car le retour clavier lorsque la touche *enter* est pressée n'est pas transmi au programme mais c'est le shell qui l'intercepte.

scanf
-----

Le format de ``scanf`` se rapproche de ``printf`` mais en plus simple. Le `man scanf <https://linux.die.net/man/3/scanf>`__ ou même la page Wikipedia de `scanf <https://en.wikipedia.org/wiki/Scanf_format_string>`__ renseigne sur son format.

Cette fonction tient son origine une nouvelle fois de `ALGOL 68 <https://en.wikipedia.org/wiki/ALGOL_68>`__ (``readf``), elle est donc très ancienne.

La compréhension de ``scanf`` n'est pas évidente et il est utile de se familiariser sur son fonctionnement à l'aide de quelques exemples.

Le programme suivant lit un entier et le place dans la variable ``n``. ``scanf`` retourne le nombre d'assignment réussis. Ici, il n'y a qu'un *placeholder*, on s'attends naturellement à lire ``1`` si la fonction réussi. Le programme écrit ensuite les nombres dans l'ordre d'apparition.

.. code-block:: c

    #include <stdio.h>

    int main(void)
    {
        int i = 0, n;

        while (scanf("%d", &n) == 1)
            printf("%i\t%d\n", ++i, n);
        return 0;
    }

Si le code est exécuté avec une suite arbitraire de nombres:

.. code-block:: text

    456 123 789     456 12
    456 1
        2378

il affichera chacun des nombres dans l'ordre d'apparition:

.. code-block:: console

    $ cat << EOF | ./a.out
    456 123 789     456 12
    456 1
        2378
    EOF
    1       456
    2       123
    3       789
    4       456
    5       12
    6       456
    7       1
    8       2378

Voyons un exemple plus complexe (c.f. C99 §7.19.6.2-19).

.. code-block:: c

    int count;
    float quantity;
    char units[21], item[21];

    do {
        count = scanf("%f%20s de %20s", &quant, units, item);
        scanf("%*[^\n]");
    } while (!feof(stdin) && !ferror(stdin));

Lorsqu'exécuté avec ce contenu:

.. code-block:: text

    2 litres de lait
    -12.8degrés Celsius
    beaucoup de chance
    10.0KG de
    poussière
    100ergs de energie

le programme se déroule comme suit:

.. code-block:: c

    quantity = 2; strcpy(units, "litres"); strcpy(item, "lait");
    count = 3;

    quantity = -12.8; strcpy(units, "degrees");
    count = 2; // "C" échoue lors du test de "d" (de)

    count = 0; // "b" de "beaucoup" échoue contre "%f" s'attendant à un float

    quantity = 10.0; strcpy(units, "KG"); strcpy(item, "poussière");
    count = 3;

    count = 0; // "100e" échoue contre "%f" car "100e3" serait un nombre valable
    count = EOF; // Fin de fichier

Dans cet exemple, la boucle ``do``... ``while`` est utilisée car il n'est pas simplement possible de traiter le cas ``while(scanf(...) > 0`` puisque l'exemple cherche à montrer les cas particuliers où justement, la capture échoue. Il est nécessaire alors de faire appel à des fonctions de plus bas niveau ``feof`` pour détecter si la fin du fichier est atteint, et ``ferror`` pour détecter une éventuelle erreur sur le flux d'entrée.

La directive ``scanf("%*[^\n]");`` étant un peu particulière, il peu valoir la peine de s'y attarder un peu. Le *flag* ``*``, différent de ``printf`` indique d'ignorer la capture en cours. L'exemple suivant montre comment ignorer un mot.

.. code-block:: c

    #include <assert.h>
    #include <stdio.h>

    int main(void) {
        int a, b;
        char str[] = "24 kayak 42";

        sscanf(str, "%d%*s%d", &a, &b);
        assert(a == 24);
        assert(b == 42);
    }

Ensuite, ``[^\n]``. Le marqueur ``[``, terminé par ``]`` cherche à capturer une séquence de caractères parmis une liste de caractères acceptés. Cette syntaxe est inspirée des `expressions régulières <https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re>`__ très utilisées en informatique. Le caractère ``^`` à une signification particulière, il indique que l'on cherche à capturer une séquence de caractères parmis une liste de caractères **qui ne sont pas acceptés**. C'est une sorte de négation. Dans le cas présent, cette directive ``scanf`` cherche à consommer tous les caractères jusqu'à une fin de ligne car, dans le cas ou la capture échoue à ``C`` de ``Celcius``, le pointeur de fichier est bloqué au caractère ``C`` et au prochain tour de boucle, ``scanf`` échoura au même endroit. Cette instruction est donc utilisée pour repartir sur des bases saines en sautant à la prochaine ligne.

Saisie de chaîne de caractères
------------------------------

Lors d'une saisie de chaîne de caractère, il est nécessaire de **toujours** indiquer une taille maximum de chaîne comme ``%20s`` qui limite la capture à 20 caractères, soit une chaîne de 21 caractères avec son ``\0``. Sinon, il y a risque de `fuite mémoire <https://fr.wikipedia.org/wiki/Fuite_de_m%C3%A9moire>`__:

.. code-block:: c

    int main(void) {
        char a[6];
        char b[10] = "Râteau";

        char str[] = "jardinage";
        sscanf(str, "%s", &a);

        printf("a. %s\nb. %s\n", a, b);
    }

.. code-block:: console

    $ ./a.out
    a. jardinage
    b. age

Ici la variable b contient ``age`` alors qu'elle devrait contenir ``râteau``. La raison est que le mot capturé ``jardinage`` est trop long pour la variable ``a`` qui n'est disposée à stocker que 5 caractères imprimables. Il y a donc dépassement mémoire et comme vous le constatez, le compilateur ne génère aucune erreur. La bonne méthode est donc de protéger la saisie ici avec ``%5s``.

Saisie arbitraire
-----------------

Comme brièvement évoqué plus haut, il est possible d'utiliser le marqueur ``[`` pour capturer une séquence de caractères. Imaginons que je souhaite capturer un nombre en `tetrasexagesimal <https://en.wikipedia.org/wiki/Base64>`__ (base 64). Je peux écrire:

.. code-block:: c

    char input[] = "Q2hvY29sYXQ";
    char output[128];
    sscanf(input, "%127[0-9A-Za-z+/]", &output);

Dans cet exemple je capture les nombres de 0 à 9 ``0-9`` (10), les caractères majuscules et minuscules ``A-Za-z`` (52), ainsi que les caractères ``+``, ``/`` (2), soit 64 caractères. Le buffer d'entrée étant fixé à 128 positions, la saisie est contrainte à 127 caractères imprimables.

.. exercise:: Crampes de doigts

    Votre collègue n'a pas cessé de se plaindre de crampes... aux doigts... Il a écrit le programme suivant avant de prendre congé pour se rendre chez son médecin.

    Grace à votre esprit affuté et votre oeil perçant vous identifiez 13 erreurs. Lesquelles sont-elles ?

    .. code-block:: c

        #include <std_io.h>
        #jnclude <stdlib.h>
        INT Main()
        {
        int a, sum;
        printf("Addition de 2 entiers a et b.\n");

        printf("a: ")
        scanf("%d", a);

        printf("b: ");
        scanf("%d", &b);

        /* Affichage du résultat
        somme = a - b;
        Printf("%d + %d = %d\n", a, b, sum);

        retturn EXIT_FAILURE;
        }
        }

    .. solution::

        Une fois la correction effectuée, vous utilisez l'outil de ``diff`` pour montrer les différences:

        .. code-block:: diff

            1,3c1,3
            <         #include <stdio.h>
            <         #include <stdlib.h>
            <         int main()
            ---
            >         #include <std_io.h>
            >         #jnclude <stdlib.h>
            >         INT Main()
            5c5
            <         int a, b, sum;
            ---
            >         int a, sum;
            9c9
            <         scanf("%d", &a);
            ---
            >         scanf("%d", a);
            14,16c14,16
            <         /* Affichage du résultat */
            <         sum = a + b;
            <         printf("%d + %d = %d\n", a, b, sum);
            ---
            >         /* Affichage du résultat
            >         somme = a - b;
            >         Printf("%d + %d = %d\n", a, b, sum);
            18c18,19
            <         return EXIT_SUCCESS;
            ---
            >         retturn EXIT_FAILURE;
            >         }


.. exercise:: Géométrie affine

    Considérez le programme suivant:

    .. code-block:: c
        :linenos:

        #include <stdio.h>
        #include <stdlib.h>

        int main(void)
        {
            float a;
            printf("a = ");
            scanf("%f", &a);

            float b;
            printf("b = ");
            scanf("%f", &b);

            float x;
            printf("x = ");
            scanf("%f", &x);

            float y = a * x + b;

            printf("y = %f\n", y);

            return 0;
        }

    #. À quelle ligne commence l'exécution de ce programme ?
    #. Dans quel ordre s'exécutent les instruction ?
    #. Décrivez ce que fait ce programme étape par étape
    #. Que verra l'utilisateur à l'écran ?
    #. Quel est l'utilité de ce programme ?

    .. solution::

        #. Ligne 6
        #. C est un langage impératif, l'ordre est séquentiel du haut vers le bas
        #. Les étapes sont les suivantes:
            #. Demande de la valeur de ``a`` à l'utilisateur
            #. Demande de la valeur de ``b`` à l'utilisateur
            #. Demande de la valeur de ``x`` à l'utilisateur
            #. Calcul de l'image affine de ``x`` (équation de droite)
            #. Affichage du résultat
        #. Que verra l'utilisateur à l'écran ?
            #. Il verra ``y = 12`` pour ``a = 2; x = 5; b = 2``
        #. Quel est l'utilité de ce programme ?
            #. Le calcul d'un point d'une droite

.. exercise:: Équation de droite

    L'exercice précédant souffre de nombreux défauts. Sauriez-vous les identifier et perfectionner l'implémentation de ce programme ?

    .. solution::

        Citons les défauts de ce programme:

        - Le programme ne peut pas être utilisé avec les arguments, uniquement en mode interactif
        - Les invité de dialogue ``a = ``, ``b = `` ne sont pas clair, ``a`` et ``b`` sont associés à quoi ?
        - La valeur de retour n'est pas exploitable directement.
        - Le nom des variables utilisé n'est pas clair.
        - Aucune valeurs par défaut.

        Une solution possible serait:

        .. literalinclude:: ../assets/src/linear.c
            :language: c
            :caption: linear.c

.. exercise:: Loi d'Ohm

    Écrivez un programme demandant deux réels ``tension`` et ``résistance``, et afficher ensuite le ``courant``. Prévoir un test pour le cas où la résistance serait nulle.

.. exercise:: Tour Eiffel

    Considérons le programme suivant:

    .. code-block:: c

        #include <stdio.h>
        #include <stdlib.h>
        #include <math.h>

        int main()
        {
            printf("Quel angle mesurez-vous en visant le sommet du bâtiment (en degrés): ");
            float angle_degre;
            scanf("%f", &angle_degrees);
            float angle_radian = angle_degrees * M_PI / 45.;

            printf("A quel distance vous trouvez vous du bâtiment (en mètres): ");
            float distance;
            scanf("%f", &distance);

            float height = distance / tan(angle_radian);
            printf("La hauteur du batiment est : %g mètres.\n", height);

            return 0;
        }

    #. Que fait le programme étape par étape ?
    #. Que verra l'utilisateur à l'écran ?
    #. A quoi sert ce programme ?
    #. Euh mais ? Ce programme comporte des erreurs, lesquelles ?
    #. Implémentez-le et testez-le.

.. exercise:: Hyperloop

    `Hyperloop <https://fr.wikipedia.org/wiki/Hyperloop>`__ (aussi orthographié **Hyperl∞p**) est un projet ambitieux d'Elon Musk visant à construire un moyen de transport ultra rapide utilsant des capsules voyageant dans un tube sous vide. Ce projet est analogue à celui étudié en suisse et nommé `Swissmetro <https://fr.wikipedia.org/wiki/Swissmetro>`__ mais abandonné en 2009.

    Néamoins, les ingénieurs suisse avaient à l'époque écrit un programme pour calculer, compte tenu d'une vitesse donnée, le temps de parcours entre deux villes de suisse.

    Écrire un programme pour calculer la distance entre deux ville de suisse parmis lesquelles proposées sont:

        - Genève
        - Zürich
        - Bâle
        - Bern
        - St-Galle

    Considérez une accélération de 0.5 g pour le calcul de mouvement, et une vitesse maximale de 1220 km/h.




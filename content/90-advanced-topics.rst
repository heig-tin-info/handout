======
Avancé
======

Ce chapitre regroupe les sujets avancés dont la compréhension n'est pas requise pour le contrôle de connaissance.

.. _sequence_point:

Points de séquences
===================

On appelle un point de séquence ou `sequence point <https://en.wikipedia.org/wiki/Sequence_point>`__ exprimé dans l'annexe C du standard C99 chaque élément de code dont l'exécution est garantie avant la séquence suivante. Ce qu'il est important de retenir c'est :

- L'appel d'une fonction est effectué après que tous ses arguments ont été évalués
- La fin du premier opérande dans les opérations ``&&``, ``||``, `?` et `,`.
    - Ceci permet de court-circuiter le calcul dans ``a() && b() ``. La condition ``b()`` n'est jamais évaluée si la condition ``a()`` est valide.
- Avant et après des actions associées à un formatage d'entrée sortie

L'opérateur d'assignation ``=`` n'est donc pas un point de séquence et l'exécution du code ``(a = 2) + a + (a = 2)`` est par conséquent indéterminée.

Complément sur les variables initialisées
=========================================

Le fait de déclarer des variables dans en langage C implique que le
logiciel doit réaliser l'initialisation de ces variables au tout début
de son exécution. De fait, on peut remarquer deux choses. Il y a les
variables initialisées à la valeur zéro et les variables initialisées à
des valeurs différentes de zéro. Le compilateur regroupe en mémoire ces
variables en deux catégories et ajoute un bout de code au début de votre
application (qui est exécuté avant le *main*).

Ce code (que l'on n'a pas à écrire) effectue les opérations suivantes :

-  mise à zéro du bloc mémoire contenant les variables ayant été
   déclarées avec une valeur d'initialisation à zéro

-  recopie d'une zone mémoire contenant les valeurs initiales des
   variables ayant été déclarées avec une valeur d'initialisation
   différente de zéro vers la zone de ces mêmes variables.

Par ce fait, dès que l'exécution du logiciel est effectuée, on a, lors
de l'exécution du *main*, des variables correctement initialisées.

Binutils
========

Les outils binaires (`binutils <https://en.wikipedia.org/wiki/GNU_Binutils>`__) sont une collection de programmes installés avec un compilateur et permettant d'aider au développement et au débogage. Certains de ces outils sont très pratiques, mais nombreux sont les développeurs qui ne les connaissent pas.

``nm``
    Liste tous les symboles dans un fichier objet (binaire). Ce programme appliqué sur le programme hello world de l'introduction donne :

    .. code-block:: console

        $ nm a.out
        0000000000200dc8 d _DYNAMIC
        0000000000200fb8 d _GLOBAL_OFFSET_TABLE_
        00000000000006f0 R _IO_stdin_used
                        w _ITM_deregisterTMCloneTable
                        w _ITM_registerTMCloneTable

        ...

                        U __libc_start_main@@GLIBC_2.2.5
        0000000000201010 D _edata
        0000000000201018 B _end
        00000000000006e4 T _fini
        00000000000004f0 T _init
        0000000000000540 T _start

        ...

        000000000000064a T main
                         U printf@@GLIBC_2.2.5
        00000000000005b0 t register_tm_clones

    On observe notamment que la fonction ``printf`` est en provenance de la bibliothèque GLIBC 2.2.5, et qu'il y a une fonction ``main``.

``strings``
    Liste toutes les chaînes de caractères imprimables dans un fichier binaire. On observe tous les symboles de débug qui sont par défaut intégrés au fichier exécutable. On lit également la chaîne de caractère ``hello, world``. Attention donc à ne pas laisser les éventuels mots de passes ou numéro de licence en clair dans un fichier binaire.

    .. code-block:: console

        $ strings a.out
        /lib64/ld-linux-x86-64.so.2
        libc.so.6
        printf

        ...

        AUATL
        []A\A]A^A_
        hello, world
        ;*3$"
        GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0

        ...

        _IO_stdin_used
        __libc_csu_init
        __bss_start
        main
        __TMC_END__
        _ITM_registerTMCloneTable
        __cxa_finalize@@GLIBC_2.2.5
        .symtab
        .strtab

        ...

        .data
        .bss
        .comment

``size``
    Liste la taille des segments mémoires utilisés. Ici le programme représente 1517 bytes, les données initialisées 8 bytes, les données variables 600 bytes, soit une somme décimale de 2125 bytes ou ``84d`` bytes.

    .. code-block:: console

        $ size a.out
        text    data     bss     dec     hex filename
        1517     600       8    2125     84d a.out

Format Q
========

Le format `Q <https://en.wikipedia.org/wiki/Q_(number_format)>`__ est une notation en virgule fixe dans laquelle le format d'un nombre est représenté par la lettre **Q** suivie de deux nombres :

1. Le nombre de bits entiers
2. Le nombre de bits fractionnaires

Ainsi, un registre 16 bits contenant un nombre allant de +0.999 à -1.0 s'exprimera **Q1.15** soit 1 + 15 valant 16 bits.

Pour exprimer la valeur pi (3.1415...) il faudra au minimum 3 bits pour représenter la partie entière, car le bit de signe doit rester à zéro. Le format sur 16 bits sera ainsi **Q4.12**.

La construction de ce nombre est facile :

1. Prendre le nombre réel
2. Le multiplier par 2 à la puissance du nombre de bits
3. Prendre la partie entière

.. code-block:: text

    1.    3.1415926535
    2.    2**12 * 3.1415926535 = 12867.963508736
    3.    12867

Pour convertir un nombre **Q4.12** en sa valeur réelle il faut :

1. Prendre le nombre encodé en **Q4.12**
2. Diviser sa valeur 2 à la puissance du nombre de bits

.. code-block:: text

    1.    12867
    2.    12867 / 2**12 = 3.141357421875

On note une perte de précision puisqu'il n'est pas possible d'encoder un tel nombre dans seulement 16 bits. L'incrément positif minimal serait : :math:`1 / 2^12 = 0.00024`. Il convient alors d'arrondir le nombre à la troisième décimale soit 3.141.

Les opérations arithmétiques sont possibles facilement entre des nombres de même types.

Addition
--------

L'addition peut se faire avec ou sans saturation :

.. code-block:: c

    typedef int16_t Q;
    typedef Q Q12;

    Q q_add(Q a, Q b) {
        return a + b;
    }

    Q q_add_sat(Q a, Q b) {
        int32_t res = (int32_t)a + (int32_t)b;
        res = res > 0x7FFF ? 0x7FFF : res
        res = res < -1 * 0x8000 ? -1 * 0x8000 : res;
        return (Q)res;
    }

Multiplication
--------------

Soit deux nombres 0.9 et 3.141 :

.. code-block:: text

    ┌─┬─┬─┬─╀─┬─┬─┬─┐┌─┬─┬─┬─┬─┬─┬─┬─┦
    │0│0│0│0│1│1│1│0││0│1│1│0│0│1│1│0│ Q4.12 (0.9) 3686
    └─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘

    ┌─┬─┬─┬─╀─┬─┬─┬─┐┌─┬─┬─┬─┬─┬─┬─┬─┦
    │0│0│1│1│0│0│1│0││0│1│0│0│0│0│1│1│ Q4.12 (3.141) 12867
    └─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘

Multiplier ces deux valeurs revient à une multiplication sur 2 fois la taille. Le résultat doit être obtenu sur 32-bits sachant que les nombre **Q** s'additionnent comme **Q4.12** x **Q4.12** donnera **Q8.24**.

On voit immédiatement que la partie entière vaut 2, donc 90% de 3.14 donnera une valeur en dessous de 3. Pour reconstruire une valeur **Q8.8** il convient de supprimer les 16-bits de poids faible

.. code-block:: text

    3686 * 12867 = 47227762

    ┌─┬─┬─┬─┬─┬─┬─┬─┦┌─┬─┬─┬─┬─┬─┬─┬─┐┌─┬─┬─┬─┬─┬─┬─┬─┐┌─┬─┬─┬─┬─┬─┬─┬─┦
    │0│0│0│0│0│0│1│0││1│1│0│1│0│0│0│0││1│0│1│0│0│0│1│1││0│1│1│1│0│0│1│0│ Q8.24
    └─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘

    ┌─┬─┬─┬─┬─┬─┬─┬─┦┌─┬─┬─┬─┬─┬─┬─┬─┦
    │0│0│0│0│0│0│1│0││1│1│0│1│0│0│0│0│ Q8.8
    └─┴─┴─┴─┴─┴─┴─┴─┘└─┴─┴─┴─┴─┴─┴─┴─┘

.. code-block:: c

    inline Q q_sat(int32_t x) {
        x = x > 0x7FFF ? 0x7FFF : x
        x = x < -1 * 0x8000 ? -1 * 0x8000 : x;
        return (Q)x;
    }

    inline int16_t q_mul(int16_t a, int16_t b, char q)
    {
        int32_t c = (int32_t)a * (int32_t)b;
        c += 1 << (q - 1);
        return sat(c >> q);
    }

    inline int16_t q12_mul(int16_t a, int16_t b)
    {
        return q_mul(a, b, 12);
    }

.. _TranslationUnits:

===================
Compilation séparée
===================

Translation unit
================

En programmation, on appelle *translation unit* (unité de traduction), un code qui peut être **compilé** en un **objet** sans autre dépendance externe. Le plus souvent, une unité de traduction correspond à un fichier C.

Diviser pour mieux régner
=========================

De même qu'un magasine illustré est divisé en sections pour accroître la lisibilité (sport, news, annonces, météo) de même un code source est organisé en éléments fonctionnels le plus souvent séparés en plusieurs fichiers et ces derniers parfois maintenus par différents développeurs.

Rappelons-le (et c'est très important) :

- une fonction ne devrait pas dépasser un écran de haut (~50 lignes) ;
- un fichier ne devrait pas dépasser 1000 lignes ;
- une ligne ne devrait pas dépasser 80 caractères.

Donc à un moment, il est essentiel de divisier son travail en créant plusieurs fichiers.

Ainsi, lorsque le programme commence à être volumineux, sa lecture, sa compréhension et sa mise au point deviennent délicates même pour le plus aguéri des développeur. Il est alors essentiel de scinder le code source en plusieurs fichiers. Prenons l'exemple d'un programme qui effectue des calculs sur les nombres complexes. Notre projet est donc constitué de trois fichiers :

.. code-block:: console

    $ tree
    .
    ├── complex.c
    ├── complex.h
    └── main.c

Le programme principal et la fonction ``main`` est contenu dans ``main.c`` quant au module *complex* il est composé de deux fichiers : ``complex.h`` l'en-tête et ``complex.c``, l'implémentation du module.

Le fichier ``main.c`` devra inclure le fichier ``complex.h`` afin de
pourvoir utiliser correctement les fonctions du module de gestion des
nombres complexes. Exemple :

.. code-block:: c

    // fichier main.c
    #include "complex.h"

    int main() {
        Complex c1 = { .real = 1., .imag = -3. };
        complex_fprint(stdout, c1);
    }

.. code-block:: c

    // fichier complex.h
    #ifndef COMPLEX_H
    #define COMPLEX_H

    #include <stdio.h>

    typedef struct Complex {
        double real;
        double imag;
    } Complex, *pComplex;

    void complex_fprint(FILE *fp, const Complex c);

    #endif // COMPLEX_H

.. code-block:: c

    // fichier complex.c
    #include "complex.h"

    void complex_fprint(FILE* fp, const Complex c) {
        fprintf(fp, "%+.3lf + %+.3lf\n", c.real, c.imag);
    }


Un des avantages majeurs à la création de modules est qu'un module
logiciel peut être réutilisé pour d'autres applications. Plus besoin de
réinventer la roue à chaque application !

Cet exemple sera compilé dans un environnement POSIX de la facon suivante :

.. code-block:: console

    gcc -c complex.c -o complex.o
    gcc -c main.c -o main.o
    gcc complex.o main.o -oprogram -lm

Nous verrons plus bas les éléments théoriques vous permettant de mieux comprendre ces lignes.

Module logiciel
===============

Les applications modernes dépendent souvent de nombreux modules logiciels externes aussi utilisés dans d'autres projets. C'est avantageux à plus d'un titre :

- les modules externes sont sous la responsabilité d'autres développeurs et le programme a développer comporte moins de code ;
- les modules externes sont souvent bien documentés et testés et il est facile de les utiliser ;
- la lisibilité du programme est accrue car il est bien découpé en des ensembles fonctionnels ;
- les modules externes sont réutilisables et indépendants, ils peuvent donc être réutilisés sur plusieurs projets.

Lorsque vous utiliser la fonction ``printf``, vous dépendez d'un module externe nommé ``stdio``. En réalité l'ensemble des modules ``stdio``, ``stdlib``, ``stdint``, ``ctype``... sont tous groupé dans une seule bibliothèque logicielle nommée ``libc`` disponible sur tous les systèmes compatibles POSIX. Sous Linux, le pendant libre ``glibc`` est utilisée. Il s'agit de la biblothèque `GNU C Library <https://fr.wikipedia.org/wiki/GNU_C_Library>`__.

Un module logiciel peut se composer de fichiers sources, c'est à dire un ensemble de fichiers ``.c`` et ``.h`` ainsi qu'une documentation et un script de compilation (``Makefile``). Alternativement, un module logiciel peut se composer de bibliothèques déjà compilées sous la forme de fichiers ``.h``, ``.a`` et ``.so``. Sous Windows on rencontre fréquemment l'extension ``.dll``. Ces fichiers compilés ne donnent pas accès au code source mais permettent d'utiliser les fonctionnalités quelles offrent dans des programmes C en mettant à disposition un ensemble de fonctions documentées.

Compilation avec assemblage différé
===================================

Lorsque nous avions compilé notre premier exemple `Hello World <hello>`__ nous avions simplement appelé ``gcc`` avec le fichier source ``hello.c`` qui nous avait créé un exécutable ``a.out``. En réalité, GCC est passé par plusieurs sous étapes de compilation :

1. **Préprocessing** : les commentaires sont retirés, les directives pré-processeur sont remplacées par leur équivalent C.
2. **Compilation** : le code C d'une seule *translation unit* est converti en langage machine en un fichier objet ``.o``.
3. **Édition des liens** : aussi nommé *link*, les différents fichiers objets sont réunis en un seul exécutable.

Lorsqu'un seul fichier est fourni à GCC, les trois opérations sont effectuées en même temps mais ce n'est plus possible aussitôt que le programme est composé de plusieurs unités de translation (plusieurs fichiers C). Il est alors nécessaire de compiler manuellement chaque fichier source et d'en créer.

La figure suivante résume les différentes étapes de GCC. Les pointillés indiquent à quel niveau les opérations peuvent s'arrêter. Il est dès lors possible de passer par des fichiers intermédiaires assembleur (``.s``) ou objets (``.o``) en utilisant la bonne commande.

.. figure:: ../assets/figures/dist/toolchain/gcc.*

    Étapes intermédiaires de compilation avec GCC

Notons que ces étapes existent quelque soit le compilateur ou le système d'exploitation. Nous retrouverons ces exactes mêmes étapes avec Microsoft Visual Studio mais le nom des commandes et les extensions des fichiers peuvent varier s'ils ne respectent pas la norme POSIX (et GNU).

Notons que généralement, seul deux étapes de GCC sont utilisées :

1. Compilation avec ``gcc -c <fichier.c>``, ceci génère automatiquement un fichier ``.o`` du même nom que le fichier d'entrée.
2. Édition des liens avec ``gcc <fichier1.o> <fichier2.o> ...``, ceci génère automatiquement un fichier exécutable ``a.out``.

Fichiers d'en-tête (*header*)
=============================

Les fichiers d'en-tête (``.h``) sont des fichiers écrits en langage C mais qui ne contienne pas d'implémentation de fonctions. Un tel fichier ne contient donc pas de ``while``, de ``for`` ou même de ``if``. Par convention ces fichiers ne contienne que :

- Des prototypes de fonctions (ou de variables).
- Des déclaration de types (``typedef``, ``struct``).
- Des définitions pré-processeur (``#include``, ``#define``).

Nous l'avons vu dans le chapitre sur le pré-processeur, la directive ``#include`` ne fait qu'inclure le contenu du fichier cible à l'emplacement de la directive. Il est donc possible (mais fort déconseillé), d'avoir la situation suivante :

.. code-block:: c

    // main.c
    int main() {
       #include "foobar.def"
    }

Et le fichier ``foobar.def`` pourrait cotenir :

.. code-block:: c

    // foobar.def
    #ifdef FOO
    printf("hello foo!\n");
    #else
    printf("hello bar!\n");
    #endif

Vous noterez que l'extension de ``foobar`` n'est pas ``.h`` puisque le contenu n'est pas un fichier d'en-tête. ``.def`` ou n'importe quelle autre extension pourrait donc faire l'affaire ici.

Dans cet exemple, le pré-processeur ne fait qu'inclure le contenu du fichier ``foobar.def`` à l'emplacement de la définition ``#include "foobar.def"``. Voyons le en détail :

.. code-block:: console

    $ cat << EOF > main.c
    → int main() {
    →     #include "foobar.def"
    →     #include "foobar.def"
    → }
    → EOF

    $ cat << EOF > foobar.def
    → #ifdef FOO
    → printf("hello foo!\n");
    → #else
    → printf("hello bar!\n");
    → #endif
    → EOF

    $ gcc -E main.c | sed '/^#/ d'
    int main() {
    printf("hello bar\n");
    printf("hello bar\n");
    }

Lorsque l'on observe le résultat du pré-processeur, on s'aperçois que toutes les directives préprocesseur ont disparues et que la directive ``#include`` a été remplacée par de contenu de ``foobar.def``. Remarquons que le fichier est inclus deux fois, nous verrons plus loin comme éviter cela.

Nous avons vu au chapitre sur les `prototypes de fonctions <function_prototype>`__ qu'il est possible de ne déclarer que la première ligne d'une fonction. Ce prototype permet au compilateur de savoir combien d'arguments est composé une fonction sans nécessairement disposer de l'implémentation de cette fonction. Aussi on trouve dans tous les fichiers d'en-tête des déclaration en amont (*forward declaration*). Dans le fichier d'en-tête ``stdio.h`` on trouvera la ligne : ``int printf( const char *restrict format, ... );``.

.. code-block::c

    $ cat << EOF > main.c
    → #include <stdio.h>
    → int main() { }
    → EOF

    $ gcc -E main.c | grep -P '\bprintf\b'
    extern int printf (const char *__restrict __format, ...);

Notons qu'ici le prototype est précédé par le mot clé ``extern``. Il s'agit d'un mot clé **optionnel** permettant de renforcer l'intention du développeur que la fonction déclarée n'est pas inclue dans fichier courant mais qu'elle est implémentée ailleurs, dans un autre fichier. Et c'est le cas car ``printf`` est déjà compilée quelque part dans la bibliothèque ``libc`` inclue par défaut lorsqu'un programme C est compilé dans un environnement POSIX.

Un fichier d'en-tête contiendra donc tout le nécessaire utile à pouvoir utiliser une bibliothèque externe.

Protection de réentrance
------------------------

La protection de réentrence aussi nommée *header guards* est une solution au problème d'inclusion multiple. Si par exemple on défini dans un fichier d'en-tête un nouveau type et que l'on inclus ce fichier, mais que ce dernier est déjà inclu par une autre bibliothèque une erreur de compilation apparaîtera :

.. code-block:: console

    $ cat << EOF > main.c
    → #include "foo.h"
    → #include "bar.h"
    → int main() {
    →    Bar bar = {0};
    →    foo(bar);
    → }
    → EOF

    $ cat << EOF > foo.h
    → #include "bar.h"
    →
    → extern void foo(Bar);
    → EOF

    $ cat << EOF > bar.h
    → typedef struct Bar {
    →    int b, a, r;
    → } Bar;
    → EOF

    $ gcc main.c
    In file included from main.c:2:0 :
    bar.h:1:16: error: redefinition of ‘struct Bar’
    typedef struct Bar {
                    ^~~
    In file included from foo.h:1:0,
                    from main.c:1 :
    bar.h:1:16: note: originally defined here
    typedef struct Bar {
                    ^~~
    In file included from main.c:2:0 :
    bar.h:3:3: error: conflicting types for ‘Bar’
    } Bar;
    ^~~
    ...

Dans cet exemple l'utilisateur ne sait pas forcément que ``bar.h`` est déjà inclus avec ``foo.h`` et le résultat après pré-processing est le suivant :

.. code-block:: console

    $ gcc -E main.c | sed '/^#/ d'
    typedef struct Bar {
    int b, a, r;
    } Bar;

    extern void foo(Bar);
    typedef struct Bar {
    int b, a, r;
    } Bar;
    int main() {
    Bar bar = {0};
    foo(bar);
    }

On y retrouve la définition de ``Bar`` deux fois et donc, le compilateur génère une erreur.

Une solution à ce problème est d'ajouter des gardes d'inclusion multiple par exemple avec ceci:

.. code-block:: c

    #ifndef BAR_H
    #define BAR_H

    typedef struct Bar {
    int b, a, r;
    } Bar;

    #endif // BAR_H

Si aucune définition du type ``#define BAR_H`` n'existe, alors le fichier ``bar.h`` n'a jamais été inclus auparavant et le contenu de la directive ``#ifndef BAR_H`` dans lequel on commence par définir ``BAR_H`` est exécuté. Lors d'une future inclusion de ``bar.h``, la valeur de ``BAR_H`` aura déjà été définie et le contenu de la directive ``#ifndef BAR_H`` ne sera jamais exécuté.

Alternativement, il existe une solution **non standard** mais supportée par la plupart des compilateurs. Elle fait intervenir un pragma :

.. code-block:: c

    #pragma once

    typedef struct Bar {
    int b, a, r;
    } Bar;

Cette solution est équivalente à la méthode traditionnelle et présente plusieurs avantages. C'est tout d'abord une solution atomique qui ne nécessite pas un ``#endif`` à la fin du fichier. Il n'y a ensuite pas de conflit avec la règle SSOT car le nom du fichier ``bar.h`` n'apparaît pas dans le fichier ``BAR_H``.

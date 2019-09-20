
==================
Assemblage différé
==================

Translation unit
================

En programmation, on appelle *translation unit* (unité de traduction), un code qui peut être **compilé** en un **objet** sans autre dépendance externe. Le plus souvent, une unité de traduction correspond à un fichier C.

Diviser pour mieux régner
=========================

De même qu'un magasine illustré est divisé en sections pour accroître la lisibilité (sport, news, annonces, météo) de même un code source est organisé en éléments fonctionnels le plus souvent séparés en plusieurs fichiers.

Rappelons-le:

- Une fonction ne devrait pas dépasser un écran de haut (~50 lignes)
- Un fichier ne devrait pas dépasser 1000 lignes
- Une ligne ne devrait pas dépasser 80 caractères

Donc à un moment, il va falloir divisier et créer plusieurs fichiers.

Lorsque le programme commence à être volumineux, sa lecture, sa
compréhension et sa mise au point deviennent délicates. Il peut être alors
intéressant de le découper en plusieurs fichiers. Si on prend par
exemple un programme qui effectue des calculs sur des nombres complexes,
on peut imaginer le découpage suivant :

-  un fichier principal qui contient la partie applicative ``main.c``

-  un ensemble de fichiers (module) qui contient la partie dédiée à la
   gestion des nombres complexes :

   -  un fichier contenant la définition du module ``complex.h``

   -  un fichier contenant le code source C du module ``complex.c``

Le fichier ``main.c`` devra inclure le fichier ``complex.h`` afin de
pourvoir utiliser correctement les fonctions du module de gestion des
nombres complexes. Exemple :

.. code-block:: c

    // fichier main.c
    #include <stdio.h>
    #include "complex.h"


    int main(void) {

      sComplex c1={1.,-3.};  // c1=1-3j

      complexDisplay(c1); // affiche le nombre complexe c1

      return 0;
    }

.. code-block:: c

    // fichier complex.h

    #ifndef _COMPLEX_H_
    #define _COMPLEX_H_

    #include <math.h>

    typedef struct {

      double real;  // real part
      double img;   // imaginary part

    } sComplex, *pComplex;

    void complexDisplay(const sComplex c);

    #endif //  _COMPLEX_H_

.. code-block:: c

    // fichier complex.c

    #include "complex.h"

    void complexDisplay(const sComplex c) {

      printf("%+.3lf + %+.3lf\n",c.real, c.img);
      return;
    }

    #endif //  _COMPLEX_H_

Un des avantages majeurs à la création de modules est qu'un module
logiciel peut être réutilisé pour d'autres applications. Plus besoin de
réinventer la roue pour chaque application !

Module logiciel
---------------

Définition
~~~~~~~~~~

La notion de module logiciel fait référence à un découpage logique et
fonctionnel du programme à écrire. En règle générale, on rassemble dans
un module les fonctions, structures, symboles…qui sont cohérents entre
elles (voir l'exemple précédent pour les nombres complexes). Un module
logiciel prend la forme de deux fichiers (au moins) :

1. un fichier .h (*header*) contenant :

   -  une protection contre les inclusions multiples

   -  l'inclusion des fichiers .h système nécessaires
      (``#include <...>``)

   -  l'inclusion des fichiers .h utilisateur nécessaire
      (``#include ...``)

   -  les symboles du préprocesseur (``#define``)

   -  les types énumérés (``typedef enum``)

   -  les structures (``typedef struct``)

   -  les prototypes des fonctions du module

   -  les variables du module visibles à l'extérieur de celui-ci
      (``extern``)

2. un fichier .c (*code C*) contenant :

   -  l'inclusion du fichiers .h du module (``#include ...``)

   -  les variables globales au module visibles à l'extérieur de
      celui-ci

   -  l'implémentation des fonctions du module

Variables globales d'un module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visibilité des variables globales d'un module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les variables globales à un modules peuvent être :

-  globale au module mais visible uniquement dans le module

-  globale au module mais visible également à l'extérieur du module

Variable globale visible uniquement dans le module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On utilisera le préfixe ``static`` pour toute déclaration de variable
globale dans le module que l'on ne veut pas partager à l'extérieur de
celui.ci.

.. code-block:: c

    static uint32_t moduleCounter=0;

L'avantage de créer des variables statiques est que si un autre module
comporte des variables avec les mêmes identificateurs, il n'y aura pas
d'erreur lors de la phase d'édition des liens (pour peu qu'elles soients
``static`` également…).

Variable globale visible à l'extérieur du module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La variable doit être créée dans le fichier .c du module.

.. code-block:: c

    uint32_t moduleStatus=0;

La variable doit être déclarée comme ``extern`` dans le fichier .h du
module.

.. code-block:: c

    extern uint32_t moduleStatus;

Dès lors qu'un autre fichier source C inclus le fichier .h référençant
des variables externes, on peut accéder à ces variables (lecture et
écriture).

Gardes d'en-têtes
-----------------

Souvent nommé *header guards*, il s'agit d'une structure pré-processeur évitant la réinclusion d'un en-tête déjà inclus.

Il existe deux stratégie. La première normalisée par le standard utilise la forme suivante:

.. code-block:: c

    #ifndef IMAGE_PROCESSING_H
    #define IMAGE_PROCESSING_H

    /* ... */

    #endif // IMAGE_PROCESSING_H

La seconde plus simple, n'est pas couverte par le standard mais largement utilisée et supportée par la plupart des compliateurs:

.. code-block:: c

    #pragma once

    /* ... */

La seconde méthode permet de s'affranchir de plusieurs problèmes:

1. Il n'y a plus de répétition du nom du fichier dans le fichier.
  - Cela évite d'éventuelles collisions de noms.
  - Cela évite d'oublier de renommer le garde si le fichier est renommé.

2. Il n'y a plus de ``#endif`` terminal (que certains oublient parfois)

Compilation de l'application
----------------------------

La compilation séparée implique la séparation de la compilation en deux phases distinctes:

1. Compilation indépendante de chacune des unités de traduction générant des fichiers objets.
2. Édition des liens consistant en l'assembla des différents objets.

Nous avons vu qu'avec ``gcc`` la compilation est réduite à une seule commande:

.. code-block:: console

    gcc $CFLAGS -o executable source.c $LFLAGS

Or, il est aussi possible de découper cette procédure en deux étapes:

1. Compilation des objets

    .. code-block:: console

        cc $CFLAGS -c -o source.o source.c

2. Édition des liens

    .. code-block:: console

        cc $LFLAGS -o executable source.o

Avec la compilation séparée, il est désormais possible d'avoir plusieurs objets:

.. code-block:: console

    export CFLAGS=-std=c99 -O2 -Wall
    export LFLAGS=-lm
    cc $CFLAGS -c foo.c
    cc $CFLAGS -c bar.c
    cc $LFLAGS foo.o bar.o -o executable

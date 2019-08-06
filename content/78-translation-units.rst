
==================
Assemblage différé
==================

Translation unit
================

En programmation, on appelle *translation unit* (unité de traduction), un code qui peut être **compilé** en un **objet** sans autres dépendance externes. Le plus souvent, une unité de traduction correspond à un fichier C.

Diviser pour mieux régner
=========================

De même qu'un magasine illustré est divisé en sections pour accroître la lisibilité (sport, news, annonces, météo) de même un code source est organisé en éléments fonctionnels le plus souvent séparés en plusieurs fichiers.

Rappelons-le:

- Une fonction ne devrait pas dépasser un écran de haut (~50 lignes)
- Un fichier ne devrait pas dépasser 1000 lignes
- Une ligne ne devrait pas dépasser 80 caractères

Donc à un moment, il va falloir divisier et créer plusieurs fichiers.

Lorsque le programme commence à être volumineux, sa lecture, sa
compréhension et sa mise au point devient délicate. Il peut être alors
intéressant de le découper en plusieurs fichiers. Si on prend par
exemple un programme qui effectue des calculs sur des nombres complexes,
on peut imaginer le découpage suivant :

-  un fichier principale qui contient la partie applicative ``main.c``

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
un module les fonctions, structures, symboles…qui sont cohérentes entre
elles (voir l'exemple précédent pour les nombres complexes). Un module
logiciel prend la forme de deux fichiers (au moins) :

1. un fichier .h (*header*) contenant :

   -  une protection contre les inclusions multiples

   -  l'inclusion des fichiers .h système nécessaires
      (``#include <...>``)

   -  l'inclusion des fichiers .h utilisateur nécessaires
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

Variable globale visible à l'extérieur du le module
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

Protection contre les multiples inclusions
------------------------------------------

Dès lors qu'on utilise des modules logiciels, il devient impératifs de
contrôler que lors de l'inclusion de fichiers d'entêtes (.h) on ne va
pas se retrouver devant des erreurs de définitions multiples lorsqu'on
compile l'application finale. Pour cela, on protège le contenu du
fichier d'entête par les directives ``#ifndef SYMBOLE`` /
``#define SYMBOLE`` / ``#endif``. Le nom du symbole est en général une
image du nom du fichier d'entête. Si le fichier est nommé ``complex.h``,
le symbole sera nommé ``_COMPLEX_H_``. Cela donne le modèle d'entête
suivant :

.. code-block:: c

    // fichier imageProcessing.h

    #ifndef _IMAGE_PROCESSING_H_
    #define _IMAGE_PROCESSING_H_

    // system includes
    #include <math.h>

    // user includes
    #include "pixel.h"

    // preprocessor symbols
    #define MAX(a,b) ( (a)>(b) ? (a):(b))

    // enumerated types
    typedef enum {

      E_BLACK=0,
      E_WHITE,
      E_RED,
      E_GREEN,
      E_BLUE

    } eColor;

    // structured types
    typedef struct {

      uint8_t *buffer;
      uint32_t imgWidth;
      uint32_t imgHeight;

    } sImage, *pImage;

    // prototypes
    void displayImage(pImage _image);

    // external variables
    extern uint32_t imageCounter;

    #endif //  _IMAGE_PROCESSING_H_

Compilation de l'application
----------------------------

Lorsqu'on utilise des modules logiciels, chacun d'eux doit être compilé
pour généré le fichier object correspondant. Les fichiers objets doivent
alors être ajouté à la liste des fichiers pour la génération de
l'exécutable final.

Compilation d'un fichier .c
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La commande suivante permet de générer le fichier objet (.o) pour un
module (ex : ``module.c``) :

.. code-block:: c

    > gcc -c module.c

Le résultat de cette commande est la création d'un fichier ``module.o``
qui est le module compilé.

La commande suivante permet de générer le fichier objet (.o) pour le
programme principal (ex : ``main.c``) :

.. code-block:: c

    > gcc -c main.c

Le résultat de cette commande est la création d'un fichier ``main.o``
qui est le programme principal compilé (mais pas l'exécutable).

Edition des liens pour générer l'exécutable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: c

    > gcc -o application main.o module.o

Le résultat de cette commande est la création d'un fichier
``application`` qui est l'exécutable proprement dit.

====================
Portée et visibilité
====================

Ce chapitre se concentre sur trois caractéristiques d'une variable:

- La portée
- La visibilité
- La durée de vie

Dans les trois cas, elles décrivent l'accessibilité, c'est à dire jusqu'à ou/et jusqu'à quand une variable est accessible.

.. figure:: ../assets/images/visibility.*

    Brouillard matinal sur le `Golden Gate Bridge <https://fr.wikipedia.org/wiki/Golden_Gate_Bridge>`__, San Francisco.

Espace de nommage
=================

L'espace de nommage ou ``namespace`` est un concept différent de celui existant dans d'autres langages tel que C++. Le standard **C99** décrit 4 types possibles pour un identifiant:

- fonction et *labels*
- noms de structures (``struct``), d'unions (``union``), d'énumération (``enum``),
- identifiants

Portée
======

La portée ou `scope <https://en.wikipedia.org/wiki/Scope_(computer_science)>`__ décrit jusqu'à où une variable est accessible.

Une variable est **globale**, c'est-à-dire accessible partout, si elle est déclarée en dehors d'une fonction:

.. code-block:: c

    int global_variable = 23;

Une variable est **locale** si elle est déclarée à l'intérieur d'un bloc, ou à l'intérieur d'une fonction. Elle sera ainsi visible de sa déclaration jusqu'à la fin du bloc courant:

.. code-block:: c

    int main(int)
    {
        {
            int i = 12;

            i += 2; // Valide
        }

        i++; // Invalide, `i` n'est plus visible.
    }

Variable shadowing
------------------

On dit qu'une variable est *shadowed* ou *masquée* si sa déclaration masque une variable préalablement déclarée:

.. code-block:: c

    int i = 23;

    for(size_t i = 0; i < 10; i++) {
        printf("%ld", i); // Accès à `i` courant et non à `i = 23`
    }

    printf("%d", i); // Accès à `i = 23`

Visibilité
==========

Visibilité et durée de vie
--------------------------

Selon l'endroit où sont déclarées les variables, leur visibilité depuis
les blocs d'instructions est particulière. On distingue les variables
locales, globales à un module (ou fichier) et globales à l'application.
La visibilité d'une variable correspond à la portion de code où la
variable est réellement utilisable. La durée de vie d'une variable
correspond à sa période d'existence lors de l'exécution du programme.

Variables locales
~~~~~~~~~~~~~~~~~

Ces variables sont simplement déclarées dans un bloc d'instructions.
Leur portée (ou visibilité) est réduite aux limites du bloc
d'instruction. Ainsi elles sont utilisables dans le bloc et invisibles
hors du bloc.

.. code-block:: c

    int fonction() {

      // variable locale à la fonction
      // initialisée à chaque appel de la fonction
      int var_locale=0;

      // code....

      // fin
      return 0;

    }

Variables globales à un module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ces variables sont déclarées à l'extérieur de tout bloc et donc visibles
dans toute fonction lui appartenant.

Pour contraindre la visibilité des variables au module (ou fichier), on
placera devant le type de ces données le mot-clé *static*.

.. code-block:: c

    // Module application.c

    // variable uniquement globale au module
    static int var_glob_modul=0;

    int fonction() {

      // code pouvant utiliser var_glob_modul

      // fin
      return 0;

    }

Variables globales à l'application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ces variables sont déclarées à l'extérieur de tout bloc et donc visibles
dans toute fonction lui appartenant. N'étant pas déclarées comme
*static*, on peut les atteindre (les lire et les modifier) depuis toute
l'application. Afin de les atteindre, on ajoutera pour chaque module
devant les utiliser, le préfix *extern*.

.. code-block:: c

    // Module main.c

    // variable globale au module
    int var_glob_appli=0;


    int main() {

      // code pouvant utiliser var_glob_appli
      ...
      // fin
      return 0;

    }

    // Module calcul.c

    // visibilité sur une variable globale externe au module
    extern int var_glob_appli;


    int fonction() {

      // code pouvant utiliser var_glob_appli
      ...
      // fin
      return 0;

    }

Classes
-------

L'attribut définissant la classe d'une variable doit précéder le type de
la variable. Il est optionnel.

Variables de classe auto
~~~~~~~~~~~~~~~~~~~~~~~~

La classe *auto* est celle utilisée par défaut lorsqu'aucune classe
n'est précisée. Les variables automatiques sont visibles uniquement dans
le bloc où elles sont déclarées. Ces variables sont créées sur la pile
mémoire (stack en anglais).

.. code-block:: c

    auto type identificateur = valeur_initiale;

Pour les variables automatiques, le mot-clé *auto* n'est pas
obligatoire.

Variables de classe statique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La classe *static* permet de déclarer des variables dont le contenu est
préservé même lorsque l'on sort du bloc où elles ont été déclarées.
Elles ne sont initialisées qu'une seule fois.

.. code-block:: c

    static type identificateur = valeur_initiale;

Utilisation dans une fonction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les variables de classe *static* déclarées dans une fonction sont
initialisées au premier appel de cette fonction. Si on sort de la
fonction, le contenu de cette variable est préservé et lorsque l'on
rentre à nouveau dedans, cette variable n'est pas réinitialisée, mais a
conservé sa valeur précédente. On peut qualifier ce comportement d'effet
mémoire.

Utilisation dans un module ou fichier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Les variables de classe *static* déclarées dans un module sont
initialisées lors du démarrage de l'application et sont visibles dans
toutes les fonctions présentes dans le module.

En dehors de ce module, il n'est pas possible d'y accéder, même en
indiquant une référence externe à ce genre de variable.

Variables de classe volatile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La classe *volatile* permet d'indiquer au compilateur que la variable de
cette classe ne doit pas être stockée dans un registre.

.. code-block:: c

    volatile type identificateur = valeur_initiale;

Une application simple est l'utilisation d'une variable liée à un
périphérique. Ce dernier est à même de modifier le contenu de cette
variable sans préavis (lors d'un évènement). Le programme doit toujours
accéder à l'espace mémoire de la variable pour donner la 'vraie'
information à chaque utilisation.

====================
Portée et visibilité
====================

Ce chapitre se concentre sur quatre caractéristiques d'une variable :

- La portée
- La visibilité
- La durée de vie
- Son qualificatif de type

Dans les quatre cas, elles décrivent l'accessibilité, c'est à dire jusqu'à ou/et jusqu'à quand une variable est accessible, et de quelle manière

.. figure:: ../assets/images/visibility.*

    Brouillard matinal sur le `Golden Gate Bridge <https://fr.wikipedia.org/wiki/Golden_Gate_Bridge>`__, San Francisco.

Espace de nommage
=================

L'espace de nommage ou ``namespace`` est un concept différent de celui existant dans d'autres langages tel que C++. Le standard **C99** décrit 4 types possibles pour un identifiant :

- fonction et *labels*
- noms de structures (``struct``), d'unions (``union``), d'énumération (``enum``),
- identifiants

Portée
======

La portée ou `scope <https://en.wikipedia.org/wiki/Scope_(computer_science)>`__ décrit jusqu'à où une variable est accessible.

Une variable est **globale**, c'est-à-dire accessible partout, si elle est déclarée en dehors d'une fonction :

.. code-block:: c

    int global_variable = 23;

Une variable est **locale** si elle est déclarée à l'intérieur d'un bloc, ou à l'intérieur d'une fonction. Elle sera ainsi visible de sa déclaration jusqu'à la fin du bloc courant :

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

On dit qu'une variable est *shadowed* ou *masquée* si sa déclaration masque une variable préalablement déclarée :

.. code-block:: c

    int i = 23;

    for(size_t i = 0; i < 10; i++) {
        printf("%ld", i); // Accès à `i` courant et non à `i = 23`
    }

    printf("%d", i); // Accès à `i = 23`

Visibilité
==========

Selon l'endoit où est déclaré une variable, elle ne sera pas nécessairement visible partout ailleurs. Une variable **locale** n'est accessible qu'à partir de sa déclaration et jusqu'à la fin du bloc dans laquelle elle est déclarée.

L'exemple suivant montre la visibilité de plusieurs variables :

.. code-block:: text

                      //   a
    void foo(int a) { //   ┬ b
        int b;        //   │ ┬
        ...           //   │ │
        {             //   │ │ c
           int c;     //   │ │ ┬
           ...        //   │ │ │ d
           int d;     //   │ │ │ ┬
           ...        //   │ │ │ │
        }             //   │ │ ┴ ┴
        ...           //   │ │
    }                 //   ┴ ┴

Une variable déclarée globalement, c'est à dire en dehors d'une fonction à une durée de vie sur l'entier du module (*translation unit*) quelque soit l'endroit ou elle est déclarée, en revanche elle n'est visible que depuis l'endroit ou elle est déclarée. Les deux variables ``i`` et ``j`` sont globales au module, c'est à dire qu'elle peuvent être accédées depuis n'importe quelle fonction contenu dans ce module.

En revanche la variable ``j``, bien qu'elle ait ait une durée de vie sur toute l'exécution du programme et que sa portée est globale, elle ne pourra être accédée depuis ``main`` car elle n'est pas visible.

.. code-block:: text

    #include <stdio.h>
                                 //  i
    int i;                       //  ┬
                                 //  │
    int main() {                 //  │
        printf("%d %d\n", i, j); //  │
    }                            //  │
                                 //  │ j
    int j;                       //  ┴ ┬

Le mot clé ``extern`` permet non pas de déclarer la variable ``j`` mais de renseigner le compilateur qu'il existe *ailleurs* une variable ``j``. C'est ce que l'on appelle une déclaration avancée ou *forward-declaration*. Dans ce cas, bien que ``j`` soit déclaré après la fonction principale, elle est maintenant visible.

.. code-block:: c

    #include <stdio.h>

                            // j
    extern int j;           // ┬   Déclaration en amont de `j`
                            // │
    int main() {            // │
        printf("%d\n", j);  // │
    }                       // │
                            // │
    int j;                  // │
                            // │

Une particularité en C est que tout symbol global (variable ou fonction) ont une accessibilité transversale. C'est à dire que dans le cas de la compilation séparée, une variable déclarée dans un fichier, peut être accédée depuis un autre fichier, il en va de même pour les fonctions.

L'exemple suivant implique deux fichiers ``foo.c`` et ``main.c``. Dans l'un deux symbols sont déclarés, une variable et une fonction.

.. code-block:: c

     // foo.c

     int foo;

     void do_foo() {
         printf("Foo does...");
     }

Depuis le programme principal, il est possible d'accéder à symboles à condition de renseigner sur le prototype de la fonction et l'existence de la variable :

.. code-block:: c

     // main.c

     extern int foo;
     extern void do_foo(); // Non obligatoire

     int main() {
         foo();
     }

Dans le cas ou l'on voudrait restreindre l'accessibilité d'une variable au module dans lequel elle est déclarée, l'usage du mot clé ``static`` s'impose.

En écrivant ``static int foo;`` dans ``foo.c``, la variable n'est plus accessible en dehors du module même avec une déclaration en avance. On dit que sa portée est réduite au module.

Qualificatif de type
====================

Les variables en C peuvent être crées de différentes manières. Selon la manière dont elle pourront être utilisées, il est courant de les classer en catégories.

Une classe de stockage peut être implicite à une déclaration de variable ou explicite, en ajoutant un attribut devant la déclaration de celle-ci.

``auto``
--------

.. index:: auto

Cette classe est utilisée par défaut lorsqu'aucune autre classe
n'est précisée. Les variables automatiques sont visibles uniquement dans
le bloc où elles sont déclarées. Ces variables sont habituellement créées sur la pile (*stack*) mais peuvent être aussi stockées dans les registres du processeur. C'est un choix qui incombe au compilateur.

.. code-block:: c

    auto type identificateur = valeur_initiale;

Pour les variables automatiques, le mot-clé *auto* n'est pas
obligatoire, et n'est pas recommandé en **C99** car son utilisation est implicite.

``register``
------------

.. index:: classe de stockage; register, register

Ce mot clé incite le compilateur à utiliser un registre processeur pour stocker la variable. Ceci permet de gagner en temps d'exécution car la variable n'a pas besoin d'être chargée depuis et écrite vers la mémoire.

Jadis, ce mot clé était utilisé devant toutes les variables d'itérations de boucles. La traditionnelle variable ``i`` utilisée dans les boucles ``for`` était déclarées ``register int i = 0;``. Les compilateurs modernes savent aujourd'hui identifier les variables les plus souvent utilisées. L'usage de ce mot clé n'est donc plus recommandé depuis **C99**.

``const``
---------

.. index:: classe de stockage; const, const

Ce mot clé rends une déclaration non modifiable par le programme lui même. Néanmoins il ne s'agit pas de constantes au sens strict du terme car une variable de type ``const`` pourrait très bien être modifiée par erreur en jardinant la mémoire. Quand ce mot clé est appliqué à une structure, aucun des champs de la structure n'est accessible en écriture. Bien qu'il puisse paraître étrange de vouloir rendre « constante » une « variable », ce mot clé a une utilité. En particulier, il permet de faire du code plus sûr.

``static``
----------

.. index:: classe de stockage; static, static

Elle permet de déclarer des variables dont le contenu est
préservé même lorsque l'on sort du bloc où elles ont été déclarées.

Elles ne sont donc initialisées qu'une seule fois. L'exemple suivant est une fonction qui retourne à chaque fois une valeur différente, incrémentée de 1. La variable ``i`` agit ici comme une variable globale, elle n'est initialisée qu'une seule fois à 0 et donc s'incrémente d'appel en appel. En revanche, elle n'est pas accessible en dehors de la fonction; c'est donc une variable locale.

.. code-block:: c

    int iterate() {
        static int i = 0;
        return i++;
    }

Il n'est pas rare de voir des variables globales, ou des fonctions précédées du mot clé ``static``. Ces variables sont dites *statiques au module*. Elle ne sont donc pas accessibles depuis un autre module (*translation unit*)

La fonction suivante est *statique* au module dans lequel elle est déclarée. Il ne sera donc pas possible d'y accéder depuis un autre fichier C.

.. code-block:: c

    static int add(int a, int b) { return a + b; }

``volatile``
------------

.. index:: classe de stockage; volatile, volatile

Cette classe de stockage indique au compilateur qu'il ne peut faire aucune hypothèse d'optimisation concernant cette variable. Elle indique que son contenu peut être modifié en tout temps en arrière plan par le système d'exploitation ou le matériel. Ce mot clé est davantage utilisé en programmation système, ou sur microcontrôleurs.

L'usage de cette classe de stockage réduit les performances d'un programme puisque qu'elle empêche l'optimisation du code et le contenu de cette variable devra être rechargé à chaque utilisation

``extern``
----------

.. index:: classe de stockage; extern, extern

Cette classe est utilisée pour signaler que la variable ou la fonction associée est déclarée dans un autre module (autre fichier). Ainsi le code suivant ne déclare pas une nouvelle variable ``foo`` mais s'attends à ce que cette variable ait été déclarée dans un autre fichier.

.. code-block:: c

    extern int foo;

``restrict``
------------

.. index:: classe de stockage; restrict, restrict

En C, le mot clé ``restrict``, apparu avec **C99**, es utililsé uniquement pour des pointeurs. Ce qualificatif de type informe le compilateur que pour toute la durée de vie du pointeur, aucun autre pointeur ne pointera que sur la valeur qu'il pointe ou une valeur dérivée de lui même (p. ex: ``p + 1``).

En d'autres termes, le qualificatif indique au compilateur que deux pointeurs différents ne peuvent pas pointer sur les même régions mémoire.

Prenons l'exemple simple d'une fonction qui met à jour deux pointeurs avec une valeur passée en paramètre :

.. code-block:: c

    void update_ptr(size_t *a, size_t *b, const size_t *value) {
        *a += *value;
        *b += *value;
    }

Le compilateur, n'ayant aucune information sur les pointeurs fournis, ne peut faire aucune hypothèse d'optimisation. En effet, ces deux pointeurs ``a`` et ``b`` ainsi que ``value`` pourraient très bien pointer sur la même région mémoire, et dans ce cas ``*a += *value`` aurait pour effet d'incrémenter ``value``. En revanche, dans le cas ou la fonction est déclarée de la façon suivante :

.. code-block:: c

    void update_ptr(size_t *restrict a, size_t * restrict b, const size_t *restrict value) {
        *a += *value;
        *b += *value;
    }

le compilateur est informé qu'il peut faire l'hypothèse que les trois pointeurs fournis en paramètres sont indépendant les uns des autres. Dans ce cas il peut optimiser le code. Voir `restrict <https://en.wikipedia.org/wiki/Restrict>`__ sur Wikipedia pour plus de détails.

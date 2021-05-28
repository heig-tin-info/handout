.. _algorithms:

=========================
Algorithmes et conception
=========================

L'algorithmique est le domaine scientifique qui étudie les algorithmes, une suite finie et non ambiguë d'opérations ou d'instructions permettant de résoudre un problème ou de traiter des données.

Un algorithme peut être également considéré comme étant n'importe quelle séquence d'opérations pouvant être simulées par un système `Turing-complet <https://fr.wikipedia.org/wiki/Turing-complet>`__. Un système est déclaré Turing-complet s'il peut simuler n'importe quelle `machine de Turing <https://fr.wikipedia.org/wiki/Machine_de_Turing>`__. For heureusement, le langage C est Turing-complet puisqu'il possède tous les ingrédients nécessaires à la simulation de ces machines, soit compter, comparer, lire, écrire...

Dans le cas qui concerne cet ouvrage, un algorithme est une recette exprimée en une liste d'instructions et permettant de résoudre un problème informatique. Cette recette contient à peu de choses près les éléments programmatiques que nous avons déjà entre aperçus: des structures de contrôle, des variables, etc.

Généralement un algorithme peut être exprimé graphiquement en utilisant un organigramme (*flowchart*) ou un structogramme (*Nassi-Shneiderman diagram*) afin de s'affranchir du langage de programmation cible.

La **conception** aussi appelée `Architecture logicielle <https://fr.wikipedia.org/wiki/Architecture_logicielle>`__ est l'art de penser un programme avant son implémentation. La phase de conception fait bien souvent appel à des algorithmes.

Pour être qualifiées d'algorithmes, certaines propriétés doivent être respectées :

#. **Entrées**, un algorithme doit posséder 0 ou plus d'entrées en provenance de l'extérieur de l'algorithme.
#. **Sorties**, un algorithme doit posséder au moins une sortie.
#. **Rigueur**, chaque étape d'un algorithme doit être claire et bien définie.
#. **Finitude**, un algorithme doit comporter un nombre fini d'étapes.
#. **Répétable**, un algorithme doit fournir un résultat répétable.

Complexité d'un algorithme
==========================

Il est souvent utile de savoir quelle est la complexité d'un algorithme afin de le comparer à un autre algorithme équivalent. Il existe deux indicateurs :

- La complexité en temps
- La complexité en mémoire

Pour l'un, l'idée est de savoir combine de temps CPU consomme un algorithme. Pour l'autre, on s'intéresse à l'utilisation de mémoire tampon.

La complexité en temps et en mémoire d'un algorithme est souvent exprimée en utilisant la notation en O (*big O notation*). Par exemple, la complexité en temps d'un algorithme qui demanderait 10 étapes pour être résolu s'écrirait :

.. math::
    O(10)

Un algorithme qui ferait une recherche dichotomique sur un tableau de :math:`n` éléments à une complexité :math:`O(log(n))`.

Quelques points à retenir :

- La complexité d'un algorithme considère toujours le cas le moins favorable.
- Le meilleur algorithme est celui qui présente le meilleur compromis entre sa complexité en temps et sa complexité en mémoire.

À titre d'exemple, le programme suivant qui se charge de remplacer les valeurs paires d'un tableau par un 0 et les valeurs impaires par un 1 à une complexité en temps de :math:`O(n)` où ``n`` est le
nombre d'éléments du tableau.

.. code-block:: c

    void discriminate(int* array, size_t length)
    {
        for (size_t i = 0; i < length; i++)
        {
            array[i] %= 2;
        }
    }

D'une manière générale, la plupart des algorithmes que l'ingénieur écrira appartiendront à ces
catégories exprimées du meilleur au plus mauvais :

.. table:: Temps pour différentes complexités d'algorithmes

    +----------------------+--------------------+----------------------------------------+
    | Complexité           | :math:`n = 100000` | i7 (100'000 MIPS)                      |
    +======================+====================+========================================+
    | :math:`O(log(n))`    |              11    | 0.11 ns                                |
    +----------------------+--------------------+----------------------------------------+
    | :math:`O(n)`         |         100'000    | 1 us                                   |
    +----------------------+--------------------+----------------------------------------+
    | :math:`O(n log(n))`  |       1'100'000    | 11 us                                  |
    +----------------------+--------------------+----------------------------------------+
    | :math:`O(n^2)`       |  10'000'000'000    | 100 ms (un battement de cil)           |
    +----------------------+--------------------+----------------------------------------+
    | :math:`O(2^n)`       | très très grand    | Le soleil devenu géante rouge          |
    |                      |                    | aura ingurgité la terre                |
    +----------------------+--------------------+----------------------------------------+
    | :math:`O(n!)`        | trop trop grand    | La galaxie ne sera plus que poussière  |
    +----------------------+--------------------+----------------------------------------+

Les différentes complexités peuvent être résumées sur la figure suivante :

.. figure:: ../../assets/images/complexity.*

    Différentes complexités d'algorithmes


Un algorithme en :math:`O(n^2)`, doit éveiller chez le développeur la volonté de voir s'il n'y a pas moyen d'optimiser l'algorithme en réduisant sa complexité, souvent on s'aperçoit qu'un algorithme peut être optimisé et s'intéresser à sa complexité est un excellent point d'entrée.

Attention toutefois à ne pas mal évaluer la complexité d'un algorithme. Voyons par exemple les deux algorithmes suivants :

.. code-block:: c

  int min = MAX_INT;
  int max = MIN_INT;

  for (size_t i = 0; i < sizeof(array) / sizeof(array[0]); i++) {
      if (array[i] < min) {
          min = array[i];
      }
      if (array[i] > min) {
          max = array[i];
      }
  }

.. code-block:: c

  int min = MAX_INT;
  int max = MIN_INT;

  for (size_t i = 0; i < sizeof(array) / sizeof(array[0]); i++)
  {
      if (array[i] < min) {
          min = array[i];
      }
  }

  for (size_t i = 0; i < sizeof(array) / sizeof(array[0]); i++)
  {
      if (array[i] > min) {
          max = array[i];
      }
  }

.. exercise:: Triangle évanescent

    Quel serait l'algorithme permettant d'afficher :

    .. code-block::text

        *****
        ****
        ***
        **
        *

    et dont la taille peut varier ?

.. exercise:: L'entier manquant

    On vous donne un gros fichier de 3'000'000'000 entiers positifs 32-bits, il vous faut générer un entier qui n'est pas dans la liste. Le hic, c'est que vous n'avez que 500 MiB de mémoire de travail. Quel algorithme proposez-vous ?

    Une fois le travail terminé, votre manager vient vous voir pour vous annoncer que le cahier des charges a été modifié. Le client dit qu'il n'a que 10 MiB. Pensez-vous pouvoir résoudre le problème quand même ?

Machines d'états
================

Diagrammes visuels
==================

- Diagrammes en flux
- Structogrammes
- Diagramme d'activités

Récursivité
===========

La `récursivité <https://fr.wikipedia.org/wiki/R%C3%A9cursivit%C3%A9>`__ est une autoréférence. Il peut s'agit en C d'une fonction qui s'appelle elle-même.

.. exercise:: La plus petite différence

    Soit deux tableaux d'entiers, trouver la paire de valeurs (une dans chaque tableau) ayant la plus petite différence (positive).

    Exemple :

    .. code-block:: text

        int a[] = {5, 3, 14, 11, 2};
        int b[] = {24, 128, 236, 20, 8};

        int diff = 3 // pair 11, 8

    #. Proposer une implémentation
    #. Quelle est la complexité de votre algorithme ?

Programmation dynamique
=======================

La programmation dynamique est une méthode algorithmique datant des années 1950, mais devenue populaire ces dernières années. Elle permet de coupler des algorithmes récursifs avec le concept de mémoïsation.

Prenons par exemple l'algorithme de Fibonacci récursif :

.. code-block:: c

    int fibonacci(int n) {
        if (n <= 1) return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

Le problème de cet algorithme est sa performance. Appeler ``fibonacci(50)`` demandera de calculer ``fibonacci(49)`` et ``fibonacci(48)`` mais pour calculer ``fibonacci(49)`` il faudra recalculer ``fibonacci(48)``. On voit qu'on effectue du travail à double. En réalité c'est bien pire que ça. La complexité est de :math:`O(2^n)`. Donc pour calculer la valeur ``50`` il faudra effectuer :math:`1 125 899 906 842 624` opérations. Avec un ordinateur capable de calculer 1 milliard d'opérations par seconde, il faudra tout de même plus d'un million de secondes. Cet algorithme est donc très mauvais !

En revanche, si l'on est capable de mémoriser dans une table les résultats précédents des appels de Fibonacci, les performances seront bien meilleures.

Voici l'algorithme modifié :

.. code-block:: c

    int fibonacci(int n) {
        static int memo[1000] = {0};
        if (memo[n]) return memo[n];
        if (n <= 1) return n;
        return memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
    }

Sa complexité est ainsi réduite à :math:`O(2\cdot n)` et donc :math:`O(n)`. En revanche, l'approche dynamique demande un espace mémoire supplémentaire. On n'a rien sans rien et l'éternel dilemme mémoire versus performance s'applique toujours.

Algorithmes de tris
===================

Heap Sort
---------

L'algorithme `Heap Sort <https://fr.wikipedia.org/wiki/Tri_par_tas>`__ aussi appelé "Tri par tas" est l'un des algorithmes de tri les plus performants offrant une complexité en temps de :math:`O(n\cdot log(n))` et une complexité en espace de :math:`O(1)`. Il s'appuie sur le concept d'arbre binaire.

Prenons l'exemple du tableau ci-dessous et deux règles suivantes :

- l'enfant de gauche est donné par ``2 * k + 1`` ;
- l'enfant de droite est donné par ``2 * k + 2``.

.. code-block:: text

      1   2       3                  4
    ┞──╀──┬──╀──┬──┬──┬──╀──┬──┬──┬──┬──┬──┬──┬──┦
    │08│04│12│20│06│42│14│11│03│35│07│09│11│50│16│
    └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
      0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  (indice)

La première valeur du tableau est appelée la racine *root*. C'est le premier élément de l'arbre. Puisqu'il s'agit d'un arbre binaire, chaque noeud peut comporter jusqu'à 2 enfants. L'enfant de gauche est calculé à partir de l'indice ``k`` de l'élément courant. Ainsi les deux enfants de l'élément ``4`` seront ``2 * 4 + 1 = 9`` et ``2 * 4 + 2 == a``.

Ce tableau linéaire en mémoire pourra être représenté visuellement comme un arbre binaire :

.. code-block:: text

                 8
                 |
             ----+----
           /           \
          4            12
       /    \        /    \
      20     6      42    14
     / \    / \    / \   /  \
    11  3  35  7  9  11 50  16

Le coeur de cet algorithme est le sous-algorithme nommé *heapify*. Ce dernier à pour objectif de satisfaire une exigence supplémentaire de notre arbre : **chaque enfant doit être plus petit que son parent**. Le principe est donc simple. On part du dernier élément de l'arbre qui possède au moins un enfant : la valeur ``14`` (indice ``6``). Le plus grand des enfants est échangé avec la valeur du parent. Ici ``50`` sera échangé avec ``14``. Ensuite on applique récursivement ce même algorithme pour tous les enfants qui ont été échangés. Comme ``14`` (anciennement ``50``) n'a pas d'enfant, on s'arrête là.

L'algorithme continue en remontant jusqu'à la racine de l'arbre. La valeur suivante analysée est donc ``42``, comme les deux enfants sont petits on continue avec la valeur ``6``. Cette fois-ci ``35`` qui est plus grand est alors échangé. Comme ``6`` n'a plus d'enfant, on continue avec ``20``, puis ``12``. À cette étape, notre arbre ressemble à ceci :

.. code-block:: text

                 8
                 |
             ----+----
           /           \
          4            12
       /    \        /    \
      20    35      42    50
     / \    / \    / \   /  \
    11  3  6   7  9  11 14  16

La valeur ``12`` est plus petite que ``50`` et est donc échangée. Mais puisque ``12`` contient deux enfants (``14`` et ``16``), l'algorithme continue. ``16`` est échangé avec ``12``. L'algorithme se poursuit avec ``4`` et se terminera avec la racine ``8``. Finalement l'arbre ressemblera à ceci :

.. code-block:: text

                35
                 |
             ----+----
           /           \
         20            50
       /    \        /    \
      11     7      42    16
     / \    / \    / \   /  \
    8   3  6   4  9  11 14  12

On peut observer que chaque noeud de l'arbre satisfait à l'exigence susmentionnée : tous les enfants sont inférieurs à leurs parents.

Une fois que cette propriété est respectée, on a l'assurance que la racine de l'arbre est maintenant le plus grand élément du tableau. Il est alors échangé avec le dernier élément du tableau ``12``, qui devient à son tour la racine.

Le dernier élément est sorti du tableau et notre arbre ressemble maintenant à ceci :

.. code-block:: text

    1   2       3                  4
    ┞──╀──┬──╀──┬──┬──┬──╀──┬──┬──┬──┬──┬──┬──┦──┦
    │12│20│50│11│ 7│42│16│ 8│ 3│ 6│ 4│ 9│11│14│35│
    └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
      0  1  2  3  4  5  6  7  8  9  a  b  c  d     (indice)

                12
                 |
             ----+----
           /           \
         20            50
       /    \        /    \
      11     7      42    16
     / \    / \    / \   /
    8   3  6   4  9  11 14

À ce moment on recommence :

1. ``heapify``
2. Échange du premier élément avec le dernier.
3. Sortie du dernier élément de l'arbre.
4. Retour à (1) jusqu'à ce que tous les éléments soient sortis de l'arbre.

Type d'algorithmes
==================

Algorithmes en ligne (incrémental)
----------------------------------

Un algorithme incrémental ou `online <https://fr.wikipedia.org/wiki/Algorithme_online>`__ est un algorithme qui peut s'exécuter sur un flux de données continu en entrée. C'est-à-dire qu'il est en mesure de prendre des décisions sans avoir besoin d'une visibilité complète sur le set de données.

Un exemple typique est le `problème de la secrétaire <https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_secr%C3%A9taire>`__. On souhaite recruter une nouvelle secrétaire et le recruteur voit défiler les candidats. Il doit décider à chaque entretien s'il engage ou non le candidat et ne peut pas attendre la fin du processus d'entretiens pour obtenir le score attribué à chaque candidat. Il ne peut comparer la performance de l'un qu'à celle de deux déjà entrevus. L'objectif est de trouver la meilleure stratégie.

La solution à ce problème est de laisser passer 37% des candidats sans les engager. Ceci correspond à une proportion de :math:`1/e`. Ensuite il suffit d'attendre un ou une candidate meilleure que tous ceux/celles du premier échantillon.

-----

.. exercise:: Intégrateur de Kahan

    L'intégrateur de Kahan (`Kahan summation algorithm <https://en.wikipedia.org/wiki/Kahan_summation_algorithm>`__) est une solution élégante pour pallier à la limite de résolution des types de données.

    L'algorithme pseudo-code peut être exprimé comme :

    .. code-block:: text

        function kahan_sum(input)
            var sum = 0.0
            var c = 0.0
            for i = 1 to input.length do
                var y = input[i] - c
                var t = sum + y
                c = (t - sum) - y
                sum = t
            next i
            return sum

    #. Implémenter cet algorithme en C compte tenu du prototype :

        .. code-block:: c

            float kahan_sum(float value, float sum, float c);

    #. Expliquer comment fonctionne cet algorithme.
    #. Donner un exemple montrant l'avantage de cet algorithme sur une simple somme.

.. exercise:: Robot aspirateur affamé

    Un robot aspirateur souhaite se rassasier et cherche le frigo, le problème c'est qu'il ne sait pas où il est. Elle serait la stratégie de recherche du robot pour se rendre à la cuisine ?

    Le robot dispose de plusieurs fonctionnalités :

    - Avancer
    - Tourner à droite de 90°
    - Détection de sa position absolue p. ex. ``P5``

    Élaborer un algorithme de recherche.

    .. code-block::

          │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │ K │ L │ M │ O │ P │ Q │
        ──┏━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
        1 ┃                     x ┃       ┃               ┃               ┃
        ──┃             F1: Frigo ┃       ┃               ┃               ┃
        2 ┃       ┃               ┃       ┃               ┃               ┃
        ──┃       ┃               ┃       ┃               ┃               ┃
        3 ┃       ┃               ┃       ┃               ┃               ┃
        ──┃       ┃               ┃       ┃               ┃               ┃
        4 ┃       ┃               ┃       ┃               ┃               ┃
        ──┃       ┃               ┃       ┃               ┃               ┃
        5 ┃       ┃               ┃       ┃               ┃      <--o     ┃
        ──┃       ┣━━━━━━━   ━━━━━┫       ┃               ┃     P5: Robot ┃
        6 ┃       ┃               ┃       ┃               ┃               ┃
        ──┃       ┃               ┃       ┃               ┃               ┃
        7 ┃                       ┃       ┃               ┃               ┃
        ──┃                       ┃       ┃               ┃               ┃
        8 ┃       ┃               ┃       ┃               ┃               ┃
        ──┣━━━━━━━┻━━━━━━━    ━━━━┛   ━━━━┛   ━━━━━━━━━━━━┛   ━━━━┳━━━━━━━┫
        9 ┃                                                       ┃       ┃
        ──┃                                                       ┃       ┃
        10┃                                                               ┃
        ──┃                                                               ┃
        11┃                                                       ┃       ┃
        ──┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━┛

=========================
Algorithmes et conception
=========================

L'algorithmie est le domaine scientifique qui étudie les algorithmes, une suite finie et non ambiguë d'opérations ou d'instructions permettant de résoudre un problème ou de traiter des données.

Un algorithme peut être également considéré comme étant n'importe quelle séquence d'opérations pouvant être simulée par un système `Turing-complet <https://fr.wikipedia.org/wiki/Turing-complet>`__. Un système est déclaré Turing-complet s'il peut simuler n'importe quelle `machine de Turing <https://fr.wikipedia.org/wiki/Machine_de_Turing>`__. Heureusement pour nous le langage C est Turing-complet puisqu'il possède tous les ingrédients nécessaires à la siumulation de ces machines (compter, comparer, lire, écrire, ...)

Dans le cas qui concerne cet ouvrage, un algorithme est une recette exprimée en une liste d'instructions et permettant de résoudre un problème infomratique. Cette recette contient à peu de choses prêt les éléments programmatiques que nous avons déjà entre aperçu: des structures de controles, des variables, etc.

Généralement un algorithme peut être exprimé graphiquement en utilisant un organigramme (*flowchart*) ou un structogramme (*Nassi-Shneiderman diagram*) afin de d'affranchir du langage de programmation cible.

La **conception** aussi appelée `Architecture logicielle <https://fr.wikipedia.org/wiki/Architecture_logicielle>`__ est l'art de penser un programme avant son implémentation. La phase de conception fait bien souvent appel à des algorithmes.

Complexité d'un algorithme
--------------------------

Il est souvent utile de savoir quelle est la complexité d'un algorithme afin de le comparer à un autre algorithme équivalent. Il existe deux indicateurs:

- La complexité en temps
- La complexité en mémoire

Pour l'un, l'idée est de savoir combine de temps CPU consomme un algorithme. Pour l'autre, on s'intéresse à l'utilisation de mémoire tampon.

La complexité en temps et en mémoire d'un algorithme est souvent exprimée en utilsant la notation en O (*big O notation*). Par exemple, la complexité en temps d'un algorithme qui demanderait 10 étapes pour être résolu s'écrirait:

.. math::
    O(10)

Un algorithme qui ferait une recherche dichotomique sur un tableau de :math:`n` éléments à une complexité :math:`O(log(n))`.

Quelques points à retenir:

- La complexité d'un algorithme considère toujours le cas le moins favorable.
- Le meilleur algorithme est celui qui présente le meilleur compromis entre sa complexité en temps et sa complexité en mémoire.

A titre d'exemple, le programme suivant qui se charge de remplacer les valeurs paires d'un tableau par un 0 et les valeurs impaires par un 1 à une complexité en temps de :math:`O(n)` où `n` est le
nombre d'éléments du tableau.

.. code-block:: c

    void discriminate(int* array, size_t length)
    {
        for (size_t i = 0; i < length; i++)
        {
            array[i] %= 2;
        }
    }

D'une manière générale, la plupart des algorithmes que l'ingénieur écrira appartiendra à ces
catégories expérimée du meilleur au plus mauvais:

+----------------------+--------------------+----------------------------------------+
| Complexité           | :math:`n = 100000` | i7 (100'000 MIPS)                      |
+======================+====================+========================================+
| :math:`O(log(n))`    |              11    | 0.11 ns                                |
+----------------------+--------------------+----------------------------------------+
| :math:`O(n)`         |         100'000    | 1 us                                   |
+----------------------+--------------------+----------------------------------------+
| :math:`O(n log(n))`  |       1'100'000    | 11 us                                  |
+----------------------+--------------------+----------------------------------------+
| :math:`O(n^2)`       |  10'000'000'000    | 100 ms (un batement de cil)            |
+----------------------+--------------------+----------------------------------------+
| :math:`O(2^n)`       | très très grand    | Le soleil devenue géante rouge         |
|                      |                    | aura ingurgité la terre                |
+----------------------+--------------------+----------------------------------------+
| :math:`O(n!)`        | trop trop grand    | La galaxie ne sera plus que poussière  |
+----------------------+--------------------+----------------------------------------+

Un algorithme en :math:`O(n^2)`, doit éveiller chez le développeur la volonté de voir s'il n'y a pas moyen d'optimiser l'algorithme en réduisant sa complexité, souvent on s'aperçoit qu'un algorithme peut être optimisé et s'intéresser à sa complexité est un excellent point d'entrée.

Attention toutefois à ne pas mal évaluer la complexité d'un algorithme. Voyons par exemple les deux algorithmes suivants:

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

Récursivité
===========

La `récursivité <https://fr.wikipedia.org/wiki/R%C3%A9cursivit%C3%A9>`__ est une auto-référence. Il peut s'agit en C d'une fonction qui s'appelle elle même.

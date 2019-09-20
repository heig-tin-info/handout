=====================
Structures récursives
=====================

Listes chaînées
===============

Une liste chaînée est une structure de données permettant de lier des éléments structurés entre eux. La liste est caractérisée par:

- un élément de tête (*head*),
- un élément de queue (*tail*).

Un élément est caractérisé par:

- un contenu (*payload*),
- une référence vers l'élément suivant et/ou précédent dans la liste.

Les listes chaînées réduisent la complexité liée à la manipulation d'éléments dans une liste. L'empreinte mémoire d'une liste chaînée est plus grande qu'avec un tableau, car à chaque élément de donnée est associé un pointeur vers l'élément suivant ou précédent.

Ce surcoût est souvent part du compromis entre la complexité d'exécution du code et la mémoire utilisée par ce programme.

+----------------------+----------------------------------------------------------------+
| Structure de donnée  | Pire cas                                                       |
|                      +--------------+--------------+----------------------------------+
|                      | Insertion    | Suppression  | Recherche                        |
|                      +--------------+--------------+-------------------+--------------+
|                      |              |              | Trié              | Pas trié     |
+======================+==============+==============+===================+==============+
| Tableau, pile, queue | :math:`O(n)` | :math:`O(n)` | :math:`O(log(n))` | :math:`O(n)` |
+----------------------+--------------+--------------+-------------------+--------------+
| Liste chaînée simple | :math:`O(1)` | :math:`O(1)` | :math:`O(n)`      | :math:`O(n)` |
+----------------------+--------------+--------------+-------------------+--------------+

Liste simplement chaînée (*linked-list*)
----------------------------------------

.. index:: linked-list, liste chaînée

La figure suivante illustre un set d'éléments liés entre eux à l'aide d'un pointeur rattaché à chaque élément. On peut s'imaginer que chaque élément peut se situer n'importe où en mémoire et
qu'il n'est alors pas indispensable que les éléments se suivent dans l'ordre.

Il est indispensable de bien identifier le dernier élément de la liste grâce à son pointeur associé
à la valeur ``NULL``.

.. figure:: ../assets/figures/dist/recursive-data-structure/list.*


.. code-block:: c

    #include <stdio.h>
    #include <stdlib.h>

    struct Point
    {
        double x;
        double y;
        double z;
    };

    struct Element
    {
        struct Point point;
        struct Element* next;
    };

    int main(void)
    {
        struct Element a = {.point = {1,2,3}, .next = NULL};
        struct Element b = {.point = {4,5,6}, .next = &a};
        struct Element c = {.point = {7,8,9}, .next = &b};

        a.next = &c;

        struct Element* walk = &a;

        for (size_t i = 0; i < 10; i++)
        {
            printf("%d. P(x, y, z) = %0.2f, %0.2f, %0.2f\n",
                i,
                walk->point.x,
                walk->point.y,
                walk->point.z
            );

            walk = walk->next;
        }
    }


Opérations sur une liste chaînée
--------------------------------

- Création
- Nombre d'éléments
- Recherche
- Insertion
- Suppression
- Concaténation
- Destruction

Lors de la création d'un élément, on utilise principalement le mécanisme
de l'allocation dynamique ce qui permet de récupérer l'adresse de
l'élément et de faciliter sa manipulation au travers de la liste.  Ne
pas oublier de libérer la mémoire allouée pour les éléments lors de leur
suppression…

Calcul du nombre d'éléments dans la liste
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pour évaluer le nombre d'éléments dans une liste, on effectue le
parcours de la liste à partir de la tête, et on passe d'élément en
élément grâce au champ *next* de la structure ``Element``. On incrément
le nombre d'éléments jusqu'à ce que le pointeur *next* soit égal à ``NULL``.

.. code-block:: c

    size_t count = 0;

    for (Element *e = &head; e != NULL; e = e->next)
        count++;
    }

Attention, cette technique ne fonctionne pas dans tous les cas, spécialement lorsqu'il y a des boucles dans la liste chaînée. Prenons l'exemple suivant:

.. figure:: ../assets/figures/dist/recursive-data-structure/loop.*

La liste se terminant par une boucle, il n'y aura jamais d'élément de fin et le nombre d'éléments
calculé sera infini. Or, cette liste a un nombre fixe d'éléments. Comment donc les compter ?

Il existe un algorithme nommé détection de cycle de Robert W. Floyd aussi appelé *algorithme du lièvre et de la tortue*. Il consiste à avoir deux pointeurs qui parcourent la liste chaînée. L'un avance deux fois plus vite que le second.

.. index:: Floyd

.. figure:: ../assets/figures/dist/recursive-data-structure/floyd.*

.. code-block:: c

  size_t compute_length(Element* head)
  {
      size_t count = 0;

      Element* slow = head;
      Element* fast = head;

      while (fast != NULL && fast->next != NULL) {
          slow = slow->next;
          fast = fast->next->next;

          count++;

          if (slow == fast) {
              // Collision
              break;
          }
      }

      // Case when no loops detected
      if (fast == NULL || fast->next == NULL) {
          return count;
      }

      // Move slow to head, keep fast at meeting point.
      slow = head;
      while (slow != fast) {
          slow = slow->next;
          fast = fast->next;

          count--;
      }

      return count;
  }


Une bonne idée pour se simplifier la vie est simplement d'éviter la création de boucles.

Insertion
^^^^^^^^^

L'insertion d'un élément dans une liste chaînée peut-être implémentée de la façon suivante:

.. code-block:: c

    Element* insert_after(Element* e, void* payload)
    {
        Element* new = malloc(sizeof(Element));

        memcpy(new->payload, payload, sizeof(new->payload));

        new->next = e->next;
        e->next = new;

        return new;
    }

Suppression
^^^^^^^^^^^

La suppression implique d'accéder à l'élément parent, il n'est donc pas possible à partir d'un élément donné de le supprimer de la liste.

.. code-block:: c

    void delete_after(Element* e)
    {
        e->next = e->next->next;
        free(e);
    }

Recherche
^^^^^^^^^

Rechercher dans une liste chaînée est une question qui peut-être complexe et il est nécessaire de ce poser un certain nombre de questions:

- Est-ce que la liste est triée?
- Combien d'espace mémoire puis-je utiliser?

On sait qu'une recherche idéale s'effectue en :math:`O(log(n))`, mais que la solution triviale en :math:`O(n)` est la suivante:

Pile
====

Queue
=====

Liste doublement chaînée
========================

Arbre binaire de recherche
==========================

L'objectif de cette section n'est pas d'entrer dans les détails des `arbres binaires <https://fr.wikipedia.org/wiki/Arbre_binaire_de_recherche>`__ dont la théorie requiert un ouvrage dédié, mais de vous sensibiliser à l'existence de ces structures de données qui sont à la base de beaucoup de langage de haut niveau comme C++, Python ou C#.

L'arbre binaire, n'est rien d'autre qu'une liste chaînée comportant deux enfants un ``left`` et un ``right``:

.. figure:: ../assets/figures/dist/recursive-data-structure/binary-tree.*

    Arbre binaire équilibré

Lorsqu'il est équilibré, un arbre binaire comporte autant d'éléments à gauche qu'à droite et lorsqu'il est correctement rempli, la valeur d'un élément est toujours:

- La valeur de l'enfant de gauche est inférieure à celle de son parent
- La valeur de l'enfant de droite est supérieure à celle de son parent

Cette propriété est très appréciée pour rechercher et insérer des données complexes. Admettons que l'on a un registre patient du type:

.. code-block:: c

    struct patient {
        size_t id;
        char firstname[64];
        char lastname[64];
        uint8_t age;
    }

    typedef struct node {
        struct patient data;
        struct node* left;
        struct node* right;
    } Node;

Si l'on cherche le patient numéro ``612``, il suffit de parcourir l'arbre de façon dichotomique:

.. code-block:: c

    Node* search(Node* node, size_t id)
    {
        if (node == NULL)
            return NULL;

        if (node->data.id == id)
            return node;

        return search(node->data.id > id ? node->left : node->right, id);
    }

L'insertion et la suppression d'éléments dans un arbre binaire fait appel à des `rotations <https://fr.wikipedia.org/wiki/Rotation_d%27un_arbre_binaire_de_recherche>`__, puisque les éléments doivent être insérés dans le correct ordre et que l'arbre, pour être performant doit toujours être équilibré. Ces rotations sont donc des mécanismes de rééquilibrage de l'arbre ne sont pas triviaux, mais dont la complexité d'exécution reste simple, et donc performante.

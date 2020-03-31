==============================
Structures de données avancées
==============================

Tableau dynamique
=================

Un tableau dynamique aussi appelé *vecteur* est, comme son nom l'indique, alloué dynamiquement dans le *heap* en fonction des besoins. Vous vous rappelez que le *heap* grossit à chaque appel de ``malloc`` et diminue à chaque appel de ``free``.  

Un tableau dynamique est souvent spécifié par un facteur de croissance (rien à voir avec les hormones). Lorsque le tableau est plein et que l'on souhaite rajouter un nouvel élément, le tableau est réalloué dans un autre espace mémoire plus grand avec la fonction ``realloc``. Cette dernière n'est rien d'autre qu'un ``malloc`` suivi d'un ``memcopy`` suivi d'un ``free``. Un nouvel espace mémoire est réservé, les données sont copiées du premier espace vers le nouveau, et enfin le premier espace est libéré. Voici un exemple : 

.. code-block:: c

    char *buffer = malloc(3); // Alloue un espace de trois chars
    buffer[0] = 'h'; 
    buffer[1] = 'e';
    buffer[2] = 'l'; // Maintenant le buffer est plein...
    *buffer = realloc(5); // Réalloue avec un espace de cinq chars
    buffer[3] = 'l'; 
    buffer[4] = 'o'; // Maintenant le buffer est à nouveau plein...
    free(buffer);

La taille du nouvel espace mémoire est plus grande d'un facteur donné que l'ancien espace. Selon les langages de programmation et les compilateurs, ces facteurs sont compris entre 3/2 et 2. C'est à dire que la taille du tableau prendra les tailles de 1, 2, 4, 8, 16, 32, etc. 

Lorsque le nombre d'éléments du tableau devient inférieur du facteur de croissance à la taille effective du tableau, il est possible de faire l'opération inverse, c'est-à-dire réduire la taille allouée. En pratique cette opération est rarement implémentée, car peu efficace (c.f. `cette <https://stackoverflow.com/a/60827815/2612235>`__ réponse sur stackoverflow).

Anatomie 
--------

Un tableau est représenté en mémoire comme un contenu séquentiel qui possède un début et une fin. On appelle son début la "tête" ou *head* et la fin du tableau sa "queue" ou *tail*. Selon que l'on souhaite ajouter des éléments au début ou à la fin du tableau la complexité n'est pas la même. 

Nous définirons par la suite le vocabulaire suivant: 

==============================================  ===============
Action                                          Terme technique 
==============================================  ===============
Ajout d'un élément à la tête du tableau         `unshift`       
Ajout d'un élément à la queue du tableau        `push`          
Suppression d'un élément à la tête du tableau   `shift`         
Suppression d'un élément à la queue du tableau  `pop`           
==============================================  ===============

Nous comprenons rapidement qu'il est plus compliqué d'ajouter ou de supprimer un élément depuis la tête du tableau, car il est nécessaire ensuite de déplacer chaque élément (l'élément 0 devient l'élément 1, l'élément 1 devient l'élément 2...). 

Un tableau dynamique peut être représenté par la figure suivante :

.. figure:: ../assets/figures/dist/data-structure/dyn-array.*

Un espace mémoire est réservé dynamiquement sur le tas. Comme ``malloc`` ne retourne pas la taille de l'espace mémoire alloué mais juste un pointeur sur cet espace, il est nécessaire de conserver dans une variable la capacité du tableau. Notons qu'un tableau de 10 ``int32_t`` représentera un espace mémoire de 4x10 bytes, soit 40 bytes. La mémoire ainsi réservée par ``malloc`` n'est généralement pas vide mais elle contient des valeurs, vestige d'une ancienne allocation mémoire d'un d'autre programme depuis que l'ordinateur a été allumé. Pour connaître le nombre d'éléments effectifs du tableau il faut également le mémoriser. Enfin, le pointeur sur l'espace mémoire est aussi mémorisé. 

Les composants de cette structure de donnée sont donc : 

- Un entier non signé ``size_t`` représentant la capacité totale du tableau dynamique à un instant T.
- Un entier non signé ``size_t`` représentant le nombre d'éléments effectivement dans le tableau.
- Un pointeur sur un entier ``int *`` contenant l'adresse mémoire de l'espace alloué par ``malloc``.
- Un espace mémoire alloué par ``malloc`` et contenant des données.

L'opération ``pop`` retire l'élément de la fin du tableau. Le nombre d'éléments est donc ajusté en conséquence.

.. figure:: ../assets/figures/dist/data-structure/dyn-array-pop.*

.. code-block:: c

    if (elements <= 0) exit(EXIT_FAILURE);
    int value = data[--elements];

L'opération ``push`` ajoute un élément à la fin du tableau. 

.. figure:: ../assets/figures/dist/data-structure/dyn-array-push.*

.. code-block:: c

    if (elements >= capacity) exit(EXIT_FAILURE);
    data[elements++] = value;

L'opération ``shift`` retire un élément depuis le début. L'opération à une complexité de O(n) puisqu'à chaque opération il est nécessaire de déplacer chaque éléments qu'il contient.

.. figure:: ../assets/figures/dist/data-structure/dyn-array-shift.*

.. code-block:: c

    if (elements <= 0) exit(EXIT_FAILURE);
    int value = data[0];
    for (int k = 0; k < capacity; k++)
        data[k] = data[k+1];

Une optimisation peut être faite en déplacant le pointeur de donnée de 1 permettant de réduite la complexité à O(1) :

.. code-block:: c

    if (elements <= 0) exit(EXIT_FAILURE);
    if (capacity <= 0) exit(EXIT_FAILURE);
    int value = data[0];
    data++;
    capacity--;

Enfin, l'opération ``unshift`` ajoute un élément depuis le début du tableau :

.. figure:: ../assets/figures/dist/data-structure/dyn-array-unshift.*

.. code-block:: c

    for (int k = elements; k < 1; k--)
        data[k] = data[k - 1];
    data[0] = value;

Dans le cas ou le nombre d'éléments atteint la capacité maximum du tableau, il est nécessaire de réallouer l'espace mémoire avec ``realloc``. Généralement on se contente de doubler l'espace alloué. 

.. code-block:: c

    if (elements > capacity) {
        data = realloc(data, capacity *= 2);
    }

Piles ou LIFO (*Last In First Out*)
===================================

Une pile est une structure de donnée similaire à un tableau dynamique dans laquelle il n'est possible que : 

- d'ajouter un élément (*push*)
- retirer un élément (*pop*)
- obtenir le dernier élément (*peek*)
- tester si la pile est vide (*is_empty*)
- tester si la pile est pleine avec (*is_full*)

Queues ou FIFO (*First In First Out*)
=====================================

Une queue est similaire à un tableau dynamique dans laquelle il n'est possible que : 

- ajouter un élément à la queue (*push*) aussi nommé *enqueue*
- supprimer un élément au début de la queue (*shift*) aussi nommé *dequeue*

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

Tableau de Hachage
==================

Les tableaux de hachage (*Hash Table*) sont une structure particulière combinant une liste chaînée avec un tableau statique ou dynamique. 

.. figure:: ../assets/figures/dist/data-structure/hash-table.*

Imaginons que nous souhaitions mémoriser une liste de 2000 étudiants. Rechercher le nom d'un étudiant dans cette liste reviendrait à parcourir les
2000 entrées dans le cas le plus défavorable. La complexité de recherche est donc de O(log n) pour un tableau statique et de O(n) dans une liste chaînée. En organisant les données différemment, il est possible de réduire cette complexité à O(1) dans le cas ou la taille du tableau de hachage est égal au nombre d'étudiants. 

Pour constituer un tableau de hachage, il convient de calculer le *hash* d'une entrée à l'aide d'une fonction de hachage. Dans le cas le plus simple imaginons la solution suivante : 

.. code-block:: c

    int hash(char *str) {
        int hash = 0;
        char c;
        while((c = str++) != '\0') 
            hash ^= c;
        return hash;
    } 

Cette fonction calcul le OU Exclusif entre chaque caractère : 

.. code-block:: text

                 ┌─┬─┬─┬─┬─┬─┬─┬─┐
    'H' == 72 == │0│1│0│0│1│0│0│0│ 
                 ├─┼─┼─┼─┼─┼─┼─┼─┤
    'E' == 69 == │0│1│0│0│0│1│0│1│ 
                 ├─┼─┼─┼─┼─┼─┼─┼─┤
    'L' == 76 == │0│1│0│0│1│1│0│0│ 
                 ├─┼─┼─┼─┼─┼─┼─┼─┤
    'L' == 76 == │0│1│0│0│1│1│0│0│ 
                 ├─┼─┼─┼─┼─┼─┼─┼─┤                 
    'O' == 79 == │0│1│0│0│1│1│1│1│ 
                 └─┴─┴─┴─┴─┴─┴─┴─┘
       XOR ─────────────────────── 
                 ┌─┬─┬─┬─┬─┬─┬─┬─┐
                 │0│1│0│0│0│0│1│0│ == 66
                 └─┴─┴─┴─┴─┴─┴─┴─┘
    
On obtient 66, qui est la valeur hachée de cette chaîne de caractère. Si nous disposons d'une table de hashage de taille 100, il suffit donc d'insérer à la position 66 de la table de hashage un pointeur vers une liste chaînée comportant cette chaîne de caractère. Si la fonction de hachage est bonne, les entrées vont se répartir équitablement dans les 100 entrées de la table de hachage et les listes chaînées seront chacune 100x plus petites. On divise ainsi par 100 la complexité de la recherche. Bien entendu dans le cas ou la fonction de hachage retourne une valeur plus grande que 100, il convient de calculer le modulo 100. 

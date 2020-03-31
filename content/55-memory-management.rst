.. _memory-management:

=====================
Gestion de la mémoire
=====================

Vous l'aurez appris à vos dépens, l'erreur *Segmentation fault* (erreur de segmentation) arrive souvent lors du développement. Ce chapitre s'intéresse à la mémoire et vulgarise les concepts de segmentation et traite de l'allocation dynamique.

La mémoire d'un programme est découpée en `segments de données <https://fr.wikipedia.org/wiki/Segment_de_donn%C3%A9es>`__. Les principaux segments sont:

Segment de code ``.text``
    Les instructions du programme exécutable sont chargées dans ce segment.

Segment de constantes et chaînes de caractères ``.rodata``
    Les constantes globales ``const int = 13`` et les chaînes de caractères sont enregistrées dans ce segment.

Segment de variables initialisées ``.bss``
    Ce segment est garanti d'être initialisé à zéro lorsque le programme est chargé en mémoire. Les variables globales statiques tels que ``static int foo = 0`` seront stockées dans ce segment.

Segment de variables non initialisées ``.data``
    Les variables globales non initialisées comme ``static int bar;`` seront placées dans ce segment.

Segment de tas ``.heap``
    Les allocations dynamiques décrites plus bas dans ce chapitre sont déclarées ici.

Segment de pile ``.stack``
    La chaîne d'appel de fonction ainsi que toutes les variables locales sont mémorisées dans ce segment.

Allocation statique
===================

Jusqu'ici toutes les variables que nous avons déclarées ont été déclarées statiquement. C'est-à-dire que le compilateur est capable a priori de savoir combien de place prend telle ou telle variable et les agencer en mémoire dans les bons segments. On appelle cette méthode d'allocation de mémoire l'allocation statique.

La `déclaration statique <https://fr.wikipedia.org/wiki/Allocation_de_m%C3%A9moire#Allocation_statique>`__ suivante déclare un tableau de 1024 entiers 64-bits initialisés à zéro et stockés dans le segment ``.bss``, soit 64 kio:

::

    static int64_t vector[1024] = {0};

Allocation dynamique
====================

Il est des circonstances ou un programme ne sait pas combien de mémoire il a besoin. Par exemple un programme qui compterait le nombre d'occurrences de chaque mot dans un texte devra se construire un index de tous les mots qu'il découvre lors de la lecture du fichier d'entrée. A priori ce fichier d'entrée étant inconnu au moment de l'exécution du programme, l'espace mémoire nécessaire à construire ce dictionnaire de mots est également inconnu.

L'approche la plus naïve serait d'anticiper le cas le plus défavorable. Le dictionnaire Littré comporte environ 132'000 mots tandis que le Petit Larousse Illustré 80'000 mots environ. Pour se donner une bonne marge de manoeuvre et anticiper les anglicismes et les noms propres. Il suffirait de réserver un tableau de 1 million de mots de 10 caractères soit un peu plus de 100 MiB de mémoire quand bien même le fichier qui serait lu ne comporterait que 2 mots: ``Hello World!``.

L'approche correcte est d'allouer la mémoire au moment ou on en a besoin, c'est ce que l'on appelle l'`allocation dynamique <https://fr.wikipedia.org/wiki/Tas_(allocation_dynamique)>`__.

Lorsqu'un programme à besoin de mémoire, il peut générer un appel système pour demander au système d'exploitation le besoin de disposer de plus de mémoire. En pratique on utilise deux fonctions de la bibliothèque standard `<stdlib.h>`:

`void *malloc(size_t size)`
    Alloue dynamiquement un espace mémoire de ``size`` bytes. Le terme *malloc* découle de *Memory ALLOCation*.

`void *calloc(size_t nitems, size_t size)`
    Fonctionne de façon similaire à ``malloc`` mais initialise l'espace alloué à zéro.

`void free(void *ptr)`
    Libère un espace préalablement alloué par ``malloc`` ou ``calloc``

L'allocation se fait sur le `tas` (*heap*) qui est de taille variable. À chaque fois qu'un espace mémoire est demandé, ``malloc`` recherche dans le segment un espace vide de taille suffisante, s'il ne parvient pas, il exécute l'appel système `sbrk <https://en.wikipedia.org/wiki/Sbrk>`__ qui permet de déplacer la frontière du segment mémoire et donc d'agrandir le segment.

.. figure:: ../assets/figures/dist/memory/malloc.*

Mémoire de programme
====================

Les segments mémoires sont une construction de la bibliothèque standard, selon la bibliothèque utilisée et à fortiori le système d'exploitation utilisé, l'agencement mémoire peut varier.

Néanmoins une bonne représentation est la suivante:

.. figure:: ../assets/figures/dist/memory/program-memory.*

    Organisation de mémoire d'un programme

On observe que le tas et la pile vont à leur rencontre, et que lorsqu'ils se percutent c'est le crash avec l'erreur bien connue `stack overflow <https://fr.wikipedia.org/wiki/D%C3%A9passement_de_pile>`__.

La pile
=======

Lorsqu'un programme s'exécute, l'ordre dont les fonctions s'exécutent n'est pas connu à priori. L'ordre d'exécution des fonctions dans l'exemple suivant est inconnu par le programme et donc les éventuelles variables locales utilisées par ces fonctions doivent dynamiquement être allouées.

.. code-block:: c

    #include <stdio.h>
    #include <stdlib.h>

    double square(double num) {
        return num * num
    }

    double cube(double num) {
        return num * num * num;
    }

    int main(void) {
        double num = 10;

        for (size_t i = 0; i < 10; i++) {
            if (rand() % 2) {
                num = square(num);
            } else {
                num = cube(num);
            }
        }

        printf("%f\n", num);
    }

Lors d'un appel de fonction, le compilateur ajoute avant la première instruction du code caché permettant d'empiler sur un espace mémoire dédié (*stack*) les variables locales dont il a besoin ainsi que certaines informations tel que l'adresse mémoire de retour.

Allocation dynamique sur le tas
===============================

L'allocation dynamique permet de réserver - lors de l'exécution - une
zone mémoire dont on vient de calculer la taille. On utilisera la
fonction *malloc* (memory allocation) pour réserver de la mémoire. Cette
fonction n'initialise pas la zone réservée.

.. code-block:: c

    typedef unsigned int size_t;
    void* malloc(size_t size);

Il est nécessaire d'inclure le fichier *stdlib.h* pour utiliser les
fonctions d'allocation mémoire. Par exemple, pour réserver un tableau de
n valeurs de type *double* :

.. code-block:: c

      int n;
      double * zone_acquisition; // pointeur sur la zone à réserver

      n = 100;

      zone_acquisition = (double*)malloc(n * sizeof(double));

Allocation dynamique sur le tas avec mise à zéro
------------------------------------------------

On utilisera la fonction *calloc* (memory allocation) pour réserver de
la mémoire avec initialisation automatique de la zone réservée.

.. code-block:: c

    void * calloc (size_t count, size_t size);

Cette fonction réserve *count* x *size* octets en mémoire et
l'initialise à zéro.

Modification de la taille d'une zone déjà allouée sur le tas
------------------------------------------------------------

Si l'on veut agrandir une zone déjà allouée avec *malloc* ou *calloc*,
on utilisera la fonction suivante :

.. code-block:: c

    void * realloc (void * ptr, size_t size);

Elle permet de :

-  réallouer un bloc de mémoire avec une nouvelle taille
-  si ptr est NULL, créer un nouveau bloc
-  si la réallocation échoue, retourner NULL ; le bloc passé en
   paramètre reste alors inchangé
-  en cas de succès, l'adresse retournée peut être différente de ptr ; le
   bloc initialement pointé par ptr a alors été libéré
-  le bloc réalloué est initialisé avec le contenu du bloc ptr ;
   l'espace supplémentaire est non initialisé

Libération
----------

Le tas n'étant pas extensible à l'infini, il faut libérer la mémoire dés
que l'on n'en a plus l'utilité.

.. code-block:: c

    void free(void *memblock);

Une fois libérée, la mémoire (donc son pointeur) ne doit plus être
utilisée sous peine de corrompre des données du système.

.. code-block:: c

      int n;
      double * zone_acquisition; // pointeur sur la zone à réserver

      n=100;

      zone_acquisition = (double*) malloc ( n * sizeof(double) );

      // utilisation...

      free(zone_acquisition); // libère la mémoire

De la même manière, il ne faut pas libérer un bloc qui n'a pas été
alloué. Si on ne libère pas la mémoire, elle reste allouée pour
l'application et la zone disponible diminue. Il peut arriver qu'il ne
reste plus d'espace disponible pour l'allocation dynamique ; cela peut
entraver la bonne marche de l'ordinateur. Ce problème est souvent dû à
des erreurs de conception des applications qui ne libèrent pas tous les
blocs alloués ; on observe alors un phénomène de fuite mémoire qui cause
le plantage de la machine. Selon les fréquences d'allocation et de non
libération, ces problèmes peuvent survenir immédiatement, ou après
plusieurs jours de fonctionnement, ce qui complique grandement les
opérations de debug...

Allocation dynamique sur la pile
--------------------------------

L'allocation dynamique sur la pile est équivalente à l'allocation sur
le tas sauf qu'elle est plus rapide (pas de recherche par le système
d'un espace suffisant et continu) et qu'elle ne nécessite pas de
libération.

On utilisera la fonction *alloca* (memory allocation) pour réserver de
la mémoire. Cette fonction n'initialise pas la zone réservée.

.. code-block:: c

    void* alloca(size_t size);

Il est nécessaire d'inclure le fichier *malloc.h* pour utiliser cette
fonction d'allocation mémoire sur la pile. L'espace est libéré à la
sortie de la fonction appelante. On veillera tout particulièrement à ce
que le pointeur ayant reçu l'adresse de la zone mémoire réservé ne soit
pas exploité en dehors de la fonction (puisque la zone est libérée quand
on en sort).

Limite d'utilisation de la pile
-------------------------------

L'espace mémoire utilisé par la pile est une zone dont l'usage est
uniquement dédié au programme. Si plusieurs programmes cohabitent en
mémoire, ils auront chacun leur propre pile.

Cet espace mémoire dédié à la pile est de taille fixe et définie lors de
la compilation du programme.

La pile reçoit les éléments suivants :

-  les variables locales aux fonctions,
-  les variables déclarées comme paramètres dans les fonctions,
-  les informations liées au mécanismes d'appel et de retour des
   fonctions,
-  les données retournées par les fonctions,
-  les zone allouées par la fonction ``alloca``.

Étant donné que la taille de la pile est fixe, il y a un risque qu'elle
soit trop petite pour supporter toutes les informations que votre
programme doit y placer. Si cela se produit, il y a corruption de la
mémoire puisque la pile 'déborde' et que vous dépassez la zone qui lui
est dédiée.

Les événements suivants peuvent générer des débordements de pile :

-  trop de variables locales (par exemple un grand tableau),
-  trop d'appels de fonctions en cascade,
-  utilisation de fonctions récursives (qui s'autoappellent).

Dans le jargon informatique, on appelle ça du *jardinage* puisque vous
allez piétiner les zones mémoires voisines sans en avoir la permission.

Le compilateur (en réalité l'éditeur de liens - le *linker*) vous permet
de spécifier la taille de la pile ; c'est une de ses nombreuses options.

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


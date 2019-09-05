===========
Philosophie
===========

La philosophie d'un bon développeur repose sur plusieurs principes de programmation relevant majoritairement du bon sens de l'ingénieur, les vaudois l'appelant parfois: **le bon sens paysan** comme l'aurait sans doute confirmé feu `Jean Villard dit Gilles <https://fr.wikipedia.org/wiki/Jean_Villard>`__.

.. _ockham:

Rasoir d'Ockham
===============

.. figure:: ../assets/images/razor.*

Le `rasoir d'Ockham <https://fr.wikipedia.org/wiki/Rasoir_d%27Ockham>`__ expose en substance que les multiples ne doivent pas être utilisés sans nécessité. C'est un principe d'économie, de simplicité et de parcimonie. Il peut être résumé par la devise `Shadok <https://en.wikipedia.org/wiki/Les_Shadoks>`__: "Pourquoi faire simple quand on peut faire compliqué ?"

En philosophie un `rasoir <https://fr.wikipedia.org/wiki/Rasoir_(philosophie)>`__ est un principe qui permet de *raser* des explications improbables d'un phénomène. Ce principe tient son nom de Guillaume d'Ockham (XIVe siècle) alors qu'il date probablement d'Empédocle (Ἐμπεδοκλῆς) vers 450 av. J.-C.

Il trouve admirablement bien sa place en programmation où le programmeur ne peut conserver une vue d'ensemble sur un logiciel qui est par nature invisible à ses yeux. Seuls la simplicité et l'art de la conception logicielle sauvent un développeur de la noyade, car un programme peut rester simple quelque soit sa taille si chaque strate de conception reste évidente et simple à comprendre pour celui qui chercherait à contribuer au projet d'autrui.

Principes de programmation
==========================

.. _dry:

DRY
---

**Ne vous répétez pas** (*Don't Repeat Yourself*)! Je répète, **ne vous répétez pas**! Il s'agit d'une philosophie de développement logiciel évitant la `redondance de code <https://fr.wikipedia.org/wiki/Duplication_de_code>`__. L'excellent livre `The Pragmatic Programmer <https://en.wikipedia.org/wiki/The_Pragmatic_Programmer>`__ de Andrew Hunt et David Thomas décrit cette philosophie en ces termes:

    Dans un système, toute connaissance doit avoir une représentation unique, non ambiguë, faisant autorité.

En d'autres termes, le programmeur doit avoir sans cesse à l'esprit une sonnette d'alarme prête à vrombir lorsque qu'il presse machinalement :kbd:`CTRL` (:kbd:`⌘`) + :kbd:`C` suivi de :kbd:`CTRL` (:kbd:`⌘`) + :kbd:`V`. Dupliquer du code et quelque soit l'envergure de texte concerné est **toujours** une mauvaise pratique, car c'est le plus souvent le signe d'un `code smell <https://fr.wikipedia.org/wiki/Code_smell>`__ qui indique que le code peut être simplifié et optimisé.

KISS
----

`Keep it simple, stupid <https://fr.wikipedia.org/wiki/Principe_KISS>`__ est une ligne directrice de conception qui encourage la simplicité d'un développement. Il est similaire au rasoir d'Ockham, mais grandement plus commun en informatique. Énoncé par `Eric Steven Raymond <https://fr.wikipedia.org/wiki/Eric_Raymond>`__ puis par le `Zen de Python <https://fr.wikipedia.org/wiki/Zen_de_Python>`__ un programme ne doit faire qu'une chose, et une chose simple. C'est une philosophie grandement respectée dans l'univers Unix/Linux. Chaque programme de base du *shell* (``ls``, ``cat``, ``echo``, ``grep``, ...) ne fait qu'une tâche simple, le nom est court et simple à retenir.

YAGNI
-----

YAGNI est un anglicisme de *you ain't gonna need it* qui peut être traduit par: vous n'en aurez pas besoin. C'est un principe très connu en développent Agile XP (`Extreme Programming <https://fr.wikipedia.org/wiki/Extreme_programming>`__) qui déclare qu'un développeur logiciel ne devrait pas implémenter une fonctionnalité à un logiciel tant que celle-ci n'est pas absolument nécessaire.

Ce principe combat le biais du développeur à vouloir sans cesse démarrer de nombreux chantiers sans se focaliser sur l'essentiel strictement nécessaire d'un programme et permettant de respecter le cahier des charges convenu avec le partenaire/client.

SSOT
----

Ce principe tient son acronyme de `single source of truth <https://en.wikipedia.org/wiki/Single_source_of_truth>`__. Il adresse principalement un défaut de conception relatif aux métadonnées que peuvent être les paramètres d'un algorithme, le modèle d'une base de données ou la méthode usitée d'un programme à collecter des données.

Un programme qui respecte ce principe évite la duplication des données. Des défauts courants de conception sont:

- Indiquer le nom d'un fichier source dans le fichier source
- Stocker la même image, le même document dans différents formats
- Stocker dans une base de données le nom *Doe*, prénom *John* ainsi que le nom complet *John Doe*
- Avoir un commentaire C du type: ``int height = 206; // Size of Hafþór Júlíus Björnsson which is 205 cm`` (deux sources de vérités contradictoires)
- Conserver une copie des mêmes données sous des formats différents (un tableau de données brutes et un tableau des mêmes données, mais triées)

Zen de Python
=============

Python est un langage de programmation qui devient très populaire, il est certes moins performant que C, mais il se veut être de très haut niveau.

Le `Zen de Python <https://fr.wikipedia.org/wiki/Zen_de_Python>`__ est un ensemble de 19 principes publiés en 1999 par Tim Peters. Largement accepté par la communauté de développeurs et il est connu sous le nom de **PEP 20**.

Voici le texte original anglais:

.. code-block::

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one—and preferably only one—obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than right now.[n 1]
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea—let's do more of those!

The code taste
==============

Dans une `conférence <https://www.ted.com/talks/linus_torvalds_the_mind_behind_linux>`__ TED en 2016, le créateur de Linux, Linus Torvald évoqua un principe nommé *code taste* traduisible par *avoir du goût pour le code*.


Il évoqua l'exemple C suivant et demanda à l'auditoire si ce code est de bon goût:

.. code-block:: c

    void remove_list_entry(List* list, Entry* entry)
    {
        Entry* prev = NULL;
        Entry* walk = list->head;

        while (walk != entry) {
            prev = walk;
            walk = walk->next;
        }

        if (!prev)
            list->head = entry->next;
        else
            prev->next = entry->next;
    }

Il répondit que ce code est de mauvais goût, qu'il est *vilain* et *moche*, car ce test placé après la boucle ``while`` jure avec le reste du code et que parce que ce code semble laid, il doit y avoir une meilleure implémentation de meilleur goût. On dit dans ce cas de figure que le code *sent*, ce test est de trop, et il doit y avoir un moyen d'éviter de traiter un cas particulier en utilisant un algorithme meilleur.

Enlever un élément d'une liste chaînée nécessite de traiter deux cas:

- Si l'élément est au début de la liste, il faut modifier ``head``
- Sinon il faut modifier l'élément précédent ``prev->next``

Après avoir longuement questionné l'auditoire, il présente cette nouvelle implémentation:

.. code-block:: c

    void remove_list_entry(List* list, Entry* entry)
    {
        Entry** indirect = &head;

        while ((*indirect) != entry)
            indirect = &(*indirect)->next;

        *indirect = entry->next;
    }

La fonction originale de 10 lignes de code a été réduite à 4 lignes et bien que le nombre de lignes compte moins que la lisibilité du code, cette nouvelle implémentation élimine le traitement des cas d'exception en utilisant un adressage indirect beaucoup plus élégant.

Un autre exemple similaire et plus simple à comprendre est présenté par Brian Barto sur un article publié sur `Medium <https://medium.com/@bartobri/applying-the-linus-tarvolds-good-taste-coding-requirement-99749f37684a>`__. Il donne l'exemple de l'initialisation à zéro de la bordure d'un tableau bidimensionnel:

.. code-block:: c

    for (size_t row = 0; row < GRID_SIZE; ++row)
    {
        for (size_t col = 0; col < GRID_SIZE; ++col)
        {
            if (row == 0)
                grid[row][col] = 0; // Top Edge

            if (col == 0)
                grid[row][col] = 0; // Left Edge

            if (col == GRID_SIZE - 1)
                grid[row][col] = 0; // Right Edge

            if (row == GRID_SIZE - 1)
                grid[row][col] = 0; // Bottom Edge
        }
    }

On constate plusieurs fautes de goût:

- ``GRID_SIZE`` pourrait être différent de la réelle taille de ``grid``
- Les valeurs d'initialisation sont dupliquées
- La complexité de l'algorithme est de :math:`O(n^2)` alors que l'on ne s'intéresse qu'à la bordure du tableau.

Voici une solution plus élégante:

.. code-block:: c

    const size_t length = sizeof(grid[0]) / sizeof(grid[0][0]);
    const int init = 0;

    // Edges initialisation
    for (size_t i = 0; i < length; i++)
    {
        grid[i][0] = grid[0][i] = init; // Top and Left
        grid[length - 1][i] = grid[i][length - 1] = init; // Bottom and Right
    }


.. _code_smell:

L'odeur du code
===============

Un code *sent* si certains indicateurs sont au rouge. On appelle ces indicateurs des `antipatterns <https://fr.wikipedia.org/wiki/Antipattern>`__. Voici quelques indicateurs les plus courants:

- **Mastodonte** Une fonction est plus longue qu'un écran de haut (~50 lignes)
- Un fichier est plus long que **1000 lignes**.
- **Ligne Dieu**, une ligne beaucoup trop longue et *de facto* illisible.
- Une fonction à plus de **trois** paramètres
    .. code-block:: c

        void make_coffee(int size, int mode, int mouture, int cup_size,
            bool with_milk, bool cow_milk, int number_of_sugars);

- **Copier coller**, du code est dupliqué
- Les commentaires expliquent le comment du code et non le pourquoi
    .. code-block:: c

        // Additionne une constante avec une autre pour ensuite l'utiliser
        double u = (a + cst);
        u /= 1.11123445143; // division par une constante inférieure à 2

- **Arbre de Noël**, plus de deux structures de contrôles sont impliquées
    .. code-block:: c

        if (a > 2) {
            if (b < 8) {
                if (c ==12) {
                    if (d == 0) {
                        exception(a, b, c, d);
                    }
                }
            }
        }

- Usage de ``goto``
    .. code-block:: c

        loop:
            i +=1;
            if (i > 100)
                goto end;
        happy:
            happy();
            if (j > 10):
                goto sad;
        sad:
            sad();
            if (k < 50):
                goto happy;
        end:

- Plusieurs variables avec des noms très similaires
    .. code-block:: c

        int advice = 11;
        int advise = 12;

- **Action à distance** par l'emploi immodéré de variables globales
- **Ancre de bateau**, un composant inutilisé, mais gardé dans le logiciel pour des raisons politiques (YAGNI)
- **Cyclomatisme aigu**, quand trop de structures de contrôles sont nécessaires pour traiter un problème apparemment simple
- **Attente active**, une boucle qui ne contient qu'une instruction de test, attendant la condition
    .. code-block:: c

        while (true) {
            if (finished) break;
        }
- **Objet divin** quand un composant logiciel assure trop de fonctions essentielles (KISS)
- **Coulée de lave** lorsqu'un code immature est mis en production
- **Chirurgie au fusil de chasse** quand l'ajout d'une fonctionnalité logicielle demande des changements multiples et disparates dans le code (`Shotgun surgery <https://en.wikipedia.org/wiki/Shotgun_surgery>`__).

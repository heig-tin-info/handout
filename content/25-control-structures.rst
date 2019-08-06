======================
Structures de contrôle
======================

Les structure de contrôle appartiennent aux langages de programmation dit `structurés <https://fr.wikipedia.org/wiki/Programmation_structur%C3%A9e>`__. Elles permettent de modifier l'ordre des opérations lors de l'exécution du code Il y a trois catégories de structures de contrôle en C:

1. Les embranchements (``branching``)
2. Les boucles (``loops``)
3. Les sauts (``jumps``)

Ces structures de contrôles sont toujours composées de

- Sequences
- Selections
- Répétitions
- Appels de fonctions

Sequences
=========

En C, chaque instruction est séparée de la suivante par un point virgule ``;`` (U+003B).

.. code-block:: c

    k = 8; k *= 2;

Une séquence est une suite d'instructions regroupées en un bloc matérialisé par des accolades ``{}``:

.. code-block:: c

    {
        double pi = 3.14;
        area = pi * radius * radius;
    }

Les embranchements
==================

Les embranchements sont des instructions de prise de décision. Une prise de décision peut être binaire, lorsqu'il y a un choix *vrai* et un choix *faux*, ou multiple lorsque la condition est scalaire. En C il y en a trois type d'embranchements:

1. ``if``, ``if else``
2. ``switch``
3. L'instruction ternaire

.. figure:: assets/branching-diagram.svg

    Exemples d'embranchements dans les diagrammes de flux BPMN (Business Process Modeleing Notation) et NSD (Nassi-Shneiderman)

Les embranchements s'appuyent sur les séquences:

.. code-block:: c

    if (value % 2)
    {
        printf("odd\n");
    }
    else
    {
        printf("even\n");
    }

if..else
--------

Le mot clé ``if`` est toujours suivi d'une condition entre parenthèses qui est évaluée. Si la condition est vraie, le premier bloc est exécuté, sinon, le second bloc situé après le ``else`` est exécuté.

Les enchaînements possibles sont:

- ``if``
- ``if`` + ``else``
- ``if`` + ``else if``
- ``if`` + ``else if`` + ``else if`` + ...
- ``if`` + ``else if`` + ``else``

Une condition n'est pas nécessairement unique mais peut-être la concaténation logique de plusieurs conditions séparées:

.. code-block:: c

    if((0 < x && x < 10) || (100 < x && x < 110) || (200 < x && x < 210))
    {
        printf("La valeur %d est valide", x);
        is_valid = true;
    }
    else
    {
        printf("La valeur %d n'est pas valide", x);
        is_valid = false;
    }

Remarquons qu'au passage cet exemple peut être simplifié:

.. code-block:: c

    is_valid = (0 < x && x < 10) || (100 < x && x < 110) || (200 < x && x < 210);

    if (is_valid)
    {
        printf("La valeur %d est valide", x);
    }
    else
    {
        printf("La valeur %d n'est pas valide", x);
    }


Notons quelques erreurs courantes:

- Il est courant de placer un point virgule derrière un ``if``. Le point virgule correspondant à une instruction vide, c'est cette instruction qui sera exécutée si la condition du test est vraie.

  .. code-block:: c

    if (z == 0);
    printf("z est nul"); // ALWAYS executed

- Le test de la valeur d'une variable s'écrite avec l'opérateur d'égalité ``==`` et non l'opérateur d'affectation ``=``. Ici, l'évaluation de la condition vaut la valeur affectée à la variable.

  .. code-block:: c

    if (z = 0)
        printf("z est nul"); // NEVER executed

- L'oubli des accolades pour déclarer un bloc d'instructions

  .. code-block:: c

        if (z == 0)
            printf("z est nul");
            is_valid = false;
        else
            printf("OK");

L'instruction ``if`` permet également l'embranchement multiple, lorsque les conditions ne peuvent pas être regroupées:

.. code-block:: c

    if (value % 2)
    {
        printf("La valeur est impaire.");
    }
    else if (value > 500)
    {
        printf("La valeur est paire et supérieure à 500.");
    }
    else if (!(value % 5)
    {
        printf("La valeur est paire, inférieur à 500 et divisible par 5.");
    }
    else
    {
        printf("La valeur ne satisfait aucune condition établies.");
    }

.. _switch:

``switch``
----------

L'embranchement multiple, lorsque la condition n'est pas binaire mais scalaire, l'instruction ``switch`` peut-être utilisée:

.. code-block:: c

    switch (defcon)
    {
        case 1:
            printf("Guerre nucléaire imminente");
            break;
        case 2:
            printf("Prochaine étape, guerre nucléaire");
            break;
        case 3:
            printf("Acroissement de la préparation des forces");
            break;
        case 4:
            printf("Mesures de sécurité renforcées et renseignements accrus");
            break;
        case 5:
            printf("Rien à signaler, temps de paix");
            break;
        default:
            printf("ERREUR: Niveau d'alerte DEFCON invalide");
    }

La valeur par défaut ``default`` est optionnelle mais recommandée pour traiter les cas d'erreurs possibles.

La structure d'un ``switch`` est composée d'une condition ``switch (condition)`` suivie d'une séquence ``{}``. Les instructions de cas ``case 42:`` sont appelés *labels*. L'instruction ``break`` termine l'exécution de la séquence ``switch``.

Les labels peuvent être chaînés sans instructions intermédiaires ni ``break``:

.. code-block:: c

    switch (coffee)
    {
        case IRISH_COFFEE:
            add_whisky();

        case CAPPUCCINO:
        case MACCHIATO:
            add_milk();

        case ESPRESSO:
        case AMERICANO:
            add_coffee();
            break;

        default:
            printf("ERREUR 418: Type de café inconnu");
    }

Notons quelques observations:

- La structure ``switch`` bien qu'elle puisse toujours être remplacée par une structure ``if..else if`` est généralement plus élégante et plus lisible. Elle évite par ailleurs de répéter la condition plusieurs fois (c.f. :numref:`DRY`).
- Le compilateur est mieux à même d'optimiser un choix multiple lorsque les valeurs scalaires de la condition triées se suivent directement e.g. ``{12, 13, 14, 15}``.
- L'ordre des cas d'un ``switch`` n'a pas d'importance, le compilateur peut même choisir de réordonner les cas pour optimiser l'exécution.

Les boucles
===========

Une boucle est une structure itérative permettant de répéter l'exécution d'une séquence. En C il existe trois type de boucles:

- ``for``
- ``while``
- ``do`` .. ``while``

.. figure:: assets/for.svg

    Aperçu des trois structure de boucles

while
-----

La structure ``while`` répête une séquence **tant que** la condition est vraie.

Dans l'exemple suivant tant que le poids d'un objet déposé sur une balance est inférieur à une valeur constante, une masse est ajoutée et le système patiente avant stabilisation

.. code-block:: c

    while (get_weight() < 420 /* newtons */)
    {
        add_one_kg();
        wait(5 /* seconds */);
    }

Sequentiellement une boucle ``while`` test la condition, puis execute la séquence associée.

do..while
---------

De temps en temps il est nécessaire de tester la condition à la sortie de la séquence et non à l'entrée. La boucle ``do``...``while`` permet justement ceci:

.. code-block:: c

    size_t i = 10;

    do {
        printf("Veuillez attendre encore %d seconde(s)\r\n", i);
        i -= 1;
    } while (i);

Contrairement à la boucle ``while``, la séquence est ici exécutée **au moins une fois**.

for
---

La boucle ``for`` est un ``while`` amélioré qui permet en une ligne de résumer les conditions de la boucle:

.. code-block:: c

    for (/* expression 1 */; /* expression 2 */; /* expression 3 */)
    {
        /* séquence */
    }

Expression 1
    Exécutée une seule fois à l'entrée dans la boucle, c'est l'expression d'initialisation permettant par exemple de déclarer une variable et de l'initialiser à une valeur particulière.

Expression 2
    Condition de validité (ou de maintient de la boucle). Tant que la condition est vraie, la boucle est exécutée.

Expression 3
    Action de fin de tour. A la fin de l'exécution de la séquence, cette action est exécutée avant le tour suivant. Cette action permet par exemple d'incrémenter une variable.

Voici comment répéter 10x un block de code:

.. code-block:: c

    for (size_t i = 0; i < 10; i++)
    {
        something();
    }

Notons que les portions de ``for`` sont optionnels et que la structure suivante est strictement identique à la boucle ``while``:

.. code-block:: c

    for (; get_weight() < 420 ;)
    {
        /* ... */
    }

Boucles infinies
----------------

Une boucle infinie n'est jamais terminée. On renconte souvent ce type de boucle dans ce que l'on appelle à tort *La boucle principale* aussi nommée `run loop <https://en.wikipedia.org/wiki/Event_loop>`__. Lorsqu'un programme est exécuté *bare-metal*, c'est à dire directement à même le microcontrôleur et sans système d'exploitation, il est fréquent d'y trouver une fonction ``main`` tel que:

.. code-block:: c

    void main_loop()
    {
        // Boucle principale
    }

    int main(void)
    {
        for (;;)
        {
            main_loop();
        }
    }

Il y a différentes variantes de boucles infinies:

.. code-block:: c

    for (;;) { }

    while (true) { }

    do { } while (true);

Notions que l'expression ``while (1)`` que l'on rencontre fréquemment dans des exemples est fausse syntaxiquement. Une condition de validité devrait être un booléen, soit vrai, soit faux. Or, la valeur scalaire ``1`` devrait préalablement être transformée en une valeur booléenne. Il est donc plus juste d'écrire ``while (1 == 1)`` ou simplement ``while (true)``.

On préférera néanmoins l'écriture ``for (;;)`` qui ne fait pas intervenir de conditions extérieure car en effet, avant **C99** définir la valeur ``true`` était à la charge du développeur et on pourrait s'imaginer cette plaisanterie de mauvais goût:

.. code-block:: c

    _Bool true = 0;

    while (true) { /* ... */ }

Lorsque l'on a besoin d'une boucle infinie il est généralement préférable de permettre au programme de se terminer correctement lorsqu'il est interrompu par le signal **SIGINT** (c.f. :numref:`signals`). On rajoute alors une condition de sortie à la boucle principale:

.. code-block:: c

    #include <stdlib.h>
    #include <signal.h>
    #include <stdbool.h>

    static volatile bool is_running = true;

    void sigint_handler(int dummy)
    {
        is_running = false;
    }

    int main(void)
    {
        signal(SIGINT, sigint_handler);

        while (is_running)
        {
           /* ... */
        }

        return EXIT_SUCCESS;
    }

Les sauts
=========

Il existe 4 instructions en C permettant de contrôler le déroulement de
l'exécution d'un programme. Elle déclanchent un saut inconditionnel à un autre endroit du programme.

- ``break`` interrompt la structure de contrôle en cours. Elle est valide pour:
    - ``while``
    - ``do``...``while``
    - ``switch``
- ``continue``: saute un tour d'exécution dans une boucle
- ``goto``: interrompt l'exécution et saute à un label situé ailleurs dans la fonction
- ``return``

``goto``
--------

Il s'agit de l'instruction la plus controversée en C. Cherchez sur internet et les détracteurs sont nombreux, et ils ont partiellement raison car dans la très vaste majorité des cas ou vous pensez avoir besoin de ``goto``, une autre solution plus élégente existe.

Néanmoins, il est importante de comprendre que ``goto`` était dans certain langage de prorgramation comme BASIC, la seule structure de contrôle disponible permettant de faire des saut. Elle est par ailleurs le reflet du langage machine car la plupart des processeurs ne connaissent que cette instruction souvent appellée ``JUMP``. Il est par conséquent possible d'immiter le comportement de n'importe quelle structure de contrôle si l'on dispose de ``if`` et de ``goto``.

``goto`` effectue un saut inconditionnel à un *label* défini en C par un :ref:`identificateur <identifiers>` suivi d'un ``:``.

L'un des seul cas de figure autorisé est celui d'un traitement d'erreur centralisé lorsque de multiples points de retours existent dans une fonction ceci évitant de répéter du code:

.. code-block::

    #include <time.h>

    int parse_message(int message)
    {
        struct tm *t = localtime(time(NULL));
        if (t->tm_hour < 7) {
            goto error;
        }

        if (message > 1000) {
            goto error;
        }

        /* ... */

        return 0;

        error:
            printf("ERROR: Une erreur a été commise\n");
            return -1;
    }

``continue``
------------

Le mot clé ``continue`` ne peut exister qu'à l'intérieur d'une boucle. Il permet d'interrompre le cycle en cours et directement passer au cycle suivant.

.. code-block:: c

    uint8_t airplane_seat = 100;

    while (--airplane_seat)
    {
        if (airplane_seat == 13) {
            continue;
        }

        printf("Dans cet avion il y a un siège numéro %d\n", airplane_seat);
    }

Cette structure est équivalente à l'utilisation d'un goto avec un label placé à la fin de la séquence de boucle, mais promettez-moi que vous n'utiliserez jamais cet exemple:

.. code-block:: c

    while (true)
    {
        if (condition) {
            goto contin;
        }

        /* ... */

        contin:
    }

``break``
---------

Le mot-clé ``break`` peut être utilisé dans une boucle ou dans un ``switch``. Il permet d'interrompre l'execution de la boucle ou de la structure ``switch`` la plus proche. Nous avions déjà évoqué l'utilisation dans un ``switch`` (c.f. :numref:`switch`).


``return``
----------

Le mot clé ``return`` suivi d'une valeur de retour ne peut apparaître que dans une fonction dont le type de retour n'est pas ``void``. Ce mot-clé permet de stopper l'exécution d'une fonction et de retourner à son point d'appel.

.. code-block:: c
    :emphasize-lines: 8

    void unlock(int password)
    {
        static tries = 0;

        if (password == 4710 /* MacGuyver: A Retrospective 1986 */) {
            open_door();
            tries = 0;
            return;
        }

        if (tries++ == 3)
        {
            alert_security_guards();
        }
    }

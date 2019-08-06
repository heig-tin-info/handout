=========
Exercices
=========

.. exercise:: Date

    Lors du formattage d'une date, on y peut y lire ``%w``, par quoi sera remplacé ce *token* ?

.. exercise:: Arc-cosinus

    La fonction Arc-Cosinus ``acos`` est-elle définie par le standard et dans quel fichier d'en-tête est-elle déclarée? Un fichier d'en-tête se termine avec l'extension ``.h``.

    .. solution::

        En cherchant ``man acos header`` dans Google, on trouve que la fonction ``acos`` est définie dans le header ``<math.h>``.

        Une autre solution est d'utiliser sous Linux la commande ``apropos``:

        .. code-block:: console

            $ apropos acos
            acos (3)     - arc cosine function
            acosf (3)    - arc cosine function
            acosh (3)    - inverse hyperbolic cosine function
            acoshf (3)   - inverse hyperbolic cosine function
            acoshl (3)   - inverse hyperbolic cosine function
            acosl (3)    - arc cosine function
            cacos (3)    - complex arc cosine
            cacosf (3)   - complex arc cosine
            cacosh (3)   - complex arc hyperbolic cosine
            cacoshf (3)  - complex arc hyperbolic cosine
            cacoshl (3)  - complex arc hyperbolic cosine
            cacosl (3)   - complex arc cosine

        Le premier résultat permet ensuite de voir:

        .. code-block:: console

            $ man acos | head -10
            ACOS(3)    Linux Programmer's Manual         ACOS(3)

            NAME
                acos, acosf, acosl - arc cosine function

            SYNOPSIS
                #include <math.h>

                double acos(double x);
                float acosf(float x);

        La réponse est donc `<math.h>`.

        Sous Windows avec Visual Studio, il suffit d'écrire ``acos`` dans un fichier source et d'appuyer sur ``F1``. L'IDE redirige l'utilisateur sur l'aide Microsoft `acos-acosf-acosl <https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acos-acosf-acosl>`__ qui indique que le header source est ``<math.h>``.

.. exercise:: Standardisation

    Ouvrez le standard `C99 <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf>`__ et cherchez la valeur maximale possible de la constante ``ULLONG_MAX``. Que vaut-elle ?

    .. solution::

        Au paragraphe §5.2.4.2.1-1 on peut lire que ``ULLONG_MAX`` est encodé sur 64-bits et donc que sa valeur est :math:`2^{64}-1` donc `18'446'744'073'709'551'615`.

.. exercise:: Précision des flottants

    Que vaut ``x``?

    .. code-block:: c

        float x = 10000000. + 0.1;

    .. solution::

        Le format float est stocké sur 32-bits avec 23-bits de mantisse et 8-bits d'exposants. Sa précision est donc limitée à environ 6 décimales. Pour représenter 10'000'000.1 il faut plus que 6 décimales et l'addition est donc caduc:

        .. code-block:: c

            #include <stdio.h>

            int main(void) {
                float x = 10000000. + 0.1;
                printf("%f\n", x);
            }

        .. code-block:: console

            $ ./a.out
            10000000.000000

.. exercise:: Pêche

    Combien y-a-t-il eu de questions posées en C sur le site Stack Overflow?

    .. solution::

        Il suffit pour cela de se rendre sur le site de `Stackoverflow <https://stackoverflow.com/tags/c>` et d'accéder à la liste des tags. En 2019/07 il y eut 307'669 questions posées.

        Seriez-vous capable de répondre à une question posée?

.. exercise:: Eclipse

    Un ami vous parle d'un outil utilisé pour le développement logiciel nommé **Eclipse**. De quel type d'outil s'agit-il ?

    .. solution::

        `Eclipse <https://www.eclipse.org/ide/>`__ est un IDE. Il n'intègre donc pas de chaîne de compilation et donc aucun compilateur.

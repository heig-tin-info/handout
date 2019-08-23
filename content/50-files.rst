============
Les fichiers
============

Système de fichiers
===================

Dans un environnement POSIX tout est fichier. ``stdin`` est un fichier, une souris USB est un fichier, un clavier est un fichier, un terminal est un fichier, un programme est un fichier.

Les fichiers sont organisés dans une arborescence gérée par un `système de fichiers <https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_fichiers>`__. Sous Windows l'arborescence classique est:

.. code-block:: console

    C:
    ├── Program Files         Programmes installés
    ├── Users                 Comptes utilisateur
    │   └── John
    │       ├── Desktop
    │       ├── Documents
    │       └── Music
    └── Windows
        ├── Fonts             Polices de caractères
        ├── System32          Système d'exploitation 64-bits (oui, oui)
        └── Temp              Fichiers temporaires

Il y a une arborescence par disque physique ``C:``, ``D:``, une arborescence par chemin réseau ``\\eistore2``, etc. Sous POSIX, la stratégie est différente, car il n'existe qu'UN SEUL système de fichier dont la racine est ``/``.

.. code-block:: console

    /
    ├── bin                   Programmes exécutables cruciaux
    ├── dev                   Périphériques (clavier, souris, ...)
    ├── usr
    │   └── bin               Programmes installés
    ├── mnt                   Points de montage (disques réseaux, CD, clé USB)
    │   └── eistore2
    ├── tmp                   Fichiers temporaires
    ├── home                  Comptes utilisateurs
    │   └── john
    │       └── documents
    └── var                   Fichiers variables comme les logs ou les database

Chaque élément qui contient d'autres éléments est appelé un **répertoire** ou **dossier**, en anglais *directory*. Chaque répertoire contient toujours au minimum deux fichiers spéciaux:

``.``
    Un fichier qui symbolise le répertoire courant, celui dans lequel je me trouve

``..``
    Un fichier qui symbolise le répertoire parent, c'est à dire ``home`` lorsque je suis dans ``john``.

La localisation d'un fichier au sein d'un système de fichier peut être soit **absolue** soit **relative**. Cette localisation s'appelle un **chemin** ou *path*. La convention est d'utiliser le symbole:

- Slash ``/`` sous POSIX
- Antislash ``\`` sous Windows

Le chemin ``/usr/bin/.././bin/../../home/john/documents`` est correct mais il n'est pas `canonique <https://fr.wikipedia.org/wiki/Canonique_(math%C3%A9matiques)>`__. La forme canonique est ``/home/john/documents``. Un chemin peut être relatif s'il ne commence pas par un ``/``: ``../bin``. Sous Windows c'est pareil mais la racine différemment selon le type de média ``C:\``, ``\\network``, ...

Lorsqu'un programme s'exécute, son contexte d'exécution est toujours par rapport à son emplacement dans le système de fichier donc le chemin peut être soit relatif, soit absolu.

Format d'un fichier
===================

Un fichier peut avoir un contenu arbitraire; une suite de zéros et de uns binaire. Selon l'interprétation, un fichier pourrait contenir une image, un texte ou un programme. Le cas particulier ou le contenu est lisible par un éditeur de texte, on appelle ce fichier un `fichier texte <https://fr.wikipedia.org/wiki/Fichier_texte>`__. C'est-à-dire que chaque caractère est encodé sur 8-bit et que la table ASCII est utilisée pour traduire le contenu en un texte intelligible. Lorsque le contenu n'est pas du texte, on l'appelle un `fichier binaire <https://fr.wikipedia.org/wiki/Fichier_binaire>`__.

La frontière est parfois assez mince, car parfois le fichier binaire peut contenir du texte intelligible, la preuve avec ce programme:

.. code-block:: c

    #include <stdio.h>
    #include <string.h>

    int main(char* argc, char** argv)
    {
        static const char password[] = "un mot de passe secret";
        return strcmp(argv[1], password);
    }

Si nous le compilons et cherchons dans son code binaire:

.. code-block::

    $ gcc example.c
    $ hexdump -C a.out | grep -C3 sec
    000006f0  f3 c3 00 00 48 83 ec 08  48 83 c4 08 c3 00 00 00  |....H...H.......|
    00000700  01 00 02 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
    00000710  75 6e 20 6d 6f 74 20 64  65 20 70 61 73 73 65 20  |un mot de passe |
    00000720  73 65 63 72 65 74 00 00  01 1b 03 3b 3c 00 00 00  |secret.....;<...|
    00000730  06 00 00 00 e8 fd ff ff  88 00 00 00 08 fe ff ff  |................|
    00000740  b0 00 00 00 18 fe ff ff  58 00 00 00 22 ff ff ff  |........X..."...|
    00000750  c8 00 00 00 58 ff ff ff  e8 00 00 00 c8 ff ff ff  |....X...........|

Sous un système POSIX, il n'existe aucune distinction formelle entre un fichier binaire et un fichier texte. En revanche sous Windows il existe une subtile différence concernant surtout le caractère de fin de ligne. La commande ``copy a.txt + b.txt c.txt`` considère des fichiers textes et ajoutera automatiquement une fin de ligne entre chaque partie concaténée, mais celle-ci ``copy /b a.bin + b.bin c.bin`` ne le fera pas.

Ouverture d'un fichier
======================

Sous POSIX, un programme doit demander au système d'exploitation l'accès à un fichier soit en lecture, soit en écriture soit les deux. Le système d'exploitation retourne un descripteur de fichier qui est simplement un entier unique pour le programme.

.. code-block:: c

    #include <fcntl.h>
    #include <stdio.h>
    #include <sys/stat.h>

    int main(void)
    {
        int fd = open("toto", O_RDONLY);
        printf("%d\n", fd);
        getchar();
    }

Lorsque le programme ci-dessus est exécuté, il va demander l'ouverture du fichier ``toto`` en lecture et recevoir un descripteur de fichier ``fd`` (*file descriptor*) positif en cas de succès ou négatif en cas d'erreur.

Dans l'exemple suivant, on compile, puis exécute en arrière-plan le programme qui ne se terminera pas puisqu'il attend un caractère d'entrée. L'appel au programme ``ps`` permet de lister la liste des processus en cours et la recherche de ``test`` permet de noter le numéro du processus, ici ``6690``. Dans l'arborescence de fichiers, il est possible d'aller consulter les descripteurs de fichiers ouverts pour le processus concerné.

.. code-block:: console

    $ gcc test.c -o test && ./test &
    $ ps -u | grep test
    ycr       6690  0.0  0.0  10540   556 pts/4    T    11:19   0:00 test
    $ ls /proc/6690/fd
    0  1  2  3

On observe que trois descripteurs de fichiers sont ouverts.

- ``0`` pour ``STDIN``
- ``1`` pour ``STDOUT``
- ``2`` pour ``STDERR``
- ``3`` pour le fichier ``toto`` ouvert en lecture seule

La fonction ``open`` est en réalité un appel système qui n'est standardisé que sous POSIX, c'est-à-dire que son utilisation n'est pas portable. L'exemple cité est principalement évoqué pour mieux comprendre le mécanisme de fond pour l'accès aux fichiers.

En réalité la bibliothèque standard, respectueuse de C99, dispose d'une fonction ``fopen`` pour *file open* qui offre plus de fonctionnalités. Ouvrir un fichier se résume donc à

.. code-block:: c

    #include <stdio.h>

    int main(void)
    {
        FILE *fp = fopen("toto", "r");

        if (fp == NULL) {
            return -1; // Error the file cannot be accessed
        }

        // ...
    }

Le mode d'ouverture du fichier peut être:

``r``
    Ouverture en lecture seule depuis le début du fichier.

``r+``
    Ouverture pour lecture et écriture depuis le début du fichier.

``w``
    Ouverture en écriture. Le fichier est créé s'il n'existe pas déjà, sinon le contenu est effacé. Le pointeur de fichier est positionné au début de ce dernier.

``w+``
    Ouverture en écriture et lecture. Le fichier est créé s'il n'existe pas déjà. Le pointeur de fichier est positionné au début de ce dernier.

``a``
    Ouverture du fichier pour insertion. Le fichier est créé s'il n'existe pas déjà. Le pointeur est positionné à la fin du fichier.

``a+``
    Ouverture du fichier pour lecture et écriture. Le fichier est créé s'il n'existe pas déjà et le pointeur du fichier est positionné à la fin.

Sous Windows et pour soucis de compatibilité, selon la norme C99, le flag ``b`` pour *binary* existe. Pour ouvrir un fichier en mode binaire on peut alors écrire ``rb+``.

L'ouverture d'un fichier cause, selon le mode, un accès exclusif au fichier. C'est-à-dire que d'autres programmes ne pourront pas accéder à ce fichier. Il est donc essentiel de toujours refermer l'accès à un fichier dès lors que l'opération de lecture ou d'écriture est terminée:

.. code-block:: c

    flose(fp);

On peut noter que sous POSIX, écrire sur ``stdout`` ou ``stderr`` est exactement la même chose qu'écrire sur un fichier, il n'y a aucune distinction.

Navigation dans un fichier
==========================

Lorsqu'un fichier est ouvert, un curseur virtuel est positionné soit au début soit à la fin du fichier. Lorsque des données sont lues ou écrites, c'est à la position de ce curseur, lequel peut être déplacé en utilisant plusieurs fonctions utilitaires.

La navigation dans un fichier n'est possible que si le fichier est *seekable*. Généralement les pointeurs de fichiers ``stdout`` et ``stderr`` ne sont pas *seekable*, et il n'est pas possible de se déplacer dans le fichier mais seulement écrire dedans.

fseek
-----

.. code-block:: c

    int fseek(FILE *stream, long int offset, int whence)

Le manuel `man fseek <http://man7.org/linux/man-pages/man3/fseek.3.html>`__ indique les trois constantes possibles pour ``whence``:

``SEEK_SET``
    Positionne le curseur au début du fichier.

``SEEK_CUR``
    Position courante du curseur. Permets d'ajouter un offset relatif à la position courante.

``SEEK_END``
    Positionne le curseur à la fin du fichier.

ftell
-----

Il est parfois utile de savoir où se trouve le curseur. ``ftell()`` retourne la position actuelle du curseur dans un fichier ouvert.

.. code-block:: c

    char filename[] = "foo";

    FILE *fp = fopen(filename, 'r');
    fseek(fp, 0, SEEK_END);
    long int size = ftell();

    printf("The file %s has a size of %ld Bytes\n", filename, size);

rewind
------

L'appel ``rewind()`` est équivalent à ``(void) fseek(stream, 0L, SEEK_SET)`` et permet de se positionner au début du fichier.

Lecture / Écriture
==================

La lecture, écriture dans un fichier s'effectue de manière analogue aux fonctions que nous avons déjà vues ``printf`` et ``scanf`` pour les flux standards (*stdout*, *stderr*), mais en utilisant les pendants fichiers:

``int fscanf(FILE *stream, const char *format, ...)``
    Équivalent à ``scanf`` mais pour les fichiers

``int fprintf(FILE *stream, const char *format, ...)``
    Équivalent à ``printf`` mais pour les fichiers

``int fgetc(FILE *stream)``
    Équivalent à ``getchar`` (ISO/IEC 9899 §7.19.7.6-2)

``int fputc(FILE *stream, char char)``
    Équivalent à ``putchar`` (ISO/IEC 9899 §7.19.7.9-2)

``char *fgets(char * restrict s, int n, FILE * restrict stream)``
    Équivalent à ``gets``

``int fputs(const char * restrict s, FILE * restrict stream)``
    Équivalent à ``puts``

Bref... Vous avez compris.

Les nouvelles fonctions à connaître sont les suivantes:

``size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream)``
    Lecture arbitraire de ``nmemb * size`` bytes depuis le flux ``stream`` dans le buffer ``ptr``:

    .. code-block:: c

        int32_t buffer[12] = {0};
        fread(buffer, 2, sizeof(int32_t), stdin);

        printf("%x\n%x\n", buffer[0], buffer[1]);

    .. code-block:: console

        $ echo -e "0123abcdefgh" | ./a.out
        33323130
        64636261

    On notera au passage la nature *little-endian* du système.

``size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream)``

    La fonction est similaire à ``fread`` mais pour écrire sur un flux.

Buffer de fichier
=================

Pour améliorer les performances, C99 prévoit (§7.19.3-3), un espace tampon pour les descripteurs de fichiers qui peuvent être:

``unbuffered`` (``_IONBF``)
    Pas de buffer, les caractères lus ou écrits sont acheminés le plus vite possible de la source à la destination.

``fully buffered`` (``_IOFBF``)


``line buffered`` (``_IO_LBF``)

Il faut comprendre qu'à chaque instant un programme souhaite écrire dans un fichier, il doit générer un appel système et donc interrompre le noyau. Un programme qui écrirait caractère par caractère sur la sortie standard agirait de la même manière qu'un employé des postes qui irait distribuer son courrier en ne prenant qu'une enveloppe à la fois, de la centrale de distribution au destinataire.

Par défaut, un pointeur de fichier est *fully buffered*. C'est-à-dire que dans le cas du programme suivant devrait exécuter 10x l'appel système ``write``, une fois par caractère.

.. code-block:: c

    #include <stdio.h>
    #include <string.h>

    int main(int argc, char* argv[])
    {
        if (argc > 1 && strcmp("--no-buffering", argv[1]) == 0)
            setvbuf(stdout, NULL, _IONBF, 0);

        for (int i = 0; i < 10; i++)
            putchar('c');
    }

Cependant le comportement réel est différent. Seulement si le buffer est désactivé que le programme interrompt le noyau pour chaque caractère:

.. code-block:: console

    $ gcc buftest.c -o buftest

    $ strace ./buftest 2>&1 | grep write
    write(1, "cccccccccc", 10cccccccccc)              = 10

    $ strace ./buftest --no-buffering 2>&1 | grep write
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1
    write(1, "c", 1c)                        = 1

Le changement de mode peut être effectué avec la fonction ``setbuf`` ou ``setvbuf``:

.. code-block:: c

    #include <stdio.h>

    int main(void) {
        char buf[1024];

        setbuf(stdout, buf);

        fputs("Allo ?");

        fflush(stdout);
    }

La fonction ``fflush`` force l'écriture malgré l'utilisation d'un buffer.

-----

.. exercise:: Variantes

    Considérez les deux programmes ci-dessous très similaires.

    .. code-block:: c

        #include <stdio.h>

        int main(void)
        {
            char texte[80];

            printf("Saisir un texte:");
            gets(texte);
            printf("Texte: %s\n", texte);
        }

    .. code-block:: c

        #include <stdio.h>

        int main(void)
        {
            char texte[80];

            printf("Saisir un texte:");
            fgets(texte, 80, stdin);
            printf("Texte: %s\n", texte);
        }

    #. Quelle est la différence  entre ces 2 programmes ?
    #. Dans quel cas est-ce que ces programmes auront un comportement différent ?
    #. Quelle serait la meilleure solution ?

.. exercise:: Numéro de ligne

    Écrire un programme qui saisit le nom d'un fichier texte, ainsi qu'un texte à rechercher. Le programme affiche ensuite le numéro de toutes les lignes du fichier contenant le texte recherché.

    .. code-block:: console

        $ ./search
        Fichier: foo.txt
        Recherche: bulbe

        4
        5
        19
        132
        981

    Question subsidiaire: que fait le programme suivant:

    .. code-block:: console

        $ grep foo.txt bulbe

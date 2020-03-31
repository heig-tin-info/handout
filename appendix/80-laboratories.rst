============
Laboratoires
============

Les laboratoires sont des travaux pratiques permettant à l'étudiant d'attaquer des problèmes de programmation plus difficiles que les exercices faits en classe.

Protocole
=========

1. Récupérer le référentiel du laboratoire en utilisant GitHub Classroom.
2. Prendre connaissance du cahier des charges.
3. Rédiger le code.
4. Le tester.
5. Le soumettre avant la date butoire.

Evaluation
==========

Une grille d'évaluation est intégrée à tous les laboratoires. Elle prends la forme d'un fichier ``criteria.yml`` que l'étudiant peut consulter en tout temps.

Directives
==========

- La recherche sur internet est autorisée et conseillée.
- Le plagia n'est pas autorisé, et sanctionné si découvert par la note de 1.0.
- Le rendu passé la date butoire est sanctionné à raison de 1 point puis 1/24 de point par heure de retard.

Format de rendu
===============

- Fin de lignes: ``LF`` (``'\n'``).
- Encodage: UTF-8 sans BOM.
- Code source respectueux de ISO/IEC 9899:1999.
- Le code doit comporter un exemple d'utilisation et une documentation mise à jour dans ``README.md``.
- Lorsqu'un rapport est demandé vous le placerez dans ``REPORT.md``.

Makefile et Visual Studio Code
==============================

Vous pouvez vous inspirer de ce ``Makefile`` générique. N'oubliez pas que la tabulation dans un Makefile doit être le caractère tabulation (pas des espaces):

.. code:: make

    CSRCS=$(wildcard *.c)
    COBJS=$(patsubst %.c,%.o,$(CSRCS))
    EXEC=gallimard

    CFLAGS=-std=c99 -g -Wall -pedantic -pg
    LDFLAGS=-lm -pg

    all: $(EXEC)

    -include $(COBJS:.o=.d)

    $(EXEC): $(COBJS)
        $(CC) -o $@ $< $(LDFLAGS)

    %.o: %.c
        $(CC) -c $(CFLAGS) -o $@ $^ -MMD -MF $(@:.o=.d)

    clean:
        $(RM) $(EXEC) *.o a.out $(COBJS:.o=.d)

    prof:
        gprof -b $(EXEC) gmon.out

    .PHONY: all prof clean

Dans ce cas fichier ``launch.json`` ressemblera à ceci:

.. code:: json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "build project",
                "type": "cppdbg",
                "request": "launch",
                "program": "${fileDirname}/${fileBasenameNoExtension}",
                "args": ["proust.md"],
                "stopAtEntry": true,
                "cwd": "${workspaceFolder}",
                "environment": [],
                "externalConsole": false,
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ],
                "preLaunchTask": "make",
                "miDebuggerPath": "/usr/bin/gdb"
            }
        ]
    }

Et le fichier ``task.json``:

.. code:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "shell",
                "label": "make",
                "command": "make",
                "problemMatcher": [
                    "$gcc"
                ],
                "group": "build"
            }
        ]
    }

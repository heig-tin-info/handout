.. raw:: latex

    \appendix

==================
Visual Studio Code
==================

Visual Studio Code est un éditeur gratuit open-source développé par Microsoft. Il gagne en popularité et réuni les avantages d'être léger, multi-platforme et multi-langage.

Pour pouvoir l'utilser avec votre compilateur et écrire du C, il faut une configuration minimale.

Visual Studio Code n'a pas la notion de **projet** mais d'espace de travail **workspace**. Un espace de travail est simplement un répertoire. A l'intérieur de ce répertoire on y trouvera:

.. code-block::

    .
    ├── .vscode
    │   └── launch.json
    └── main.c

Visual Studio Code peut en général générer automatiquement le fichier ``.vscode/launch.json`` qui contient tout ce qu'il faut pour compiler et exécuter le programme:

.. code-block:: json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "gcc",
                "type": "cppdbg",
                "request": "launch",
                "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
                "args": [],
                "stopAtEntry": false,
                "cwd": "${workspaceFolder}",
                "environment": [],
                "externalConsole": false,
                "MIMode": "gdb",
                "miDebuggerPath": "C:\\ProgramData\\chocolatey\\lib\\mingw\\tools\\install\\mingw64\\bin\\gdb.exe",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ],
                "preLaunchTask": "gcc.exe build active file"
            }
        ]
    }

.. code-block:: json

    {
        "version": "2.0.0",
        "tasks": [
            {
                "type": "shell",
                "label": "gcc.exe build active file",
                "command": "C:\\ProgramData\\chocolatey\\lib\\mingw\\tools\\install\\mingw64\\bin\\gcc.exe",
                "args": [
                    "-g",
                    "${file}",
                    "-o",
                    "${fileDirname}\\${fileBasenameNoExtension}.exe"
                ],
                "options": {
                    "cwd": "C:\\ProgramData\\chocolatey\\lib\\mingw\\tools\\install\\mingw64\\bin"
                },
                "problemMatcher": [
                    "$gcc"
                ]
            }
        ]
    }
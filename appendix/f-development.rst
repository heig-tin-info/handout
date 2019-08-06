Environnement de développement
------------------------------

Si ce n'est pas déjà le cas, vous devriez disposer sur votre ordinateur d'un environnement de développement. Pour ce cours, vous êtes libre d'utiliser l'outil qui vous semble le plus pertinent mais il proposé d'utiliser un environnement POSIX qui est aujourd'hui le standard le plus établi et le plus largement utiilsé, des téléphones portables aux serveurs informatiques, aux Macbooks et aux fusées spatiales. L'autre consensus, également largement utilisé est Windows.

Pour disposer d'un environnement POSIX sous Windows il existe 3 solutions:

`MinGW <http://www.mingw.org/>`__
    Un environnement POSIX GNU pour Windows. La solution la plus facile.

`WSL Windows Subsystem for Linux <https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux>`__
    Une distribution Ubuntu pour Windows 10. La meilleure solution si vous voulez vous confronter à la ligne de commande et mieux comprendre le fonctionnement de Linux.

`Cygwin <http://www.cygwin.org/>`__
    Un émulateur POSIX pour Windows. Une excellente alternative aux autres solutions qui se fait peu à peu remplacer par WSL.

Pour installer le plus facilement votre environnement de développement, je vous recommande `Chocolatey <https://chocolatey.org/>`__, un gestionnaire de paquets pour Windows. Une fois l'outil installé, vous pouvez installer les paquets suivants:

.. code-block:: console

    C:\> choco install gcc
    C:\> choco install vscode
    C:\> choco install git

Ensuite vous pouvez exécuter ``Git Bash`` depuis le menu Démarrer et diposer d'une console comme si vous étiez sous Linux ou MacOSx.

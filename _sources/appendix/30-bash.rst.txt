
=================
Ligne de commande
=================


La maîtrise de la ligne de commande n'est pas indispensable pour ce cours mais la compréhension de quelques commandes est utile pour bien comprendre les exemples données. 

Dans un environnement **POSIX** l'interaction avec le système s'effectue pour la plupart du temps via un terminal. Le programme utilisé pour intéragir avec le système d'exploitation est appelé un `interpréteur de commande <https://en.wikipedia.org/wiki/Command-line_interface#Command-line_interpreter>`__. Sous Windows vous utilisez le programme ``cmd.exe`` ou ``PowerShell.exe``. Sous Linux vous utilisez très souvant un dérivé du `Bourne shell <https://en.wikipedia.org/wiki/Bourne_shell>`__ nom éponyme de `Stephen Bourne <https://en.wikipedia.org/wiki/Stephen_R._Bourne>`__ et apparu en 1979. La compatibilité est toujours maintenu aujourd'hui via son successeur `Bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`__ dont le nom est un acronyme de *Bourne-again shell*. 

Bash est écrit en C et les sources sont naturellement disponible sur internet. Lorsque vous lancez Bash vous aurez un simple prompt : 

.. code-block:: console

    $

Ce dernier vous invite à tapper une commande laquelle est le plus souvent le nom d'un programme. 

Pipe
----

.. code-block:: console

    $ cat foo.txt | hexdump -C -n100


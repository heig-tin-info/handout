Documentation automatique avec Doxygen
======================================

| La documentation d'un logiciel est toujours un point épineux car
  l'effort à mettre en œuvre pour l'écrire est loin d'être négligeable…
| L'outil gratuit et multi-plateforme Doxygen [1]_ permet de générer une
  documentation au format PDF ou sous la forme d'un site Internet à
  partir d'informations qui sont *embarquées* dans le code sous la forme
  de commentaires. Dès lors, une bonne pratique pour réaliser la
  documentation consiste à ajouter les commentaires nécessaires lors de
  l'écriture du code C lui-même. On gagne alors un temps précieux pour
  la réalisation de la documentation du code !

Page principale de la documentation
-----------------------------------

Pour documenter la page d'introduction du logiiel, on placera au début
du fichier principal un commentaire comme ci-dessous.

.. code-block:: c

    /**
     * @mainpage Documentation of the labo 22 for INFO1.
     *
     * @section one Lab description
     *
     * The aim of this lab is to find the shortest path between to nodes.
     *
     * @section two Software architecture
     *
     * The architecture is based on the xxx algorithm....
     */

Documentation au niveau fichier (.c ou .h)
------------------------------------------

Pour documenter un fichier, on placera au début de ce fichier un
commentaire comme ci-dessous.

.. code-block:: c

    /**
     * main file for labo22 (INFO1).
     * @author Pierre BRESSY
     * @version 1.0
     * @date Tue Sep  5 11:24:08 2017
     */

Documentation au niveau fonction
--------------------------------

Pour documenter une fonction, on placera avant la fonction un
commentaire comme ci-dessous.

.. code-block:: c

    /**
     * Entry point of labo22.
     * @param[in] argc is the number of arguments of the software (included the software itself)
     * @param[in] argv is the table of arguments of the software
     * @return a integer value
     */
    int main(int argc, char const *argv[])
    {
        puts("INFO1 - Lab22");
        return 0;
    }

Documentation d'un type structuré
---------------------------------

Pour documenter un type structuré, on placera avant la fonction un
commentaire comme ci-dessous.

.. code-block:: c

    /**
     * structure for 2D point management.
     *
     * s2DPoint contains the x and y coordinates of a point (real values)
     */
    typedef struct {
       double x;  /*!< coordinate of the point along the X axis */
       double y;  /*!< coordinate of the point along the Y axis */
    } s2DPoint;

Documentation d'un type enumérés
--------------------------------

Pour documenter un type enumérés, on placera avant la fonction un
commentaire comme ci-dessous.

.. code-block:: c

    /**
     * list of possible errors.
     *
     * eErrorCode is the list a all possible errors for this software
     */
    typedef enum {
       E_NO_ERROR,  /*!< no error at all */
       E_ERR_OPEN_FILE,   /*!< error while opening file */
       E_ERR_WRITING_FILE,   /*!< error while writing file */
       E_ERR_READING_FILE   /*!< error while readin file */
    } eErrorCode;

Documentation d'un symbole du préprocesseur
-------------------------------------------

Pour documenter un symbole du préprocesseur, on placera avant la
fonction un commentaire comme ci-dessous.

.. code-block:: c

    /**
     * preprocessor symbol for the THE_ANSWER.
     *
     * This symbol is the value of the answer
     */
    #define THE_ANSWER 42

Documentation d'une macro
-------------------------

Pour documenter une macro, on placera avant la fonction un commentaire
comme ci-dessous.

.. code-block:: c

    /**
     * macro to get the maximum value from a and b
     * @param a first value for maximum evaluation
     * @param b second value for maximum evaluation
     *
     * This macro returns the maxium value between a and b
     */
    #define MAX(a,b) ( (a)>(b) ? (a):(b) )

.. [1]
   Doxygen est téléchargeable depuis le site Internet
   http://www.doxygen.org


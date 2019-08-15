# TO-DO list

- [ ] Sphinx
    - [ ] Numbered section with letters for appendix
    - [ ] List figures
    - [ ] Numbered figures
    - [ ] Bibliography
    - [ ] Center les tables
    - [ ] Rename source file with ascending order
    - [ ] Numbered exercices
    - [ ] Display code-block with filename like https://docs.travis-ci.com/user/deployment/releases/
    - [ ] Code
        - [ ] Copy to clipboard icon
        - [ ] Build and run icon
- [ ] Sphinx Theme
    - [ ] Favicon in theme
    - [x] Center figures
    - [ ] Left title on sidebar, only center figures
    - [ ] Admonitions
    - [ ] Spacing on bullets
    - [ ] Menu déroulant pour toc-tree
- [ ] Custom
    - [ ] Rendu de la fiche d'unité
- [ ] Latex
    - [ ] LaTeX to PDF
- [ ] Advanced
    - [ ] Keep track of the hyperlinked used
- [ ] Bugs
    - [ ] Quotes in french
    - [ ] Navlink header: Contenu, Exercices, Annexes,

- [ ] Order wireless keyboard for students
    - Logitech K830 or K400
    - With touchpad
    - If possible in Bluetooth


# Propositions

- Examen
    - Mettre à disposition de l'étudiant un laptop pas cher avec un éditeur de texte basic (pas de réseau)
    - Facilite le rendu d'examen, facilite la correction
    - Eviter les scanf....

## Sphinx

### Custom section numbering

https://stackoverflow.com/questions/57271548/custom-section-numbering-in-sphinx
https://github.com/sphinx-doc/sphinx/issues/6614

```
.. toctree::
    :numbering: uppercase-letters
```

This change would mean to extend the `TocTreeCollector` class to support the toctree option it would be nice to supports the standard numbering formats:

```
A1, A2 A1.1, B, B1.1, B1.2...
1. 1.1. 1.1.1, 1.2.1...
```

### Custom span for the number

https://github.com/sphinx-doc/sphinx/issues/6613

### Exercice extension

- An exercise should be numbered by chapter: Exercise 5.1
- `.. exercise::` to start an exercise
- `.. solution::` to give the solution the exercises

Voir comment mettre les exercices sur quel chapitres.

# TO-DO list

- [ ] Sphinx
  - [ ] Missing character from _build/latex/main.log (japanese/korean)
  - [ ] Bibliography
  - [ ] Rename source file with ascending order
  - [ ] Display code-block with filename like https://docs.travis-ci.com/user/deployment/releases/
  - [ ] Code
      - [ ] Copy to clipboard icon
      - [ ] Build and run icon
- [ ] Sphinx Theme
  - [ ] Left title on sidebar, only center figures
  - [ ] Spacing on bullets
  - [ ] Menu déroulant pour toc-tree
- [ ] Custom
  - [ ] Rendu de la fiche d'unité
- [ ] Advanced
  - [ ] Keep track of the hyperlinked used
- [ ] Bugs
  - [ ] Quotes in french
  - [ ] Navlink header: Contenu, Exercices, Annexes,
- [ ] §3.3.3 ou exclusif : symbole ^ dans l'entête du tableau
- [ ] §3.3.4 complément à un : symbole ~ dans l'entête du tableau
- [ ] Page d'accueil LateX
- [ ] Article 12
- [ ] Enumeration vilaine (indentation)
- [ ] Exercice (environment exercice)
- [ ] Solutions des exercices
- [ ] Organisationd de l'ouvrage, conventions d'ecriture
- [ ] Logo C pour l'ingénieur : Atome, outil chirurgical
- [ ] Taille des figures
- [ ] Index italique et références
- [ ] Build from GitHub Actions
- [ ] Index at the end of document?
- [ ] Exercice thing...
- [ ] LaTeX pygments style
- [ ] Reduce PDF size (should be much smaller!)

## Exercices

- Chaque chapitre à des exercices:

```
Exercice 3.8

...

> Voir solution...(html only)
```

- La version PDF à une section "Solution des exercices"
- Sous section "Solutions du chapitre 8"
- Puis "Exercice 8.2"

## Sphinx

### Custom section numbering

https://stackoverflow.com/questions/57271548/custom-section-numbering-in-sphinx
https://github.com/sphinx-doc/sphinx/issues/6614

```rst
.. toctree::
    :numbering: uppercase-letters
```

This change would mean to extend the `TocTreeCollector` class to support the toctree option it would be nice to supports the standard numbering formats:

```text
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

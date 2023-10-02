# Classe

# Fiches d'unités de cours

Les fiches d'unités sont les documents de référence pour les cours d'info1 et d'info2, ici présentées sous forme de données brutes au format **YAML**.





## Modalités d'évaluation et de validation

Le cours se compose de :

- Travaux écrits notés (coefficient 100%)
- Quiz notés ou non (coefficient 10% ou 0%)
- Séries d'exercices
- Travaux pratiques, 2 à 3 labos notés (laboratoires)
- Labo test noté comptabilisé comme un labo

La note finale est donnée par l'expression :

$$
\text{final} =
\frac{
\sum\limits_{t=1}^\text{T}{\text{TE}_t} +
10\% \cdot \sum\limits_{q=1}^\text{Q}{\text{Quiz}_q}
}{
4 \cdot (\text{T} + 10\% \cdot \text{Q})
}
+
\frac{1}{4 L}
\sum\limits_{l=1}^L
\text{Labo}_l
+
\frac{1}{2}
\text{Exam}
$$

L'équivalent en C :

```c
#define QUIZ_WEIGHT (.1) // Percent
#define EXAM_WEIGHT (.5) // Percent

typedef struct notes {
    size_t size;
    float values[];
} Notes;

float sum(Notes *notes) {
    float s = 0;
    for (int i = 0; i < notes->size; i++)
        s += notes->values[i];
    return s;
}

float mark(Notes tes, Notes quizzes, Notes labs, float exam) {
    return (
    sum(tes) + QUIZ_WEIGHT * sum(quizzes)
    ) / (
        (EXAM_WEIGHT / 2.) * (tes.size + QUIZ_WEIGHT * quizzes.size)
    ) +
            (EXAM_WEIGHT / 2.) * sum(labs) / labs.size +
        EXAM_WEIGHT * exam;
}
```

Les règles sont :

- En cas d'absence à un quiz, la note de 1.0 est donnée.
- En cas de plagiat, le [dilemme du prisonnier](https://fr.wikipedia.org/wiki/Dilemme_du_prisonnier#:~:text=Le%20dilemme%20du%20prisonnier%2C%20%C3%A9nonc%C3%A9,est%20jou%C3%A9%20qu'une%20fois.) s'applique.
- Le quiz le plus mauvais ne compte pas.


```{toctree}
:caption: Classe

laboratories
info1
info2
summary
```
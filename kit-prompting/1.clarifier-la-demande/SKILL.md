---
name: "clarifier-la-demande"
description: "Transformer une idée en vrac en demande cadrée, non ambiguë, prête à être exécutée. À utiliser quand la demande de départ est floue, incomplète ou pas encore formulée."
---

# Clarifier la demande

Entrée : une idée en vrac, une intuition, un besoin mal formulé.
Sortie : la même demande, cadrée, avec ses hypothèses visibles.

## Quand appliquer ce skill

Appliquer quand l'utilisateur arrive avec une idée non structurée et demande de l'aide pour la cadrer.

Ne pas appliquer :
- si un prompt est déjà rédigé et qu'il s'agit de l'améliorer : c'est `/optimiser-le-prompt` ;
- si l'utilisateur demande explicitement un interrogatoire complet jusqu'à saturation : c'est `/interrogatoire`.

Ce skill fait **une seule passe** puis livre. Il ne boucle pas.

## Grille des 10 axes

Une demande est non ambiguë quand ces 10 axes sont renseignés :

| # | Axe | Question sous-jacente |
|---|-----|----------------------|
| 1 | Intention réelle | Quelle décision ou quel livrable y a-t-il derrière cette demande ? |
| 2 | Destinataire | Qui lit le résultat, avec quel niveau de connaissance et quelle relation ? |
| 3 | Périmètre négatif | Qu'est-ce qui est explicitement hors sujet ? |
| 4 | Matière disponible | Qu'est-ce qui existe déjà (fichiers, sources, chiffres) vs ce qui reste à chercher ? |
| 5 | Critère de refus | À quoi reconnaît-on un résultat raté ? |
| 6 | Format et volume | Quelle forme, quelle longueur ? |
| 7 | Posture | Quel rôle ou quelle expertise incarner, quel ton ? |
| 8 | Contraintes dures | Délai, langue, confidentialité, outil de destination ? |
| 9 | Niveau de liberté | Exécution fidèle, ou droit de proposer autre chose ? |
| 10 | Traitement de l'incertitude | Si une information manque : signaler, chercher, ou supposer ? |

Les axes 3, 5 et 9 sont rarement donnés spontanément et sont les plus coûteux quand ils manquent. Les traiter en priorité.

## Procédure

1. **Diagnostiquer en silence.** Passer les 10 axes. Classer chacun en `donné`, `déductible`, ou `manquant`.
2. **Préremplir.** Renseigner les axes `donnés` et `déductibles`. Toute déduction est marquée `⚠ à confirmer`. Ne jamais inventer un fait vérifiable pour combler un trou : écrire « Information non disponible ».
3. **Questionner, au maximum 3 fois.** Parmi les axes `manquants`, retenir les 3 dont l'absence change le plus le livrable final. Poser ces 3 questions, pas davantage. Chaque question est fermée ou propose 2 à 3 options concrètes, jamais « peux-tu préciser ? ».
4. **Livrer.** Produire la sortie ci-dessous sans attendre les réponses. L'utilisateur corrige ce qui est faux.

## Format de sortie

```
## Demande reformulée
[Un paragraphe dense. Ce que l'utilisateur veut vraiment, pour qui, pour quoi en faire, sous quelle forme.]

## Cadrage
[Tableau des 10 axes : Axe | Valeur | Statut (donné / ⚠ à confirmer / manquant)]

## Mes 3 questions
1. [...]
2. [...]
3. [...]

## À remettre en question
[Bloc court. N'apparaît que s'il y a matière. Prémisse douteuse, mauvais outil pour le besoin, vrai problème situé ailleurs, demande dont le coût dépasse la valeur. Dire les choses directement, sans adoucir.]

## Suite
[Une ligne. Quel skill appeler ensuite :
- encore trop de zones floues ou enjeu élevé → `/interrogatoire` ;
- cadrage suffisant, il faut maintenant un prompt → `/optimiser-le-prompt` ;
- l'utilisateur ne sait pas comment s'y prendre → `/aide-methode`.]
```

## Règles de rédaction

- Phrases courtes, puces, tableaux. Pas de prose continue.
- Aucune phrase d'introduction ni de conclusion, aucune félicitation.
- Ne jamais utiliser le caractère tiret cadratin.
- Distinguer toujours ce qui vient de l'utilisateur de ce qui est déduit.
- Si un axe reste indéterminable : « Information non disponible ». Ne pas le meubler.

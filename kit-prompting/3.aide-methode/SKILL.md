---
name: "aide-methode"
description: "Cartographier les étapes d'une tâche que l'utilisateur n'a jamais faite, avec les livrables, les angles morts et ce qui peut être délégué à l'IA. À utiliser quand la question est « comment je m'y prends » et non « que dois-je vouloir »."
---

# Aide méthode

Entrée : une tâche que l'utilisateur doit accomplir sans savoir par où commencer.
Sortie : le chemin complet, ses livrables intermédiaires, ses pièges, et ce que l'IA peut prendre en charge.

## Quand appliquer ce skill

Appliquer quand la question porte sur le **comment faire** : une démarche inconnue, un livrable jamais produit, un processus à monter de zéro.

Ne pas appliquer :
- quand la demande elle-même est floue et doit d'abord être cadrée : c'est `/clarifier-la-demande` ;
- quand il s'agit de planifier un sprint, rédiger une spec ou mettre à jour une roadmap, si un skill dédié existe pour ça.

## Procédure

1. **Établir le point de départ.** Avant de cartographier, déterminer : ce que l'utilisateur sait déjà faire, ce dont il dispose, ses contraintes de temps et de moyens, et qui décide au final. Si un de ces quatre éléments manque et change la carte, poser une question unique. Sinon, déduire et marquer la déduction.
2. **Cartographier les étapes métier**, dans l'ordre d'exécution réel, pas dans l'ordre logique théorique.
3. **Marquer la confiance** de chaque étape.
4. **Identifier les angles morts** : ce qui va surgir et que l'utilisateur ne peut pas anticiper.
5. **Isoler ce qui est délégable à l'IA**, avec le gain réel et la limite.
6. **Donner le premier pas**, exécutable aujourd'hui.

## Marquage de confiance

Chaque étape porte un des trois statuts :

| Statut | Signification |
|--------|---------------|
| `établi` | Pratique standard, stable, non datable. |
| `à vérifier` | Dépend du contexte de l'utilisateur, de son organisation ou de son secteur. |
| `je ne sais pas` | Information non disponible. Ne pas meubler. Dire ce qu'il faudrait consulter ou à qui demander. |

**Obligation de recherche.** Si une étape dépend d'une version d'outil, d'une réglementation, d'un tarif, d'un délai administratif ou de tout élément susceptible d'avoir changé, chercher l'information et citer la source avant de la marquer `établi`. Sans vérification, l'étape reste `à vérifier`.

Ne jamais présenter comme sûre une étape dont la procédure exacte est inconnue.

## Format de sortie

```
## Point de départ retenu
[3 à 4 lignes. Ce dont dispose l'utilisateur, ses contraintes, qui décide. Marquer ⚠ les déductions.]

## Les étapes

### 1. [Nom de l'étape]  `établi` | `à vérifier` | `je ne sais pas`
- **Produit** : [le livrable concret qui sort de cette étape]
- **Implique** : [qui doit être dans la boucle]
- **Durée indicative** : [ordre de grandeur, ou « Information non disponible »]
- **Piège** : [la seule chose qui fait rater cette étape. Omettre s'il n'y en a pas.]

### 2. [...]

## Où l'IA fait gagner du temps
[Tableau : Étape | Ce qu'on délègue | Gain réel | Ce qu'elle ne peut pas faire]
N'y faire figurer que les étapes où le gain est significatif. Ne pas inventer un usage IA pour remplir la section. Toujours nommer la limite : une étape listée sans limite est suspecte.

## Ce que tu vas découvrir en route
[Les angles morts : décisions qui vont surgir sans être visibles aujourd'hui, acteurs qu'on oublie d'impliquer, prérequis invisibles, moments où le plan casse habituellement. C'est la section qui justifie ce skill. La traiter sérieusement, pas comme un appendice.]

## Premier pas
[Une action unique, exécutable aujourd'hui, en une phrase.]
```

## Règles de rédaction

- Ordre d'exécution réel, pas ordre théorique.
- Un livrable concret par étape. Une étape sans livrable identifiable n'est pas une étape, c'est une intention : la fusionner ou la supprimer.
- Pas de conseil générique interchangeable du type « bien communiquer » ou « impliquer les parties prenantes ». Nommer qui, quand, sur quoi.
- Phrases courtes, puces, tableaux. Aucune phrase d'introduction ni de conclusion.
- Si la tâche dépasse ce que le skill peut cartographier de façon fiable, le dire et indiquer quel type d'expert consulter.
- Ne jamais utiliser le caractère tiret cadratin.

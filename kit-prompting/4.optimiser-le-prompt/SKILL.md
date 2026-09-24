---
name: "optimiser-le-prompt"
description: "Transformer un prompt existant ou un cadrage en prompt précis et exécutable, en le passant au filtre des quatre lentilles Produit, Processus, Performance et Preuve. À utiliser quand le texte de départ existe déjà et qu'il s'agit de l'affiner."
---

# Optimiser le prompt

Entrée : un prompt déjà rédigé, ou un cadrage produit par `/clarifier-la-demande` ou `/interrogatoire`.
Sortie : un prompt prêt à copier, plus le journal de ce qui a changé.

## Quand appliquer ce skill

Appliquer quand un texte de départ existe et qu'il s'agit de l'améliorer : un prompt écrit par l'utilisateur, ou le cadrage sorti de `/clarifier-la-demande` ou `/interrogatoire`.

Ne pas appliquer quand il n'y a qu'une idée en vrac sans formulation : passer d'abord par `/clarifier-la-demande`.

## Les quatre lentilles

| Lentille | Question | Ce qu'elle règle |
|----------|----------|------------------|
| **Produit** | Quoi obtenir ? | Livrable, destinataire, support, objectif, format, longueur, périmètre, contraintes dures |
| **Processus** | Comment travailler ? | Orientation, séquence d'étapes, ou démonstration par l'exemple |
| **Performance** | Qui être, comment se comporter ? | Registre, posture, degré de franchise, niveau de détail du raisonnement |
| **Preuve** | Sur quoi s'appuyer, que faire sans ? | Sources fournies, sources interdites, conduite à tenir quand l'information manque, critère de refus |

### Règles d'application

- **Produit et Preuve : toujours.** Un prompt sans Produit est ininterprétable. Un prompt sans Preuve produit du plausible inventé que personne ne détecte.
- **Processus et Performance : selon la variance.** Test : *combien de sorties différentes seraient toutes acceptables ?*
  - Peu (un email de confirmation, une reformulation) : ne pas guider le processus. Ajouter des étapes ici alourdit sans rien gagner.
  - Beaucoup (une analyse stratégique, un benchmark, un cadrage) : guider le processus, c'est là que le gain est maximal.
- **Performance** ne s'ajoute que si le ton, la posture ou le degré de franchise changent le résultat attendu.

### Instruction directe plutôt que rôle

Préférer l'instruction comportementale au personnage assigné. « Cherche les failles de mon raisonnement » est plus fiable que « joue le rôle d'un consultant qui cherche les failles » : le personnage ajoute du décor stylistique sans ajouter de rigueur. N'assigner un rôle que s'il apporte un corpus de connaissances spécifique, pas une simple attitude.

## Procédure

1. **Diagnostiquer.** Passer le texte d'entrée aux quatre lentilles. Pour chacune : `couvert`, `partiel`, `absent`.
2. **Appliquer le test de variance** pour décider si Processus et Performance sont nécessaires. Énoncer le résultat du test dans le journal.
3. **Compléter.** Renseigner ce qui manque. Toute valeur déduite et non fournie par l'utilisateur est marquée `⚠` dans le journal, jamais dans le prompt final.
4. **Élaguer.** Retirer toute instruction dont la suppression ne changerait pas le résultat. Un optimiseur sans frein produit des prompts qui grossissent à chaque passage. La longueur n'est pas un signe de qualité.
5. **Livrer** le prompt et le journal.

## Squelette du prompt produit

N'inclure que les rubriques qui portent de la matière. Une rubrique vide est supprimée, pas laissée en blanc.

```
RÔLE
[Seulement si un corpus spécifique est requis. Sinon, supprimer.]

CONTEXTE
- Qui je suis : [poste, organisation]
- Destinataire : [qui lit, quelle relation, quel niveau]
- Situation : [ce qui motive cette demande]

TÂCHE
[Ce qu'il faut produire, avec l'objectif précis.]

PROCESSUS
[Seulement si le test de variance le justifie. Orientation, séquence numérotée, ou démonstration.]

RÈGLES
- [Contraintes de fond et de forme adaptées au type de demande :
  rédactionnel → ton, longueur, registre, formulations à proscrire ;
  analyse → critères de comparaison, seuils, périmètre étudié ;
  technique → stack, versions, contraintes d'exécution.]
- Hors sujet : [ce qui ne doit pas être traité]

SOURCES ET INCERTITUDE
- Matière à utiliser : [documents fournis, données, périmètre de recherche autorisé]
- Si une information manque : ne pas l'inventer. Écrire « Information non disponible » ou signaler la vérification à faire.
- [Le cas échéant : exiger les sources et le raisonnement pour permettre la vérification.]

FORMAT
[Forme exacte de la sortie et longueur.]

CRITÈRE DE REFUS
[À quoi on reconnaît un résultat raté. Omettre si l'utilisateur ne l'a pas fourni et qu'il n'est pas déductible.]

<exemples>
Bon : [...]
Mauvais : [...]
</exemples>
[Section incluse seulement s'il y a de la matière réelle. Sinon supprimer et le signaler dans le journal.]
```

## Format de sortie

```
## Prompt optimisé
[Bloc de code contenant le prompt complet, prêt à copier. Rien d'autre dans ce bloc.]

## Ce qui a changé
[Tableau : Lentille | Modification | Pourquoi | Statut]
Statut : `fourni` si l'utilisateur l'a dit, `⚠ déduit` sinon.

## Test de variance
[Une ligne. Nombre de sorties acceptables : faible ou élevé. Conséquence : Processus et Performance ajoutés ou écartés.]

## Ce qui manque encore
[Ce que le skill n'a pas pu renseigner et qui dégradera le résultat. Une ligne par point, avec l'effet concret. Omettre la section s'il n'y a rien.]
```

## Règles de rédaction

- Ne jamais mettre de marqueur d'incertitude dans le prompt final. Le prompt doit être copiable tel quel. Les ⚠ vont dans le journal.
- Ne pas spécifier ce dont le comportement par défaut convient déjà. Chaque ligne ajoutée doit changer quelque chose.
- Ne pas gonfler un prompt court qui fonctionne. Si le prompt d'entrée est déjà suffisant, le dire et ne rien ajouter.
- Phrases courtes, puces, tableaux. Aucune phrase d'introduction ni de conclusion.
- Ne jamais utiliser le caractère tiret cadratin.

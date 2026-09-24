---
name: "interrogatoire"
description: "Interroger une demande et les prémisses qui la soutiennent, une question à la fois, jusqu'à ce qu'aucune zone floue ne subsiste. À utiliser quand l'enjeu justifie un interrogatoire complet plutôt qu'un cadrage rapide."
---

# Interrogatoire

Interrogatoire méthodique. Une question à la fois. Ne s'arrête pas tant qu'il reste du vague.

## Quand appliquer ce skill

Appliquer quand l'utilisateur demande explicitement d'être questionné à fond, ou quand l'enjeu d'une demande justifie un interrogatoire complet plutôt qu'un cadrage rapide.

Ne pas appliquer :
- pour un cadrage rapide en une passe, avec livraison immédiate : c'est `/clarifier-la-demande` ;
- pour générer des options, des idées ou des solutions. Ce skill ne propose rien, il interroge. Un skill de brainstorming sert à produire des pistes ; celui-ci sert à détruire le flou.

## Ce qui est passé au gril

Deux volets. Les deux sont traités.

### Volet A : la demande (10 axes)

| # | Axe | Question sous-jacente |
|---|-----|----------------------|
| 1 | Intention réelle | Quelle décision ou quel livrable y a-t-il derrière ? |
| 2 | Destinataire | Qui lit, avec quel niveau de connaissance et quelle relation ? |
| 3 | Périmètre négatif | Qu'est-ce qui est explicitement hors sujet ? |
| 4 | Matière disponible | Qu'est-ce qui existe déjà vs ce qui reste à chercher ? |
| 5 | Critère de refus | À quoi reconnaît-on un résultat raté ? |
| 6 | Format et volume | Quelle forme, quelle longueur ? |
| 7 | Posture | Quel rôle incarner, quel ton ? |
| 8 | Contraintes dures | Délai, langue, confidentialité, outil de destination ? |
| 9 | Niveau de liberté | Exécution fidèle, ou droit de proposer autre chose ? |
| 10 | Traitement de l'incertitude | Si une information manque : signaler, chercher, ou supposer ? |

### Volet B : les prémisses (3 questions)

| # | Prémisse | Question |
|---|----------|----------|
| P1 | Origine | Sur quoi repose la conviction de départ : un fait observé, un retour utilisateur, une intuition, une consigne reçue ? |
| P2 | Preuve | Quelle preuve existe ? Quelle source, quelle fraîcheur, quel échantillon ? |
| P3 | Falsifiabilité | Qu'est-ce qui, s'il était vrai, rendrait cette demande inutile ? |

P3 est la question la plus productive. Ne jamais la sauter.

## Procédure

1. **Diagnostic initial silencieux.** Passer les 13 points. Marquer chacun `donné`, `déductible` ou `ouvert`. Un point `déductible` reste `ouvert` tant qu'il n'est pas confirmé.
2. **Une question par tour.** Choisir le point ouvert dont l'absence change le plus le livrable final. Poser cette seule question. Ne pas en grouper plusieurs.
3. **Afficher la progression** à chaque tour : `Tour n · X/13 renseignés · reste : [liste courte des points ouverts]`.
4. **Traiter les réponses évasives.** Si une réponse ne tranche pas le point, ne pas reposer la question ouverte. Proposer 2 à 3 réponses concrètes et demander laquelle est la bonne. Si aucune ne convient, l'utilisateur en donne une quatrième.
5. **Relancer sur le même point** tant qu'il n'est pas tranché, avant de passer au suivant.
6. **Accepter l'indéterminable.** Si l'utilisateur dit qu'il ne sait pas et qu'aucune option proposée ne convient, marquer le point `indéterminable`, énoncer en une ligne le risque que ça fait peser sur le livrable, et avancer.
7. **S'arrêter** quand les 13 points sont `renseignés` ou `indéterminables`.

## Garde-fou

Au-delà de 12 questions posées, arrêter l'interrogatoire quel que soit l'état de la grille. Livrer en l'état, en listant les points restés ouverts et le risque associé à chacun. L'utilisateur peut demander de continuer.

Si l'utilisateur dit d'arrêter, arrêter immédiatement et livrer.

## Format de sortie finale

```
## Demande reformulée
[Un paragraphe dense, intégrant tout ce qui a été obtenu pendant l'interrogatoire.]

## Grille complète
[Tableau des 13 points : Point | Valeur retenue | Statut (renseigné / indéterminable)]

## Ce qui reste ouvert
[Points indéterminables, et pour chacun le risque concret sur le livrable. Omettre la section s'il n'y en a aucun.]

## Ce que l'interrogatoire a fait tomber
[Une à trois lignes. Les hypothèses de départ qui se sont révélées fausses, absentes de preuve, ou sans effet sur le résultat. Omettre s'il n'y a rien.]

## Suite
[Une ligne : appeler `/optimiser-le-prompt` pour transformer ce cadrage en prompt, ou enchaîner directement sur le livrable.]
```

## Règles de conduite

- Une question par message. Jamais deux.
- Questions fermées ou à options. Jamais « peux-tu préciser ? » ni « dis-m'en plus ».
- Ton factuel, pas agressif. L'objectif est de faire tomber le vague, pas de mettre l'utilisateur en difficulté.
- Ne jamais valider par complaisance. Une réponse qui ne tranche pas est signalée comme telle.
- Ne rien inventer pour combler un trou. « Information non disponible ».
- Phrases courtes, puces, tableaux. Aucune phrase d'introduction ni de conclusion.
- Ne jamais utiliser le caractère tiret cadratin.

---
name: "ecrit-comme-moi"
description: "Réécrire un texte existant dans la voix de Julien, selon le registre approprié au destinataire et au support. À utiliser quand un brouillon est correct sur le fond mais ne sonne pas comme lui."
---

# Écrit comme moi

Entrée : un texte déjà rédigé, correct sur le fond.
Sortie : le même texte dans la voix de Julien, plus les règles appliquées.

## Quand appliquer ce skill

Appliquer quand un brouillon existe et qu'il s'agit de le faire sonner juste.

Ne pas appliquer :
- pour retirer les tics d'écriture génériques de l'IA : c'est `/chasser-le-ton-ia`. Opération différente : elle **enlève** des marqueurs négatifs, celle-ci **ajoute** des marqueurs positifs. Un texte peut être nettoyé de tout tic IA et ne ressembler à personne. Dans l'ordre : nettoyer d'abord, personnaliser ensuite ;
- pour rédiger un texte qui n'existe pas encore.

## Le profil

### Construction de la phrase

- Phrases courtes. Une idée par phrase.
- Puces et tableaux pour structurer, plutôt que la prose continue.
- Pas de phrase d'introduction annonçant ce qui va être dit. Entrer dans le sujet.
- Pas de conclusion qui résume ce qui vient d'être écrit.

### Lexique

- **Conserver les anglicismes professionnels** : roadmap, backlog, sprint, scope, deadline, POC, MVP. Ne jamais les franciser, même vers un francophone natif.
- **Bannir le jargon creux** : synergie, disruptif, paradigme, écosystème au sens figuré, ADN de l'entreprise, mise en musique.
- **Ne jamais utiliser le caractère tiret cadratin.** Le remplacer par une virgule, un deux-points, ou couper la phrase.

### Ton

- **Consultatif, pas assertif.** « Je propose », « on peut », « une option serait ». Éviter « il faut », « vous devez ».
- **Neutre plutôt que première personne dans les livrables.** Le « je » est réservé aux messages d'échange et à la prise de position explicite.
- Direct sans être brutal. Une objection se pose factuellement, pas avec des précautions oratoires.

### Structure

- **Compte rendu et note : le contexte d'abord, jamais la conclusion en ouverture.** Le lecteur doit savoir de quoi il s'agit avant de savoir ce qui a été décidé.
- **Formalisme calibré sur le niveau hiérarchique et le nombre de destinataires**, pas sur le fait que ce soit interne ou client.

### Humour

Second degré et absurde, sur les situations, jamais sur les personnes. Exclus : l'humour noir en contexte professionnel, et l'humour qui écrase quelqu'un sous couvert d'être décontracté. Ne jamais forcer une plaisanterie : si le texte n'en appelle pas, ne pas en ajouter.

### Orthographe

Vérifier systématiquement les accords infinitif / participe passé (« manger » contre « mangé »). C'est la faute qui compte.

## Les registres

Identifier le registre avant de réécrire. En cas de doute entre deux, demander.

| Registre | Quand | Marqueurs spécifiques |
|----------|-------|----------------------|
| **Email formel** | Hiérarchie, client, externe, ou plusieurs destinataires | Ouverture « Bonjour « + prénom ». Clôture « Bien à vous » ou « Cordialement ». Une demande claire par message. Formalisme croissant avec le niveau et le nombre de destinataires. |
| **Livrable projet** | Compte rendu, note de cadrage, spec, support de COPIL | Neutre, pas de « je ». Contexte, puis constat, puis décision ou recommandation. Tableaux plutôt que paragraphes. |
| **Message interne** | Équipe, canal projet, échange court | Direct, familier sans être relâché. Second degré possible. Aller au fait dès la première ligne. |
| **Contenu public** | LinkedIn, candidature, présentation de positionnement | Première personne assumée. Un fait concret ou un chiffre vérifiable plutôt qu'une affirmation générale. Pas de formule d'accroche artificielle. |

## Procédure

1. **Identifier le registre** à partir du destinataire et du support. Si le texte ne permet pas de trancher, poser une question unique.
2. **Réécrire** en appliquant le profil et les marqueurs du registre.
3. **Préserver le fond intégralement.** Ce skill change la forme. Il ne retire pas un argument, n'ajoute pas une idée, ne modifie pas un chiffre. Si le fond pose problème, le signaler séparément sans y toucher.
4. **Signaler les zones indéterminées.** Si un passage relève d'un choix de registre que le profil ne couvre pas, proposer deux formulations plutôt que d'en inventer une.

## Format de sortie

```
## Texte réécrit
[Le texte complet, prêt à copier.]

## Registre retenu
[Une ligne, avec la raison.]

## Règles appliquées
[Liste courte : la règle, et le changement qu'elle a produit. Se limiter aux changements notables.]

## À trancher
[Passages où deux formulations sont défendables, avec les deux options. Omettre la section s'il n'y en a pas.]
```

## Limite connue

Ce profil est déclaratif : il encode des règles énoncées, pas des marqueurs extraits de textes réels. Il est fiable sur la structure, le lexique banni et les formules d'ouverture. Il l'est moins sur les tournures propres à Julien.

Pour l'améliorer : analyser 3 à 5 textes qu'il a écrits lui-même sans IA, en extraire les marqueurs récurrents, et les ajouter à ce profil. Quand un résultat sonne faux, la correction qu'il apporte est une règle manquante : la proposer à l'ajout.

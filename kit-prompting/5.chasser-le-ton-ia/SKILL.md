---
name: "chasser-le-ton-ia"
description: "Retirer d'un texte les marqueurs structurels, rythmiques et typographiques qui trahissent une production IA non relue. À utiliser sur un brouillon dont le fond convient mais dont la forme sonne mécanique."
---

# Chasser le ton IA

Entrée : un texte produit ou assisté par IA.
Sortie : le même texte débarrassé de ce qui trahit l'absence de relecture, plus le journal des retraits.

## Quand appliquer ce skill

Appliquer quand un texte est correct sur le fond mais sonne mécanique.

Ne pas appliquer :
- pour faire sonner un texte comme son auteur : c'est `/ecrit-comme-moi`. Opération inverse : celle-ci **retire** des marqueurs génériques, l'autre **ajoute** des marqueurs personnels. Un texte parfaitement nettoyé peut ne ressembler à personne. Dans l'ordre : nettoyer d'abord, personnaliser ensuite ;
- pour corriger le fond, la structure d'un argument ou une erreur factuelle.

## Principe

On ne traque pas des mots. On traque des **formes**.

Aucune liste noire lexicale. Les listes de « mots IA » qui circulent sont en grande partie folkloriques : elles proscrivent des mots français légitimes et appauvrissent le texte sans le rendre plus humain. Les marqueurs ci-dessous sont observables dans la phrase, pas déduits de la réputation d'un mot.

## Les marqueurs

### Structure

| # | Marqueur | Ce qu'on fait |
|---|----------|---------------|
| 1 | **Triade systématique** : trois éléments à chaque énumération, toujours trois | Passer à deux ou quatre quand la matière le dit. Une triade justifiée reste. |
| 2 | **Antithèse de balancier** : « ce n'est pas X, c'est Y », « non pas X mais Y » | Affirmer Y directement. Garder si le contraste avec X porte une information. |
| 3 | **Clausule qui reformule** : dernier paragraphe qui résume ce qui précède | Supprimer. Le texte s'arrête sur son dernier point utile. |
| 4 | **Ouverture qui s'annonce** : « dans cet article », « voyons ensemble », « commençons par » | Supprimer et entrer dans le sujet. |
| 5 | **Pivot artificiel** : « mais il y a un piège », « le problème ? », « sauf que » isolé | Supprimer ou fondre dans la phrase suivante. |
| 6 | **Question rhétorique isolée** sur une ligne, suivie de sa réponse | Poser l'affirmation. |
| 7 | **Découpage en parties égales** imposé à une matière qui ne s'y prête pas | Redécouper selon le contenu réel, quitte à produire des sections inégales. |
| 8 | **Transition sans rapport logique** : un connecteur qui n'exprime aucun lien réel entre les deux paragraphes | Supprimer le connecteur, ou expliciter le lien s'il existe. |

### Rythme

| # | Marqueur | Ce qu'on fait |
|---|----------|---------------|
| 9 | **Longueur de phrase homogène** : aucune variation sur tout le texte | Casser. Une phrase courte après deux longues. |
| 10 | **Parallélisme mécanique des puces** : même construction grammaticale et même longueur partout | Varier. Le parallélisme reste quand les items sont vraiment de même nature. |
| 11 | **Adjectifs par paires** : « clair et concis », « simple et efficace », « robuste et fiable » | Garder un seul adjectif, le plus précis. |
| 12 | **Intensificateur vide** : « véritablement », « réellement », « particulièrement » sans contraste | Supprimer l'adverbe. |
| 13 | **Gradation ascendante artificielle** : chaque item présenté comme plus fort que le précédent | Ordonner selon l'importance réelle. |

### Ponctuation et typographie

| # | Marqueur | Ce qu'on fait |
|---|----------|---------------|
| 14 | **Tiret cadratin** | Retirer sans discussion. Remplacer par une virgule, un deux-points, ou couper la phrase. |
| 15 | **Gras sur les premiers mots de chaque puce**, systématiquement | Ne garder le gras que sur les puces où il sert à scanner. |
| 16 | **Emoji décoratif** en tête de section ou de puce | Retirer, sauf demande explicite. |

## Test de suppression

Avant chaque retrait, poser : **la phrase est-elle meilleure sans ?**

- Oui : retirer.
- Non, ou équivalent : garder et l'inscrire dans la section « Gardé volontairement ».

Un marqueur identifié n'est pas une faute. Certaines triades sont justes, certains parallélismes sont nécessaires. Le nettoyage mécanique casse des textes corrects.

## Règles

- **Ne pas toucher au fond.** Aucun argument retiré, aucun chiffre modifié, aucune idée ajoutée. Si le fond pose problème, le signaler séparément.
- **Ne pas réécrire ce qui va bien.** Un passage sans marqueur reste intact, au mot près.
- **Ne pas substituer un tic à un autre.** Une antithèse retirée ne se remplace pas par une question rhétorique.
- Si le texte ne contient aucun marqueur, le dire et ne rien changer.

## Format de sortie

```
## Texte nettoyé
[Le texte complet, prêt à copier.]

## Retraits
[Tableau : Marqueur (numéro et nom) | Passage d'origine | Remplacement | Pourquoi la phrase est meilleure]

## Gardé volontairement
[Marqueurs identifiés mais conservés, avec la raison. Omettre la section s'il n'y en a aucun.]
```

## Limite connue

Ce skill n'a aucun effet garanti sur un détecteur automatique de texte IA. Ces outils ont des taux de faux positifs élevés et documentés, y compris sur des textes entièrement humains. Ne jamais présenter le résultat comme « indétectable ». L'objectif de ce skill est un texte qui a l'air relu, pas un texte qui trompe un classifieur.

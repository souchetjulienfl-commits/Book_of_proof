---
name: routes-connues
description: Faits empiriques déjà constatés sur des routes spécifiques (jours de vol opérés, particularités), à consulter avant l'étape 1 du skill tour-operator-perso pour gagner du temps, mais toujours reverifier avant de conclure, ces fréquences peuvent changer.
---

# Routes connues

## ORY ↔ SOF (Orly ↔ Sofia)

- **Transavia** : vole en général uniquement le **vendredi** sur cette route (aller comme retour). Confirmé aussi dans le sens Sofia→Orly (SOF→ORY à l'aller) le 2026-09-14 : seul vendredi 16/10/2026 avait un vol, tous les autres jours de la semaine du 12 au 18/10 affichaient "aucun vol disponible".
- **easyJet** : vole en général le **jeudi**, et parfois le **dimanche**, sur cette route, mais ce n'est pas garanti chaque semaine. Test du 2026-09-14 (semaines du 12/10 et du 19/10/2026, sens SOF→ORY) : seul le **jeudi** (15/10 et 22/10) avait un vol ; le **dimanche** (18/10 et 25/10) affichait explicitement "Aucun vol disponible" sur les deux semaines. Donc : viser le jeudi en priorité, mais vérifier le dimanche au cas par cas plutôt que de le supposer disponible.
- Ryanair ne dessert pas Paris Orly (base parisienne = Beauvais), inutile de le chercher sur une route au départ d'ORY.
- Constaté empiriquement (test du 2026-09-11 puis confirmé par Julien le 2026-09-14, et re-testé le 2026-09-14 dans le sens SOF→ORY). Vérifie quand même à chaque recherche que ça n'a pas changé (nouvelle route, saison différente...) plutôt que de le supposer aveuglément, mais ça permet de directement viser le bon jour de la semaine dans le calendrier au lieu de tâtonner.

## BVA ↔ SOF (Beauvais ↔ Sofia)

- **easyJet et Transavia ne desservent pas cette route** : ces deux compagnies opèrent leurs vols vers Sofia depuis Paris Orly/CDG, pas depuis Beauvais. Inutile de lancer une recherche sur easyjet.com/transavia.com pour BVA↔SOF, pivoter directement.
- **Ryanair ne dessert pas non plus BVA↔SOF**, malgré Beauvais étant sa base parisienne. Constaté empiriquement le 2026-09-24 sur ryanair.com : "Désolé, il n'y a pas de vols disponibles ce jour" pour toute la semaine du 14 au 18/12/2026, et re-testé en hors-saison (semaine du 14/06/2027, donc pas un problème de vente pas encore ouverte) avec le même résultat sur les 5 jours affichés → la route n'existe simplement pas chez Ryanair, pas seulement "pas encore en vente".
- **Wizz Air dessert BVA↔SOF en direct** (Airbus A321neo, vols W6, ~2h45 à l'aller BVA→SOF et ~3h10 au retour SOF→BVA à cause du décalage horaire). C'est la seule compagnie low-cost pertinente sur cette route.
- **Fréquence Wizz Air** : vole uniquement les **dimanche, lundi, mercredi et vendredi** (pas mardi/jeudi/samedi), constaté sur le graphique de prix (price chart) de wizzair.com pour décembre 2026 et janvier 2027, dans les deux sens (BVA→SOF et SOF→BVA). Viser un de ces 4 jours en priorité plutôt que de tâtonner.
- **Formules tarifaires Wizz Air** (constaté le 2026-09-24, noms stables mais prix à revérifier à chaque lancement) : **Basic** (sac sous le siège 40×30×20cm seul) → **Wizz Smart** (+ bagage cabine à roulettes 10kg 55×40×23cm, toujours pas de soute) → **Wizz Go** (première formule avec bagage en soute enregistré, 20kg) → **Wizz Plus** (32kg soute + confort/flexibilité, au-delà du périmètre par défaut du skill). Prix par passager, affichés par jambe de vol (aller et retour tarifés séparément, pas de prix "aller-retour" unique affiché avant sélection des deux vols).
- Le prix de la formule Basic varie fortement selon la date (ex: retour 28/12/2026 à 55,99€/pers. vs retour 04/01/2027 à 114,99€/pers., soit la période du Nouvel An nettement plus chère), donc bien comparer plusieurs dates de retour si Julien en demande plusieurs.
- **Skyscanner n'était pas bloqué le 2026-09-24 sur cette route** (contrairement au constat précédent sur ORY↔SOF ci-dessous) : recherche BVA-SOF fonctionnelle, résultats affichés normalement (Wizz Air direct, revendu aussi via des agrégateurs/OTA type "W" ou Trip.com à des prix légèrement inférieurs à wizzair.com en direct, écarts constatés de l'ordre de -15% à -20%, sous le seuil d'alerte). Donc toujours retenter Skyscanner d'abord plutôt que de supposer un blocage systématique.

## Comparateurs

- **Skyscanner** bloque la navigation automatisée avec un contrôle anti-bot. Constaté le 2026-09-11, puis reconfirmé techniquement le 2026-09-14 : le champ de recherche "De/À" ne remonte plus aucune suggestion, et l'inspection réseau montre que l'API `g/autosuggest-search/api/v1/search-flight/...` répond systématiquement **403 Forbidden** dès qu'un navigateur automatisé l'appelle (pas de CAPTCHA visible cette fois, juste un blocage silencieux de l'autocomplete). Ne pas tenter de contourner, basculer sur un autre comparateur (Google Flights, Kayak) si besoin. Google Flights a fonctionné sans blocage le 2026-09-14 (formulaire classique, pas d'API séparée bloquée).

## Comment enrichir ce fichier

Chaque fois qu'un lancement du skill découvre un fait réutilisable sur une route ou un site (jours opérés, comparateur bloqué, particularité de recherche), ajoute-le ici avec la date de constat, pour que les prochains lancements n'aient pas à le redécouvrir. Ne remplace jamais un fait constaté par une supposition non vérifiée.

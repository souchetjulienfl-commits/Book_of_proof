---
name: tour-operator-perso
description: "Recherche et compare les prix de billets d'avion (easyJet, Transavia puis comparateurs) pour les prochaines vacances scolaires françaises zone C, formule par formule (bagage cabine, bagage soute), et produit un tableau comparatif détaillé. Utilise ce skill dès que Julien parle d'un vol, d'un billet d'avion, d'un aller-retour, d'une destination de vacances, d'un aéroport de départ/arrivée, ou mentionne \"tour operator perso\", même s'il ne donne pas toutes les dates (dans ce cas prends automatiquement la ou les prochaines vacances scolaires zone C à partir d'aujourd'hui). Se déclenche aussi bien manuellement qu'via un rapport programmé récurrent."
---

# Tour Operator Perso

Julien veut un point régulier (et déclenchable à la demande) sur le prix des billets d'avion pour ses prochains déplacements pendant les vacances scolaires. L'enjeu n'est pas de faire joli : c'est de lui donner des chiffres vérifiables, à jour, sur lesquels il peut décider de réserver ou d'attendre. Chaque approximation ou date inventée lui fait perdre plus de temps qu'elle n'en fait gagner, reste factuel, et dis explicitement quand une info n'a pas pu être vérifiée plutôt que de la deviner.

Le skill suit toujours les 5 étapes ci-dessous, dans l'ordre. Ne saute pas l'étape 0/1 : chercher des prix pour une période qui n'est pas encore ouverte à la réservation est une perte de temps et produit un rapport vide ou trompeur.

## Entrées attendues

À chaque déclenchement, identifie dans le prompt :
- **Aéroport de départ** et **aéroport d'arrivée** (codes IATA si possible, ex: ORY, SOF). Ces deux informations sont toujours censées être données dans la requête, si l'une manque, demande-la avant de continuer plutôt que de supposer un aéroport par défaut.
- **Période de voyage** (optionnel). Si aucune date n'est mentionnée, ne demande rien : prends automatiquement la **prochaine** période de vacances scolaires zone C à partir de la date du jour (voir étape 0-1).
- **Composition des passagers** (optionnel) : ça varie selon les voyages (ex: 1 adulte seul, ou 2 adultes + 1 enfant). Si le prompt ne le précise pas, ne bloque pas dessus, pars sur l'hypothèse **1 adulte** et affiche cette hypothèse en toutes lettres en tête du rapport, pour que Julien la corrige au besoin plutôt que de découvrir un prix calculé sur une composition qu'il n'a pas demandée.
- **Formule(s) à exclure** (optionnel) : Julien peut préciser qu'il ne veut pas telle formule pour cette recherche précise (ex: "je ne veux pas l'option avec seulement bagage à main"). Dans ce cas, ne cherche/n'affiche pas cette formule dans le tableau de cette exécution, mais ce n'est pas un réglage permanent du skill, donc ne le retiens pas pour les prochains lancements sauf si Julien le redemande.

## Étape 0 : Base des vacances scolaires zone C

Lis `references/vacances-zone-c.md` : il contient les dates officielles (source service-public.gouv.fr) des vacances de la zone C pour les années scolaires déjà vérifiées.

Si la période dont tu as besoin (la prochaine à partir d'aujourd'hui, ou celle demandée explicitement) n'y figure pas encore, ne l'invente jamais. Refais un `WebFetch` sur https://www.service-public.gouv.fr/particuliers/vosdroits/F31952 (ou une recherche web si l'URL a changé), puis mets à jour le fichier de référence avec les nouvelles dates trouvées et la date de vérification, pour que les prochains lancements du skill n'aient pas à refaire cette recherche.

## Étape 1 : Vérifier que la période est ouverte à la réservation

Avant de lancer la moindre recherche de prix : détermine la prochaine période de vacances zone C par rapport à aujourd'hui (ou la période demandée), puis vérifie que les vols sont déjà ouverts à la réservation sur ces dates chez easyJet et Transavia (ces compagnies ouvrent en général les ventes environ 6 à 11 mois à l'avance ; le calendrier de vente exact varie et n'est pas garanti, vérifie-le en le constatant plutôt qu'en le supposant, par exemple en tentant une recherche sur ces dates).

Cette vérification n'est pas forcément un simple oui/non global, en pratique (constaté sur test) deux pièges reviennent souvent, à checker explicitement :
- **L'aller et le retour peuvent ne pas ouvrir à la vente en même temps.** Si le retour (souvent plus loin dans le temps) n'est pas encore en vente alors que l'aller l'est, ne bloque pas tout : dis-le clairement dans le rapport et cherche la date de retour ouverte la plus proche de la fin des vacances.
- **La compagnie ne vole pas forcément tous les jours sur cette route.** Une compagnie low-cost dessert souvent une route 2 à 4 jours par semaine seulement (ex: uniquement vendredi, ou jeudi/dimanche). Le jour exact de début/fin des vacances (souvent un samedi ou un lundi) peut donc n'être desservi par personne. Dans ce cas, ne considère pas ça comme "vols non ouverts" : prends les dates réellement volées les plus proches à l'intérieur (ou en léger débord autour) de la période de vacances, et indique dans le rapport les dates réellement utilisées à côté des dates de vacances demandées, pour que Julien voie l'écart d'un coup d'œil.

- Si, malgré ça, aucun vol n'est trouvable sur toute la période (vraiment rien en vente, pas juste un jour qui ne convient pas) : arrête-toi là, dis-le clairement dans le rapport ("vols pas encore ouverts à la réservation pour [période], réessayer après le [date estimée d'ouverture si trouvable]") plutôt que de produire un tableau vide ou incomplet.
- Sinon : passe à l'étape 2 avec les dates réellement disponibles trouvées.

Consulte aussi `references/routes-connues.md` avant de commencer : il liste des fréquences déjà constatées (ex: sur ORY↔SOF, Transavia ne vole en général que le vendredi, easyJet que le jeudi/dimanche). Ça permet de viser directement le bon jour dans le calendrier au lieu de tâtonner, mais reste une indication à vérifier, pas une vérité figée.

**Mode empirique, vérifie, ne déduis pas.** Ne conclus jamais qu'une date "n'est pas disponible" à partir d'un simple clic qui n'a rien donné (bouton qui ne répond pas, page qui n'a pas changé, chargement en cours). Vérifie de façon programmatique/positive : un message explicite du site ("aucun vol ce jour-là", case grisée dans le calendrier de dates, résultat de recherche vide), pas une absence de réaction que tu interprètes toi-même. Si un clic semble ne rien faire, réessaie ou change d'approche avant de conclure, une fausse indisponibilité fait perdre confiance dans tout le rapport.

## Étape 2 : Recherche easyJet et Transavia

Pour l'aéroport de départ et d'arrivée donnés, la composition de passagers identifiée (adultes/enfants), et sur toute la période de vacances identifiée (du jour de début au jour de reprise inclus, cf. convention dans le fichier de référence), cherche sur easyjet.com et transavia.com.

Ces deux compagnies ne vendent pas un billet "avec ou sans bagage" en bloc : elles proposent plusieurs formules nommées, chacune ajoutant un bagage ou un service de plus. Julien suit déjà ça à la main dans Notion avec une ligne par formule (date aller, date retour, nom de la formule, bagages inclus, capture d'écran, prix), reproduis cette logique plutôt que de forcer artificiellement les résultats dans seulement deux colonnes "cabine / soute". Les trois formules pertinentes pour ce comparatif, par compagnie :

| Compagnie | Formule | Contenu bagages |
|---|---|---|
| easyJet | **Light** | bagage à main seul (sac sous le siège) |
| easyJet | **Smart+** | bagage à main + bagage cabine (valise en soute d'avion, pas de soute enregistrée) |
| easyJet | **Extra** | bagage à main + bagage cabine + **bagage en soute enregistré** |
| Transavia | **Basic** | bagage à main seul (sac sous le siège) |
| Transavia | **Smart** | bagage à main + bagage cabine |
| Transavia | **Plus** | bagage à main + bagage cabine + **bagage en soute enregistré** |

Ces noms et ce découpage sont stables (confirmés par Julien), pas besoin de les redécouvrir à chaque fois. Ce qui change et doit être vérifié à chaque lancement, c'est le **prix** de chacune de ces 3 formules, et leurs poids/dimensions exacts si le site les affiche (ils peuvent varier légèrement).

- Relève les 3 formules (Light/Smart+/Extra pour easyJet, Basic/Smart/Plus pour Transavia), sauf si Julien a explicitement exclu une formule pour cette recherche (voir "Entrées attendues").
- Ne va pas au-delà de la formule "bagage en soute inclus" (Extra / Plus), sauf demande explicite : les formules encore au-dessus (All-in / Max chez Transavia) ajoutent surtout du confort (siège, embarquement prioritaire) sans rien changer aux bagages.
- Pour chaque formule retenue, note : le nom exact affiché sur le site, une description courte de ce qu'elle inclut niveau bagages, et le prix (pour la composition de passagers demandée, précise si c'est un prix total ou par personne, cf. étape 4).

Ces sites reposent sur des formulaires de recherche dynamiques : une recherche web classique ne remonte pas des prix fiables. Utilise un outil de navigateur (Claude in Chrome, le navigateur intégré, ou le navigateur de l'ordinateur lié de Julien, selon celui disponible dans la session) pour naviguer sur le site, saisir origine/destination/dates/passagers, et lire les prix affichés sur la page de choix de formule. Si l'outil de navigateur le permet, prends une **capture d'écran** de cette page de choix de formule pour chaque compagnie : ça sert de preuve vérifiable du prix constaté à ce moment précis, exactement comme Julien le fait déjà à la main. La capture est un plus, pas un bloquant : par exemple, quand le navigateur utilisé est celui de l'ordinateur de Julien plutôt qu'un navigateur en sandbox, l'image peut ne pas être récupérable sans permission de dossier supplémentaire, dans ce cas, saute simplement la capture (indique "capture non disponible" dans le rapport) sans que ça remette en cause le prix lui-même, qui reste vérifié puisque tu l'as lu directement sur la page. Si aucun navigateur n'est disponible dans la session (par exemple lors d'un lancement programmé sans appareil lié), utilise la recherche web pour une estimation, saute la capture d'écran, et signale explicitement dans le rapport que les prix sont des estimations non vérifiées en direct, à recouper manuellement.

S'il y a plusieurs dates possibles dans la période (ex: plusieurs allers-retours envisageables sur des vacances de 2 semaines), retiens au minimum la combinaison la moins chère trouvée pour chaque compagnie, et mentionne les autres bonnes options si l'écart de prix est faible (moins de 15€).

## Étape 3 : Comparateurs

Cherche ensuite sur un ou plusieurs comparateurs de vols (Google Flights, Skyscanner, Kayak...) sur la même période et le même trajet, en comparant sur la même base bagages (bagage cabine seul, et bagage en soute inclus), pour voir si une autre compagnie ou un autre canal de vente bat les prix easyJet/Transavia trouvés à l'étape 2.

Considère l'écart comme "sensiblement moins élevé" à partir de **20% moins cher ou plus** que le meilleur prix easyJet/Transavia équivalent (même option bagage). En dessous de ce seuil, ne mets pas en avant l'écart comme une alerte, indique juste le prix dans le tableau, sans le signaler comme significatif.

Certains comparateurs (Skyscanner en particulier, constaté sur test) bloquent la navigation automatisée avec un contrôle anti-bot (CAPTCHA visible, ou blocage silencieux de l'autocomplétion/API en arrière-plan). Ne tente jamais de le contourner. Note simplement dans le rapport que ce comparateur était inaccessible pour cette recherche, et si tu as la place dans le temps imparti, essaie-en un autre (Google Flights a bien fonctionné sur test, ou Kayak) plutôt que de laisser l'étape 3 entièrement vide.

Si le comparateur ne fait que revendre le même vol au même prix qu'easyJet/Transavia trouvé à l'étape 2 (pas d'offre différente, pas d'écart), n'en fais pas une ligne à part dans le tableau final, mentionne-le juste dans le résumé en tête de rapport ("comparateur vérifié, aucune offre plus intéressante trouvée"). Une ligne comparateur ne mérite sa place dans le tableau que si elle apporte un prix ou une compagnie différente de ce qui est déjà en étape 2.

## Étape 4 : Tableau de comparaison

Produis **une ligne par formule tarifaire trouvée** (pas une ligne par compagnie) : c'est ce qui permet de voir d'un coup d'œil ce que chaque palier de prix ajoute réellement. Reprends la logique des tableaux Notion de Julien (une ligne par option, avec son détail bagages et sa capture). Format de tableau imposé par Julien, respecte exactement ces colonnes et cet ordre :

| Dép. | Arr. | Pax | Date aller | Jour | Date retour | Jour | Compagnie | Formule | Bagages inclus | Direct / escale | Durée | Prix | Écart vs meilleure formule soute easyJet/Transavia | Lien | Capture | Recherche le |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ORY | SOF | 1 | 16/10/2026 | vendredi | 23/10/2026 | vendredi | Transavia | Basic | 1 bagage à main (40×30×20cm), pas de soute | Direct | ≈2h45 / ≈3h05 | **191,00 €** | *n/a (ligne étape 2)* | transavia.com | non disponible | 11/09/2026 |

Précisions sur les colonnes :
- **Jour** : jour de la semaine de la date aller / retour respectivement, utile car easyJet/Transavia ne desservent pas toutes les routes tous les jours (cf. `references/routes-connues.md`), donc voir le jour d'un coup d'œil évite une confusion.
- **Bagages inclus** : phrase courte reprenant ce que montre le site (poids/dimensions si affichés), pas juste "oui/non".
- **Écart vs meilleure formule soute easyJet/Transavia** : uniquement rempli pour les lignes issues des comparateurs (étape 3), mets `n/a` pour les lignes easyJet/Transavia elles-mêmes (étape 2), avec un repère visuel si ≥ 20% (ex: "🔻 -24%").
- **Lien** : lien de réservation si trouvé, sinon le nom du site.
- **Capture** : si une capture a pu être prise (cf. étape 2), intègre-la dans le rapport HTML (directement dans la cellule ou juste en dessous de la ligne) ; sinon "non disponible", ce n'est jamais bloquant, cf. étape 2.
- **Recherche le** : date du jour du lancement, les prix évoluent en continu, ça sert à comparer les rapports entre eux dans le temps.
- **Prix** : mets-le en évidence (gras) dans le rapport HTML. Précise juste au-dessus du tableau si les prix affichés sont le **total pour l'ensemble des passagers** ou un **prix par personne**, les deux se justifient selon les sites, mais il faut que ce soit sans ambiguïté et cohérent sur toutes les lignes.

Trie le tableau par compagnie puis par prix croissant, pour que les formules d'une même compagnie restent groupées et lisibles en escalier.

### Format de sortie

Produis un rapport HTML autonome (une page, pas de fichiers externes) avec le tableau ci-dessus et un court résumé en tête (2-3 lignes : trajet, période couverte, meilleur prix trouvé, alerte éventuelle sur un écart comparateur ≥ 20%). Respecte le style ultra-concis habituel de Julien pour ce résumé : faits vérifiables, pas de commentaire ni de formule d'intro/conclusion.

Nomme le fichier `vols_<AEROPORT-DEPART>-<AEROPORT-ARRIVEE>_<AAAA-MM-JJ>.html` (date du jour du lancement) et livre-le avec l'outil d'envoi de fichier, c'est un rapport daté, pas un tableau de bord à mettre à jour : chaque lancement doit produire un nouveau fichier séparé, pour garder un historique des prix observés dans le temps, jamais écraser un rapport précédent.

Si des données n'ont pas pu être trouvées ou vérifiées pour une compagnie ou un comparateur (site indisponible, aucun vol sur la période, etc.), dis-le explicitement dans le tableau ou le résumé (ex: "Transavia : aucune donnée récupérée, site inaccessible") plutôt que de laisser une case vide sans explication ou d'inventer un prix.


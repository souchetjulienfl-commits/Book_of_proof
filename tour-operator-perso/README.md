# tour-operator-perso

Skill Claude (format `SKILL.md`) qui recherche et compare, en conditions réelles, les prix de billets d'avion easyJet/Transavia (puis comparateurs) pour les prochaines vacances scolaires françaises de zone C, formule par formule (bagage cabine, bagage soute), avec un tableau comparatif détaillé.

## Contexte

Créé le 11/09/2026 avec `skill-creator` (Claude), en itérant sur des tests réels plutôt que sur des suppositions : deux exécutions complètes ont été lancées via navigateur (recherche live sur easyJet, Transavia, Skyscanner, Google Flights, Ryanair), chacune ayant fait remonter des corrections concrètes intégrées au skill.

Ce dépôt sert de preuve du processus : la démarche de cadrage, la version finale du skill, et les rapports HTML réellement produits lors des tests (prix vérifiés en direct, pas générés).

## Contenu

- `SKILL.md` : le skill lui-même (instructions suivies par Claude à chaque déclenchement).
- `references/vacances-zone-c.md` : base des dates officielles de vacances scolaires zone C (source service-public.gouv.fr), vérifiée et datée.
- `references/routes-connues.md` : faits empiriques accumulés au fil des tests (fréquences de vol par compagnie, comparateurs bloqués par anti-bot), pour que chaque nouvelle exécution reparte plus vite.
- `examples/vols_ORY-SOF_2026-09-11.html` : premier test réel (Orly, Sofia, vacances de la Toussaint), avec ses limites documentées (Ryanair ne dessert pas Orly, Skyscanner bloqué par CAPTCHA).
- `examples/vols_SOF-ORY_2026-09-14.html` : second test après corrections (sens Sofia, Orly inversé, formules restreintes à la demande, blocage Skyscanner confirmé et contourné via Google Flights).

## Méthode

1. Cadrage initial avec l'utilisateur (objectif, périmètre, format de sortie).
2. Premier jet du skill, testé en conditions réelles (navigation live, pas de prix inventés).
3. Retours de l'utilisateur intégrés (formules tarifaires exactes easyJet/Transavia, format de tableau imposé, exclusion de formule à la demande).
4. Deuxième test réel sur un cas différent (sens du trajet inversé, dates différentes) pour vérifier que le skill généralise.
5. Corrections empiriques versionnées dans `references/routes-connues.md` au lieu d'être perdues à chaque exécution.

## Usage

Ce skill est conçu pour Claude (Cowork / Claude Code). Pour l'installer, importer le fichier `.skill` packagé (ou le dossier de ce dépôt) dans son profil Claude.


---
name: vacances-zone-c
description: Dates officielles des vacances scolaires françaises de la zone C (Créteil, Montpellier, Paris, Toulouse, Versailles). À lire en premier pour la sous-tâche 0/1 du skill tour-operator-perso, avant toute recherche de vol.
---

# Vacances scolaires - Zone C

Source officielle : [service-public.gouv.fr - Calendrier scolaire](https://www.service-public.gouv.fr/particuliers/vosdroits/F31952)
Page consultée et vérifiée le 2026-09-11 (mise à jour du site indiquée : 2026-09-02).

Zone C = académies de Créteil, Montpellier, Paris, Toulouse, Versailles.

Convention : les vacances commencent le jour indiqué après la classe, et la reprise a lieu le matin du jour indiqué. Pour une recherche de vol, considère donc que la période "voyageable" va du samedi (jour de début) au lundi ou mardi suivant (jour de reprise) inclus.

## Année scolaire 2026-2027

| Période | Début | Fin |
|---|---|---|
| Rentrée | mardi 1 septembre 2026 | n.a. |
| Toussaint | samedi 17 octobre 2026 | lundi 2 novembre 2026 |
| Noël | samedi 19 décembre 2026 | lundi 4 janvier 2027 |
| Hiver | samedi 6 février 2027 | lundi 22 février 2027 |
| Printemps | samedi 3 avril 2027 | lundi 19 avril 2027 |
| Été (début) | samedi 3 juillet 2027 | n.a. |

## Année scolaire 2027-2028

| Période | Début | Fin |
|---|---|---|
| Rentrée | jeudi 2 septembre 2027 | n.a. |
| Toussaint | samedi 23 octobre 2027 | lundi 8 novembre 2027 |
| Noël | samedi 18 décembre 2027 | lundi 3 janvier 2028 |
| Hiver | samedi 12 février 2028 | lundi 28 février 2028 |
| Printemps | samedi 15 avril 2028 | mardi 2 mai 2028 |
| Été (début) | mardi 4 juillet 2028 | n.a. |

## Maintenance de ce fichier

- Si la période demandée (ou la "prochaine période" calculée depuis la date du jour) n'apparaît pas dans les deux tableaux ci-dessus, ne pas deviner : refaire un `WebFetch` sur https://www.service-public.gouv.fr/particuliers/vosdroits/F31952 (ou une recherche web si la page a changé d'URL), compléter ce fichier avec `memory` n'est pas nécessaire, le fichier vit dans le skill, donc régénère-le via une édition directe du fichier avec les nouvelles dates trouvées et leur source.
- Toujours dater la vérification (comme fait ci-dessus) pour que l'utilisateur sache si les dates ont pu changer depuis.
- Ne jamais inventer une date de vacances : c'est un point de vérifiabilité factuelle explicitement demandé par l'utilisateur (esprit critique, pas d'hallucination).

Kit de prompting

Six skills Claude qui prennent une idée en vrac et la transforment en demande exécutable, puis en texte qui sonne juste.

Chaque skill s'invoque avec sa commande slash, ou se déclenche tout seul quand la demande correspond à sa description.

Les six skills
Commande	Quand l'utiliser	Ce qui sort
/clarifier-la-demande	Vous avez une idée, elle est floue, vous voulez avancer vite	La demande reformulée, une grille de 10 axes renseignés, 3 questions ciblées
/interrogatoire	L'enjeu est élevé, vous voulez qu'on ne laisse rien passer	Un questionnement, une question à la fois, jusqu'à ce que 13 points soient tranchés
/aide-methode	Vous savez ce que vous voulez, pas comment vous y prendre	Les étapes dans l'ordre réel, leurs livrables, leurs pièges, et un premier pas
/optimiser-le-prompt	Un prompt ou un cadrage existe, il faut l'affiner	Un prompt prêt à copier, plus le journal de ce qui a changé
/ecrit-comme-moi	Le texte est bon sur le fond, il ne sonne pas comme vous	Le texte réécrit dans le bon registre, plus les règles appliquées
/chasser-le-ton-ia	Le texte sent le brouillon non relu	Le texte nettoyé de 16 marqueurs, plus le détail des retraits
Le parcours type
Une idée en vrac
      |
      v
/clarifier-la-demande  ------> encore trop flou ? --> /interrogatoire
      |                                                      |
      |  <---------------------------------------------------+
      v
Vous ne savez pas comment faire ? --> /aide-methode
      |
      v
/optimiser-le-prompt   -->  un prompt prêt à l'emploi
      |
      v
Vous obtenez un texte
      |
      v
/chasser-le-ton-ia  -->  /ecrit-comme-moi  -->  texte final

Le parcours complet est rarement nécessaire. La plupart des demandes passent par deux skills, pas six.

Comment choisir entre deux skills proches

/clarifier-la-demande ou /interrogatoire ? Le premier fait une seule passe et livre immédiatement, avec des hypothèses marquées que vous corrigez. Le second boucle, une question à la fois, et ne livre qu'une fois tout tranché. Le premier pour démarrer vite, le second quand se tromper coûte cher.

/chasser-le-ton-ia ou /ecrit-comme-moi ? Ce sont deux opérations inverses. Le premier retire des marqueurs génériques. Le second ajoute des marqueurs personnels. Un texte parfaitement nettoyé de tout tic IA ne ressemble encore à personne. Dans l'ordre : nettoyer, puis personnaliser.

/aide-methode ou /clarifier-la-demande ? La question « que dois-je vouloir » appelle le clarificateur. La question « comment je m'y prends » appelle l'aide méthode.

Ce que le kit ne fait pas
Il ne produit pas le livrable final. Il prépare la demande, il affine le prompt, il retravaille le texte. La production reste une conversation normale.
/chasser-le-ton-ia ne garantit rien face à un détecteur automatique de texte IA. Ces outils ont des taux de faux positifs élevés, y compris sur des textes entièrement humains.
/ecrit-comme-moi encode un profil déclaratif, construit sur des règles énoncées et non sur des textes réels. Il est fiable sur la structure et le lexique banni, plus faible sur les tournures propres à son auteur. Le corriger quand il sonne faux fait partie de son usage.
Principes communs aux six skills
Toute valeur déduite et non fournie par l'utilisateur est marquée.
Rien n'est inventé pour combler un trou. Quand l'information manque, les skills écrivent « Information non disponible ».
Le caractère tiret cadratin n'est jamais utilisé.
Phrases courtes, puces et tableaux. Pas de phrase d'introduction ni de conclusion.
Historique des noms

Ces skills ont d'abord porté d'autres noms, repris d'un visuel de présentation. Si vous croisez un SKILL.md avec l'un de ces noms, c'est une version antérieure.

Nom d'origine	Nom actuel
clarificateur-de-demande	clarifier-la-demande
passe-moi-au-gril	interrogatoire
mode-d-emploi	aide-methode
optimiseur-de-prompt	optimiser-le-prompt
voix-personnelle	ecrit-comme-moi
chasse-aux-mots-ia	chasser-le-ton-ia

Un skill ne se renomme pas : il se recrée sous le nouveau nom, et l'ancien doit être supprimé à la main dans les paramètres. Tant que les deux coexistent avec la même description, le déclenchement automatique entre eux est imprévisible.

Archivage et réinstallation

Chaque dossier contient un SKILL.md autonome : un en-tête YAML avec name et description, puis les instructions.

Ces fichiers sont une archive, pas une source vivante. Les modifier ici ne change pas les skills actifs dans Claude. Pour modifier un skill, demandez la modification à Claude et validez la proposition qui s'affiche.

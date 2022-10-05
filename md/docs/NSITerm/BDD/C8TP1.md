TP SQL
======

## Requêtes simples, sans jointure

Soit la hase de données de `Livres` disponible sur [bdarid.noho.st](https://bdarid.noho.st) et déjà étudiée.  
Donner le code SQL de chacune des requêtes ci-dessous. Les mots en police fixe donnent une indication sur les attributs et les tables à utiliser dans la requête.  

1. Tous les `titre`s de `livre`.
2. Tous les `nom`s d'`usager`.
3. Tous les `nom`s d'`usager` en retirant les doublons.
4. Les `titre`s des livres publiés avant 1980.
5. Les `titre`s des livres dont le titre commence par la lettre « A ».
6. Les `isbn` des livres à rendre pour le 01/01/2020.
7. Les `nom`s d'`auteur`s triés par ordre alphabétique.
8. Les `nom`s d'`usager`s vivant dans le 12e ou 13e arrondissement de Paris (codes postaux 75012 et 75013).
9. Les `nom`s et `adresse`s des usagers n'habitant pas dans une rue. (la chaîne « Rue » ne doit pas apparaître dans l'adresse).
10. Les `annee`s et `titre`s des `livre`s publiés lors d'une année bissextile. On rappelle que ce sont les années divisibles par 4, mais pas celles divisibles  par 100 sauf si elles sont divisibles par 400.


## Requêtes avancées avec jointure

Soit la base de données `Livres` utilisée en cours et disponible en suivant le lien ci-dessus. Donner le code SQL de chacune des requêtes ci-dessous. Les mots en police fixe donnent une indication sur les attributs et les tables à utiliser dans la requête.  

1. Le `titre` des `livre`s `emprunt`és.
2. Le `titre` des `livre`s `emprunt`és à rendre avant le 31/03/2020.
3. Le `nom` et `prenom` de l'auteur du livre '1984' .
4. Le `nom` et le `prenom` des `usager`s ayant emprunté des livres, sans doublons (c'est-à-dire si un usager a emprunté plusieurs livres, il ne doit apparaître qu'une fois dans le résultat).
5. Même requête que précédemment, avec les noms triés par ordre alphabétique.

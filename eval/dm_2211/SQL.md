## 📚 Travaux Pratiques : SQL
---

#### Requêtes simples, sans jointure

1) Tous les « titre »s de « livre ».
```SQL
SELECT `titre` FROM `livre`;
```

2) Tous les « nom »s d'« usager ».
```SQL
SELECT `nom` FROM `usager`;
```

3) Tous les « nom »s d'« usager » en retirant les doublons.
```SQL
SELECT DISTINCT `nom` FROM `usager`;
```

4) Les « titre »s des livres publiés avant 1980.
```SQL
SELECT `titre` FROM `livre`
WHERE `annee` < 1980;
```

5) Les « titre »s des livres dont le titre commence par la lettre « A ».
```SQL
SELECT `titre` FROM `livre`
WHERE `titre` LIKE 'A%';
```

6) Les « isbn » des livres à rendre pour le 01/01/2020.
```SQL
SELECT `isbn` FROM `emprunt`
WHERE `retour` = '2020-01-01';
```

7) Les « nom »s d'« auteur »s triés par ordre alphabétique.
```SQL
SELECT `nom` FROM `auteur`
ORDER BY `nom` ASC;
```

8) Les « nom »s d'« usager »s vivant dans le 12e ou 13e arrondissement de Paris (codes postaux 75012 et 75013).
```SQL
SELECT `nom` FROM `usager`
WHERE `cp` = 75012 OR `cp` = 75013;
```

9) Les « nom »s et « adresse »s des usagers n'habitant pas dans une rue.
(la chaîne « Rue » ne doit pas apparaître dans l'adresse).
```SQL
SELECT `nom`, `adresse` FROM usager
WHERE `adresse` NOT LIKE '%Rue%';
```

10) Les « annee »s et « titre »s des « livre »s publiés lors d'une année bissextile.
```SQL
SELECT `annee`, `titre` FROM `livre`
WHERE (`annee` % 4 = 0 AND `annee` % 100 != 0) OR `annee` % 400 = 0;
```

####  Requêtes avancées avec jointure

1) le « titre » des « livre »s « emprunt »és.
```SQL
SELECT `livre`.`titre` FROM `livre`
JOIN `emprunt` ON `emprunt`.`isbn` = `livre`.`isbn`;
```

2) Le « titre » des « livre »s « emprunt »és à rendre avant le 31/03/2020.
```SQL
SELECT `livre`.`titre` FROM `livre`
JOIN `emprunt` ON `emprunt`.`isbn` = `livre`.`isbn`
WHERE `emprunt`.`retour` < '2020-03-31';
```

3) Le « nom » et « prenom » de l'auteur du livre '1984' .
```SQL
SELECT `auteur`.`nom`, `auteur`.`prenom` FROM `auteur`
JOIN `auteur_de` ON `auteur`.`a_Id` = `auteur_de`.`a_Id`
JOIN `livre` ON `livre`.`isbn` = `auteur_de`.`isbn`
WHERE `livre`.`titre` LIKE '1984';
```

4) Le « nom » et le « prenom »  des « usager »s ayant emprunté des livres, sans doublons.
```SQL
SELECT DISTINCT `nom`, `prenom` FROM `usager`
JOIN `emprunt` ON `usager`.`code_barre` = `emprunt`.`code_barre`;
```

5) Même requête que précédemment, avec les noms triés par ordre alphabétique.
```SQL
SELECT DISTINCT `nom`, `prenom` FROM `usager`
JOIN `emprunt` ON `usager`.`code_barre` = `emprunt`.`code_barre`
ORDER BY `nom` ASC;
```

---
###### 📜 Sites de recherche : [LearnSQL.com](https://learnsql.com/tags/cheat-sheet/), [Sql.sh](https://sql.sh/), [W3schools.com](https://www.w3schools.com/sql/)
###### ✒Editeur Markdown : [Obsidian](https://obsidian.md/)
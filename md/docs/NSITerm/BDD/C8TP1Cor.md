Correction du TP1
=================

## Requêtes simples

```sql
SELECT titre FROM livre;
SELECT nom FROM usager;
SELECT DISTINCT nom FROM usager;
SELECT titre FROM livre WHERE annee <= 1980;
SELECT titre FROM livre WHERE titre LIKE 'A%';
SELECT isbn FROM emprunt WHERE retour='2020-01-01';
SELECT nom FROM auteur ORDER BY nom;
SELECT nom FROM usager WHERE cp='75012' OR cp='75013';
SELECT nom,adresse FROM usager WHERE NOT (adresse LIKE '%Rue%');
SELECT annee, titre FROM livre WHERE annee%4 = 0 AND (annee%100 <> 0 OR annee%400 = 0);
```

## Requêtes avec jointure

```sql
SELECT titre FROM livre JOIN emprunt ON livre.isbn=emprunt.isbn;
SELECT titre FROM livre JOIN emprunt ON livre.isbn=emprunt.isbn WHERE emprunt.retour <= '2020-03-31';
SELECT nom, prenom FROM auteur JOIN auteur_de ON auteur_de.a_id=auteur.a_id JOIN livre ON livre.isbn=auteur_de.isbn WHERE livre.titre='1984';
SELECT DISTINCT nom, prenom FROM emprunt JOIN usager ON emprunt.code_barre=usager.code_barre;
SELECT DISTINCT nom, prenom FROM emprunt JOIN usager ON emprunt.code_barre=usager.code_barre ORDER BY nom;
```

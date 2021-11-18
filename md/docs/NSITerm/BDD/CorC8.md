Correction
==========

## Application 3

`LIVRES`(^^(`id` INT)^^, (`titre` STRING), #(`id_auteur` INT), (`ann_publi` INT), (`note` INT))  

`AUTEURS` (^^(`id` INT)^^, (`nom` STRING), (`prenom` STRING), (`ann_naissance` INT), (`titre` STRING))

## Relation Livres

1, 2 et 3 impossible à cause d'une contrainte de non unicité. `titre` est possible ici mais c'est quand même une très mauvaise idée.

## Relation Films

Pour alléger l'écriture, on ne fera pas apparaitre les domaines ici.  


REALISATEURS(<u>id</u>, nom, prenom et ann_naissance)  

| id | nom     | prenom  | ann_naissance |
|----|---------|---------|---------------|
| 1  | Scott   | Ridley  | 1937          |
| 2  | Lynch   | David   | 1946          |
| 3  | Kubrick | Stanley | 1928          |

Le schéma de la relation `FILMS` est alors modifié en:  

Films (<u>id</u>, titre, #idrealisateur, ann_sortie, note_sur_10)


| id |            titre             | idrealisateur | ann_sortie | note_sur_10 |
|----|------------------------------|-------------|------------|-------------|
| 1  | Alien, le huitième passager  |    1    |    1979    |     10      |
| 2  |             Dune             |    2    |    1985    |      5      |
| 3  | 2001 : l'odyssée de l'espace |   3   |    1968    |      9      |
| 4  |         Blade Runner         |    1   |    1982    |     10      |

## Exercice 140

Annuaire ((`nom` STRING), (`prenom` STRING), <u>(`tel` STRING)</u>)

## Exercice 141

Eleve ((`nom` STRING), (`prenom` STRING), <u>(`id` STRING)</u>)  

Matiere ((`intitule` STRING), <u>(`id_mat` INT)</u>)  

Note (<u> #(`id_eleve` STRING), #(`id_mat` INT)</u>, `note` FLOAT)

## Exercice 144

Departement ((`nom` STRING), (`chef_lieu` STRING), <u>(`code` STRING)</u>)  

Voisins (<u>#(`code_d1` STRING), #(`code_d2` STRING)</u>

## Exercice 145

Arret ((`lat` FLOAT), (`lon` FLOAT), (`nom` STRING), <u>(`id` INT)</u>)  

Ligne (<u>(`num` INT)</u>, (`nom` STRING))  

Horaire (<u>#(`num` INT), #(`id` INT), (`heure` TIME), (`jour` STRING) </u>)


```python

```

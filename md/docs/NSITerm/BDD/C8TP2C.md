Résolution de l'énigme
===================

![base](img/schema.png)

## Informations sur le crime

```sql
SELECT * FROM crime_scene_report WHERE city='SQL City' AND type='murder';
```

Réponse:  
*Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".*

## Identification des témoins

```sql
SELECT * FROM person WHERE address_street_name LIKE '%Northwestern Dr' 
ORDER BY address_number DESC LIMIT 1;
```

Réponse:  

| id  | name | license_id | address_number | address\_street\_name | ssn |
| --- | --- | --- | --- | --- | --- |
| 14887 | Morty Schapiro | 118009 | 4919 | Northwestern Dr | 111564949 |

```sql
SELECT * FROM person WHERE name LIKE '%Annabel%' 
and address_street_name LIKE '%Franklin Ave%';
```

Réponse:  

| id  | name | license_id | address_number | address\_street\_name | ssn |
| --- | --- | --- | --- | --- | --- |
| 16371 | Annabel Miller | 490173 | 103 | Franklin Ave | 318771143 |

## Transcription des entretiens des témoins

```sql
SELECT transcript FROM interview
JOIN person ON interview.person_id = person.id
WHERE person.address_street_name LIKE '%Northwestern Dr' 
ORDER BY person.address_number DESC LIMIT 1;
```

Réponse:

| transcript |
| --- |
| I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W". |

```sql
SELECT transcript FROM interview
JOIN person ON interview.person_id = person.id
WHERE name LIKE '%Annabel%' 
and address_street_name LIKE '%Franklin Ave%';
```

Réponse: 

| transcript |
| --- |
| I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th. |

## Exploitation des entretiens

```sql
SELECT * FROM get_fit_now_check_in
JOIN get_fit_now_member 
ON get_fit_now_check_in.membership_id = get_fit_now_member.id 
WHERE get_fit_now_check_in.check_in_date = 20180109
AND get_fit_now_member.membership_status = 'gold';
```

Réponse:

| membership_id | check\_in\_date | check\_in\_time | check\_out\_time | id  | person_id | name | membership\_start\_date | membership_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XTE42 | 20180109 | 486 | 1124 | XTE42 | 55662 | Sarita Bartosh | 20170524 | gold |
| 6LSTG | 20180109 | 399 | 515 | 6LSTG | 83186 | Burton Grippe | 20170214 | gold |
| GE5Q8 | 20180109 | 367 | 959 | GE5Q8 | 92736 | Carmen Dimick | 20170618 | gold |
| 48Z7A | 20180109 | 1600 | 1730 | 48Z7A | 28819 | Joe Germuska | 20160305 | gold |
| 48Z55 | 20180109 | 1530 | 1700 | 48Z55 | 67318 | Jeremy Bowers | 20160101 | gold |
| 90081 | 20180109 | 1600 | 1700 | 90081 | 16371 | Annabel Miller | 20160208 | gold |

```sql
select * from drivers_license AS dl
JOIN person ON person.license_id = dl.id
WHERE dl.plate_number LIKE '%H42W%'
AND dl.gender = 'male';
```

Réponse:

| id  | age | height | eye_color | hair_color | gender | plate_number | car_make | car_model | id  | name | license_id | address_number | address\_street\_name | ssn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 664760 | 21  | 71  | black | black | male | 4H42WR | Nissan | Altima | 51739 | Tushar Chandra | 664760 | 312 | Phi St | 137882671 |
| 423327 | 30  | 70  | brown | brown | male | 0H42W2 | Chevrolet | Spark LS | 67318 | Jeremy Bowers | 423327 | 530 | Washington Pl, Apt 3A | 871539279 |

gold

On en déduit que l'assassin est très certainement `Jeremy Bowers`.

## Entretien de Jeremy Bowers

```sql
SELECT transcript FROM interview
JOIN person ON interview.person_id = person.id
WHERE person.name = 'Jeremy Bowers';
```

Réponse:  

|transcript|
|--- |
|I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017.|

## Final

```sql
SELECT DISTINCT name FROM drivers_license AS dl
JOIN person ON dl.id = person.license_id
JOIN facebook_event_checkin ON facebook_event_checkin.person_id=person.id
WHERE dl.gender='female' AND dl.hair_color='red' AND dl.car_make='Tesla' 
AND dl.height BETWEEN 65 AND 67;
```

Réponse:  

|name|
|--- |
|Miranda Priestly|

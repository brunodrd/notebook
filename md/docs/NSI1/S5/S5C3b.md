Séquence 4 - Deuxième type construit: les p-uplets
==================================================

## Construction et propriétés d'un p-uplet  

!!! tip "p-uplet"
    En mathématique, un **p-uplet** est une collection ordonnée d'objets.  


Python fournit un type adapté à la représentation des p-uplets: le type `tuple`.  On créé un tuple en écrivant les composantes du p-uplet **séparées par une virgule** et de préférence **entre parenthèses**:  

```python
notes = (17, 15, 16) 
```

Comme avec les tableaux, on peut obtenir la taille d'un tuple avec la fonction native `len` et accéder au $i^{ème}$ élément avec la notation habituelle des crochets:


```python
notes = (17, 15, 16, 10)
print("Taille du p-uplet: ", len(notes))
print("Valeur du 3ème élément (index 2): ", notes[2])
```

    Taille du p-uplet:  4
    Valeur du 3ème élément (index 2):  16



```python
notes[1] = 7
print(notes)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-c340dc6cd5d2> in <module>
    ----> 1 notes[1] = 7
          2 print(notes)


    TypeError: 'tuple' object does not support item assignment


**Contrairement aux tableaux les composantes d'un tuple ne sont pas modifiables**. On dit que les tuples sont des objets immuables (ou non mutables). 

```python
notes[3] = 16.5
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-06e2d03882e0> in <module>()
----> 1 notes[3] = 16.5

TypeError: 'tuple' object does not support item assignment
```

## Parcourir un p-uplet  

Les méthodes de parcours rencontrées lors de la découverte des tableaux sont toujours valables. On peut itérer sur les index ou sur les éléments.


```python
print("****Relevé de notes****")
for n in notes:
    print(n)
print("****Moyenne****")
s = 0
for i in range(len(notes)):
    s = s + notes[i]
m = s / len(notes)
print(m)
```

    ****Relevé de notes****
    17
    15
    16
    10
    ****Moyenne****
    14.5


## Insuffisance des p-uplets

Etant donné le problème suivant:  

*On souhaite stocker les informations concernant des fichers image dans un p-uplet. Ce dernier aura pour composante sa largeur en pixel, sa hauteur en pixel et sa taille en kilo-octet.*  

Par exemple, soit le fichier "dog.png" qui a une largeur de 384 pixels, une hauteur de 576 pixels et dont la taille est de 243 ko.  

<figure>
<img alt="dog" src="img/dog.png" width="190px" />
</figure>
On peut le modéliser par un simple tuple:


```python
image = (384, 576, 243)
```

Cependant cette solution n'est pas idéale. En effet, il faut se souvenir de l'ordre dans lequel les entiers ont été rentrés !  
**On évitera d'utiliser des p-uplets lorsque des ambiguités ou confusions sont possibles**.

### Une solution possible

Pour contourner le problème soulevé précédemment, Python a une solution: les **p-uplets nommés**. Chaque composante du p-uplet se voit donner un nom!  

Python possède un type permettant de manipuler les p-uplets nommés: les `namedtuple` du module `collections`.  Cependant, et conformément au programme, en classe de 1re NSI, **on utilisera des dictionnaires pour implémenter des p-uplets nommés** (*voir cours dictionnaires*).

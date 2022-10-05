Séquence 4 - Aller plus loin avec les tableaux
==============================================

## Construction de tableaux en compréhension  

Supposons le problème suivant:  

*Construire un tableau des 10 premiers entiers naturels multiples de 9*.   

On peut construire ce tableau comme on l'a vu lors de la découverte des tableaux (on dit aussi construire en **extension**):  

```python
t = [0, 9, 18, 27, ...]
```

C'est potentiellement long et pas très élégant! Une deuxième solution serait d'utiliser une boucle `for`:  

```python
t = [0] * 10
for i in range(10):
    t[i] = 9 * i
```

Python propose une syntaxe plus compacte pour réaliser cette opération. Il s'agit de la **construction par compréhension** (on dit aussi en *intension*):  

```python
t = [9 * i for i in range(10)]
```

!!! info "À retenir"
    Plus généralement, au lieu de déclarer un tableau puis de le remplir avec une boucle, on préfèrera une construction plus concise appelée 
    construction par compréhension, qui prend la forme suivante:  
    
    ```python
    tableau = [expr(i) for i in sequence]
    ```
    
    `expr(i)` est une *expression* de la variable `i` qui parcourt tous les éléments de `sequence` (qui peut être un objet `range`, un tableau, 
    une chaine de caractère ou un des types qui seront vus dans les paragraphes ci-après). 

Modifions notre consigne de départ:  

*Parmi les 10 premiers entiers naturels multiples de 9, construire un tableau des entiers pairs uniquement*.  

La construction par compréhension permet là encore, une écriture compacte:  

```python
t = [9 * i for i in range(10) if 9 * i % 2 == 0]
```


!!! info "À retenir"
    La construction par compréhension permet d'ajouter une condition booléenne.  
    
    ```python
    tableau = [expr(i) for i in sequence if condition]
    ```  
    
    `condition` est exprimée avec les opérateurs de comparaisons habituels.


```python
# Exemple
t = [9 * i for i in range(20) if 9 * i % 2 == 0]
print(t)
```

    [0, 18, 36, 54, 72, 90, 108, 126, 144, 162]


## Complément: agrandir un tableau

Le langage python autorise un traitement particulier sur un tableau: pouvoir **l'agrandir sur sa droite**, même si sa taille a déjà été fixée. La syntaxe fait intervenir une fonction disponible avec les objets de type *list* (on dit aussi une *méthode*): `append`.


```python
tab = [1, 2, 3]
tab.append(5)
print(tab)
```

    [1, 2, 3, 5]


!!! warning "Attention"
    Dans le cadre du programme de 1re NSI, on privilégiera autant que possible la compréhension de tableau par 
    rapport à l'utilisation de la méthode `append`.

```python
from typing import List


def mat2tab(m: List[List[int]]) -> list:
    """
    renvoie la matrice m sous la forme d'un tableau
    m: tableau de tableaux d'entiers
    """
    tab = m[0] # on récupère l'intégralité du 1er sous tableau
    for t in m[1:]:
        tab += t # on va concaténer avec les sous tableaux restants
    return tab
```


```python
!mypy mestests.py
```

    [1m[32mSuccess: no issues found in 1 source file[m



```python
mat = [[1, 2, 3], 
       [4, 5, 6,], 
       [7, 8, 9]]
t = mat2tab(mat)
print(t)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
import ipytest
ipytest.autoconfig()
```


```python
%%ipytest
import pytest
from random import randint
from tri import  tri_insertion


def test_tab_neg_1():
    t = [-1,-1,-1]
    tri_insertion(t)
    assert  t == [-1,-1,-1]

def test_inverse_2():
    t = [14,10,5,1]
    tri_insertion(t)
    assert  t == [1,5,10,14]

def test_vide_0():
    with pytest.raises(ValueError):
        tri_insertion([])

def test_deja_tri_3():
    t = [1,2,3,4,5]
    tri_insertion(t)
    assert  t == [1,2,3,4,5]

def test_random_4():    
    t = [randint(-20, 20) for _ in range(10)]
    tri_insertion(t)
    assert all(t[i] <= t[i + 1] for i in range(9))

def test_en_place_5():
    assert tri_insertion([1,2,3]) is None

```

    [32m.[0m[32m.[0m[31mF[0m[32m.[0m[32m.[0m[32m.[0m[31m                                                                                       [100%][0m
    ============================================= FAILURES =============================================
    [31m[1m___________________________________________ test_vide_0 ____________________________________________[0m
    
        [94mdef[39;49;00m [92mtest_vide_0[39;49;00m():
    >       [94mwith[39;49;00m pytest.raises([96mValueError[39;49;00m):
    [1m[31mE       Failed: DID NOT RAISE <class 'ValueError'>[0m
    
    [1m[31m/tmp/ipykernel_7122/2745413413.py[0m:17: Failed
    ===================================== short test summary info ======================================
    FAILED tmpguxs08cg.py::test_vide_0 - Failed: DID NOT RAISE <class 'ValueError'>
    [31m[31m[1m1 failed[0m, [32m5 passed[0m[31m in 0.76s[0m[0m


---

La fonction `f1` effectue la multiplication de $2\times \pi$ avec le nombre passé en paramètre. On pourrait imaginer qu'elle effectue le calcul du périmètre d'un cercle. D'où, la proposition:


```python
def perimetre(r: float) -> str:
    """
    Calcul le périmètre d'un cercle de rayon r et renvoie le résultat sous
    forme d'une chaîne de caractère.
    r: rayon (float), décimal positif
    """
    assert r > 0, "Erreur, r > 0"
    
    return str(2 * 3.14 * r) + ' cm'
```


```python
perimetre(3)
```




    '18.84 cm'



La fonction `f2` vérifie si la somme du carré de deux nombres est égal au carré d'un troisième. On peut supposer qu'il vérifie si un triangle de côtés $a, b, c$ est rectangle en testant l'égalité $a^2+b^2=c^2$ (*Pythagore*). 


```python
from typing import Tuple


def est_rectangle(cotes: Tuple[int, int, int]) -> bool:
    """
    Vérifie si un triangle rectangle. Renvoie True si oui ou False sinon.
    cotes: tuple d'entiers positifs
    """
    a, b, c = cotes
    assert a > 0 and b > 0 and c > 0, "Erreur a,b,c positifs"
    
    return a**2 + b**2 == c**2
```


```python
est_rectangle((3, 4, 5))
```




    True




```python
est_rectangle(3, 4, 5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /tmp/ipykernel_7122/681810540.py in <module>
    ----> 1 est_rectangle(3, 4, 5)
    

    TypeError: est_rectangle() takes 1 positional argument but 3 were given



```python
est_rectangle((1, 7, 5))
```




    False



---

La fonction `f3` augmente la valeur associée à la clé passée en deuxième paramètre de 1, sauf si cette clé vaut `nsi`. Le code proposé modifie une entrée du dictionnaire, il serait souhaitable de vérifier que celle-ci existe !


```python
def augmente_note(releve: dict, matiere: str) -> None:
    """
    Augmente la valeur associée à la clé matière de 1, sauf si celle-ci vaut 'nsi'.
    """
    assert matiere in releve, "Erreur: matière absente"
    
    if matiere != 'nsi':
        releve[matiere] += 1    
```


```python
r1 = {'math': 10, 'ses': 12.5, 'nsi': 6}
augmente_note(r1, 'ses')
print(r1)
```

    {'math': 10, 'ses': 13.5, 'nsi': 6}



```python
augmente_note(r1, 'anglais')
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    /tmp/ipykernel_7122/3385823553.py in <module>
    ----> 1 augmente_note(r1, 'anglais')
    

    /tmp/ipykernel_7122/1063914476.py in augmente_note(releve, matiere)
          3     Augmente la valeur associée à la clé matière de 1, sauf si celle-ci vaut 'nsi'.
          4     """
    ----> 5     assert matiere in releve, "Erreur: matière absente"
          6 
          7     if matiere != 'nsi':


    AssertionError: Erreur: matière absente
    assert 'anglais' in {'math': 10, 'nsi': 6, 'ses': 13.5}



```python
augmente_note(r1, 'nsi')
print(r1)
```

    {'math': 10, 'ses': 13.5, 'nsi': 6}


---


```python
from typing import List


def mat2tab_v2(m: List[list]) -> list:
    """
    renvoie la matrice m sous la forme d'un tableau
    m: tableau de tableaux d'entiers
    """
    nb_element = len(m)
    a_plat = []
    for i in range(nb_element):
        for valeur in m[i]:
            a_plat.append(valeur)
    return a_plat
```


```python
mat = [[1, 2, 3], 
       [4, 5, 6,], 
       [7, 8, 9]]
t = mat2tab_v2(mat)
print(t)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
print(mat)
```

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


... ou de manière plus concise, en utilisant une compréhension de liste:


```python
def mat2tab_v3(m: List[list]) -> list:
    """
    renvoie la matrice m sous la forme d'un tableau
    m: tableau de tableaux d'entiers
    """
    return [valeur for i in range(len(m)) for valeur in m[i]]
```


```python
mat = [[1, 2, 3], 
       [4, 5, 6,], 
       [7, 8, 9]]
t = mat2tab_v3(mat)
print(t)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
print(mat)
```

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


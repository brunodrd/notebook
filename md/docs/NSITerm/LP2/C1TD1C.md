Le problème du rendu de monnaie
============================

## Analyse de l'énoncé

Pour plus de lisibilité, certaines variables suggérées par l'énoncé sont renommées.


```python
PIECES = [100, 50, 20, 10, 5, 2, 1] # système monnaitaire canonique


def rendu_aux(somme_a_rendre, solution, i):
    # Cas de base
    if somme_a_rendre == 0:
        return solution
    # Cas récursifs
    if somme_a_rendre < PIECES[i]:
        # On ne peut prendre la pièce, on essaie avec la suivante
        return rendu_aux(somme_a_rendre, solution, i+1)
    else:        
        solution.append(PIECES[i]) # On prend la pièce...
        # ... et on résoud le pb avec somme_a_rendre - PIECES[i]
        return rendu_aux(somme_a_rendre - PIECES[i], solution, i) 
```


```python
rendu_aux(73, [], 0)
```




    [50, 20, 2, 1]




```python
rendu_aux(68, [], 0)
```




    [50, 10, 5, 2, 1]




```python
rendu_aux(100, [], 0)
```




    [100]



## Autre solution

On remarque que l'appel de la fonction `rendu_aux` est assez lourd et que les deux derniers paramètres seront systématiquement `[]` et `0`. On pourrait alors simplifier l'appel avec:


```python
def rendu(somme):
    """ résoud récursivement le pb du rendu de monnaie"""
    
    def rendu_aux(somme_a_rendre, solution, i):
        """ Une fonction auxiliaire"""
        # Cas de base
        if somme_a_rendre == 0:
            return solution
        # Cas récursifs
        if somme_a_rendre < PIECES[i]:
            # On ne peut prendre la pièce, on essaie avec la suivante
            return rendu_aux(somme_a_rendre, solution, i+1)
        else:        
            solution.append(PIECES[i]) # On prend la pièce...
            # ... et on résoud le pb avec somme_a_rendre - PIECES[i]
            return rendu_aux(somme_a_rendre - PIECES[i], solution, i)
    
    return rendu_aux(somme, [], 0)

```


```python
# TESTS
assert rendu(0) == []
assert rendu(37) == [20, 10, 5, 2]
assert rendu(300) == [100, 100, 100]
```

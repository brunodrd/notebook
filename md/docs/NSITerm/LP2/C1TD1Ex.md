TD récursivité: Rendu de monnaie
===========================

*Pour travailler à la maison, sans installation de Jupyter, ouvrir le notebook avec basthon, depuis* [cette adresse](https://notebook.basthon.fr/?from=https://nsiboisdo.bdrd.fr/NSITerm/LP2/ipynb/C1TD1Ex.ipynb)

Le problème du rendu de monnaie est un problème d'algorithmique. Il s'énonce de la façon suivante: étant donné un système de monnaie (pièces et billets), comment rendre une somme donnée de façon optimale, c'est-à-dire avec le nombre minimal de pièces et billets ?

Par exemple, la meilleure façon de rendre 7 euros est de rendre un billet de cinq et une pièce de deux, même si d'autres façons existent (rendre 7 pièces de un euro, par exemple). 

Cependant pour certains systèmes de monnaie dits *canoniques*, l'**algorithme glouton** est optimal, c'est-à-dire qu'il suffit de rendre systématiquement la pièce ou le billet de valeur maximale — ce tant qu'il reste quelque chose à rendre. C'est la méthode employée en pratique, ce qui se justifie car la quasi-totalité des systèmes ayant cours dans le monde sont canoniques. 

[Source: wikipedia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_rendu_de_monnaie)

## Modélisation du problème

On considère un système monétaire canonique $S=\{p_1, p_2, \cdots, p_n\}$, avec $p_1>p_2>\cdots >p_n$. On appelle $v$ la valeur à rendre et $sol$ la solution du problème.  
Le problème du rendu de monnaie peut être vu comme un problème de choix de pièces (billets) ou ... pas, suivant la valeur à rendre.  
Si la valeur $v$ à rendre est nulle, on a terminé, il suffit de renvoyer la solution. Dans le cas contraire, 
on compare $v$ à la valeur de la i-ème pièce $S\left[i\right]$:  

* si la valeur à rendre est plus petite que la valeur de la i-ème pièce, on ne peut évidemment pas choisir cette dernière; il faudra essayer de **rendre la monnaie** avec la prochaine pièce;
* sinon, la pièce peut être choisie et doit être ajoutée à la solution et on doit essayer de **rendre la monnaie**  sur $v-S\left[ i\right]$.

!!! question "A faire"
    On adopte une démarche récursive pour résoudre ce problème. En utilisant la description précédente:  
    
    * identifier le cas de base et le ou les cas récursifs;
    * coder une fonction `rendu` dont la signature est donnée dans la cellule suivante.

## Codage


```python
def rendu(v, sol, i):
    """
    v (entier): valeur à rendre;
    sol (liste python): la solution
    i (entier): index de la pièce à tester
    """
    if ... # Cas de base
    ...
    else:
        ... # Cas récursifs
```

## Tests

Tester votre fonction


```python
S = [500, 200, 100, 50, 20, 10, 5, 2, 1]
assert rendu(0, [], 0) == []
assert rendu(37, [], 0) == [20, 10, 5, 2]
assert rendu(300, [], 0) == [200, 100]
```

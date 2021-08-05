# -*- coding: utf-8 -*-
from typing import List


def tri_insertion(t: List[int]) -> None:
    """
    Trie le tableau t par ordre croissant;
    effectue un tri "en place"
    """
    for i in range(1,len(t)):
        elt_a_classer = t[i]
        j = i
        #décalage des éléments du tableau pour trouver la place de t[i]
        while j>0 and t[j - 1] > elt_a_classer:
            t[j] = t[j - 1]
            j = j - 1
        #on insère l'élément à sa place
        t[j] = elt_a_classer

# -*- coding: utf-8 -*-
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer


class Cell:
    """ Une classe pour les listes chainées"""
    
    def __init__(self, v, s):
        self.val = v
        self.suiv = s

def longueur_iter(l):
    n = 0
    cellule = l
    while cellule is not None:
        n += 1
        cellule = cellule.suiv
    return n

input_long = [
    Args(Cell(1, None)), Args(Cell(2, Cell(3, Cell(10, None))))
]

q1 = ExerciseFunction(
    longueur_iter,
    input_long,
    result_renderer=PPrintRenderer(width=20),
)

def nieme(n, l):
    assert n >= 0 and l is not None, "Erreur: recherche impossible"
    if n == 0:
        return l.val
    else:
        return nieme(n - 1, l.suiv)

input_nieme = [
    Args(2, Cell(2, Cell(3, Cell(10, None)))),
    Args(1, Cell(2, Cell(3, Cell(10, None)))),
]

q2 = ExerciseFunction(
    nieme,
    input_nieme,
    result_renderer=PPrintRenderer(width=20),
)


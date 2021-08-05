#!/usr/bin/env python
# coding: utf-8
# %%
from typing import List


def max_tab(t: List[int]) -> int:
    """
    renvoie le maximum d'un tableau t;
    t: tableau d'entiers, non vide
    """
    assert len(t) > 0, "Erreur: tableau vide"
    m = t[0]
    for i in range(1, len(t)):
        if t[i] > m:
            m = t[i]
    return m

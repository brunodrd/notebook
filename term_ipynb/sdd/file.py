"""
Opérations du type abstrait file
"""

from pile import *


def creer_file():
    """
    renvoie une file vide
    """
    return (creer_pile(), creer_pile())

def enfiler(f, val):
    """
    enfile val dans la file f
    """
    p_in = f[0]
    #A compléter
    empiler(p_in, val)
    
def defiler(f):
    """
    défile f et renvoie la valeur défilée
    """
    assert not est_filevide(f), "Erreur: file vide"
    #A compléter
    p_in, p_out = f[0], f[1]
    if est_pilevide(p_out):
        while not est_pilevide(p_in):
            empiler(p_out, depiler(p_in))
    return depiler(p_out)

def est_filevide(f):
    """
    renvoie un booléen signalant l'état de la file
    """
    p_in, p_out = f[0], f[1]
    return est_pilevide(p_in) and est_pilevide(p_out)
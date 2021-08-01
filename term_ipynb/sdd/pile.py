"""
Operations du type abstrait Pile
"""


def creer_pile(n=None):
    """
    Créer une pile vide; le paramètre optionnel inutilisé n
    est maintenu pour une compatibilité avec la pile bornée
    """
    return []

def est_pilevide(p):
    """
    Retourne un booléen signalant une pile vide
    """
    return len(p) == 0

def depiler(p):
    """
    Dépile la valeur au sommet de la pile et la renvoie
    """
    assert not est_pilevide(p), "Erreur: pile vide"
    return p.pop()
    
def empiler(p, val):
    """
    Empile val dans la pile p
    """
    p.append(val)
    
def sommet(p):
    """
    Renvoie la valeur au sommet de la pile sans la dépiler
    """
    return p[-1]
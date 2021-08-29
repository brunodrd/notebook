# -*- coding: utf-8 -*-
"""
Diverses fonctions utiles à l'affichage du processus de 
résolution du problèmes des tours de Hanoï
"""

N = 6


def gen_disk(n, total_disk):
    """
    génère un disque de taille n, en renvoyant une chaine de caractères de largeur
    2*total_disk+1 et composée de 2n caractères '=', 2(total_disk-n) caractères ' ' (espaces)
    et d'un caractère '|' au centre.
    Exemple: gen_disk(3, 4) renvoie ' ===|=== '.
    """
    demi_disk = (total_disk - n) * ' ' + n * '='
    return ''.join((demi_disk, '|', demi_disk[::-1]))

def deplacer(jeu, orig, dest):
    """
    déplace le dernier disque de la tour 'orig' de 'jeu', vers la tour
    'dest' de destination.
    jeu: dictionnaire de la forme {'A':[], 'B':[], 'C':[]}
    orig, dest: clés du dictionnaire jeu.
    """
    jeu[dest].append(jeu[orig].pop())

def affiche(jeu, total_disk):
    """
    affiche un jeu
    """
    def gen_tour(id_tour):
        t = [gen_disk(k, total_disk) for k in jeu[id_tour]]
        while len(t) <= total_disk:
            t.append(gen_disk(0, total_disk))
        return t
    tA, tB, tC = gen_tour('A'), gen_tour('B'), gen_tour('C')
    # Affichage des contenu, en commençant par le haut
    for i in range(total_disk-1, -1, -1):
        print(tA[i], ' '*3, tB[i], ' '*3, tC[i])
    print('-' * (3 * (2*total_disk + 1) + total_disk + 7))
    print()

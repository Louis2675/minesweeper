"""
Fichier contenant les principales fonctions du noyau du programme.
"""

from saisie import *

def creuser(grille, TAILLE_GRILLE):
    choix_case = saisie_creuser(TAILLE_GRILLE)
    grille[choix_case[0]][choix_case[1]] = 1


def compter_cases(grille):
    etat = saisie_etat()
    cpt = 0
    for i in range(0, len(grille)):
        for j in range(0, len(grille[0])):
            if grille[i][j] == etat:
                cpt = cpt + 1


def voisins(grille, x, y):
    voisins = []
    TAILLE_GRILLE = len(grille)
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < TAILLE_GRILLE and 0 <= j < TAILLE_GRILLE and (i, j) != (x, y):
                voisins.append((i, j))
    return voisins


def incrementer_voisins(grille, x, y):
    bombes_voisines = 0
    for voisin in voisins(grille, x, y):
        if grille[voisin[0]][voisin[1]]["bombe"] == 1:
            bombes_voisines += 1
    grille[x][y]["voisins"] = bombes_voisines


def decouvrir_zone_securisee(grille, x, y):
    TAILLE_GRILLE = len(grille)
    a_decouvrir = [(x, y)]
    decouvertes = set()

    while a_decouvrir:
        cx, cy = a_decouvrir.pop()
        if (cx, cy) not in decouvertes:
            decouvertes.add((cx, cy))
            incrementer_voisins(grille, cx, cy)
            if grille[cx][cy]["voisins"] == 0:
                for vx, vy in voisins(grille, cx, cy):
                    if (vx, vy) not in decouvertes and grille[vx][vy]["bombe"] == 0:
                        a_decouvrir.append((vx, vy))

    for dx, dy in decouvertes:
        grille[dx][dy]["revelee"] = True


def decouvrir(grille, x, y):
    if grille[x][y]["bombe"] == 1:
        return False
    incrementer_voisins(grille, x, y)
    if grille[x][y]["voisins"] == 0:
        decouvrir_zone_securisee(grille, x, y)
    else:
        grille[x][y]["revelee"] = True
    return True



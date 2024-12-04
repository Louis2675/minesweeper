"""
Fichier contenant les parametres d'initialisation du programme.
"""
from random import randint
from affichage import afficher_grille
from parametres import TAILLE_GRILLE

def generer_grilles(TAILLE_GRILLE):
    grille = [[{
        "bombe": False,
        "voisins": 0,
        "drapeau": False,
        "revelee": False
    } for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]
    return grille


def generer_bombes(nb_bombes, TAILLE_GRILLE=TAILLE_GRILLE):
    cpt_bombes = 0
    bombes = []
    while cpt_bombes < nb_bombes:
        x, y = randint(0, TAILLE_GRILLE - 1), randint(0, TAILLE_GRILLE - 1)
        if (x, y) not in bombes:
            bombes.append((x, y))
            cpt_bombes += 1
    return bombes


def saisir_bombes(grille, bombes):
    for bombe in bombes:
        grille[bombe[0]][bombe[1]]["bombe"] = True


if "__main__" == __name__:
    grille = generer_grilles(TAILLE_GRILLE)
    saisir_bombes(grille, generer_bombes(5, TAILLE_GRILLE))
    afficher_grille(grille, TAILLE_GRILLE, reveler_bombes=True)

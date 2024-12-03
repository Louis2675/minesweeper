"""
Fichier contenant les differentes fonctions et procedures associes aux affichages.
"""

def afficher_grille(grille, TAILLE_GRILLE, reveler_bombes=False):
    for i in range(TAILLE_GRILLE):
        for j in range(TAILLE_GRILLE):
            if grille[i][j] == -1 and reveler_bombes:
                print("B", end=" ")
            elif grille[i][j] == -1:
                print(".", end=" ")
            elif grille[i][j] == 0:
                print(".", end=" ")
        print()
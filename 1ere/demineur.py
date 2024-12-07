"""
Fichier principal du jeu de démineur, il permet de demarrer la partie
"""

from noyau import *
from affichage import *
from parametres import *
from initialisation import *

def jouer_au_demineur():
    """
    Fonction principale du jeu de démineur
    """
    print("Bienvenue dans le jeu de démineur !")
    continuer = True
    while continuer:
        print("Nouvelle partie")
        continuer = input("Voulez-vous continuer ? (o/n) : ") == "o"
        grille = generer_grilles(TAILLE_GRILLE)
        saisir_bombes(grille, generer_bombes(NB_MINES, TAILLE_GRILLE))
        
"""
Fichier contenant l'integralite des saisies
"""

def saisie_creuser(TAILLE_GRILLE):
    saisie = input('Entrez les coordonnees de la case a creuser sous la forme "x,y" : ')
    coordonees = saisie.split(',')
    try:
        coordonees = (int(coordonees[0]), int(coordonees[1]))
    except ValueError:
        print("Veuillez entrer deux ENTIERS séparés par une virgule")
        return saisie_creuser(TAILLE_GRILLE)
    except IndexError:
        print("Veuillez entrer DEUX coordonnees")
        return saisie_creuser(TAILLE_GRILLE)
    if coordonees[0] < 0 or coordonees[0] >= TAILLE_GRILLE or coordonees[1] < 0 or coordonees[1] >= TAILLE_GRILLE:
        print("Coordonnees trop extremes")
        return saisie_creuser(TAILLE_GRILLE)
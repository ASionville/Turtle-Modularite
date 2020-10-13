from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle as t

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''

    # La hauteur dépend du niveau de l'étage
    y = y_sol + niveau * 60

    # On dessine la facade sans les elements dedans
    facade(x, y_sol, couleur, niveau)

    # On construit les 3 éléments (1 porte et 2 fenetres)
    elements = []

    # On choisit aléatoirement une fenêtre seule ou un balcon avec
    for _ in range(3):
        choix_fenetre = randint(0,1)
        elements.append(["fenetre", "balcon"][choix_fenetre])

    # On dessine chaque élement
    for i in range(len(elements)):
        if elements[i] == "balcon":
            fenetre_balcon(x - 70 + (i + 1) * 12.5 + (i * 2 + 2) * 15,
                           y + 5)
        else:
            fenetre(x - 70 + (i + 1) * 12.5 + (i * 2 + 2) * 15,
                    y + 15)

if __name__ == '__main__':
    etage(0,0,"red",1)
    # On ferme la fenêtre s'il y a un clique gauche
    t.exitonclick()
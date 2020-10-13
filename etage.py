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
    # dessin des murs

    # dessin des 3 Eléments
    lst = []
    facade(0, 0, couleur, 1)
    for i in range(0,3):
        nbr = randint(0,2)
        if nbr == 0:
            lst.append(fenetre(x,y_sol + (niveau + 1) * 60))
        else:
            lst.append(fenetre_balcon(x,y_sol + (niveau + 1) * 60))
        shuffle(lst)
    print(lst[0,1,2])







if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    t.exitonclick()
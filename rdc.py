from facade import facade
from random import shuffle, randint
from porte import porte
from fenetre import fenetre
import turtle

def rdc(x, y_sol, c_facade, c_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''

    # On dessine la facade sans les elements dedans
    facade(x, y_sol, c_facade, 0)

    
    elements = ["porte"]

    # On choisit aléatoirement une fenêtre seule ou un balcon avec

    for _ in range(2):
        elements.append("fenetre")
        
    shuffle(elements)

    # On dessine chaque élement
    for i in range(len(elements)):

        if elements[i] == "porte":
            porte(x - 70 + (i + 1) * 12.5 + (i * 2 + 1) * 15,
                  y_sol, c_porte)

        else:
            fenetre(x - 70 + (i + 1) * 12.5 + (i * 2 + 2) * 15,
                    y_sol + 15)
    

if __name__ == '__main__':
    rdc(0,0,"red","pink")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
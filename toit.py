from random import randint
from toit1 import toit1
from toit2 import toit2
import turtle

def toit(x, y_sol, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Cette fonction dessine au hasard un des 2 types de toit

    '''
    choix_toit = randint(1,2)
    if choix_toit == 1:
        toit1(x, y_sol, niveau)
    else:
        toit2(x, y_sol, niveau)
    turtle.penup()

if __name__ == '__main__':
    toit(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
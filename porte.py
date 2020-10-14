from porte1 import porte1
from porte2 import porte2
from rectangle import rectangle
from random import randint
import turtle

def porte(x, y, couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    Cette fonction dessine au hasard un des 2 types de porte
    '''

    turtle.penup()

    # Choix de la porte (aléatoire)
    choix_porte = randint(1, 2)

    if choix_porte == 1:
        porte1(x, y, couleur)
    else:
        porte2(x, y, couleur)
        
    turtle.penup()

if __name__ == '__main__':
    porte(0, 0, "red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

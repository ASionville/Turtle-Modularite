import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    """
    Paramètres :
        x : abcisse du centre de la facade
        y_sol : ordonnée du sol de la rue
        couleur : couleur de la facade
        niveau : num du niveau (0 pour le rdc, ...)
    remarque :
        Facade dessine une facade sans les élèments interieurs
    """

    turtle.penup()

    turtle.fillcolor(couleur)

    y = y_sol + niveau * 60 #Ordonnée en bas de l'étage

    turtle.setposition(x, y)
    turtle.begin_fill()

    rectangle(x, y, 140, 60)

    turtle.end_fill()
    turtle.penup()

if __name__ == '__main__':
    facade(0,0,"red",0)
    #On ferme la fenêtre si il y a un clique gauche
    turtle.exitonclick()
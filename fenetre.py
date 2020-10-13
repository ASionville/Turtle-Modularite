from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''

    turtle.penup()

    turtle.pencolor("grey")

    turtle.fillcolor("white")
    turtle.setposition(x - 15, y)

    turtle.begin_fill()

    rectangle(x - 15, y, 30, 30)

    turtle.end_fill()
    turtle.pencolor("black")
    turtle.penup()

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
from rectangle import rectangle
import turtle as T

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
    T.setx(x-15)
    T.sety(y)
    T.pencolor("grey")
    T.pendown()
    T.fillcolor("white")
    T.begin_fill()
    rectangle(x,y,30,30)
    T.penup()
    T.end_fill()
    T.setposition(x+15,y)


if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    T.exitonclick()
import turtle
from rectangle import rectangle
def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte dont le haut est un demi cercle
        La porte a une largeur totale de 30 pixels
        La partie rectangulaire a une hauteur de 40 pixels
        La partie semi circulaire a un rayon de 15 pixels
    '''
    turtle.fillcolor(couleur)
    turtle.pencolor(couleur)
    turtle.begin_fill()
    rectangle(x - 15, y, x + 15, y + 40)
    turtle.end_fill()

    turtle.setposition(x - 15, y + 40)

    turtle.begin_fill()
    turtle.setheading(-90)
    turtle.circle(7.5, -180)
    turtle.end_fill()
    turtle.pencolor('black')
    turtle.setheading(0)


if __name__ == '__main__':
    porte2(0,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
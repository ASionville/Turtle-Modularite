import turtle
from trait import trait

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

    turtle.penup()

    turtle.fillcolor(couleur)

    turtle.setposition(x - 15, y)

    turtle.begin_fill()

    trait(x - 15, y,
          x + 15, y)

    trait(x + 15, y,
          x + 15, y + 40)
    
    turtle.pendown()

    turtle.setheading(90)
    turtle.circle(15, 180)

    trait(x - 15, y + 40,
          x - 15, y)

    turtle.end_fill()

    turtle.penup()


if __name__ == '__main__':
    porte2(20,0,"red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
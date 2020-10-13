import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''

    turtle.penup()
    # On dessine le cadre en gris pour plus de contraste avec le balcon
    turtle.pencolor("grey")

    turtle.fillcolor("white")
    turtle.setposition(x - 15, y)

    turtle.begin_fill()

    # La porte-fenêtre est un rectangle de 30 par 50
    rectangle(x - 15, y, 30, 50)

    turtle.end_fill()
    turtle.penup()

    # On dessine le balcon en noir pour plus de contraste avec le balcon
    turtle.pencolor("black")
    turtle.left(90)

    trait((turtle.xcor() - 4.2), turtle.ycor(),
          (turtle.xcor() - 4.2), turtle.ycor())

    trait(turtle.xcor(), turtle.ycor(),
          turtle.xcor(), (turtle.ycor() + 25))

    # On dessine tous les barreaux
    for i in range (9):

        trait((turtle.xcor() + 4.2), turtle.ycor() - 25,
              (turtle.xcor() + 4.2), turtle.ycor())

    rectangle(x - 15, y, 38.4, 25)
    turtle.right(90)


if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
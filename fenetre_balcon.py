import turtle as T
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

    T.setx(x-15)
    T.sety(y)
    T.pencolor("grey")
    T.pendown()
    T.fillcolor("white")
    T.begin_fill()
    rectangle(x,y,30,50)
    T.penup()
    T.end_fill()
    # porte-fenetre

    T.pencolor("black")
    T.left(90)
    trait((T.xcor()-4.2),T.ycor(),(T.xcor()-4.2),T.ycor())
    trait(T.xcor(),T.ycor(),T.xcor(),(T.ycor()+25))
    for i in range (0,9):
        trait((T.xcor()+4.2),T.ycor()-25,(T.xcor()+4.2),T.ycor())
    rectangle(x,y,38.4,25)


    # balcon




if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    T.exitonclick()
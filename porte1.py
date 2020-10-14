import turtle
from rectangle import rectangle

def porte1(x, y, couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte de 30 pixels de large pour 50 pixels de hauteur
    '''
    
    turtle.penup()
    turtle.fillcolor(couleur)

    # On va à la première position avant de commencer à remplir
    # pour éviter les bugs
    turtle.setposition(x - 15, y)
    turtle.begin_fill()

    rectangle(x, y, 30, 50)

    turtle.end_fill()
    turtle.pencolor("black")
    turtle.penup()

if __name__ == '__main__':
    porte1(0, 0, "red")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()

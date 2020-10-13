import turtle
from trait import trait

def rectangle(x,y,w,h):
    '''
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    Cette fonction dessine un rectangle Le point de coordonnées (x,y) est
    sur le côté en bas au milieu
    '''
    turtle.penup() # On lève le crayon
    turtle.setposition(x, y) # On position le crayon
    turtle.pendown() # On baisse le crayon
    trait(x, y, x + w, y)
    trait(x + w, y, x + w, y + h)
    trait(x, y, x, y + h)
    trait(x, y + h, x + w, y + h)
    turtle.penup()

if __name__ == '__main__':
    rectangle(0,0,150,100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
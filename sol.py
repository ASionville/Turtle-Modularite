import turtle
from trait import trait

def sol(y_sol):
    """
    Paramètres :
        Y_sol : ordonnée du sol de la rue
    cette fonction dessine un trait horizontale de 3 pixels d'épaisseur.
    """
    turtle.pensize(3)
    turtle.speed(10)

    trait(-500, y_sol, 500, y_sol)

    turtle.speed(6)
    turtle.pensize(1)


if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre si il y a in clique gauche
    turtle.exitonclick()
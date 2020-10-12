import turtle as t
from Trait import trait

def sol(y_sol):
    """
    Paramètres :
        Y_sol : ordonnée du sol de la rue
    cette fonction dessine un trait horizontale de 3 vpixels d'épaisseur.
    """
    t.pensize(3)
    trait(-90,y_sol,90,y_sol)


if __name__ == '__main__':
    sol(0)
    # On ferme la fenêtre si il y a in clique gauche
    t.exitonclick()
import turtle
from trait import trait

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    turtle.penup()
    turtle.speed(10)
    for i in range(10):
        trait(x,
            y_sol + (niveau + 1) * 60 + i,
            x + 140,
            y_sol + (niveau + 1) * 60 + i)
        
    turtle.penup()
    turtle.speed(6)

if __name__ == '__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
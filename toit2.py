import turtle
from rectangle import rectangle

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''

    y = y_sol + (niveau + 1) * 60 #Ordonnée en bas de l'étage

    turtle.penup()
    turtle.fillcolor("black")

    turtle.setposition(x - 70, y)
    
    turtle.begin_fill()

    rectangle(x, y, 140, 10)

    turtle.end_fill()
    turtle.penup()
    turtle.setposition(x, y)

if __name__ == '__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
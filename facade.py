import turtle as t
#from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    """
    Paramètres :
        x : abcisse du centre de la facade
        y_sol : ordonnée du sol de la rue
        couleur : couleur de la facade
        niveau : num du niveau (0 pour le rdc, ...)
    remarque :
        Facade dessine une facade sans les élèments interieurs
    """
    t.penup()
    t.setx(x-70)
    t.sety(y_sol-30)
    t.pendown()
    t.setposition(x+70,y_sol-30)
    t.setposition(x+70,y_sol+30)
    t.setposition(x-70,y_sol+30)
    t.setposition(x-70,y_sol-30)
    t.penup()
    t.fillcolor(couleur)
    t.begin_fill()
    t.filling()
    t.end_fill()



if __name__ == '__main__':
    facade(0,0,"red",0)
    #On ferme la fenêtre si il y a un clique gauche
    t.exitonclick()
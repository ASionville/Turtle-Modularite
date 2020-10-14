import turtle
from trait import trait

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''

    turtle.fillcolor(0, 0, 0)

    # Le toit 1 est un triangle

    bas_g = (x - 80,
             y_sol + (niveau + 1) * 60) #Coin en bas à gauche
    bas_d = (x + 80,
             y_sol + (niveau + 1) * 60) #Coin en bas à droite
    haut = (x,
            y_sol + (niveau + 1) * 60 + 40) #Coin en haut

    turtle.begin_fill()
    
    # On dessine le triangle
    trait(bas_g[0], bas_g[1],
          haut[0], haut[1])

    trait(haut[0], haut[1],
          bas_d[0], bas_d[1])

    trait(bas_d[0], bas_d[1],
          bas_g[0], bas_g[1])
    
    turtle.end_fill()

if __name__ == '__main__':
    toit1(0, 0, 0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
import turtle

def trait(x1, y1, x2, y2):
    '''
    Paramètres :
        x1, y1 : coordonnées du premier point
        x2, y2 : coordonnées du deuxième point
    Cette fonction trace un trait entre les deux points
    '''

    turtle.penup() # On lève le crayon

    turtle.setposition(x1, y1) # On position le crayon
    turtle.pendown() # On baisse le crayon
    turtle.setposition(x2, y2) # On repositionne le crayon ==> trace un trait

    turtle.penup() # On lève le crayon 
    
if __name__ == '__main__':
    trait(0, 0, 100, 100)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    
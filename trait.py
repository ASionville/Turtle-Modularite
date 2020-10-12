import turtle

def trait(x1, y1, x2, y2):
    '''
    '''
    turtle.penup() # On lève le crayon
    turtle.setposition(x1, y1) # On position le crayon
    turtle.pendown() # On baisse le crayon
    turtle.setposition(x2, y2) # On repositionne le crayon ==> trace un trait
    turtle.penup() # On lève le crayon 
    
if __name__ == '__main__':
    trait(0,0,100,150)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    
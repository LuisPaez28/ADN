import turtle
from random import randrange

#Creo los nucleotidos por separado
#Cada letra dentro de un nucleotido se refiere a un atomo  o enlace. Por ejemplo la N es el nitrogeno, la O el oxigeno, etc. 
#nucleotido
a = ['N','N','N','N','NH']
#Guanina
g = ['N','N','N','NH','N','O']
#Timina
t = ['N','O','N','O','CH']
#Citosina
c = ['N','N','O','NH']

#Arreglo con todas las posibilidades
posibilidades = [a,g,t,c]

def colorin(nucleoti):
    if nucleoti == a:
        return 'red'
    if nucleoti == g:
        return 'blue'
    if nucleoti == t:
        return 'green'
    if nucleoti == c:
        return 'yellow'
inicio = 10
#Creo el 5' 
for x in range(100):

    n1 = posibilidades[randrange(4)]
    n2 = posibilidades[randrange(4)]
    n3 = posibilidades[randrange(4)]
    n4 = posibilidades[randrange(4)]
    cinco = [n1,n2,n3,n4]

    turtle.title('ADN')
    for y in range(4):
        seleccionado = cinco[y]
        colorUsar = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.left(90)
        fosf.forward(inicio+2)

        nucleo = turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.color(colorUsar)
        nucleo.pensize(4)
        nucleo.left(90)
        nucleo.pu()
        nucleo.forward(inicio)
        nucleo.down()
        nucleo.right(90)
        nucleo.forward(30)
        
        inicio+=10
    inicio+=10
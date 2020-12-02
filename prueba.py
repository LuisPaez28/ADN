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

#Probamos con una base
acidobacteria = [t,g,g,a,a,g,c,t,t,g,a,a,t,c,c,g,g,a,g,a,g,g,g,a,t,g,t,g,g,a,a,t,t,c,c,a,g,g,t,g,t,a,g,g,g,t,g,a,a,a,t,g,c,g,t,a,g,a,t,a,t,t,g,g,a,g,g,a,a,c,a,c,c,g,g,t,g,g,c,g,a,a,g,g,c,g,g,c,t,c,c,t,g,g,a,c,c,g,a,t,t,g,a,c,g,c,t,g,a,g,g,c,g,c,g,a,a,a,g,c,c,g,g,g,g,a,g,c,a,a,a,c,g,g,g,a,t,t,a,g,a,t,a,c,c,c,g,g,t,a,g,t,c,c,t,g,g,c,c,c,t,a,a,a,c,g,a,t,g,a,a,t,g,c,t,t,g,g,t,g,t,g,g,g,g,g,a,t,c,g,a,t,c,c,c,t,g,c,c,g,t,g,c,c,a,a,c,t,a,a,c,t,t,a,a,c,a,t,t,c,c,c,c,t,g,g,g,a,g,t,a,c,g,g,t,c,g,c,a,a,g,g,c,t,g,a,a,a,c,t,c,a,a,a,g,g,a,a,t,t,g,a,c,g,g,g,g,g,c,c,c,g,c,a,c,a,a,g,c,g,g,t,g,g,a,g,c,a,t,g,t,g,g,t,t,t,a,a,t,t,c,a,c,g,c,a,a,c,g,c,a,a,a,a,c,c,t,t,a,c,c,c,a,g,c,t,c,g,a,a,a,t,g,c,g,a,t,g,a,c,c,g,c,c,g,g,t,g,a,a,a,g,c,c,g,g,t,t,t,c,c,c,a,g,a,c,a,t,c,t,g,t,a,t,a,g,g,t,g,c,t,g,c,a,t,g,g,c,t,g,t,c,c,t,c,a,g,c,t,c,g,t,g,t,c,g,t,g,a,g,a,t,g,t,t,g,g,g,t,t,a,a,g,t,c,c,c,g,c,a,a,c,g,a,g,c,g,c,a,a,c,c,c,t,t,g,t,t,c,t,c,t,g,t,t,g,c,c,a,t,c,a,g,t,c,a,a,c,t,g,g,g,c,c,t,c,t,g,a,a,a,a,c,t,g,c,c,g,g,a,t,a,a,a,c,c,g,g,a,g,g,a,a,g,g,t,g,g,g,g,a,t,g,a,c,g,t,c,a,a,g,t,c,c,t,g,g,c,c,t,t,t,a,t,g,t,c,t,g,g,g,g,c,t,a,c,a,c,a,c,t,g,c,t,a,c,a,a,t,g,g,c,c,g,g,a,c,a,a,a,g]
otraParte =[]
def rellenado(bacteria):
    base = [a,t,g,c]
    completar = [t,a,c,g]

    for x in range(len(bacteria)):
        if bacteria[x] == base[0]:
            otraParte.append(completar[0])
        if bacteria[x] == base[1]:
            otraParte.append(completar[1])
        if bacteria[x] == base[2]:
            otraParte.append(completar[2])
        if bacteria[x] == base[3]:
            otraParte.append(completar[3]) 

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
inicio2 = 10
inicioBien = 10


turtle.title('ADN')
turtle.setup((1530)/2, 1000, 0, 0)
turtle.screensize(20,8000)
turtle.hideturtle()
turtle.penup()
turtle.goto(-10,-40)
turtle.write("Prueba",False,"left",("arial", 20, "bold italic"))

rellenado(acidobacteria)

#Simulo el ADN
for x in range(len(acidobacteria)):
    seleccionado = acidobacteria[x]
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
    
    seleccionado = otraParte[x]
    usarColor = colorin(seleccionado)

    fosf = turtle.Turtle()
    fosf.hideturtle()
    fosf.color('black')
    fosf.pensize(8)
    fosf.penup()
    fosf.forward(60)
    fosf.left(90)
    fosf.pendown()
    fosf.forward(inicio2+2)

    nucleo =turtle.Turtle()
    nucleo.hideturtle()
    nucleo.speed(10)
    nucleo.pensize(4)
    nucleo.left(90)
    nucleo.pu()
    nucleo.forward(inicio2)
    nucleo.right(90)
    nucleo.forward(30)
    nucleo.pendown()
    nucleo.pencolor(usarColor)
    nucleo.forward(30)
    inicio2+=10
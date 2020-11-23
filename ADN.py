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
inicio2 = 10

turtle.title('ADN')
turtle.setup(1530, 1000, 0, 0)
turtle.screensize(20,8000)
turtle.hideturtle()
turtle.penup()
turtle.goto(-10,-40)
turtle.write("Arreglo 5'",False,"left",("arial", 20, "bold italic"))
turtle.goto(-200,-40)
turtle.write("Errores",False,"left",("arial", 20, "bold italic"))
turtle.goto(-500,300)
turtle.pencolor('red')
turtle.write("Adenina",False,"left",("arial", 18, "bold italic"))
turtle.goto(-500,250)
turtle.pencolor('blue')
turtle.write("Guanina",False,"left",("arial", 18, "bold italic"))
turtle.goto(-500,200)
turtle.pencolor('green')
turtle.write("Timina",False,"left",("arial", 18, "bold italic"))
turtle.goto(-500,150)
turtle.pencolor('yellow')
turtle.write("Citocina",False,"left",("arial", 18, "bold italic"))

#Simulo el ADN
for x in range(5):
#Creo el 5' 
    n1 = posibilidades[randrange(4)]
    n2 = posibilidades[randrange(4)]
    n3 = posibilidades[randrange(4)]
    n4 = posibilidades[randrange(4)]
    cinco = [n1,n2,n3,n4]
#Creo el 3'
    n5 = posibilidades[randrange(4)]
    n6 = posibilidades[randrange(4)]
    n7 = posibilidades[randrange(4)]
    n8 = posibilidades[randrange(4)]
    tres = [n5,n6,n7,n8]

    for y in range(4):
        seleccionado = cinco[y]
        colorUsar = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.left(180)
        fosf.penup()
        fosf.forward(200)
        fosf.pendown()
        fosf.right(90)
        fosf.forward(inicio+2)

        nucleo = turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(200)
        nucleo.pendown()
        nucleo.color(colorUsar)
        nucleo.pensize(4)
        nucleo.right(90)
        nucleo.pu()
        nucleo.forward(inicio)
        nucleo.down()
        nucleo.right(90)
        nucleo.forward(30)
        
        inicio+=10
    
    for w in range(4):
        seleccionado = tres[w]
        usarColor = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.penup()
        fosf.left(180)
        fosf.forward(140)
        fosf.right(90)
        fosf.pendown()
        fosf.forward(inicio2+2)

        nucleo =turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(200)
        nucleo.right(180)
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
inicio = 10
inicio2 =10
inicioBien = 10
#Simulo el ADN
for f in range(5):
#Creo el 5' 
    n1 = posibilidades[randrange(4)]
    n2 = posibilidades[randrange(4)]
    n3 = posibilidades[randrange(4)]
    n4 = posibilidades[randrange(4)]
    cinco = [n1,n2,n3,n4]
#Creo el 3'
    n5 = posibilidades[randrange(4)]
    n6 = posibilidades[randrange(4)]
    n7 = posibilidades[randrange(4)]
    n8 = posibilidades[randrange(4)]
    tres = [n5,n6,n7,n8]

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
    
    for w in range(4):
        seleccionado = tres[w]
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
    #Hacemos revision en el primer nucleotido
    if n1==t:
        n5=a
    if n1==g:
        n5=c
    if n1==a:
        n5=t
    if n1==c:
        n5=g
    #Hacemos revision en el segundo nucleotido
    if n2==t:
        n6=a
    if n2==g:
        n6=c
    if n2==a:
        n6=t
    if n2==c:
        n6=g
    #Hacemos revision en el tercer nucleotido
    if n3==t:
        n7=a
    if n3==g:
        n7=c
    if n3==a:
        n7=t
    if n3==c:
        n7=g
    #Hacemos la revision en el cuarto nucleotido
    if n4==t:
        n8=a
    if n4==g:
        n8=c
    if n4==a:
        n8=t
    if n4==c:
        n8=g
    tres=[n5,n6,n7,n8]
    #Mostrar resultados
    for i in range(4):
        seleccionado = tres[i]
        usarColor = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.penup()
        fosf.forward(60)
        fosf.left(90)
        fosf.pendown()
        fosf.forward(inicioBien+2)

        nucleo =turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.pensize(4)
        nucleo.left(90)
        nucleo.pu()
        nucleo.forward(inicioBien)
        nucleo.right(90)
        nucleo.forward(30)
        nucleo.pendown()
        nucleo.pencolor(usarColor)
        nucleo.forward(30)
        inicioBien+=10

            

#    inicio+=10
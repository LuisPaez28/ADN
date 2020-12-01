import turtle
from random import randrange
import math 

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

#Arreglo con todas las posibilidades
posibilidades = [a,g,t,c,a,g,t,c,a,g,t,c,a,g,t,c]
posiAT = [a,t,a,t,g,c,a,t,c,g]
posiCG = [c,g,c,g,a,t,c,g,a,t]

posibiA = [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,t,g,c,a,a,a,a,a,a,a]
posibiT = [t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,t,g,c,a,t,t,t,t,t]
posibiG = [g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,g,c,a,t,g,g,g,g]
posibiC = [c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,g,a,t,c,c,c]

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

inicioB = 10
inicio2B =10
inicioBien = 10

inicio3 = 10
inicio23 = 10
inicioBien3 = 10

inicioPartes = 10
inicio2Partes = 10
inicioBienPartes = 10

inicioBorrador = 50

brinco = 0

ini = 0
ini2 = 0

window = turtle.Screen()
window.bgcolor('gray')
turtle.title('ADN de Acidobacteria')
turtle.setup(1530, 1000, 0, 0)
turtle.screensize(20,8000)
turtle.hideturtle()
turtle.penup()
turtle.goto(-170,-40)
turtle.write("Arreglo 3'",False,"left",("arial", 20, "bold italic"))
turtle.goto(-15,-40)
turtle.write("Arreglo 5'",False,"left",("arial", 20, "bold italic"))
turtle.goto(-320,-40)
turtle.write("Errores",False,"left",("arial", 20, "bold italic"))
#turtle.goto(150,-40)
#turtle.write("Parte",False,"left",("arial", 20, "bold italic"))
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

def creaCinco(bacteria):
    base = [a,t,g,c]
    for x in range(len(bacteria)):
        if bacteria[x] == base[0]:
            otraParte.append(posibiT[randrange(len(posibiT))])
        if bacteria[x] == base[1]:
            otraParte.append(posibiA[randrange(len(posibiA))])
        if bacteria[x] == base[2]:
            otraParte.append(posibiC[randrange(len(posibiC))])
        if bacteria[x] == base[3]:
            otraParte.append(posibiG[randrange(len(posibiG))]) 
#Aqui se creo la otra parte de la cadena (con errores)
creaCinco(acidobacteria)

cinquin=[]
def creacinquin(arreglo):
    base = [a,t,g,c]
    respuesta = [t,a,c,g]
    for x in range(len(arreglo)):
        if arreglo[x] == base[0]:
            cinquin.append(respuesta[0])
        if arreglo[x] == base[1]:
            cinquin.append(respuesta[1])
        if arreglo[x] == base[2]:
            cinquin.append(respuesta[2])
        if arreglo[x] == base[3]:
            cinquin.append(respuesta[3])
#Aqi se creo cinquin, una respuesta correcta a base del lado derecho
#creacinquin(otraParte)

for x in range(0,len(acidobacteria),15):
#Creo el 5' 
    n1 = acidobacteria[x]
    n2 = acidobacteria[x+1]
    n3 = acidobacteria[x+2]
    n4 = acidobacteria[x+3]
    n5 = acidobacteria[x+4]
    n6 = acidobacteria[x+5]
    n7 = acidobacteria[x+6]
    n8 = acidobacteria[x+7]
    n9 = acidobacteria[x+8]
    n10 = acidobacteria[x+9]
    n11 = acidobacteria[x+10]
    n12 = acidobacteria[x+11]
    n13 = acidobacteria[x+12]
    n14 = acidobacteria[x+13]
    n15 = acidobacteria[x+14]
    cinco = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15]
#Creo el 3'
    creacinquin(otraParte)
    n16 = otraParte[x]
    n17 = otraParte[x+1]
    n18 = otraParte[x+2]
    n19 = otraParte[x+4]
    n20 = otraParte[x+5]
    n21 = otraParte[x+6]
    n22 = otraParte[x+7]
    n23 = otraParte[x+8]
    n24 = otraParte[x+9]
    n25 = otraParte[x+10]
    n26 = otraParte[x+11]
    n27 = otraParte[x+12]
    n28 = otraParte[x+13]
    n29 = otraParte[x+14]
    n30 = otraParte[x+15]
    tres = [n16,n17,n18,n19,n20,n21,n22,n23,n24,n25,n26,n27,n28,n29,n30]

    #Creo el arreglo de 3'
    cinQ = []
    base = [a,t,g,c]
    respuesta = [t,a,c,g]
    for l in range(len(tres)):
        if tres[l] == base[0]:
            cinQ.append(respuesta[0])
        if tres[l] == base[1]:
            cinQ.append(respuesta[1])
        if tres[l] == base[2]:
            cinQ.append(respuesta[2])
        if tres[l] == base[3]:
            cinQ.append(respuesta[3])

    tree = []
    for tr in range(len(cinco)):
        if cinco[tr] == base[0]:
            tree.append(respuesta[0])
        if cinco[tr] == base[1]:
            tree.append(respuesta[1])
        if cinco[tr] == base[2]:
            tree.append(respuesta[2])
        if cinco[tr] == base[3]:
            tree.append(respuesta[3])

    for y in range(15):
        seleccionado = cinco[y]
        colorUsar = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.left(180)
        fosf.penup()
        fosf.forward(300)
        fosf.pendown()
        fosf.right(90)
        fosf.forward(inicio+2)

        nucleo = turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(300)
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
    
    for w in range(15):
        seleccionado = tres[w]
        usarColor = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.penup()
        fosf.left(180)
        fosf.forward(240)
        fosf.right(90)
        fosf.pendown()
        fosf.forward(inicio2+2)

        nucleo =turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(300)
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

    #Aqui comienza el de 3'
    for m in range(15):
        if m == 2 or m == 5 or m == 8 or m == 11 or m==14:
            division = turtle.Turtle()
            division.hideturtle()
            division.penup()
            division.left(180)
            division.forward(140)
            division.pendown()
            division.pencolor('white')
            division.pensize(0.5)
            division.right(90)
            division.penup()
            division.forward(inicio3+5)
            division.pendown()
            division.right(90)
            for num in range(3):
                division.forward(10)
                division.pu()
                division.forward(10)
                division.pendown()

        seleccionado = cinco[m]
        colorUsar = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.left(180)
        fosf.penup()
        fosf.forward(140)
        fosf.pendown()
        fosf.right(90)
        fosf.forward(inicio3+2)

        nucleo = turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(140)
        nucleo.pendown()
        nucleo.color(colorUsar)
        nucleo.pensize(4)
        nucleo.right(90)
        nucleo.pu()
        nucleo.forward(inicio3)
        nucleo.down()
        nucleo.right(90)
        nucleo.forward(30)
        
        inicio3+=10
    for n in range(15):
        seleccionado = tres[n]
        usarColor = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.penup()
        fosf.left(180)
        fosf.forward(80)
        fosf.right(90)
        fosf.pendown()
        fosf.forward(inicio23+2)

        nucleo =turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(140)
        nucleo.right(180)
        nucleo.pensize(4)
        nucleo.left(90)
        nucleo.pu()
        nucleo.forward(inicio23)
        nucleo.right(90)
        nucleo.forward(30)
        nucleo.pendown()
        nucleo.pencolor(usarColor)
        nucleo.forward(30)
        inicio23+=10

    for ñ in range(15):
        seleccionado = cinQ[ñ]
        colorUsar = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.left(180)
        fosf.penup()
        fosf.forward(140)
        fosf.pendown()
        fosf.right(90)
        fosf.forward(inicioBien3+2)

        nucleo = turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.penup()
        nucleo.left(180)
        nucleo.forward(140)
        nucleo.pendown()
        nucleo.color(colorUsar)
        nucleo.pensize(4)
        nucleo.right(90)
        nucleo.pu()
        nucleo.forward(inicioBien3)
        nucleo.down()
        nucleo.right(90)
        nucleo.forward(30)
        
        inicioBien3+=10

#Aqui comienza el 5'
    for r in range(15):
        if r == 4 or r == 9 or r==14:
            division = turtle.Turtle()
            division.hideturtle()
            division.pendown()
            division.pencolor('white')
            division.pensize(0.5)
            division.left(90)
            division.penup()
            division.forward(inicioB+5)
            division.pendown()
            division.right(90)
            for num in range(3):
                division.forward(10)
                division.pu()
                division.forward(10)
                division.pendown()

        seleccionado = cinco[r]
        colorUsar = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.left(90)
        fosf.forward(inicioB+2)

        nucleo = turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.color(colorUsar)
        nucleo.pensize(4)
        nucleo.left(90)
        nucleo.pu()
        nucleo.forward(inicioB)
        nucleo.down()
        nucleo.right(90)
        nucleo.forward(30)
        
        inicioB+=10

    for h in range(15):
        seleccionado = tres[h]
        usarColor = colorin(seleccionado)

        fosf = turtle.Turtle()
        fosf.hideturtle()
        fosf.color('black')
        fosf.pensize(8)
        fosf.penup()
        fosf.forward(60)
        fosf.left(90)
        fosf.pendown()
        fosf.forward(inicio2B+2)

        nucleo =turtle.Turtle()
        nucleo.hideturtle()
        nucleo.speed(10)
        nucleo.pensize(4)
        nucleo.left(90)
        nucleo.pu()
        nucleo.forward(inicio2B)
        nucleo.right(90)
        nucleo.forward(30)
        nucleo.pendown()
        nucleo.pencolor(usarColor)
        nucleo.forward(30)
        inicio2B+=10
        #Mostrar resultados

    for i in range(15):
        seleccionado = tree[i]
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

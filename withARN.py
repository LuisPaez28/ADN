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
#Uracilo
u = ['N','O','NH','O']

#Arreglo con todas las posibilidades
posibilidades = [a,g,t,c,a,g,t,c,a,g,t,c,a,g,t,c]
posiAT = [a,t,a,t,g,c,a,t,c,g]
posiCG = [c,g,c,g,a,t,c,g,a,t]

#Metodo para especificar un color dependiendo de la cadena para su muestra grafica.
def colorin(nucleoti):
    if nucleoti == a:
        return 'red'
    if nucleoti == g:
        return 'blue'
    if nucleoti == t:
        return 'green'
    if nucleoti == c:
        return 'yellow'
    if nucleoti == u:
        return 'brown'

#Creo metodo para calcular la distribuci[on estandar]
def distrNorm(aleatorio,media,desvEstandar):
    sumatioria = math.fsum(aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio,aleatorio)
    return (sumatioria-6)*desvEstandar+media

#Construcci[on de ARN] en funcion del ADN corregido
def constrARN3(nucleotidos):
    nuc = [a,t,c,g]
    arnP = [u,a,g,c]
    arn = []
    for x in range (len(nucleotidos)):
        for xx in range(4):
            if nucleotidos[xx] == nuc[0]:
                arn.append(arnP[0])
            if nucleotidos[xx] == nuc[1]:
                arn.append(arnP[1])
            if nucleotidos[xx] == nuc[2]:
                arn.append(arnP[2])
            if nucleotidos[xx] == nuc[3]:
                arn.append(arnP[3])
    #Devuelve un arreglo con la configuración del ARN
    return arn

#Variable que va a regular el crecimiento del ARN de 3 en 3 o de 5 en 5
crecimiento = 3
#Inicios de espacios para la graficación
inicio = 10
inicio2 = 10

inicioB = 10
inicio2B =10
inicioBien = 10

inicio3 = 10
inicio23 = 10
inicioBien3 = 10

inicioARN = 10

#Se crean las bases para guardar ahi los resultados del ARN tanto de la formacion del arreglo final 3 cómo el del arreglo final 5
arreglofinal3 = []
arreglofinal5 = []

window = turtle.Screen()
window.bgcolor('gray')
turtle.title('ADN')
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
turtle.goto(150,-40)
turtle.write("ARN",False,"left",("arial", 20, "bold italic"))
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
for x in range(2):
#Creo el 5' 
    n1 = posiAT[randrange(10)]
    n2 = posiCG[randrange(10)]
    n3 = posiCG[randrange(10)]
    n4 = posiCG[randrange(10)]
    cinco = [n1,n2,n3,n4]
#Creo el 3'
    n5 = posiAT[randrange(10)]
    n6 = posiCG[randrange(10)]
    n7 = posiAT[randrange(10)]
    n8 = posiCG[randrange(10)]
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
    
    for w in range(4):
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

    for m in range(4):
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
    
    for n in range(4):
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

    #Hacemos revision en el primer nucleotido
    if n5==t:
        n11=a
        arreglofinal3.append(n11)
    if n5==g:
        n11=c
        arreglofinal3.append(n11)
    if n5==a:
        n11=t
        arreglofinal3.append(n11)
    if n5==c:
        n11=g
        arreglofinal3.append(n11)
    #Hacemos revision en el segundo nucleotido
    if n6==t:
        n22=a
        arreglofinal3.append(n22)
    if n6==g:
        n22=c
        arreglofinal3.append(n22)
    if n6==a:
        n22=t
        arreglofinal3.append(n22)
    if n6==c:
        n22=g
        arreglofinal3.append(n22)
    #Hacemos revision en el tercer nucleotido
    if n7==t:
        n33=a
        arreglofinal3.append(n33)
    if n7==g:
        n33=c
        arreglofinal3.append(n33)
    if n7==a:
        n33=t
        arreglofinal3.append(n33)
    if n7==c:
        n33=g
        arreglofinal3.append(n33)
    #Hacemos la revision en el cuarto nucleotido
    if n8==t:
        n44=a
        arreglofinal3.append(n44)
    if n8==g:
        n44=c
        arreglofinal3.append(n44)
    if n8==a:
        n44=t
        arreglofinal3.append(n44)
    if n8==c:
        n44=g
        arreglofinal3.append(n44)
    cinquin=[n11,n22,n33,n44]

    for ñ in range(4):
        seleccionado = cinquin[ñ]
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
    
    for r in range(4):
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
    
    for h in range(4):
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
    #Hacemos revision en el primer nucleotido
    if n1==t:
        n5=a
        arreglofinal5.append(n5)
    if n1==g:
        n5=c
        arreglofinal5.append(n5)
    if n1==a:
        n5=t
        arreglofinal5.append(n5)
    if n1==c:
        n5=g
        arreglofinal5.append(n5)
    #Hacemos revision en el segundo nucleotido
    if n2==t:
        n6=a
        arreglofinal5.append(n6)
    if n2==g:
        n6=c
        arreglofinal5.append(n6)
    if n2==a:
        n6=t
        arreglofinal5.append(n6)
    if n2==c:
        n6=g
        arreglofinal5.append(n6)
    #Hacemos revision en el tercer nucleotido
    if n3==t:
        n7=a
        arreglofinal5.append(n7)
    if n3==g:
        n7=c
        arreglofinal5.append(n7)
    if n3==a:
        n7=t
        arreglofinal5.append(n7)
    if n3==c:
        n7=g
        arreglofinal5.append(n7)
    #Hacemos la revision en el cuarto nucleotido
    if n4==t:
        n8=a
        arreglofinal5.append(n8)
    if n4==g:
        n8=c
        arreglofinal5.append(n8)
    if n4==a:
        n8=t
        arreglofinal5.append(n8)
    if n4==c:
        n8=g
        arreglofinal5.append(n8)
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
    
    print(arreglofinal3)

#Se crea la cadena ARN con el arreglo 3'
#TODO poner dependiendo de cual se escog[io]
for y in range(len(arreglofinal3)):
    print(y)
    arregloUsar = constrARN3(arreglofinal3)
    print(arregloUsar)
    seleccionado = arregloUsar[y]
    colorUsar = colorin(seleccionado)
    print(seleccionado)
    fosf = turtle.Turtle()
    fosf.hideturtle()
    fosf.color('black')
    fosf.pensize(8)
    fosf.penup()
    fosf.forward(160)
    fosf.pendown()
    fosf.left(90)
    fosf.forward(inicioARN+2) 

    nucleo = turtle.Turtle()
    nucleo.hideturtle()
    nucleo.speed(10)
    nucleo.pensize(4)
    nucleo.left(90)
    nucleo.pu()
    nucleo.forward(inicioARN)
    nucleo.right(90)
    nucleo.forward(190)
    nucleo.pendown()
    nucleo.pencolor(usarColor)
    nucleo.forward(30)
    inicioARN+=10
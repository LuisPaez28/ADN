import turtle
import numpy as np
from random import randrange
#Creo la base quimica de los nucleotidos
Fostato = ['P','O','O','O']
Ribosa = ['CHHOH','COH','CHOH','CHOH','CHOH']
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
#Creo una base de nucleotidos correctos, para que tenga una base para revisar
nucleotidoAT =[a,t]
nucleotidoTA = [t,a]
nucleotidoCG = [c,g]
nucleotidoGC = [g,c]
#Hago que se creen solos para crear el ADN

#Base de ADN
#5' = fosfato + [ribosa - nucleotido] + fosfato + [ribosa - nucleotido]
#3' = fosfato + [ribosa - nucleotido] + fosfato + [ribosa - nucleotido]
#Comparas los nucleotidos 



#Dibujado
turtle.title("ADN")
turtle.setup((1530)/2, 1000, 0, 0)
turtle.screensize(20,8000)

#luis = turtle.Turtle()
#luis.shape('turtle')
#luis.color('green')
#luis.left(180)
#luis.left(180)
#luis.speed(1)
#luis.forward(100)

#enrique = turtle.Turtle()
#enrique.shape('turtle')
#enrique.color('red')
#enrique.speed(1)
#enrique.right(180)
#enrique.right(180)
#enrique.left(180)
#enrique.forward(100)

inicio = 10
asi='red'
tim='green'
gua='blue'
cito='yellow'
posibilidades=[asi,tim,gua,cito]

turtle.hideturtle()
turtle.penup()
turtle.goto(-10,-40)
turtle.write("Prueba",False,"left",("arial", 20, "bold italic"))

for x in range(1000):
    fos1=turtle.Turtle()
    fos1.hideturtle()
    fos1.color('black')
    fos1.pensize(8)
    fos1.left(90)
    fos1.forward(inicio+2)

    fos2=turtle.Turtle()
    fos2.hideturtle()
    fos2.color('black')
    fos2.pensize(8)
    fos2.penup()
    fos2.forward(60)
    fos2.left(90)
    fos2.pendown()
    fos2.forward(inicio+2)

    elegido = posibilidades[randrange(4)]

#nucleotido para dibujar todo desde aquí.
    nucleotido = turtle.Turtle()
    nucleotido.hideturtle()
    nucleotido.speed(10)
#Ponerle color
    nucleotido.color(elegido)
#Ponerle un tama;o de 4
    nucleotido.pensize(4)
#Mostrar la flecha
#    nucleotido.showturtle()
#Rotar 90 grados a la izquierda
    nucleotido.left(90)
#Dejar de dibujar
    nucleotido.pu()
#mover el trazo en 10
    nucleotido.forward(inicio)
#Volver a dibujar
    nucleotido.down()
#rotamos 90 grados a la derecha
    nucleotido.right(90)
#Mover (y dibujar) en 30
    nucleotido.forward(30)
#Dejar de mostrar la flecha
#    nucleotido.hideturtle()
#Cambiar el color de pintado de la flecha
    elegido2 = posibilidades[randrange(4)]
    nucleotido.pencolor(elegido2)
#Mover el apuntador a un sitio en especifico del canvas, el primer parametro es la posici[on en X y el segundo en la Y]
    nucleotido.goto(60,inicio)
#Inclemento el n[umero] paa que se mueva hacia arriba
    inicio+=10

#Hacer lo mismo que lo de arriba, pero separando los de la izquierda de la derecha y haciendolos de 4 en 4

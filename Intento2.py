import turtle
import numpy as np
from random import randrange

#Creo la base quimica de los nucleotidos
fosfato = ['P','O','O','O']
ribosa = ['CHHOH','COH','CHOH','CHOH','CHOH']

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

#Base de ADN
#5´ = fosfato + [ribosa + nucleotido] + fosfato
    n1 = posibilidades[randrange(4)]
    n2 = posibilidades[randrange(4)]
    n3 = posibilidades[randrange(4)]
    n4 = posibilidades[randrange(4)]
    for x in range(4):
        inicio = 10
    #base del nucleotido 5'
        nucleotin = [fosfato,[ribosa,n1],fosfato,[ribosa,n2],fosfato,[ribosa,n3],fosfato,[ribosa,n4]]
    #Creo la base para la comparaci[on]
        cinco = [n1,n2,n3,n4]
    #Dibujo
        turtle.title("ADN")
    for x in cinco:
        i = 0
        seleccionado = cinco[0]
        colorUsar = colorin(seleccionado)
        fos1=turtle.Turtle()
        fos1.hideturtle()
        fos1.color('black')
        fos1.pensize(8)
        fos1.left(90)
        fos1.forward(inicio+2)
#nucleotido para dibujar todo desde aquí.
        nucleotido = turtle.Turtle()
        nucleotido.hideturtle()
        nucleotido.speed(10)
#Ponerle color
        nucleotido.color(colorUsar)
#Ponerle un tama;o de 4
        nucleotido.pensize(4)
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
        #Incremento el n[umero]
        i+=1
        #Incremento la variable para que suba el sibujo
        inicio+=10

#TODO falta acabar de hacer la estructura, luego que la revise, despues que la corrija, todo con graficos

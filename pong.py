##INDICACION PARA LUIS
## NO ENTIENDO PORQUE EN ALGUNOS ORDENADORES LA PELOTA VA BIEN DE VELOCIDAD
## Y EN OTROS VA MUY LENTO

import turtle
import random
a = random.randint(0,1)
b = random.randint(0,1)
marca1 = 0
marca2 = 0
print(a,b)
ven = turtle.Screen()
ven.bgcolor("black")
ven.title("Pong")
ven.setup(width = 800, height = 600)
ven.tracer(0)


#JUGADOR1

jugador1 = turtle.Turtle()
jugador1.speed(0)
jugador1.color("white")
jugador1.shape("square")
jugador1.penup()
jugador1.goto(-350, 0) 
jugador1.shapesize(stretch_wid=5, stretch_len = 1)


##JUGADOR2
jugador2 = turtle.Turtle()
jugador2.speed(0)
jugador2.color("white")
jugador2.shape("square")
jugador2.penup()

jugador2.goto(350, 0) 

jugador2.goto(350, 0)

jugador2.shapesize(stretch_wid=5, stretch_len = 1)

##PELOTA
pelota = turtle.Turtle()
pelota.speed(0)
pelota.color("white")
pelota.shape("circle")
pelota.penup()
pelota.color("red")
pelota.shape("circle")
pelota.penup()
pelota.goto(0, 0)


marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.goto(0,260)
marcador.hideturtle()
marcador.write("Jugador A: {}            Jugador B: {}".format(marca1,marca2), font=("Courier", 17), align = "center")




if a == 0:
    pelota.dx = 0.2
else:
    pelota.dx = -0.2
if b == 0:
    pelota.dy = 0.2
else:
    pelota.dy = -0.2


def jugador1_arriba():
    y = jugador1.ycor()
    y +=  20
    jugador1.sety(y)

def jugador1_abajo():
    y = jugador1.ycor()
    y -=  20
    jugador1.sety(y)

def jugador2_arriba():
    y = jugador2.ycor()
    y +=  20
    jugador2.sety(y)

def jugador2_abajo():
    y = jugador2.ycor()
    y -=  20
    jugador2.sety(y)


##CONECTAR TECLADO
ven.listen()
ven.onkeypress(jugador1_arriba, "w")
ven.onkeypress(jugador1_abajo, "s")
ven.onkeypress(jugador2_arriba, "Up")
ven.onkeypress(jugador2_abajo, "Down")
##BUCLE PRINCIPAL
while True:
    ven.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    if pelota.ycor() > 287:
        pelota.dy *= -1
    if pelota.ycor() < -287:
        pelota.dy *= -1
    if pelota.xcor() > 387:
        pelota.goto(0,0)
        marca1 = marca1 + 1
        marcador.clear()
        marcador.write("Jugador A: {}            Jugador B: {}".format(marca1,marca2), font=("Courier", 17), align = "center")
    if pelota.xcor() < -387:
        pelota.goto(0,0)
        marca2 = marca2 + 1
        marcador.clear()
        marcador.write("Jugador A: {}            Jugador B: {}".format(marca1,marca2), font=("Courier", 17), align = "center")



    if ((pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < jugador2.ycor() + 50 and pelota.ycor() > jugador2.ycor() -50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < jugador1.ycor() + 50 and pelota.ycor() > jugador1.ycor()  -50)):
        pelota.dx *= -1
        

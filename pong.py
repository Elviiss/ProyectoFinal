import turtle

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

def jugador1_arriba():
    y = jugador1.ycor()
    y +=  20
    jugador1.sety(y)

def jugador1_abajo():
    y = jugador1.ycor()
    y -=  20
    jugador1.sety(y)


##CONECTAR TECLADO
ven.listen()
ven.onkeypress(jugador1_arriba, "w")
ven.onkeypress(jugador1_abajo, "s")
##BUCLE PRINCIPAL
while True:
    ven.update()

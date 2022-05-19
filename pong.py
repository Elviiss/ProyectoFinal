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

##BUCLE PRINCIPAL
while True:
    ven.update()

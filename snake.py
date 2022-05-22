import turtle
import time
import random
from playsound import playsound


ven = turtle.Screen()
ven.bgcolor("black")
ven.title("Snake")
ven.setup(width = 800, height = 600)
ven.tracer(0)
##SERPIENTE
snake = turtle.Turtle()
snake.speed(0)
snake.color("white")
snake.shape("square")
snake.penup()
snake.goto(-250, 0)


##MANZANA
manza = turtle.Turtle()
manza.color("red")
manza.shape("square")


##BUCLE PRINCIPAL
while True:
    ven.update()


##SONIDO DE MUERTE
##nombre = "mario.mp3"
##playsound(nombre)

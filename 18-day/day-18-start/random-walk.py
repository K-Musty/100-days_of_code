#!/usr/bin/env python3
import turtle
from turtle import Turtle, Screen, colormode
import random
tim = Turtle()
tim.speed("fastest")
tim.pensize(5)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

turns = [0, 90, 180, 270]

for i in range(10000):
    tim.color(random_color())
    steps = 20
    angle = int(random.choice(turns))
    tim.setheading(angle)
    tim.fd(steps)

screen = Screen()
screen.exitonclick()

#!/usr/bin/env python3
import turtle
from turtle import Turtle, Screen, colormode
import random
tim = Turtle()
tim.speed("fastest")
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + 10)


screen = Screen()
screen.exitonclick()

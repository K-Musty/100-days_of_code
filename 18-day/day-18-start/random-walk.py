#!/usr/bin/env python3
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.speed("fast")
tim.pensize(5)

turns = [0, 90, 180, 270]
for i in range(10000):
    steps = 20
    angle = int(random.choice(turns))
    tim.setheading(angle)
    tim.fd(steps)

screen = Screen()
screen.exitonclick()

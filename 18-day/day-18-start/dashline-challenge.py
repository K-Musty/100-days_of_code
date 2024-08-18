#!/usr/bin/env python3
from turtle import Turtle, Screen

tim = Turtle()
for i in range(20):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()

#!/usr/bin/env python3
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)

screen.exitonclick()
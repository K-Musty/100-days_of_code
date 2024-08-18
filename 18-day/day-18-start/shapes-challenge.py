#!/usr/bin/env python3
import turtle
from turtle import Turtle, Screen, colormode
import random
tim = Turtle()
colormode(255)

colors = ["red", "blue", "orange", "yellow", "green", "pink", "teal"]


def draw_shape(sides_num):
    angle = 360 / sides_num
    for i in range(sides_num):
        tim.forward(100)
        tim.right(angle)


for sides_num in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(sides_num)


screen = Screen()
screen.exitonclick()

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# for _ in range(3):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(120)
# for _ in range(4):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(90)
# for _ in range(5):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(72)
# for _ in range(6):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(60)
# for _ in range(7):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(51.42)
# for _ in range(8):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(45)
# for _ in range(9):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(40)
# for _ in range(10):
#     tim.pencolor(random_color())
#     tim.forward(150)
#     tim.right(36)
#

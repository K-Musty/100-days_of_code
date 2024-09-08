#!/usr/bin/python3
from turtle import Turtle, Screen, colormode
import random

# Initialize the screen
screen = Screen()
screen.bgcolor("black")
colormode(255)

# Initialize the Turtle
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("normal")

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Draw a beautiful spiral pattern
for i in range(360):
    timmy.color(random_color())
    timmy.forward(i * 3 / 4)
    timmy.left(59)

# Keep the window open until clicked
screen.exitonclick()


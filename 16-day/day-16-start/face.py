#!/usr/bin/python3
from turtle import Turtle, Screen

# Initialize the Turtle
timmy = Turtle()
timmy.speed("normal")

# Function to draw a circle
def draw_circle(turtle, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(radius)

# Draw the face
timmy.color("yellow")
timmy.begin_fill()
draw_circle(timmy, 100, 0, -100)
timmy.end_fill()

# Draw the left eye
timmy.color("white")
timmy.begin_fill()
draw_circle(timmy, 20, -40, 20)
timmy.end_fill()

# Draw the right eye
timmy.begin_fill()
draw_circle(timmy, 20, 40, 20)
timmy.end_fill()

# Draw the pupils
timmy.color("black")
timmy.begin_fill()
draw_circle(timmy, 10, -40, 35)
timmy.end_fill()

timmy.begin_fill()
draw_circle(timmy, 10, 40, 35)
timmy.end_fill()

# Draw the nose
timmy.color("black")
timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
timmy.circle(10)

# Draw the mouth
timmy.penup()
timmy.goto(-40, -20)
timmy.setheading(-60)
timmy.pendown()
timmy.circle(40, 120)

# Keep the window open until clicked
screen = Screen()
screen.exitonclick()


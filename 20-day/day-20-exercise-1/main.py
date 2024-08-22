#!/usr/bin/python3
from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake_positions = [(-40, 0), (-20, 0), (0,0)]
segments = []
for place in snake_positions:
    s1 = Turtle()
    s1.color("white")
    s1.shape("square")
    s1.penup()
    s1.goto(place)
    segments.append(s1)
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments)-1, 0, -1):
        new_x = segments[seg -1].xcor()
        new_y = segments[seg -1].ycor()
        segments[seg].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].right(90)
screen.exitonclick()

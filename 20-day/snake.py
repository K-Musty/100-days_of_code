import time
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")


positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for place in positions:
    body = Turtle("square")
    body.color("white")
    body.penup()
    body.goto(place)
    segments.append(body)


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

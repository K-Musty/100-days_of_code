from turtle import Turtle, Screen
from ball import Ball

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

pong = Turtle()
pong.goto(-380, 0)
pong.shape("square")
pong.shapesize(stretch_wid=5, stretch_len=1)
pong.color("white")
pong.penup()
screen.update()

ping = Turtle()
ping.goto(380, 0)
ping.shape("square")
ping.shapesize(stretch_len=1, stretch_wid=5)
ping.color("white")
ping.penup()
screen.update()

center = Turtle()
center.goto(0,-320)
center.hideturtle()
center.color("white")
# center.goto(0, 370)
center.left(90)
for i in range(21):
    center.forward(15)
    center.penup()
    center.forward(15)
    center.pendown()
screen.update()

ball = Ball()
screen.update()

screen.exitonclick()

#!/usr/bin/env python3
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
center = Turtle()
center.goto(0, -320)
center.hideturtle()
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

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detection with wall
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.bounce_y()

    # Detection with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
    # left point
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # right point
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

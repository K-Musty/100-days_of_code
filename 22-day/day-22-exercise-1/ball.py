from turtle import Turtle


class Ball:

    def __init__(self):
        pass

    def ball(self):
        ball = Turtle("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)

#!/usr/bin/env python3
import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 500)
user_choice = screen.textinput("Make you bet", 'Which turtle would win the race: "red", "blue", "yellow", "orange", "pink", or "green"')

colors = ["red", "blue", "yellow", "orange", "pink", "green"]
y_pos = [80, 40, 0, -40, -80, -120]
turtle_list = []
for t in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[t])
    tim.penup()
    tim.goto(x=-230, y=y_pos[t])
    turtle_list.append(tim)

if user_choice:
    is_race_on = True

while is_race_on:


    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won!!, the {winning_color} turtle won")
            else:
                print(f"You've lost, the {winning_color} turtle won ")
        speed = random.randint(0, 10)
        turtle.forward(speed)



screen.exitonclick()

#!/usr/bin/env python3
import turtle
from turtle import Turtle, Screen, TK
import random

is_race_on = False
screen = Screen()
screen.setup(500, 500)
user_choice = screen.textinput("Make you bet", 'Which turtle would win the race: pick a color')

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
                TK.messagebox.showinfo(title="You won", message="Hooray, you won")
            else:
                print(f"You've lost, the {winning_color} turtle won ")
                TK.messagebox.showinfo(title="You lost", message="Better luck next time")
        speed = random.randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()

# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
#
# cool_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     cool_colors.append(rgb)
#
# print(cool_colors)
import random
from turtle import Turtle, Screen, colormode
tim = Turtle()
colormode(255)
tim.hideturtle()
tim.penup()
tim.speed("fastest")


color_list = [(162, 168, 34), (242, 78, 54), (148, 50, 101), (239, 67, 131), (8, 144, 64), (230, 115, 164), (242, 219, 73), (4, 141, 182), (69, 198, 223), (161, 58, 50), (22, 171, 133), (120, 37, 85), (251, 231, 0), (25, 190, 210), (113, 195, 165)]
def move():
    for _ in range(10):
        tim.dot(20, random.choice(color_list));
        tim.fd(50)
tim.setheading(220)
tim.fd(250)
tim.setheading(0)
for i in range(5):
    move()
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(180)
    tim.fd(50)
    move()
    tim.setheading(90)
    tim.fd(50)
    tim.setheading(360)
    tim.fd(50)







screen = Screen()
screen.exitonclick()
from turtle import Turtle
from random import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        all_cars = []
        for i in range(6):
            self.create_cars()
            all_cars.append(i)

    def create_cars(self):
        self.new_car = Turtle()
        self.new_car.shape("square")
        self.new_car.penup()
        self.new_car.color(COLORS[0])
        self.new_car.shapesize(stretch_len=2, stretch_wid=1)

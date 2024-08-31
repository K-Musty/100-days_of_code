from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        for i in range(6):
            self.create_cars()
            self.all_cars.append(i)


    def create_cars(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        for i in range(random.randint(20, 20)):
            new_car.backward(20)
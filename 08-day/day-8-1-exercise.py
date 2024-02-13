#!/usr/bin/python3
import math
''' Wall Paint Calculator '''
print("Wall Paint Calculator")
def paint_calc(height, width, cover):
    area = height * width
    number_of_can = math.ceil(area/cover)
    print(f"You need {number_of_can} to paint the wall")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


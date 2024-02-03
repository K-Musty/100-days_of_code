#!/usr/bin/python3
student_heights = input("input a list of student height ").split()
for n in range(0, len(student_heights)):
   student_heights[n] = int(student_heights[n])
print(student_heights)

height_sum = 0
for height in student_heights:
    height_sum += height
#sum of height

student_number = 0
for number in student_heights:
    student_number += 1
#number of items

average_height = round(height_sum / student_number)
print(average_height)

#!/usr/bin/python3

row1 = ["#","#","#"]
row2 = ["#","#","#"]
row3 = ["#","#","#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

axis_y = int(position[0])
axis_x = int(position[1])

selected_row = map[axis_x - 1]
selected_row[axis_y - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

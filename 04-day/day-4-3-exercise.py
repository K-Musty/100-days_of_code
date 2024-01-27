#!/usr/bin/python3

row1 = ["#","#","#"]
row2 = ["#","#","#"]
row3 = ["#","#","#"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

y-axis = int(position[0])
x-axis = int(position[1])

selected_row = map[x-axis - 1]
selected_row[y-axis - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

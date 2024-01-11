#!/usr/bin/python3
print("Body Mass Calculator!")
height = input("Enter your height in m: ")
weight = input("Entter your weight in kg: ")

body_mass_index = int(weight) / float(height) ** 2
bmi = (int(body_mass_index))
print(bmi)

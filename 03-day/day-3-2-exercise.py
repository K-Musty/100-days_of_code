#!/usr/bin/python3
#Body Mass Calculator 2.0

print("Body Mass Calculator!")
height = float(input("Enter your height in m: "))
weight = float(input("Entter your weight in kg: "))

body_mass_index = float(weight) / float(height) ** 2
bmi = (float(body_mass_index))
if bmi <= 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi <= 25:
    print("You have a normal weight")
elif bmi > 25 and bmi <= 30:
    print("You are overweight")
elif bmi > 30 and bmi <= 35:
    print("You are Obese")
else:
    print("You are clinically Obese")

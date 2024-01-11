#!/usr/bin/python3
print("Day, Week and Month Calculator! ")

age = int(input("What is your current age? "))

years_left = 90 - age
day = years_left * 365
week = years_left * 52
month = years_left * 12
print(f"You have {day}, {week} weeks and {month} months left")

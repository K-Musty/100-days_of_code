#!/usr/bin/python3
print("Day, Week and Month Calculator!")

age = input("What is your current age?")
day = age * 365
week = (age * 365)/ 52
month = (age * 365)/ 12
print(f"You have {day}, {week} weeks and {month} months left")

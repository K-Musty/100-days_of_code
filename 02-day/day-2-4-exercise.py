#!/usr/bin/python3
print("Day, Week and Month Calculator!")

age = int(input("What is your current age?"))
day = age * 365
week = int(age * 365)/ 52
month = int(age * 365)/ 12
print(f"You have {day}, {week} weeks and {month} months left")

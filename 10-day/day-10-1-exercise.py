#!/usr/bin/python3
#Leap year calculator

print("Leap year checker!")
year = int(input("Which year do you want to check? "))


if year % 4 == 0:
    if year % 100 != 0:
        return True
    elif year % 400 == 0:
        return False
    else:
        return True
else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(input("Enter a year: "))
month = int(input("Enter a month"))
days = days_in_month(year, month)
print(days)

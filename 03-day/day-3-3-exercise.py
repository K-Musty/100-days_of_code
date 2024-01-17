#!/usr/bin/python3
#Leap year calculator

print("Leap year checker!")
year = int(input("Which year do you want to check? "))

if (year / 4) == 0:
    {
    if year / 100 != 0:
        print("This is a Leap year")
    elif year / 400 == 0:
        print("This is a Leap year")
    else:
        print("This is not a Leap year")
        }
else:
    print("This is not a Leap year")

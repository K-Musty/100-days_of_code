#!/usr/bin/python3
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0


if size == 'S' or size == 's':
    price += 15
elif size == 'M' or size == 'm':
    price += 20
elif size == 'L' or size == 'l':
    price += 25
else:
    print("input Error: 98!")

if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        price += 2
    elif size == 'm' or size == 'M':
        price += 3
    elif size == 'L' or size == 'l':
        price += 3
    else:
        price += 0

if extra_cheese == 'Y' or extra_cheese == "y":
    price += 1
else:
    price += 0

print(f"You total bill is ${price}")

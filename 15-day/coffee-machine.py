#!/usr/bin/env python3
# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

start_machine = False
while not start_machine:
    userInput = input("What would you like (espresso, latte or cappuccino): ")

    if userInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif userInput == "off":
        print("Thanks you !!!")
        start_machine = False

    else:
        drink = MENU[userInput]
        if enough_resources(drink["ingredients"]):
            print ("yessss")


def enough_resources(resources_needed):
    for stuff in resources_needed:
        if resources_needed[stuff] >= resources[stuff]:
            print(f"Sorry there is not enough {stuff}")
            return False
    return True

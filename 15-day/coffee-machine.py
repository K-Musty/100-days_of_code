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


    #TODO report option
    if userInput == "report":
        print(resources)
    # TODO off option
    if userInput == "off":
        print("Thanks you !!!")
        start_machine = True
# TODO Function to get water, coffee and milk
def waterin(MENU, drink):
    water_in = MENU[drink]["ingredients"]["water"]
    return water_in

def coffeein(MENU, drink):
    coffee_in = MENU[drink]["ingredients"]["coffee"]
    return coffee_in

def milkin(MENU, drink):
    if drink != espresso:
        milk_in = MENU[drink]["ingredient"]["coffee"]
        return milk_in

# TODO Function to get cost
def espressocost(MENU, drink):
    espresso_cost = MENU[drink]["cost"]
    return espresso_cost

def lattecost(MENU, drink):
    latte_cost = MENU[drink]["cost"]
    return latte_cost

def cappucinocost(MENU, drink):
    cappuccino_cost = MENU[drink]["cost"]
    return cappuccino_cost



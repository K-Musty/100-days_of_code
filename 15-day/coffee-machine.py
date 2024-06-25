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

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def enough_resources(resources_needed):
    for stuff in resources_needed:
        if resources_needed[stuff] >= resources[stuff]:
            print(f"Sorry there is not enough {stuff}")
            return False
        return True


def coins(total):
    quaters = int(input("Insert Quaters: ")) * 0.25
    dimes = int(input("Insert dimes: ")) * 0.10
    nickles = int(input("Insert nickles: ")) * 0.05
    pennies = int(input("Insert pennies: ")) * 0.01
    total = quaters + dimes + nickles + pennies
    print(total)


start_machine = True
while start_machine:
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
        def enough_money(money_needed, money_need):
            if money_need >= money_needed:
                return False
            return True



        if enough_resources(drink["ingredients"]):
            
            #enough_money(to_int, cash)

            print("good")

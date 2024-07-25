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

insert = 0
def coins(total):
    quaters = int(input("Insert Quaters: ")) * 0.25
    dimes = int(input("Insert dimes: ")) * 0.10
    nickles = int(input("Insert nickles: ")) * 0.05
    pennies = int(input("Insert pennies: ")) * 0.01
    total = quaters + dimes + nickles + pennies
    print(total)
    return total

def deduct_resources(drink_type):
    for items in drink_type:
        resources[items] = resources[items] - drink_type[items]
    return resources

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
        def enough_money(MENU, userInput, money_needed):
            if money_needed >= MENU[userInput]["cost"]:
                return True
            print("Sorry that's not enough money. Money refunded")
            return False


        if enough_resources(drink["ingredients"]):
            cash = coins(insert)
            def process_change(cash):
                total_cost = MENU[userInput]["cost"]
                change = cash - total_cost
                print(f"Your change is {change:.2f}, thank you")
                return change

            if enough_money(MENU, userInput, cash):
                money += cash
                changed = process_change(cash)
                deduct_resources(MENU[userInput]["ingredients"])
                money -= changed
                print(f"Here is your {userInput}, ENJOY!")

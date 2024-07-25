#!/usr/bin/python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ingredients = MenuItem
menu = Menu()
process_money = MoneyMachine()
process_coffee = CoffeeMaker()
machine_start = True
print("Welcome to Coffee Machine")

while machine_start:
    userInput = input("What would you like? (espresso/latte/cappuccino)? ")
    if userInput == "off":
        machine_start = False
    elif userInput == "report":
        process_coffee.report()
        process_money.report()
    else:
        drink = menu.find_drink(userInput)
        if process_coffee.is_resource_sufficient(drink):
            if process_money.make_payment(drink.cost):
                process_coffee.make_coffee(drink)

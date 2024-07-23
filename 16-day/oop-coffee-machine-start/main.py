#!/usr/bin/python3
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine#!/usr/bin/pyhton3

ingredients = MenuItem
menu = Menu()
process_money = MoneyMachine()
process_coffee = CoffeeMacker()
machine_start = True
print(Welcome to Coffee Machine)

while machine_start:
    userInput = input("What would you like? (espresso/latte/cappuccino)? ")
    if userInput == "off":
        machine_start = False

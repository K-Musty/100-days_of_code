#!/usr/bin/python3
#Calculator project challenge one
from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide
}
def calculator():
    num1 = int(input("What's the first number?: "))
    for keys in operators:
        print(keys)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation ")

        num2 = int(input("What's the next number?: "))
        calculations = operators[operation_symbol]
        answer = calculations(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        ask_continue = input("Type 'y' to contine and 'n' to stop and 'r' to restart ")
        lower_cont = ask_continue.lower()
        if lower_cont == "y":
            num1 = answer
        elif lower_cont == "r":
            calculator()
        else:
            should_continue = False

calculator()

'''
if operation_symbol == "+":
    add(num1, num2)
elif operational_symbol == "-":
    substract(num1, num2)
elif operational_symbol == "*":
    multiply(num1, num2)
elif operational_symbol == "/":
    divide(num1, num2)
else:
    print("Error: invalid operator!!!")
'''

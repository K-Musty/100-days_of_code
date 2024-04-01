#!/usr/bin/python3
#Calculator project challenge one

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

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for keys in operators:
    print(keys)

operation_symbol = input("Pick an operation from the line above ")



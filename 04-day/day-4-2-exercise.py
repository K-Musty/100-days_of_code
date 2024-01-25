#!/usr/bin/python3
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, separated by comma. ")

names = namesAsCSV.split(", ")

#you can use random.choice
maximumnumber = len(names)

randomPerson = random.randint(0, maximumnumber - 1)

person_to_pay = names[randomPerson]
print(person_to_pay + " Go buy")




#!/usr/bin/python3
print("Welcome to Love Calculator!")

input_name1 = input("What is your name? \n")
input_name2 = input("What is thier name? \n")

name1 = input_name1.lower()
name2 = input_name2.lower()

name1_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
name2_love = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

print(str(name1_true) + str(name2_love) + "%")



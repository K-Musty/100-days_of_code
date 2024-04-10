#!/usr/bin/python3
# Guess the Number Game

from art import logo
import random

print(logo)

answer = randint(1, 100)

def campare(guess, answer):
    if guess > answer:
        print("Too High")
    elif guess < answer:
        print("Too Low")
    elif guess == answer:
        print("Guess is Correct!!!")


def level_game():
    level = int(input("Select '1' for easy and '2' for hard"))
    if level == 1:
        easy_mode()
    elif level == 2:
        hard_mode()
    else:
        print("Wrong choice: Try again !!")


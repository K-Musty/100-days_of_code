#!/usr/bin/python3
# Guess the Number Game

from art import logo
import random

print(logo)

numbers = []

def get_number():
    guessed_num = random.choice(numbers)
    return guessed_num
game_over = False
def easy_mode():
    lives = 10
    while not game_over:
        user_num = int(input("Select a number between 1 & 100"))

        for n in lives:
            n -= lives
            return lives
def hard_mode():
    lives = 4:
        while not game_over:
            for n in lives:
                n -= lives
                return lives

def level_game():
    level = int(input("Select '1' for easy and '2' for hard"))
    if level == 1:
        easy_mode()
    elif level == 2:
        hard_mode()
    else:
        print("Wrong choice: Try again !!")


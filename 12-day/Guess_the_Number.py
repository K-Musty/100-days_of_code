#!/usr/bin/python3
# Guess the Number Game

from art import logo
from random import randint

print(logo)

answer = randint(1, 100)

def easy_mode():
    game_over = False
    tries = 10
    while not game_over:
        for n in tries:
            n -= tries
        game_over = True
def hard_mode():
    game_over = False
    tries = 4
    while not game_over:
        for n in tries:
            n -= tries
        game_over = True
        
def level_game():
    level = int(input("Select '1' for easy and '2' for hard "))
    if level == 1:
        easy_mode()
        compare(guess, answer)
    elif level == 2:
        hard_mode()
        compare(guess, answer)

    else:
        print("Wrong choice: Try again !!")

def begin_game():
    game_over = False
    while not game_over:
        guess = int(input("choose a number from 1 to 100: "))
        def compare(guess, answer):
            if guess > answer:
                print("Too High")
            elif guess < answer:
                print("Too Low")
            elif guess == answer:
                print("Guess is Correct!!!")
                game_over = True
            else:
                print("invalid input!!!")
                game_over = True
        compare(guess, answer)
        if guess == answer:
            game_over = True
begin_game()

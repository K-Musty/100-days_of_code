#!/usr/bin/python3
# Guess the Number Game

from art import logo
from random import randint

print(logo)

answer = randint(1, 100)

def begin_game():
    max_tries = 5
    tries = 0
    game_over = False
    while tries < max_tries:
        guess = int(input("choose a number from 1 to 100: "))
        def compare(guess, answer):
            nonlocal tries
            if guess > answer:
                print("Too High")
            elif guess < answer:
                print("Too Low")
            elif guess == answer:
                print("Guess is Correct!!!")
                return True
            else:
                print("invalid input!!")
            tries += 1
            return false
        compare(guess, answer)
        if guess == answer:
            return True

begin_game()

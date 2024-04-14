#!/usr/bin/python3
# Guess the Number Game

from art import logo
from random import randint

print(logo)

answer = randint(1, 100)

def hard_game():
    end_tries = 0
    tries = 5
    while tries > end_tries:
        print(f"You have {tries} tries left")
        guess = int(input("choose a number from 1 to 100: "))
        def compare(guess, answer):
            if guess > answer:
                print("Too High")
            elif guess < answer:
                print("Too Low")
            elif guess == answer:
                print("Guess is Correct!!!")
                return True
            else:
                print("invalid input!!")
        tries -= 1
        return False 
        compare(guess, answer)
        if guess == answer:
            print("You loose, try again")
            return True

def easy_game():
    end_tries = 0
    tries = 10
    while tries > end_tries:
        print(f"You have {tries} tries left")
        guess = int(input("choose a number from 1 to 100: "))
        def compare(guess, answer):
            if guess > answer:
                print("Too High")
            elif guess < answer:
                print("Too Low")
            elif guess == answer:
                print("Guess is Correct!!!")
                return True
            else:
                print("invalid input!!")
        tries -= 1
        return False
        compare(guess, answer)
        if guess == answer:
            print("You loose")
            return True

def begin_game():
    level = int(input("Choose '1' for easy and '2' for hard: "))
    if level == 1:
        print("yes")
        easy_game()
    elif level == 2:
        hard_game()

begin_game()

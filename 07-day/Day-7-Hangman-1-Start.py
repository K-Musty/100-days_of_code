#!/usr/bin/python3
import random
''' Hangman Game First Challenge '''
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
input_guess = input("Guess a letter: ")
guess = input_guess.lower()

for char in chosen_word:
    if char == guess:
        print("Correct")
    else:
        print("Wrong")

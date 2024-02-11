#!/usr/bin/python3
import random

''' Hangman Game Third Challenge '''

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#Testing code
print(f'psst, the soluton is {chosen_word}.')
word_len = len(chosen_word)
display = []
for char in range(word_len):
    display += '_'
print(display)

the_end = False
while not the_end:
    input_guess = input("Guess a letter: ")
    guess = input_guess.lower()

    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if "_" not in display:
        the_end = True
        print("You win")

#!/usr/bin/python3
import random

''' Hangman Game Second Challenge '''

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#Testing code
print(f'psst, the soluton is {chosen_word}.')
word_len = len(chosen_word)
display = []
for char in range(word_len):
    display += '_'
print(display)

input_guess = input("Guess a letter: ")
guess = input_guess.lower()

for position in range(word_len):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)

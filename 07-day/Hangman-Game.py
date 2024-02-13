#!/usr/bin/python3
'''
100 days of code
Day 8
Challenge: Hang-Man
'''
print(logo)
import random
from stages import stages
from Hangmanwords_logo import logo, word_list

chosen_word = random.choice(word_list)
#Testing code
print(f'psst, the soluton is {chosen_word}.')
word_len = len(chosen_word)
lives = 6

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

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            the_end = True
            print("Game Over!!!, Try Again")

    print(display)
    if "_" not in display:
        the_end = True
        print("You win")

    print(stages[lives])


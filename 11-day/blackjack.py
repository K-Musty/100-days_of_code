#!/usr/bin/python3
#BackJack Game
import random
def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10, 10]
    card_taken = random.choice(cards)
    return card_taken
user_card = []
computer_card = []
def begin_game():
    for n in range(0,2):
        user_card.append(get_card())
        computer_card.append(get_card())
    print(user_card)
    print(computer_card)

begin_game()

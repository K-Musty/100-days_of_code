#!/usr/bin/python3
#BackJack Game
import random
def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10, 10]
    card_taken = random.choice(cards)
    return card_taken
user_card = []
computer_card = []
game_over = false


def begin_game():
    for n in range(0,2):
        user_card.append(get_card())
        computer_card.append(get_card())

    def calculate_sum(cards):
        total_sum = sum(cards)
        return total_sum
    
    whlie not game_over:
        user_sum = calculate_sum(user_card)
        computer_sum = calculate_sum(computer_card)

        def calculate_score(cards):
            total_sum = sum(cards)
            return total_sum
            if sum(cards) == 21 and len(cards) == 2:
                return 0
            if 11 in cards and sum(cards) > 21:
                cards.remove(11)
                cards.append(1)

        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Youre cards are {user_card} and Score is {user_score} ")
        print(f"Computer cards are {computer_card} and Score is {computer_score} ")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else:
            pick_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if pick_another_card == "y":
                user_card.append(get_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_card.append(get_card())
        computer_score = calculate_score(computer card)


    

begin_game()

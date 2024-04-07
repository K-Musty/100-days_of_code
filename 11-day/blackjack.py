#!/usr/bin/python3
#Back-Jack Game
from art import logo
import random
def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10, 10]
    card_taken = random.choice(cards)
    return card_taken

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "This game is a Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "You Won the blackjack"
    elif user_score > 21:
        return "You went over you lose"
    elif computer_score > 21:
        return "Computer went over, you Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
def begin_game():
    print(logo)
    user_card = []
    computer_card = []
    game_over = False

    for n in range(0,2):
        user_card.append(get_card())
        computer_card.append(get_card())
    
    while not game_over:

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
        print(f"Computer cards are {computer_card[0]}")

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
            computer_score = calculate_score(computer_card)

    print(compare(user_score, computer_score))

    while input("Play Again: 'y', end 'n'") == "y":
        begin_game()

begin_game()

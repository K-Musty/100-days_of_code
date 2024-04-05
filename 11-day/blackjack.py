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
    print(computer_card[0])

    user_sum = sum(user_card)
    print(user_sum)

    computer_sum = sum(computer_card)
    print(computer_sum)

    
    if computer_sum == 21 and user_sum != 21:
        print("computer wins")
    elif computer_sum != 21 and user_sum == 21:
        print("You win Hooray")
    elif computer_sum == 21 and user_sum == 21:
        print("This game is a Draw, please try again")
    elif computer_sum > 21 and user_sum > 21:
        print("This game is a Draw, please try again")
    elif computer_sum > 21 and user_sum < 21:
        print("You win Hooray")
    elif computer_sum < 21 and user_sum > 21:
        print("You lose, computer wins")
    

begin_game()

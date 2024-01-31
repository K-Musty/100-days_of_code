#!/usr/bin/python3

import random
print("Rock, Paper and Scissors Game!!!")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rps_choice = [rock, paper, scissors]

player_input = input("Choose 0 for rock, 1 for paper and 2 for scissors ")

player_choice = int(player_input)

computer_choice = random.randint(0,2)

if player_choice == 0 and computer_choice == 0:
    print("This is a draw, Play Again!!")
elif player_choice == 0 and computer_choice == 1:
    print("Computer wins, please try again!!")
elif player_choice == 0 and computer_choice == 2:
    print("You Win, Hooray!!")
elif player_choice == 1 and computer_choice == 0:
    print("You Win, Hooray!!")
elif player_choice == 1 and computer_choice == 1:
    print("This is a draw, Play Again!!")
elif player_choice == 1 and computer_choice == 2:
    print("Computer wins, please try Again")
elif player_choice == 2 and computer_choice == 0:
    ("Computer wins, Please play Again!!")
elif player_choice == 2 and computer_choice == 1:
    ("You Win, Hoooray!!")
elif player_choice == 2 and computer_choice == 2:
    print("This is a draw, Please try again")

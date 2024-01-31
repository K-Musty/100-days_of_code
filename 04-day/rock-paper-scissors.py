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


player_input = input("Choose 0 for rock, 1 for paper and 2 for scissors ")
display_choice = int(player_input)
if display_choice == 0:
    print(rock)
elif display_choice == 1:
    print(paper)
elif display_choice == 2:
    print(scissors)
player_choice = int(player_input)

computer_choice = random.randint(0,2)
computer_display = computer_choice
if computer_display == 0:
    print(rock)
elif computer_display == 1:
    print(paper)
elif computer_display == 2:
    print(scissors)

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
    print("Computer wins, Please play Again!!")
elif player_choice == 2 and computer_choice == 1:
    print("You Win, Hoooray!!")
elif player_choice == 2 and computer_choice == 2:
    print("This is a draw, Please try again")

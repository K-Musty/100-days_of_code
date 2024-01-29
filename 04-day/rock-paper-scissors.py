#!/usr/bin/python3
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

if player_choice == 0:
    print(rock)
    if

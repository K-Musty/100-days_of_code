#!/usr/bin/env python3
# Higher/Lower Game
from art import logo
from art import vs
from game_data import data
import random

print(logo)

def format_data(entity):
    """Formatted output"""
    entity_name  = entity["name"]
    entity_descrpt = entity["description"]
    entity_country = entity["country"]
    return f"{entity_name}, a {entity_descrpt}, from {entity_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they are right"""
    if a_followers > b_followers:
        return guess == "a"
    elif b_followers > a_followers:
        return guess == "b"
    else:
        return false


entity_a = random.choice(data)
entity_b = random.choice(data)

if entity_a == entity_b:
    entity_b = random.choice(data)

compare_a = format_data(entity_a)
compare_b = format_data(entity_b)

print(f"Compare A: {compare_a}")
print(vs)
print(f"Against B: {compare_b}")

guess = input("Who has more followers, A or B: ").lower()

a_follower_account = entity_a["follower_count"]
b_follower_account = entity_b["follower_count"]

is_correct = check_answer(guess, a_follower_account, b_follower_account)

score = 0
if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
else:
    print("Sorry, that's wrong. Final score: {score}.")

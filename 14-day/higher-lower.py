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


entity_a = random.choice(data)
entity_b = random.choice(data)

if entity_a == entity_b:
    entity_b = random.choice(data)

compare_a = format_data(entity_a)
compare_b = format_data(entity_b)

print(f"Compare A: {compare_a}")
print(vs)
print(f"Against B: {compare_b}")


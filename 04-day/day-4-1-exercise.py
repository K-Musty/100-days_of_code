#!/usr/bin/python3
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
coin_face = random.randint(0,1)
if coin_face == 1:
    print("Heads")
else:
    print("Tails")


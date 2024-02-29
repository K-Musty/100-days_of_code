#!/usr/bin/python3
from art import logo

print(logo)
print("Welcome to the blind Auction")

auction_dict = {}
name = input("What is your name?: ")
bid_price = int(input("How much would you want to bid?: $"))

auction_dict[name] = bid_price

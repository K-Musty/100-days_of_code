#!/usr/bin/python3
#from art import logo

#print(logo)
print("Welcome to the blind Auction")

auction_dict = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bid = False
while not continue_bid:
    name = input("What is your name?: ")
    bid_price = int(input("How much would you want to bid?: $"))
    auction_dict[name] = bid_price
    restart = input("Do you want to cotinue, 'yes' or 'no' ")
    if restart == 'no':
        continue_bid = True


find_highest_bidder(auction_dict)

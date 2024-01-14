#!/usr/bin/python3
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int(input("How many people to split the bill? "))

total_bill = tip_percentage / 100 * bill + bill

bill_for_each = total_bill / people_to_split
amount = round(bill_for_each, 2)

print(f"Each person should pay ${amount}")

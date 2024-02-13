#!/usr/bin/python3
'''Prime Nummber Checker '''
def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = false
        if is_prime:
            print("It is a Prime Number")
        else:
            print("It is not a Prime Number")




n = int(input("Enter number you want to check: "))
prime_checker(number=n)

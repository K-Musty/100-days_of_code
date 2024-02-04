#!/usr/bin/python3

total_even = 0
for n in range(1, 101):
    if n % 2 == 0:
        total_even += n
print(total_even)

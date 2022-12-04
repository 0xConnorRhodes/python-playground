#!/usr/bin/env python3

import random

"""
1. choose random number for MMs in the jar
2. give the user 5 attempts to guess the correct number of MMs
3. tell the user if their guess is too low or 2 high
4. if the user guesses correctly, exit immediately and tell them the number of guesses it took them to guess correctly
"""

num = random.randint(1, 101)

count = 0

while count < 5:
    count += 1

    guess = int(input("Pick a number between 1 and 100: "))

    if guess < num:
        print("That number is too low.")
    elif guess > num:
        print("That number is too high.")
    else:
        print("That's correct!")
        break

print(f"Bye. You finished in {count} attempts.")

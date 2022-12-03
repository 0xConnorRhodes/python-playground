#!/usr/bin/env python3

while True:
    num = int(input("Please choose a number "))

    if num == 0:
        print("Goodbye")
        break
    elif num % 2 == 1:
        print("The number is odd.")
    else:
        print("The number is even.")

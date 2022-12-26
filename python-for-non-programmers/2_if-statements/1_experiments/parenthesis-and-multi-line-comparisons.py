#!/usr/bin/env py

x = 10

if (x == 10 # inside parenthesis, python does not care about whitespace
       or x == 15 or
x == 20):
    print("It is 10 or 15 or 20.")
else:
    print("It's another number")


#!/usr/bin/env python3

length = 10
astr = "*"

for i in range(length):
    for j in range(length-i):
        print(" ", end='')
    print(astr)
    astr = astr + "**"

length -= 1
astrNum = len(astr) - 4
space = 2

for i in range(length):
    print(" " * space, end='')
    print("*" * astrNum)
    astrNum -= 2
    space += 1

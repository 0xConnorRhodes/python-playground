#!/usr/bin/env python3

length = 11
space = 1
count = 0
astr = "*" * length

for i in range(length):
    for i in range(i):
        print(" ", end='')
    print(astr)
    astr = "*" * (len(astr) - 2 )
    if len(astr) < 1:
        break

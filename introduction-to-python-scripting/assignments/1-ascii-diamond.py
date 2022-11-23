#!/usr/bin/env python3

length = 10
astr = "*"

for i in range(length):
    for j in range(length):
        print("-", end='')
    print(astr)
    astr = astr + "**"

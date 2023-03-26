#!/usr/bin/env python3

from sys import argv

print(argv)

count = 0
for one_arg in argv:
    print(f'Argument {count} is {one_arg}')
    count += 1

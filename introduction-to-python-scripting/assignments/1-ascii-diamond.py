#!/usr/bin/env python3

length = 10
astr = "*"

# iterate 10 times
for i in range(length):
    # iterate to print spaces up to the first asterisk
    for j in range(length-i):
        print(" ", end='')
    # print the string of asterisk(s)
    print(astr)
    # increase asterisk string size
    astr = astr + "**"

# reduce length by one since the middle line is already drawn
length -= 1

# subtract 4 from asterisk number, 2 to undo the last addition on line 14 and 2 to reduce the length of the string one step below the middle line
astrNum = len(astr) - 4

# add a variable to increment for number of spaces.
# set to 2 because there is always at least one space (even on the middle line) because in line 9, the maximum value of i (set by range(0,10) in line 7) is 9. 
# This means that the smallest number of spaces  printed by the for loop in lines 9 and 10 is 10 - 9 which is 1.
space = 2

for i in range(length):
    print(" " * space, end='')
    print("*" * astrNum)
    astrNum -= 2
    space += 1

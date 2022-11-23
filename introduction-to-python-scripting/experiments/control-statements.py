#!/usr/bin/env python3

# break
for num in range(1,6):
    if num > 3:
        break
    print(num)

    if num == 4: # skipped
        print("It's four") # skipped

print("break done") # executed

# continue
for num in range(1,6):

    if num == 3:
        continue # skips printing 3

    print(num)

print("continue done")

# pass
for num in range(1,6):

    if num == 3:
        pass # pass allows the empty if to execute

    print(num)

print("pass done")

#!/usr/bin/env python3

length = 10
astr = "*"

for i in range(length):
    for j in range(length - i):
        print(" ", end='') # note replace space with `-` to get a clearer idea of how the nested loop works
    print(astr)
    astr += "**"

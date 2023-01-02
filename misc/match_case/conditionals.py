#!/usr/bin/env python3

myvar = 'a'
x = 10

match myvar:
    case 'a' | 'b' : # equivalent to a or b, but this is the only supported syntax
        print("It's a or b")
    case 'c' if x > 10: # equivalent to 'c' and x > 10, but this is the only supported syntax.
        print("It's c")
    case 'd' | 'e' as value: # value is assigned to the matched case and can be used in the code inside the case statement
        print("It's d or e")
        print(f"It was actually {value}")


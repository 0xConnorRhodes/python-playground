# (1) Ask the user to enter a number (x)
# (2) Ask the user to enter a second number (y)
# (3) Ask the user to enter "operation, either '+' or '*'
# (4) Print either x+y or x*y, depending on the operation

num1 = input("Enter a numer: ")
num2 = input("Enter another numer: ")

operation = input("Choose '+' or '*': ")

if operation == "+":
    solution = int(num1) + int(num2)
elif operation == "*":
    solution = int(num1) * int(num2)
else:
    print("That operation is invalid.")
    exit(1)

print(f"{num1} {operation} {num2} is {solution}")
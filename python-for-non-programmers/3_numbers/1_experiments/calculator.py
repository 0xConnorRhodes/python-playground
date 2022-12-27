# (1) Ask the user to enter a number (x)
# (2) Ask the user to enter a second number (y)
# (3) Ask the user to enter "operation, either '+' or '*'
# (4) Print either x+y or x*y, depending on the operation

num1 = int(input("Enter a numer: "))
num2 = int(input("Enter another numer: "))

operation = input("Choose '+' or '*': ")

if operation == "+":
    print(f"{num1} + {num2} is {num1 + num2}")
elif operation == "*":
    print(f"{num1} * {num2} is {num1 * num2}")
else:
    print("that operation is invalid")

'''
Ask the user to enter a string. Then ask the user to enter two numbers
(as separate inputs). Print the string from the first number to the
second number, assuming that both are legitimate indexes in the string.
If the user gives non-numbers, then scold them. If the user gives
indexes that are negative or too high, scold them. (Please don’t
scold your users when it comes to real software!) So if the user
enters abcdefg and the numbers 3 and 5, then we should see de in
the output, since that’s from index 3 to index 5 (not including 5).
'''

string = input("Please enter a string: ")
num1 = input("Enter the lower bound: ")

if '-' in num1:
    print("Sorry. This program does not accept negative indices.")
elif not num1.isdigit():
    print("Sorry. That is not a valid index")
    exit(1)
elif int(num1) < 1:
    print("Sorry. This program only supports indices from one.")
    exit(1)

num1 = int(num1)

num2 = input("Enter the upper bound: ")

if not num2.isdigit():
    print("Sorry. That is not a valid indes")
    exit(1)
elif int(num2) > len(string):
    print("Sorry. That number is too high for this string.")
    exit(1)
elif int(num2) < num1:
    print("Second index must be greater than the first.")
    exit(1)

num2 = int(num2)

print(string[num1:num2])
num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")

if not num1.isdigit() and not num2.isdigit():
    print(f"Sorry, neither {num1} nor {num2} are digits.")
    exit(1)
elif not num1.isdigit():
    print(f"Sorry, {num1} is not a digit.")
    exit(1)
elif not num2.isdigit():
    print(f"Sorry, {num2} is not a digit.")
    exit(1)
elif num1.isdigit() and num2.isdigit():
    print(f"The sum of {num1} and {num2} is {int(num1) + int(num2)}")

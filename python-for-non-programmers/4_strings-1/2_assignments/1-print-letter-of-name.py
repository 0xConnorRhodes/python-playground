# Ask the user to enter their name
# and assign that to a variable called name.
# Then ask the user to enter an integer,
# and assign that to a variable called index.
# (You can assume, for now, that the index
# is legal for this string.) Print the letter at that index.

name = input("Enter your name: ")

index = int(
    input("*Print nth character* Enter n: ")
    # subtract 1 to fix with python's indexing from 0
    ) - 1

print(name[index])


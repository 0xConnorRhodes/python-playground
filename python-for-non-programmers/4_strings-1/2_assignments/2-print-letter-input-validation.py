# Now modify the above code,
# so that you check whether index is legal.
# If the user enters either a negative number
# or a positive number that’s too high, then scold them.
# Otherwise, print the letter at that index.

name = input("Enter your name: ")

index = int(
    input("*Print nth character* Enter n: ")
    # subtract 1 to fix with python's indexing from 0
) - 1

print(name[index])

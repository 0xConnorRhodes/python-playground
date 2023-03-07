# Now modify the above code,
# so that you check whether index is legal.
# If the user enters either a negative number
# or a positive number that’s too high, then scold them.
# Otherwise, print the letter at that index.

name = input("Enter your name: ")

index = int(input("*Print nth character* Enter n: "))

if index > len(name):
    print("Sorry. That index is too high.")
    exit(1)
elif index <= 0:
    print("Sorry. That index is too low.")
    exit(1)
else:
    print(name[index-1])

# Now modify the above code,
# so that you check whether index is legal.
# If the user enters either a negative number
# or a positive number that’s too high, then scold them.
# Otherwise, print the letter at that index.

vowels = ['a', 'e', 'i', 'o', 'u']

name = input("Please enter a name: ")

if name[-1] in vowels:
    print("That name ends with a vowel.")
else:
    print("That name does not end with a vowel.")

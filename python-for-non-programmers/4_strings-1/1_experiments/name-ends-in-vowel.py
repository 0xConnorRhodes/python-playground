vowels = ['a', 'e', 'i', 'o', 'u']

name = input("Please enter a name: ")

if name[len(name) - 1] in vowels:
    print("That name ends with a vowel.")
else:
    print("That name does not end with a vowel.")

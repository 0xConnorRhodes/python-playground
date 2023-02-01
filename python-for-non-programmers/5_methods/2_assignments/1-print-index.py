'''
Ask the user to enter a string. Now ask the user to enter a letter.
Print the index at which that letter was found, as well as the one
letter preceding and the one letter following what was asked for.
For example, if the string is abcdefg and the user asks to find c,
then the program should print 2 (the index where c can be found),
and the string bcd. Note that the program should ignore any
leading or trailing whitespace in the user’s input.
'''

string = input("Please enter a string: ")

letter = input("Enter a letter to search for: ")
letter = letter.strip()

if len(letter) < 1:
    print(f"It doesn't look like you entered a letter. Please enter a letter.")
    exit(1)
elif len(string) == 0:
    print(f"It doesn't look like you entered a string. Please enter a string.")
    exit(1)
elif len(letter) > 1:
    print(f"Sorry, that is too many characters. Please enter one letter.")
    exit(1)
elif not letter.isalpha():
    print(f"Sorry, {letter} is not a letter.")
    exit(1)
elif letter not in string:
    print(f"Sorry, {letter} is not in the string.")
    exit(1)
elif letter in string:
    index = string.index(letter)
    print(f"Letter {letter} is in string {string} at index {index}.")

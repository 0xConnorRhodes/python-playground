# Ask the user to enter their name. Print a “name triangle,” meaning: On the first line, print just the first letter. Then on the second line, print the first two letters. Then on the third line, print the first three letters… If the name is n letter long, then there should be n lines, with the nth line printing the user’s name (as entered).

name = input("Enter your name: ")

line = 1

while line <= len(name):
    print(name[:line])
    line += 1

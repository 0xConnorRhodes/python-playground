# Password Generator Project
import random as r
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pw_letters = []
for i in range(0, nr_letters):
    choice = letters[r.randint(0, len(letters)-1)]
    pw_letters.append(choice)

pw_numbers = []
for i in range(0, nr_numbers):
    choice = numbers[r.randint(0, len(numbers)-1)]
    pw_numbers.append(choice)

pw_symbols = []
for i in range(0, nr_symbols):
    choice = symbols[r.randint(0, len(symbols)-1)]
    pw_symbols.append(choice)

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#combined_string = ''
#for i in pw_letters:
#    combined_string += i
#
#for i in pw_numbers:
#    combined_string += i
#
#for i in pw_symbols:
#    combined_string += i
#
#print(f"Here is your password: {combined_string}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

combined_list = []
for i in pw_numbers:
    combined_list.append(i)

for i in pw_letters:
    combined_list.append(i)

for i in pw_symbols:
    combined_list.append(i)

random_list = []
for i in range(0, len(combined_list)):
    choice = r.randint(0, len(combined_list)-1)
    random_list.append(combined_list[choice])
    del(combined_list[choice])

combined_string = ''
for i in random_list:
    combined_string += i

print(f"Here is your password: {combined_string}")

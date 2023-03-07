input_numbers = input("Enter a list of numbers separated by spaces: ").split()


# convert all numbers to integers
numbers = []
for one_number in input_numbers:
    numbers.append(int(one_number))

even_numbers_int = []
odd_numbers_int = []
for one_number in numbers:
    if one_number % 2 == 0:
        even_numbers_int.append(one_number)
    else:
        odd_numbers_int.append(one_number)

# convert the even numbers back to strings for printing
even_numbers_string = []
for one_number in even_numbers_int:
    even_numbers_string.append(str(one_number))

# convert the odd numbers back to strings for printing
odd_numbers_string = []
for one_number in odd_numbers_int:
    odd_numbers_string.append(str(one_number))


print('The even numbers are:' + '\n' + '\n'.join(even_numbers_string))
print('')
print('The odd numbers are:' + '\n' + '\n'.join(odd_numbers_string))

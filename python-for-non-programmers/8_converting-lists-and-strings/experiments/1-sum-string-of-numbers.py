num_string = input('Enter a string of numbers separated by spaces:\n').strip()

num_list = num_string.split()

count = 0
for one_number in num_list:
    count += int(one_number)

print(f'The sum of those numbers is {count}.')

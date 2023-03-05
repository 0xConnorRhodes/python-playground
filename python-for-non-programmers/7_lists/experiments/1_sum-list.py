numbers = [1, 2, 3, 4, 5]

count = 0

for one_number in numbers:
    count += one_number

mean = count / len(numbers)

print(f"The sum of the numbers is {count}")
print(f"The mean of the numbers is {mean}")

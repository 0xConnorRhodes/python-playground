numbers = []

while True:
    num = input("Please enter a number: ")

    if num == "":
        break
    elif not num.isdigit():
        print("That's not a number.")
        continue

    num = int(num)

    numbers.append(num)

# add all the numbers without the sum() function
count = 0

for one_number in numbers:
    count += one_number

average = count / len(numbers)

high_numbers = []
for one_number in numbers:
    if one_number > average:
        high_numbers.append(one_number)

low_numbers = []
for one_number in numbers:
    if one_number < average:
        low_numbers.append(one_number)




print(f"The average of those number is {average}")
print(f"The numbers above the average are {high_numbers}")
print(f"The numbers below the average are {low_numbers}")

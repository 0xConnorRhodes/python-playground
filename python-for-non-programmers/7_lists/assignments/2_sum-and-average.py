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




print(f"The average of those number is {average}")

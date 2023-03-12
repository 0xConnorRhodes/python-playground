# prompt the user for a number
# write only the number from nums.txt that are >= the given number

number = int(input("Enter a number: "))

with open('nums.txt') as infile, open('selected-nums.txt', 'w') as outfile:
    nums = []
    for one_line in infile:
        one_line = one_line.strip()

        if not one_line.isdigit(): continue

        nums.append(one_line)

    selected = []
    for one_number in nums:
        one_number = int(one_number)

        if one_number >= number:
            selected.append(one_number)

    for one_number in selected:
        outfile.write(str(one_number) + '\n')

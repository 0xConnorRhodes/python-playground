file = open('nums.txt')

count = 0
for one_line in file:
    one_line = one_line.strip()

    if not one_line.isdigit():
        continue

    count += int(one_line)

print(count)

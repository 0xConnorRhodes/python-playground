file = open('linux-etc-passwd.txt')

for one_line in file:
    one_line = one_line.strip()

    if one_line == "": continue
    if one_line[0] == "#": continue

    username = one_line.split(':')[0]

    print(username)

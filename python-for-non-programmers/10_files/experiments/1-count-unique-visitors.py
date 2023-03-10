file = open('mini-access-log.txt')

counts = {}
for one_line in file:
    ip_address = one_line.split()[0]

    if ip_address not in counts:
        counts[ip_address] = 1
    else:
        counts[ip_address] += 1

for visitor, count in counts.items():
    print(f'{visitor}: {count}')

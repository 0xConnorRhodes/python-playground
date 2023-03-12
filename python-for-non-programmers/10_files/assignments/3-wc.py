file = open('wcfile.txt')

counts = {'lines': 0,
          'characters': 0,
          'words': 0}

for one_line in file:
    counts['lines'] += 1
    counts['characters'] += len(one_line)
    counts['words'] += len(one_line.split())

for key, value in counts.items():
    print(f'{key}: {value}')


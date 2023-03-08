counts = {}
while True:
    word = input('Enter a word: ')

    if word == '':
        break

    for one_char in word:
        if one_char in counts:
            counts[one_char] += 1
        else:
            counts[one_char] = 1

for key, value in counts.items():
    print(f'{key}: {value}')

sentence = input("Enter a sentance:\n").strip()

counts = {
        'digits': 0,
        'vowels': 0,
        'other': 0
        }

for one_char in sentence:
    if one_char.isdigit():
        counts['digits'] += 1
    elif one_char in 'aeiou':
        counts['vowels'] += 1
    else:
        counts['other'] += 1

for key, value in counts.items():
    print(f'{key}: {value}')

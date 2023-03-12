vowel_counts = {}
while True:
    word = input("Enter a word: ").strip()

    if word == '': 
        break

    vowels = 0
    for one_letter in word:
        if one_letter.lower() in 'aeiou':
            vowels += 1

    vowel_counts[word] = vowels

for word, count in vowel_counts.items():
    print(f'{word}: {count}')


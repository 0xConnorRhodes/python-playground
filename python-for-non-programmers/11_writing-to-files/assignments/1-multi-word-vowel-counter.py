vowel_counts = {}
while True:
    sentence = input("Enter a sentence: ").strip()
    if sentence == '':break

    words = sentence.split()

    for one_word in words:
        vowels = 0
        for one_letter in one_word:
            if one_letter.lower() in 'aeiou':
                vowels += 1

        vowel_counts[one_word] = vowels

for word, count in vowel_counts.items():
    print(f'{word}: {count}')


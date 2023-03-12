with open('word-list.txt', 'w') as outfile:
    while True:
        sentence = input("Enter a sentence: ").strip()

        if sentence == '':
            break
    
        words = sentence.split()
    
        for one_word in words:
            vowels = 0
            for one_letter in one_word:
                if one_letter.lower() in 'aeiou':
                    vowels += 1
    
            outfile.write(f'{one_word} {vowels}\n')

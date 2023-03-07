import re

sentence = input("Please enter a sentence:\n").strip().lower()

sentence = re.sub('[^a-z ]', '', sentence)

sentence = sentence.split()

pl_sentence = []
for one_word in sentence:
    if one_word[0] in 'aeiou':
        pl_word = one_word + 'way'
    else:
        pl_word = one_word[1::] + one_word[0] + 'ay'

    pl_sentence.append(pl_word)

pl_sentence = ' '.join(pl_sentence)

print(pl_sentence)

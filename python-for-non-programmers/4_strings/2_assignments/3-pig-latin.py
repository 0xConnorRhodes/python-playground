# Ask the user to enter a word, and assign it to the variable word.
# Then print the translation of the word into Pig Latin.

word = input("Please enter a word: ")

if word[0] in 'aeiou':
    pl_word = word + 'way'
else:
    pl_word = word[1::] + word[0] + 'ay'

print(pl_word)

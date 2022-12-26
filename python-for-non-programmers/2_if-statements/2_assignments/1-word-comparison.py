word1 = input("Please enter a word: ")
word2 = input("Please enter another word: ")

if word1 == word2:
    print("The words are the same")
elif word1 < word2:
    print(f"{word1} comes first in the alphabet.")
else:
    print(f"{word2} comes first in the alphabet.")

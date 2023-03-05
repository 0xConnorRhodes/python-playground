# Create a list containing words (i.e., strings). Ask the user to enter a search string. Print all of the words in that list containing the user’s input.

words = ["this", "is", "a", "list", "of", "words"]

query = input("Enter a search string: ")

matches = []
for one_word in words:
    if query in one_word:
        matches.append(one_word)

if len(matches) < 1:
    print("There were no matches.")
else:
    print(f"{query} is present in {matches}")


count = 0

while True:
    word = input("Please enter a word: ")

    if word == "":
        break

    for one_letter in word:
        if one_letter in 'aeiou':
            count += 1

print(f"Those words have a total of {count} vowels in them.")

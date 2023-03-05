# Ask the user to enter a sentence. Print the number of vowels, digits, and other characters that were in the user’s input

sentence = input("Please enter a sentance: ")

sentence = sentence.lower()

vowel_count = 0
digit_count = 0
other_count = 0

for one_char in sentence:
    if one_char in 'aeiou':
        vowel_count += 1
    elif one_char in '1234567890':
        digit_count += 1
    else:
        other_count += 1

print(f"That sentance has {vowel_count} vowels, {digit_count} digits, and {other_count} other characters.")

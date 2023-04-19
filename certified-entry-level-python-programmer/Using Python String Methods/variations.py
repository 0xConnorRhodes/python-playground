#!/usr/bin/env python3

message = input("Enter a string: ").strip()

print(f'lowercase: {message.lower()}')
print(f'uppercase: {message.upper()}')
print(f'titlecase: {message.title()}')
print(f'capitalized: {message.capitalize()}')

words = message.split()
print(f'words: {words}')

first_word = sorted([word.lower() for word in words])[0]
print(f'the first word is {first_word}')

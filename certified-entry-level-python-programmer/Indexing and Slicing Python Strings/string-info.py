#!/usr/bin/env python3

input_string = input("Enter a string: ")

print(f'The first character in the string is {input_string[0]}')
print(f'The last character in the string is {input_string[-1]}')

middle_char = input_string[int(len(input_string) / 2)]

print(f'The middle character of the string is {middle_char}')

even_chars = list(input_string[::2])

print(f'The even characters are {even_chars}')

odd_chars = list(input_string[1::2])

print(f'The odd characters are {odd_chars}')

print(f'The string in reverse is {input_string[::-1]}')

file = open('wcfile.txt')

char_count = 0
for one_char in open('wcfile.txt').read():
    char_count += 1

print(f'wcfile.txt has {char_count} characters.')

line_count = 0
for one_line in open('wcfile.txt'):
    line_count += 1

print(f'wcfile.txt has {line_count} lines.')

word_list = []
for one_line in open('wcfile.txt'):
    one_line = one_line.split()

    for one_word in one_line:
        word_list.append(one_word)

word_count = 0
for one_word in word_list:
    word_count += 1

print(f'wcfile.txt has {word_count} words.')

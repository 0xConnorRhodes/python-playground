def charcount(string):
    chars = {}
    for one_char in string:
        if not one_char in chars:
            chars[one_char] = 1
        else:
            chars[one_char] += 1

    return chars


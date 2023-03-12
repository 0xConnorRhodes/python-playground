def countVowels(word):
    count = 0
    for one_letter in word:
        if one_letter in 'aeiou':
            count += 1
    return count

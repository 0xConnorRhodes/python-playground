# length: number_of_occurrances
def wordslength(file):
    dictionary = {}
    for one_line in open(file):
        for one_word in one_line.split():
            key = len(one_word)
            if key not in dictionary:
                dictionary[key] = 1
            else:
                dictionary[key] += 1
    return dictionary


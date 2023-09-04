from random import shuffle as list_shuffle


def reverse(str_value):
    index = 0
    reversed_string = ''
    for i in range(len(str_value)):
        index -= 1
        reversed_string += str_value[index]
    return reversed_string


def shuffle(str_value):
    as_list = list(str_value)
    list_shuffle(as_list)
    return ''.join(as_list)

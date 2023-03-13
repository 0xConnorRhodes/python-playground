def factor(dictionary, factor=2):
    new_dict = {}

    for key, value in dictionary.items():
        new_dict[key] = value * factor

    return new_dict


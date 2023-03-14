def countExtensions(folder):
    import os

    extensions = {}
    for one_item in os.listdir(folder):
        if '.' not in str(one_item):
            continue
        one_extension = str(
                one_item.rsplit('.', maxsplit=1)[1]
                )

        if one_extension not in extensions:
            extensions[one_extension] = 1
        else:
            extensions[one_extension] += 1

    return extensions


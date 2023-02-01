string = 'abc abc abc'
searching_for = 'a'

count = string.count(searching_for)

start_from = 0

for i in range(count):
    index = string.index(searching_for, start_from)
    print(index)
    start_from = index + 1



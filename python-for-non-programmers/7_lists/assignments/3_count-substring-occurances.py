string = input("Please enter a string to search: ")

query1 = input("Please enter a search query: ")
query2 = input("Please enter a second search query: ")

total1 = string.count(query1)
total2 = string.count(query2)

print(f'Found {query1} {total1} times.')
print(f'Found {query2} {total2} times.')


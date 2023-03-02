digits = input("Enter a string of digits: ")

try:
    int(digits)
except: 
    print("Sorry. Please enter a string of only digits")
    exit(1)

count = 0

for i in digits:
    count = count + int(i)

print(f"The sum of all those digits is {count}")


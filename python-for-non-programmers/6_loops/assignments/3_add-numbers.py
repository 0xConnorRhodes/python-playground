count = 0

while True:

    num = input("Enter a number: ").strip()

    if num == "":
        break
    elif not num.isdigit():
        print("That's not a number.")
        continue
    else: 
        count += int(num)

print(f"The total count is {count}.")

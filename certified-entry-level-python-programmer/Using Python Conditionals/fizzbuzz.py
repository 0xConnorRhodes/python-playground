
given = int(input("Enter an integer value: "))

if given % 5 == 0 and given % 3 == 0:
        print("FizzBuzz")
elif given % 5 == 0:
    print("Buzz")
elif given % 3 == 0:
    print("Fizz")
else:
    print(f"{given} is not FizzBuzzable.")
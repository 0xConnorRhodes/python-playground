
countdown = int(input("How many values should we FizzBuzz: "))

for num in range(1, countdown+1):
    if num % 5 == 0 and num % 3 ==0:
        print('FizzBuzz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 3 == 0:
        print('Fizz')
    else:
        print(num)


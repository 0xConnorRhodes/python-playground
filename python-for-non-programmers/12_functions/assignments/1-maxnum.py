# Write a function, maxnum, that takes a single argument, a list of numbers. It returns the largest number in that list. (Do not use the built-in max function to do this!)

def maxnum(numbers):
    numbers.sort(reverse=True)
    return numbers[0]


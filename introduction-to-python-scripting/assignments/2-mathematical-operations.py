#!/usr/bin/env python3

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by 0"
    return num1 / num2

num1 = 10
num2 = 2

print(add(num1, num2))

print(subtract(num1, num2))

print(multiply(num1, num2))

print(divide(num1, num2))

num2 = 0
print(divide(num1, num2))

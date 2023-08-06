# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# concat the names together
name_pair = name1 + name2

# count for the letters of true in both names
# lower() makes the names all lowercase to make counting accurate
# count() counts the number of occurrences of each letter, and reports as an integer.
true_count = (
        name_pair.lower().count("t")
        + name_pair.lower().count("r")
        + name_pair.lower().count("u")
        + name_pair.lower().count("e")
)

# count for the letters of true in both names
love_count = (
        name_pair.lower().count("l")
        + name_pair.lower().count("o")
        + name_pair.lower().count("v")
        + name_pair.lower().count("e")
)

# concat numbers together and convert back to an int to remove leading zeroes
compatibility = int(str(true_count) + str(love_count))

if compatibility < 10 or compatibility > 90:
    print(f"Your score is {compatibility}, you go together like coke and mentos.")
elif compatibility >=40 and compatibility <= 50:
    print(f"Your score is {compatibility}, you are alright together.")
else:
    print(f"Your score is {compatibility}.")

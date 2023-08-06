# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Write your code below this line 👇

# a leap year is
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

# for example: 2020 and 2024 are leap years. 2022 is not

# if {year} is evenly divisible by 4
if year % 4 == 0:
    # then if it is also evenly divisible by 100...
    if year % 100 == 0:
        # check if it's also evenly divisible by 400.
        # if so, it is a leap year
        if year % 400 == 0:
            print(f"Leap year.")
        # but if not, it isn't a leap year
        else:
            print(f"Not a leap year.")
    # or if it isn't evently divisible by 100 at all
    else:
        print(f"Leap year.")
else:
    print(f"Not leap year.")

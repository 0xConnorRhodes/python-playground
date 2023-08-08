print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("Choose which way to go: \"left\" or \"right\"\n").lower()

if choice1 == "left":
    print("You come to the door")
elif choice1 == "right":
    print("You fall into a hole.\nGame Over")
    exit(0)
else:
    print("Sorry, that is not a valid choice")
    exit(1)

choice2 = input("You come to a river. Do you \"swim\" or \"wait\" for the ferry.\n").lower()

if choice2 == "swim":
    print("You are eaten by piranhas.\nGame Over")
    exit(0)
elif choice2 == "wait":
    print("The ferry carries you across the river.")
else:
    print("Sorry, that is not a valid choice")
    exit(1)

choice3 = input("You come to three doors. One red, one yellow, and one blue. Which door do you open?\n").lower()

if choice3 == "yellow":
    print("You Win!")
    exit(0)
elif choice3 == "red":
    print("You are burned by fire.\nGame Over")
    exit(0)
elif choice3 == "blue":
    print("You are eaten by beasts.\nGame Over")
    exit(0)
else:
    print("Sorry, that is not a valid choice")
    exit(1)

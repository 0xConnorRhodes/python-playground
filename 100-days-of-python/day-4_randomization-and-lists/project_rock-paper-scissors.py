import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n")

if player_choice not in ['0', '1', '2']:
    print("You typed an invalid choice.")
    exit(1)

player_choice = int(player_choice)

computer_choice = random.randint(0, 2)

def print_choices():
    print(f"You chose:\n{choices[player_choice]}")
    print(f"Computer chose:\n{choices[computer_choice]}")

if player_choice == computer_choice:
    print_choices()
    print("It's a tie.")
elif player_choice == 2 and computer_choice == 0:
    print_choices()
    print("You lose.")
elif computer_choice == 2 and player_choice == 0:
    print_choices()
    print("You win.")
elif player_choice > computer_choice:
    print_choices()
    print("You win.")
elif computer_choice > player_choice:
    print_choices()
    print("You lose.")


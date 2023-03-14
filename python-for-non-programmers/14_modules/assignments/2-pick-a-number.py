def pickNumber(items):
    import random
    choice = random.choice(items)

    count = 0

    while True:
        guess = input("Enter your guess: ")


        if guess != str(choice):
            count += 1
            print("Sorry. That's not it.")
            continue
        else:
            count += 1
            print(f"That's correct! It was {choice}.")
            break

    return f'You took {count} guesses.'


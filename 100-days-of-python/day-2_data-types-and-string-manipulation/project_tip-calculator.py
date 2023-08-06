print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
split_number = int(input("How many people to split the bill? "))
bill_split = bill / split_number

tip_pct = 0.01 * int(input("What percentage tip would you like to give? "))
total_tip = bill * tip_pct
tip_split = total_tip / split_number

person_amt = "{:.2f}".format(round((bill_split + tip_split), 2))

print(f"Each person should pay ${person_amt}")

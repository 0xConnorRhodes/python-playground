import datetime

birth_year = int(input("What year were you born?: "))

current_day = datetime.date.today()
current_year = current_day.year

age = current_year - birth_year

print(f"This year you will turn {age}.")
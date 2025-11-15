months = {
    1: ("January", 31),
    2: ("February", 28), 
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

month = int(input("Enter the month number (1-12): "))

if month < 1 or month > 12:
    print("That is invalid! Please enter a number between 1 and 12.")
else:
    month_name, days = months[month]
    if month == 2:
        leap_year = input("Is it a leap year? (Yes/No): ")
        if leap_year.lower() == "yes":
            days = 29
    print(f"{month_name} has {days} days.")
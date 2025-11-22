# Store the months, their numbers, their number of day values and the name of the month as key-pair values in a dictionary
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

# Ask the user to input the month number
month = int(input("Enter the month number (1-12): "))

# Check using an if-else statement to see if the input is valid
if month < 1 or month > 12:
    print("That is invalid! Please enter a number between 1 and 12.")
else:
    # Define that the month name and number of days is according to the corresponding month number inputted
    month_name, days = months[month]
    if month == 2:
        # Ask the user if it is a leap year
        leap_year = input("Is it a leap year? (Yes/No): ")
        if leap_year.lower() == "yes":
            # If yes, the number of days is adjusted
            days = 29
    # Print the month name and number of days according to the user's input
    print(f"{month_name} has {days} days.")
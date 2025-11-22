# Store the name and hometown variables in a dictionary
information = {
    # Ask the user to input their name
    "name": str(input("What is your name? ")),
    # Ask the user to input their hometown
    "hometown": str(input("What is your hometown? ")),
}

# Check if the user inputs a valid number for their age
while True:
    # Ask the user to input their age
    age_input = input("What is your age? ")
    if age_input.isdigit():
        age = int(age_input)
        break
    # If age is an invalid number, print an appropriate message
    else:
        print("That's an invalid number. Please enter a valid age number.")

# Print the information in a single print statement
print (information["name"] + "\n" + information["hometown"] + "\n" + age_input)
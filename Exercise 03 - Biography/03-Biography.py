information = {
    "name": str(input("What is your name? ")),
    "hometown": str(input("What is your hometown? ")),
}

while True:
    age_input = input("What is your age? ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("That's an invalid number. Please enter a valid age number.")

print (information["name"] + "\n" + information["hometown"] + "\n" + age_input)
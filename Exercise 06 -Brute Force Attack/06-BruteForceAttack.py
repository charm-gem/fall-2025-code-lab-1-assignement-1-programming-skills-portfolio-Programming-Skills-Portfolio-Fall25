# Define the correct password
correct_password = 12345
# Define login, attempts and maximum attempt variables for the while loop
login = 0
attempts = 0
max_attempts = 5

# Use a while loop to repeatedly ask the user for the password
while login == 0 and attempts < max_attempts:
    password = int(input("Please enter your password: "))
    if password == correct_password:
        login = login + 1
    else:
        attempts = attempts + 1
        remain = max_attempts - attempts
        # Inform the user that their attempt is incorrect and inform them of the remaining attempts left
        if remain > 1:
            print(f"That is incorrect. You have {remain} attempts left.")
        elif remain == 1:
            print(f"That is incorrect. You have {remain} attempt left.")
if login == 1:
    # Print an appropriate message if the password is correct
    print ("You entered the correct password.")
else:
    # Print an appropriate message if the maximum number of attempts is reached and that the authorities have been alerted
    print ("You have reached the maximum number of attempts. The authorities have been alerted.")
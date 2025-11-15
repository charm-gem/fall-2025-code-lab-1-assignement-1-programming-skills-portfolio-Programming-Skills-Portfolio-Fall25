names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
found = "sam".lower()



correct_password = 12345
login = 0
attempts = 0
max_attempts = 5

while login == 0 and attempts < max_attempts:
    password = int(input("Please enter your password: "))
    if password == correct_password:
        login = login + 1
    else:
        attempts = attempts + 1
        remain = max_attempts - attempts
        if remain > 1:
            print(f"That is incorrect. You have {remain} attempts left.")
        elif remain == 1:
            print(f"That is incorrect. You have {remain} attempt left.")
if login == 1:
    print ("You entered the correct password.")
else:
    print ("You have reached the maximum number of attempts. The authorities have been alerted.")
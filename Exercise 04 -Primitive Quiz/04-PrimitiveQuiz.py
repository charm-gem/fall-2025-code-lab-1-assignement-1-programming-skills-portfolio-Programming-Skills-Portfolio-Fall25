# Store the countires and their capitals as key-pair values in a dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Norway": "Oslo",
    "Sweden": "Stockholm",
    "Ukraine": "Kyiv",
    "Denmark": "Copenhagen"
}

# Print the questions for the quiz
for country, capital in capitals.items():
    # Ask the user to input the capital of a country and disregard upper/lowercase spellings
    answer = input(f"What is the capital of {country}? ").lower()
    # Print an appropriate response if the user's answer is correct
    if answer == capital.lower():
        print("That answer is correct!")
    # Print an appropriate response if the user's answer is incorrect
    else:
        print(f"That answer is incorrect! The correct answer is {capital}.")
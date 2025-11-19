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

for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}? ").lower()
    if answer == capital.lower():
        print("That answer is correct!")
    else:
        print(f"That answer is incorrect! The correct answer is {capital}.")
# Define names dictionary list
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Ask the user to input what name they're searching for
search_name = input("Enter the name you want to search for: ")
# Define the found variable before a name is found
found = False

for name in names:
    if name.lower() == search_name.lower():
        # Redefine found variable once a name is found
        found = True
        # Print an appropriate message if Sam is found
        if name == "Sam":
            print(f"Yes, {name} is in the list. You found {name}!")
        # Print an appropriate message if another name is found in the list but is not Sam
        else:
            print(f"{name} is in the list but that's not who you're looking for.")

# If name is not listed, print an appropriate message
if not found:
    print("That person is not in the list.")

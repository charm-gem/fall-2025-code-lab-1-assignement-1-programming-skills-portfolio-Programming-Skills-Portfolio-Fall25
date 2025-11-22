# Define main function to ask for a number and print the corresponding message depending on the user's input
def main():
    # Ask user to input a number
    num = int(input("Enter a number: "))
    # Define the corresponding message depending on the even_odd(num) function
    message = even_odd(num)
    # Print the message
    print(message)

# Define even_odd(num) function to return the right corresponding message
def even_odd(num): 
    # If the inputted num is divisible by 2 and equals 0 then print that number is even
    if (num % 2) == 0:
        return "The number is even."
    # If the inputted num's output is any other then print that number is odd
    else:
        return "The number is odd."

# If the code is run directly from the built-in variable then print main function
if __name__ == "__main__":
    main()
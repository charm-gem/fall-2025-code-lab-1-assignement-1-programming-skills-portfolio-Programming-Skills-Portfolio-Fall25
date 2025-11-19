def main():
    num = int(input("Enter a number: "))
    message = even_odd(num)
    print(message)
    
def even_odd(num): 
    if (num % 2) == 0:
        return "The number is even."
    else:
        return "The number is odd."

if __name__ == "__main__":
    main()
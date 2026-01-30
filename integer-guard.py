def main():
    number = get_number()
    print(f"Validated number: {number}")

def get_number():
    while True:
        try:
            return int(input("Please enter a number: "))
        except ValueError:
            # This triggers if the input is not a valid integer
            print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()

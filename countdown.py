def main():
    try:
        number = int(input("Start countdown from: "))
        countdown(number)
    except ValueError:
        print("Please enter a valid integer.")

def countdown(n):
 
    while n > 0:
        print(n)
        n -= 1
    print("Fire! ")

if __name__ == "__main__":
    main()

def check_number(number):
    if number > 0:
        print("The number is Positive (+)")
  
    elif number < 0:
        print("The number is Negative (-)")

    else:
        print("The number is Zero (0)")

user_input = float(input("Enter a number: "))

check_number(user_input)
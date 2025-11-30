def simple_calculator(num1, num2):
    addition = num1 + num2        
    subtraction = num1 - num2     
    multiplication = num1 * num2  
    division = num1 / num2        

    print("--- Results ---")
    print(f"Sum (+): {addition}")
    print(f"Difference (-): {subtraction}")
    print(f"Product (*): {multiplication}")
    print(f"Division (/): {division}")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

simple_calculator(number1, number2)
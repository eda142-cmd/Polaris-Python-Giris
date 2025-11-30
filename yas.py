def calculate_100_years(name, age):
    current_year = 2025
    years_left = 100 - age
    target_year = current_year + years_left
    
    print(f"Hi {name}, you will be 100 years old in {target_year}.")

user_name = input("What is your name?: ")
user_age = input("How old are you?: ")

user_age = int(user_age)

calculate_100_years(user_name, user_age)
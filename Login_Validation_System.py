import re

def main():
    password = input("Set a new password: ")
    if is_strong(password):
        print("Success: Your password is strong! ")
    else:
        print("Warning: Password too weak. ")

def is_strong(s):
    # ^: Start, $: End
    # (?=.*[A-Z]): At least one uppercase
    # (?=.*\d): At least one digit
    # (?=.*[@$!%*?&]): At least one special character
    # .{8,}: At least 8 characters long
    pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    if re.search(pattern, s):
        return True
    return False

if __name__ == "__main__":
    main()

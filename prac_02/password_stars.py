MINIMUM_LENGTH = 6
password = input("Enter your password: ")
if len(password) < MINIMUM_LENGTH:
    print("Your password is too short")
    password = input("Enter your password: ")
print("*" * len(password))
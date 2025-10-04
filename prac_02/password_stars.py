MINIMUM_LENGTH = 6
def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)

def get_password(MINIMUM_LENGTH):
    password = input("Enter your password: ")
    if len(password) < MINIMUM_LENGTH:
        print("Your password is too short")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    print("*" * len(password))

main()

def main():
    """get the length of the password and print the star related to the length of password"""
    minimum_length = 4
    password = get_password(minimum_length)
    print_asterisks(password)

def get_password(minimum_length):
    """get the length of the password and make sure the length of the password is at least 4"""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password must be at least 4 characters long")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password

def print_asterisks(password):
    """print the asterisks of the password"""
    print("*" * len(password))

main()
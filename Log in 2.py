def get_user_input():
    username = input("Enter your username: ")
    new_password = input("Enter your new password: ")
    confirm_password = input("Confirm your new password: ")
    return username, new_password, confirm_password

def validate_password(new_password, confirm_password):
    if new_password != confirm_password:
        print("Error: Passwords do not match.")
        return False
    elif len(new_password) < 8:
        print("Error: Password should be at least 8 characters long.")
        return False
    return True

def main():
    username, new_password, confirm_password = get_user_input()
    
    while not validate_password(new_password, confirm_password):
        # Prompt user again until a valid password is provided
        username, new_password, confirm_password = get_user_input()

    print("Registration successful!")
    
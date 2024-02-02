def create_account():
    username = input("Enter your username: ")
    while True:
        new_password = input("Enter your new password: ")
        # Checks if password is up to 8 characters
        if len(new_password) < 8:
            print("The password must be at least 8 characters long.")
            continue
        confirm_password = input("Confirm your new password: ")
        # Checks if passwords match
        if new_password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            print("Account created successfully!")
            break

# Call the function to start the account creation process
create_account()

username = input("Username: ")

New_password = input("New password: ".capitalise())

Confirm_password = input("Confirm password: ")


if Confirm_password == New_password:
    print("Saved sucessfully")
else:
    print("Password Mismatch")

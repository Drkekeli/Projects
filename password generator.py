import random

print("Your Password: ")

chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&()_+-=?><"

password = ""
for x in range(10):
    password += random.choice(chars)

print(password)

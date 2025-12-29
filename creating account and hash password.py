import bcrypt

username = input("Please enter desired username ")
password = bcrypt.hashpw(input("Please enter desired password ").encode(), bcrypt.gensalt())

users = {}

users.update({username: password})
print(f"Thank you, your account was created!")
print(f"{users}")
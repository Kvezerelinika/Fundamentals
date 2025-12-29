username = input("Please enter desired username ")
password = input("Please enter desired password ")

users = {}

users.update({username: password})
print(f"Thank you, your account was created!")
print(f"{users}")
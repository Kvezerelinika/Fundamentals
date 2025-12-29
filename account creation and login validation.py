import bcrypt

username = input("Please enter desired username ")
password = bcrypt.hashpw(input("Please enter desired password ").encode(), bcrypt.gensalt())

users = {}

users.update({username: password})
print(f"Thank you, your account was created!")
print(f"{users}")

attempts = 3

while attempts > 0:
    name = input("Username: ")
    password = input("Password: ").encode()
    if name not in users:
        print("Username is incorrect!")
        attempts -= 1
    elif not bcrypt.checkpw(password, users[name]):
        print("Password is incorrect!")
        attempts -= 1
    else:
        print("Username and Password is correct!")
        break
else:
    print("Account is locked.")

    
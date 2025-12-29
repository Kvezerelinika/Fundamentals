import bcrypt

users = {}

def creation():
    username = input("Please enter desired username ").strip()

    if username in users:
        print("This username already exists!")
        return

    password = input("Please enter desired password ").encode()
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    users[username] = hashed_password
    print(f"Thank you, your account was created!")
    print(f"{users}")

def validation():
    attempts = 3

    while attempts > 0:
        name = input("Username: ").strip()
        password = input("Password: ").encode()

        if name not in users:
            print("Username is incorrect!")
        elif not bcrypt.checkpw(password, users[name]):
            print("Password is incorrect!")
        else:
            print("Username and Password is correct!")
            return
        attempts -= 1
        print(f"Attempts left: {attempts}")
    print("Account is locked.")

option = input("Choose: create or login? ").strip().upper()

if option == "CREATE":
    creation()
elif option == "LOGIN":
    validation()
else:
    print("Incorrect option")
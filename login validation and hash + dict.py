import bcrypt

users = {
    "nikoloz": bcrypt.hashpw("nikaloz".encode(), bcrypt.gensalt())
}

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

    
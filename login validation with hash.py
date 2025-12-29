import bcrypt

name = input("Username: ")
password = input("Password: ").encode()

saved_username = "nikoloz"
saved_password = bcrypt.hashpw(b"nikaloz", bcrypt.gensalt())

if name != saved_username:
    print("Username is incorrect!")
elif not bcrypt.checkpw(password, saved_password):
    print("Password is incorrect!")
else:
    print("Username and Password is correct!")
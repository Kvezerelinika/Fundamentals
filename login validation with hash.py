import bcrypt

name = input("Username: ")
password = input("Password: ").encode()

s = bcrypt.gensalt()

saved_username = "nikoloz"
saved_password = bcrypt.hashpw("nikaloz".encode(), s)


if name == saved_username and bcrypt.checkpw(password, saved_password):
    print("Username and Password is correct!")
elif name != saved_username:
    print("Username is incorrect!")
else:
    print("Password is incorrect!")
    
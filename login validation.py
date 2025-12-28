name = input("Username: ")
password = input("Password: ")

saved_username = "nikoloz"
saved_password = "nikaloz"

if name == saved_username and password == saved_password:
    print("Username and Password is correct!")
elif name != saved_username:
    print("Username is incorrect!")
elif password != saved_password:
    print("Password is incorrect!")
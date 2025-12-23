profile = {
    "Name": input("Name: "),
    "Surname": input("Surname: "),
    "Age": input("Age: "),
    "Email": input("Email: "),
    "Country": input("Country: "),
    "Employed": input("Employed: "),
}

print("\nUSER PROFILE")
for key, value in profile.items():
    print(f"{key}: {value}")
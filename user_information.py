while True:
    name = input("What's your name? ")
    if name.isalpha():
        print("Correct input")
        break
    else:
        print("Incorrect input")

while True:
    surname = input("What's your surname? ")
    if surname.isalpha():
        print("Correct input")
        break
    else:
        print("Incorrect input")

while True:
    cellphone = input("What's your cellphone? ")
    if cellphone.isdigit():
        print("Correct input")
        break
    else:
        print("Incorrect input")


email = input("What's your email? ")


while True:
    gender = input("What's your gender? (Male/Female/None) ")
    m = "male"
    f = "female"
    n = "none"
    if gender.lower() == m or gender.lower() == f or gender.lower() == n:
        print("Correct input")
        break
    else:
        print("Incorrect input")


employed = input("What's your employement status? (Yes/No) ")

print(f"Full Name: {name} {surname}")
print(f"Cellphone: {cellphone}")
print(f"Eail: {email}")
print(f"Gender: {gender}")
print(f"Employment Status: {employed}")
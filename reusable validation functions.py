import re

def is_valid_age(age):
    age = age.strip()
    if not age.isdigit():
        return False
    age = int(age)
    return 0 <= age <= 120

def is_valid_email(email):
    return(
        bool(re.fullmatch(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}', email))
    )

def is_positive_number(n):
    return n.isdigit() and int(n) > 0

age = input("Type age: ")
print(is_valid_age(age))

email = input("Type email: ")
print(is_valid_email(email))

positive_number = input("Type positive number: ")
print(is_positive_number(positive_number))





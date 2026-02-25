import re

def check_password(password):
    return (
        len(password) >= 8 and
        bool((re.search(r'[a-zA-Z]', password))) and
        bool((re.search(r'\d', password)))
        )
    
checker = input("Please type your password: ")
print(f"{check_password(checker)}")
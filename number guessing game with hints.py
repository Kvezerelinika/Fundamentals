import random

secret = random.randrange(1,1000)
attempt = 0
max_attempts = 10

while attempt < max_attempts:
    try: 
        users_answer = int(input(f"Guess the number? "))
    except ValueError:
        print("Please enter the number!")
        continue

    if users_answer == secret:
        print("You guess is right!")
        break
    else:
        attempt += 1
        print(f"Wrong! Only {max_attempts - attempt} attempt(s) left!")

        if users_answer < secret:
            print(f"The number is higher!")
        else:
            print(f"The number is lower!")
else:
    print(f"You lost. The number was {secret}!")
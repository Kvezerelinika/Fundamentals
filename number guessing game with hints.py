import random

number = random.randrange(1,1000)
attempt = 0
max_attempts = 10

while attempt < max_attempts:
    try: 
        answer = int(input(f"Guess the number? "))
    except ValueError:
        print("Please enter the number!")
        continue

    if answer == number:
        print("You guess is right!")
        break
    else:
        attempt += 1
        print(f"Wrong! Only {max_attempts - attempt} attempt(s) left!")
        if answer < number:
            print(f"{answer} is lower than your answer")
        else:
            print(f"{answer} is higher than your answer")
else:
    print(f"You lost. The number was {number}!")
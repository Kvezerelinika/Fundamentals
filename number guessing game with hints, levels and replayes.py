import random

def guess_the_number():
    print("Welcome to the game!")

    wins = 0
    play_again = True

    while play_again:
        print("\nChoose difficulty:")
        print("1 - Easy (1-100, 15 attempts)")
        print("2 - Medium (1-500, 12 attempts)")
        print("3 - Hard (1-1000, 10 attempts)")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            max_attempts = 15
            max_number = 100
        elif choice == "2":
            max_attempts = 12
            max_number = 500
        elif choice == "3":
            max_attempts = 10
            max_number = 1000
        else:
            print("Try number from 1 to 3!")
            break

        secret = random.randrange(1,max_number)
        attempt = 0

        print(f"\nI am thinking of number between 1 and {max_number}! Can you guess? You have {max_attempts} attempt(s)")

        while attempt < max_attempts:
            try: 
                users_answer = int(input(f"Guess the number? "))
            except ValueError:
                print("Please enter the number!")
                continue

            if users_answer == secret:
                print("You guess is right!")
                wins += 1
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

        again = input("\nDo you want to play again? (y/n) ").lower()
        if again != "y":
            play_again = False
            print(f"\nThanks for plating! You won {wins} time(s)!")

guess_the_number()
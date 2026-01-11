number = int(input("Please enter number to check: "))

if number <= 1:
    print("This number is not Prime!")
elif number > 4 and number % 2 == 0:
    print("This number is not Prime!")
else:
    is_prime = True
    n = 2

    while n <= number // 2:
        if number % n == 0:
            is_prime = False
            break
        n += 1

    if is_prime:
        print("The number is Prime!")
    else:
        print("This number is not Prime")
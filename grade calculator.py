try:
    grade = int(input("What is your grade from 0 - 100? (ex. 91) "))
except ValueError:
    print("Please enter a number")
    exit()

if grade < 0 or grade > 100:
    print("Incorrect grade!")
elif grade <= 50:
    print("F. You failed!")
elif grade <= 60:
    print("E. You barely survived!")
elif grade <= 70:
    print("D. You are asking for it!")
elif grade <= 80:
    print("C. You are alright!")
elif grade <= 90:
    print("B. You are Second best, sorry!")
else:
    print("A. You are winning in life!")
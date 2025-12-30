try:
    grades = {
        "math": int(input("What is your grade in math from 0 - 100? (ex. 91) ")),
        "biology": int(input("What is your grade in biology from 0 - 100? (ex. 91) ")),
        "chemistry": int(input("What is your grade in chemistry from 0 - 100? (ex. 91) ")),
        "literature": int(input("What is your grade in literature from 0 - 100? (ex. 91) ")),
        "philosophy": int(input("What is your grade in philosophy from 0 - 100? (ex. 91) ")),
    }
except ValueError:
    print("Please enter a number")
    exit()

for k, v in grades.items():
    if v < 0 or v > 100:
        print(f"Incorrect grade. {v} should be between 0 and 100!")
        exit()

total_ave = sum(grades.values()) / len(grades)
print(f"Your average grade is {total_ave}")

def to_gpa(score):
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0
    
gpa = sum(to_gpa(g) for g in grades.values()) / len(grades)
print(f"Your GPA is {gpa:.2f}")

if total_ave <= 50:
    print("F. You failed!")
elif total_ave <= 60:
    print("E. You barely survived!")
elif total_ave <= 70:
    print("D. You are asking for it!")
elif total_ave <= 80:
    print("C. You are alright!")
elif total_ave <= 90:
    print("B. You are Second best, sorry!")
else:
    print("A. You are winning in life!")
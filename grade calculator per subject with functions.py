def get_grades():
    try:
        return {
            "math": int(input("What is your grade in math from 0 - 100? (ex. 91) ")),
            "biology": int(input("What is your grade in biology from 0 - 100? (ex. 91) ")),
            "chemistry": int(input("What is your grade in chemistry from 0 - 100? (ex. 91) ")),
            "literature": int(input("What is your grade in literature from 0 - 100? (ex. 91) ")),
            "philosophy": int(input("What is your grade in philosophy from 0 - 100? (ex. 91) ")),
        }
    except ValueError:
        print("Please enter a number")
        return None

def validate_grades(grades):
    for k, v in grades.items():
        if v < 0 or v > 100:
            print(f"Incorrect grade for {k}. {v} should be between 0 and 100!")
            return False
    return True

def calculate_average(grades):
    return sum(grades.values()) / len(grades)

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
    
def calculate_gpa(grades):
    return sum(to_gpa(g) for g in grades.values()) / len(grades)

def letter_grade(total_ave):
    if total_ave <= 50:
        return "F. You failed!"
    elif total_ave <= 60:
        return "E. You barely survived!"
    elif total_ave <= 70:
        return "D. You are asking for it!"
    elif total_ave <= 80:
        return "C. You are alright!"
    elif total_ave <= 90:
        return "B. You are Second best, sorry!"
    else:
        return "A. You are winning in life!"

def main():
    grades = get_grades()
    if not grades:
        return
    
    if not validate_grades(grades):
        return
    
    average = calculate_average(grades)
    gpa = calculate_gpa(grades)
    final_letter = letter_grade(average)

    print(f"Your average grade is {average:.2f}")
    print(f"Your GPA is {gpa:.2f}")
    print(final_letter)
main()
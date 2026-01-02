import random

questions = {
  "Which number is even: 2 or 3? ": "2",
  "Which is bigger: 10 or 5? ": "10",
  "Which is a color: red or dog? ": "red",
  "Which is an animal: cat or table? ": "cat",
  "Which is a fruit: apple or chair? ": "apple",
  "Which can fly: bird or rock? ": "bird",
  "Which is hot: fire or ice? ": "fire",
  "Which is faster: car or snail? ": "car",
  "Which is used to write: pen or bread? ": "pen",
  "Which is alive: tree or stone? ": "tree",
}

def asking():
    attempt = len(questions)
    score = 0

    question_list = list(questions.items())
    random.shuffle(question_list)

    for question, answer in question_list:
        users_answer = input(question + " ").strip().lower()

        if users_answer == answer.lower():
            print("Your answer is correct")
            score += 1
        else:
            print("Your answer is incorrect")

    print(f"There is no more questions! Score is {score}/{attempt}")

asking()

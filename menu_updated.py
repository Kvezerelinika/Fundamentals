import json

FILE_NAME = "tasks.json"
tasks = []

def load_tasks():
    global tasks

    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def generate_id():
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def show_tasks():
    if not tasks:
        print("There is no tasks!")
        return
    
    for task in tasks:
        print(f"""
ID: {task["id"]},
Title: {task["title"]},
Task: {task["task"]},
Deadline: {task["deadline"]}
              """)

def add_task():
    title = input("Type title to add: ")
    task_desc = input("Type task to add: ")
    deadline = input("Type date to add: ")

    task = {
        "id": generate_id(),
        "title": title, 
        "task": task_desc, 
        "deadline": deadline
        }
    
    tasks.append(task)
    save_tasks()
    print("Your task has been added!")

def edit_task():
    if not tasks:
        print("There is no tasks!")
        return
    
    show_tasks()

    task_id = input("Input task ID to edit: ")
    if not task_id.isdigit():
        print("Invalid ID")
        return
    
    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            field = input("What do you want to update: (title/task/deadline) ").lower()

            if field in ("title", "task", "deadline"):
                task[field] = input("Enter new value: ")
                save_tasks()
                print("Task updated!")
                return
            else:
                print("Wrong input!")
                return
            
    print("Task not found!")

def remove_task():
    if not tasks:
        print("There is no tasks!")
        return
    
    show_tasks()
    
    task_id = input("Please enter task ID: ")
    if not task_id.isdigit():
        print("Invalid ID")
        return
    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            print("Task removed!")
            return
    print("Task not found")

def main():
    load_tasks()


    while True:
        print("""
1. Add task
2. Edit task
3. Remove task
4. View task
5. Exit
              """)

        choice = input("Make your choice: ").strip()
        if not choice.isdigit():
            print("Please type a digit!")
            continue
        choice = int(choice)

        if choice == 1:
            add_task()

        elif choice == 2:
            edit_task()
        elif choice == 3:
            remove_task()
        elif choice == 4:
            show_tasks()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Wrong number of input!")

main()
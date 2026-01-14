task = None

while True:
    print("1. Add task")
    print("2. Edit task")
    print("3. Remove task")
    print("4. View task")
    print("5. Exit")

    option = input("Make your choice: ").strip()
    if not option.isdigit():
        print("Please type a digit!")
        continue
    choice = int(option)

    if choice == 1:
        title = input("Type title to add: ")
        task_desc = input("Type task to add: ")
        deadline = input("Type date to add: ")
        task = { "title": title, "task": task_desc, "deadline": deadline}
        print("Your task has been added!")

    elif choice == 2:
        if not task:
            print("No task to edit!")
            continue

        field = input("What do you want to update: (title/task/deadline) ").lower()

        if field in task:
            task[field] = input("Enter new value: ")
            print("Task updated!")
        else:
            print("Wrong input!")
    elif choice == 3:
        task = None
        print("Your task has been removed")
    elif choice == 4:
        print(f"Title: {task["title"]}, Task: {task["task"]}, Deadline: {task["deadline"]}")
    elif choice == 5:
        print("Thank you for your time!")
        break
    else:
        print("Wrong number of input!")
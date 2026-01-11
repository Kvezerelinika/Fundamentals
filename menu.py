while True:
    print("1. Add task")
    print("2. Edit task")
    print("3. Remove task")
    print("4. Settings")
    print("5. Exit")

    option = int(input("Make your choice: ").strip())

    if option == 1:
        print("You can add task now!")
        title = input("Type title to add: ")
        task = input("Type task to add: ")
        deadline = input("Type date to add: ")
    elif option == 2:
        update = input("What you want to update: ")
        if update == "title":
            type = input("Please type the update: ")
            title == type
        elif update == "task":
            type = input("Please type the update: ")
            task == type
        elif update == "deadline":
            type = input("Please type the update: ")
            deadline == type
        else:
            print("Wrong input!")
    elif option == 3:
        print("Your task has been removed")
    elif option == 4:
        print("You can add number now!")
    elif option == 5:
        print("Thank you for your time!")
        break
    else:
        print("Wrong number of input!")
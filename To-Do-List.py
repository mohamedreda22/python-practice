print("Welcome to the To-Do List App")
print("Enter 'HELP' for help")
print("Enter 'SHOW' to show your To-Do List")
print("Enter 'DONE' to remove a task from your To-Do List")
print("Enter 'QUIT' to quit the app")
print("Enter 'ADD' to add your task to the To-Do List")
tasks = []
while True:
    command = input("Enter your command: ").upper()
    if command == "HELP":
        print("Enter 'SHOW' to show your To-Do List")
        print("Enter 'DONE' to remove a task from your To-Do List")
        print("Enter 'QUIT' to quit the app")
    elif command == "SHOW":
        for task in tasks:
            print(task)
    elif command == "DONE":
        task = input("Enter the task you want to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found!")
    elif command == "QUIT":
        break
    elif command == "":
        print("Please enter a valid command!")
    elif command in tasks:
        print("Task already exists!")
    elif command == "ADD":
        task = input("Enter the task you want to add: ")
        tasks.append(task)
    else:
        tasks.append(command)
print("To-Do List:")
for task in tasks:
    print(task)
print("End of the program!")
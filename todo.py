tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!\n")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

def complete_task():
    view_tasks()
    index = int(input("Enter task number to complete: "))
    if index < 1 or index > len(tasks):
        print("Invalid task number!\n")
    else:
        task = tasks.pop(index-1)
        print(f"{task} completed successfully!\n")

while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Quit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")
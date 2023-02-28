import os
from colorama import init, Fore, Style

# Initialize colorama for Windows support
init()

# Define the filename to store tasks
filename = "tasks.txt"

# Check if the file exists, if not create an empty file
if not os.path.isfile(filename):
    open(filename, 'a').close()

# Load tasks from file
with open(filename, 'r') as f:
    tasks = f.read().splitlines()

def save_tasks():
    # Save tasks to file
    with open(filename, 'w') as f:
        f.write('\n'.join(tasks))

def add_task():
    task = input(Fore.GREEN + "Enter task: " + Style.RESET_ALL)
    tasks.append(task)
    save_tasks()
    print(Fore.YELLOW + "Task added successfully!\n" + Style.RESET_ALL)

def view_tasks():
    if len(tasks) == 0:
        print(Fore.YELLOW + "No tasks found!\n" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Tasks:\n" + Style.RESET_ALL)
        for i, task in enumerate(tasks):
            print(Fore.YELLOW + f"{i+1}. {task}" + Style.RESET_ALL)
        print()

def complete_task():
    view_tasks()
    index = int(input(Fore.GREEN + "Enter task number to complete: " + Style.RESET_ALL))
    if index < 1 or index > len(tasks):
        print(Fore.RED + "Invalid task number!\n" + Style.RESET_ALL)
    else:
        task = tasks.pop(index-1)
        save_tasks()
        print(Fore.YELLOW + f"{task} completed successfully!\n" + Style.RESET_ALL)

while True:
    print(Fore.GREEN + "1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Quit" + Style.RESET_ALL)
    choice = int(input(Fore.GREEN + "Enter choice: " + Style.RESET_ALL))
    
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        print(Fore.GREEN + "Goodbye!\n" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Invalid choice!\n" + Style.RESET_ALL)
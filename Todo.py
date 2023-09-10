# Simple To-Do List in Python

# Function to display the menu
def show_menu():
    print("MENU:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

# Function to view tasks
def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks to display.")
            else:
                print("TASKS:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks to display. Add some tasks!")

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Task '{removed_task.strip()}' removed successfully!")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

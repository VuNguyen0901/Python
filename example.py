
# add task function
def add_task():
    task = input("Please input your new task:")
    with open("doc.txt","a") as file:
        file.write(task + "\n\r")
 #show menu function
def show_menu():
    print("Menu:")
    print("1. View Task")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_task():
    try:
        with open("doc.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("have no task")
            else:
                for i, getdata in enumerate(data,1):
                    print(f"{i}. {getdata.strip()}")

    except FileNotFoundError:
        print("No tasks to display. Add some tasks!")
def remove_task():
    view_task()
    try:
        number_task = int (input("Number of task remove:"))
        with open("doc.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= number_task <= len(tasks):
            remove_task = tasks.pop(number_task-1)
            with open("doc.txt", "w") as file:
                file.writelines(tasks)
            print(f"Remove task : {remove_task.strip()}")
        else:
            print("Invalid number of task")    
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

#add_task()
remove_task()
# with open("doc.txt", "a") as file:
#     file.write("good evening\n\r")

# print("example")
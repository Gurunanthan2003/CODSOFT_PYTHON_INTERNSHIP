tasks = []

def display_tasks():
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {'Done' if task['completed'] else 'Pending'}")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added!")

def update_task():
    display_tasks()
    task_number = int(input("Enter task number to update: ")) - 1
    tasks[task_number]["title"] = input("Enter new task title: ")
    print("Task updated!")

def delete_task():
    display_tasks()
    task_number = int(input("Enter task number to delete: ")) - 1
    del tasks[task_number]
    print("Task deleted!")

def mark_completed():
    display_tasks()
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    tasks[task_number]["completed"] = True
    print("Task marked as completed!")

while True:
    print("\nTo-Do List Menu:")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Quit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_completed()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please Give correct Choice")
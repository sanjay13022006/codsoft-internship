# To-Do List Program

# Initialize an empty list to store tasks
tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    task_number = int(input("\nEnter the task number to delete: "))
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' deleted!")
    except IndexError:
        print("Invalid task number!")

def main():
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
# Function to load saved tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [task.strip() for task in file.readlines()]

    except FileNotFoundError:
        return []


# Function to save tasks
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Load previous tasks
tasks = load_tasks()


# Main application
while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":

        task = input("Enter your task: ")

        tasks.append(task)

        save_tasks()

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")

            for i, task in enumerate(tasks, start=1):
                print(i, task)

    # Remove Task
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to remove.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

            number = int(input("Enter task number to remove: "))

            if 1 <= number <= len(tasks):

                tasks.pop(number - 1)

                save_tasks()

                print("Task removed successfully!")

            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":

        print("Thank you for using To-Do List!")

        break

    else:
        print("Invalid choice!")
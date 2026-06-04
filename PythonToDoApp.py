tasks = []
global tasks

# Function to display options
def display_menu():
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Quit")
    
# Function to add a task to the list 
def add_tasks():
    new_task = input("Enter a new task: ") #Prompt the user to enter a new task
    tasks.append(new_task) #Append the new task to the list
    print(f"Task '{new_task}' added to the list.")
    print(tasks)


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()
    try:
        choice = int(input("Enter task number to delete: "))
        removed = tasks.pop(choice - 1)
        print(f"Deleted '{removed}'.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("That task number does not exist.")


def run_app():
    print("Welcome to your To-Do List App!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

run_app()
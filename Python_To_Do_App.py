tasks = []

# Function to display options
def display_menu():
    """Display the menu options for the to-do list app."""
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Quit")

# Function to add a task to the list
def add_tasks():
    """Add a new task to the tasks list."""
    try:
        new_task = input("Enter a new task: ").strip()
        if not new_task:
            raise ValueError("Task cannot be empty.")
    except ValueError as e:
        print(f"⚠️ {e}")
    else:
        tasks.append(new_task)
        print(f"Task '{new_task}' added.")
    finally:
        print("-" * 30)  # always runs


def view_tasks():
    """Display all tasks in the to-do list."""
    try:
        if not tasks:
            raise IndexError("No tasks yet.")
    except IndexError as e:
        print(f"⚠️ {e}")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    finally:
        print("-" * 30)


def delete_task():
    """Delete a task from the to-do list."""
    try:
        if not tasks:
            raise IndexError("No tasks to delete.")
        view_tasks()
        choice = int(input("Enter task number to delete: "))
        if choice < 1 or choice > len(tasks):
            raise ValueError(f"Must be between 1 and {len(tasks)}.")
        removed = tasks.pop(choice - 1)
    except (ValueError, IndexError) as e:
        print(f"⚠️ {e}")
    else:
        print(f"Deleted '{removed}'.")
    finally:
        print("-" * 30)


def run_app():
    """Run the main to-do list application."""
    print("Welcome to your To-Do List App!")
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-4): ").strip()
            if choice not in ("1", "2", "3", "4"):
                raise ValueError(f"'{choice}' is not a valid option.")
        except ValueError as e:
            print(f"⚠️ {e} Please choose 1–4.")
            continue

        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break

run_app()

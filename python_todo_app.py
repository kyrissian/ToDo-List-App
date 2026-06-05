"""A simple command-line To-Do List application."""
# Simple To-Do List App in Python

tasks = []  # starts with an empty list of tasks

# Function to display options
def display_menu():
    """Display the menu options for the to-do list app."""
    print(f"\nYou have {len(tasks)} task(s).")
    print("\nPlease choose an option:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Edit a task")
    print("5. Quit")

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
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
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
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        choice = int(input("Enter task number to delete: "))
        if choice < 1 or choice > len(tasks):
            raise ValueError(f"Must be between 1 and {len(tasks)}.")
        confirm = input(f"Are you sure? Delete '{tasks[choice - 1]}'? (y/n): ").strip().lower()
        if confirm != "y":
            print("Deletion cancelled.")
            return  # exits the function cleanly, finally still runs
        removed = tasks.pop(choice - 1)
    except (ValueError, IndexError) as e:
        print(f"⚠️ {e}")
    else:
        print(f"Deleted '{removed}'.")
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    finally:
        print("-" * 30)

def edit_task():
    """Edit an existing task in the to-do list."""
    try:
        if not tasks:
            raise IndexError("No tasks to edit.")
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        choice = int(input("Enter task number to edit: "))
        if choice < 1 or choice > len(tasks):
            raise ValueError(f"Must be between 1 and {len(tasks)}.")
        new_text = input(f"New description for task {choice}: ").strip()
        if not new_text:
            raise ValueError("Task description cannot be empty.")
        old_task = tasks[choice - 1]
        tasks[choice - 1] = new_text
    except (ValueError, IndexError) as e:
        print(f"⚠️ {e}")
    else:
        print(f"Task updated: '{old_task}' → '{new_text}'")
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    finally:
        print("-" * 30)

def run_app():
    """Run the main to-do list application."""
    print("Welcome to your To-Do List App!")
    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-5): ").strip()
            if choice not in ("1", "2", "3", "4", "5"):
                raise ValueError(f"'{choice}' is not a valid option.")
        except ValueError as e:
            print(f"⚠️ {e} Please choose 1–5.")
            continue

        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            edit_task()
        elif choice == "5":
            print("Goodbye!")
            break

run_app()

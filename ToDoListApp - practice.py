# todo_app.py
# -----------
# A command-line To-Do List Application built for the SE Foundations Module Project.
# Demonstrates: functions, lists, control structures, input validation, and error handling.
# """

# CREATE AN EMPTY LIST TO HOLD TASKS
tasks = []
# ONCE THE USER ADDS TASKS, THEY WILL BE APPENDED TO THIS LIST AND WILL BE PRINTED
print(tasks)


# PROMPT USER TO ADD A TASK
new_task = input("What would you like to add to your to-do list? ")

# ADD THE NEW TASK TO THE LIST
tasks.append(new_task)



print(tasks)


# DELETING A TASK
tasks = []

def initialize_list():
    """Initialize the task list with sample tasks."""
    global tasks
    tasks = ["Buy groceries", "Call mom", "Finish project"]
    print("Initial tasks: " + str(tasks))


# # METHOD 1: remove() - removes the first occurrence of a value
# print("\nMETHOD 1:")
# initialize_list()
# tasks.remove("Call mom")  # This will remove the task "Call mom"
# print("CURRENT TASKS: " + str(tasks))


# # METHOD 2: pop() - removes an item by index and returns it
# print("\nMETHOD 2:")
# initialize_list()
# removed_task = tasks.pop(1)  # This will remove the task at index 1 ("Call mom")
# print(f"Removed task: {removed_task}")
# print("CURRENT TASKS: " + str(tasks))


# # METHOD 3: del statement - removes an item by index without returning it
# print("\nMETHOD 3:")
# initialize_list()
# del tasks[1]  # This will remove the task at index 1 ("Call mom")
# print("CURRENT TASKS: " + str(tasks))


# # METHOD 4: BONUS METHOD (not recommended for this use case) - loop through the list, check if any element contains a particular substring, and use remove() to delete it
# print("\nMETHOD 4:")
# initialize_list()   
# for task in tasks:
#     if "Call" in task:  # Check if the substring "Call" is in the task
#         tasks.remove(task)  # This will remove the task that contains "Call"
#         break  # Exit the loop after removing the task


# METHOD 5 - THE BEST METHOD - deleting items by index using a while loop to avoid issues with modifying the list while iterating
print("\nMETHOD 5:")
tasks = ["Buy groceries", "Call mom", "Finish project", "Call dad"]

choice = int(input("Which task number would you like to delete?"))
choice = choice - 1  # Adjust for 0-based indexing
tasks.pop(choice)  # Remove the desired element from the list
print(tasks)



# LOOPING THROUGH A LIST
# METHOD 1: 
print("\nLOOPING METHOD 1:")
for task in tasks:
    print(task)
    
# METHOD 2:
print("\nLOOPING METHOD 2:")
for i in range(len(tasks)):
    print(tasks[i])  # Print using index access
    
# METHOD 3:    
print("\nLOOPING METHOD 3:")
for i in range(len(tasks)):
    print(f"{i+1}. {tasks[i]}")  # Print with a numbered index (1-based)
    
# METHOD 4:
print("\nLOOPING METHOD 4:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")  # Print with a numbered index (1-based)


















# def print_banner():
#     """Print the welcome banner shown once at startup."""
#     print("\n" + "=" * 45)
#     print("       ✅  MY TO-DO LIST APP  ✅")
#     print("=" * 45)

# def print_menu():
#     """Display the main menu options to the user."""
#     print("\n┌─────────────────────────┐")
#     print("│        MAIN MENU        │")
#     print("├─────────────────────────┤")
#     print("│  1. Add a task          │")
#     print("│  2. View all tasks      │")
#     print("│  3. Delete a task       │")
#     print("│  4. Quit                │")
#     print("└─────────────────────────┘")
    
#     # ─────────────────────────────────────────────
# # CORE FEATURES
# # ─────────────────────────────────────────────
 
# def add_task():
#     """
#     Prompt the user to enter a new task and append it to the tasks list.
#     Uses try/except/else/finally to handle unexpected errors and always
#     give the user feedback.
#     """
#     print("\n── ADD A TASK ──")
#     try:
#         task = input("Enter the task description: ").strip()
#         # Validate: don't allow blank tasks
#         if not task:
#             raise ValueError("Task description cannot be empty.")
#     except ValueError as e:
#         print(f"⚠️  Invalid input: {e}")
#     else:
#         # Only runs if NO exception was raised
#         tasks.append(task)
#         print(f"✅ Task added: \"{task}\"")
#     finally:
#         # Always runs — good place for cleanup or a separator
#         print("────────────────────────")
        
        
        
# def view_tasks():
#     """
#     Display all current tasks with numbered indices.
#     Uses try/except/else/finally:
#       - Raises an exception if the list is empty
#       - else block prints the tasks if all is well
#     """
#     print("\n── YOUR TASKS ──")
#     try:
#         if not tasks:
#             raise IndexError("No tasks found. Your list is empty!")
#     except IndexError as e:
#         print(f"⚠️  {e}")
#     else:
#         # Only runs when tasks list has items
#         for i, task in enumerate(tasks, start=1):
#             print(f"  {i}. {task}")
#     finally:
#         print("────────────────────────"
              
              
# def delete_task():
#     """
#     Show the task list, ask the user for a task number, and remove that task.
#     Handles:
#       - Empty list (nothing to delete)
#       - Non-numeric input
#       - Out-of-range task numbers
#     Uses try/except/else/finally throughout.
#     """
#     print("\n── DELETE A TASK ──")
#     try:
#         if not tasks:
#             raise IndexError("There are no tasks to delete.")
 
#         # Show the list so the user knows what numbers are valid
#         for i, task in enumerate(tasks, start=1):
#             print(f"  {i}. {task}")
 
#         # int() will raise ValueError if the user types a non-number
#         task_num = int(input("Enter the task number to delete: ").strip())
 
#         # Check the range manually; raise a descriptive error if out of bounds
#         if task_num < 1 or task_num > len(tasks):
#             raise ValueError(f"Task number must be between 1 and {len(tasks)}.")
 
#     except IndexError as e:
#         print(f"⚠️  {e}")
#     except ValueError as e:
#         print(f"⚠️  Invalid input: {e}")
#     else:
#         # Only runs when no exception occurred — safe to delete
#         removed = tasks.pop(task_num - 1)   # list is 0-indexed, menu is 1-indexed
#         print(f"🗑️  Deleted task: \"{removed}\"")
#     finally:
#         print("────────────────────────")
        
        
        
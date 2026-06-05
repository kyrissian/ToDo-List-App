# ✅ Python To-Do List App

A simple, interactive command-line To-Do List application built in Python.
Created as a project for the SE Foundations Module at Coding Temple.

---

## What It Does

This app lets you manage a personal task list entirely from your terminal. You can:

- Add a new task
- View all current tasks
- Delete a task (with confirmation before removing)
- Edit an existing task in place
- Quit the application cleanly

---

## How to Run

Requirements: Python 3.x — no external libraries needed.


# 1. Clone the repository
git clone https://github.com/kyrissian/ToDo-List-App.git
cd todo-app

# 2. Run the app
python3 python_todo_app.py


On Windows you may need to use python instead of python3.

---

## How to Use

When you launch the app, you'll see how many tasks you have and a menu:


You have 0 task(s).

Please choose an option:
1. Add a task
2. View all tasks
3. Delete a task
4. Edit a task
5. Quit
Enter your choice (1-5):


Type a number and press Enter, then follow the on-screen prompts.

### Example Walkthrough


# Add a task
Enter a new task: Buy groceries
Task 'Buy groceries' added.

# Edit it
Enter task number to edit: 1
New description for task 1: Buy groceries and cook dinner
Task updated: 'Buy groceries' → 'Buy groceries and cook dinner'

# Delete it
Enter task number to delete: 1
Delete 'Buy groceries and cook dinner'? (y/n): y
Deleted 'Buy groceries and cook dinner'.


---

## Error Handling

The app handles all of the following gracefully — no crashes:


Blank task entered	⚠️ Task cannot be empty
Viewing with no tasks	⚠️ No tasks yet
Deleting from empty list	⚠️ No tasks to delete
Editing from empty list	⚠️ No tasks to edit
Task number out of range	⚠️ Must be between 1 and N
Non-number for task #	⚠️ Invalid input caught
Invalid menu option	⚠️ Please choose 1–5
Deletion cancelled (y/n)	Deletion cancelled, list unchanged



---

## Python Concepts Demonstrated


Lists	tasks = [] — central data store
Functions	add_tasks(), view_tasks(), delete_task(), edit_task(), run_app()
while loop	Main menu loop in run_app()
if/elif/else	Menu dispatch and input validation
try/except/else/finally	Every core function
input() + .strip()	Every user prompt
enumerate()	Numbered task display
Docstrings & comments	Throughout the file



---

## Project Structure


todo-app/
├── python_todo_app.py   # Main application
└── README.md            # This file


---

## Author

Built for the SE Foundations Module Project — Coding Temple, by Kathy Booth, with a little help from Claude. 

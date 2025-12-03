import json
import os

TODO_FILE = "todo.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour TODO list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added!")

def remove_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def TODO_MENU():
    tasks = load_tasks()
    while True:
        print("\nTODO List App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

TODO_MENU()
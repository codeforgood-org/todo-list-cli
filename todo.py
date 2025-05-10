import json
import os
import sys

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']}")

def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed['task']}")
    else:
        print("Invalid task number.")

def show_help():
    print("To-Do List Manager")
    print("Usage:")
    print("  python todo.py add 'Task description'")
    print("  python todo.py list")
    print("  python todo.py remove [task number]")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]
        if command == "add" and len(sys.argv) >= 3:
            add_task(" ".join(sys.argv[2:]))
        elif command == "list":
            list_tasks()
        elif command == "remove" and len(sys.argv) == 3:
            try:
                remove_task(int(sys.argv[2]))
            except ValueError:
                print("Please provide a valid task number.")
        else:
            show_help()

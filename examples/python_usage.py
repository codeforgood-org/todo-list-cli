#!/usr/bin/env python3
"""Example of using TodoList programmatically in Python."""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from todolist import TodoList


def main():
    """Demonstrate programmatic usage of TodoList."""

    # Create a TodoList instance
    print("=" * 50)
    print("Todo List CLI - Python Usage Example")
    print("=" * 50)
    print()

    # Use a separate file for this example
    todo = TodoList("example_tasks.json")

    # Add some tasks
    print("Adding tasks...")
    todo.add_task("Learn Python programming", priority="high")
    todo.add_task("Build a web application", priority="medium")
    todo.add_task("Read Python documentation", priority="low")
    todo.add_task("Write unit tests", priority="high")
    print()

    # List all tasks
    print("All tasks:")
    todo.list_tasks()
    print()

    # Complete some tasks
    print("Completing task #1...")
    todo.complete_task(1)
    print()

    # List pending tasks only
    print("Pending tasks only:")
    todo.list_tasks(status="pending")
    print()

    # List high priority tasks
    print("High priority tasks:")
    todo.list_tasks(priority="high")
    print()

    # Search for tasks
    print("Searching for 'Python':")
    todo.search_tasks("Python")
    print()

    # Add more tasks and complete them
    print("Adding and completing more tasks...")
    todo.add_task("Review code changes", priority="medium")
    todo.complete_task(2)
    print()

    # List completed tasks
    print("Completed tasks:")
    todo.list_tasks(status="completed")
    print()

    # Clear completed tasks
    print("Clearing completed tasks...")
    todo.clear_completed()
    print()

    # Final task list
    print("Final task list:")
    todo.list_tasks()
    print()

    print("=" * 50)
    print("Example complete!")
    print(f"Tasks saved to: {todo.tasks_file}")
    print("=" * 50)


if __name__ == "__main__":
    main()

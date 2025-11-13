"""Core functionality for the todo list manager."""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Literal


Priority = Literal["high", "medium", "low"]
Status = Literal["pending", "completed"]


class TodoList:
    """Manages a todo list with persistent JSON storage.

    Attributes:
        tasks_file: Path to the JSON file storing tasks
    """

    def __init__(self, tasks_file: str = "tasks.json"):
        """Initialize the TodoList with a storage file.

        Args:
            tasks_file: Path to the JSON file for storing tasks
        """
        self.tasks_file = tasks_file

    def load_tasks(self) -> List[Dict]:
        """Load tasks from the JSON file.

        Returns:
            List of task dictionaries. Returns empty list if file doesn't exist.
        """
        if not os.path.exists(self.tasks_file):
            return []
        try:
            with open(self.tasks_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
            return []

    def save_tasks(self, tasks: List[Dict]) -> None:
        """Save tasks to the JSON file.

        Args:
            tasks: List of task dictionaries to save
        """
        try:
            with open(self.tasks_file, "w") as f:
                json.dump(tasks, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def add_task(
        self,
        description: str,
        priority: Priority = "medium"
    ) -> None:
        """Add a new task to the list.

        Args:
            description: Task description
            priority: Task priority (high, medium, or low)
        """
        tasks = self.load_tasks()
        task = {
            "task": description,
            "status": "pending",
            "priority": priority,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        tasks.append(task)
        self.save_tasks(tasks)
        print(f"Added task: {description} [Priority: {priority}]")

    def list_tasks(
        self,
        status: Optional[Status] = None,
        priority: Optional[Priority] = None
    ) -> None:
        """List all tasks with optional filtering.

        Args:
            status: Filter by status (pending or completed)
            priority: Filter by priority (high, medium, or low)
        """
        tasks = self.load_tasks()

        if not tasks:
            print("No tasks found.")
            return

        # Apply filters
        if status:
            tasks = [t for t in tasks if t.get("status") == status]
        if priority:
            tasks = [t for t in tasks if t.get("priority") == priority]

        if not tasks:
            print("No tasks match the filter criteria.")
            return

        # Print tasks
        for i, task in enumerate(tasks, 1):
            status_icon = "✓" if task.get("status") == "completed" else "○"
            priority_str = task.get("priority", "medium").upper()
            priority_icon = {
                "HIGH": "!!!",
                "MEDIUM": "!!",
                "LOW": "!"
            }.get(priority_str, "!!")

            print(f"{i}. [{status_icon}] {task['task']}")
            print(f"   Priority: {priority_icon} {priority_str}")

            if task.get("completed_at"):
                print(f"   Completed: {task['completed_at']}")
            print()

    def remove_task(self, index: int) -> None:
        """Remove a task by its index.

        Args:
            index: 1-based index of the task to remove
        """
        tasks = self.load_tasks()
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            self.save_tasks(tasks)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")

    def complete_task(self, index: int) -> None:
        """Mark a task as completed.

        Args:
            index: 1-based index of the task to complete
        """
        tasks = self.load_tasks()
        if 1 <= index <= len(tasks):
            tasks[index - 1]["status"] = "completed"
            tasks[index - 1]["completed_at"] = datetime.now().isoformat()
            self.save_tasks(tasks)
            print(f"Completed task: {tasks[index - 1]['task']}")
        else:
            print("Invalid task number.")

    def search_tasks(self, query: str) -> None:
        """Search for tasks containing the query string.

        Args:
            query: Search query string
        """
        tasks = self.load_tasks()
        matching_tasks = [
            (i, task) for i, task in enumerate(tasks, 1)
            if query.lower() in task["task"].lower()
        ]

        if not matching_tasks:
            print(f"No tasks found matching '{query}'.")
            return

        print(f"Found {len(matching_tasks)} task(s) matching '{query}':\n")
        for i, task in matching_tasks:
            status_icon = "✓" if task.get("status") == "completed" else "○"
            print(f"{i}. [{status_icon}] {task['task']}")
            print(f"   Priority: {task.get('priority', 'medium').upper()}\n")

    def clear_completed(self) -> None:
        """Remove all completed tasks."""
        tasks = self.load_tasks()
        remaining = [t for t in tasks if t.get("status") != "completed"]
        removed_count = len(tasks) - len(remaining)

        if removed_count == 0:
            print("No completed tasks to clear.")
            return

        self.save_tasks(remaining)
        print(f"Cleared {removed_count} completed task(s).")

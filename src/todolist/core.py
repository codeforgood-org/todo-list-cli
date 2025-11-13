"""Core functionality for the todo list manager."""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional, Literal

from . import colors


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
        priority: Priority = "medium",
        tags: Optional[List[str]] = None,
        due_date: Optional[str] = None
    ) -> None:
        """Add a new task to the list.

        Args:
            description: Task description
            priority: Task priority (high, medium, or low)
            tags: Optional list of tags/categories
            due_date: Optional due date (ISO format or natural language)
        """
        tasks = self.load_tasks()
        task = {
            "task": description,
            "status": "pending",
            "priority": priority,
            "tags": tags or [],
            "due_date": due_date,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        tasks.append(task)
        self.save_tasks(tasks)

        msg = colors.success("✓ Added task: ") + f"{description} [{colors.color_priority(priority)}]"
        if tags:
            tag_str = ", ".join([colors.colorize(f"#{tag}", colors.Colors.CYAN) for tag in tags])
            msg += f" {tag_str}"
        if due_date:
            msg += colors.colorize(f" 📅 Due: {due_date}", colors.Colors.MAGENTA)
        print(msg)

    def list_tasks(
        self,
        status: Optional[Status] = None,
        priority: Optional[Priority] = None,
        tags: Optional[List[str]] = None
    ) -> None:
        """List all tasks with optional filtering.

        Args:
            status: Filter by status (pending or completed)
            priority: Filter by priority (high, medium, or low)
            tags: Filter by tags (tasks must have at least one matching tag)
        """
        tasks = self.load_tasks()

        if not tasks:
            print(colors.info("No tasks found."))
            return

        # Apply filters
        if status:
            tasks = [t for t in tasks if t.get("status") == status]
        if priority:
            tasks = [t for t in tasks if t.get("priority") == priority]
        if tags:
            tasks = [
                t for t in tasks
                if any(tag in t.get("tags", []) for tag in tags)
            ]

        if not tasks:
            print(colors.warning("No tasks match the filter criteria."))
            return

        # Print tasks
        for i, task in enumerate(tasks, 1):
            status_icon = colors.color_status(task.get("status", "pending"))
            task_text = task['task']

            # Dim completed tasks
            if task.get("status") == "completed":
                task_text = colors.dim(task_text)

            print(f"{i}. [{status_icon}] {task_text}")
            print(f"   Priority: {colors.color_priority(task.get('priority', 'medium'))}")

            # Show tags if present
            if task.get("tags"):
                tag_str = ", ".join([colors.colorize(f"#{tag}", colors.Colors.CYAN) for tag in task["tags"]])
                print(f"   Tags: {tag_str}")

            # Show due date if present
            if task.get("due_date"):
                due_str = colors.colorize(f"📅 Due: {task['due_date']}", colors.Colors.MAGENTA)
                print(f"   {due_str}")

            if task.get("completed_at"):
                completed_time = task['completed_at'].split('T')[0] if 'T' in task['completed_at'] else task['completed_at']
                print(colors.dim(f"   Completed: {completed_time}"))
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
            print(colors.success("✓ Removed task: ") + f"{removed['task']}")
        else:
            print(colors.error("✗ Invalid task number."))

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
            print(colors.success("✓ Completed task: ") + f"{tasks[index - 1]['task']}")
        else:
            print(colors.error("✗ Invalid task number."))

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
            print(colors.warning(f"No tasks found matching '{query}'."))
            return

        print(colors.info(f"Found {len(matching_tasks)} task(s) matching '{query}':\n"))
        for i, task in matching_tasks:
            status_icon = colors.color_status(task.get("status", "pending"))
            task_text = task['task']
            if task.get("status") == "completed":
                task_text = colors.dim(task_text)
            print(f"{i}. [{status_icon}] {task_text}")
            print(f"   Priority: {colors.color_priority(task.get('priority', 'medium'))}\n")

    def clear_completed(self) -> None:
        """Remove all completed tasks."""
        tasks = self.load_tasks()
        remaining = [t for t in tasks if t.get("status") != "completed"]
        removed_count = len(tasks) - len(remaining)

        if removed_count == 0:
            print(colors.info("No completed tasks to clear."))
            return

        self.save_tasks(remaining)
        print(colors.success(f"✓ Cleared {removed_count} completed task(s)."))

    def list_tags(self) -> None:
        """List all unique tags with task counts."""
        tasks = self.load_tasks()

        if not tasks:
            print(colors.info("No tasks found."))
            return

        # Collect all tags with counts
        tag_counts: Dict[str, int] = {}
        for task in tasks:
            for tag in task.get("tags", []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        if not tag_counts:
            print(colors.info("No tags found."))
            return

        print(colors.info("Available tags:\n"))
        for tag, count in sorted(tag_counts.items()):
            tag_colored = colors.colorize(f"#{tag}", colors.Colors.CYAN, bold=True)
            print(f"  {tag_colored} ({count} task{'s' if count != 1 else ''})")

    def get_statistics(self) -> None:
        """Display statistics about tasks."""
        tasks = self.load_tasks()

        if not tasks:
            print(colors.info("No tasks found."))
            return

        # Calculate statistics
        total = len(tasks)
        completed = len([t for t in tasks if t.get("status") == "completed"])
        pending = total - completed

        # Priority breakdown
        high_priority = len([t for t in tasks if t.get("priority") == "high" and t.get("status") == "pending"])
        medium_priority = len([t for t in tasks if t.get("priority") == "medium" and t.get("status") == "pending"])
        low_priority = len([t for t in tasks if t.get("priority") == "low" and t.get("status") == "pending"])

        # Completion percentage
        completion_pct = (completed / total * 100) if total > 0 else 0

        # Display statistics
        print(colors.colorize("=" * 50, colors.Colors.BLUE))
        print(colors.colorize("  Task Statistics", colors.Colors.BLUE, bold=True))
        print(colors.colorize("=" * 50, colors.Colors.BLUE))
        print()

        print(f"  Total tasks: {colors.colorize(str(total), colors.Colors.WHITE, bold=True)}")
        print(f"  Completed:   {colors.colorize(str(completed), colors.Colors.GREEN, bold=True)} ({completion_pct:.1f}%)")
        print(f"  Pending:     {colors.colorize(str(pending), colors.Colors.YELLOW, bold=True)}")
        print()

        print("  Pending by priority:")
        print(f"    {colors.color_priority('high')}: {high_priority}")
        print(f"    {colors.color_priority('medium')}: {medium_priority}")
        print(f"    {colors.color_priority('low')}: {low_priority}")
        print()

        # Tags statistics
        tag_counts: Dict[str, int] = {}
        for task in tasks:
            for tag in task.get("tags", []):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1

        if tag_counts:
            print(f"  Total tags: {len(tag_counts)}")
            top_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            print("  Top tags:")
            for tag, count in top_tags:
                tag_colored = colors.colorize(f"#{tag}", colors.Colors.CYAN)
                print(f"    {tag_colored}: {count}")
        print()

        print(colors.colorize("=" * 50, colors.Colors.BLUE))

    def export_tasks(self, format: str = "json", output_file: Optional[str] = None) -> None:
        """Export tasks to various formats.

        Args:
            format: Export format (json, csv, or markdown)
            output_file: Output file path (defaults to tasks.[format])
        """
        tasks = self.load_tasks()

        if not tasks:
            print(colors.warning("No tasks to export."))
            return

        if output_file is None:
            output_file = f"tasks_export.{format}"

        try:
            if format == "json":
                with open(output_file, "w") as f:
                    json.dump(tasks, f, indent=4)

            elif format == "csv":
                import csv
                with open(output_file, "w", newline="") as f:
                    fieldnames = ["task", "status", "priority", "tags", "due_date", "created_at", "completed_at"]
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    for task in tasks:
                        task_copy = task.copy()
                        task_copy["tags"] = ",".join(task.get("tags", []))
                        writer.writerow(task_copy)

            elif format == "markdown":
                with open(output_file, "w") as f:
                    f.write("# Todo List\n\n")

                    # Pending tasks
                    pending_tasks = [t for t in tasks if t.get("status") == "pending"]
                    if pending_tasks:
                        f.write("## Pending Tasks\n\n")
                        for task in pending_tasks:
                            priority = task.get("priority", "medium").upper()
                            tags_str = " ".join([f"`#{tag}`" for tag in task.get("tags", [])])
                            due = f" (Due: {task.get('due_date')})" if task.get("due_date") else ""
                            f.write(f"- [ ] **{task['task']}** [{priority}]{due}\n")
                            if tags_str:
                                f.write(f"  - Tags: {tags_str}\n")
                        f.write("\n")

                    # Completed tasks
                    completed_tasks = [t for t in tasks if t.get("status") == "completed"]
                    if completed_tasks:
                        f.write("## Completed Tasks\n\n")
                        for task in completed_tasks:
                            priority = task.get("priority", "medium").upper()
                            tags_str = " ".join([f"`#{tag}`" for tag in task.get("tags", [])])
                            f.write(f"- [x] ~~{task['task']}~~ [{priority}]\n")
                            if tags_str:
                                f.write(f"  - Tags: {tags_str}\n")

            print(colors.success(f"✓ Exported {len(tasks)} task(s) to {output_file}"))

        except Exception as e:
            print(colors.error(f"✗ Error exporting tasks: {e}"))

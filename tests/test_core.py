"""Unit tests for core TodoList functionality."""

import json
import os
import tempfile
import unittest
from datetime import datetime

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from todolist.core import TodoList


class TestTodoList(unittest.TestCase):
    """Test cases for TodoList class."""

    def setUp(self):
        """Set up test fixtures."""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.todo_list = TodoList(self.temp_file.name)

    def tearDown(self):
        """Clean up test fixtures."""
        # Remove the temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_add_task_default_priority(self):
        """Test adding a task with default priority."""
        self.todo_list.add_task("Test task")
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Test task")
        self.assertEqual(tasks[0]["priority"], "medium")
        self.assertEqual(tasks[0]["status"], "pending")
        self.assertIsNone(tasks[0]["completed_at"])
        self.assertIsNotNone(tasks[0]["created_at"])

    def test_add_task_high_priority(self):
        """Test adding a task with high priority."""
        self.todo_list.add_task("Urgent task", priority="high")
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["priority"], "high")

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.add_task("Task 3")
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 3)

    def test_remove_task(self):
        """Test removing a task."""
        self.todo_list.add_task("Task to remove")
        self.todo_list.add_task("Task to keep")

        self.todo_list.remove_task(1)
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Task to keep")

    def test_remove_invalid_index(self):
        """Test removing a task with invalid index."""
        self.todo_list.add_task("Test task")

        # Try to remove with invalid index (should not crash)
        self.todo_list.remove_task(10)
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)

    def test_complete_task(self):
        """Test completing a task."""
        self.todo_list.add_task("Task to complete")

        self.todo_list.complete_task(1)
        tasks = self.todo_list.load_tasks()

        self.assertEqual(tasks[0]["status"], "completed")
        self.assertIsNotNone(tasks[0]["completed_at"])

    def test_complete_invalid_index(self):
        """Test completing a task with invalid index."""
        self.todo_list.add_task("Test task")

        # Try to complete with invalid index (should not crash)
        self.todo_list.complete_task(10)
        tasks = self.todo_list.load_tasks()

        self.assertEqual(tasks[0]["status"], "pending")

    def test_clear_completed(self):
        """Test clearing completed tasks."""
        self.todo_list.add_task("Task 1")
        self.todo_list.add_task("Task 2")
        self.todo_list.add_task("Task 3")

        # Complete some tasks
        self.todo_list.complete_task(1)
        self.todo_list.complete_task(3)

        # Clear completed
        self.todo_list.clear_completed()
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Task 2")

    def test_clear_completed_none(self):
        """Test clearing completed tasks when there are none."""
        self.todo_list.add_task("Task 1")

        # Clear completed (should not remove pending tasks)
        self.todo_list.clear_completed()
        tasks = self.todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)

    def test_load_nonexistent_file(self):
        """Test loading tasks from a non-existent file."""
        # Create a TodoList with a non-existent file
        todo = TodoList("nonexistent_file.json")
        tasks = todo.load_tasks()

        self.assertEqual(tasks, [])

    def test_persistence(self):
        """Test that tasks persist across TodoList instances."""
        self.todo_list.add_task("Persistent task")

        # Create a new TodoList instance with the same file
        new_todo_list = TodoList(self.temp_file.name)
        tasks = new_todo_list.load_tasks()

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Persistent task")

    def test_task_structure(self):
        """Test that task has correct structure."""
        self.todo_list.add_task("Test task", priority="high")
        tasks = self.todo_list.load_tasks()
        task = tasks[0]

        # Check all required fields exist
        self.assertIn("task", task)
        self.assertIn("status", task)
        self.assertIn("priority", task)
        self.assertIn("created_at", task)
        self.assertIn("completed_at", task)

        # Check types
        self.assertIsInstance(task["task"], str)
        self.assertIsInstance(task["status"], str)
        self.assertIsInstance(task["priority"], str)
        self.assertIsInstance(task["created_at"], str)


class TestTodoListOutput(unittest.TestCase):
    """Test cases for TodoList output methods (list, search)."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.todo_list = TodoList(self.temp_file.name)

        # Add some test tasks
        self.todo_list.add_task("Buy groceries", priority="high")
        self.todo_list.add_task("Read book", priority="low")
        self.todo_list.add_task("Write code", priority="medium")
        self.todo_list.complete_task(2)  # Complete "Read book"

    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_list_all_tasks(self):
        """Test listing all tasks (should not crash)."""
        # This just tests that the method runs without errors
        # Output testing would require capturing stdout
        try:
            self.todo_list.list_tasks()
        except Exception as e:
            self.fail(f"list_tasks() raised {e}")

    def test_list_filtered_by_status(self):
        """Test listing tasks filtered by status."""
        try:
            self.todo_list.list_tasks(status="pending")
            self.todo_list.list_tasks(status="completed")
        except Exception as e:
            self.fail(f"list_tasks(status=...) raised {e}")

    def test_list_filtered_by_priority(self):
        """Test listing tasks filtered by priority."""
        try:
            self.todo_list.list_tasks(priority="high")
            self.todo_list.list_tasks(priority="low")
        except Exception as e:
            self.fail(f"list_tasks(priority=...) raised {e}")

    def test_search_tasks(self):
        """Test searching for tasks."""
        try:
            self.todo_list.search_tasks("book")
            self.todo_list.search_tasks("nonexistent")
        except Exception as e:
            self.fail(f"search_tasks() raised {e}")


if __name__ == "__main__":
    unittest.main()

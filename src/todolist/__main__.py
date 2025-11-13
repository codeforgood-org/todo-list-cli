"""CLI entry point for the todo list manager."""

import argparse
import sys
from typing import Optional

from .core import TodoList, Priority, Status


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple command-line todo list manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  todo add "Buy groceries"
  todo add "Urgent meeting" --priority high
  todo list
  todo list --status pending
  todo complete 1
  todo search "project"
  todo clear
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", nargs="+", help="Task description")
    add_parser.add_argument(
        "-p", "--priority",
        choices=["high", "medium", "low"],
        default="medium",
        help="Task priority (default: medium)"
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "-s", "--status",
        choices=["pending", "completed"],
        help="Filter by status"
    )
    list_parser.add_argument(
        "-p", "--priority",
        choices=["high", "medium", "low"],
        help="Filter by priority"
    )

    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a task")
    remove_parser.add_argument("index", type=int, help="Task number to remove")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("index", type=int, help="Task number to complete")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search for tasks")
    search_parser.add_argument("query", help="Search query")

    # Clear command
    subparsers.add_parser("clear", help="Clear all completed tasks")

    return parser


def main() -> None:
    """Main entry point for the CLI."""
    parser = create_parser()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    # Initialize todo list
    todo_list = TodoList()

    # Execute command
    try:
        if args.command == "add":
            description = " ".join(args.description)
            todo_list.add_task(description, args.priority)

        elif args.command == "list":
            todo_list.list_tasks(args.status, args.priority)

        elif args.command == "remove":
            todo_list.remove_task(args.index)

        elif args.command == "complete":
            todo_list.complete_task(args.index)

        elif args.command == "search":
            todo_list.search_tasks(args.query)

        elif args.command == "clear":
            todo_list.clear_completed()

        else:
            parser.print_help()

    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

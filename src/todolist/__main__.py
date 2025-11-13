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
        description="A powerful command-line todo list manager with colors, tags, and more",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  todo add "Buy groceries" --priority high --tags shopping,personal
  todo add "Team meeting" --due "2025-11-15"
  todo list
  todo list --status pending --priority high
  todo list --tags work
  todo complete 1
  todo search "project"
  todo stats
  todo tags
  todo export --format markdown
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
    add_parser.add_argument(
        "-t", "--tags",
        help="Comma-separated list of tags (e.g., work,urgent)"
    )
    add_parser.add_argument(
        "-d", "--due",
        help="Due date (e.g., 2025-11-15 or 'tomorrow')"
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
    list_parser.add_argument(
        "-t", "--tags",
        help="Filter by tags (comma-separated)"
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

    # Tags command
    subparsers.add_parser("tags", help="List all tags with task counts")

    # Stats command
    subparsers.add_parser("stats", help="Display task statistics")

    # Export command
    export_parser = subparsers.add_parser("export", help="Export tasks to file")
    export_parser.add_argument(
        "-f", "--format",
        choices=["json", "csv", "markdown"],
        default="json",
        help="Export format (default: json)"
    )
    export_parser.add_argument(
        "-o", "--output",
        help="Output file path"
    )

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
            tags = args.tags.split(",") if args.tags else None
            todo_list.add_task(description, args.priority, tags, args.due)

        elif args.command == "list":
            tags = args.tags.split(",") if args.tags else None
            todo_list.list_tasks(args.status, args.priority, tags)

        elif args.command == "remove":
            todo_list.remove_task(args.index)

        elif args.command == "complete":
            todo_list.complete_task(args.index)

        elif args.command == "search":
            todo_list.search_tasks(args.query)

        elif args.command == "clear":
            todo_list.clear_completed()

        elif args.command == "tags":
            todo_list.list_tags()

        elif args.command == "stats":
            todo_list.get_statistics()

        elif args.command == "export":
            todo_list.export_tasks(args.format, args.output)

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

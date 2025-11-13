# Todo List CLI

A simple, efficient command-line todo list manager built with Python. Track your tasks, set priorities, mark completion status, and stay organized from your terminal.

## Features

- Add, list, and remove tasks
- Set task priorities (high, medium, low)
- Mark tasks as complete/incomplete
- Search and filter tasks
- Lightweight JSON-based storage
- No external dependencies (pure Python)
- Cross-platform support

## Installation

### Option 1: Install with pip (recommended)

```bash
pip install -e .
```

This will install the `todo` command globally on your system.

### Option 2: Run directly

```bash
python todo.py [command] [arguments]
```

## Usage

### Basic Commands

#### Add a task
```bash
todo add "Buy groceries"
todo add "Complete project report" --priority high
```

#### List all tasks
```bash
todo list
```

#### List tasks by status
```bash
todo list --status pending
todo list --status completed
```

#### List tasks by priority
```bash
todo list --priority high
```

#### Complete a task
```bash
todo complete 1
```

#### Remove a task
```bash
todo remove 2
```

#### Search tasks
```bash
todo search "project"
```

### Advanced Usage

#### Add a task with priority
```bash
todo add "Urgent meeting" --priority high
todo add "Read documentation" --priority low
```

#### Mark multiple tasks as complete
```bash
todo complete 1 3 5
```

#### Clear all completed tasks
```bash
todo clear
```

## Data Storage

Tasks are stored in a `tasks.json` file in the current directory. The file is created automatically when you add your first task.

### Task Structure

Each task is stored as a JSON object with the following properties:
- `task`: Task description (string)
- `status`: Task status - "pending" or "completed" (string)
- `priority`: Task priority - "high", "medium", or "low" (string)
- `created_at`: Creation timestamp (ISO format)
- `completed_at`: Completion timestamp (ISO format, null if not completed)

Example:
```json
[
    {
        "task": "Buy groceries",
        "status": "pending",
        "priority": "medium",
        "created_at": "2025-11-13T10:30:00",
        "completed_at": null
    }
]
```

## Development

### Setting up development environment

1. Clone the repository:
```bash
git clone https://github.com/codeforgood-org/todo-list-cli.git
cd todo-list-cli
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install in development mode:
```bash
pip install -e .
```

### Running Tests

```bash
pytest tests/
```

Run tests with coverage:
```bash
pytest --cov=todolist tests/
```

### Code Quality

This project uses:
- Type hints for better code documentation
- Docstrings following Google style
- pytest for testing

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap

Future enhancements planned:
- [ ] Due dates and reminders
- [ ] Task categories/tags
- [ ] Recurring tasks
- [ ] Export to different formats (CSV, Markdown)
- [ ] Sync across devices
- [ ] Color-coded output
- [ ] Task notes/descriptions
- [ ] Undo/redo functionality

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Contribute to the documentation

## Acknowledgments

Built with Python and maintained by the Code for Good organization.

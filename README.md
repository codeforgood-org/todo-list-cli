# Todo List CLI ✓

> A powerful, colorful, and feature-rich command-line todo list manager built with Python.

[![CI](https://github.com/codeforgood-org/todo-list-cli/workflows/CI/badge.svg)](https://github.com/codeforgood-org/todo-list-cli/actions)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Track your tasks, set priorities, organize with tags, and stay productive from your terminal with beautiful colorized output!

## ✨ Features

### Core Functionality
- ✅ Add, list, complete, and remove tasks
- 🎯 Priority system (high, medium, low) with color-coded display
- 🏷️  Tags/categories for organizing tasks
- 📅 Due date tracking
- 🔍 Powerful search with filtering
- 📊 Statistics and analytics dashboard
- 💾 Lightweight JSON-based storage
- 🎨 Beautiful colorized terminal output
- 🚀 Fast and responsive
- 🐳 Docker support

### Advanced Features
- Export tasks to JSON, CSV, or Markdown
- Filter tasks by status, priority, or tags
- View task completion statistics
- List all tags with usage counts
- Shell completions for Bash and Zsh
- Cross-platform (Linux, macOS, Windows)
- No external dependencies for basic usage

## 🚀 Quick Start

### Installation

#### Option 1: Install with pip (Recommended)

```bash
git clone https://github.com/codeforgood-org/todo-list-cli.git
cd todo-list-cli
pip install -e .
```

#### Option 2: Run directly

```bash
python todo.py [command] [arguments]
```

#### Option 3: Docker

```bash
# Build the image
docker build -t todo-cli .

# Run with volume mount for persistent storage
docker run -v $(pwd)/data:/data todo-cli list

# Create alias for convenience
alias todo='docker run -v $(pwd)/data:/data todo-cli'
```

## 📖 Usage

### Adding Tasks

```bash
# Simple task
todo add "Buy groceries"

# With priority
todo add "Complete project report" --priority high

# With tags
todo add "Fix bug #123" --tags work,urgent

# With due date
todo add "Submit proposal" --due "2025-11-20"

# All together
todo add "Team presentation" --priority high --tags work,meeting --due "2025-11-15"
```

### Listing Tasks

```bash
# List all tasks
todo list

# List by status
todo list --status pending
todo list --status completed

# List by priority
todo list --priority high

# List by tags
todo list --tags work
todo list --tags personal,shopping

# Combine filters
todo list --status pending --priority high --tags work
```

### Managing Tasks

```bash
# Complete a task
todo complete 1

# Remove a task
todo remove 2

# Search tasks
todo search "project"

# Clear all completed tasks
todo clear
```

### Organization & Analytics

```bash
# List all tags
todo tags

# View statistics
todo stats

# Export tasks
todo export --format json
todo export --format csv --output tasks.csv
todo export --format markdown --output TODO.md
```

## 📊 Example Output

### Task List
```
1. [○] Complete project documentation
   Priority: !!! HIGH
   Tags: #work, #urgent
   📅 Due: 2025-11-15

2. [✓] Review pull requests
   Priority: !!  MEDIUM
   Tags: #work, #code-review
   Completed: 2025-11-13
```

### Statistics Dashboard
```
==================================================
  Task Statistics
==================================================

  Total tasks: 15
  Completed:   8 (53.3%)
  Pending:     7

  Pending by priority:
    !!! HIGH: 3
    !!  MEDIUM: 3
    !   LOW: 1

  Total tags: 5
  Top tags:
    #work: 8
    #personal: 4
    #urgent: 2

==================================================
```

## 🎨 Color Output

The CLI uses colors to make your tasks easier to scan:

- 🔴 **Red** - High priority tasks
- 🟡 **Yellow** - Medium priority tasks (and pending status)
- 🔵 **Blue** - Low priority tasks
- 🟢 **Green** - Completed tasks and success messages
- 🔷 **Cyan** - Tags
- 🟣 **Magenta** - Due dates

Colors can be disabled with the `NO_COLOR` environment variable.

## 🔧 Configuration

### Shell Completions

Enable tab completion for faster workflow:

#### Bash
```bash
# Copy completion script
sudo cp completions/todo-completion.bash /etc/bash_completion.d/todo
source /etc/bash_completion.d/todo
```

#### Zsh
```bash
# Copy completion script
mkdir -p ~/.zsh/completions
cp completions/todo-completion.zsh ~/.zsh/completions/_todo

# Add to ~/.zshrc
fpath=(~/.zsh/completions $fpath)
autoload -Uz compinit && compinit
```

See [completions/README.md](completions/README.md) for detailed instructions.

## 📦 Data Storage

Tasks are stored in `tasks.json` in the current directory. Each task contains:

```json
{
  "task": "Task description",
  "status": "pending",
  "priority": "medium",
  "tags": ["work", "important"],
  "due_date": "2025-11-20",
  "created_at": "2025-11-13T10:30:00",
  "completed_at": null
}
```

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/codeforgood-org/todo-list-cli.git
cd todo-list-cli

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=todolist --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py
```

### Code Quality

```bash
# Format code
black src/

# Lint code
flake8 src/

# Type checking
mypy src/todolist/ --ignore-missing-imports
```

## 📚 Documentation

- [CHANGELOG.md](CHANGELOG.md) - Version history and release notes
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contributing guidelines
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community standards
- [examples/](examples/) - Usage examples and integration patterns

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Quick contribution steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🗺️ Roadmap

Future enhancements planned:

- [ ] Recurring tasks
- [ ] Task reminders/notifications
- [ ] Natural language date parsing ("tomorrow", "next week")
- [ ] Task dependencies
- [ ] Cloud sync support
- [ ] Interactive TUI mode
- [ ] Task notes and descriptions
- [ ] Undo/redo functionality
- [ ] Task archiving
- [ ] Custom themes

## 🆘 Support

- 📫 [Open an issue](https://github.com/codeforgood-org/todo-list-cli/issues)
- 💬 [Start a discussion](https://github.com/codeforgood-org/todo-list-cli/discussions)
- 📖 [Read the docs](https://github.com/codeforgood-org/todo-list-cli#readme)

## 🙏 Acknowledgments

- Built with ❤️ by the Code for Good organization
- Inspired by the need for a simple, powerful CLI task manager
- Thanks to all contributors and users!

---

<p align="center">Made with ❤️ for productivity enthusiasts</p>

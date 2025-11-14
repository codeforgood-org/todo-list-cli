# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-13

### Added

#### Core Features
- Complete Python package reorganization with modular architecture
- Colorized terminal output with ANSI color support
- Priority system for tasks (high, medium, low) with colored indicators
- Task status tracking (pending, completed) with timestamps
- Tags/categories system for organizing tasks
- Due date support for tasks
- Search functionality with case-insensitive matching
- Filter tasks by status, priority, and tags
- Clear completed tasks command
- Statistics and analytics dashboard
- Export tasks to multiple formats (JSON, CSV, Markdown)

#### User Interface
- Enhanced CLI with argparse for better argument handling
- Color-coded task priorities (red for high, yellow for medium, blue for low)
- Status icons (✓ for completed, ○ for pending)
- Dimmed text for completed tasks
- Visual task count and completion percentage in stats
- Emoji support for due dates (📅) and status indicators

#### Developer Experience
- Comprehensive type hints throughout the codebase
- Detailed docstrings following Google style guide
- Modern Python packaging with pyproject.toml
- Full unit test suite with pytest (17+ test cases)
- GitHub Actions CI/CD pipeline
- Code coverage reporting
- Support for Python 3.8-3.12
- Black, Flake8, and MyPy integration

#### Documentation
- Comprehensive README with installation instructions
- CONTRIBUTING.md with development guidelines
- CODE_OF_CONDUCT.md for community standards
- Examples directory with Python and shell script usage examples
- Detailed inline code documentation
- Shell completion scripts for Bash and Zsh

#### Infrastructure
- Docker support with optimized multi-stage Dockerfile
- .dockerignore for efficient Docker builds
- GitHub issue templates (bug reports, feature requests)
- GitHub pull request template
- Automated testing across multiple OS (Linux, Windows, macOS)
- Automated linting and code quality checks

#### Command Line Interface
- `todo add` - Add tasks with priority, tags, and due dates
- `todo list` - List tasks with optional filtering
- `todo complete` - Mark tasks as completed
- `todo remove` - Remove tasks
- `todo search` - Search tasks by keyword
- `todo clear` - Clear all completed tasks
- `todo tags` - List all tags with usage counts
- `todo stats` - Display comprehensive task statistics
- `todo export` - Export tasks to various formats

### Changed
- Migrated from simple script to proper Python package structure
- Updated `todo.py` to serve as legacy entry point
- Enhanced error handling and user feedback
- Improved JSON storage format with additional metadata fields

### Fixed
- Better error messages for invalid operations
- Proper handling of edge cases in task operations
- Cross-platform compatibility improvements

## [0.1.0] - Initial Release

### Added
- Basic todo list functionality
- Add, list, and remove tasks
- Simple JSON-based storage
- Command-line interface
- MIT License

---

## Upgrade Guide

### From 0.x to 1.0

The 1.0 release includes significant enhancements while maintaining backwards compatibility for basic operations.

#### Task Data Format Changes

Tasks now include additional fields:
- `status`: "pending" or "completed"
- `priority`: "high", "medium", or "low"
- `tags`: Array of tag strings
- `due_date`: Optional due date string
- `completed_at`: ISO timestamp when task was completed

Old task files will continue to work, with default values applied:
- Missing `status` defaults to "pending"
- Missing `priority` defaults to "medium"
- Missing `tags` defaults to empty array

#### Installation Changes

**Old way:**
```bash
python todo.py add "Task"
```

**New way (recommended):**
```bash
pip install -e .
todo add "Task"
```

The old way still works for backwards compatibility.

#### New Features to Try

1. **Use priorities:**
   ```bash
   todo add "Urgent task" --priority high
   ```

2. **Organize with tags:**
   ```bash
   todo add "Work on project" --tags work,project
   ```

3. **Set due dates:**
   ```bash
   todo add "Submit report" --due "2025-11-20"
   ```

4. **View statistics:**
   ```bash
   todo stats
   ```

5. **Export your tasks:**
   ```bash
   todo export --format markdown -o tasks.md
   ```

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

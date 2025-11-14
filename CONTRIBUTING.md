# Contributing to Todo List CLI

Thank you for your interest in contributing to Todo List CLI! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version)
- Any relevant logs or error messages

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- A clear and descriptive title
- Detailed description of the proposed feature
- Use cases and benefits
- Any potential drawbacks or considerations

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our coding standards
3. **Add tests** for any new functionality
4. **Ensure all tests pass** by running `pytest`
5. **Update documentation** if needed
6. **Commit your changes** with clear, descriptive messages
7. **Push to your fork** and submit a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- git

### Setting Up Your Development Environment

1. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/todo-list-cli.git
cd todo-list-cli
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode with dev dependencies:
```bash
pip install -e ".[dev]"
```

### Running Tests

Run the test suite:
```bash
pytest tests/
```

Run tests with coverage:
```bash
pytest --cov=todolist tests/
```

### Code Style

We use several tools to maintain code quality:

- **Black** for code formatting:
```bash
black src/
```

- **Flake8** for linting:
```bash
flake8 src/
```

- **MyPy** for type checking:
```bash
mypy src/todolist/
```

Before submitting a PR, ensure your code passes all checks:
```bash
black src/
flake8 src/
mypy src/todolist/ --ignore-missing-imports
pytest tests/
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for function parameters and return values
- Maximum line length: 88 characters (Black default)
- Use descriptive variable and function names

### Documentation

- Add docstrings to all public functions, classes, and methods
- Follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) for docstrings
- Update README.md if you add new features
- Include examples in docstrings where appropriate

### Testing

- Write unit tests for all new functionality
- Maintain or improve code coverage
- Test edge cases and error conditions
- Use descriptive test names that explain what is being tested

### Commit Messages

Write clear, concise commit messages:

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Examples:
```
Add search functionality for tasks

- Implement case-insensitive search
- Add tests for search feature
- Update documentation

Fixes #123
```

## Project Structure

```
todo-list-cli/
├── src/
│   └── todolist/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       └── cli.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
├── LICENSE
├── pyproject.toml
└── todo.py
```

## Release Process

Releases are managed by project maintainers. Version numbers follow [Semantic Versioning](https://semver.org/):

- MAJOR version for incompatible API changes
- MINOR version for new functionality in a backwards compatible manner
- PATCH version for backwards compatible bug fixes

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion in the Issues section
- Reach out to project maintainers

Thank you for contributing to Todo List CLI!

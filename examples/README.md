# Todo List CLI Examples

This directory contains examples demonstrating various uses of the Todo List CLI.

## Basic Usage Examples

### Adding Tasks

```bash
# Add a simple task
todo add "Buy groceries"

# Add a task with high priority
todo add "Complete project report" --priority high

# Add a task with low priority
todo add "Read documentation" --priority low
```

### Listing Tasks

```bash
# List all tasks
todo list

# List only pending tasks
todo list --status pending

# List only completed tasks
todo list --status completed

# List high-priority tasks
todo list --priority high

# Combine filters
todo list --status pending --priority high
```

### Completing Tasks

```bash
# Mark task #1 as completed
todo complete 1

# Complete multiple tasks (requires running command multiple times)
todo complete 1
todo complete 2
todo complete 3
```

### Removing Tasks

```bash
# Remove task #2
todo remove 2
```

### Searching Tasks

```bash
# Search for tasks containing "project"
todo search "project"

# Search is case-insensitive
todo search "PROJECT"
todo search "Project"
```

### Clearing Completed Tasks

```bash
# Remove all completed tasks
todo clear
```

## Workflow Examples

### Daily Task Management

```bash
# Morning: Add today's tasks
todo add "Check emails" --priority high
todo add "Team standup meeting" --priority high
todo add "Code review" --priority medium
todo add "Update documentation" --priority low

# Throughout the day: Mark tasks as complete
todo complete 1
todo complete 2

# End of day: Review remaining tasks
todo list --status pending

# Clean up completed tasks
todo clear
```

### Project Management

```bash
# Add project tasks with priorities
todo add "Set up project repository" --priority high
todo add "Create project documentation" --priority high
todo add "Implement authentication" --priority high
todo add "Add unit tests" --priority medium
todo add "Setup CI/CD pipeline" --priority medium
todo add "Code cleanup" --priority low

# Track progress
todo list --priority high
todo list --status completed

# Find specific tasks
todo search "test"
```

### Personal Task Tracking

```bash
# Add various personal tasks
todo add "Buy birthday gift" --priority high
todo add "Call dentist" --priority medium
todo add "Read new book chapter" --priority low
todo add "Organize desk" --priority low

# List by priority to focus on important items
todo list --priority high
todo list --priority medium
```

## Integration Examples

### Shell Script Integration

Create a script `daily_tasks.sh`:

```bash
#!/bin/bash

echo "Adding daily tasks..."
todo add "Check emails" --priority high
todo add "Review pull requests" --priority high
todo add "Daily standup" --priority high
todo add "Update task tracker" --priority medium
todo add "Read tech articles" --priority low

echo "Today's tasks:"
todo list
```

Run it:
```bash
chmod +x daily_tasks.sh
./daily_tasks.sh
```

### Cron Job for Daily Task Reports

Add to your crontab:

```bash
# Daily task summary at 9 AM
0 9 * * * cd /path/to/todo-list-cli && python todo.py list

# Weekly cleanup of completed tasks on Sunday at midnight
0 0 * * 0 cd /path/to/todo-list-cli && python todo.py clear
```

### Python Script Integration

```python
from todolist import TodoList

# Create a todo list instance
todo = TodoList("my_tasks.json")

# Add tasks programmatically
todo.add_task("Automated task 1", priority="high")
todo.add_task("Automated task 2", priority="medium")

# List tasks
print("Current tasks:")
todo.list_tasks()

# Complete a task
todo.complete_task(1)

# Search tasks
todo.search_tasks("automated")

# Clear completed tasks
todo.clear_completed()
```

## Tips and Tricks

### Organize by Context

Use descriptive task names with context:
```bash
todo add "[Work] Finish quarterly report" --priority high
todo add "[Home] Fix leaking faucet" --priority medium
todo add "[Personal] Schedule dentist appointment" --priority low
```

Then search by context:
```bash
todo search "[Work]"
todo search "[Home]"
```

### Priority System

Develop a consistent priority system:
- **High**: Must be done today, urgent and important
- **Medium**: Should be done soon, important but not urgent
- **Low**: Nice to have, can wait

### Daily Review

Make it a habit to:
1. Start day: `todo list --status pending`
2. Add new tasks as they come up
3. Complete tasks: `todo complete [number]`
4. End of day: `todo clear`

### Backup Your Tasks

```bash
# Backup tasks
cp tasks.json tasks_backup_$(date +%Y%m%d).json

# Restore from backup
cp tasks_backup_20231113.json tasks.json
```

## Advanced Usage

### Multiple Task Lists

```bash
# Work tasks
python todo.py list  # Uses default tasks.json

# Personal tasks
TASKS_FILE=personal_tasks.json python todo.py list

# Project-specific tasks
cd project_directory
python /path/to/todo.py list  # Uses tasks.json in current directory
```

### Combine with Other Tools

```bash
# Count pending tasks
todo list --status pending | grep -c "○"

# Export to text file
todo list > my_tasks.txt

# Add multiple tasks from a file
while IFS= read -r task; do
    todo add "$task"
done < tasks_to_add.txt
```

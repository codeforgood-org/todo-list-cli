#!/bin/bash
# Example shell script demonstrating Todo List CLI integration

echo "=================================================="
echo "Todo List CLI - Shell Script Example"
echo "=================================================="
echo ""

# Navigate to the project directory
cd "$(dirname "$0")/.." || exit 1

echo "1. Adding daily tasks..."
echo "------------------------"
python todo.py add "Morning standup meeting" --priority high
python todo.py add "Code review for PR #123" --priority high
python todo.py add "Update documentation" --priority medium
python todo.py add "Refactor authentication module" --priority medium
python todo.py add "Read team updates" --priority low
echo ""

echo "2. Listing all tasks..."
echo "------------------------"
python todo.py list
echo ""

echo "3. Listing high priority tasks..."
echo "------------------------"
python todo.py list --priority high
echo ""

echo "4. Completing first two tasks..."
echo "------------------------"
python todo.py complete 1
python todo.py complete 2
echo ""

echo "5. Searching for 'update' tasks..."
echo "------------------------"
python todo.py search "update"
echo ""

echo "6. Listing pending tasks..."
echo "------------------------"
python todo.py list --status pending
echo ""

echo "7. Listing completed tasks..."
echo "------------------------"
python todo.py list --status completed
echo ""

echo "=================================================="
echo "Example complete!"
echo "=================================================="

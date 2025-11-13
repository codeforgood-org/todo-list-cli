# Shell Completions for Todo List CLI

This directory contains shell completion scripts for the `todo` command.

## Installation

### Bash

1. Copy the bash completion script to your completions directory:

```bash
# System-wide (requires sudo)
sudo cp completions/todo-completion.bash /etc/bash_completion.d/todo

# User-specific
mkdir -p ~/.bash_completion.d
cp completions/todo-completion.bash ~/.bash_completion.d/todo
```

2. Add to your `~/.bashrc` (if using user-specific):

```bash
if [ -f ~/.bash_completion.d/todo ]; then
    . ~/.bash_completion.d/todo
fi
```

3. Reload your shell or source the file:

```bash
source ~/.bashrc
```

### Zsh

1. Copy the zsh completion script to your completions directory:

```bash
# Create completions directory if it doesn't exist
mkdir -p ~/.zsh/completions

# Copy the completion file
cp completions/todo-completion.zsh ~/.zsh/completions/_todo
```

2. Add to your `~/.zshrc` (if not already present):

```bash
# Add custom completions directory
fpath=(~/.zsh/completions $fpath)

# Initialize completions
autoload -Uz compinit && compinit
```

3. Reload your shell or source the file:

```bash
source ~/.zshrc
```

## Usage

Once installed, you can use Tab completion with the `todo` command:

```bash
# Complete commands
todo <TAB>

# Complete priorities
todo add "My task" --priority <TAB>

# Complete statuses
todo list --status <TAB>

# Complete export formats
todo export --format <TAB>
```

## Features

The completion scripts provide:

- Command completion (add, list, remove, complete, etc.)
- Option completion (--priority, --status, --tags, etc.)
- Value completion for known options (priorities, statuses, formats)
- File path completion for export output files

## Troubleshooting

### Bash

If completions aren't working:

1. Check that bash-completion is installed:
```bash
apt-get install bash-completion  # Debian/Ubuntu
brew install bash-completion     # macOS
```

2. Verify the completion file is sourced:
```bash
complete -p todo
```

### Zsh

If completions aren't working:

1. Check that the completion system is initialized:
```bash
echo $fpath
```

2. Rebuild the completion cache:
```bash
rm -f ~/.zcompdump
compinit
```

3. Make sure the file is executable (not strictly necessary):
```bash
chmod +x ~/.zsh/completions/_todo
```

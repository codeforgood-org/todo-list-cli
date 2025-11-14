#!/usr/bin/env bash
# Bash completion script for todo-list-cli

_todo_completions() {
    local cur prev words cword
    _init_completion || return

    local commands="add list remove complete search clear tags stats export"
    local priorities="high medium low"
    local statuses="pending completed"
    local formats="json csv markdown"

    # Complete commands
    if [[ $cword -eq 1 ]]; then
        COMPREPLY=($(compgen -W "$commands" -- "$cur"))
        return
    fi

    # Command-specific completions
    case "${words[1]}" in
        add)
            case "$prev" in
                -p|--priority)
                    COMPREPLY=($(compgen -W "$priorities" -- "$cur"))
                    return
                    ;;
                -t|--tags|-d|--due)
                    return
                    ;;
            esac
            COMPREPLY=($(compgen -W "-p --priority -t --tags -d --due" -- "$cur"))
            ;;
        list)
            case "$prev" in
                -s|--status)
                    COMPREPLY=($(compgen -W "$statuses" -- "$cur"))
                    return
                    ;;
                -p|--priority)
                    COMPREPLY=($(compgen -W "$priorities" -- "$cur"))
                    return
                    ;;
                -t|--tags)
                    return
                    ;;
            esac
            COMPREPLY=($(compgen -W "-s --status -p --priority -t --tags" -- "$cur"))
            ;;
        export)
            case "$prev" in
                -f|--format)
                    COMPREPLY=($(compgen -W "$formats" -- "$cur"))
                    return
                    ;;
                -o|--output)
                    _filedir
                    return
                    ;;
            esac
            COMPREPLY=($(compgen -W "-f --format -o --output" -- "$cur"))
            ;;
        remove|complete)
            # Could potentially list task numbers here
            ;;
        search)
            ;;
        *)
            ;;
    esac
}

complete -F _todo_completions todo

#compdef todo

# Zsh completion script for todo-list-cli

_todo() {
    local curcontext="$curcontext" state line
    typeset -A opt_args

    local -a commands
    commands=(
        'add:Add a new task'
        'list:List tasks'
        'remove:Remove a task'
        'complete:Mark a task as completed'
        'search:Search for tasks'
        'clear:Clear all completed tasks'
        'tags:List all tags'
        'stats:Display task statistics'
        'export:Export tasks to file'
    )

    _arguments -C \
        '1: :->command' \
        '*:: :->args'

    case $state in
        command)
            _describe 'command' commands
            ;;
        args)
            case $words[1] in
                add)
                    _arguments \
                        '-p[Priority]:priority:(high medium low)' \
                        '--priority[Priority]:priority:(high medium low)' \
                        '-t[Tags]:tags:' \
                        '--tags[Tags]:tags:' \
                        '-d[Due date]:due date:' \
                        '--due[Due date]:due date:' \
                        '*:description:'
                    ;;
                list)
                    _arguments \
                        '-s[Status]:status:(pending completed)' \
                        '--status[Status]:status:(pending completed)' \
                        '-p[Priority]:priority:(high medium low)' \
                        '--priority[Priority]:priority:(high medium low)' \
                        '-t[Tags]:tags:' \
                        '--tags[Tags]:tags:'
                    ;;
                export)
                    _arguments \
                        '-f[Format]:format:(json csv markdown)' \
                        '--format[Format]:format:(json csv markdown)' \
                        '-o[Output file]:file:_files' \
                        '--output[Output file]:file:_files'
                    ;;
                remove|complete)
                    _arguments \
                        ':task number:'
                    ;;
                search)
                    _arguments \
                        ':query:'
                    ;;
            esac
            ;;
    esac
}

_todo "$@"

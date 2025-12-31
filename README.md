# TodoCLI

A clean, menu-driven Python CLI application for managing tasks with a high-contrast terminal interface.

## Features

- **Add Tasks** - Create new tasks with titles and optional descriptions
- **View Tasks** - Display all tasks with completion status indicators
- **Update Tasks** - Modify task titles and descriptions
- **Delete Tasks** - Remove tasks from the list with confirmation
- **Mark Complete/Incomplete** - Toggle task completion status
- **In-Memory Storage** - Tasks persist during application runtime
- **High-Contrast UI** - Professional ANSI color scheme for excellent readability

## Requirements

- Python 3.13 or higher
- No external dependencies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd todo_console
```

2. Run the application:
```bash
python src/main.py
```

## Usage

Launch the application and navigate using the numbered menu options:

```
MAIN MENU

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
0. Exit
```

### Adding Tasks

Select option 1 to create new tasks:
- Enter a task title (required)
- Optionally add a description
- Continue adding more tasks or return to menu

### Viewing Tasks

Select option 2 to see all tasks:
- Task ID (Cyan, bold)
- Completion status: `[X]` (Green) or `[ ]` (Yellow)
- Task title (Bright Yellow)
- Description (Dim Cyan)

### Updating Tasks

Select option 3 to modify existing tasks:
- View available tasks
- Enter task ID to update
- Modify title and/or description (press Enter to keep existing values)
- View updated task details

### Deleting Tasks

Select option 4 to remove tasks:
- View available tasks
- Enter task ID to delete
- Review task details
- Confirm deletion (y/n)

### Marking Complete/Incomplete

Select option 5 to change task status:
- View available tasks
- Choose: (c)omplete or (i)ncomplete
- Enter task ID
- Status updates immediately reflect in view

## Color Scheme

The application uses a professional, high-contrast ANSI color palette:

| Element | Color | ANSI Code |
|---------|--------|------------|
| Main Headers | Bold Cyan | `\033[1m\033[96m` |
| Section Headers | Bold Blue | `\033[1m\033[94m` |
| Success Messages | Bold Green | `\033[1m\033[92m` |
| Errors | Bold Red | `\033[1m\033[91m` |
| Warnings | Yellow | `\033[93m` |
| Menu Numbers | Bold Green | `\033[1m\033[92m` |
| Menu Labels | Magenta | `\033[95m` |
| Input Prompts | Bold Orange | `\033[1m\033[38;5;208m` |
| Task IDs | Bold Cyan | `\033[1m\033[96m` |
| Task Titles | Bright Yellow | `\033[93;1m` |
| Descriptions | Dim Cyan | `\033[96;2m` |
| Completed [X] | Bold Green | `\033[1m\033[92m` |
| Incomplete [ ] | Bold Yellow | `\033[1m\033[93m` |

## Architecture

```
src/
├── main.py        # Entry point, main menu, color utilities
├── add.py        # Task creation functionality
├── view.py       # Task display functionality
├── update.py     # Task modification functionality
├── delete.py     # Task deletion functionality
└── complete.py   # Task completion toggling
```

### Key Design Decisions

- **Frozen Dataclasses**: Task objects are immutable, requiring new instances for updates
- **Shared State**: All modules import `_tasks` list from `add.py` for consistency
- **Error Handling**: Clear, actionable error messages with proper validation
- **Modular Design**: Each feature is self-contained with standalone executable capability

## Development

### Running Individual Modules

Each module can be run independently for testing:

```bash
# Add tasks
python src/add.py

# View tasks
python src/view.py

# Update tasks
python src/update.py

# Delete tasks
python src/delete.py

# Mark complete/incomplete
python src/complete.py
```

### Project Structure

- `specs/` - Feature specifications and design documents
- `src/` - Source code
- `history/` - Prompt history and architectural decisions
- `test_*.py` - Unit tests for individual features

## Notes

- **In-Memory Storage**: Tasks are lost when the application exits
- **Single-User**: Designed for single-user sessions
- **Terminal-Based**: Requires an ANSI color-compatible terminal

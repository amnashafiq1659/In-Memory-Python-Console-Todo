# TodoCLI

A clean, menu-driven Python CLI application for managing tasks with a high-contrast terminal interface.

## Features

- **Add Tasks** - Create new tasks with titles, descriptions, priorities, categories, and due dates
- **View Tasks** - Display all tasks with completion status, priority, category, and due date indicators
- **Update Tasks** - Modify task titles, descriptions, priorities, categories, and due dates
- **Delete Tasks** - Remove tasks from the list with confirmation
- **Mark Complete/Incomplete** - Toggle task completion status
- **Search & Filter Tasks** - Find tasks by keyword, status, priority, or category
- **Sort Tasks** - Organize tasks by title, priority, or due date
- **Priority Number Mapping** - Enter priorities as numbers (1=High, 2=Medium, 3=Low) or text
- **In-Memory Storage** - Tasks persist during application runtime
- **High-Contrast UI** - Professional ANSI color scheme for excellent readability

## Requirements

- Python 3.13 or higher
- No external dependencies

## Installation

1. Clone repository:
```bash
git clone <repository-url>
cd todo_console
```

2. Run application:
```bash
python src/main.py
```

## Usage

Launch the application and navigate using numbered menu options:

```
MAIN MENU

1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Search / Filter Tasks
7. Sort Tasks
0. Exit
```

### Adding Tasks

Select option 1 to create new tasks:
- Enter a task title (required)
- Optionally add a description
- Set priority (1=High, 2=Medium, 3=Low) - can use numbers or text
- Set category (default: General)
- Set due date (optional, format: YYYY-MM-DD)
- Continue adding more tasks or return to menu

**Priority Options:**
- `1` or `high` → High
- `2` or `medium`/`med` → Medium
- `3` or `low` → Low
- Press Enter → Medium (default)

### Viewing Tasks

Select option 2 to see all tasks:
- Task ID (Cyan, bold)
- Completion status: `[X]` (Green) or `[ ]` (Yellow)
- Task title (Bright Yellow)
- Description (Dim Cyan)
- Priority (color-coded: Red=High, Orange=Medium, Blue=Low)
- Category (Pink)
- Due date (Purple, if present)

### Updating Tasks

Select option 3 to modify existing tasks:
- View available tasks
- Enter task ID to update
- Modify title, description, priority, category, and/or due date
- Press Enter to keep existing values
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

### Searching & Filtering Tasks

Select option 6 to find specific tasks:
- Enter keyword (optional) - matches title or description
- Filter by status: complete/incomplete (optional)
- Filter by priority: High/Medium/Low (optional)
- Filter by category (optional)
- All filters use AND logic (task must match all criteria)
- Results display with task count

### Sorting Tasks

Select option 7 to organize tasks:
- Choose sort option:
  1. Sort by Title (A-Z, case-insensitive)
  2. Sort by Priority (High → Medium → Low)
  3. Sort by Due Date (earliest → latest)
- Tasks without due dates appear last when sorting by date
- Original task order is preserved for identical values (stable sort)

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
| High Priority | Bold Red | `\033[1m\033[91m` |
| Medium Priority | Bold Orange | `\033[1m\033[38;5;208m` |
| Low Priority | Bold Blue | `\033[1m\033[94m` |
| Categories | Pink | `\033[38;5;206m` |
| Due Dates | Purple | `\033[38;5;141m` |

## Architecture

```
src/
├── main.py        # Entry point, main menu, color utilities
├── add.py        # Task creation functionality, priority mapping
├── view.py       # Task display functionality
├── update.py     # Task modification functionality
├── delete.py     # Task deletion functionality
├── complete.py   # Task completion toggling
├── search.py      # Search and filter tasks functionality
└── sort_tasks.py # Sort tasks functionality
```

### Key Design Decisions

- **Frozen Dataclasses**: Task objects are immutable, requiring new instances for updates
- **Shared State**: All modules import `_tasks` list from `add.py` for consistency
- **Priority Mapping**: Supports both numeric (1, 2, 3) and text inputs for flexibility
- **Error Handling**: Clear, actionable error messages with proper validation
- **Modular Design**: Each feature is self-contained with standalone executable capability
- **Color Consistency**: All modules use the same color coding for visual consistency
- **Stable Sorting**: Sort operations preserve original order for identical values

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

# Search and filter tasks
python src/search.py

# Sort tasks
python src/sort_tasks.py

# Run full application
python src/main.py
```

### Project Structure

- `specs/` - Feature specifications and design documents
  - `007-sort-tasks/` - Sort tasks feature
  - `006-search-filter-tasks/` - Search and filter feature
- `src/` - Source code
- `history/` - Prompt history and architectural decisions
  - `prompts/` - Prompt History Records (PHRs)
  - `adr/` - Architectural Decision Records
- `.specify/` - SpecKit Plus templates and scripts

## Notes

- **In-Memory Storage**: Tasks are lost when the application exits
- **Single-User**: Designed for single-user sessions
- **Terminal-Based**: Requires an ANSI color-compatible terminal
<<<<<<< HEAD
- **Priority Flexibility**: Accepts both numeric (1, 2, 3) and text (High, Medium, Low) inputs
- **Search Performance**: All search and sort operations complete in under 1 second for typical task lists

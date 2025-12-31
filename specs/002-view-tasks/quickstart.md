# Quickstart Guide: View Tasks & Status Indication

**Feature**: 002-view-tasks
**Purpose**: Get up and running with the task viewing functionality quickly

## Overview

This feature provides functionality to view all tasks currently stored in memory. Each task displays its unique ID, title, description, and completion status with clear visual indicators.

## Prerequisites

- Python 3.9 or higher installed
- Basic familiarity with running Python scripts from command line
- Tasks must be added using Spec 001 functionality (add task)

## Installation

No installation required. This feature uses only Python standard library.

## Quick Start

### 1. Understand the Task Model

The Task dataclass is shared with Spec 001 and defined in `src/add.py`:

```python
@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    completed: bool
```

### 2. View All Tasks (Core Function)

```python
from src.add import _tasks
from src.add import Task

def get_all_tasks() -> list[Task]:
    """Retrieve all tasks from in-memory storage."""
    return _tasks  # Returns list of Task objects
```

### 3. Display Tasks (Console UI)

```python
def run_view_tasks_ui() -> None:
    """Display all tasks with status indicators."""
    tasks = get_all_tasks()

    if not tasks:
        print("No tasks found. Add tasks using add task functionality.")
        return

    print("=== Tasks ===")
    print()

    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"{task.id} | {status} | {task.title} | {task.description}")

    print()
    print(f"Total: {len(tasks)} tasks")
```

### 4. Main Entry Point

```python
if __name__ == "__main__":
    print("=== Task Viewer ===")
    run_view_tasks_ui()
    print("\nGoodbye!")
```

## Complete Implementation (view.py)

```python
from src.add import _tasks, Task

def get_all_tasks() -> list[Task]:
    """
    Retrieve all tasks from in-memory storage.

    Returns:
        list[Task]: List of all tasks currently stored. Returns empty list if no tasks exist.
    """
    return _tasks

def run_view_tasks_ui() -> None:
    """
    Display all tasks in a user-friendly console format.

    Shows task ID, title, description, and completion status
    with visual indicators for completed vs incomplete tasks.

    Returns:
        None
    """
    tasks = get_all_tasks()

    if not tasks:
        print("No tasks found. Add tasks using add task functionality.")
        return

    print("=== Tasks ===")
    print()

    for task in tasks:
        status = "[X]" if task.completed else "[ ]"
        print(f"{task.id} | {status} | {task.title} | {task.description}")

    print()
    print(f"Total: {len(tasks)} tasks")

if __name__ == "__main__":
    print("=== Task Viewer ===")
    run_view_tasks_ui()
    print("\nGoodbye!")
```

## Running the Program

### From Command Line

```bash
python src/view.py
```

### Example Session (Tasks Present)

```
=== Task Viewer ===
=== Tasks ===

1 | [ ] | Buy groceries | Milk, bread, eggs
2 | [X] | Call doctor | Annual checkup
3 | [ ] | Learn Python | Basics and advanced topics

Total: 3 tasks

Goodbye!
```

### Example Session (No Tasks)

```
=== Task Viewer ===
=== Tasks ===

No tasks found. Add tasks using add task functionality.

Goodbye!
```

## Key Concepts

### Status Indicators

Every task has a visual completion indicator:
- **[X]**: Task is completed
- **[ ]**: Task is incomplete/pending

### Display Format

Tasks are displayed in a single line format:
```
ID | [status] | Title | Description
```

This format is:
- Easy to scan visually
- Handles long content by terminal line wrapping
- Shows all task information at once

### Read-Only Access

The view functionality does not:
- Add tasks (handled by Spec 001)
- Modify tasks (future feature)
- Delete tasks (future feature)
- Toggle completion status (future feature)

It only reads from the in-memory `_tasks` list.

## Common Use Cases

### View Tasks Programmatically

```python
from src.view import get_all_tasks

tasks = get_all_tasks()

for task in tasks:
    print(f"Task {task.id}: {task.title}")
    if task.completed:
        print("  Status: Completed")
    else:
        print("  Status: Pending")
```

### Count Tasks by Status

```python
from src.view import get_all_tasks

tasks = get_all_tasks()
completed = sum(1 for t in tasks if t.completed)
incomplete = len(tasks) - completed

print(f"Completed: {completed}")
print(f"Pending: {incomplete}")
print(f"Total: {len(tasks)}")
```

### Find Specific Task by ID

```python
from src.view import get_all_tasks

tasks = get_all_tasks()
task_id = 2

task = next((t for t in tasks if t.id == task_id), None)

if task:
    print(f"Found: {task.title}")
else:
    print(f"Task {task_id} not found")
```

## Integration with Spec 001

The view functionality integrates seamlessly with Spec 001 (Add Task):

1. **Add tasks** using `src/add.py`:
   ```bash
   python src/add.py
   ```

2. **View tasks** using `src/view.py`:
   ```bash
   python src/view.py
   ```

3. Both share the same:
   - Task dataclass
   - In-memory storage (`_tasks` list)
   - Task data

## Testing Your Implementation

### Test 1: View Tasks (Tasks Present)

1. Add some tasks using `python src/add.py`
2. Run `python src/view.py`
3. Verify all tasks are displayed with correct ID, title, description, and status

### Test 2: View Tasks (No Tasks)

1. Start fresh session (no tasks in memory)
2. Run `python src/view.py`
3. Verify "No tasks found" message is displayed

### Test 3: Status Indicators

1. Create tasks with different completion statuses
2. View tasks
3. Verify `[X]` appears for completed tasks
4. Verify `[ ]` appears for incomplete tasks

## Troubleshooting

### "No tasks found" but you added tasks

**Issue**: Tasks were added in a different program session
**Solution**: In-memory storage doesn't persist. Add tasks in current session.

### Tasks display in wrong order

**Issue**: Tasks are stored in insertion order
**Solution**: This is expected behavior. Tasks display in the order they were added.

### Status indicators not showing correctly

**Issue**: Check logic in status assignment
**Solution**: Verify `task.completed` boolean is being checked correctly

## Next Steps

After implementing this feature:

1. Test viewing tasks with various data (empty list, many tasks, long text)
2. Test status indicators with both completed and incomplete tasks
3. Verify display format is readable
4. Consider integration with future features (update, delete, toggle)

For future features, this foundation can be extended with:
- Filter tasks by status
- Sort tasks by various criteria
- Search tasks by title/description
- Export tasks to file

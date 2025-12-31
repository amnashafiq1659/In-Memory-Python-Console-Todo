# Quickstart Guide: Mark Task Complete / Incomplete

**Feature**: 005-mark-complete
**Purpose**: Get up and running with task completion status management quickly

## Overview

This feature provides functionality to mark tasks as complete or incomplete by entering their unique ID through the console interface. Each operation validates the task ID and provides clear feedback to the user.

## Prerequisites

- Python 3.9 or higher installed
- Basic familiarity with running Python scripts from command line
- Tasks must be added using Spec 001 functionality (add task)
- Task dataclass and storage must be available (from `src/add.py`)

## Installation

No installation required. This feature uses only Python standard library.

## Quick Start

### 1. Understand Task Mutation

The Task dataclass is `@dataclass(frozen=True)`, meaning objects are immutable. To update status, we create a new object:

```python
# Old approach (doesn't work - frozen)
task.completed = True  # Error: cannot assign to frozen instance

# Correct approach
updated_task = Task(
    id=task.id,
    title=task.title,
    description=task.description,
    completed=True  # Only this field changes
)
```

### 2. Validate Task ID

```python
def validate_task_id(task_id: int) -> None:
    """Validate that a task ID is valid and exists."""
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Invalid ID format")

    # Check if task exists
    for task in _tasks:
        if task.id == task_id:
            return

    raise ValueError("Task not found")
```

### 3. Mark Task Complete (Core Function)

```python
from src.add import _tasks, Task

def mark_complete(task_id: int) -> Task:
    """Mark a task as complete by its ID."""
    global _tasks

    # Find task by ID
    for i, task in enumerate(_tasks):
        if task.id == task_id:
            # Create new task with completed=True
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=True
            )
            # Replace in list
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")
```

### 4. Mark Task Incomplete (Core Function)

```python
def mark_incomplete(task_id: int) -> Task:
    """Mark a task as incomplete by its ID."""
    global _tasks

    # Find task by ID
    for i, task in enumerate(_tasks):
        if task.id == task_id:
            # Create new task with completed=False
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=False
            )
            # Replace in list
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")
```

### 5. Console UI (User Interaction)

```python
def run_complete_task_ui() -> None:
    """Interactive console interface for marking tasks complete/incomplete."""
    if not _tasks:
        print("No tasks to update. Add tasks first.")
        return

    print("=== Mark Task Complete / Incomplete ===")
    print()

    while True:
        # Get action
        action = input("Do you want to mark a task as (c)omplete or (i)ncomplete? ").strip().lower()
        if action not in ('c', 'i'):
            print("Invalid choice. Please enter 'c' or 'i'.")
            continue

        # Get task ID
        task_id_str = input("Enter task ID: ").strip()

        # Validate and convert ID
        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Invalid ID format")
            continue

        # Perform operation
        try:
            if action == 'c':
                updated_task = mark_complete(task_id)
                status_word = "complete"
            else:
                updated_task = mark_incomplete(task_id)
                status_word = "incomplete"

            # Check if status actually changed
            old_status = not updated_task.completed if action == 'c' else updated_task.completed
            if old_status == updated_task.completed:
                state = "complete" if updated_task.completed else "incomplete"
                print(f"Task {task_id} is already {state}")
            else:
                print(f"Task {task_id} marked as {status_word}")

        except ValueError as e:
            print(f"Error: {e}")

        # Ask if continue
        choice = input("\nMark another task? (y/n): ").strip().lower()
        if choice != 'y':
            break
```

### 6. Main Entry Point

```python
if __name__ == "__main__":
    from src.add import _tasks, Task

    print("=== Task Completion Manager ===")
    run_complete_task_ui()
    print("\nGoodbye!")
```

## Complete Implementation (complete.py)

```python
from src.add import _tasks, Task

def validate_task_id(task_id: int) -> None:
    """
    Validate that a task ID is valid and exists.

    Args:
        task_id: The task ID to validate.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Invalid ID format")

    # Check if task exists
    for task in _tasks:
        if task.id == task_id:
            return

    raise ValueError("Task not found")

def mark_complete(task_id: int) -> Task:
    """
    Mark a task as complete by its ID.

    Args:
        task_id: The unique ID of the task to mark complete.

    Returns:
        Task: The updated task with completed=True.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    global _tasks

    for i, task in enumerate(_tasks):
        if task.id == task_id:
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=True
            )
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")

def mark_incomplete(task_id: int) -> Task:
    """
    Mark a task as incomplete by its ID.

    Args:
        task_id: The unique ID of the task to mark incomplete.

    Returns:
        Task: The updated task with completed=False.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    global _tasks

    for i, task in enumerate(_tasks):
        if task.id == task_id:
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=False
            )
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")

def run_complete_task_ui() -> None:
    """
    Interactive console interface to mark tasks complete or incomplete.

    Returns:
        None
    """
    if not _tasks:
        print("No tasks to update. Add tasks first.")
        return

    print("=== Mark Task Complete / Incomplete ===")
    print()

    while True:
        # Get action
        action = input("Do you want to mark a task as (c)omplete or (i)ncomplete? ").strip().lower()
        if action not in ('c', 'i'):
            print("Invalid choice. Please enter 'c' or 'i'.")
            continue

        # Get task ID
        task_id_str = input("Enter task ID: ").strip()

        # Validate and convert ID
        try:
            task_id = int(task_id_str)
            validate_task_id(task_id)
        except ValueError:
            print("Invalid ID format")
            continue

        # Perform operation
        try:
            if action == 'c':
                updated_task = mark_complete(task_id)
                status_word = "complete"
            else:
                updated_task = mark_incomplete(task_id)
                status_word = "incomplete"

            print(f"Task {task_id} marked as {status_word}")

        except ValueError as e:
            print(f"Error: {e}")

        # Ask if continue
        choice = input("\nMark another task? (y/n): ").strip().lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    from src.add import _tasks, Task

    print("=== Task Completion Manager ===")
    run_complete_task_ui()
    print("\nGoodbye!")
```

## Running the Program

### From Command Line

```bash
python src/complete.py
```

### Example Session (Mark Complete)

```
=== Task Completion Manager ===
=== Mark Task Complete / Incomplete ===

Do you want to mark a task as (c)omplete or (i)ncomplete? c
Enter task ID: 1
Task 1 marked as complete

Mark another task? (y/n): n

Goodbye!
```

### Example Session (Mark Incomplete)

```
=== Task Completion Manager ===
=== Mark Task Complete / Incomplete ===

Do you want to mark a task as (c)omplete or (i)ncomplete? i
Enter task ID: 2
Task 2 marked as incomplete

Mark another task? (y/n): n

Goodbye!
```

### Example Session (No Tasks)

```
=== Task Completion Manager ===
No tasks to update. Add tasks first.

Goodbye!
```

## Key Concepts

### Task Mutation Pattern

Since Task objects are frozen (`@dataclass(frozen=True)`):
1. Find task in `_tasks` list by ID
2. Create new Task object with updated `completed` field
3. Replace old task in list at same index
4. All other fields (id, title, description) are preserved unchanged

### Validation Strategy

Two levels of validation:
1. **Format validation**: Is `task_id` a positive integer?
2. **Existence validation**: Does a task with that ID exist?

This provides clear error messages:
- "Invalid ID format" for bad input
- "Task not found" for non-existent IDs

### Status Change Detection

The UI checks if status actually changed:
- If task is already complete when marking complete → "Task is already complete"
- If task is already incomplete when marking incomplete → "Task is already incomplete"
- Otherwise → "Task marked as complete/incomplete"

## Common Use Cases

### Programmatically Mark Task Complete

```python
from src.complete import mark_complete

# Mark task with ID 1 as complete
updated_task = mark_complete(1)
print(f"Task {updated_task.id} completed: {updated_task.completed}")
```

### Programmatically Mark Task Incomplete

```python
from src.complete import mark_incomplete

# Mark task with ID 2 as incomplete
updated_task = mark_incomplete(2)
print(f"Task {updated_task.id} completed: {updated_task.completed}")
```

### Validate Task ID Before Operation

```python
from src.complete import validate_task_id

try:
    validate_task_id(5)
    print("Task ID is valid and exists")
except ValueError as e:
    print(f"Validation error: {e}")
```

### Get All Completed Tasks

```python
from src.add import _tasks

completed_tasks = [t for t in _tasks if t.completed]
print(f"Completed tasks: {len(completed_tasks)}")
```

### Get All Incomplete Tasks

```python
from src.add import _tasks

incomplete_tasks = [t for t in _tasks if not t.completed]
print(f"Pending tasks: {len(incomplete_tasks)}")
```

## Integration with Previous Specs

This feature integrates with previous specs:

1. **Spec 001 (Add Task)**: Creates tasks with `completed=False` by default
2. **Spec 002 (View Tasks)**: Displays tasks with `[X]` for complete, `[ ]` for incomplete
3. **Spec 003 (Update Task)**: Can modify title/description without affecting `completed` status
4. **Spec 004 (Delete Task)**: Removes tasks from `_tasks` list

### Complete Workflow Example

```bash
# 1. Add tasks
python src/add.py

# 2. View tasks (all incomplete)
python src/view.py

# 3. Mark some tasks complete
python src/complete.py

# 4. View tasks (showing status)
python src/view.py
```

## Testing Your Implementation

### Test 1: Mark Task Complete

1. Add tasks using `python src/add.py`
2. Run `python src/complete.py`
3. Choose to mark task complete
4. Enter a valid task ID
5. Verify "Task marked as complete" message appears
6. Run `python src/view.py` to verify status changed

### Test 2: Mark Task Incomplete

1. Mark a task as complete
2. Run `python src/complete.py`
3. Choose to mark task incomplete
4. Enter the task ID
5. Verify "Task marked as incomplete" message appears

### Test 3: Invalid Task ID Format

1. Run `python src/complete.py`
2. Enter non-numeric ID (e.g., "abc")
3. Verify "Invalid ID format" error appears

### Test 4: Task Not Found

1. Run `python src/complete.py`
2. Enter a valid number that doesn't exist (e.g., 999)
3. Verify "Task not found" error appears

### Test 5: No Tasks

1. Start fresh session (no tasks in memory)
2. Run `python src/complete.py`
3. Verify "No tasks to update" message appears

## Troubleshooting

### "Task not found" but task exists

**Issue**: Task was added in a different program session
**Solution**: In-memory storage doesn't persist. Add tasks in current session.

### Status not updating in view

**Issue**: Not viewing tasks after updating status
**Solution**: Run `python src/view.py` after marking complete/incomplete to see updated status.

### Error: cannot assign to frozen instance

**Issue**: Trying to modify task.completed directly
**Solution**: Use `mark_complete()` or `mark_incomplete()` functions which create new Task objects.

### Import errors when running complete.py

**Issue**: Python cannot find `src.add` module
**Solution**: Ensure you're running from project root and `src/add.py` exists.

## Next Steps

After implementing this feature:

1. Test marking tasks complete and incomplete
2. Verify status updates are reflected in view
3. Test error handling (invalid IDs, non-existent tasks)
4. Test edge cases (already complete/incomplete, empty task list)

For future features, this foundation can be extended with:
- Bulk mark operations (mark all tasks complete)
- Filter tasks by completion status
- Sort tasks by completion status
- Task completion history tracking

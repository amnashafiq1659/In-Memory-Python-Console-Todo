# Quick Start: Delete Task

**Feature**: Delete Task
**Date**: 2025-12-31
**Prerequisites**: Python 3.13+

## Overview

This guide provides quick instructions for using Delete Task functionality in Todo console application.

## Installation

No installation required. The Delete Task feature is part of the in-memory Todo console application.

1. Ensure Python 3.13 or later is installed:
```bash
python --version
```

2. Navigate to the project directory:
```bash
cd D:\todo_console
```

## Basic Usage

### Running Delete Task UI

```bash
python src/delete.py
```

This launches the interactive console interface for deleting tasks.

### Example Session

```bash
=== Task Deleter ===

Available tasks:
1 | [ ] | Buy groceries | Milk, eggs, bread
2 | [X] | Write report | Q4 sales analysis

Enter task ID: 1

Current task:
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: [ ] (incomplete)

Delete this task? (y/n): y

Task deleted successfully!

Delete another task? (y/n): n

Goodbye!
```

## Features

### Confirmation Before Deletion

The system displays task details and requires explicit confirmation before deleting:

```bash
Enter task ID: 1

Current task:
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread
Status: [ ] (incomplete)

Delete this task? (y/n):
```

### Error Handling

**Invalid task ID**:
```bash
Enter task ID: 99
Error: Task with ID 99 not found
```

**Non-numeric input**:
```bash
Enter task ID: abc
Error: Invalid task ID format. Please enter a number.
```

**Negative ID**:
```bash
Enter task ID: -1
Error: Task ID must be a positive integer
```

### Task Reference

Before each deletion, the system displays all available tasks:

```bash
Available tasks:
1 | [ ] | Buy groceries | Milk, eggs, bread
2 | [X] | Write report | Q4 sales analysis
3 | [ ] | Call client | Discuss project
```

This helps users find the correct ID before proceeding with deletion.

## Command-Line Reference

### Main Script

```bash
python src/delete.py
```

Launches interactive delete task interface.

## Requirements Validation

### Before Deleting

To delete a task, you must:
1. Have tasks already created (use `python src/add.py`)
2. Know the task ID (use `python src/view.py` to list tasks)
3. Task will be displayed for confirmation before deletion

### During Deletion

- Enter a valid numeric task ID
- Confirm deletion when prompted (y/n)
- 'n' or any non-'y' input will cancel the deletion

## Common Workflows

### Workflow 1: Delete Task

```bash
# Step 1: View tasks to find ID
python src/view.py

# Step 2: Delete task by ID
python src/delete.py
# Enter task ID: [ID from view]
# Confirm deletion: y
```

### Workflow 2: Delete Multiple Tasks

```bash
python src/delete.py
# Enter task ID: [first task]
# Confirm: y

Delete another task? (y/n): y

# Enter task ID: [second task]
# Confirm: y

Delete another task? (y/n): n
```

## Data Persistence

**Important**: All tasks and deletions are stored in memory only.

- Tasks persist during the current runtime session
- Deletions are reflected immediately
- Changes are lost when the application exits
- To persist data, you would need to implement file/database storage (not in scope for Spec 4)

## Module Functions

### `delete_task(task_id: int) -> None`

Programmatic function to delete a task without UI.

**Parameters:**
- `task_id` (int): The ID of the task to delete

**Returns:**
- `None`: No return value (deletion is destructive)

**Raises:**
- `ValueError`: If task ID doesn't exist
- `ValueError`: If task_id is not positive

**Example:**
```python
from delete import delete_task

# Delete task by ID
delete_task(1)
```

### `run_delete_task_ui() -> None`

Interactive console UI for deleting tasks.

**Returns:**
- `None` (interacts via stdin/stdout)

**Example:**
```python
from delete import run_delete_task_ui

run_delete_task_ui()
```

## Testing

### Manual Test Scenarios

1. **Valid deletion**: Create task, view to get ID, delete by ID, verify task is gone
2. **Invalid ID**: Attempt to delete non-existent task, verify error message
3. **Non-numeric input**: Enter "abc" as ID, verify error message
4. **Cancellation**: Select task, view details, enter "n" to cancel, verify task remains
5. **Multiple deletions**: Delete one task, then another, verify both are removed
6. **Empty task list**: Try to delete when no tasks exist
7. **Delete completed task**: Delete a task with completed status
8. **Delete incomplete task**: Delete a task with incomplete status

## Troubleshooting

### Issue: "Task not found" error

**Cause**: Task ID doesn't exist in memory

**Solution**:
1. Run `python src/view.py` to list all tasks
2. Use a valid task ID from the list
3. Create tasks first with `python src/add.py` if none exist

### Issue: Changes not persisting

**Cause**: In-memory storage is session-based

**Solution**: This is expected behavior. To see changes, run delete and view in the same session.

### Issue: Import errors

**Cause**: Missing dependencies or incorrect working directory

**Solution**:
1. Ensure you're in project root: `cd D:\todo_console`
2. Verify `add.py` exists in `src/` directory
3. Check Python version: `python --version` (requires 3.13+)

## Integration with Other Features

### Add Task (Spec 1)

Create tasks to delete:
```bash
python src/add.py
# Creates tasks with IDs 1, 2, 3, etc.
```

### View Tasks (Spec 2)

View tasks to see what's available:
```bash
python src/view.py
# Displays all tasks with their IDs and status
```

### Update Task (Spec 3)

Modify existing tasks:
```bash
python src/update.py
# Updates title and/or description by task ID
```

### Delete Task (Spec 4)

Remove unwanted or completed tasks:
```bash
python src/delete.py
# Deletes tasks by task ID with confirmation
```

## Next Steps

After completing deletions:
- Verify deletions with `python src/view.py`
- Continue deleting more tasks in the same session
- Exit the application (changes are lost on exit)

## Support

For issues or questions:
1. Review the specification: `specs/004-delete-task/spec.md`
2. Review the implementation plan: `specs/004-delete-task/plan.md`
3. Check test cases for examples: `tests/test_delete.py`

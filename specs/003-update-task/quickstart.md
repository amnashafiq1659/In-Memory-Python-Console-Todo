# Quick Start: Update Task

**Feature**: Update Task
**Date**: 2025-12-31
**Prerequisites**: Python 3.13+

## Overview

This guide provides quick instructions for using the Update Task functionality in the Todo console application.

## Installation

No installation required. The Update Task feature is part of the in-memory Todo console application.

1. Ensure Python 3.13 or later is installed:
```bash
python --version
```

2. Navigate to the project directory:
```bash
cd D:\todo_console
```

## Basic Usage

### Running Update Task UI

```bash
python src/update.py
```

This launches the interactive console interface for updating tasks.

### Example Session

```bash
=== Task Updater ===

Available tasks:
1 | [ ] | Buy groceries | Milk, eggs, bread
2 | [X] | Write report | Q4 sales analysis

Enter task ID: 1

Current task:
ID: 1
Title: Buy groceries
Description: Milk, eggs, bread

Enter new title (press Enter to keep current): Buy weekly groceries
Enter new description (press Enter to keep current): Milk, eggs, bread, fruits

Task updated successfully!
ID: 1
Title: Buy weekly groceries
Description: Milk, eggs, bread, fruits
Status: [ ] (incomplete)

Update another task? (y/n): n

Goodbye!
```

## Features

### Partial Updates

You can update just the title, just the description, or both:

**Update title only:**
```
Enter new title (press Enter to keep current): New title here
Enter new description (press Enter to keep current): [press Enter]
```

**Update description only:**
```
Enter new title (press Enter to keep current): [press Enter]
Enter new description (press Enter to keep current): New description here
```

**Update both:**
```
Enter new title (press Enter to keep current): New title here
Enter new description (press Enter to keep current): New description here
```

### Error Handling

**Invalid task ID:**
```
Enter task ID: 99
Error: Task with ID 99 not found
```

**Non-numeric input:**
```
Enter task ID: abc
Error: Invalid task ID format. Please enter a number.
```

**Empty title:**
```
Enter new title (press Enter to keep current): [just spaces]
Error: Title cannot be empty or whitespace-only
```

## Command-Line Reference

### Main Script

```bash
python src/update.py
```

Launches interactive update task interface.

## Requirements Validation

### Before Updating

To update a task, you must:
1. Have tasks already created (use `python src/add.py`)
2. Know the task ID (use `python src/view.py` to list tasks)

### During Update

- Enter a valid numeric task ID
- Optionally provide new title (can't be empty/whitespace if provided)
- Optionally provide new description (can be empty)
- Press Enter on either field to keep the current value

## Common Workflows

### Workflow 1: Update Task Title

```bash
# Step 1: View tasks to find ID
python src/view.py

# Step 2: Update task by ID
python src/update.py
# Enter task ID: [ID from view]
# Enter new title: [new title]
# Enter new description: [press Enter to skip]
```

### Workflow 2: Update Task Description

```bash
python src/update.py
# Enter task ID: [known ID]
# Enter new title: [press Enter to skip]
# Enter new description: [new description]
```

### Workflow 3: Update Both Fields

```bash
python src/update.py
# Enter task ID: [known ID]
# Enter new title: [new title]
# Enter new description: [new description]
```

## Data Persistence

**Important**: All tasks and updates are stored in memory only.

- Tasks persist during the current runtime session
- Changes are lost when the application exits
- To persist data, you would need to implement file/database storage (not in scope for Spec 3)

## Module Functions

### `update_task(task_id, new_title, new_description)`

Programmatic function to update a task without UI.

**Parameters:**
- `task_id` (int): The ID of the task to update
- `new_title` (str | None): New title, or None to keep current
- `new_description` (str | None): New description, or None to keep current

**Returns:**
- `Task`: The updated Task object

**Raises:**
- `ValueError`: If task ID doesn't exist
- `ValueError`: If new_title is empty/whitespace

**Example:**
```python
from update import update_task

# Update both title and description
task = update_task(1, "New title", "New description")

# Update title only
task = update_task(1, "New title", None)

# Update description only
task = update_task(1, None, "New description")
```

### `run_update_task_ui()`

Interactive console UI for updating tasks.

**Returns:**
- None (interacts via stdin/stdout)

**Example:**
```python
from update import run_update_task_ui

run_update_task_ui()
```

## Testing

### Manual Test Scenarios

1. **Valid update both fields**: Create task, update title and description, verify both changed
2. **Valid update title only**: Create task, update title only, verify description unchanged
3. **Valid update description only**: Create task, update description only, verify title unchanged
4. **Invalid task ID**: Attempt to update non-existent task, verify error message
5. **Empty input validation**: Provide empty title, verify error message
6. **Whitespace validation**: Provide whitespace-only title, verify error message
7. **No changes**: Skip both fields, verify task unchanged

### Automated Testing

Tests are located in `tests/test_update.py`:
```bash
pytest tests/test_update.py -v
```

## Troubleshooting

### Issue: "Task not found" error

**Cause**: Task ID doesn't exist in memory

**Solution**:
1. Run `python src/view.py` to list all tasks
2. Use a valid task ID from the list
3. Create tasks first with `python src/add.py` if none exist

### Issue: Changes not persisting

**Cause**: In-memory storage is session-based

**Solution**: This is expected behavior. To see changes, run update and view in the same session.

### Issue: Import errors

**Cause**: Missing dependencies or incorrect working directory

**Solution**:
1. Ensure you're in the project root: `cd D:\todo_console`
2. Verify `add.py` exists in `src/` directory
3. Check Python version: `python --version` (requires 3.13+)

## Integration with Other Features

### Add Task (Spec 1)

Create tasks to update:
```bash
python src/add.py
# Creates tasks with IDs 1, 2, 3, etc.
```

### View Tasks (Spec 2)

View tasks to see updates:
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

## Next Steps

After completing updates:
- Verify changes with `python src/view.py`
- Continue updating more tasks in the same session
- Exit the application (changes are lost on exit)

## Support

For issues or questions:
1. Review the specification: `specs/003-update-task/spec.md`
2. Review the implementation plan: `specs/003-update-task/plan.md`
3. Check test cases for examples: `tests/test_update.py`

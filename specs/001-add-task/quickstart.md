# Quickstart Guide: Task Model & Add Task

**Feature**: 001-add-task
**Purpose**: Get up and running with the task creation functionality quickly

## Overview

This feature provides an in-memory task management system where users can add tasks via console interface. Each task has a unique ID, title, description, and completion status (default: incomplete).

## Prerequisites

- Python 3.9 or higher installed
- Basic familiarity with running Python scripts from command line

## Installation

No installation required. This feature uses only Python standard library.

## Quick Start

### 1. Create the Source File

Create `src/add.py` with the following structure:

```python
from dataclasses import dataclass

# In-memory storage
_tasks: list["Task"] = []
_next_id: int = 1

@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    completed: bool

def add_task(title: str, description: str) -> Task:
    """Create a new task with the given title and description."""
    global _next_id, _tasks

    if not title or title.isspace():
        raise ValueError("Title cannot be empty")

    task = Task(id=_next_id, title=title, description=description, completed=False)
    _tasks.append(task)
    _next_id += 1

    return task

def run_add_task_ui() -> None:
    """Interactive console interface for adding tasks."""
    while True:
        print()  # Blank line for readability

        # Get title
        while True:
            title = input("Enter task title: ").strip()
            if title:
                break
            print("Error: Title cannot be empty")

        # Get description
        description = input("Enter task description (optional, press Enter to skip): ").strip()

        # Add task
        task = add_task(title, description)
        print(f"Task added with ID: {task.id}")

        # Ask if user wants to continue
        choice = input("\nAdd another task? (y/n): ").strip().lower()
        if choice != "y":
            break

if __name__ == "__main__":
    print("=== Task Creator ===")
    run_add_task_ui()
    print("\nGoodbye!")
```

### 2. Run the Program

```bash
python src/add.py
```

### 3. Interact with the Console

```
=== Task Creator ===

Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, bread, eggs
Task added with ID: 1

Add another task? (y/n): y

Enter task title: Call doctor
Enter task description (optional, press Enter to skip):
Task added with ID: 2

Add another task? (y/n): n

Goodbye!
```

## Key Concepts

### Task Structure

Every task has four fields:
- **ID**: Automatically assigned sequential number (1, 2, 3, ...)
- **Title**: Required text field (must not be empty)
- **Description**: Optional text field (can be empty)
- **Completed**: Boolean status (always `False` for new tasks)

### In-Memory Storage

- Tasks are stored in a Python list (`_tasks`)
- Tasks exist only during program execution
- When the program exits, all tasks are lost
- No file or database persistence

### Adding Tasks

- Use `add_task(title, description)` function in code
- Or use `run_add_task_ui()` for interactive console input
- Title validation: rejects empty or whitespace-only titles
- Description is optional (can be empty string)

## Common Use Cases

### Add a Task Programmatically

```python
from src.add import add_task

task = add_task("Finish project", "Complete phase 1 by Friday")
print(f"Created task {task.id}: {task.title}")
```

### Handle Invalid Input

```python
try:
    add_task("", "Invalid task")
except ValueError as e:
    print(f"Error: {e}")  # Error: Title cannot be empty
```

## Testing Your Implementation

### Manual Test Checklist

- [ ] Program starts without errors
- [ ] Can add a task with title and description
- [ ] Can add a task with title and empty description
- [ ] Empty title is rejected with error message
- [ ] Whitespace-only title is rejected with error message
- [ ] Each new task receives a unique, sequential ID
- [ ] Tasks are accepted with unicode characters (e.g., "学习中文")
- [ ] Tasks are accepted with very long titles/descriptions (1000+ chars)
- [ ] Can add multiple tasks in one session
- [ ] All tasks are accessible in memory during session

### Quick Test Script

```python
# Test script to verify functionality
from src.add import add_task, _tasks, _next_id

# Test 1: Valid task
task1 = add_task("Task 1", "Description")
assert task1.id == 1
assert task1.title == "Task 1"
assert task1.completed == False

# Test 2: Empty description
task2 = add_task("Task 2", "")
assert task2.description == ""

# Test 3: Sequential IDs
task3 = add_task("Task 3", "Description")
assert task3.id == 3

# Test 4: Empty title raises error
try:
    add_task("", "Invalid")
    assert False, "Should have raised ValueError"
except ValueError:
    pass

print("All tests passed!")
```

## Next Steps

After implementing this feature:

1. Run the program and verify the console interface works
2. Test with various inputs (unicode, long text, edge cases)
3. Check that tasks remain accessible during session
4. Verify tasks are lost when program exits (no persistence)

For future features, this foundation can be extended with:
- View/list tasks functionality
- Task completion toggle
- Task update/delete operations
- File persistence

# Function Contract: Add Task

**Feature**: 001-add-task
**Created**: 2025-12-31
**Type**: Internal Function Contract

## Function: `add_task(title: str, description: str) -> Task`

### Purpose
Create a new task with the provided title and description, generate a unique ID, set completion status to incomplete, and store the task in memory.

### Signature

```python
def add_task(title: str, description: str) -> Task:
    """
    Create a new task and add it to the in-memory task list.

    Args:
        title: The title/name of the task. Must not be empty.
        description: Optional description of the task. Can be empty string.

    Returns:
        Task: The newly created task object.

    Raises:
        ValueError: If title is empty or whitespace-only.
    """
    pass
```

### Input Parameters

| Parameter | Type | Required | Validation | Description |
|-----------|------|----------|------------|-------------|
| `title` | `str` | Yes | Non-empty, non-whitespace | Title/name of the task |
| `description` | `str` | Yes | None | Optional description; defaults to empty string |

### Return Value

| Type | Description |
|------|-------------|
| `Task` | The newly created task object with all fields populated |

### Errors

| Error Type | Condition | Handling |
|------------|-----------|-----------|
| `ValueError` | `title` is empty string or contains only whitespace | Function raises, caller should handle and display error message to user |
| `TypeError` | `title` or `description` is not a string | Function raises (should not occur with proper input handling) |

### Pre-conditions

1. `_tasks` list is accessible (module-level variable)
2. `_next_id` counter is initialized (module-level variable)

### Post-conditions

1. A new `Task` object is created with:
   - `id` = current value of `_next_id`
   - `title` = provided `title` argument
   - `description` = provided `description` argument
   - `completed` = `False`
2. `_next_id` is incremented by 1
3. New task is appended to `_tasks` list
4. Length of `_tasks` list increases by 1

### Side Effects

- Modifies module-level `_tasks` list (appends new task)
- Modifies module-level `_next_id` counter (increments)
- No I/O side effects (no file/DB writes)

### Example Usage

```python
# Valid task
task1 = add_task("Buy groceries", "Milk, bread, eggs")
# Result: Task(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False)

# Task with empty description (allowed)
task2 = add_task("Call doctor", "")
# Result: Task(id=2, title="Call doctor", description="", completed=False)

# Empty title (raises error)
try:
    add_task("", "Invalid")
except ValueError as e:
    print(f"Error: {e}")  # Error: Title cannot be empty
```

### Performance Characteristics

- **Time Complexity**: O(1) - list append operation
- **Space Complexity**: O(1) per task (fixed size object)
- **Max Throughput**: Satisfies SC-002 (1,000+ tasks without degradation)

---

## Class: Task (Data Class)

### Purpose
Immutable data structure representing a task.

### Signature

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Task:
    """
    Represents a task with an ID, title, description, and completion status.

    Attributes:
        id: Unique identifier for the task.
        title: Title/name of the task.
        description: Description of the task.
        completed: Whether the task is completed (always False for new tasks).
    """
    id: int
    title: str
    description: str
    completed: bool
```

### Attributes

| Attribute | Type | Immutability | Default | Description |
|-----------|------|--------------|----------|-------------|
| `id` | `int` | Immutable | Auto-generated | Unique identifier |
| `title` | `str` | Immutable | Required | Task title |
| `description` | `str` | Immutable | `""` | Task description |
| `completed` | `bool` | Immutable | `False` | Completion status |

### Design Rationale

- **Dataclass**: Clean, concise representation with auto-generated `__init__`, `__repr__`, etc.
- **Frozen**: Prevents accidental mutation after creation (ensures data integrity)
- **Type Hints**: Supports static type checking and IDE auto-completion

---

## Console Interaction Function: `run_add_task_ui()`

### Purpose
Interactive console interface for adding a task. Prompts user for title and description, validates input, and adds the task.

### Signature

```python
def run_add_task_ui() -> None:
    """
    Interactive console interface to add a task.

    Prompts user for title and description, validates input,
    and calls add_task() to create the task.

    Displays success or error messages to the user.

    Returns:
        None
    """
    pass
```

### User Interaction Flow

1. Display prompt: "Enter task title: "
2. Read user input for title
3. Validate title:
   - If empty/whitespace: display error "Error: Title cannot be empty" and re-prompt
   - If valid: continue
4. Display prompt: "Enter task description (optional, press Enter to skip): "
5. Read user input for description
6. Call `add_task(title, description)`
7. Display success: "Task added with ID: {id}"
8. Return to step 1 (allow adding multiple tasks) or exit based on user choice

### Side Effects

- Reads from stdin (`input()` function)
- Writes to stdout (`print()` function)
- Calls `add_task()` which modifies `_tasks` list

### Example Session

```
Enter task title: Buy groceries
Enter task description (optional, press Enter to skip): Milk, bread, eggs
Task added with ID: 1

Enter task title: Call doctor
Enter task description (optional, press Enter to skip):
Task added with ID: 2

Enter task title:
Error: Title cannot be empty

Enter task title: Review documents
Enter task description (optional, press Enter to skip): Q4 financial reports
Task added with ID: 3
```

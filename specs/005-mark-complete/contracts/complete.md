# Function Contract: Mark Task Complete / Incomplete

**Feature**: 005-mark-complete
**Created**: 2025-12-31
**Type**: Internal Function Contract

## Function: `mark_complete(task_id: int) -> Task`

### Purpose
Mark a task as complete by updating its completion status to `True`.

### Signature

```python
def mark_complete(task_id: int) -> Task:
    """
    Mark a task as complete by its ID.

    Args:
        task_id: The unique ID of the task to mark complete.
                 Must be a positive integer.

    Returns:
        Task: The updated Task object with completed=True.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    pass
```

### Input Parameters

| Parameter | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `task_id` | `int` | Positive integer, must exist in task list | Unique identifier of task to mark complete |

### Return Value

| Type | Description |
|------|-------------|
| `Task` | The updated Task object with `completed=True` |

### Errors

| Error | Condition | Message |
|-------|-----------|----------|
| `ValueError` | task_id is not a positive integer | "Invalid ID format" |
| `ValueError` | task_id does not exist in task list | "Task not found" |

### Pre-conditions

1. `_tasks` list is accessible (module-level variable in `src/add.py`)
2. Task class is imported from `src/add.py`
3. `task_id` is a positive integer
4. A task with matching ID exists in `_tasks` list

### Post-conditions

1. Returned Task object has `completed=True`
2. `_tasks` list contains the updated Task object
3. All other Task objects remain unchanged
4. Task ID, title, and description are preserved

### Side Effects

- Modifies `_tasks` list by replacing the target Task object
- Does not modify `_next_id` counter
- No file or external system interactions

### Example Usage

```python
# Mark task as complete
updated_task = mark_complete(1)
print(f"Task {updated_task.id} is now complete: {updated_task.completed}")
```

### Performance Characteristics

- **Time Complexity**: O(n) - linear search through `_tasks` list
- **Space Complexity**: O(1) - creates one new Task object
- **Max Throughput**: Satisfies SC-001 (complete in < 3 seconds for 1,000+ tasks)

---

## Function: `mark_incomplete(task_id: int) -> Task`

### Purpose
Mark a task as incomplete by updating its completion status to `False`.

### Signature

```python
def mark_incomplete(task_id: int) -> Task:
    """
    Mark a task as incomplete by its ID.

    Args:
        task_id: The unique ID of the task to mark incomplete.
                 Must be a positive integer.

    Returns:
        Task: The updated Task object with completed=False.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    pass
```

### Input Parameters

| Parameter | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `task_id` | `int` | Positive integer, must exist in task list | Unique identifier of task to mark incomplete |

### Return Value

| Type | Description |
|------|-------------|
| `Task` | The updated Task object with `completed=False` |

### Errors

| Error | Condition | Message |
|-------|-----------|----------|
| `ValueError` | task_id is not a positive integer | "Invalid ID format" |
| `ValueError` | task_id does not exist in task list | "Task not found" |

### Pre-conditions

1. `_tasks` list is accessible (module-level variable in `src/add.py`)
2. Task class is imported from `src/add.py`
3. `task_id` is a positive integer
4. A task with matching ID exists in `_tasks` list

### Post-conditions

1. Returned Task object has `completed=False`
2. `_tasks` list contains the updated Task object
3. All other Task objects remain unchanged
4. Task ID, title, and description are preserved

### Side Effects

- Modifies `_tasks` list by replacing the target Task object
- Does not modify `_next_id` counter
- No file or external system interactions

### Example Usage

```python
# Mark task as incomplete
updated_task = mark_incomplete(2)
print(f"Task {updated_task.id} is now incomplete: {updated_task.completed}")
```

### Performance Characteristics

- **Time Complexity**: O(n) - linear search through `_tasks` list
- **Space Complexity**: O(1) - creates one new Task object
- **Max Throughput**: Satisfies SC-002 (complete in < 3 seconds for 1,000+ tasks)

---

## Helper Function: `validate_task_id(task_id: int) -> None`

### Purpose
Validate that a task ID is a positive integer and exists in the task list.

### Signature

```python
def validate_task_id(task_id: int) -> None:
    """
    Validate that a task ID is valid and exists.

    Args:
        task_id: The task ID to validate.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    pass
```

### Input Parameters

| Parameter | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| `task_id` | `int` | Any integer | Task ID to validate |

### Return Value

None

### Errors

| Error | Condition | Message |
|-------|-----------|----------|
| `ValueError` | task_id is not positive (<= 0) | "Invalid ID format" |
| `ValueError` | task_id does not exist in task list | "Task not found" |

### Pre-conditions

1. `_tasks` list is accessible (module-level variable in `src/add.py`)

### Post-conditions

1. If no error raised, task_id is valid and exists in `_tasks`

### Side Effects

- None (read-only validation)

### Performance Characteristics

- **Time Complexity**: O(n) - linear search through `_tasks` list
- **Space Complexity**: O(1) - no additional storage

---

## Console Interaction Function: `run_complete_task_ui() -> None`

### Purpose
Interactive console interface for marking tasks complete or incomplete.

### Signature

```python
def run_complete_task_ui() -> None:
    """
    Interactive console interface to mark tasks as complete or incomplete.

    Prompts user for task ID and action (mark complete or incomplete),
    validates input, and calls appropriate function to update task status.

    Returns:
        None
    """
    pass
```

### User Interaction Flow

1. Display header: "=== Mark Task Complete / Incomplete ==="
2. Check if task list is empty:
   - If empty: Display "No tasks to update. Add tasks first." and return
3. Prompt user for action:
   - "Do you want to mark a task as (c)omplete or (i)ncomplete? "
4. If invalid choice: Display error and prompt again
5. Prompt user for task ID: "Enter task ID: "
6. Validate task ID:
   - If invalid: Display "Invalid ID format" and prompt again
   - If not found: Display "Task not found" and prompt again
7. Perform operation:
   - If complete: Call `mark_complete(task_id)`
   - If incomplete: Call `mark_incomplete(task_id)`
8. Display success message: "Task {task_id} marked as complete/incomplete"
9. Check for special states:
   - If task was already complete: "Task {task_id} is already complete"
   - If task was already incomplete: "Task {task_id} is already incomplete"
10. Ask if user wants to continue:
    - "Mark another task? (y/n): "
    - If 'y': Return to step 3
    - Otherwise: Return

### Side Effects

- Writes to stdout (`print()` function)
- Reads from stdin via `input()` function
- Modifies `_tasks` list via `mark_complete()` or `mark_incomplete()`

### Example Session

```
=== Mark Task Complete / Incomplete ===

Do you want to mark a task as (c)omplete or (i)ncomplete? c
Enter task ID: 1
Task 1 marked as complete

Mark another task? (y/n): y

Do you want to mark a task as (c)omplete or (i)ncomplete? i
Enter task ID: 2
Task 2 marked as incomplete

Mark another task? (y/n): n
```

### Edge Case Handling

| Scenario | Behavior |
|----------|----------|
| Empty task list | Display "No tasks to update. Add tasks first." and return |
| Invalid action (not c/i) | Display error and prompt again |
| Invalid ID (non-integer, negative, zero) | Display "Invalid ID format" and prompt again |
| Task not found | Display "Task not found" and prompt again |
| Task already complete | Display "Task {id} is already complete" |
| Task already incomplete | Display "Task {id} is already incomplete" |
| Whitespace input | Strip whitespace before processing |
| Mixed case input (C/I/c/i) | Accept case-insensitive input |

### Input Validation Rules

1. **Action Selection**:
   - Accept: 'c' or 'i' (case-insensitive)
   - Reject: any other character

2. **Task ID Validation**:
   - Must be positive integer
   - Must exist in task list
   - Strip whitespace before conversion

3. **Continue Prompt**:
   - Accept: 'y' or 'Y' to continue
   - Any other input exits

---

## Task Mutation Pattern

### Immutability Handling

Since Task is `@dataclass(frozen=True)`, objects cannot be modified in-place:

```python
def mark_complete(task_id: int) -> Task:
    """Mark task complete by replacing the immutable object."""
    global _tasks

    # Find task by ID
    for i, task in enumerate(_tasks):
        if task.id == task_id:
            # Create new task with updated status
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=True  # Only this field changes
            )
            # Replace in list
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")
```

### State Preservation

All fields except `completed` are preserved:
- `id`: Remains unchanged (unique identifier)
- `title`: Remains unchanged (immutable after creation)
- `description`: Remains unchanged (immutable after creation)
- `completed`: Updated to target state (`True` or `False`)

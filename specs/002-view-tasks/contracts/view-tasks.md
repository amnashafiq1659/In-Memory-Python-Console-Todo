# Function Contract: View Tasks

**Feature**: 002-view-tasks
**Created**: 2025-12-31
**Type**: Internal Function Contract

## Function: `get_all_tasks() -> list[Task]`

### Purpose
Retrieve all tasks currently stored in memory.

### Signature

```python
def get_all_tasks() -> list[Task]:
    """
    Retrieve all tasks from in-memory storage.

    Returns:
        list[Task]: List of all tasks currently stored. Returns empty list if no tasks exist.
    """
    pass
```

### Input Parameters

None

### Return Value

| Type | Description |
|------|-------------|
| `list[Task]` | List of all Task objects currently stored in memory. Empty list if no tasks exist. |

### Errors

No errors raised for normal operation. Access errors would only occur if `_tasks` variable is missing (implementation bug).

### Pre-conditions

1. `_tasks` list is accessible (module-level variable in `src/add.py`)
2. Task class is imported from `src/add.py`

### Post-conditions

1. Returns all tasks currently in `_tasks` list
2. Does not modify `_tasks` or `_next_id` (read-only operation)
3. List preserves insertion order

### Side Effects

- None (read-only operation)

### Example Usage

```python
# Retrieve all tasks
tasks = get_all_tasks()

# Display count
print(f"Total tasks: {len(tasks)}")

# Iterate through tasks
for task in tasks:
    print(f"{task.id}: {task.title}")
```

### Performance Characteristics

- **Time Complexity**: O(n) - returns list reference (no iteration)
- **Space Complexity**: O(n) - reference to existing list
- **Max Throughput**: Satisfies SC-002 (display 1,000+ tasks)

---

## Console Interaction Function: `run_view_tasks_ui() -> None`

### Purpose
Interactive console interface to display all tasks with status indicators.

### Signature

```python
def run_view_tasks_ui() -> None:
    """
    Display all tasks in a user-friendly console format.

    Shows task ID, title, description, and completion status
    with visual indicators for completed vs incomplete tasks.

    Returns:
        None
    """
    pass
```

### User Interaction Flow

1. Display header: "=== Tasks ==="
2. Retrieve all tasks using `get_all_tasks()`
3. If no tasks:
   - Display message: "No tasks found. Add tasks using add task functionality."
   - Return
4. For each task:
   - Display in format: `ID | [status] | Title | Description`
   - Status indicator: `[X]` for completed, `[ ]` for incomplete
5. Display summary: f"Total: {task_count} tasks"
6. Return to caller

### Side Effects

- Writes to stdout (`print()` function)
- Reads from `_tasks` list via `get_all_tasks()`
- Does not modify any state

### Example Session

```
=== Tasks ===

1 | [ ] | Buy groceries | Milk, bread, eggs
2 | [X] | Call doctor | Annual checkup
3 | [ ] | Learn Python | Basics and advanced topics

Total: 3 tasks
```

### Edge Case Handling

| Scenario | Behavior |
|----------|----------|
| Empty task list | Display "No tasks found" message with guidance |
| Task with empty description | Display task with empty description field |
| Very long title/description | Display without truncation, let terminal wrap |
| Unicode/special characters | Display as-is |
| Mixed completed/incomplete | Show different status indicators correctly |

### Display Format Details

**Format String**:
```python
print(f"{task.id} | [{status}] | {task.title} | {task.description}")
```

**Status Indicators**:
- Completed: `[X]` (checkmark)
- Incomplete: `[ ]` (empty checkbox)

**Field Order**: ID | Status | Title | Description

---

## Status Indicator Specification

### Visual Indicators

| Status | Indicator | Description |
|--------|-----------|-------------|
| Completed | `[X]` | Checkmark indicates task is complete |
| Incomplete | `[ ]` | Empty checkbox indicates task is pending |

### Rationale

- **Universally recognizable**: Checkmarks are intuitive across cultures
- **Cross-platform**: ASCII characters work on all terminals
- **Scannable**: Status is visible at a glance without reading full text
- **Consistent**: Matches common todo list UI patterns

### Accessibility

- Clear visual distinction between states
- Position is consistent (always after ID, before title)
- High contrast between `[X]` and `[ ]`

### Alternative Considerations (Rejected)

| Alternative | Reason Rejected |
|------------|-----------------|
| Text "completed"/"incomplete" | Less scannable, takes more space |
| Colors (green/red) | Terminal color support varies |
| Unicode boxes [☑]/[☐] | Less universal, may not display correctly |
| Symbols (●/○) | Less semantically clear than checkmarks |

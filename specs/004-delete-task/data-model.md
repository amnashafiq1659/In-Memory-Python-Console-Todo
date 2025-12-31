# Data Model: Delete Task

**Feature**: Delete Task
**Date**: 2025-12-31
**Status**: Complete

## Overview

The Delete Task feature reuses existing `Task` dataclass from Spec 1 without modification. This document describes entity structure, validation rules, and state transitions for deletion operations.

## Entity: Task

### Definition

The `Task` entity represents a single todo item and is defined as a frozen dataclass in `src/add.py`:

```python
@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    completed: bool
```

**Location**: `src/add.py:7-12`

### Field Descriptions

| Field | Type | Mutability | Description | Validation |
|-------|------|-------------|-------------|-------------|
| `id` | int | Read-only | Unique identifier for task | Auto-incremented by add.py, positive integer |
| `title` | str | Read-only | Title/name of task | Required, non-empty, non-whitespace |
| `description` | str | Read-only | Optional description of task | Optional, can be empty string |
| `completed` | bool | Read-only | Completion status | True if completed, False otherwise |

**Note**: The `frozen=True` parameter makes Task instances immutable, which means updates require creating new Task instances. For deletion, tasks are removed from the list entirely.

## Storage Model

### In-Memory Storage

Tasks are stored in a global list:

```python
_tasks: list[Task] = []
```

**Location**: `src/add.py:4`

### Storage Characteristics

- **Type**: List of Task objects
- **Scope**: Global to `add.py` module, imported by `view.py`, `update.py`, and `delete.py`
- **Persistence**: In-memory only (not persisted across application restarts)
- **Access Pattern**: Sequential search by `task.id` (O(n) lookup)
- **Thread Safety**: Not required (single-threaded console application)

### ID Generation

```python
_next_id: int = 1
```

**Location**: `src/add.py:5`

- Auto-increments each time a new task is added via `add_task()`
- Provides unique, sequential task IDs
- Read-only for delete operations
- IDs are never reused (once deleted, that ID is gone)

## Validation Rules

### Task ID Validation

| Rule | Condition | Error |
|------|-----------|--------|
| Must be integer | Input can be parsed as `int` | `ValueError` |
| Must be positive | `task_id > 0` | `ValueError` |
| Must exist | `task.id == task_id` found in `_tasks` | `ValueError` |

### User Confirmation Validation

| Rule | Condition | Error |
|------|-----------|--------|
| Must confirm before deletion | User enters 'y' or 'n' | Prompt if invalid input |
| 'n' or any non-'y' input | Aborts deletion | Returns to start |

## State Transitions

### Delete Operation Flow

```
Current Task State
        │
        ▼
┌─────────────────────┐
│ Validate task ID    │
│ exists              │
└─────────────────────┘
        │
        │ Found?
        ▼
    Yes │      No
        │         │
        ▼         ▼
┌────────────┐  ┌────────────────┐
│ Display     │  │ Return Error:  │
│ task details│  │  Task not found│
└────────────┘  └────────────────┘
        │
        ▼
┌─────────────────────┐
│ Request            │
│ confirmation        │
└─────────────────────┘
        │
        │ Confirmed?
        ▼
    Yes │      No
        │         │
        ▼         ▼
┌────────────┐  ┌────────────────┐
│ Remove task  │  │ Return to start │
│ from _tasks  │  └─────────────────┘
└────────────┘
        │
        ▼
┌─────────────────────┐
│ Display success    │
│ message           │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Ask if user      │
│ wants to delete    │
│ another task       │
└─────────────────────┘
```

### State Change Example

**Before**:
```python
_tasks = [
    Task(id=1, title="Task 1", description="Description", completed=False),
    Task(id=2, title="Task 2", description="", completed=True),
    Task(id=3, title="Task 3", description="Description", completed=False),
]
```

**After** (delete task ID 2):
```python
_tasks = [
    Task(id=1, title="Task 1", description="Description", completed=False),
    Task(id=3, title="Task 3", description="Description", completed=False),
]
```

**Storage Update**:
```python
# Find and remove task by ID
index = _find_task_index(task_id=2)
del _tasks[index]
# Or using pop/pop
_tasks.pop(index)
```

## Data Integrity

### Invariants

1. **Uniqueness**: Task IDs are unique and never reused
2. **Complete Removal**: Deleted tasks are removed from `_tasks` list entirely
3. **Isolation**: Deleting one task does not affect other tasks in `_tasks`
4. **ID Non-Reuse**: Deleted task IDs are never assigned to new tasks
5. **No Mutation**: Other tasks' attributes remain unchanged during deletion

### Constraints

- All tasks in `_tasks` have unique `id` values
- `id` values are sequential starting from 1
- Deleted IDs are never reused
- No external dependencies for data integrity (in-memory only)

## Relationships

### Entity Relationships

```
Task
│
├─ id: int (unique identifier)
├─ title: str
├─ description: str
└─ completed: bool

Task Store (_tasks: list[Task])
│
└─ Contains: [Task, Task, Task, ...]
```

### Module Dependencies

```
add.py
│
├─ Defines: Task dataclass
├─ Defines: _tasks (storage)
├─ Defines: _next_id (counter)
└─ Exports: Task, _tasks

view.py (consumer)
│
└─ Imports: _tasks, Task from add.py

update.py (consumer)
│
└─ Imports: _tasks, Task from add.py

delete.py (consumer) [NEW]
│
└─ Imports: _tasks, Task from add.py
```

## Testing Considerations

### Test Data

Example test tasks for deletion:
```python
task1 = Task(id=1, title="Task 1", description="Description", completed=False)
task2 = Task(id=2, title="Task 2", description="", completed=True)
task3 = Task(id=3, title="Task 3", description="Description", completed=False)
```

### Edge Cases

1. Delete task from empty `_tasks` list
2. Delete task with non-existent ID
3. Delete with non-numeric ID input
4. Delete with negative ID input
5. Delete already-deleted task ID
6. User cancels deletion after seeing task details
7. User provides empty or whitespace-only task ID
8. Delete the last remaining task

## Summary

The Delete Task feature reuses existing Task dataclass from Spec 1. The key design considerations are:
- Frozen dataclass - tasks are immutable objects
- List removal - O(n) deletion by index after ID lookup
- Explicit validation for task ID existence before deletion
- Confirmation required before deletion to prevent accidents
- Deleted task IDs are never reused
- Support for user cancellation and error recovery

No new entities are required. All validation rules and state transitions are derived from existing Task model.

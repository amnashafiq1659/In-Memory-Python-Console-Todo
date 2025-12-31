# Data Model: Update Task

**Feature**: Update Task
**Date**: 2025-12-31
**Status**: Complete

## Overview

The Update Task feature reuses the existing `Task` dataclass from Spec 1 without modification. This document describes the entity structure, validation rules, and state transitions for update operations.

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
| `id` | int | Read-only | Unique identifier for the task | Auto-incremented by add.py, positive integer |
| `title` | str | Updatable | Title/name of the task | Required, non-empty, non-whitespace |
| `description` | str | Updatable | Optional description of the task | Optional, can be empty string |
| `completed` | bool | Read-only | Completion status | True if completed, False otherwise |

**Note**: The `frozen=True` parameter makes Task instances immutable, which means updates require creating new Task instances.

## Storage Model

### In-Memory Storage

Tasks are stored in a global list:

```python
_tasks: list[Task] = []
```

**Location**: `src/add.py:4`

### Storage Characteristics

- **Type**: List of Task objects
- **Scope**: Global to `add.py` module, imported by `view.py` and `update.py`
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
- Read-only for update operations

## Validation Rules

### Task ID Validation

| Rule | Condition | Error |
|------|-----------|--------|
| Must be integer | Input can be parsed as `int` | `ValueError` |
| Must be positive | `task_id > 0` | `ValueError` |
| Must exist | `task.id == task_id` found in `_tasks` | `ValueError` |

### Title Validation

| Rule | Condition | Error |
|------|-----------|--------|
| Cannot be empty | `len(title) > 0` | `ValueError` |
| Cannot be whitespace | `not title.isspace()` | `ValueError` |
| **Note**: Empty string is allowed to skip title update |

### Description Validation

| Rule | Condition | Error |
|------|-----------|--------|
| Optional | Can be empty string or None | N/A |
| **Note**: No validation applied |

## State Transitions

### Update Operation Flow

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
│ Validate   │  │ Return Error:  │
│ inputs     │  │ Task not found│
└────────────┘  └────────────────┘
        │
        ▼
┌─────────────────────┐
│ Create new Task      │
│ instance with       │
│ modified fields     │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Replace in _tasks   │
│ at same index      │
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│ Return updated      │
│ Task               │
└─────────────────────┘
```

### State Change Example

**Before**:
```python
Task(
    id=1,
    title="Buy groceries",
    description="Milk, eggs",
    completed=False
)
```

**After** (update title only):
```python
Task(
    id=1,
    title="Buy weekly groceries",  # Changed
    description="Milk, eggs",     # Unchanged
    completed=False                # Unchanged
)
```

**Storage Update**:
```python
# Find task by ID and replace
index = _find_task_index(task_id=1)
_tasks[index] = new_task
```

## Data Integrity

### Invariants

1. **Uniqueness**: Task IDs are unique and never reused
2. **Immutability**: Task instances are never modified directly (frozen dataclass)
3. **Preservation**: `completed` status is never changed during title/description updates
4. **Consistency**: Updates replace Task objects at the same index in `_tasks`

### Constraints

- All tasks in `_tasks` have unique `id` values
- `id` values are sequential starting from 1
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

update.py (consumer) [NEW]
│
└─ Imports: _tasks, Task from add.py
```

## Testing Considerations

### Test Data

Example test tasks for validation:
```python
task1 = Task(id=1, title="Task 1", description="Description", completed=False)
task2 = Task(id=2, title="Task 2", description="", completed=True)
task3 = Task(id=3, title="Task 3", description=None, completed=False)
```

### Edge Cases

1. Update with empty title/description (should skip)
2. Update when no tasks exist in `_tasks`
3. Update with non-existent task ID
4. Update task that was already updated in same session
5. Update with whitespace-only title (should error)
6. Update with whitespace-only description (allowed)

## Summary

The Update Task feature reuses the existing Task dataclass from Spec 1. The key design considerations are:
- Frozen dataclass requires creating new instances for updates
- Sequential search in `_tasks` list for task lookup
- Explicit validation for task ID existence
- Preservation of `completed` field during title/description updates
- Support for partial updates (title only, description only, or both)

No new entities are required. All validation rules and state transitions are derived from existing Task model.

# Function Interface Contracts: Sort Tasks

**Feature**: Sort Tasks (007-sort-tasks)
**Date**: 2026-01-01

## Overview

This document defines the public function interfaces for the sort.py module. All functions are pure (no side effects) except `display_tasks` and `run_sort_ui` which print to console.

## Public Functions

### 1. sort_by_title

Sorts tasks alphabetically by title (A-Z) using case-insensitive comparison.

**Signature**:
```python
def sort_by_title(tasks: list[Task]) -> list[Task]
```

**Parameters**:
| Name | Type | Description |
|------|------|-------------|
| `tasks` | `list[Task]` | List of tasks to sort (not modified) |

**Returns**:
- Type: `list[Task]`
- Description: New list with tasks sorted by title
- Notes: Returns shallow copy with new order, original list unchanged

**Behavior**:
- Uses case-insensitive comparison (`title.lower()`)
- Stable sort (preserves original order for identical titles)
- Handles empty list (returns empty list)
- Handles special characters via Unicode collation

**Error Conditions**:
- None (pure function, no exceptions)

**Complexity**:
- Time: O(n log n)
- Space: O(n)

**Examples**:
```python
tasks = [Task(1, "Zebra", "..."), Task(2, "alpha", "..."), Task(3, "Beta", "...")]
sorted_tasks = sort_by_title(tasks)
# Result: [Task(2, "alpha", "..."), Task(3, "Beta", "..."), Task(1, "Zebra", "...")]
```

---

### 2. sort_by_priority

Sorts tasks by priority in order: High → Medium → Low.

**Signature**:
```python
def sort_by_priority(tasks: list[Task]) -> list[Task]
```

**Parameters**:
| Name | Type | Description |
|------|------|-------------|
| `tasks` | `list[Task]` | List of tasks to sort (not modified) |

**Returns**:
- Type: `list[Task]`
- Description: New list with tasks sorted by priority
- Notes: All High tasks first, then Medium, then Low

**Behavior**:
- Priority mapping: High (0) < Medium (1) < Low (2)
- Stable sort (preserves original order within same priority)
- Handles unexpected priority values (treated as Medium)
- Handles empty list (returns empty list)

**Error Conditions**:
- None (pure function, no exceptions)

**Complexity**:
- Time: O(n log n)
- Space: O(n)

**Examples**:
```python
tasks = [
    Task(1, "Task A", priority="Low"),
    Task(2, "Task B", priority="High"),
    Task(3, "Task C", priority="Medium")
]
sorted_tasks = sort_by_priority(tasks)
# Result: [High tasks..., Medium tasks..., Low tasks...]
```

---

### 3. sort_by_due_date

Sorts tasks by due date in ascending order (earliest to latest).

**Signature**:
```python
def sort_by_due_date(tasks: list[Task]) -> list[Task]
```

**Parameters**:
| Name | Type | Description |
|------|------|-------------|
| `tasks` | `list[Task]` | List of tasks to sort (not modified) |

**Returns**:
- Type: `list[Task]`
- Description: New list with tasks sorted by due date
- Notes: Tasks with due dates appear first, followed by tasks without due dates

**Behavior**:
- Due date format assumed: ISO 8601 (YYYY-MM-DD)
- String comparison for chronological ordering
- `None` due dates placed after all dated tasks
- Stable sort (preserves original order for identical dates)
- Handles empty list (returns empty list)

**Error Conditions**:
- None (pure function, no exceptions)

**Complexity**:
- Time: O(n log n)
- Space: O(n)

**Examples**:
```python
tasks = [
    Task(1, "Task A", due_date="2026-01-20"),
    Task(2, "Task B", due_date="2026-01-10"),
    Task(3, "Task C", due_date=None)
]
sorted_tasks = sort_by_due_date(tasks)
# Result: [Task(2, "Task B", due_date="2026-01-10"),
#          Task(1, "Task A", due_date="2026-01-20"),
#          Task(3, "Task C", due_date=None)]
```

---

### 4. display_tasks

Displays tasks in a user-friendly console format with color coding.

**Signature**:
```python
def display_tasks(tasks: list[Task]) -> None
```

**Parameters**:
| Name | Type | Description |
|------|------|-------------|
| `tasks` | `list[Task]` | List of tasks to display (not modified) |

**Returns**:
- Type: `None`
- Description: Prints to console, no return value

**Behavior**:
- Displays each task with:
  - Status indicator: `[X]` (completed) or `[ ]` (incomplete)
  - Task ID and title
  - Description
  - Priority with color coding (Red: High, Orange: Medium, Blue: Low)
  - Category and due date (if present)
- Handles empty list (displays message from FR-008)
- Uses `Colors` class from `add.py` for color codes

**Error Conditions**:
- None (prints to console, no exceptions)

**Complexity**:
- Time: O(n)
- Space: O(1)

**Examples**:
```python
tasks = [Task(1, "Buy groceries", "Milk and eggs", False, "High")]
display_tasks(tasks)
# Output: [ ] [1] Buy groceries
#         Desc: Milk and eggs
#         Priority: High | Category: General
```

---

### 5. run_sort_ui

Interactive console UI for selecting and executing sorting options.

**Signature**:
```python
def run_sort_ui(tasks: list[Task]) -> None
```

**Parameters**:
| Name | Type | Description |
|------|------|-------------|
| `tasks` | `list[Task]` | List of tasks to sort (not modified) |

**Returns**:
- Type: `None`
- Description: Displays menu and sorted results, then returns

**Behavior**:
- Displays menu with options:
  1. Sort by Title
  2. Sort by Priority
  3. Sort by Due Date
- Prompts user for selection (1, 2, or 3)
- Executes corresponding sort function
- Displays sorted results
- Returns control to caller after display

**Error Conditions**:
- Invalid input: Reprompts user
- No tasks: Displays message and returns early

**Complexity**:
- Time: O(n log n) for sorting + O(n) for display
- Space: O(n) for sorted copy

**Examples**:
```python
tasks = [...]
run_sort_ui(tasks)
# Displays: "1. Sort by Title"
#           "2. Sort by Priority"
#           "3. Sort by Due Date"
#           "Enter your choice: "
# User enters: "1"
# Displays sorted tasks, then returns
```

---

## Internal Constants

### PRIORITY_ORDER

Mapping of priority strings to numeric values for sorting.

**Signature**:
```python
PRIORITY_ORDER: dict[str, int] = {"High": 0, "Medium": 1, "Low": 2}
```

**Purpose**: Used as key function for priority sorting

---

## Test Scenarios

### Unit Test Cases

1. **Empty list**: `[]` → returns empty list or displays message
2. **Single element**: `[task1]` → returns `[task1]` unchanged
3. **All identical values**: All same title/priority/date
4. **Mixed values**: Normal case with variety
5. **Edge cases**: None values, special characters, unexpected priorities

### Integration Test Cases

1. **UI flow**: Select option → sort → display → return
2. **Multi-sort**: Sort by title, then by priority, verify independence
3. **Empty handling**: No tasks → message → return

---

## Compliance

All contracts satisfy:
- ✅ FR-001 through FR-012 from spec.md
- ✅ Single file constraint (sort.py)
- ✅ No external libraries
- ✅ Non-destructive sorting (returns new list)
- ✅ No memory ownership (accepts parameter, returns result)

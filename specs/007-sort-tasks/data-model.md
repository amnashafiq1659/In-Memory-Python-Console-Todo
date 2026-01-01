# Data Model: Sort Tasks Feature

**Feature**: Sort Tasks (007-sort-tasks)
**Date**: 2026-01-01

## Overview

This feature does NOT introduce new data models. It works with the existing `Task` dataclass defined in `add.py` and performs non-destructive sorting for display purposes.

## Existing Entity: Task

**Location**: `src/add.py:8-15`

### Definition

```python
@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    completed: bool
    priority: str = "Medium"  # High / Medium / Low
    category: str = "General"  # user-defined label
    due_date: str | None = None  # optional value (string-based)
```

### Fields Used for Sorting

| Field | Type | Used For | Notes |
|-------|------|----------|-------|
| `title` | `str` | Title sorting | Case-insensitive alphabetical order (A-Z) |
| `priority` | `str` | Priority sorting | Enum values: "High", "Medium", "Low" |
| `due_date` | `str | None` | Due date sorting | ISO format (YYYY-MM-DD), None treated specially |
| `completed` | `bool` | Display only | Not used for sorting, only for status indicator |
| `id` | `int` | Display only | Not used for sorting |

### Validation Rules

#### Title Field
- **Type**: Non-empty string
- **Constraints**: Must not be empty or whitespace (validated in add.py)
- **Case Sensitivity**: Stored with original case, sorted case-insensitively
- **Special Characters**: Supported via standard Unicode handling

#### Priority Field
- **Type**: String
- **Valid Values**: "High", "Medium", "Low"
- **Default**: "Medium"
- **Invalid Handling**: Treated as "Medium" if unexpected value appears

#### Due Date Field
- **Type**: Optional string (`str | None`)
- **Format**: ISO 8601 (YYYY-MM-DD) for chronological comparison
- **Null Handling**: `None` values placed after all dated tasks
- **Invalid Formats**: Treated as string, may sort incorrectly (documented limitation)

## Sorting Behavior

### Sort Keys

Each sorting criterion uses a computed sort key:

1. **Title Sort Key**: `task.title.lower()`
   - Type: `str`
   - Comparison: Standard string comparison (Unicode-aware)

2. **Priority Sort Key**: `PRIORITY_ORDER[task.priority]`
   - Type: `int`
   - Mapping: `{"High": 0, "Medium": 1, "Low": 2}`
   - Default: `1` (Medium) for unexpected values

3. **Due Date Sort Key**: Two-tiered key
   - Type: Tuple `(int, str)`
   - Structure: `(0, task.due_date)` for tasks with due dates
   - Structure: `(1, "")` for tasks without due dates
   - Effect: All dated tasks (tier 0) before non-dated (tier 1)

### Stability

- **Algorithm**: Python's Timsort (stable sorting)
- **Behavior**: When sort keys are equal, original order is preserved
- **Requirement**: Satisfies FR-010 ("maintain relative order")

## Data Flow

```
Input (from caller)
    ↓
task_list: list[Task]
    ↓
┌─────────────────────┐
│  Sort Functions     │  (pure, no side effects)
│  (sort_by_title)   │  → Returns: list[Task] (new)
│  (sort_by_priority)│  → Returns: list[Task] (new)
│  (sort_by_date)    │  → Returns: list[Task] (new)
└─────────────────────┘
    ↓
sorted_tasks: list[Task]
    ↓
┌─────────────────────┐
│  Display Functions  │  (uses Colors from add.py)
│  (display_tasks)   │  → Returns: None (prints to console)
└─────────────────────┘
    ↓
Output (console)
```

## Constraints

### Immutability

- **Task Object**: Frozen dataclass (`@dataclass(frozen=True)`)
- **Original List**: Never modified (FR-009)
- **Sorted List**: New instance created by `sorted()`

### Memory

- **Ownership**: Caller maintains ownership of task list
- **Lifetime**: Sorted list exists only during display
- **No Persistence**: Sorting is transient, display-only

### Dependencies

- **From `add.py`**:
  - `Task` dataclass (read-only access)
  - `Colors` class (for display formatting)

## Edge Cases

### Empty List
- **Input**: `[]`
- **Output**: Empty list or early exit with message (FR-008)
- **Sorting**: Not attempted (early return)

### Single Element
- **Input**: `[task1]`
- **Output**: `[task1]` (unchanged order)
- **Complexity**: O(1) effectively

### All Identical Values
- **Input**: All tasks have same title/priority/due date
- **Output**: Original order preserved (stable sort)

### Missing Optional Fields
- **Due Date**: `None` values sorted last
- **Priority**: Unexpected values treated as "Medium"

### Unicode Characters
- **Titles**: Standard Unicode collation (locale-dependent)
- **Case Handling**: Lowercase for comparison, original for display

## No New Entities Required

This feature extends existing functionality without introducing:
- New data classes or structures
- Database schemas or migrations
- API models or DTOs
- Configuration or state management

All sorting operations are pure functions that transform the existing `Task` entity.

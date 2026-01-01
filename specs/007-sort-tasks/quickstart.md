# Quick Start Guide: Sort Tasks

**Feature**: Sort Tasks (007-sort-tasks)
**Date**: 2026-01-01

## Overview

This guide explains how to use the task sorting functionality once implemented. The sort feature provides three sorting criteria and displays results in a user-friendly console format.

## Prerequisites

- Python 3.13+ installed
- Task list exists in memory (created via `add.py`)
- `sort.py` module is available in `src/` directory

## Basic Usage

### Running Sort UI

From your main menu or script:

```python
from add import _tasks
from sort import run_sort_ui

# Run sort interface
run_sort_ui(_tasks)
```

### Interactive Flow

1. **Display Menu**:
   ```
   === Sort Tasks ===

   1. Sort by Title
   2. Sort by Priority
   3. Sort by Due Date

   Enter your choice (1-3):
   ```

2. **Select Sorting Option**:
   - Enter `1` to sort by Title (A-Z, case-insensitive)
   - Enter `2` to sort by Priority (High → Medium → Low)
   - Enter `3` to sort by Due Date (earliest → latest)

3. **View Results**:
   - Tasks display with color-coded status and priority indicators
   - Empty list shows message: "No tasks found. Add tasks using add task functionality."
   - Control returns to caller after display

## Examples

### Example 1: Sort by Title

**Input Tasks**:
- Task 3: "Zebra task" (Medium)
- Task 1: "alpha task" (High)
- Task 2: "Beta task" (Low)

**Result**:
```
[ ] [2] Beta task
    Desc: ...
    Priority: Low | Category: General

[ ] [1] alpha task
    Desc: ...
    Priority: High | Category: General

[ ] [3] Zebra task
    Desc: ...
    Priority: Medium | Category: General

Total: 3 tasks
```

### Example 2: Sort by Priority

**Input Tasks**:
- Task 1: "Task A" (Low)
- Task 2: "Task B" (High)
- Task 3: "Task C" (Medium)

**Result**:
```
[ ] [2] Task B
    Desc: ...
    Priority: High | Category: General

[ ] [3] Task C
    Desc: ...
    Priority: Medium | Category: General

[ ] [1] Task A
    Desc: ...
    Priority: Low | Category: General

Total: 3 tasks
```

### Example 3: Sort by Due Date

**Input Tasks**:
- Task 1: "Task A" (due: 2026-01-20)
- Task 2: "Task B" (due: 2026-01-10)
- Task 3: "Task C" (no due date)

**Result**:
```
[ ] [2] Task B
    Desc: ...
    Priority: Medium | Category: General | Due: 2026-01-10

[ ] [1] Task A
    Desc: ...
    Priority: Medium | Category: General | Due: 2026-01-20

[ ] [3] Task C
    Desc: ...
    Priority: Medium | Category: General

Total: 3 tasks
```

## Color Coding

### Status Indicators
- `[X]` = Completed task (green)
- `[ ]` = Incomplete task (yellow)

### Priority Colors
- **High** = Red text
- **Medium** = Orange text
- **Low** = Blue text

### Additional Attributes
- **Category** = Pink text
- **Due Date** = Purple text

## API Reference

### Public Functions

#### `run_sort_ui(tasks: list[Task]) -> None`
Interactive UI for sorting and displaying tasks.

#### `sort_by_title(tasks: list[Task]) -> list[Task]`
Returns new list sorted alphabetically by title.

#### `sort_by_priority(tasks: list[Task]) -> list[Task]`
Returns new list sorted by priority (High → Medium → Low).

#### `sort_by_due_date(tasks: list[Task]) -> list[Task]`
Returns new list sorted by due date (earliest → latest).

#### `display_tasks(tasks: list[Task]) -> None`
Displays tasks in formatted console output.

## Direct Function Usage

You can also use sorting functions directly without the UI:

```python
from add import _tasks
from sort import sort_by_title, display_tasks

# Sort by title and display
sorted_tasks = sort_by_title(_tasks)
display_tasks(sorted_tasks)
```

## Integration Example

```python
from add import _tasks
from sort import run_sort_ui, sort_by_due_date

# Interactive sort
run_sort_ui(_tasks)

# Or programmatic sort
urgent_tasks = sort_by_due_date(_tasks)
display_tasks(urgent_tasks)
```

## Error Handling

The sorting functions handle edge cases gracefully:

- **Empty list**: Displays message, no errors
- **Single task**: Returns unchanged list
- **Missing due dates**: Placed after all dated tasks
- **Unexpected priority values**: Treated as "Medium"
- **Identical sort values**: Original order preserved (stable sort)

## Notes

- Sorting is **non-destructive**: Original task list is never modified
- Sorting is **transient**: Sorted list exists only during display
- **Performance**: All sorts complete in under 1 second for typical task lists
- **Case-insensitive**: Title sorting ignores case ("alpha" and "Alpha" sort together)

## Next Steps

After sorting, you can:
- Return to main menu
- Sort by a different criterion
- Add, edit, or delete tasks via other features
- Exit the application

## Troubleshooting

### "No tasks found" message
- Ensure you've added tasks using the add task functionality first
- Check that `_tasks` list is not empty before calling sort functions

### Tasks not in expected order
- Verify due date format is ISO 8601 (YYYY-MM-DD)
- Check that priority values are "High", "Medium", or "Low"
- Confirm no external libraries are interfering with sorting

### Colors not displaying correctly
- Ensure your terminal supports ANSI color codes
- Windows users: Enable virtual terminal processing if needed

## Support

For issues or questions:
- Check the specification: `specs/007-sort-tasks/spec.md`
- Review implementation plan: `specs/007-sort-tasks/plan.md`
- See function contracts: `specs/007-sort-tasks/contracts/function-interfaces.md`

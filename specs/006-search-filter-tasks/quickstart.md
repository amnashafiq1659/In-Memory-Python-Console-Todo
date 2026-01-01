# Quickstart: Search & Filter Tasks

**Feature**: 006-search-filter-tasks
**Purpose**: Enable users to find and organize tasks through search and filter functionality

## Overview

This feature adds search and filter capabilities to the todo console application. Users can:
- Search tasks by keyword (matches title or description)
- Filter by completion status (complete/incomplete)
- Filter by priority (High/Medium/Low)
- Filter by category/tag

All operations are case-insensitive and maintain existing color conventions.

## Module Structure

### Single File: `src/search.py`

```python
# Imports
from add import _tasks, Task
from typing import List, Optional

# Core Functions
def search_tasks(keyword: str) -> List[Task]
def filter_by_status(status: str) -> List[Task]
def filter_by_priority(priority: str) -> List[Task]
def filter_by_category(category: str) -> List[Task]
def search_and_filter(...) -> List[Task]
def display_search_results(tasks: List[Task]) -> None

# Console UI
def run_search_ui() -> None

# Entry Point
if __name__ == "__main__":
    run_search_ui()
```

## Integration Points

### Read from Existing Module
```python
# Import shared task storage (read-only)
from add import _tasks, Task
```

### Reuse Colors
```python
# Use same color coding as view.py
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    ORANGE = '\033[38;5;208m'
    BRIGHT_YELLOW = '\033[93;1m'
    DIM_CYAN = '\033[96;2m'
    PINK = '\033[38;5;206m'
```

## Usage Examples

### Example 1: Search by Keyword
```python
# Find all tasks containing "project"
results = search_tasks("project")
display_search_results(results)
```

### Example 2: Filter by Status
```python
# Show only incomplete tasks
results = filter_by_status("incomplete")
display_search_results(results)
```

### Example 3: Combined Search + Filter
```python
# Search for "project" in High priority tasks only
results = search_and_filter(
    keyword="project",
    priority="High",
    status=None,
    category=None
)
display_search_results(results)
```

## Key Implementation Details

### Case-Insensitive Matching
```python
keyword_lower = keyword.lower()
if (keyword_lower in task.title.lower() or
    keyword_lower in task.description.lower()):
    results.append(task)
```

### Color Coding Display
```python
# Priority colors
if task.priority == "High":
    color = Colors.RED
elif task.priority == "Medium":
    color = Colors.ORANGE
else:  # Low
    color = Colors.BLUE
```

### Input Validation
```python
valid_priorities = ["High", "Medium", "Low"]
if priority not in valid_priorities:
    print(f"Error: Priority must be one of: {valid_priorities}")
    return
```

## Console Flow

```
=== Search & Filter Tasks ===

Enter keyword (or press Enter to skip):
> project

Apply filters? (y/n):
> y

Filter by status? (complete/incomplete/skip):
> incomplete

Filter by priority? (High/Medium/Low/skip):
> High

Filter by category? (or press Enter to skip):
> Work

=== Search Results ===

[ ] [1] Complete project
    Desc: Finish the todo app
    Priority: High | Category: Work

Total: 1 task
```

## Error Handling

### No Tasks Available
```
No tasks found in memory. Add tasks first using Add Task functionality.
```

### No Matching Results
```
No tasks match your search criteria.
```

### Invalid Filter Value
```
Error: Priority must be one of: ['High', 'Medium', 'Low']
Please try again.
```

## Testing Checklist

- [ ] Search by keyword finds tasks in title
- [ ] Search by keyword finds tasks in description
- [ ] Search is case-insensitive
- [ ] Filter by status (complete) works
- [ ] Filter by status (incomplete) works
- [ ] Filter by priority works (High/Medium/Low)
- [ ] Filter by category works
- [ ] Empty search shows all tasks
- [ ] No tasks message displays correctly
- [ ] No results message displays correctly
- [ ] Invalid filter values show error message
- [ ] Color coding matches existing conventions

## Notes

- **No Persistence**: All search/filter operations are ephemeral (in-memory)
- **Read-Only**: Never modifies the `_tasks` list
- **Backward Compatible**: Works with existing Task data structure
- **Console Only**: No GUI or web interface components

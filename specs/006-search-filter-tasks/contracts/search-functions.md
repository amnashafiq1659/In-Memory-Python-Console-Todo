# Search & Filter Function Contracts

**Feature**: 006-search-filter-tasks
**Date**: 2025-12-31
**Type**: Internal Module Contracts

## Function Contracts

### 1. search_tasks(keyword: str) -> List[Task]

**Purpose**: Find tasks matching a keyword in title or description.

**Input Parameters**:
| Parameter | Type | Required | Description | Constraints |
|-----------|--------|-----------|---------------|--------------|
| keyword   | str    | Yes       | Search term    | Case-insensitive matching applied |

**Returns**:
- `List[Task]`: All tasks where keyword appears in title OR description

**Behavior**:
1. Convert keyword to lowercase for case-insensitive matching
2. Empty keyword returns all tasks (no filter applied)
3. Matches against both `task.title` and `task.description`
4. Uses OR logic: match if keyword in title OR description

**Error Conditions**: None (returns empty list if no matches)

**Examples**:
```python
# Returns tasks with "project" in title or description
search_tasks("project")

# Returns all tasks (empty keyword)
search_tasks("")

# Case-insensitive
search_tasks("PROJECT") # matches "project"
```

---

### 2. filter_by_status(status: str) -> List[Task]

**Purpose**: Filter tasks by completion status.

**Input Parameters**:
| Parameter | Type | Required | Description | Constraints |
|-----------|--------|-----------|---------------|--------------|
| status    | str    | Yes       | Filter value   | Must be "complete" or "incomplete" (case-insensitive) |

**Returns**:
- `List[Task]`: Tasks where `task.completed` matches status value

**Behavior**:
1. Convert status to lowercase for validation
2. "complete" matches `task.completed == True`
3. "incomplete" matches `task.completed == False`
4. Invalid status raises ValueError

**Error Conditions**:
- `ValueError`: If status is not "complete" or "incomplete"

**Examples**:
```python
# Returns only completed tasks
filter_by_status("complete")

# Returns only incomplete tasks
filter_by_status("incomplete")

# Case-insensitive
filter_by_status("COMPLETE") # matches "complete"
```

---

### 3. filter_by_priority(priority: str) -> List[Task]

**Purpose**: Filter tasks by priority level.

**Input Parameters**:
| Parameter | Type   | Required | Description | Constraints |
|-----------|--------|-----------|---------------|--------------|
| priority  | str    | Yes       | Priority level | Must be "High", "Medium", or "Low" (case-insensitive) |

**Returns**:
- `List[Task]`: Tasks where `task.priority` matches priority value

**Behavior**:
1. Convert priority to lowercase for validation and matching
2. Exact match against `task.priority` field
3. Invalid priority raises ValueError

**Error Conditions**:
- `ValueError`: If priority is not "High", "Medium", or "Low"

**Examples**:
```python
# Returns only High priority tasks
filter_by_priority("High")

# Returns Low priority tasks
filter_by_priority("low")

# Case-insensitive
filter_by_priority("MEDIUM") # matches "Medium"
```

---

### 4. filter_by_category(category: str) -> List[Task]

**Purpose**: Filter tasks by category tag.

**Input Parameters**:
| Parameter | Type | Required | Description | Constraints |
|-----------|--------|-----------|---------------|--------------|
| category  | str    | Yes       | Category name  | Case-insensitive matching |

**Returns**:
- `List[Task]`: Tasks where `task.category` matches category value

**Behavior**:
1. Convert category to lowercase for matching
2. Exact match against `task.category` field
3. Empty category raises ValueError

**Error Conditions**:
- `ValueError`: If category is empty string

**Examples**:
```python
# Returns all Work tasks
filter_by_category("Work")

# Returns Personal tasks
filter_by_category("personal")

# Case-insensitive
filter_by_category("HOME") # matches "Home"
```

---

### 5. search_and_filter(keyword: str, status: Optional[str], priority: Optional[str], category: Optional[str]) -> List[Task]

**Purpose**: Combine search and filter operations to find tasks matching all criteria.

**Input Parameters**:
| Parameter | Type        | Required | Description | Constraints |
|-----------|-------------|-----------|---------------|--------------|
| keyword   | str         | No        | Search term    | Case-insensitive, empty = no search |
| status    | Optional[str] | No        | Status filter   | "complete" or "incomplete" or None |
| priority  | Optional[str] | No        | Priority filter | "High", "Medium", "Low" or None |
| category  | Optional[str] | No        | Category filter | Non-empty string or None |

**Returns**:
- `List[Task]`: Tasks matching all provided criteria (AND logic)

**Behavior**:
1. If keyword provided, perform search first
2. Apply each active filter sequentially (if provided)
3. Use AND logic: task must satisfy all criteria
4. Returns empty list if no tasks match
5. Validation occurs before filtering

**Error Conditions**:
- `ValueError`: If any provided filter value is invalid

**Examples**:
```python
# Search "project" with High priority
search_and_filter(keyword="project", priority="High")

# Filter by incomplete only
search_and_filter(status="incomplete")

# Combined search + multiple filters
search_and_filter(
    keyword="report",
    status="incomplete",
    priority="High",
    category="Work"
)
```

---

### 6. display_search_results(tasks: List[Task]) -> None

**Purpose**: Display filtered tasks with color coding to console.

**Input Parameters**:
| Parameter | Type        | Required | Description |
|-----------|-------------|-----------|---------------|
| tasks     | List[Task] | Yes       | Tasks to display |

**Returns**: None

**Behavior**:
1. If tasks list is empty, show "No matching tasks" message
2. Display header with task count
3. For each task:
   - Show completion status indicator (colored)
   - Show task ID and title
   - Show description (dimmed)
   - Show priority (color-coded)
   - Show category (pink)
   - Show due date (purple) if available
4. Maintain existing color conventions from view.py

**Error Conditions**: None

---

### 7. run_search_ui() -> None

**Purpose**: Interactive console interface for search and filter operations.

**Input Parameters**: None

**Returns**: None

**Behavior**:
1. Display header
2. Prompt for keyword (optional, press Enter to skip)
3. Prompt for filters (optional, can skip each):
   - Status filter (complete/incomplete/skip)
   - Priority filter (High/Medium/Low/skip)
   - Category filter (or press Enter to skip)
4. Validate all inputs before applying
5. Call `search_and_filter()` with user inputs
6. Call `display_search_results()` with results
7. Allow user to continue or exit

**Error Conditions**:
- Displays error message and re-prompts on invalid input

---

## Data Structures

### Task (from add.py)
```python
@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool
    priority: str        # "High" | "Medium" | "Low"
    category: str
    due_date: str | None
```

## Color Constants

```python
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'        # High priority, errors
    GREEN = '\033[92m'      # Complete status
    YELLOW = '\033[93m'     # Incomplete status
    BLUE = '\033[94m'       # Low priority
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ORANGE = '\033[38;5;208m'  # Medium priority
    BRIGHT_YELLOW = '\033[93;1m'  # Task titles
    DIM_CYAN = '\033[96;2m'  # Descriptions
    PINK = '\033[38;5;206m'  # Categories
```

## Validation Rules

### Status Values
- Valid: "complete", "incomplete" (case-insensitive)
- Error: `ValueError("Status must be 'complete' or 'incomplete'")`

### Priority Values
- Valid: "High", "Medium", "Low" (case-insensitive)
- Error: `ValueError("Priority must be one of: ['High', 'Medium', 'Low']")`

### Category Values
- Valid: Non-empty string
- Error: `ValueError("Category cannot be empty")`

### Keyword Values
- Valid: Any string (including empty)
- Behavior: Empty keyword treated as no search filter

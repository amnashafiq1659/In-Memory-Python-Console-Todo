# Data Model: Search & Filter Tasks

**Feature**: 006-search-filter-tasks
**Date**: 2025-12-31

## Entities

### Search Query
**Purpose**: User-provided keyword to match against task attributes

**Fields**:
- `keyword: str` - The search term to match (case-insensitive)
- `is_empty: bool` - Whether the keyword is empty string

**Constraints**:
- Cannot exceed reasonable console input length (handled by system)
- Case-insensitive matching applied

**Relationships**:
- Matches against: `Task.title` and `Task.description`

---

### Filter Criteria
**Purpose**: Set of conditions used to narrow task results

**Fields**:
- `status_filter: str | None` - "complete" or "incomplete" or None (no filter)
- `priority_filter: str | None` - "High", "Medium", "Low" or None (no filter)
- `category_filter: str | None` - Category name or None (no filter)

**Constraints**:
- Only one value per filter type at a time
- Case-insensitive matching applied
- Values must match Task enum/string values

**Relationships**:
- Filters: `Task.completed`, `Task.priority`, `Task.category`

---

### Search Result
**Purpose**: Subset of tasks matching provided search and filter criteria

**Fields**:
- `matching_tasks: List[Task]` - Tasks that satisfy all search/filter criteria
- `count: int` - Number of matching tasks
- `is_empty: bool` - Whether no tasks matched

**Constraints**:
- Read-only: Never modifies original task data
- AND logic: Must satisfy all provided criteria (search + any filters)
- Preserves original task order from `_tasks` list

**Relationships**:
- Derived from: `_tasks` list (shared in-memory storage)

---

## Task Entity (Reference)

**Purpose**: Core data entity representing a todo task (from add.py)

**Fields**:
- `id: int` - Unique identifier (read-only for search)
- `title: str` - Task name (searchable field)
- `description: str` - Task details (searchable field)
- `completed: bool` - Completion status (filterable)
- `priority: str` - Priority level: "High" | "Medium" | "Low" (filterable)
- `category: str` - User-defined category label (filterable)
- `due_date: str | None` - Optional due date (not searchable/filterable)

**Validation Rules**:
- `title` - Must not be empty (enforced by add module)
- `completed` - Boolean value
- `priority` - Must be one of: "High", "Medium", "Low"
- `category` - Non-empty string (defaults to "General")

**State Transitions** (for reference):
- `completed` transitions from `False` → `True` (mark_complete in complete.py)
- `completed` transitions from `True` → `False` (mark_incomplete in complete.py)

---

## Data Flow

```
User Input (keyword, filters)
    ↓
Search Query + Filter Criteria
    ↓
Search & Filter Functions
    ↓
Filtered Task List (read-only subset)
    ↓
Display Function (with colors)
    ↓
Console Output
```

## Key Operations

1. **Search**: Match keyword against `title` OR `description` (case-insensitive)
2. **Filter by Status**: Match `completed` == True or False
3. **Filter by Priority**: Match `priority` string (case-insensitive)
4. **Filter by Category**: Match `category` string (case-insensitive)
5. **Combined Search & Filter**: Apply search first, then apply filters (AND logic)

## Constraints Summary

- Read-only access to `_tasks` list (no modifications)
- Case-insensitive matching for all operations
- AND logic when combining search and filters
- Preserve original task ordering
- No persistence of search/filter history

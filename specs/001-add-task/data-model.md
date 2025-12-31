# Data Model: Task Model & Add Task

**Feature**: 001-add-task
**Created**: 2025-12-31

## Entity: Task

### Description
Represents a single task in the in-memory task management system.

### Fields

| Field Name | Type | Constraints | Default | Description |
|------------|------|-------------|----------|-------------|
| `id` | `int` | Required, Unique, Positive | Auto-generated (sequential) | Unique identifier for the task |
| `title` | `str` | Required, Non-empty | N/A | Title/name of the task |
| `description` | `str` | Optional, Can be empty | `""` | Detailed description of the task |
| `completed` | `bool` | Required | `False` | Task completion status |

### Validation Rules

1. **ID Generation**
   - IDs must be positive integers starting from 1
   - Each new task receives the next sequential ID
   - IDs are immutable once assigned

2. **Title Validation**
   - Title must not be empty or whitespace-only
   - Title may contain unicode characters
   - No maximum length enforced (handles 1000+ characters gracefully)

3. **Description Validation**
   - Description is optional (may be empty string)
   - May contain unicode characters
   - No maximum length enforced (handles 1000+ characters gracefully)

4. **Completion Status**
   - Must be boolean
   - Defaults to `False` for new tasks

### State Transitions

| Current State | Allowed Transition | Next State | Trigger |
|---------------|-------------------|------------|---------|
| `completed=False` | → `completed=True` | `completed=True` | Task marked complete (future feature) |
| `completed=True` | → `completed=False` | `completed=False` | Task marked incomplete (future feature) |

**Note**: State transitions are documented for future reference. This spec only covers task creation (no transitions implemented).

### Relationships

None - Tasks are independent entities with no relationships to other entities.

### Storage Model

- **In-Memory**: Python list containing Task objects
- **Lifetime**: Tasks persist only during program execution
- **Scope**: Module-level variable accessible across functions in `add.py`
- **Persistence**: None - tasks are lost when program terminates

### Example Instance

```python
Task(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False)
```

## Data Access Pattern

Since this is an in-memory system with no persistence:

1. **Collection**: Module-level list `_tasks = []`
2. **ID Counter**: Module-level integer `_next_id = 1`
3. **Add Operation**:
   - Generate new ID from `_next_id`
   - Increment `_next_id`
   - Create Task object
   - Append to `_tasks` list
   - Return new Task object

### Edge Case Handling

| Scenario | Behavior |
|----------|----------|
| Empty title | Reject with validation error |
| Empty description | Accept (optional field) |
| Very long text (1000+ chars) | Accept and store without truncation |
| Special characters/unicode | Accept and store as-is |
| Duplicate title | Allow (title is not unique constraint) |

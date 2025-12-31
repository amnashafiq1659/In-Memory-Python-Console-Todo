# Data Model: View Tasks & Status Indication

**Feature**: 002-view-tasks
**Created**: 2025-12-31

## Entity: Task (Shared with Spec 001)

### Description
Represents a single task in the in-memory task management system. This entity is defined in Spec 001 and reused by Spec 002.

### Fields

| Field Name | Type | Constraints | Default | Description |
|------------|------|-------------|----------|-------------|
| `id` | `int` | Required, Unique, Positive | Auto-generated | Unique identifier for the task |
| `title` | `str` | Required, Non-empty | N/A | Title/name of the task |
| `description` | `str` | Optional, Can be empty | `""` | Detailed description of the task |
| `completed` | `bool` | Required | Varies | Task completion status |

### Validation Rules

**Note**: Validation rules are enforced in Spec 001. Spec 002 only reads from this entity.

1. **ID Generation**
   - IDs are positive integers starting from 1
   - Each task receives the next sequential ID
   - IDs are immutable once assigned

2. **Title Validation**
   - Title must not be empty or whitespace-only
   - Title may contain unicode characters
   - No maximum length enforced

3. **Description Validation**
   - Description is optional (may be empty string)
   - May contain unicode characters
   - No maximum length enforced

4. **Completion Status**
   - Must be boolean
   - Defaults to `False` for new tasks
   - Can be modified by future features (not in Spec 002)

### State Transitions

| Current State | Allowed Transition | Next State | Trigger |
|---------------|-------------------|------------|---------|
| `completed=False` | → `completed=True` | `completed=True` | Task marked complete (future feature) |
| `completed=True` | → `completed=False` | `completed=False` | Task marked incomplete (future feature) |

**Note**: State transitions are documented for future reference. Spec 002 only displays the current state.

### Relationships

None - Tasks are independent entities with no relationships to other entities.

### Storage Model

- **In-Memory**: Python list containing Task objects (defined in Spec 001)
- **Lifetime**: Tasks persist only during program execution
- **Scope**: Module-level variable `_tasks` accessible in `src/add.py`
- **Persistence**: None - tasks are lost when program terminates
- **Access Pattern**: Spec 002 reads from `_tasks` list without modification

### Data Access Pattern

Since this is a read-only feature:

1. **Collection**: Module-level list `_tasks` (from `src/add.py`)
2. **Read Operation**:
   - Iterate over `_tasks` list
   - Display each task's fields
   - Apply status indicators based on `completed` boolean
3. **No Write Operations**: Spec 002 does not modify `_tasks` or `_next_id`

### Example Instance

```python
Task(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False)
```

### Edge Case Handling

| Scenario | Behavior |
|----------|----------|
| Empty task list | Display "No tasks found" message |
| Task with empty description | Display task with empty description field |
| Very long text (1000+ chars) | Display without truncation |
| Special characters/unicode | Display as-is |
| Multiple tasks | Display all tasks in sequential order |

## No New Entities

Spec 002 does not introduce new entities. It operates solely on the existing Task entity defined in Spec 001.

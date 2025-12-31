# Data Model: Mark Task Complete / Incomplete

**Feature**: 005-mark-complete
**Created**: 2025-12-31

## Entity: Task (Shared with Spec 001)

### Description
Represents a single task in the in-memory task management system. This entity is defined in Spec 001 and reused by Spec 005 for completion status updates.

### Fields

| Field Name | Type | Constraints | Default | Description |
|------------|------|-------------|----------|-------------|
| `id` | `int` | Required, Unique, Positive | Auto-generated | Unique identifier for the task |
| `title` | `str` | Required, Non-empty | N/A | Title/name of the task |
| `description` | `str` | Optional, Can be empty | `""` | Detailed description of the task |
| `completed` | `bool` | Required | `False` (for new tasks) | Task completion status |

### Validation Rules

**Note**: Validation rules are enforced in Spec 001. Spec 005 only modifies the `completed` field.

1. **ID Constraints**
   - IDs are positive integers starting from 1
   - Each task has a unique ID
   - IDs are immutable once assigned
   - IDs must exist in the task list to be updated

2. **Title Constraints**
   - Title must not be empty or whitespace-only
   - Title may contain unicode characters
   - No maximum length enforced
   - Title is immutable after task creation

3. **Description Constraints**
   - Description is optional (may be empty string)
   - May contain unicode characters
   - No maximum length enforced
   - Description is immutable after task creation

4. **Completion Status Constraints**
   - Must be boolean (`True` or `False`)
   - Can be toggled between states
   - Default is `False` for new tasks
   - Can be modified by user via Spec 005

### State Transitions

| Current State | Allowed Transition | Next State | Trigger (Spec 005) |
|---------------|-------------------|------------|---------------------|
| `completed=False` | → `completed=True` | `completed=True` | User marks task complete via `mark_complete()` |
| `completed=True` | → `completed=False` | `completed=False` | User marks task incomplete via `mark_incomplete()` |

### Relationships

None - Tasks are independent entities with no relationships to other entities.

### Storage Model

- **In-Memory**: Python list containing Task objects (defined in Spec 001)
- **Lifetime**: Tasks persist only during program execution
- **Scope**: Module-level variable `_tasks` accessible in `src/add.py`
- **Persistence**: None - tasks are lost when program terminates
- **Access Pattern**: Spec 005 reads from and modifies `_tasks` list to update task status

### Data Access Pattern

Spec 005 performs both read and write operations:

1. **Collection**: Module-level list `_tasks` (from `src/add.py`)
2. **Read Operation**:
   - Find task in `_tasks` list by matching `id` field
   - Return task object if found
3. **Write Operation**:
   - Create new Task object with updated `completed` field
   - Replace original task in `_tasks` list at same index
   - Since Task is `@dataclass(frozen=True)`, objects are immutable

### Example Instances

```python
# Incomplete task
Task(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=False)

# After marking complete
Task(id=1, title="Buy groceries", description="Milk, bread, eggs", completed=True)
```

### Mutation Strategy

Since Task dataclass is `@dataclass(frozen=True)`:

1. **Immutability**: Task objects cannot be modified in-place
2. **Update Pattern**:
   ```python
   # Find task by ID
   index = find_task_index(task_id)
   old_task = _tasks[index]

   # Create new task with updated status
   new_task = Task(
       id=old_task.id,
       title=old_task.title,
       description=old_task.description,
       completed=True  # Updated value
   )

   # Replace in list
   _tasks[index] = new_task
   ```

### Edge Case Handling

| Scenario | Behavior |
|----------|----------|
| Task not found | Raise error "Task not found" |
| Invalid ID (negative, zero, non-integer) | Raise error "Invalid ID format" |
| Task already complete | Display message "Task is already complete" |
| Task already incomplete | Display message "Task is already incomplete" |
| Empty task list | Display message "No tasks to update" |
| Multiple tasks with same ID | Cannot happen - IDs are unique by design |

## No New Entities

Spec 005 does not introduce new entities. It operates solely on the existing Task entity defined in Spec 001.

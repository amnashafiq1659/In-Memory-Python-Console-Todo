# Research: Update Task

**Feature**: Update Task
**Date**: 2025-12-31
**Status**: Complete

## Summary

Research completed for implementing Update Task functionality. All technical decisions aligned with existing codebase patterns from Spec 1 (Add Task) and Spec 2 (View Tasks). No NEEDS CLARIFICATION items - all requirements are clear and implementable.

## Design Decisions

### 1. Task Storage Access

**Decision**: Import `_tasks` and `Task` from `add.py` module

**Rationale**:
- Maintains consistency with existing `view.py` pattern
- Ensures single source of truth for task storage
- Avoids code duplication and synchronization issues
- `_tasks` is the canonical storage for all tasks in the application

**Alternatives Considered**:
- Copy task model to `update.py`: Rejected due to data duplication risk and potential sync issues
- Create shared `models.py`: Rejected as over-engineering for simple project scope
- Use external file storage: Rejected - Spec 3 requires in-memory storage only

**Code Reference**:
- `src/add.py:4` - `_tasks` global variable declaration
- `src/add.py:7-12` - `Task` dataclass definition

### 2. Task Object Immutability

**Decision**: Respect frozen dataclass - create new Task instances for updates

**Rationale**:
- `Task` is defined with `frozen=True` parameter in add.py
- Updates require replacing the existing Task object at the same index
- Maintains immutability guarantees while supporting updates
- Consistent with functional programming principles

**Implementation Approach**:
```python
# Find task by ID
index = None
for i, task in enumerate(_tasks):
    if task.id == task_id:
        index = i
        break

# Replace with new instance
if index is not None:
    new_task = Task(
        id=task.id,
        title=new_title or task.title,
        description=new_description or task.description,
        completed=task.completed  # Preserve completion status
    )
    _tasks[index] = new_task
```

### 3. Input Validation Strategy

**Decision**: Validate task ID existence before requesting update values

**Rationale**:
- Provides immediate feedback on invalid IDs (FR-008, FR-009)
- Follows user story 2 requirements for clear error handling
- Reduces user friction by catching errors early
- Matches pattern from existing acceptance scenarios

**Validation Rules**:
1. Parse task ID as integer (handle non-numeric input gracefully)
2. Search `_tasks` list for matching `task.id`
3. If not found: raise `ValueError` with clear message
4. Validate new_title (if provided) is not empty/whitespace
5. Allow empty/None for new_title to skip title update
6. Allow empty/None for new_description to skip description update

### 4. Partial Update Support

**Decision**: Support partial updates (title only, description only, or both)

**Rationale**:
- Directly supports acceptance scenarios 2 and 3
- Provides user flexibility - update what's needed
- Maintains backward compatibility with existing values
- Spec FR-005 and FR-006 require this capability

**Implementation Logic**:
```python
if new_title and not new_title.isspace():
    title = new_title
else:
    title = task.title  # Keep existing

if new_description is not None:  # Allow empty string
    description = new_description
else:
    description = task.description  # Keep existing
```

### 5. Console Interaction Flow

**Decision**: Linear flow with early exit on invalid ID

**Rationale**:
- Simple and predictable for users
- Matches pattern from `run_add_task_ui()` in add.py
- Clear separation of validation and update phases
- Reduces cognitive load for users

**Flow**:
1. (Optional) Display available tasks for reference
2. Prompt for task ID
3. Validate task ID exists → if not: display error, exit
4. Display current task details
5. Prompt for new title (Enter to skip)
6. Prompt for new description (Enter to skip)
7. Validate at least one field is being updated → if not: inform user, exit
8. Apply update
9. Display success message with updated task

### 6. Error Handling

**Decision**: Use exceptions for programmatic errors, user-friendly messages for console UI

**Rationale**:
- Separates concerns: business logic vs. UI layer
- Allows testing of error conditions without UI
- Consistent with existing `add_task()` pattern (raises `ValueError`)
- Console UI catches exceptions and displays clear messages

**Exception Types**:
- `ValueError`: Task ID not found
- `ValueError`: Invalid title (empty/whitespace)
- `ValueError`: Non-integer task ID input

**UI Error Messages**:
- "Error: Task with ID {task_id} not found"
- "Error: Title cannot be empty or whitespace-only"
- "Error: Invalid task ID format. Please enter a number."

### 7. Completion Status Preservation

**Decision**: Always preserve `completed` field unchanged

**Rationale**:
- Spec FR-011 requires this explicitly
- Prevents accidental state changes during title/description updates
- Separates concerns: title/description updates vs. completion toggles
- Consistent with data integrity requirements

## Technical Constraints

### Python Version
- Python 3.13 (matching existing codebase)
- Uses type hints (`str | None` syntax)
- Standard library only (no external dependencies)

### Data Structures
- `list[Task]` for storage (O(n) search for updates)
- Acceptable for in-memory console app scale
- Single session runtime (<1000 tasks expected)

### Console I/O
- Standard `input()` and `print()` functions
- No external UI libraries
- Cross-platform (Windows/macOS/Linux)

## No Unresolved Unknowns

All technical decisions have been made. No NEEDS CLARIFICATION items remain. The implementation is ready to proceed to Phase 2 (tasks generation).

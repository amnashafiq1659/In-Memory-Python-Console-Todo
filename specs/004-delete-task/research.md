# Research: Delete Task

**Feature**: Delete Task
**Date**: 2025-12-31
**Status**: Complete

## Summary

Research completed for implementing Delete Task functionality. All technical decisions aligned with existing codebase patterns from Spec 1 (Add Task), Spec 2 (View Tasks), and Spec 3 (Update Task). No NEEDS CLARIFICATION items - all requirements are clear and implementable.

## Design Decisions

### 1. Task Storage Access

**Decision**: Import `_tasks` and `Task` from `add.py` module

**Rationale**:
- Maintains consistency with existing `view.py` and `update.py` patterns
- Ensures single source of truth for task storage across all modules
- Avoids code duplication and synchronization issues

**Alternatives Considered**:
- Copy task model to `delete.py`: Rejected due to data duplication risk and potential sync issues
- Create shared `models.py`: Rejected as over-engineering for simple project scope
- Use external file storage: Rejected as Spec 4 requires in-memory only

### 2. Task Deletion Strategy

**Decision**: Remove task from `_tasks` list by index after finding task by ID

**Rationale**:
- O(n) lookup is acceptable for in-memory console application
- List pop or index removal preserves order of remaining tasks
- Consistent with update.py pattern (find by ID, modify at index)
- Task IDs are never reused (`_next_id` continues incrementing)

**Alternatives Considered**:
- Mark as deleted (soft delete): Rejected as over-engineering for simple scope
- Filter out deleted tasks: Rejected as less memory-efficient and more complex
- Rebuild entire list: Rejected as unnecessary for in-memory scope

### 3. Input Validation Strategy

**Decision**: Validate task ID existence before requesting deletion confirmation

**Rationale**:
- Provides immediate feedback on invalid IDs, follows user story 2 requirements
- Prevents displaying confirmation dialog for non-existent tasks
- Consistent with update.py pattern (validate before proceeding)

**Implementation**: Search `_tasks` list by matching `task.id` to user input before confirmation prompt

### 4. Confirmation Strategy

**Decision**: Display task details and require explicit y/n confirmation before deletion

**Rationale**:
- Prevents accidental deletions (FR-007 from spec)
- Follows destructive operation best practices
- Provides user visibility into what they're deleting
- Consistent with destructive action patterns in CLI tools

**Alternatives Considered**:
- Delete immediately without confirmation: Rejected as too dangerous for destructive operation
- Undo/rollback mechanism: Rejected as over-engineering for in-memory scope
- Double confirmation: Rejected as excessive friction for simple CLI

### 5. Error Handling

**Decision**: Use exceptions for programmatic errors, user-friendly messages for console UI

**Rationale**:
- Separates concerns: business logic vs. UI layer
- Allows testing of error conditions without UI
- Consistent with existing `add_task()` and `update_task()` patterns
- Console UI catches exceptions and displays clear messages

**Exception Types**:
- `ValueError`: Task ID not found
- `ValueError`: Invalid task ID format (non-numeric, negative)

**UI Error Messages**:
- "Error: Task with ID {task_id} not found"
- "Error: Invalid task ID format. Please enter a number."
- "Error: Task ID must be a positive integer"

## Technical Constraints

### Python Version
- Python 3.13 (matching existing codebase)
- Uses type hints (`str | None` syntax)
- Standard library only (no external dependencies)

### Data Structures
- `list[Task]` for storage (O(n) search and O(n) removal)
- Acceptable for in-memory console app scale
- Single session runtime (<1000 tasks expected)

### Console I/O
- Standard `input()` and `print()` functions
- No external UI libraries
- Cross-platform (Windows/macOS/Linux)

## No Unresolved Unknowns

All technical decisions have been made. No NEEDS CLARIFICATION items remain. The implementation is ready to proceed to Phase 2 (tasks generation).

## Design Summary

**Architecture**:
- Module: `delete.py` imports `_tasks` and `Task` from `add.py`
- Functions: `find_task_by_id()`, `validate_task_id()`, `delete_task()`, `display_task_details()`, `run_delete_task_ui()`
- Entry point: `if __name__ == "__main__": run_delete_task_ui()`

**Data Flow**:
1. User enters task ID
2. System validates ID exists
3. System displays task details
4. System requests y/n confirmation
5. If confirmed: task removed from `_tasks` list
6. System displays success message
7. If not confirmed or invalid: return to start

**Error Handling**:
- Non-existent task IDs → Error message, return to start
- Non-numeric input → Error message, return to start
- Negative IDs → Error message, return to start

All design decisions are complete and ready for implementation.

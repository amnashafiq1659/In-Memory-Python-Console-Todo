# Implementation Plan: Delete Task

**Branch**: `004-delete-task` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/004-delete-task/spec.md`

## Summary

Implement task deletion functionality for console Todo application, allowing users to remove existing tasks by their unique ID. The feature follows existing pattern established in Spec 1 (Add Task), Spec 2 (View Tasks), and Spec 3 (Update Task), using the same in-memory Task model and dataclass structure. The implementation will validate task IDs before deletion, display task details for confirmation, require user confirmation to prevent accidental deletions, and preserve data integrity of remaining tasks.

## Technical Context

**Language/Version**: Python 3.13 (consistent with existing codebase)
**Primary Dependencies**: dataclasses (built-in), sys (built-in)
**Storage**: In-memory list `_tasks` (shared with add.py module)
**Testing**: pytest (if needed for verification)
**Target Platform**: Console application (Windows via PowerShell/bash)
**Project Type**: Single project (console CLI)
**Performance Goals**: Delete operations complete in <5 seconds (from success criteria)
**Constraints**: Console-based interaction only, no external dependencies beyond standard library
**Scale/Scope**: In-memory storage for single session runtime

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: PASS (constitution.md is a template with no active constraints)

The project constitution is currently a template with placeholder content. No architectural gates or constraints are enforced at this time. The implementation will follow clean code principles and maintain consistency with existing Spec 1, Spec 2, and Spec 3 implementations.

## Project Structure

### Documentation (this feature)

```text
specs/004-delete-task/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── add.py               # Existing: Task dataclass, in-memory storage (_tasks), add_task()
├── view.py              # Existing: get_all_tasks(), run_view_tasks_ui()
├── update.py            # Existing: update_task(), run_update_task_ui()
└── delete.py            # NEW: delete_task(), run_delete_task_ui()

tests/
├── test_add.py          # Existing: Tests for add task functionality
├── test_update.py       # Existing: Tests for update task functionality
└── test_delete.py       # NEW: Tests for delete task functionality
```

**Structure Decision**: Single project structure with modular files in `src/` directory. The `delete.py` module will import `_tasks` and `Task` from `add.py` to maintain consistency with the existing pattern used by `view.py` and `update.py`. All interaction flows through console I/O (stdin/stdout) with clear user feedback.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (None - no constitution violations) | N/A | N/A |

## Phase 0: Research & Design Decisions

### Research Findings

**Task Storage Pattern**: Analysis of `add.py`, `view.py`, and `update.py` reveals a shared in-memory storage pattern:
- `_tasks` (list[Task]) stores all tasks globally in `add.py`
- `Task` is a frozen dataclass with fields: `id`, `title`, `description`, `completed`
- `_next_id` (int) provides auto-incrementing task IDs
- `update.py` demonstrates pattern: `find_task_by_id()`, `validate_task_id()`, display helpers

**Delete Strategy Decision**:
- **Decision**: Import `_tasks` and `Task` from `add.py` module
- **Rationale**: Maintains consistency with existing `view.py` and `update.py` patterns, avoids code duplication, ensures single source of truth for task storage
- **Alternatives Considered**:
  - Copy task model to `delete.py`: Rejected due to data duplication and sync issues
  - Create shared `models.py`: Rejected as over-engineering for simple project scope
  - Use external file storage: Rejected as Spec 4 requires in-memory only

**Input Validation Strategy**:
- **Decision**: Validate task ID existence before requesting confirmation
- **Rationale**: Provides immediate feedback on invalid IDs, follows user story 2 requirements
- **Implementation**: Search `_tasks` list by matching `task.id` to user input
- **Pattern**: Reuse `find_task_by_id()` and `validate_task_id()` from `update.py`

**Confirmation Strategy**:
- **Decision**: Display task details before deletion and require explicit user confirmation
- **Rationale**: Prevents accidental deletions (FR-007), follows user safety best practices
- **Implementation**: Display task with id/title/description/status, prompt for y/n confirmation

**Removal Strategy**:
- **Decision**: Remove task from `_tasks` list by index after finding task by ID
- **Rationale**: O(n) list removal is acceptable for in-memory scope, preserves order of remaining tasks
- **Alternatives Considered**:
  - Mark as deleted (soft delete): Rejected as over-engineering for simple spec
  - Rebuild entire list: Rejected as inefficient and unnecessary

## Phase 1: Data Model & Interfaces

### Data Model

The `Task` dataclass from Spec 1 is reused without modification:

```python
@dataclass(frozen=True)
class Task:
    id: int              # Unique identifier (read-only for deletion)
    title: str           # Displayed for confirmation
    description: str     # Displayed for confirmation
    completed: bool      # Displayed for confirmation
```

**State Transition**:
- Task is completely removed from `_tasks` list
- Task ID is not reused ( `_next_id` counter in add.py continues incrementing)

### Interface Contracts

**Function: `delete_task(task_id: int) -> None`**

| Parameter | Type | Validation |
|-----------|------|------------|
| task_id | int | Must be positive integer, must match existing task ID |

| Return | Type | Description |
|--------|------|-------------|
| None | No return value (deletion is destructive operation) |

| Exception | Condition |
|-----------|-----------|
| ValueError | task_id does not exist |

**Console UI Function: `run_delete_task_ui() -> None`**

Input flow:
1. Display available tasks (for user reference)
2. Prompt for task ID
3. Validate task ID exists
4. If invalid: display error, return to start
5. Display task details
6. Prompt for confirmation (y/n)
7. If confirmed: remove task from memory
8. Display success message
9. If not confirmed: return to start
10. Ask if user wants to continue deleting

### Quick Start

**Dependencies**: None (standard library only)

**Module Layout**:
```python
from add import _tasks, Task

def find_task_by_id(task_id: int) -> Task | None:
    """Search for task by ID"""
    ...

def delete_task(task_id: int) -> None:
    """Core delete logic with validation"""
    ...

def prompt_for_task_id() -> int:
    """Prompt user for task ID"""
    ...

def display_task_details(task: Task) -> None:
    """Display task for confirmation"""
    ...

def run_delete_task_ui() -> None:
    """Interactive console interface"""
    ...

if __name__ == "__main__":
    run_delete_task_ui()
```

**Usage Example**:
```bash
python src/delete.py
```

## Phase 2: Implementation (Not executed by /sp.plan)

The actual implementation code will be generated by `/sp.implement` command based on tasks.md (created by `/sp.tasks`).

## Architectural Decision Record (ADR) Summary

No significant architectural decisions requiring formal ADR documentation. All design choices follow established patterns from existing codebase (add.py, view.py, update.py) and are straightforward extensions of the current architecture.

**Next Step**: Run `/sp.tasks` to generate testable tasks from this plan.

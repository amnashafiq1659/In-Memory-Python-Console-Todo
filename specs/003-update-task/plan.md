# Implementation Plan: Update Task

**Branch**: `003-update-task` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/003-update-task/spec.md`

## Summary

Implement task update functionality for the console Todo application, allowing users to modify the title and/or description of existing tasks by their unique ID. The feature follows the existing pattern established in Spec 1 (Add Task) and Spec 2 (View Tasks), using the same in-memory Task model and dataclass structure. The implementation will validate task IDs before updates, support partial updates (title only, description only, or both), and preserve task completion status unchanged.

## Technical Context

**Language/Version**: Python 3.13 (consistent with existing codebase)
**Primary Dependencies**: dataclasses (built-in), sys (built-in)
**Storage**: In-memory list `_tasks` (shared with add.py module)
**Testing**: pytest (if needed for verification)
**Target Platform**: Console application (Windows via PowerShell/bash)
**Project Type**: Single project (console CLI)
**Performance Goals**: Update operations complete in <10 seconds (from success criteria)
**Constraints**: Console-based interaction only, no external dependencies beyond standard library
**Scale/Scope**: In-memory storage for single session runtime

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: PASS (constitution.md is a template with no active constraints)

The project constitution is currently a template with placeholder content. No architectural gates or constraints are enforced at this time. The implementation will follow clean code principles and maintain consistency with existing Spec 1 and Spec 2 implementations.

## Project Structure

### Documentation (this feature)

```text
specs/003-update-task/
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
└── update.py            # NEW: update_task(), run_update_task_ui()

tests/
├── test_add.py          # Existing: Tests for add task functionality
└── test_update.py       # NEW: Tests for update task functionality
```

**Structure Decision**: Single project structure with modular files in `src/` directory. The `update.py` module will import `_tasks` and `Task` from `add.py` to maintain consistency with the existing pattern used by `view.py`. All interaction flows through console I/O (stdin/stdout) with clear user feedback.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| (None - no constitution violations) | N/A | N/A |

## Phase 0: Research & Design Decisions

### Research Findings

**Task Storage Pattern**: Analysis of `add.py` and `view.py` reveals a shared in-memory storage pattern:
- `_tasks` (list[Task]) stores all tasks globally in `add.py`
- `Task` is a frozen dataclass with fields: `id`, `title`, `description`, `completed`
- `_next_id` (int) provides auto-incrementing task IDs

**Update Strategy Decision**:
- **Decision**: Import `_tasks` and `Task` from `add.py` module
- **Rationale**: Maintains consistency with existing `view.py` pattern, avoids code duplication, ensures single source of truth for task storage
- **Alternatives Considered**:
  - Copy task model to `update.py`: Rejected due to data duplication and sync issues
  - Create shared `models.py`: Rejected as over-engineering for simple project scope
  - Use external file storage: Rejected as Spec 3 requires in-memory only

**Input Validation Strategy**:
- **Decision**: Validate task ID existence before requesting new values
- **Rationale**: Provides immediate feedback on invalid IDs, follows user story 2 requirements
- **Implementation**: Search `_tasks` list by matching `task.id` to user input

**Partial Update Support**:
- **Decision**: Allow empty strings for title/description to skip updates
- **Rationale**: Supports use cases from acceptance scenarios (update title only, description only, or both)
- **Implementation**: Only modify field if non-empty value provided

## Phase 1: Data Model & Interfaces

### Data Model

The `Task` dataclass from Spec 1 is reused without modification:

```python
@dataclass(frozen=True)
class Task:
    id: int              # Unique identifier (read-only for updates)
    title: str           # Updatable
    description: str     # Updatable
    completed: bool      # Read-only for title/description updates
```

**State Transition**:
- Task objects are immutable (frozen dataclass)
- Updates require creating new Task instances with modified fields
- Old instance is replaced in `_tasks` list at the same index

### Interface Contracts

**Function: `update_task(task_id: int, new_title: str | None, new_description: str | None) -> Task`**

| Parameter | Type | Validation |
|-----------|------|------------|
| task_id | int | Must be positive integer, must match existing task ID |
| new_title | str \| None | If provided and non-empty: must not be whitespace-only |
| new_description | str \| None | Optional, can be empty string |

| Return | Type | Description |
|--------|------|-------------|
| Task | Task | The updated task object with new values |

| Exception | Condition |
|-----------|-----------|
| ValueError | task_id does not exist |
| ValueError | new_title provided but empty/whitespace |

**Console UI Function: `run_update_task_ui() -> None`**

Input flow:
1. Display available tasks (optional, for user reference)
2. Prompt for task ID
3. Validate task ID exists
4. If invalid: display error, return
5. Prompt for new title (press Enter to skip)
6. Prompt for new description (press Enter to skip)
7. Apply updates if any non-empty values provided
8. Display success message with updated task details

### Quick Start

**Dependencies**: None (standard library only)

**Module Layout**:
```python
from add import _tasks, Task

def update_task(task_id: int, new_title: str | None, new_description: str | None) -> Task:
    """Core update logic with validation"""
    ...

def run_update_task_ui() -> None:
    """Interactive console interface"""
    ...

if __name__ == "__main__":
    run_update_task_ui()
```

**Usage Example**:
```bash
python src/update.py
```

## Phase 2: Implementation (Not executed by /sp.plan)

The actual implementation code will be generated by `/sp.implement` command based on tasks.md (created by `/sp.tasks`).

## Architectural Decision Record (ADR) Summary

No significant architectural decisions requiring formal ADR documentation. All design choices follow established patterns from existing codebase and are straightforward extensions of the current architecture.

**Next Step**: Run `/sp.tasks` to generate testable tasks from this plan.

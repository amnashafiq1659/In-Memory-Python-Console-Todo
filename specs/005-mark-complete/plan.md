# Implementation Plan: Mark Task Complete / Incomplete

**Branch**: `005-mark-complete` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/005-mark-complete/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement task completion status management for the in-memory Python console Todo application. This feature enables users to mark tasks as complete or incomplete by entering their unique task IDs through the console interface. The system validates task IDs, updates the completion status in memory, and provides clear feedback to users. The implementation is constrained to a single file (`complete.py` in `/src`) and reuses the existing Task dataclass and storage from Spec 001.

## Technical Context

**Language/Version**: Python 3.9+
**Primary Dependencies**: None (standard library only, imports from existing `src/add.py`)
**Storage**: In-memory (reuses `_tasks` list from `src/add.py`)
**Testing**: pyunit (standard library `unittest`)
**Target Platform**: Console/terminal (cross-platform)
**Project Type**: Single (single console application)
**Performance Goals**: Mark complete/incomplete operation completes in < 3 seconds per SC-001/SC-002
**Constraints**: Single file (`complete.py` in `/src`), no file/database persistence, console-based interaction only
**Scale/Scope**: Support 1,000+ tasks per session per spec assumptions

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The project constitution is not yet defined (template only). No constitutional violations detected. This feature:
- Reuses existing data model from Spec 001
- Follows single-responsibility principle (only handles completion status)
- Uses standard library only (no external dependencies)
- Maintains consistency with existing specs (similar UI patterns)

**Status**: PASSED

## Project Structure

### Documentation (this feature)

```text
specs/005-mark-complete/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── complete.yaml    # Function contracts for marking complete/incomplete
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── add.py              # Task model and storage (Spec 001)
├── view.py             # View tasks functionality (Spec 002)
├── update.py           # Update task functionality (Spec 003)
├── delete.py           # Delete task functionality (Spec 004)
└── complete.py         # Mark complete/incomplete functionality (THIS SPEC - Spec 005)

tests/
├── test_complete.py    # Unit tests for complete.py
```

**Structure Decision**: Single project structure with one Python file (`complete.py`) in `/src` directory. Reuses Task dataclass and storage from `src/add.py` via import pattern established in previous specs.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitutional violations identified. Complexity tracking not applicable.

---

## Phase 0: Research Decisions

*Completed: 2025-12-31*

### Task Model Access
- **Decision**: Import Task dataclass and access `_tasks` list directly from `src/add.py`
- **Rationale**: Consistent with Specs 002, 003, and 004. Tasks are stored in global state; direct access is simplest.
- **Alternatives considered**:
  - Copy Task class definition (rejected: duplication, inconsistency risk)
  - Create getter function in add.py (rejected: unnecessary indirection, not done in other specs)

### Task Mutation Strategy
- **Decision**: Since Task is `@dataclass(frozen=True)`, create new Task instance with updated `completed` field and replace in list
- **Rationale**: Frozen dataclasses are immutable. Finding task by ID and replacing entire object is the cleanest pattern.
- **Alternatives considered**:
  - Make Task mutable (rejected: breaks existing code from Spec 001)
  - Use dict instead of dataclass (rejected: changes type system, breaks other specs)

### Task Lookup Strategy
- **Decision**: Linear search through `_tasks` list to find task by ID
- **Rationale**: Simple, matches pattern from Spec 003 (update) and Spec 004 (delete). For 1,000 tasks, O(n) is acceptable for SC-001/SC-002 (3 seconds).
- **Alternatives considered**:
  - Build dictionary index (rejected: requires maintaining sync state, complexity not justified for 1,000 tasks)
  - Binary search on sorted list (rejected: list not sorted by ID, requires extra sorting logic)

### Console UI Pattern
- **Decision**: Follow `run_*_ui()` pattern from Specs 001, 002, 003, 004
- **Rationale**: Consistent user experience. Separation of core logic (`mark_complete()`, `mark_incomplete()`) from UI (`run_complete_task_ui()`).
- **Alternatives considered**:
  - Single function for both logic and UI (rejected: violates single responsibility)
  - Command-line arguments instead of interactive menu (rejected: spec requires console interaction)

### User Input Validation
- **Decision**: Validate task ID as positive integer before lookup
- **Rationale**: Early validation provides clear error messages. Covers edge cases: empty, whitespace, negative, non-numeric, float.
- **Alternatives considered**:
  - Try-except during lookup (rejected: less precise error messages, harder to distinguish "invalid ID" from "task not found")
  - Allow any int and let lookup fail (rejected: negative IDs are never valid, should reject early)

### Status Toggle vs Separate Operations
- **Decision**: Separate functions for `mark_complete()` and `mark_incomplete()` (not toggle)
- **Rationale**: Clear intent in code. User stories 1 and 2 are independent. UI can offer both options.
- **Alternatives considered**:
  - Single toggle function (rejected: less explicit, harder to test edge cases separately)
  - UI-driven toggle only (rejected: need core functions for testing and reusability)

### Confirmation Message Format
- **Decision**: Display "Task {id} marked as complete/incomplete" after successful operation
- **Rationale**: Clear feedback matches pattern from Spec 001 ("Task added with ID: {id}"). Provides confirmation and shows what happened.
- **Alternatives considered**:
  - Silent success (rejected: user has no confirmation)
  - Display task details after update (rejected: redundant with view functionality)

### Error Message Strategy
- **Decision**: Specific messages for each error type: "Invalid ID format" vs "Task not found"
- **Rationale**: Per FR-006, users need actionable feedback. Differentiating format errors vs existence errors helps users correct input.
- **Alternatives considered**:
  - Generic "Invalid ID" message (rejected: less actionable)
  - Stack traces (rejected: not user-friendly)

### Testing Framework
- **Decision**: Use standard library `unittest` (consistent with existing project)
- **Rationale**: No external dependencies needed. Matches patterns in existing test files.
- **Alternatives considered**:
  - pytest (rejected: external dependency, not in project)
  - No tests (rejected: FR requirements are testable, should have automated verification)

---

## Phase 1: Design Artifacts

### Data Model

See [data-model.md](./data-model.md)

### API/Function Contracts

See [contracts/](./contracts/)

### Quickstart Guide

See [quickstart.md](./quickstart.md)

---

## Phase 1: Constitution Check (Re-evaluation)

*Status*: PASSED

No constitutional violations. The design maintains simplicity, reuses existing patterns, and adheres to single-responsibility principles.

---

## Next Steps

Proceed to `/sp.tasks` to generate testable implementation tasks based on this plan.

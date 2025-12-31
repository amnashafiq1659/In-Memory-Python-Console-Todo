# Implementation Plan: View Tasks & Status Indication

**Branch**: `002-view-tasks` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/002-view-tasks/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement functionality to view all tasks stored in memory and display them with clear status indicators. The feature reads from the existing Task model and in-memory storage established in Spec 001, providing read-only access to task data. Users can view all tasks with their ID, title, description, and completion status, with visual indicators distinguishing completed from incomplete tasks.

## Technical Context

**Language/Version**: Python 3.13+ (from pyproject.toml)
**Primary Dependencies**: None (standard library only)
**Storage**: In-memory (no persistence) - reads from existing `_tasks` list in `src/add.py`
**Testing**: pytest (from existing test_tasks.py pattern)
**Target Platform**: Console/terminal (cross-platform)
**Project Type**: Single
**Performance Goals**: Display up to 1,000 tasks without issues (SC-002)
**Constraints**: Single file (`view.py` in `/src`), no persistence, read-only access to tasks
**Scale/Scope**: Display all tasks in memory (1,000+ tasks supported)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The project constitution is not yet defined (template only). No constitutional violations detected. This feature maintains simplicity and follows established patterns from Spec 001.

**Status**: PASSED

## Project Structure

### Documentation (this feature)

```text
specs/002-view-tasks/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
│   └── view-tasks.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── add.py               # Existing: Task model and add task functionality (Spec 001)
└── view.py              # New: View tasks functionality (Spec 002)
```

**Structure Decision**: Create separate `src/view.py` file to maintain single-file-per-spec pattern while keeping concerns separate. The `view.py` will import Task class from `src/add.py` and read from the shared in-memory `_tasks` list.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitutional violations identified. Complexity tracking not applicable.

---

## Phase 0: Research Decisions

*Completed: 2025-12-31*

### Task Model Reuse
- **Decision**: Import Task dataclass from existing `src/add.py` instead of redefining
- **Rationale**: Task entity is shared across specs (noted in spec.md). Avoids duplication and ensures consistency.
- **Alternatives considered**:
  - Redefine Task class in view.py (rejected: duplication, inconsistency risk)

### Storage Access Pattern
- **Decision**: Read directly from module-level `_tasks` list in `src/add.py`
- **Rationale**: Tasks are stored in global state; direct read access is simplest and follows Spec 001 pattern.
- **Alternatives considered**:
  - Create getter function in add.py (rejected: unnecessary indirection)
  - Move storage to shared module (rejected: scope creep beyond current spec)

### Status Indicator Format
- **Decision**: Use checkmark symbols [✓] for completed, [ ] for incomplete
- **Rationale**: Clear visual distinction that works across platforms. Symbols are immediately recognizable.
- **Alternatives considered**:
  - Text "completed"/"incomplete" (rejected: less scannable at a glance)
  - Different colors (rejected: console color support varies)
  - Unicode boxes [☑]/[☐] (rejected: less universal than checkmarks)

### Display Format
- **Decision**: One task per line with tab-separated fields: ID | [status] | Title | Description
- **Rationale**: Simple format that's easy to parse visually. Handles long content by natural line wrapping.
- **Alternatives considered**:
  - Table with borders (rejected: unnecessary complexity for console)
  - JSON output (rejected: not human-readable)
  - Multi-line per task (rejected: harder to scan many tasks)

### Empty List Handling
- **Decision**: Display "No tasks found. Add tasks using the add task functionality."
- **Rationale**: Clear user guidance on how to proceed. Matches UI patterns from Spec 001.
- **Alternatives considered**:
  - Display nothing (rejected: confusing, user doesn't know if functionality worked)
  - Display error (rejected: not an error, just empty state)

### Long Content Handling
- **Decision**: No explicit truncation; let terminal naturally wrap lines
- **Rationale**: Tasks can be 1000+ chars (spec requirement). Terminal wrapping is standard behavior.
- **Alternatives considered**:
  - Truncate at 80 chars (rejected: loses information)
  - Ellipsis truncation (rejected: unclear what was omitted)
  - Multi-line display (rejected: breaks scannability for many tasks)

### Console UI Pattern
- **Decision**: Follow `run_add_task_ui()` pattern from Spec 001
- **Rationale**: Consistent user experience. Separation of core logic (`get_all_tasks()`) from UI (`run_view_tasks_ui()`).
- **Alternatives considered**:
  - Single function for both logic and UI (rejected: violates single responsibility)
  - Command-line arguments instead of interactive menu (rejected: spec requires console interaction)

---

## Phase 1: Design Artifacts

### Data Model

See [data-model.md](./data-model.md)
- Task entity is shared with Spec 001
- No new entities introduced

### API/Function Contracts

See [contracts/](./contracts/)

### Quickstart Guide

See [quickstart.md](./quickstart.md)

---

## Phase 1: Constitution Check (Re-evaluation)

*Status*: PASSED

No constitutional violations. The design maintains simplicity, follows Spec 001 patterns, and adheres to single-responsibility principles.

---

## Next Steps

Proceed to `/sp.tasks` to generate testable implementation tasks based on this plan.

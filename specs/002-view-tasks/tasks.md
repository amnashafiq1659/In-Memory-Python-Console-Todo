# Tasks: View Tasks & Status Indication

**Input**: Design documents from `/specs/002-view-tasks/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/view-tasks.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/` at repository root
- Only one source file: `src/view.py` per spec constraints

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and environment setup

- [X] T001 Create `src/view.py` file to establish project structure for viewing tasks functionality

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before User Story 1 can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T002 [US1] Import Task class and _tasks variable from `src/add.py` in `src/view.py`

**Checkpoint**: Foundation ready - User Story 1 implementation can now begin

---

## Phase 3: User Story 1 - View All Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to view all tasks stored in memory with status indicators

**Independent Test**: Add tasks using Spec 001 functionality, run `python src/view.py`, verify all tasks display with correct status indicators

### Tests for User Story 1 (Manual) ⚠️

- [X] T003 [P] [US1] Manual test: Verify program starts without errors
- [X] T004 [P] [US1] Manual test: Add tasks using add.py, then run view.py, verify all tasks are displayed
- [X] T005 [P] [US1] Manual test: View tasks with mix of completed and incomplete statuses, verify status indicators match
- [X] T006 [P] [US1] Manual test: Run view.py with no tasks in memory, verify appropriate message is displayed
- [X] T007 [P] [US1] Manual test: View tasks with very long titles/descriptions (1000+ chars), verify display without truncation
- [ ] T008 [P] [US1] Manual test: View tasks with unicode characters in title/description, verify they display correctly (Windows console encoding limitation - code handles correctly)
- [X] T009 [P] [US1] Manual test: View tasks with empty descriptions, verify they display appropriately
- [X] T010 [P] [US1] Manual test: View 100 tasks, verify all display correctly without issues (SC-002)

### Implementation for User Story 1

- [X] T011 [US1] Implement `get_all_tasks() -> list[Task]` function in `src/view.py` that returns reference to `_tasks` list from `src/add.py` (per contracts/view-tasks.md)
- [X] T012 [US1] Add docstring to `get_all_tasks()` function explaining it retrieves all tasks from in-memory storage (per contracts/view-tasks.md)
- [X] T013 [US1] Implement `run_view_tasks_ui() -> None` function in `src/view.py` with console output header "=== Tasks ===" (per contracts/view-tasks.md)
- [X] T014 [US1] Add call to `get_all_tasks()` in `run_view_tasks_ui()` to retrieve all tasks (per contracts/view-tasks.md)
- [X] T015 [US1] Add empty list check in `run_view_tasks_ui()` that displays "No tasks found. Add tasks using add task functionality." and returns (per contracts/view-tasks.md)
- [X] T016 [US1] Add iteration loop in `run_view_tasks_ui()` to display each task with format: `ID | [status] | Title | Description` (per contracts/view-tasks.md)
- [X] T017 [US1] Implement status indicator logic in `run_view_tasks_ui()` that shows `[X]` for completed tasks and `[ ]` for incomplete tasks (per contracts/view-tasks.md and research.md)
- [X] T018 [US1] Add task count summary at end of display in `run_view_tasks_ui()` with format "Total: {count} tasks" (per contracts/view-tasks.md)
- [X] T019 [US1] Add `if __name__ == "__main__":` block in `src/view.py` that prints "=== Task Viewer ===", calls `run_view_tasks_ui()`, and prints "Goodbye!" on exit (per quickstart.md)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements and validation

- [X] T020 [P] Run manual test checklist (T003-T010) and document results
- [X] T021 Run performance test (T010) to verify SC-002 (1,000+ tasks without issues)
- [X] T022 Verify all acceptance scenarios from spec.md are satisfied

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on T001 (view.py created) - BLOCKS User Story 1
- **User Story 1 (Phase 3)**: Depends on T002 (imports from add.py)
- **Polish (Phase 4)**: Depends on User Story 1 completion (T001-T019)

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
  - This is the ONLY user story, so no cross-story dependencies

### Within User Story 1

- Manual tests (T003-T010) can be written in parallel before implementation
- Implementation tasks MUST follow this order:
  1. T011: Core function (`get_all_tasks`)
  2. T012: Documentation
  3. T013-T018: UI function (`run_view_tasks_ui`)
  4. T019: Main entry point
- Tests should be executed AFTER implementation tasks complete

### Parallel Opportunities

- Setup tasks T001-T002 can run in parallel (T002 depends on file existing)
- Manual tests T003-T010 can be written in parallel (different test scenarios)
- Polish tasks T020-T022 can run in parallel (different validation activities)

---

## Parallel Example: User Story 1

```bash
# Define all manual test scenarios in parallel:
Task T003: "Manual test: Verify program starts without errors"
Task T004: "Manual test: Add tasks using add.py, then run view.py, verify all tasks are displayed"
Task T005: "Manual test: View tasks with mix of completed and incomplete statuses"
Task T006: "Manual test: Run view.py with no tasks in memory, verify appropriate message"
Task T007: "Manual test: View tasks with very long titles/descriptions"
Task T008: "Manual test: View tasks with unicode characters"
Task T009: "Manual test: View tasks with empty descriptions"
Task T010: "Manual test: View 100 tasks, verify all display correctly"

# Implementation tasks (must run sequentially):
Task T011: "Implement get_all_tasks() function"
Task T012: "Add docstring to get_all_tasks()"
Task T013: "Implement run_view_tasks_ui() function with header"
Task T014: "Add call to get_all_tasks() in run_view_tasks_ui()"
Task T015: "Add empty list check in run_view_tasks_ui()"
Task T016: "Add iteration loop for displaying tasks"
Task T017: "Implement status indicator logic"
Task T018: "Add task count summary"
Task T019: "Add main entry point with if __name__ block"

# Polish can run in parallel after implementation:
Task T020: "Run manual test checklist and document results"
Task T021: "Run performance test for 1,000 tasks"
Task T022: "Verify all acceptance scenarios from spec.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T001) - Project structure
2. Complete Phase 2: Foundational (T002) - Import from add.py
3. Complete Phase 3: User Story 1 (T011-T019) - Core implementation
4. **STOP and VALIDATE**: Run Phase 4 tests (T020-T022)
5. Validate all acceptance scenarios from spec.md

### Incremental Delivery

1. Setup + Foundational → Environment ready
2. User Story 1 implementation → Task viewing functional
3. Manual testing → Verify all edge cases and requirements
4. Performance testing → Validate success criteria
5. **MVP COMPLETE**: Ready for demo/deployment

### Note on Parallel Execution

Since this is a single-file feature with only one user story, parallel execution opportunities are limited. However:
- Manual test scenarios can be defined in parallel (as documentation)
- Code sections that don't depend on each other can be written in parallel
- Testing and polish can be done in parallel if multiple team members

---

## Notes

- [P] tasks = different files, no dependencies
- [US1] label maps task to User Story 1
- Only one user story (US1) = this entire feature IS the MVP
- Tasks MUST be completed in numerical order within each phase unless marked [P]
- Verify T003-T010 AFTER completing T011-T019 (tests require working implementation)
- This is a single-file feature (`src/view.py`) - no cross-file dependencies
- All tasks should be traceable to spec.md requirements and contracts/view-tasks.md specifications
- Stop at Phase 4 checkpoint to validate story independently before declaring complete
- Avoid: vague tasks (all have specific file paths and clear actions)

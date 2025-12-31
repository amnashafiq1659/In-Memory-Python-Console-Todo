# Tasks: Task Model & Add Task

**Input**: Design documents from `/specs/001-add-task/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/add-task.md, quickstart.md

**Tests**: Manual testing included as requested in user prompt

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Only one source file: `src/add.py` per spec constraints

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and environment setup

- [X] T001 Run `uv init` to create virtual environment for the project
- [X] T002 Activate UV environment using `uv activate`
- [X] T003 Verify Python 3.13+ is being used (check with `python --version`)
- [X] T004 Create `src` directory if it doesn't exist
- [X] T005 Create empty placeholder file `src/add.py` to establish project structure

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before User Story 1 can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 [P] Initialize in-memory storage variables in `src/add.py` (`_tasks: list[Task] = []` and `_next_id: int = 1`)

**Checkpoint**: Foundation ready - User Story 1 implementation can now begin

---

## Phase 3: User Story 1 - Add a New Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks via console interface with titles and descriptions

**Independent Test**: Run `python src/add.py`, enter a title and description, verify a task is created with a unique ID and stored in memory

### Tests for User Story 1 (Manual) ⚠️

- [X] T007 [P] [US1] Manual test: Verify program starts without errors
- [X] T008 [P] [US1] Manual test: Add a task with title and description, verify success message with correct ID
- [X] T009 [P] [US1] Manual test: Add a task with title and empty description, verify it's accepted
- [X] T010 [P] [US1] Manual test: Attempt to add task with empty title, verify error message
- [X] T011 [P] [US1] Manual test: Attempt to add task with whitespace-only title, verify error message
- [X] T012 [P] [US1] Manual test: Add multiple tasks in sequence, verify unique sequential IDs
- [X] T013 [P] [US1] Manual test: Add task with unicode characters (e.g., "学习中文"), verify it's accepted
- [X] T014 [P] [US1] Manual test: Add task with very long title/description (1000+ chars), verify it's accepted
- [X] T015 [P] [US1] Manual test: Add multiple tasks, verify all tasks remain accessible in memory during session
- [X] T016 [P] [US1] Manual test: Exit program and restart, verify previous tasks are lost (no persistence)
- [X] T017 [P] [US1] Performance test: Add 1,000 tasks in a loop, verify no ID collisions and performance meets SC-001 (< 5 seconds per task)

### Implementation for User Story 1

- [X] T018 [US1] Import `dataclass` from `dataclasses` in `src/add.py`
- [X] T019 [US1] Define frozen `Task` dataclass in `src/add.py` with fields: `id: int`, `title: str`, `description: str`, `completed: bool` (per contracts/add-task.md)
- [X] T020 [US1] Implement `add_task(title: str, description: str) -> Task` function in `src/add.py` with title validation (raises ValueError for empty/whitespace titles)
- [X] T021 [US1] Add logic in `add_task()` to generate unique ID from `_next_id`, increment counter, create Task object, append to `_tasks` list, and return the task (per contracts/add-task.md)
- [X] T022 [US1] Implement `run_add_task_ui()` function in `src/add.py` with while loop for continuous task addition (per contracts/add-task.md)
- [X] T023 [US1] Add title prompt in `run_add_task_ui()` with validation loop that re-prompts on empty/whitespace input
- [X] T024 [US1] Add description prompt in `run_add_task_ui()` that accepts empty input (optional field)
- [X] T025 [US1] Add call to `add_task(title, description)` in `run_add_task_ui()` and print success message with task ID
- [X] T026 [US1] Add continuation prompt in `run_add_task_ui()` asking "Add another task? (y/n): " and exit loop on non-"y" response
- [X] T027 [US1] Add `if __name__ == "__main__":` block in `src/add.py` that prints "=== Task Creator ===", calls `run_add_task_ui()`, and prints "Goodbye!" on exit (per quickstart.md)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Improvements and validation

- [X] T028 [P] Run manual test checklist (T007-T016) and document results
- [X] T029 Run performance test (T017) to verify SC-002 (1,000+ unique IDs)
- [X] T030 Verify all acceptance scenarios from spec.md are satisfied

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on T004 (src directory created) - BLOCKS User Story 1
- **User Story 1 (Phase 3)**: Depends on T006 (in-memory storage initialized)
- **Polish (Phase 4)**: Depends on User Story 1 completion (T001-T027)

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
  - This is the ONLY user story, so no cross-story dependencies

### Within User Story 1

- Manual tests (T007-T017) can be written/defined in parallel before implementation
- Implementation tasks MUST follow this order:
  1. T018-T019: Setup (imports, dataclass definition)
  2. T020-T021: Core function (`add_task`)
  3. T022-T026: UI function (`run_add_task_ui`)
  4. T027: Main entry point
- Tests should be executed AFTER implementation tasks complete

### Parallel Opportunities

- Setup tasks T001-T004 can run in parallel (T005 depends on directory existing)
- Manual tests T007-T017 can be written in parallel (different test scenarios)
- T018 (import) and T019 (dataclass) can run in parallel (different sections of code)
- Polish tasks T028-T030 can run in parallel (different validation activities)

---

## Parallel Example: User Story 1

```bash
# Define all manual test scenarios in parallel:
Task T007: "Manual test: Verify program starts without errors"
Task T008: "Manual test: Add a task with title and description, verify success message"
Task T009: "Manual test: Add a task with title and empty description"
Task T010: "Manual test: Attempt to add task with empty title, verify error message"
Task T011: "Manual test: Attempt to add task with whitespace-only title"
Task T012: "Manual test: Add multiple tasks, verify unique sequential IDs"
Task T013: "Manual test: Add task with unicode characters"
Task T014: "Manual test: Add task with very long title/description"
Task T015: "Manual test: Verify tasks remain accessible in memory"
Task T016: "Manual test: Verify tasks are lost after program exit"
Task T017: "Performance test: Add 1,000 tasks to verify no ID collisions"

# Setup can run in parallel:
Task T018: "Import dataclass from dataclasses"
Task T019: "Define frozen Task dataclass with required fields"

# Polish can run in parallel after implementation:
Task T028: "Run manual test checklist and document results"
Task T029: "Run performance test for 1,000 tasks"
Task T030: "Verify all acceptance scenarios from spec.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T005) - Environment and project structure
2. Complete Phase 2: Foundational (T006) - In-memory storage initialization
3. Complete Phase 3: User Story 1 (T018-T027) - Core implementation
4. **STOP and VALIDATE**: Run Phase 4 tests (T028-T030)
5. Validate all acceptance scenarios from spec.md

### Incremental Delivery

1. Setup + Foundational → Environment ready
2. User Story 1 implementation → Task creation functional
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
- Verify T007-T017 AFTER completing T018-T027 (tests require working implementation)
- This is a single-file feature (`src/add.py`) - no cross-file dependencies
- All tasks should be traceable to spec.md requirements and contracts/add-task.md specifications
- Stop at Phase 4 checkpoint to validate story independently before declaring complete
- Avoid: vague tasks (all have specific file paths and clear actions)

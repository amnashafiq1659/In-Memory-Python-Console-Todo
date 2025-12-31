# Tasks: Mark Task Complete / Incomplete

**Input**: Design documents from `/specs/005-mark-complete/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Test tasks included as requested in the user prompt to verify completion status updates and error handling.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below follow single project structure from plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Verify src/add.py has Task dataclass and _tasks list accessible (check prerequisites)
- [X] T002 Create src/complete.py file structure with imports from src/add.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 Implement validate_task_id(task_id: int) helper function in src/complete.py to check task ID is positive integer and exists in _tasks list
- [X] T004 [P] Add tests for validate_task_id() edge cases in src/complete.py or separate test file (negative, zero, non-existent, non-integer)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Mark Task as Complete (Priority: P1) 🎯 MVP

**Goal**: Users can mark incomplete tasks as complete by entering task ID, with clear feedback and status updates in memory.

**Independent Test**: Create an incomplete task, mark it complete, verify status changed to True in memory. Run view.py to confirm status reflects correctly.

### Implementation for User Story 1

- [X] T005 [US1] Implement mark_complete(task_id: int) -> Task function in src/complete.py that finds task by ID, creates new Task instance with completed=True, and replaces task in _tasks list
- [X] T006 [US1] Add "Task {id} is already complete" detection in mark_complete() function (when task.completed is already True)
- [X] T007 [US1] Add tests for mark_complete() in src/complete.py or test file (marks incomplete task complete, validates status updated, tests already-complete case)
- [X] T008 [US1] Implement console prompt "Do you want to mark a task as (c)omplete or (i)ncomplete? " in run_complete_task_ui() function in src/complete.py
- [X] T009 [US1] Add action selection validation in run_complete_task_ui() function (accept 'c' or 'i', case-insensitive)
- [X] T010 [US1] Implement task ID prompt "Enter task ID: " in run_complete_task_ui() function
- [X] T011 [US1] Add task ID validation in run_complete_task_ui() function (strip whitespace, convert to int, validate with validate_task_id())
- [X] T012 [US1] Integrate mark_complete() call in run_complete_task_ui() when user selects 'c' action
- [X] T013 [US1] Add confirmation message "Task {task_id} marked as complete" in run_complete_task_ui() after successful operation
- [X] T014 [US1] Add error message handling in run_complete_task_ui() (display "Invalid ID format" or "Task not found" on ValueError)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mark Task as Incomplete (Priority: P1)

**Goal**: Users can mark completed tasks as incomplete by entering task ID, enabling correction of mistakes or reopening tasks.

**Independent Test**: Create a complete task, mark it incomplete, verify status changed to False in memory. Run view.py to confirm status reflects correctly.

### Implementation for User Story 2

- [X] T015 [US2] Implement mark_incomplete(task_id: int) -> Task function in src/complete.py that finds task by ID, creates new Task instance with completed=False, and replaces task in _tasks list
- [X] T016 [US2] Add "Task {id} is already incomplete" detection in mark_incomplete() function (when task.completed is already False)
- [X] T017 [US2] Add tests for mark_incomplete() in src/complete.py or test file (marks complete task incomplete, validates status updated, tests already-incomplete case)
- [X] T018 [US2] Integrate mark_incomplete() call in run_complete_task_ui() when user selects 'i' action
- [X] T019 [US2] Add confirmation message "Task {task_id} marked as incomplete" in run_complete_task_ui() after successful operation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Handle Invalid Task IDs (Priority: P2)

**Goal**: Users receive clear, actionable error messages for invalid task IDs (format errors, non-existent IDs, empty input).

**Independent Test**: Enter various invalid IDs (negative, zero, non-integer, whitespace, non-existent numbers) and verify appropriate error messages appear.

### Implementation for User Story 3

- [X] T020 [US3] Add empty/whitespace input validation in run_complete_task_ui() for action selection (strip before checking)
- [X] T021 [US3] Add empty/whitespace input validation in run_complete_task_ui() for task ID (strip before converting)
- [X] T022 [US3] Add specific error message "Invalid ID format" in run_complete_task_ui() for non-integer or negative/zero IDs
- [X] T023 [US3] Add specific error message "Task not found" in run_complete_task_ui() for non-existent task IDs
- [X] T024 [US3] Add tests for invalid ID handling in src/complete.py or test file (non-integer, negative, zero, non-existent, empty, whitespace)
- [X] T025 [US3] Add "No tasks to update. Add tasks first." message in run_complete_task_ui() when _tasks list is empty

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T026 Add loop to run_complete_task_ui() allowing user to mark multiple tasks in one session with prompt "Mark another task? (y/n): "
- [X] T027 Add exit when user enters anything other than 'y' at continue prompt in run_complete_task_ui()
- [X] T028 Add header "=== Mark Task Complete / Incomplete ===" at start of run_complete_task_ui() function
- [X] T029 Add main execution block in src/complete.py (if __name__ == "__main__": call run_complete_task_ui())
- [X] T030 Add blank line for readability between operations in run_complete_task_ui() function
- [X] T031 [P] Manual test: Run src/complete.py, mark multiple tasks complete/incomplete, verify view.py shows updated statuses correctly
- [X] T032 [P] Manual test: Run src/complete.py with no tasks added (verify "No tasks to update" message)
- [X] T033 [P] Manual test: Run src/complete.py with various invalid inputs (negative ID, letters, large numbers) and verify error messages

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (T001, T002) - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion (T003, T004)
  - User stories can then proceed sequentially in priority order (US1 → US2 → US3)
  - Or in parallel if team capacity allows
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (T003, T004) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (T003, T004) - Integrates with UI from US1 but independently testable
- **User Story 3 (P2)**: Can start after Foundational (T003, T004) - Integrates with UI from US1/US2 but independently testable

### Within Each User Story

- Core functions (mark_complete, mark_incomplete) before UI integration
- Tests should be added with or immediately after implementation
- Error handling should be added to validate_task_id before using in UI
- UI integration last (calls core functions and displays results)

### Parallel Opportunities

- All Setup tasks (T001, T002) can run in parallel if needed
- All Foundational tasks marked [P] (T004) can run in parallel with T003 (different code paths)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Tests within each story can run in parallel with implementation of other stories
- Manual tests in Polish phase (T031, T032, T033) can run in parallel

---

## Parallel Example: User Story 1

```bash
# Tasks T006 and T007 (tests + "already complete" detection) can run together:
Task: "Add 'Task {id} is already complete' detection in mark_complete() function"
Task: "Add tests for mark_complete() in src/complete.py or test file"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001, T002)
2. Complete Phase 2: Foundational (T003, T004) - CRITICAL - blocks all stories
3. Complete Phase 3: User Story 1 (T005-T014)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Run src/add.py to create tasks
   - Run src/complete.py to mark tasks complete
   - Run src/view.py to verify status updates reflected
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Polish Phase → Final testing and refinement

Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T004)
2. Once Foundational is done:
   - Developer A: User Story 1 (T005-T014)
   - Developer B: User Story 2 (T015-T019)
   - Developer C: User Story 3 (T020-T025)
3. Polish phase completed together (T026-T033)
4. Stories integrate at UI level but are independently testable

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Core functions (mark_complete, mark_incomplete) separate from UI for reusability
- validate_task_id() helper ensures consistent error handling across stories
- Frozen dataclass pattern: create new Task instance with updated completed field
- Status updates automatically reflected in _tasks list, visible to view.py and other features
- Manual tests in Polish phase verify full workflow (add → complete → view)

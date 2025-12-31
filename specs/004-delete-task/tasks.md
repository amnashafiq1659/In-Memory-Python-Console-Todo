# Tasks: Delete Task

**Input**: Design documents from `/specs/004-delete-task/`
**Prerequisites**: plan.md, spec.md
**Available Docs**: research.md, data-model.md, quickstart.md

**Tests**: Manual testing per spec (no automated tests requested)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

No setup tasks needed - project structure already exists with src/ directory and existing add.py, view.py, and update.py modules.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

No foundational tasks needed - we're extending existing codebase with same data model and storage pattern.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Delete Task by ID (Priority: P1) 🎯 MVP

**Goal**: Allow users to delete existing tasks by entering their unique ID

**Independent Test**: Can be fully tested by creating tasks, then selecting them by ID and deleting them, verifying that they are removed from memory. This delivers the core value of allowing users to manage task lifecycle by removing completed or unwanted tasks.

### Implementation for User Story 1

- [X] T001 [US1] Implement find_task_by_id(task_id: int) -> Task | None helper function in src/delete.py
- [X] T002 [US1] Implement validate_task_id(task_id: int) -> int function with error handling in src/delete.py
- [X] T003 [US1] Implement delete_task(task_id: int) -> None core function in src/delete.py
- [X] T004 [US1] Implement prompt_for_task_id() -> int helper function in src/delete.py
- [X] T005 [US1] Implement display_task_details(task: Task) -> None helper function in src/delete.py
- [X] T006 [US1] Implement prompt_for_confirmation() -> bool helper function in src/delete.py
- [X] T007 [US1] Implement run_delete_task_ui() -> None main console interface in src/delete.py
- [X] T008 [US1] Add if __name__ == "__main__": entry point block in src/delete.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Invalid Task Deletion (Priority: P2)

**Goal**: Display clear error messages when user enters non-existent or invalid task IDs

**Independent Test**: Can be tested by entering invalid task IDs and verifying appropriate error messages are displayed without crashes or data corruption. This delivers value by ensuring users understand when their input is incorrect and can recover gracefully.

### Implementation for User Story 2

- [X] T009 [US2] Add handle_invalid_id(error_msg: str) -> None error display function in src/delete.py
- [X] T010 [US2] Add handle_non_numeric_id() -> None error display function in src/delete.py
- [X] T011 [US2] Enhance run_delete_task_ui() with error handling for invalid IDs in src/delete.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T012 [P] Add code comments and docstrings to src/delete.py
- [X] T013 [P] Validate against quickstart.md examples
- [X] T014 Manual test: Run delete task scenarios from spec acceptance criteria
- [X] T015 Manual test: Verify integration with add.py and view.py modules

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: N/A - no tasks required
- **Foundational (Phase 2)**: N/A - no tasks required
- **User Stories (Phase 3-4)**: All work in src/delete.py, must complete sequentially within each phase
- **Polish (Phase 5)**: Depends on User Story 2 completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start immediately - creates core delete.py file
- **User Story 2 (P2)**: Depends on US1 completion - enhances existing run_delete_task_ui() with error handling

### Within Each User Story

- User Story 1: Helper functions (T001-T002) → Core delete function (T003) → UI helpers (T004-T006) → Main UI (T007) → Entry point (T008)
- User Story 2: Error handlers (T009-T010) → Integrate into UI (T011)

### Parallel Opportunities

- All Polish tasks marked [P] can run in parallel
- Within User Story 1: Helper functions (T001-T002) can be implemented in parallel
- Within User Story 2: Error handlers (T009-T010) can be implemented in parallel

---

## Parallel Example: User Story 1

```bash
# Launch helper functions together:
Task: "Implement find_task_by_id(task_id: int) -> Task | None helper function in src/delete.py"
Task: "Implement prompt_for_task_id() -> int helper function in src/delete.py"

# Then implement core delete function:
Task: "Implement delete_task(task_id: int) -> None core function in src/delete.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (N/A)
2. Complete Phase 2: Foundational (N/A)
3. Complete Phase 3: User Story 1 (T001-T008)
4. **STOP and VALIDATE**: Test User Story 1 independently with manual testing
5. Demo MVP functionality

### Incremental Delivery

1. Add User Story 1 → Test independently → MVP Deliverable
2. Add User Story 2 → Test independently → Enhanced error handling
3. Polish phase → Documentation and validation
4. Each increment adds value without breaking previous work

### Manual Testing Strategy

Since tests are not explicitly requested:
1. Test acceptance scenarios from spec.md manually
2. Verify integration with add.py (create tasks) and view.py (view updated tasks)
3. Test edge cases: invalid IDs, empty input, whitespace-only IDs
4. Confirm data integrity: deleted tasks removed from memory, other tasks remain intact

---

## Notes

- [P] tasks = different files, no dependencies (not applicable here - all work in delete.py)
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Manual testing validates functionality without automated tests
- Commit after each phase for progress tracking
- Stop at User Story 1 checkpoint to validate MVP before adding error handling
- All functions follow pattern from add.py and view.py for consistency

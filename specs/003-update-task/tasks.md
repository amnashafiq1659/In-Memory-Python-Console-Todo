# Tasks: Update Task

**Input**: Design documents from `/specs/003-update-task/`
**Prerequisites**: plan.md, spec.md
**Available Docs**: research.md, data-model.md, quickstart.md

**Tests**: Tests are OPTIONAL per spec - not explicitly requested, so manual testing only

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

No setup tasks needed - project structure already exists with src/ directory and existing add.py and view.py modules.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

No foundational tasks needed - we're extending existing codebase with same data model and storage pattern.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Update Task Title and Description (Priority: P1) 🎯 MVP

**Goal**: Allow users to update a task's title and/or description by entering its unique ID

**Independent Test**: Create tasks via add.py, then select by ID in update.py and modify title/description. Verify changes are immediately reflected in memory by running view.py. This delivers core value of modifying existing task information without recreation.

### Implementation for User Story 1

- [X] T001 [US1] Implement find_task_by_id(task_id: int) -> Task | None helper function in src/update.py
- [X] T002 [US1] Implement validate_task_id(task_id: int) -> int function with error handling in src/update.py
- [X] T003 [US1] Implement update_task(task_id: int, new_title: str | None, new_description: str | None) -> Task core function in src/update.py
- [X] T004 [US1] Implement prompt_for_task_id() -> str | None helper function in src/update.py
- [X] T005 [US1] Implement prompt_for_title() -> str | None helper function in src/update.py
- [X] T006 [US1] Implement prompt_for_description() -> str | None helper function in src/update.py
- [X] T007 [US1] Implement display_task_details(task: Task) -> None helper function in src/update.py
- [X] T008 [US1] Implement run_update_task_ui() -> None main console interface in src/update.py
- [X] T009 [US1] Add if __name__ == "__main__": entry point block in src/update.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Invalid Task Selection (Priority: P2)

**Goal**: Display clear error messages when user enters non-existent or invalid task IDs

**Independent Test**: Enter invalid task IDs (non-existent, non-numeric, negative) and verify appropriate error messages display without crashes or data corruption. Other tasks remain unchanged.

### Implementation for User Story 2

- [X] T010 [US2] Add handle_invalid_id(error_msg: str) -> None error display function in src/update.py
- [X] T011 [US2] Add handle_non_numeric_id() -> None error display function in src/update.py
- [X] T012 [US2] Enhance run_update_task_ui() with error handling for invalid IDs in src/update.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T013 [P] Add code comments and docstrings to src/update.py
- [X] T014 [P] Validate against quickstart.md examples
- [X] T015 Manual test: Run update task scenarios from spec acceptance criteria
- [X] T016 Manual test: Verify integration with add.py and view.py modules

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: N/A - no tasks required
- **Foundational (Phase 2)**: N/A - no tasks required
- **User Stories (Phase 3-4)**: All work in src/update.py, must complete sequentially within each phase
- **Polish (Phase 5)**: Depends on User Story 2 completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start immediately - creates core update.py file
- **User Story 2 (P2)**: Depends on US1 completion - enhances existing run_update_task_ui() with error handling

### Within Each User Story

- User Story 1: Helper functions (T001-T002) → Core update function (T003) → UI helpers (T004-T007) → Main UI (T008) → Entry point (T009)
- User Story 2: Error handlers (T010-T011) → Integrate into UI (T012)

### Parallel Opportunities

- All Polish tasks marked [P] can run in parallel
- Within User Story 1: Helper functions (T001-T002) and (T004-T006) can be implemented in parallel
- Within User Story 2: Error handlers (T010-T011) can be implemented in parallel

---

## Parallel Example: User Story 1

```bash
# Launch helper functions together:
Task: "Implement find_task_by_id(task_id: int) -> Task | None helper function in src/update.py"
Task: "Implement prompt_for_task_id() -> str | None helper function in src/update.py"

# Then implement core update function:
Task: "Implement update_task(task_id: int, new_title: str | None, new_description: str | None) -> Task core function in src/update.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (N/A)
2. Complete Phase 2: Foundational (N/A)
3. Complete Phase 3: User Story 1 (T001-T009)
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
3. Test edge cases: invalid IDs, empty inputs, whitespace-only titles
4. Confirm data integrity: task IDs and completion status unchanged

---

## Notes

- [P] tasks = different files, no dependencies (not applicable here - all work in update.py)
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Manual testing validates functionality without automated tests
- Commit after each phase for progress tracking
- Stop at User Story 1 checkpoint to validate MVP before adding error handling
- All functions follow pattern from add.py and view.py for consistency

# Tasks: Sort Tasks

**Input**: Design documents from `/specs/007-sort-tasks/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are NOT included in this task breakdown - tests should be created as a separate task or by using `/sp.implement` with test generation enabled.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure from plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create sort.py file and set up imports

- [x] T001 Create new file sort.py in src/sort.py
- [x] T002 Add import statement for Task from add.py in src/sort.py
- [x] T003 Add import statement for Colors from add.py in src/sort.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story sorting can be implemented

**⚠️ CRITICAL**: No user story sorting work can begin until this phase is complete

- [x] T004 Define PRIORITY_ORDER constant at module level in src/sort.py with mapping {"High": 0, "Medium": 1, "Low": 2}
- [x] T005 Implement empty list check helper function in src/sort.py to return True when tasks list is empty

**Checkpoint**: Foundation ready - user story sorting implementation can now begin in parallel

---

## Phase 3: User Story 1 - Sort Tasks by Due Date (Priority: P1) 🎯 MVP

**Goal**: Provide function to sort tasks by due date in ascending order (earliest to latest), with tasks without due dates appearing last

**Independent Test**: Create test tasks with various due dates (including None values), call sort_by_due_date(), verify chronological order and that None values appear last

### Implementation for User Story 1

- [x] T006 [US1] Implement sort_by_due_date function in src/sort.py that accepts tasks list and returns sorted list
- [x] T007 [US1] Add two-tiered sort key logic in sort_by_due_date to separate dated (tier 0) from non-dated tasks (tier 1)
- [x] T008 [US1] Add string comparison for due dates in sort_by_due_date using task.due_date as key
- [x] T009 [US1] Handle None due_date values in sort_by_due_date by placing them after all dated tasks
- [x] T010 [US1] Ensure sort_by_due_date uses Python's sorted() function for O(n log n) performance and stable sort

**Checkpoint**: At this point, due date sorting should be fully functional

---

## Phase 4: User Story 2 - Sort Tasks by Priority (Priority: P1)

**Goal**: Provide function to sort tasks by priority in order High → Medium → Low, maintaining relative order within same priority level

**Independent Test**: Create test tasks with mixed priorities (including duplicates), call sort_by_priority(), verify High tasks appear first, then Medium, then Low, with relative order preserved for same priorities

### Implementation for User Story 2

- [x] T011 [US2] Implement sort_by_priority function in src/sort.py that accepts tasks list and returns sorted list
- [x] T012 [US2] Add PRIORITY_ORDER dictionary lookup in sort_by_priority to map priority strings to numeric values
- [x] T013 [US2] Handle unexpected priority values in sort_by_priority by treating them as Medium (value 1)
- [x] T014 [US2] Ensure sort_by_priority uses Python's sorted() function for O(n log n) performance and stable sort

**Checkpoint**: At this point, priority sorting should be fully functional

---

## Phase 5: User Story 3 - Sort Tasks by Title (Priority: P2)

**Goal**: Provide function to sort tasks alphabetically by title (A-Z) using case-insensitive comparison

**Independent Test**: Create test tasks with various titles (different cases, special characters), call sort_by_title(), verify alphabetical order is case-insensitive

### Implementation for User Story 3

- [x] T015 [US3] Implement sort_by_title function in src/sort.py that accepts tasks list and returns sorted list
- [x] T016 [US3] Add case-insensitive comparison in sort_by_title using task.title.lower() as sort key
- [x] T017 [US3] Ensure sort_by_title handles special characters and Unicode in task titles via standard string comparison
- [x] T018 [US3] Ensure sort_by_title uses Python's sorted() function for O(n log n) performance and stable sort

**Checkpoint**: At this point, title sorting should be fully functional

---

## Phase 6: User Story 4 - Handle Empty Task List Gracefully (Priority: P1)

**Goal**: Display clear, user-friendly message when no tasks exist instead of showing errors or empty output

**Independent Test**: Attempt to sort an empty task list, verify message "No tasks found" displays with instructions, no errors shown

### Implementation for User Story 4

- [x] T019 [US4] Add empty list check at start of display_tasks function in src/sort.py
- [x] T020 [US4] Display user-friendly message using Colors when tasks list is empty in display_tasks
- [x] T021 [US4] Add early return in display_tasks when empty list is detected to prevent further processing

**Checkpoint**: At this point, empty list handling should be fully functional

---

## Phase 7: Display Function (Cross-Cutting for US1, US2, US3, US4)

**Purpose**: Display sorted tasks with colored status and priority indicators, used by all three sorting user stories

- [x] T022 Implement display_tasks function in src/sort.py that accepts tasks list and prints to console
- [x] T023 [P] Add status indicator logic in display_tasks to show [X] for completed, [ ] for incomplete using Colors.GREEN and Colors.YELLOW
- [x] T024 [P] Add priority color coding in display_tasks to use Colors.RED for High, Colors.ORANGE for Medium, Colors.BLUE for Low
- [x] T025 [P] Display task ID and title in display_tasks using Colors.BOLD and Colors.CYAN
- [x] T026 [P] Display task description in display_tasks using Colors.DIM_CYAN
- [x] T027 [P] Display category and due date (if present) in display_tasks using Colors.PINK and Colors.PURPLE
- [x] T028 [P] Add task count summary at end of display_tasks function

**Checkpoint**: Display function complete - can be used by all sorting user stories

---

## Phase 8: UI Function (Cross-Cutting for US1, US2, US3)

**Purpose**: Interactive console UI for selecting sorting options, executing sort, and displaying results

- [x] T029 Implement run_sort_ui function in src/sort.py that accepts tasks list as parameter
- [x] T030 Add empty list check in run_sort_ui to call display_tasks with empty list and return early
- [x] T031 Display menu with three sorting options in run_sort_ui: 1) Sort by Title, 2) Sort by Priority, 3) Sort by Due Date
- [x] T032 Add user input prompt in run_sort_ui with validation to accept only 1, 2, or 3
- [x] T033 Add routing logic in run_sort_ui to call sort_by_title, sort_by_priority, or sort_by_due_date based on user selection
- [x] T034 Call display_tasks with sorted results in run_sort_ui
- [x] T035 Add error handling for invalid input in run_sort_ui to reprompt user instead of crashing

**Checkpoint**: UI function complete - provides user interaction for all sorting options

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, validation, and final improvements

- [x] T036 Add module-level docstring to src/sort.py explaining the sorting functionality and API
- [x] T037 Add function docstrings to all public functions in src/sort.py (sort_by_title, sort_by_priority, sort_by_due_date, display_tasks, run_sort_ui)
- [x] T038 Verify all sorting functions return new lists and do not modify original task data (FR-009)
- [x] T039 Verify empty list message displays correctly in all sorting paths (FR-008)
- [x] T040 Verify color codes match patterns used in view.py for consistency (FR-006, FR-007)
- [x] T041 Test sorting performance with typical task lists (<1000 tasks) to confirm <1 second response time (SC-001, SC-002, SC-003)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user story sorting
- **User Stories (Phases 3-5)**: All depend on Foundational phase completion
  - User stories can proceed in parallel after Foundational (US1, US2, US3 can be done simultaneously)
- **Display (Phase 7)**: Can start in parallel with user stories but needs T002 (Colors import) and T019 (empty check)
- **UI (Phase 8)**: Depends on sorting functions (Phases 3-5) and display function (Phase 7)
- **Polish (Phase 9)**: Depends on all implementation phases (Phases 1-8) complete

### User Story Dependencies

- **User Story 1 (US1 - Due Date)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (US2 - Priority)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (US3 - Title)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (US4 - Empty List)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models/Entities: None (reuses Task from add.py)
- Sorting functions: US1 (T006-T010), US2 (T011-T014), US3 (T015-T018)
- Each sort function is independent and testable

### Parallel Opportunities

- **Setup (Phase 1)**: T002 and T003 can run in parallel (different imports)
- **Foundational (Phase 2)**: T004 and T005 can run in parallel
- **User Stories (Phases 3-5)**: After Foundational complete, all three sorting user stories (US1, US2, US3) can proceed in parallel
  - US1 tasks: T006-T010 are sequential (within US1)
  - US2 tasks: T011-T014 are sequential (within US2)
  - US3 tasks: T015-T018 are sequential (within US3)
- **Display (Phase 7)**: T023-T028 can run in parallel (different display components)
- **Polish (Phase 9)**: T038-T041 can run in parallel (verification tasks)

---

## Parallel Example: User Stories After Foundational

```bash
# After Foundational (Phase 2) completes, launch all three sorting stories in parallel:

# User Story 1 - Due Date (one developer):
Task: "Implement sort_by_due_date function in src/sort.py"
Task: "Add two-tiered sort key logic in sort_by_due_date"
Task: "Add string comparison for due dates in sort_by_due_date"
Task: "Handle None due_date values in sort_by_due_date"
Task: "Ensure sort_by_due_date uses Python's sorted() function"

# User Story 2 - Priority (second developer, can start in parallel):
Task: "Implement sort_by_priority function in src/sort.py"
Task: "Add PRIORITY_ORDER dictionary lookup in sort_by_priority"
Task: "Handle unexpected priority values in sort_by_priority"
Task: "Ensure sort_by_priority uses Python's sorted() function"

# User Story 3 - Title (third developer, can start in parallel):
Task: "Implement sort_by_title function in src/sort.py"
Task: "Add case-insensitive comparison in sort_by_title"
Task: "Ensure sort_by_title handles special characters and Unicode"
Task: "Ensure sort_by_title uses Python's sorted() function"
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, 4 Only - Recommended)

Since US1, US2, and US4 are all P1 and US3 is P2, MVP approach is:

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T005)
3. Complete Phase 3: User Story 1 - Due Date (T006-T010) - P1
4. Complete Phase 4: User Story 2 - Priority (T011-T014) - P1
5. Complete Phase 6: User Story 4 - Empty List (T019-T021) - P1
6. Complete Phase 7: Display Function (T022-T028)
7. Complete Phase 8: UI Function (T029-T035)
8. **STOP and VALIDATE**: Test all three sorting options with empty list handling
9. Deploy/demo if ready

**Value**: Users can sort by due date and priority (two most critical sorting options) with proper empty list handling.

### Incremental Delivery

1. Complete Setup + Foundational (Phases 1-2) → Foundation ready
2. Add User Story 1 (Due Date) + Display + UI → Test independently → Deploy (MVP option A)
3. Add User Story 2 (Priority) + Update UI → Test independently → Deploy (MVP option B)
4. Add User Story 3 (Title) + Update UI → Test independently → Deploy (Complete feature)
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers (3+):

1. Team completes Setup + Foundational together (Phases 1-2)
2. Once Foundational is done:
   - Developer A: User Story 1 (Due Date) - T006-T010
   - Developer B: User Story 2 (Priority) - T011-T014
   - Developer C: User Story 3 (Title) - T015-T018
3. Developer A (after US1): Display function (Phase 7) - T022-T028
4. Developer B (after US2): UI function (Phase 8) - T029-T035
5. Team: Polish and validation (Phase 9) - T036-T041

---

## Summary

**Total Tasks**: 41
**Task Count by User Story**:
- Setup (Phase 1): 3 tasks
- Foundational (Phase 2): 2 tasks
- User Story 1 (Due Date - P1): 5 tasks
- User Story 2 (Priority - P1): 4 tasks
- User Story 3 (Title - P2): 4 tasks
- User Story 4 (Empty List - P1): 3 tasks
- Display Function (Phase 7): 7 tasks
- UI Function (Phase 8): 7 tasks
- Polish (Phase 9): 6 tasks

**Parallel Opportunities**:
- Setup imports: 2 tasks (T002, T003)
- Foundational: 2 tasks (T004, T005)
- User stories (after Foundational): 3 stories can proceed in parallel
- Display function components: 6 tasks (T023-T028)
- Polish verification: 4 tasks (T038-T041)

**Independent Test Criteria per Story**:
- **US1 (Due Date)**: Create tasks with various due dates, sort, verify chronological order and None values appear last
- **US2 (Priority)**: Create tasks with mixed priorities, sort, verify High→Medium→Low order with relative order preserved
- **US3 (Title)**: Create tasks with various titles, sort, verify alphabetical case-insensitive order
- **US4 (Empty List)**: Attempt to sort empty list, verify message displays without errors

**Suggested MVP Scope**: User Stories 1, 2, 4 (due date, priority sorting, and empty list handling) - 19 tasks (Phases 1-2, 3-4, 6, 7-8, partial 9)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Tasks in same phase/story that are not marked [P] are sequential
- Tests were not included in this breakdown as not explicitly requested - should be added separately
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- The user input mentioned `sort_by_title(order="asc")` and `sort_tasks(sort_type: str)` but these were not in the plan.md contracts, so tasks follow the approved plan.md contracts

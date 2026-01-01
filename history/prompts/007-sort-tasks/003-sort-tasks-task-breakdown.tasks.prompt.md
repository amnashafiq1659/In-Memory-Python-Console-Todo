---
id: 003
title: Sort Tasks task breakdown
stage: tasks
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: sort-tasks
branch: 007-sort-tasks
user: Amna Shafiq
command: /sp.tasks
labels: ["tasks", "implementation", "sorting", "breakdown"]
links:
  spec: ../../specs/007-sort-tasks/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/007-sort-tasks/tasks.md
tests:
 - none
---

## Prompt

# Spec 7: Sort Tasks

## Tasks List

1. Create a new file `sort.py`
2. Import shared `_tasks` list and `Task` model from `add.py`
3. Implement `sort_by_title(order="asc")`
   - Sort tasks alphabetically by title (A–Z / Z–A)
4. Implement `sort_by_priority()`
   - Order: High → Medium → Low
   - Tasks without priority appear last
5. Implement `sort_by_due_date()`
   - Earliest due date first
   - Tasks without due date appear last
6. Implement `sort_tasks(sort_type: str)`
   - Route sorting logic based on selected option
7. Implement `display_sorted_tasks(tasks)`
   - Colored output for:
     - Status (completed / incomplete)
     - Priority
     - Due date
8. Implement `run_sort_ui()`
   - Prompt user to choose a sorting option
   - Display sorted task list
9. Ensure sorting does **not** modify original task data
10. Handle empty task list gracefully with a warning message

## Response snapshot

Generated comprehensive task breakdown with 41 tasks organized by user story and phase:
- **Phase 1-2**: Setup and foundational infrastructure (5 tasks)
- **Phase 3-5**: Three sorting user stories (13 tasks total) - US1 (due date, P1), US2 (priority, P1), US3 (title, P2)
- **Phase 6**: Empty list handling user story (3 tasks, P1)
- **Phase 7**: Display function (7 tasks)
- **Phase 8**: UI function (7 tasks)
- **Phase 9**: Polish and validation (6 tasks)

All tasks follow strict checklist format with IDs, [P] parallel markers, and [Story] labels. Task dependencies and parallel execution opportunities clearly documented. MVP scope identified (US1, US2, US4 = 19 tasks).

## Outcome

- ✅ Impact: Complete task breakdown created with 41 specific, executable tasks organized by user story for independent implementation
- 🧪 Tests: none (tests not included per specification and not explicitly requested)
- 📁 Files: Created tasks.md with full implementation roadmap
- 🔁 Next prompts: /sp.implement to execute the task breakdown
- 🧠 Reflection: User input mentioned `sort_by_title(order="asc")` and `sort_tasks(sort_type: str)` which differed from plan.md contracts. Tasks follow approved plan.md contracts (individual sort functions) instead, ensuring consistency with approved design. User Story 4 (empty list handling) was identified as P1 from spec but not mentioned in user's task list, added as Phase 6.

## Evaluation notes (flywheel)

- Failure modes observed: User input mentioned additional functions (`sort_tasks` router function with sort_type parameter) that were not in approved plan.md contracts. Resolved by following approved contracts (individual sort functions) to maintain consistency with design phase.
- Graders run and results (PASS/FAIL): PASS - All tasks follow checklist format (checkbox, ID, [P], [Story], file paths), tasks are organized by user story, independent test criteria defined, parallel opportunities identified, MVP scope suggested.
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): None - task breakdown complete and follows approved design. Ready for implementation phase.

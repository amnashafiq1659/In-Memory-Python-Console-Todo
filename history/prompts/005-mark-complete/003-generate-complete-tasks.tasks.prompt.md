---
id: 3
title: generate-complete-tasks
stage: tasks
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 005-mark-complete
branch: 005-mark-complete
user: unknown
command: /sp.tasks
labels: [tasks,implementation,task-management,console-application]
links:
  spec: specs/005-mark-complete/spec.md
  plan: specs/005-mark-complete/plan.md
  tasks: specs/005-mark-complete/tasks.md
  ticket: null
  adr: null
  pr: null
files:
- specs/005-mark-complete/tasks.md
tests:
- Task organization validation: PASS (all tasks follow checklist format)
- User story mapping: PASS (all tasks mapped to US1, US2, US3)
- File path inclusion: PASS (all tasks include exact file paths)

---

## Prompt

# Spec 5: Tasks Prompt

Create a **list of implementation tasks** for Spec 5: Mark Task Complete / Incomplete for an in-memory Python console Todo application.

Tasks should include:

1. **Retrieve Task by ID**
   - Ask user to enter the unique ID of the task
   - Check if the task exists in the in-memory collection
   - Handle invalid or non-existing IDs gracefully

2. **Implement Completion Toggle Function**
   - Function to mark a task as complete
   - Function to mark a task as incomplete (or a single toggle function)
   - Update the task's completion status in memory

3. **Implement Console Flow**
   - Prompt user for task ID
   - Ask whether to mark as complete or incomplete
   - Call appropriate function
   - Confirm status update to the user

4. **Test Completion Status**
   - Mark multiple tasks as complete and incomplete
   - Verify status updates correctly in memory
   - Test invalid ID handling

5. **Save File**
   - Implement all above in a single Python file: `complete.py` inside `/src`

## Response snapshot

Successfully generated implementation tasks for Spec 5: Mark Task Complete / Incomplete.

**Generated File**: `specs/005-mark-complete/tasks.md`

**Task Summary**:
- Total Tasks: 33 (T001-T033)
- Task Count by User Story:
  - User Story 1 (Mark Complete - P1): 10 tasks (T005-T014)
  - User Story 2 (Mark Incomplete - P1): 5 tasks (T015-T019)
  - User Story 3 (Invalid IDs - P2): 6 tasks (T020-T025)
- Setup/Foundational: 4 tasks (T001-T004)
- Polish/Cross-cutting: 8 tasks (T026-T033)

**Organization**:
- Tasks organized by user story for independent implementation
- Each story includes core functions, UI integration, error handling, and tests
- Phase structure enables incremental delivery

**Independent Test Criteria**:
- US1: Create incomplete task, mark complete, verify status changed to True
- US2: Create complete task, mark incomplete, verify status changed to False
- US3: Enter invalid IDs, verify appropriate error messages appear

**Format Validation**: All tasks follow checklist format with checkboxes, IDs, story labels, and file paths.

## Outcome

- ✅ Impact: Generated 33 implementation tasks organized by user story for independent development and testing
- 🧪 Tests: Task format validated, independent test criteria defined for each user story
- 📁 Files: Created specs/005-mark-complete/tasks.md
- 🔁 Next prompts: `/sp.implement` to execute the tasks, or manual task execution
- 🧠 Reflection: Tasks enable incremental delivery - US1 provides MVP, US2 adds toggle flexibility, US3 adds error handling.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Task format validation (PASS), Story mapping validation (PASS)
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None - tasks are complete and ready for implementation

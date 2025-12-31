---
id: 3
title: create-update-task-tasks
stage: tasks
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5
feature: update-task
branch: 003-update-task
user: user
command: /sp.tasks
labels: [tasks, update-task, implementation]
links:
  spec: specs/003-update-task/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/003-update-task/tasks.md
tests:
  - Manual testing per user stories
---

## Prompt

# Spec 3: Tasks Prompt

Create a **list of implementation tasks** for Spec 3: Update Task for an in-memory Python console Todo application.

Tasks should include:

1. **Retrieve Task by ID**
   - Ask user to enter unique ID of task to update
   - Check if task exists in-memory collection
   - Handle invalid or non-existing IDs gracefully

2. **Implement Update Task Function**
   - Function to update title and/or description of selected task
   - Accept new values from user
   - Save changes in memory

3. **Implement Console Flow**
   - Display prompt for task ID
   - Ask for new title (allow skipping if user wants to keep current)
   - Ask for new description (allow skipping)
   - Call update function
   - Confirm update success to user

4. **Test Updating Tasks**
   - Update multiple tasks and verify changes in memory
   - Test invalid ID handling

5. **Save File**
   - Implement all above in a single Python file: `update.py` inside `/src`

## Response snapshot

Generated comprehensive task list for Update Task feature organized by user stories:

**Phase 1 & 2**: No setup/foundational tasks needed - extending existing codebase

**Phase 3 - User Story 1 (P1) - MVP**: 9 tasks
- Helper functions: find_task_by_id(), validate_task_id(), prompt functions, display_task_details()
- Core function: update_task() with validation and in-memory updates
- Main UI: run_update_task_ui() with console interaction flow
- Entry point: if __name__ == "__main__"

**Phase 4 - User Story 2 (P2)**: 3 tasks
- Error handlers for invalid IDs and non-numeric input
- Integration into main UI function

**Phase 5 - Polish**: 4 tasks
- Documentation, quickstart validation, manual testing scenarios, integration testing

**Total**: 16 tasks organized by user story with clear dependencies
- Each story independently implementable and testable
- MVP = US1 only (T001-T009)
- Incremental delivery with error handling (US2) then polish

## Outcome

- ✅ Impact: Generated 16 testable implementation tasks organized by user story
- 🧪 Tests: Manual testing per spec (no automated tests requested)
- 📁 Files: Created tasks.md with task checklist, dependencies, parallel opportunities
- 🔁 Next prompts: /sp.implement to execute all tasks and build src/update.py
- 🧠 Reflection: Tasks are granular and specific, following plan.md design decisions. Each task has clear file path and purpose. User story organization enables MVP delivery (US1) followed by error handling (US2).

## Evaluation notes (flywheel)

- Failure modes observed: None - task generation completed successfully
- Graders run and results (PASS/FAIL): All tasks follow checklist format ✅
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A

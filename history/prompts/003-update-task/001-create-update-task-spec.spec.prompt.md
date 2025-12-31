---
id: 1
title: create-update-task-spec
stage: spec
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5
feature: update-task
branch: 003-update-task
user: user
command: /sp.specify
labels: [spec, update-task]
links:
  spec: specs/003-update-task/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/003-update-task/spec.md
  - specs/003-update-task/checklists/requirements.md
tests:
  - None (specification phase)
---

## Prompt

# Spec 3: Update Task

## Overview
Spec 3 covers updating existing tasks for Phase I of an in-memory Python console Todo application.

## Scope
- Implement functionality to **update a task's title and description** using its unique ID.
- Access tasks stored in memory (from Spec 1).
- Only one Python file must be created for this spec, named `update.py` inside the `/src` folder.

## Constraints
- Follow clean code principles.
- Console-based interaction only.
- Do not include add, delete, view, or completion toggle functionality in this spec.

## Acceptance Criteria
- The user can select a task by entering its unique ID.
- The user can update the task's title and/or description.
- Changes are reflected in memory during runtime.
- All functionality is implemented in a single file: `update.py`.

## Response snapshot

Created specification for Update Task feature with the following components:

**User Stories**:
- P1: Update Task Title and Description - Core functionality to modify existing tasks by ID
- P2: Handle Invalid Task Selection - Error handling for non-existent task IDs

**Functional Requirements** (FR-001 through FR-012):
- Task selection by unique ID
- Update title, description, or both
- Validation and error handling
- Immediate memory reflection
- Data integrity preservation

**Success Criteria**:
- Complete updates in under 10 seconds
- 100% reflection of changes in memory
- 100% correct error handling for invalid IDs
- Zero data corruption

**Quality Validation**: All checklist items passed - specification is complete, testable, technology-agnostic, and ready for planning.

## Outcome

- ✅ Impact: Complete specification created for Update Task feature with clear requirements, user stories, and measurable success criteria
- 🧪 Tests: Specification phase - no tests yet
- 📁 Files: Created spec.md and requirements.md checklist
- 🔁 Next prompts: /sp.plan to create implementation plan, then /sp.implement to build update.py
- 🧠 Reflection: Specification is clear and complete with no clarification needed. All edge cases identified, requirements are testable, and success criteria are measurable.

## Evaluation notes (flywheel)

- Failure modes observed: None - specification generation completed successfully
- Graders run and results (PASS/FAIL): All quality validation checks PASSED
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A

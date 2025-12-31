---
id: 2
title: create-mark-complete-plan
stage: plan
date: 2025-12-31
surface: agent
model: claude-sonnet-4-5-20250929
feature: 005-mark-complete
branch: 005-mark-complete
user: unknown
command: /sp.plan
labels: [planning,architecture,task-management,console-application]
links:
  spec: specs/005-mark-complete/spec.md
  plan: specs/005-mark-complete/plan.md
  ticket: null
  adr: null
  pr: null
files:
- specs/005-mark-complete/plan.md
- specs/005-mark-complete/research.md
- specs/005-mark-complete/data-model.md
- specs/005-mark-complete/contracts/complete.md
- specs/005-mark-complete/quickstart.md
tests:
- Constitution check: PASSED (no violations)

---

## Prompt

# Spec 5: Plan Prompt

Create a **development plan** for Spec 5: Mark Task Complete / Incomplete for an in-memory Python console Todo application.

## Scope
- Mark a task as complete using its unique task ID.
- Mark a task as incomplete using its unique task ID.
- Update the task's completion status in memory.
- Only one Python file: `complete.py` inside the `/src` folder.

## Plan Requirements
- List all functions or classes needed

- Define responsibilities for each function/class:
  - Accept task ID from user
  - Verify task existence
  - Update completion status
  - Handle invalid or non-existing IDs gracefully
- Include console interaction flow for marking tasks complete/incomplete
- Ensure updated status is reflected in memory
- Follow clean code principles

## Response snapshot

Successfully created implementation plan for Spec 5: Mark Task Complete / Incomplete.

**Generated Artifacts**:
1. `specs/005-mark-complete/plan.md` - Complete implementation plan
2. `specs/005-mark-complete/research.md` - Phase 0 research decisions (9 topics)
3. `specs/005-mark-complete/data-model.md` - Phase 1 data model documentation
4. `specs/005-mark-complete/contracts/complete.md` - Phase 1 function contracts
5. `specs/005-mark-complete/quickstart.md` - Phase 1 quickstart guide

**Key Design Decisions**:
- Import Task dataclass and `_tasks` list from `src/add.py` (consistent with Specs 002-004)
- Create new Task instances for mutation (frozen dataclass pattern)
- Linear search for task lookup (O(n) - acceptable for 1,000+ tasks)
- Separate functions: `mark_complete()`, `mark_incomplete()`, `validate_task_id()`, `run_complete_task_ui()`
- Console UI follows existing `run_*_ui()` pattern
- Validation: early ID validation, specific error messages

**Constitution Check**: PASSED - No violations, maintains simplicity and single-responsibility

## Outcome

- ✅ Impact: Complete architectural plan for task completion status management
- 🧪 Tests: Constitution check passed, ready for task generation
- 📁 Files: Created plan.md, research.md, data-model.md, contracts/complete.md, quickstart.md
- 🔁 Next prompts: `/sp.tasks` to generate testable implementation tasks
- 🧠 Reflection: Plan reuses existing patterns from Specs 002-004, ensuring consistency across the codebase.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Constitution check (PASS)
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None - plan is complete and ready for implementation

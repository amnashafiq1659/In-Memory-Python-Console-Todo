---
id: 005
title: Enhance Add Task Model with Priority, Category, and Due Date
stage: green
date: 2025-12-31
surface: agent
model: claude-sonnet-4.5-20250929
feature: add-task
branch: main
user: Amna Shafiq
command: "Enhance the existing Add Task functionality to improve task organization by extending the Task model with additional attributes"
labels: ["enhancement", "task-model", "attributes"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - src/add.py
tests:
  - Manual test: Created tasks with all enhanced attributes (priority, category, due_date)
  - Manual test: Verified default values (Medium, General, None)
  - Manual test: Verified partial attribute creation
  - Manual test: Confirmed in-memory storage persistence
---

## Prompt

Enhance the existing Add Task functionality to improve task organization by extending the Task model with additional attributes.

### Task Model Enhancements
Extend the existing `Task` model to include:
- `priority` → High / Medium / Low
- `category` → user-defined label (e.g., Work, Home, Personal)
- `due_date` → optional value (string-based)

The following fields must remain unchanged:
- unique ID
- title
- description
- completion status (default: incomplete)

### Add Task Enhancements
- Update the Add Task console flow to prompt for:
  - priority
  - category
  - optional due date

## Constraints
- Modify **only `add.py`**.
- No new Python files should be created.
- No changes to view, update, delete, search, sort, or completion logic.
- Console-based interaction only.
- No file or database persistence.
- Follow clean code principles.

## Acceptance Criteria
- User can add a task with title, description, priority, category, and optional due date.
- Each task still receives a unique ID.
- All tasks are stored in shared in-memory storage during runtime.
- Existing basic-level functionality continues to work without breaking.

## Response snapshot

Successfully enhanced the Add Task functionality by:

1. Extended the Task dataclass with three new attributes:
   - `priority: str = "Medium"` (defaults to Medium)
   - `category: str = "General"` (defaults to General)
   - `due_date: str | None = None` (optional, defaults to None)

2. Updated the `add_task()` function to accept these new parameters with appropriate defaults:
   ```python
   def add_task(title: str, description: str, priority: str = "Medium",
                 category: str = "General", due_date: str | None = None) -> Task
   ```

3. Enhanced the `run_add_task_ui()` console interface with new prompts:
   - Priority: Validates user input against High/Medium/Low with default fallback to Medium
   - Category: User-defined label with default fallback to General
   - Due Date: Optional prompt that defaults to None if skipped

4. Verified functionality through manual testing:
   - Tasks created with all enhanced attributes work correctly
   - Default values (Medium, General, None) apply when not specified
   - Partial attribute creation (priority and category without due date) works
   - All tasks persist in shared in-memory storage
   - Existing functionality (ID generation, completed status, title, description) remains intact

## Outcome

- ✅ Impact: Enhanced task organization capabilities by adding priority, category, and due_date attributes while maintaining backward compatibility
- 🧪 Tests: Manual tests confirmed all scenarios work correctly - full attributes, defaults, partial attributes, and in-memory storage
- 📁 Files: Modified only `src/add.py` as specified
- 🔁 Next prompts: No immediate next prompts required
- 🧠 Reflection: The implementation followed clean code principles, used sensible defaults, and maintained the existing dataclass structure. The frozen=True property of the dataclass remains unchanged, and the new attributes have appropriate defaults to support existing code patterns.

## Evaluation notes (flywheel)

- Failure modes observed: None during implementation
- Graders run and results (PASS/FAIL): N/A (manual testing)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): None required

---
id: 005
title: Enhance View Tasks Display with Additional Attributes
stage: green
date: 2025-12-31
surface: agent
model: claude-sonnet-4.5-20250929
feature: view-tasks
branch: main
user: Amna Shafiq
command: "Enhance the task viewing experience to improve usability and clarity by displaying additional task attributes and providing a more informative task overview"
labels: ["enhancement", "view-display", "color-coding"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - src/view.py
tests:
  - Manual test: Created tasks with various priorities (High, Medium, Low), categories, and due dates
  - Manual test: Verified completed vs incomplete task distinction with color indicators
  - Manual test: Confirmed priority color coding (Red=High, Orange=Medium, Blue=Low)
  - Manual test: Verified category display with pink color
  - Manual test: Confirmed due date display with purple color only when available
  - Manual test: Verified output readability and console formatting
---

## Prompt

Enhance the task viewing experience to improve usability and clarity by displaying additional task attributes and providing a more informative task overview.

### View Enhancements
Update the task listing to display the following attributes for each task:
- unique ID
- title
- description
- completion status
- priority
- category
- due date (if available)

### UI Requirements
- Maintain existing ANSI color usage.
- Clearly distinguish:
  - completed vs incomplete tasks
  - priorities (High / Medium / Low)
  - categories/tags
- Keep output clean and readable in a console environment.

## Constraints
- Modify **only `view.py`**.
- No task creation, update, delete, search, sort, or completion toggle logic.
- No persistence (in-memory only).
- Console-based output only.
- Follow clean code principles.

## Acceptance Criteria
- User can view all tasks with priority, category, and due date visible.
- Tasks remain displayed from the shared in-memory task list.
- Existing basic-level view functionality continues to work without breaking.

## Response snapshot

Successfully enhanced the task viewing experience by:

1. Added two new ANSI color codes to the Colors class:
   - `PINK = '\033[38;5;206m'` - for category display
   - `PURPLE = '\033[38;5;141m'` - for due date display

2. Completely redesigned the task display format in `run_view_tasks_ui()`:
   - Implemented priority-based color coding:
     * High priority: Red + Bold
     * Medium priority: Orange + Bold
     * Low priority: Blue + Bold
   - Display format shows task details on multiple lines for better readability:
     * Line 1: Status indicator + ID + Title
     * Line 2: Description
     * Line 3: Priority + Category + Due Date (if available)
   - Due date only appears when task has a due_date value (not None)
   - Maintained existing color usage for status, ID, title, and description

3. Updated docstring to reflect new attributes displayed

## Outcome

- ✅ Impact: Enhanced task viewing with clear visual distinction of all task attributes including priority, category, and due date
- 🧪 Tests: Manual testing confirmed all scenarios work correctly - different priorities show appropriate colors, categories display in pink, due dates show in purple only when available, completed vs incomplete status clearly distinguished
- 📁 Files: Modified only `src/view.py` as specified
- 🔁 Next prompts: No immediate next prompts required
- 🧠 Reflection: The multi-line display format provides excellent readability while maintaining clean console output. Color coding makes it easy to quickly scan and identify task characteristics. The implementation follows clean code principles and maintains backward compatibility with the existing in-memory task storage system.

## Evaluation notes (flywheel)

- Failure modes observed: None during implementation
- Graders run and results (PASS/FAIL): N/A (manual testing)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): None required

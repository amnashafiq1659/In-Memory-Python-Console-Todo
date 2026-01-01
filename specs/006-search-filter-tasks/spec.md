# Feature Specification: Search & Filter Tasks

**Feature Branch**: `006-search-filter-tasks`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Allow users to easily find and organize tasks using search and filter options"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Search Tasks by Keyword (Priority: P1)

User wants to find tasks that contain specific text in either the title or description to quickly locate relevant items.

**Why this priority**: This is the core search functionality and provides the most immediate value to users by enabling them to find tasks based on content.

**Independent Test**: Can be fully tested by creating multiple tasks with different titles and descriptions, then searching for keywords to verify only matching tasks appear.

**Acceptance Scenarios**:

1. **Given** user has tasks with titles "Buy groceries", "Complete project", "Read book", **When** user searches for "groceries", **Then** only the task with "Buy groceries" in title or description is displayed
2. **Given** user has tasks with descriptions including "weekly shopping", "monthly review", **When** user searches for "weekly", **Then** only tasks containing "weekly" in title or description are displayed
3. **Given** user searches for "PROJECT", **When** system performs search, **Then** results include tasks with "project" (case-insensitive match)
4. **Given** user searches for keyword that exists in no tasks, **When** search is performed, **Then** clear message indicates no matching tasks found

---

### User Story 2 - Filter Tasks by Completion Status (Priority: P2)

User wants to view only completed tasks or only incomplete tasks to focus on specific work states.

**Why this priority**: This enables users to quickly review their progress (completed) or focus on remaining work (incomplete).

**Independent Test**: Can be fully tested by creating a mix of completed and incomplete tasks, then filtering by each status to verify correct results.

**Acceptance Scenarios**:

1. **Given** user has 3 completed and 2 incomplete tasks, **When** user filters by "complete", **Then** only the 3 completed tasks are displayed
2. **Given** user has 3 completed and 2 incomplete tasks, **When** user filters by "incomplete", **Then** only the 2 incomplete tasks are displayed
3. **Given** user has no completed tasks, **When** user filters by "complete", **Then** clear message indicates no matching tasks found

---

### User Story 3 - Filter Tasks by Priority (Priority: P2)

User wants to view tasks based on priority level to focus on high-importance items or organize work.

**Why this priority**: Helps users prioritize their workload by viewing tasks grouped by importance level.

**Independent Test**: Can be fully tested by creating tasks with different priorities (High, Medium, Low), then filtering by each priority to verify correct results.

**Acceptance Scenarios**:

1. **Given** user has 2 High, 3 Medium, and 1 Low priority tasks, **When** user filters by "High", **Then** only the 2 High priority tasks are displayed
2. **Given** user has tasks with different priorities, **When** user filters by "low", **Then** only Low priority tasks are displayed (case-insensitive)
3. **Given** user has no Medium priority tasks, **When** user filters by "Medium", **Then** clear message indicates no matching tasks found

---

### User Story 4 - Filter Tasks by Category (Priority: P3)

User wants to view tasks belonging to a specific category or tag to organize work by context (e.g., Work, Personal, Home).

**Why this priority**: Useful for users who organize tasks by project, context, or department but is secondary to search and status filtering.

**Independent Test**: Can be fully tested by creating tasks with various categories, then filtering by a specific category to verify only matching tasks appear.

**Acceptance Scenarios**:

1. **Given** user has 4 tasks with category "Work" and 3 tasks with category "Personal", **When** user filters by "Work", **Then** only the 4 Work tasks are displayed
2. **Given** user searches for category "HOME", **When** filter is applied, **Then** tasks with category "Home" are displayed (case-insensitive match)
3. **Given** user has no tasks with category "Finance", **When** user filters by "Finance", **Then** clear message indicates no matching tasks found

---

### Edge Cases

- What happens when user searches for an empty string?
  - System should treat empty search as showing all tasks (no filter applied)
- What happens when no tasks exist in memory?
  - System should display clear message that no tasks are available for searching/filtering
- What happens when user provides invalid filter value (e.g., priority "Urgent")?
  - System should display clear error message indicating valid options and prompt for correct input
- What happens when multiple criteria are applied (e.g., search + filter)?
  - System should apply both criteria and return tasks matching all conditions (AND logic)
- What happens when search term contains special characters?
  - System should handle special characters gracefully and search for the literal string

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to search for tasks by keyword matching against both title and description fields
- **FR-002**: System MUST perform keyword search in case-insensitive manner
- **FR-003**: System MUST allow users to filter tasks by completion status (complete/incomplete)
- **FR-004**: System MUST allow users to filter tasks by priority level (High/Medium/Low)
- **FR-005**: System MUST allow users to filter tasks by category/tag
- **FR-006**: System MUST perform all filter comparisons in case-insensitive manner
- **FR-007**: System MUST display only tasks matching the search or filter criteria
- **FR-008**: System MUST display clear message when no tasks match the search/filter criteria
- **FR-009**: System MUST display clear message when no tasks exist in memory
- **FR-010**: System MUST maintain existing color conventions for task display
- **FR-011**: System MUST read tasks from shared in-memory task list without modifying them
- **FR-012**: System MUST validate filter inputs and display error messages for invalid values

### Key Entities

- **Search Query**: User-provided keyword to match against task title or description fields
- **Filter Criteria**: Set of conditions (status, priority, category) used to narrow task results
- **Search Result**: Subset of tasks from in-memory storage that match provided search or filter criteria

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can locate specific tasks by keyword in under 10 seconds
- **SC-002**: 100% of keyword searches correctly match tasks regardless of case (upper/lower/mixed)
- **SC-003**: Users can filter tasks by any single criteria (status, priority, or category) in under 15 seconds
- **SC-004**: Clear error messages appear within 1 second for invalid filter inputs
- **SC-005**: Users receive feedback about no matching results in under 2 seconds
- **SC-006**: All displayed results maintain existing color coding for task attributes (status, priority, category)
- **SC-007**: Zero tasks are modified during search or filter operations

## Assumptions

- Users understand basic console interaction (entering text and selecting options)
- Tasks have been previously created using the Add Task functionality
- Users recognize that search operates on both title and description fields
- Users prefer case-insensitive matching for better search experience
- Filter values are single selections (e.g., one priority level at a time, not multiple)
- Color conventions from view.py should be maintained for consistency

## Out of Scope

- Combining multiple search criteria (e.g., keyword + priority filter simultaneously)
- Sorting search results (by date, priority, etc.)
- Saving search history or favorite filters
- Advanced search operators (AND, OR, NOT logic, wildcards)
- Searching in task fields other than title and description
- Modifying or deleting tasks through the search interface
- Persisting search preferences or filter settings

## Constraints

- Must use shared in-memory task list from add module
- No file or database persistence of search history
- Console-based user interface only
- Single file implementation: search.py
- No modification of existing task data
- No task creation, update, delete, or sort functionality included

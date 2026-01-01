# Research: Sort Tasks Feature

**Feature**: Sort Tasks (007-sort-tasks)
**Date**: 2026-01-01
**Purpose**: Research technical decisions for implementing task sorting functionality

## Overview

This document captures technical research and decisions for implementing task sorting functionality in a console-based Python CLI application. The feature requires sorting tasks by due date, priority, and title without modifying the original task data.

## Decision 1: Sorting Algorithm

**Decision**: Use Python's built-in `sorted()` function with custom key functions

**Rationale**:
- Python's `sorted()` is stable (preserves order for equal elements), satisfying FR-010
- Time complexity O(n log n) is more than adequate for in-memory task lists (expected <1000 tasks)
- Zero external dependencies required
- Supports custom key functions for complex sorting criteria

**Alternatives Considered**:
1. Custom quicksort/mergesort implementation - Rejected: Python's built-in is optimized C implementation
2. List.sort() with in-place modification - Rejected: Would modify original task list, violates FR-009
3. Pandas DataFrame operations - Rejected: Requires external library, violates constraint "No external libraries"

## Decision 2: Due Date Comparison Strategy

**Decision**: Treat due dates as string comparison for ISO format (YYYY-MM-DD)

**Rationale**:
- String comparison works correctly for ISO 8601 format (e.g., "2026-01-10" < "2026-01-15")
- Tasks without due dates (`None`) are handled by placing them after all dated tasks
- No date parsing libraries required
- Assumption from spec: "Due dates are provided as strings in a format that allows chronological comparison"

**Alternatives Considered**:
1. Python `datetime` parsing - Rejected: External module (though standard library), adds complexity
2. Timestamp conversion - Rejected: Requires format assumptions, string comparison is simpler
3. Locale-aware date parsing - Rejected: Over-engineering, violates YAGNI

## Decision 3: Priority Sorting Implementation

**Decision**: Use priority mapping dictionary to sort High → Medium → Low

**Rationale**:
- Maps string priorities to numeric values: `{"High": 0, "Medium": 1, "Low": 2}`
- Simpler than ordinal comparison of strings
- Handles missing/invalid priority values gracefully (treats as Medium or logs warning)
- Constant-time lookup, O(n) for sorting

**Alternatives Considered**:
1. String ordinal comparison ("High" < "Low") - Rejected: Incorrect ordering (H < L < M)
2. Enum-based priority - Rejected: Requires modifying existing Task dataclass from add.py
3. Multiple if-elif chains - Rejected: Less readable, harder to maintain

## Decision 4: Case-Insensitive Title Sorting

**Decision**: Use `str.lower()` in key function for case-insensitive comparison

**Rationale**:
- Satisfies FR-005 (case-insensitive comparison)
- Python's default Unicode handling supports special characters
- Maintains original title casing in display (sorting key is temporary)
- No external libraries required

**Alternatives Considered**:
1. `str.casefold()` - Rejected: More aggressive (handles German ß, Turkish I), not needed for English titles
2. Locale-aware sorting (`locale.strxfrm`) - Rejected: Requires import, platform-dependent
3. External text processing libraries - Rejected: Violates "No external libraries" constraint

## Decision 5: Display Function Integration

**Decision**: Reuse existing display logic from view.py via helper function

**Rationale**:
- Spec requires "sorted tasks displayed with colored status and priority indicators"
- view.py already implements Colors class and display formatting
- Create a shared display utility to avoid code duplication
- Single file constraint (sort.py) can import Colors from add.py

**Alternatives Considered**:
1. Copy-paste display code into sort.py - Rejected: Violates DRY principle
2. Subclass/extend view.py - Rejected: Single file constraint, adds complexity
3. Create separate display.py module - Rejected: Violates single file constraint

## Decision 6: Memory Ownership Pattern

**Decision**: Accept task list as parameter, return sorted copy

**Rationale**:
- Explicit input/output design clarifies no ownership (meets user constraint)
- `sorted()` naturally returns new list, preserving original
- Caller maintains control over task lifecycle
- Stateless function design is more testable

**Alternatives Considered**:
1. Import and use `_tasks` global from add.py - Rejected: Violates "Do not import or define shared memory" constraint
2. Store reference to task list in sort.py - Rejected: Violates "Do not create or store task list" constraint
3. Singleton pattern for task access - Rejected: Over-engineering, unnecessary state

## Decision 7: UI Interaction Pattern

**Decision**: Simple menu with numbered options (1, 2, 3) for sorting criteria

**Rationale**:
- Consistent with existing CLI patterns in add.py and view.py
- Clear user experience: "1. Sort by Due Date", "2. Sort by Priority", etc.
- Return to caller after display (meets "Return control after display")
- Minimal input validation required

**Alternatives Considered**:
1. Command-line arguments (--sort-by due-date) - Rejected: Requires integration with main.py, out of scope
2. Interactive prompts with partial matching ("date", "due") - Rejected: Adds complexity, ambiguous
3. Single-key shortcuts (d, p, t) - Rejected: Less discoverable than numbered menu

## Decision 8: Testing Strategy (Future)

**Decision**: Unit tests for sort functions with mock task lists

**Rationale**:
- Pure functions are easily testable
- Test edge cases: empty list, single task, all same value, mixed values
- Test stability: sorting twice should produce same order
- Integration testing via main.py when feature is complete

**Alternatives Considered**:
1. Property-based testing (Hypothesis) - Rejected: External library
2. Manual testing only - Rejected: Insufficient confidence, violates quality standards
3. End-to-end UI testing - Rejected: Overkill for simple sorting logic

## Performance Analysis

**Complexity**:
- Sorting: O(n log n) where n = number of tasks
- Space: O(n) for sorted copy (non-destructive requirement)
- Display: O(n) for iteration

**Expected Performance**:
- With 1,000 tasks: ~10,000 operations (< 1ms on modern hardware)
- Meets success criterion SC-001/002/003 (within 1 second)
- Memory overhead: Negligible for in-memory lists

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Invalid due date formats cause incorrect sorting | Medium | Document expected format (ISO 8601), handle None values |
| Non-standard priority values appear | Low | Treat as Medium, log warning, document behavior |
| Unicode title collation varies by locale | Low | Use Python default Unicode handling, document limitation |
| Sort key function creates large temporary objects | Very Low | Key functions create only strings/integers, negligible memory |

## Open Questions (Resolved by Assumptions)

- **Q**: What due date format is used?
  - **A**: Assumed ISO 8601 (YYYY-MM-DD) for string comparison
- **Q**: How to handle invalid priority values?
  - **A**: Treat as Medium, maintain original order within same priority
- **Q**: Should sorting be stable?
  - **A**: Yes, Python's sorted() is stable by default
- **Q**: Performance requirements?
  - **A**: Within 1 second for any reasonable task list (<10,000 tasks)

## Implementation Guidance

### Code Structure (sort.py)

```python
from add import Task, Colors

# Priority mapping for sorting
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}

# Sorting functions (pure, no side effects)
def sort_by_title(tasks: list[Task]) -> list[Task]
def sort_by_priority(tasks: list[Task]) -> list[Task]
def sort_by_due_date(tasks: list[Task]) -> list[Task]

# Display function (uses Colors from add.py)
def display_tasks(tasks: list[Task]) -> None

# UI entry point
def run_sort_ui(tasks: list[Task]) -> None
```

### Key Implementation Details

1. **Title sort**: `sorted(tasks, key=lambda t: t.title.lower())`
2. **Priority sort**: `sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t.priority, 1))`
3. **Due date sort**: Separate into dated and non-dated, sort dated, concatenate
4. **Empty list**: Display message from FR-008 before attempting sort

### Dependencies

- `add.Task`: Task dataclass definition (read-only)
- `add.Colors`: ANSI color codes for display
- Standard library only (no external dependencies)

## Conclusion

All technical decisions aligned with constraints:
- ✅ No external libraries
- ✅ No memory ownership (accepts task list as parameter)
- ✅ Single file implementation (sort.py)
- ✅ Non-destructive sorting (returns new list)
- ✅ Console-based with color support
- ✅ Handles edge cases (empty list, missing values)

Feature is ready for Phase 1 (data model, contracts, quickstart) and Phase 2 (task breakdown).

# Research: Search & Filter Tasks

**Feature**: 006-search-filter-tasks
**Date**: 2025-12-31

## Technology Decisions

### Decision: Use Python's built-in string methods for case-insensitive search
**Rationale**: Python's `.lower()` method provides clean, efficient case-insensitive comparison without external dependencies. This aligns with project's existing Python 3.x codebase.

**Alternatives considered**:
- Regular expressions with `re.IGNORECASE` - Overkill for simple substring matching
- Third-party search libraries (e.g., fuzzy matching) - Adds unnecessary complexity and dependencies

### Decision: Direct iteration over shared `_tasks` list for filtering
**Rationale**: The shared task list from `add.py` is a simple Python list. Direct iteration with list comprehension is the most Pythonic and efficient approach for this scale.

**Alternatives considered**:
- Database queries - Not applicable (in-memory storage only)
- Indexing structures (e.g., dict lookup) - Unnecessary complexity for small task lists

### Decision: Reuse Colors class from existing modules
**Rationale**: Maintain consistency with existing codebase. The Colors class is already defined in `add.py`, `view.py`, and other modules.

**Alternatives considered**:
- Create new Colors class in search.py - Duplicates code, inconsistent styling
- Use library like `colorama` - Adds dependency, existing ANSI codes work fine

### Decision: Console UI with input validation loop
**Rationale**: Follows pattern established in existing modules (add.py, view.py, complete.py) for consistency and user experience.

**Alternatives considered**:
- Single-pass command-line arguments - Less interactive, harder to validate
- Menu-driven selection - More complex, not needed for this feature

## Best Practices Applied

1. **Clean Code**: Single Responsibility Principle - Separate functions for search, filter, and display
2. **DRY Principle**: Reuse existing Colors class and task data structure
3. **Input Validation**: Clear error messages for invalid filter values
4. **Console UX**: Maintain existing color conventions for consistency
5. **Type Hints**: Use Python type annotations for better code documentation

## Edge Cases Addressed

- Empty search string: Treated as no filter (show all tasks)
- No tasks in memory: Display clear message
- Invalid filter values: Show error with valid options
- Case sensitivity: All comparisons use `.lower()` for case-insensitive matching
- Special characters: Treated as literal string (no regex interpretation)

## Integration Points

- **Module**: `add.py` - Import `_tasks` list (read-only)
- **Task Model**: Uses existing Task dataclass with id, title, description, completed, priority, category, due_date fields
- **Display**: Reuse color coding conventions from view.py

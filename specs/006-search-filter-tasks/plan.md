# Implementation Plan: Search & Filter Tasks

**Branch**: `006-search-filter-tasks` | **Date**: 2025-12-31 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/006-search-filter-tasks/spec.md`

## Summary

Implement search and filter functionality on shared in-memory task list, keeping logic isolated in one file `search.py`. Users can search tasks by keyword (title/description) and filter by status, priority, or category. All operations are case-insensitive and maintain existing color conventions.

## Technical Context

**Language/Version**: Python 3.x (matches existing codebase)
**Primary Dependencies**: None (uses built-in Python features)
**Storage**: In-memory list (`_tasks` from add.py - read-only)
**Testing**: Manual testing (no automated test framework required)
**Target Platform**: Cross-platform (Windows, Linux, macOS) via console/terminal
**Project Type**: Single-module console application
**Performance Goals**: <1 second response for searches/filters on typical task lists (<1000 tasks)
**Constraints**: No file/database persistence; Console-based ANSI colors only; Single file implementation
**Scale/Scope**: Small task lists (<1000 tasks typical); Single filter at a time

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: ✅ PASSED

**Gates Evaluated**:
- **Library-First**: Feature implemented as single module that can be imported independently
- **CLI Interface**: Uses console input/output (stdin/stdout) with colored output
- **Test-First**: Manual test scenarios defined in spec and quickstart
- **Integration**: Works with existing `_tasks` shared storage and Task dataclass
- **Observability**: Color-coded output for immediate user feedback
- **Simplicity**: Minimal dependencies, clear separation of concerns

**Violations**: None

## Project Structure

### Documentation (this feature)

```text
specs/006-search-filter-tasks/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output - Technology decisions
├── data-model.md        # Phase 1 output - Entity definitions
├── quickstart.md        # Phase 1 output - Usage guide
├── contracts/
│   └── search-functions.md  # Phase 1 output - Function contracts
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created yet)
```

### Source Code (repository root)

```text
src/
├── add.py        # Existing - provides _tasks and Task
├── view.py       # Existing - provides color reference
├── search.py     # NEW - Search and filter functionality (single file)
├── update.py     # Existing - task update
├── delete.py     # Existing - task delete
└── complete.py   # Existing - task completion toggle
```

**Structure Decision**: Single-module implementation. The feature is a self-contained module (`search.py`) that imports the shared `_tasks` list from `add.py` and follows the established pattern of other feature modules. No new directories or package structure needed.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations. Implementation follows all project principles and patterns established in existing modules.

## Implementation Details

### Phase 0: Research ✅ COMPLETED

**Deliverables**:
- research.md - Technology decisions and best practices

**Key Decisions**:
1. Use Python's built-in string methods for case-insensitive search
2. Direct iteration over shared `_tasks` list for filtering
3. Reuse Colors class from existing modules
4. Console UI with input validation loop

### Phase 1: Design ✅ COMPLETED

**Deliverables**:
- data-model.md - Entity definitions (Search Query, Filter Criteria, Search Result)
- quickstart.md - Usage guide and examples
- contracts/search-functions.md - Function contracts with validation rules

**Key Design Elements**:
1. **Seven core functions**:
   - `search_tasks(keyword: str) -> List[Task]`
   - `filter_by_status(status: str) -> List[Task]`
   - `filter_by_priority(priority: str) -> List[Task]`
   - `filter_by_category(category: str) -> List[Task]`
   - `search_and_filter(...) -> List[Task]` (combined)
   - `display_search_results(tasks: List[Task]) -> None`
   - `run_search_ui() -> None` (console interface)

2. **Data Flow**:
   ```
   User Input → Search/Filter Functions → Display → Console Output
   ```

3. **Validation Rules**:
   - Status: "complete" or "incomplete" (case-insensitive)
   - Priority: "High", "Medium", "Low" (case-insensitive)
   - Category: Non-empty string
   - Keyword: Any string (empty = no filter)

4. **Error Handling**:
   - Invalid filter values → ValueError with valid options
   - No tasks in memory → Clear message
   - No matching results → Clear message

5. **Color Coding**:
   - Match existing conventions from view.py
   - Priority: Red (High), Orange (Medium), Blue (Low)
   - Status: Green (complete), Yellow (incomplete)
   - Category: Pink
   - Due date: Purple (if available)

## Architecture Decisions

### Decision 1: Single File Implementation
**Rationale**: Feature scope is limited to search and filter operations. No need for multiple modules or classes.

### Decision 2: AND Logic for Combined Search + Filter
**Rationale**: Spec states "Search and filters must be case-insensitive" and FR-007 requires displaying tasks matching ALL criteria. AND logic is appropriate.

### Decision 3: No Sorting
**Rationale**: Out of scope per spec. No performance requirement for sorted results. Preserve original task order from `_tasks`.

### Decision 4: No Search History
**Rationale**: Out of scope per spec. No persistence requirement. Each search/filter is independent operation.

## Integration Plan

### External Dependencies
- **Import from add.py**:
  - `_tasks: list[Task]` - Shared in-memory storage (read-only)
  - `Task` - Dataclass definition

### Integration Points
1. Read shared task list (no modifications)
2. Use existing Task dataclass fields
3. Match color conventions from view.py
4. Follow console UI pattern from add.py, complete.py

### No Breaking Changes
- All existing modules remain unchanged
- search.py is new independent module
- `_tasks` list structure unchanged
- Task dataclass fields unchanged

## Testing Strategy

### Manual Test Scenarios (from spec.md)

**User Story 1 - Search by Keyword (P1)**:
1. Create tasks with various titles/descriptions
2. Search for keyword in title → verify correct results
3. Search for keyword in description → verify correct results
4. Search with uppercase → verify case-insensitive match
5. Search for non-existent keyword → verify "no matching tasks" message

**User Story 2 - Filter by Status (P2)**:
1. Create mix of completed/incomplete tasks
2. Filter by "complete" → verify only completed tasks shown
3. Filter by "incomplete" → verify only incomplete tasks shown
4. Filter with case variation → verify case-insensitive match

**User Story 3 - Filter by Priority (P2)**:
1. Create tasks with different priorities
2. Filter by "High" → verify only High priority tasks
3. Filter by "Low" → verify only Low priority tasks
4. Filter with uppercase → verify case-insensitive match

**User Story 4 - Filter by Category (P3)**:
1. Create tasks with different categories
2. Filter by specific category → verify only matching tasks shown
3. Filter with case variation → verify case-insensitive match

### Edge Cases
1. Empty search string → shows all tasks
2. No tasks in memory → displays clear message
3. Invalid filter value → shows error with valid options
4. Special characters in search → treats as literal string
5. Empty keyword + filters → applies filters only

## Success Metrics

From spec.md Success Criteria:
- **SC-001**: Users can locate specific tasks by keyword in under 10 seconds
- **SC-002**: 100% of keyword searches correctly match tasks regardless of case
- **SC-003**: Users can filter tasks by any single criteria in under 15 seconds
- **SC-004**: Clear error messages appear within 1 second for invalid filter inputs
- **SC-005**: Users receive feedback about no matching results in under 2 seconds
- **SC-006**: All displayed results maintain existing color coding
- **SC-007**: Zero tasks are modified during search or filter operations

## Implementation Checklist

### Phase 1 Complete ✅
- [x] research.md created with technology decisions
- [x] data-model.md created with entity definitions
- [x] quickstart.md created with usage guide
- [x] contracts/search-functions.md created with function signatures

### Phase 2 (Implementation - via /sp.tasks)
- [ ] Create src/search.py file
- [ ] Implement Colors class (reuse existing codes)
- [ ] Implement search_tasks() function
- [ ] Implement filter_by_status() function
- [ ] Implement filter_by_priority() function
- [ ] Implement filter_by_category() function
- [ ] Implement search_and_filter() function
- [ ] Implement display_search_results() function
- [ ] Implement run_search_ui() function
- [ ] Add __main__ entry point
- [ ] Test all user stories manually
- [ ] Verify color conventions match view.py
- [ ] Verify case-insensitive matching works
- [ ] Verify error messages display correctly

## Next Steps

1. Run `/sp.tasks` to generate testable implementation tasks
2. Implement search.py following contracts
3. Manual testing against all user stories
4. Integration testing with existing modules
5. Update main.py to include search option (if needed)

## Notes

- **No persistence requirement**: All search/filter operations are ephemeral
- **Read-only access**: search.py never modifies `_tasks` list
- **Backward compatible**: Works with existing Task data structure
- **Console only**: No GUI or web components
- **Single responsibility**: Each function has one clear purpose

# Implementation Plan: Sort Tasks

**Branch**: `007-sort-tasks` | **Date**: 2026-01-01 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/007-sort-tasks/spec.md`

## Summary

Implement task sorting functionality that accepts a task list as input and provides three sorting criteria (title, priority, due date) with a console-based UI. The implementation is non-destructive (creates sorted copies), uses no external libraries, and follows the single-file constraint (`sort.py`). Sorting functions are pure with well-defined contracts, display uses existing color coding from `add.py`, and memory ownership remains with the caller.

## Technical Context

**Language/Version**: Python 3.13
**Primary Dependencies**: None (standard library only)
**Storage**: N/A (in-memory task lists, caller-owned)
**Testing**: pytest (for future unit tests)
**Target Platform**: Cross-platform console (Windows, Linux, macOS)
**Project Type**: Single project (console CLI)
**Performance Goals**: Sort and display within 1 second for typical task lists (<1000 tasks)
**Constraints**:
- Single file implementation (`sort.py`)
- No external libraries
- Non-destructive sorting (display-only)
- No task storage ownership
- Console-based interaction only
**Scale/Scope**: In-memory lists, expected <1000 tasks, display-only sorting

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Status**: ✅ PASSED

The constitution file is a template with no specific principles defined. The implementation follows standard best practices:
- Clean code principles (pure functions, clear contracts)
- Separation of concerns (sorting, display, UI)
- Testability (pure functions with clear inputs/outputs)
- No unnecessary complexity (uses built-in `sorted()`)

No violations to justify.

## Project Structure

### Documentation (this feature)

```text
specs/007-sort-tasks/
├── spec.md                  # Feature specification
├── plan.md                  # This file (implementation plan)
├── research.md              # Phase 0: Technical research and decisions
├── data-model.md            # Phase 1: Task entity and sorting behavior
├── quickstart.md            # Phase 1: Usage guide for developers and users
├── contracts/
│   └── function-interfaces.md # Phase 1: Public function contracts
├── checklists/
│   └── requirements.md       # Specification quality checklist
└── tasks.md                 # Phase 2: Implementation tasks (created by /sp.tasks)
```

### Source Code (repository root)

```text
src/
├── add.py                  # Task dataclass and creation (existing)
├── view.py                 # Task viewing (existing)
└── sort.py                 # NEW: Task sorting (this feature)

tests/                      # Future: Unit and integration tests
```

**Structure Decision**: Single project structure selected. The feature extends the existing console CLI by adding a new `sort.py` module to the `src/` directory. No backend/frontend separation needed for this console-only feature.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No complexity tracking required - Constitution Check passed with no violations.

## Implementation Phases

### Phase 0: Research ✅ COMPLETED

**Output**: `research.md`

**Key Decisions**:
1. Use Python's `sorted()` function (O(n log n), stable sort)
2. Due date comparison via string comparison for ISO format (YYYY-MM-DD)
3. Priority sorting using mapping dictionary: `{"High": 0, "Medium": 1, "Low": 2}`
4. Case-insensitive title sorting using `str.lower()`
5. Display logic reuses `Colors` class from `add.py`
6. Memory pattern: Accept task list as parameter, return sorted copy
7. Simple numbered menu (1, 2, 3) for UI interaction
8. Unit testing strategy with mock task lists

All technical decisions aligned with constraints and requirements.

### Phase 1: Design ✅ COMPLETED

**Outputs**:
- `data-model.md`: Existing Task entity, sorting behavior, data flow
- `contracts/function-interfaces.md`: 5 public functions with signatures, examples
- `quickstart.md`: Usage guide, examples, API reference

**Design Summary**:
- **No new data models**: Reuses existing Task from `add.py`
- **Public API**: 5 functions (3 sort, 1 display, 1 UI)
- **Contracts**: Complete with signatures, parameters, returns, behavior, complexity
- **Integration**: Imports Task and Colors from `add.py`, accepts task list parameter

### Phase 2: Implementation Planning (Current Phase)

**Output**: Implementation breakdown in `tasks.md` (created by `/sp.tasks`)

**Key Components**:

1. **Constants**:
   - `PRIORITY_ORDER`: Dictionary mapping priorities to numeric values

2. **Sorting Functions** (pure, no side effects):
   - `sort_by_title(tasks)`: Returns sorted copy by title (case-insensitive)
   - `sort_by_priority(tasks)`: Returns sorted copy by priority (High→Medium→Low)
   - `sort_by_due_date(tasks)`: Returns sorted copy by due date (earliest→latest)

3. **Display Function**:
   - `display_tasks(tasks)`: Prints tasks with color coding (uses Colors from add.py)

4. **UI Function**:
   - `run_sort_ui(tasks)`: Interactive menu, executes sort, displays results

**Integration Points**:
- **From `add.py`**:
  - `Task` dataclass (read-only)
  - `Colors` class (for display formatting)
- **To `main.py`** (future):
  - Import and call `run_sort_ui(_tasks)`
  - Handle return to main menu

**Non-Goals** (explicitly out of scope):
- Task storage or persistence
- Task creation or modification
- Search or filter functionality
- Multi-sort criteria (e.g., by priority, then by title)
- Configuration or user preferences

### Phase 3: Implementation (Next Steps)

**Command**: `/sp.implement` or `/sp.tasks`

**Implementation Tasks** (will be generated in `tasks.md`):
1. Setup sort.py file structure
2. Implement PRIORITY_ORDER constant
3. Implement sort_by_title function
4. Implement sort_by_priority function
5. Implement sort_by_due_date function
6. Implement display_tasks function
7. Implement run_sort_ui function
8. Add module-level documentation
9. Create unit tests for sorting functions
10. Create integration tests for UI flow

**Testing Strategy**:
- Unit tests for each sort function (5 scenarios each)
- Unit tests for display_tasks (empty, single, multiple)
- Integration tests for UI flow (menu selection → sort → display)
- Test edge cases: None values, empty lists, identical values

**Quality Assurance**:
- Verify all functional requirements (FR-001 through FR-012)
- Verify success criteria (SC-001 through SC-007)
- Verify constraints (single file, no external libs, non-destructive)
- Verify color coding matches existing patterns in view.py

### Phase 4: Integration (Future)

**Steps** (after implementation):
1. Integrate `run_sort_ui(_tasks)` into main menu
2. Test full user flow: add tasks → sort → view → return
3. Verify no side effects on original task list
4. Verify memory management (no leaks, proper cleanup)

## Acceptance Criteria

### Must Have (P1)

- [x] Specification created and approved
- [x] Research completed with all decisions documented
- [x] Data model defined (reuses existing Task)
- [x] Function contracts documented
- [ ] Implementation completed (sort.py with all functions)
- [ ] All sorting criteria work correctly (title, priority, due date)
- [ ] Display uses color coding from add.py
- [ ] Empty list handled gracefully (message displayed)
- [ ] Original task list never modified
- [ ] No external libraries used

### Should Have (P2)

- [x] Quick start guide created
- [ ] Unit tests for sorting functions
- [ ] Integration tests for UI
- [ ] Performance benchmark (confirms <1 second sorting)

### Nice to Have (P3)

- [ ] Error handling for invalid priority values (log warning)
- [ ] Support for case-insensitive priority comparison
- [ ] Multiple sort options (e.g., by priority, then by title)

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|---------|------------|
| Due date format incompatibility | Low | Medium | Document ISO 8601 requirement in spec and quickstart |
| Unicode title sorting issues | Low | Low | Use Python default Unicode handling, document limitation |
| Color codes not working on terminal | Low | Low | Test on multiple platforms, document requirements |
| Priority value mismatches | Medium | Medium | Treat unexpected values as "Medium", log warning |
| Performance degradation with large lists | Very Low | Low | Document expected scale (<1000 tasks), O(n log n) is adequate |

## Dependencies

### External Dependencies
- None (standard library only)

### Internal Dependencies
- `add.Task`: Dataclass definition (read-only)
- `add.Colors`: ANSI color codes for display

### Integration Dependencies (Future)
- `main.py`: Will need to import and call `run_sort_ui(_tasks)`

## Success Metrics

### Quantitative
- Sort operations complete in <1 second (SC-001, SC-002, SC-003)
- 100% of sorts succeed without errors (SC-004)
- 100% of empty lists handled gracefully (SC-005)
- 100% of displays show correct colors (SC-006)
- 100% of sorts preserve original data (SC-007)

### Qualitative
- Clear, user-friendly UI messages
- Consistent with existing application style (add.py, view.py)
- Code is readable, maintainable, and well-documented
- Functions are pure and testable

## Next Steps

1. **Immediate**: Run `/sp.tasks` to generate implementation task breakdown
2. **Then**: Run `/sp.implement` to execute implementation tasks
3. **Finally**: Integrate with main menu and perform end-to-end testing

---

**Status**: ✅ Phase 0, 1, 2 Complete | Ready for `/sp.tasks`
**Date**: 2026-01-01
**Branch**: `007-sort-tasks`

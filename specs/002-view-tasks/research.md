# Research: View Tasks & Status Indication

**Feature**: 002-view-tasks
**Completed**: 2025-12-31

### Task Model Reuse
- **Decision**: Import Task dataclass from existing `src/add.py` instead of redefining
- **Rationale**: Task entity is shared across specs (noted in spec.md). Avoids duplication and ensures consistency.
- **Alternatives considered**:
  - Redefine Task class in view.py (rejected: duplication, inconsistency risk)

### Storage Access Pattern
- **Decision**: Read directly from module-level `_tasks` list in `src/add.py`
- **Rationale**: Tasks are stored in global state; direct read access is simplest and follows Spec 001 pattern.
- **Alternatives considered**:
  - Create getter function in add.py (rejected: unnecessary indirection)
  - Move storage to shared module (rejected: scope creep beyond current spec)

### Status Indicator Format
- **Decision**: Use checkmark symbols [✓] for completed, [ ] for incomplete
- **Rationale**: Clear visual distinction that works across platforms. Symbols are immediately recognizable.
- **Alternatives considered**:
  - Text "completed"/"incomplete" (rejected: less scannable at a glance)
  - Different colors (rejected: console color support varies)
  - Unicode boxes [☑]/[☐] (rejected: less universal than checkmarks)

### Display Format
- **Decision**: One task per line with tab-separated fields: ID | [status] | Title | Description
- **Rationale**: Simple format that's easy to parse visually. Handles long content by natural line wrapping.
- **Alternatives considered**:
  - Table with borders (rejected: unnecessary complexity for console)
  - JSON output (rejected: not human-readable)
  - Multi-line per task (rejected: harder to scan many tasks)

### Empty List Handling
- **Decision**: Display "No tasks found. Add tasks using add task functionality."
- **Rationale**: Clear user guidance on how to proceed. Matches UI patterns from Spec 001.
- **Alternatives considered**:
  - Display nothing (rejected: confusing, user doesn't know if functionality worked)
  - Display error (rejected: not an error, just empty state)

### Long Content Handling
- **Decision**: No explicit truncation; let terminal naturally wrap lines
- **Rationale**: Tasks can be 1000+ chars (spec requirement). Terminal wrapping is standard behavior.
- **Alternatives considered**:
  - Truncate at 80 chars (rejected: loses information)
  - Ellipsis truncation (rejected: unclear what was omitted)
  - Multi-line display (rejected: breaks scannability for many tasks)

### Console UI Pattern
- **Decision**: Follow `run_add_task_ui()` pattern from Spec 001
- **Rationale**: Consistent user experience. Separation of core logic (`get_all_tasks()`) from UI (`run_view_tasks_ui()`).
- **Alternatives considered**:
  - Single function for both logic and UI (rejected: violates single responsibility)
  - Command-line arguments instead of interactive menu (rejected: spec requires console interaction)

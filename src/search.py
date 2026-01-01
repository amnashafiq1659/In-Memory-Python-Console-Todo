"""
Search and Filter Tasks Feature

This module provides functionality to search and filter tasks
by keyword, completion status, priority, and category.
All operations work on the shared in-memory task list from add module.
"""

import sys
sys.path.insert(0, '.')
from add import _tasks, Task
from typing import List, Optional


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    ORANGE = '\033[38;5;208m'  # Medium priority
    BRIGHT_YELLOW = '\033[93;1m'  # Task titles
    DIM_CYAN = '\033[96;2m'  # Descriptions
    PINK = '\033[38;5;206m'  # Categories
    PURPLE = '\033[38;5;141m'  # Due dates


def search_tasks(keyword: str) -> List[Task]:
    """
    Find tasks matching a keyword in title or description.

    Args:
        keyword: The search term to match (case-insensitive).

    Returns:
        List[Task]: All tasks where keyword appears in title OR description.

    Notes:
        - Empty keyword returns all tasks (no filter applied)
        - Uses OR logic: match if keyword in title OR description
        - Case-insensitive matching applied
    """
    if not keyword or keyword.strip() == "":
        return _tasks[:]

    keyword_lower = keyword.lower()
    matching_tasks = []

    for task in _tasks:
        if (keyword_lower in task.title.lower() or
            keyword_lower in task.description.lower()):
            matching_tasks.append(task)

    return matching_tasks


def filter_by_status(status: str) -> List[Task]:
    """
    Filter tasks by completion status.

    Args:
        status: Filter value ("complete" or "incomplete", case-insensitive).

    Returns:
        List[Task]: Tasks where task.completed matches status value.

    Raises:
        ValueError: If status is not "complete" or "incomplete".
    """
    status_lower = status.lower()

    if status_lower not in ("complete", "incomplete"):
        raise ValueError("Status must be 'complete' or 'incomplete'")

    target_completed = (status_lower == "complete")

    matching_tasks = [
        task for task in _tasks
        if task.completed == target_completed
    ]

    return matching_tasks


def filter_by_priority(priority: str) -> List[Task]:
    """
    Filter tasks by priority level.

    Args:
        priority: Priority level ("High", "Medium", "Low", case-insensitive).

    Returns:
        List[Task]: Tasks where task.priority matches priority value.

    Raises:
        ValueError: If priority is not "High", "Medium", or "Low".
    """
    priority_lower = priority.lower()

    if priority_lower not in ("high", "medium", "low"):
        raise ValueError("Priority must be one of: ['High', 'Medium', 'Low']")

    matching_tasks = [
        task for task in _tasks
        if task.priority.lower() == priority_lower
    ]

    return matching_tasks


def filter_by_category(category: str) -> List[Task]:
    """
    Filter tasks by category tag.

    Args:
        category: Category name (case-insensitive matching).

    Returns:
        List[Task]: Tasks where task.category matches category value.

    Raises:
        ValueError: If category is empty string.
    """
    category_stripped = category.strip()

    if not category_stripped:
        raise ValueError("Category cannot be empty")

    category_lower = category_stripped.lower()

    matching_tasks = [
        task for task in _tasks
        if task.category.lower() == category_lower
    ]

    return matching_tasks


def search_and_filter(
    keyword: str = "",
    status: Optional[str] = None,
    priority: Optional[str] = None,
    category: Optional[str] = None
) -> List[Task]:
    """
    Combine search and filter operations to find tasks matching all criteria.

    Args:
        keyword: Search term (optional, empty = no search).
        status: Status filter (complete/incomplete or None).
        priority: Priority filter (High/Medium/Low or None).
        category: Category filter (non-empty string or None).

    Returns:
        List[Task]: Tasks matching all provided criteria (AND logic).

    Raises:
        ValueError: If any provided filter value is invalid.

    Notes:
        - Applies search first (if keyword provided)
        - Applies each active filter sequentially
        - Uses AND logic: task must satisfy all criteria
        - Returns empty list if no tasks match
    """
    # Validate filter inputs first
    if status is not None:
        status_lower = status.lower()
        if status_lower not in ("complete", "incomplete"):
            raise ValueError("Status must be 'complete' or 'incomplete'")

    if priority is not None:
        priority_lower = priority.lower()
        if priority_lower not in ("high", "medium", "low"):
            raise ValueError("Priority must be one of: ['High', 'Medium', 'Low']")

    if category is not None:
        category_stripped = category.strip()
        if not category_stripped:
            raise ValueError("Category cannot be empty")

    # Apply search if keyword provided
    results = search_tasks(keyword)

    # Apply each active filter sequentially (AND logic)
    if status is not None:
        status_lower = status.lower()
        target_completed = (status_lower == "complete")
        results = [
            task for task in results
            if task.completed == target_completed
        ]

    if priority is not None:
        priority_lower = priority.lower()
        results = [
            task for task in results
            if task.priority.lower() == priority_lower
        ]

    if category is not None:
        category_lower = category.lower()
        results = [
            task for task in results
            if task.category.lower() == category_lower
        ]

    return results


def display_search_results(tasks: List[Task]) -> None:
    """
    Display filtered tasks with color coding to console.

    Args:
        tasks: Tasks to display.

    Returns:
        None

    Notes:
        - If tasks list is empty, shows "No matching tasks" message
        - Displays header with task count
        - Shows completion status, ID, title, description
        - Shows priority (color-coded), category, due date
        - Maintains existing color conventions from view.py
    """
    if not _tasks:
        print(f"{Colors.YELLOW}No tasks found in memory. Add tasks using Add Task functionality.{Colors.RESET}")
        print()
        return

    if not tasks:
        print(f"{Colors.YELLOW}No tasks match your search/filter criteria.{Colors.RESET}")
        print()
        return

    print(f"{Colors.BOLD}{Colors.CYAN}=== Search Results ==={Colors.RESET}")
    print()

    for task in tasks:
        # Status indicator
        status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"

        # Priority color coding
        if task.priority == "High":
            priority_color = f"{Colors.BOLD}{Colors.RED}"
        elif task.priority == "Medium":
            priority_color = f"{Colors.BOLD}{Colors.ORANGE}"
        else:  # Low
            priority_color = f"{Colors.BOLD}{Colors.BLUE}"

        # Due date display
        due_date_str = f" | Due: {Colors.PURPLE}{task.due_date}{Colors.RESET}" if task.due_date else ""

        # Print task with all attributes
        print(f"{status} {Colors.BOLD}{Colors.CYAN}[{task.id}]{Colors.RESET} {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET}")
        print(f"    Desc: {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
        print(f"    Priority: {priority_color}{task.priority}{Colors.RESET} | Category: {Colors.PINK}{task.category}{Colors.RESET}{due_date_str}")
        print()

    print(f"{Colors.BOLD}{Colors.CYAN}Total: {Colors.RESET}{len(tasks)}{Colors.BOLD}{Colors.CYAN} task{'s' if len(tasks) != 1 else ''}{Colors.RESET}")


def run_search_ui() -> None:
    """
    Interactive console interface for search and filter operations.

    Allows user to:
    - Enter keyword (optional, press Enter to skip)
    - Filter by status (complete/incomplete/skip)
    - Filter by priority (High/Medium/Low/skip)
    - Filter by category (press Enter to skip)
    - See confirmation or error messages

    Returns:
        None

    Notes:
        - Validates all inputs before applying
        - Calls search_and_filter() with user inputs
        - Calls display_search_results() with results
        - Allows user to continue or exit
    """
    print()
    print(f"{Colors.BOLD}{Colors.CYAN}=== Search & Filter Tasks ==={Colors.RESET}")
    print()

    # Check if tasks exist
    if not _tasks:
        print(f"{Colors.YELLOW}No tasks available for searching/filtering.{Colors.RESET}")
        print()
        return

    # Get keyword
    keyword = input(f"{Colors.BOLD}{Colors.ORANGE}Enter keyword (or press Enter to skip): {Colors.RESET}").strip()

    # Get filters
    print(f"\n{Colors.BOLD}{Colors.CYAN}Optional Filters:{Colors.RESET}")
    print(f"{Colors.DIM_CYAN}(Press Enter to skip any filter){Colors.RESET}")
    print()

    # Status filter
    status = None
    while True:
        status_input = input(f"{Colors.BOLD}{Colors.ORANGE}Filter by status? (complete/incomplete/skip): {Colors.RESET}").strip()
        if not status_input or status_input.lower() == "skip":
            break
        try:
            status_lower = status_input.lower()
            if status_lower in ("complete", "incomplete"):
                status = status_input
                break
            else:
                print(f"{Colors.BOLD}{Colors.RED}Error: Status must be 'complete' or 'incomplete'{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.BOLD}{Colors.RED}Error: {str(e)}{Colors.RESET}")

    # Priority filter
    priority = None
    while True:
        priority_input = input(f"{Colors.BOLD}{Colors.ORANGE}Filter by priority? (High/Medium/Low/skip): {Colors.RESET}").strip()
        if not priority_input or priority_input.lower() == "skip":
            break
        try:
            priority_lower = priority_input.lower()
            if priority_lower in ("high", "medium", "low"):
                priority = priority_input
                break
            else:
                print(f"{Colors.BOLD}{Colors.RED}Error: Priority must be one of: ['High', 'Medium', 'Low']{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.BOLD}{Colors.RED}Error: {str(e)}{Colors.RESET}")

    # Category filter
    category = None
    while True:
        category_input = input(f"{Colors.BOLD}{Colors.ORANGE}Filter by category? (or press Enter to skip): {Colors.RESET}").strip()
        if not category_input:
            break
        try:
            filter_by_category(category_input)  # Validate
            category = category_input
            break
        except ValueError as e:
            print(f"{Colors.BOLD}{Colors.RED}Error: {str(e)}{Colors.RESET}")

    # Apply search and filter
    try:
        results = search_and_filter(
            keyword=keyword,
            status=status,
            priority=priority,
            category=category
        )
        display_search_results(results)
    except ValueError as e:
        print(f"{Colors.BOLD}{Colors.RED}Error: {str(e)}{Colors.RESET}")
        print()
        return


if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Searcher ==={Colors.RESET}")
    run_search_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

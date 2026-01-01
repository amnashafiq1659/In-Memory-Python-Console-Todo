"""
Task sorting module for console-based task management.

Provides functions to sort tasks by title, priority, or due date.
Sorting is non-destructive - creates sorted copies without modifying original task data.

Functions:
    sort_by_title(tasks): Sort tasks alphabetically by title (case-insensitive)
    sort_by_priority(tasks): Sort tasks by priority (High → Medium → Low)
    sort_by_due_date(tasks): Sort tasks by due date (earliest → latest)
    display_tasks(tasks): Display tasks with colored status and priority indicators
    run_sort_ui(tasks): Interactive UI for selecting sorting options
"""

from add import Task


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
    DIM = '\033[2m'
    ORANGE = '\033[38;5;208m'  # Orange
    BRIGHT_YELLOW = '\033[93;1m'  # Bright Yellow for task titles
    DIM_CYAN = '\033[96;2m'  # Dim Cyan for descriptions
    PINK = '\033[38;5;206m'  # Pink for categories
    PURPLE = '\033[38;5;141m'  # Purple for due dates


# Priority mapping for sorting: High (0) < Medium (1) < Low (2)
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def is_empty_list(tasks):
    """
    Check if tasks list is empty.

    Args:
        tasks: List of tasks to check

    Returns:
        bool: True if list is empty, False otherwise
    """
    return len(tasks) == 0


def sort_by_due_date(tasks):
    """
    Sort tasks by due date in ascending order (earliest to latest).

    Tasks without due dates are placed after all tasks with due dates.
    Sort is stable - maintains original order for identical due dates.

    Args:
        tasks: List of tasks to sort (not modified)

    Returns:
        list[Task]: New list with tasks sorted by due date
    """
    # Separate tasks with and without due dates
    dated_tasks = [task for task in tasks if task.due_date is not None]
    non_dated_tasks = [task for task in tasks if task.due_date is None]

    # Sort dated tasks by due date (string comparison works for ISO format)
    sorted_dated = sorted(dated_tasks, key=lambda t: t.due_date)

    # Return sorted dated tasks followed by non-dated tasks
    return sorted_dated + non_dated_tasks


def sort_by_priority(tasks):
    """
    Sort tasks by priority in order: High → Medium → Low.

    Maintains relative order within same priority level (stable sort).
    Unexpected priority values are treated as Medium.

    Args:
        tasks: List of tasks to sort (not modified)

    Returns:
        list[Task]: New list with tasks sorted by priority
    """
    return sorted(tasks, key=lambda t: PRIORITY_ORDER.get(t.priority, 1))


def sort_by_title(tasks):
    """
    Sort tasks alphabetically by title (A-Z) using case-insensitive comparison.

    Sort is stable - maintains original order for identical titles.

    Args:
        tasks: List of tasks to sort (not modified)

    Returns:
        list[Task]: New list with tasks sorted alphabetically by title
    """
    return sorted(tasks, key=lambda t: t.title.lower())


def display_tasks(tasks):
    """
    Display tasks in a user-friendly console format with color coding.

    Shows task ID, title, description, completion status, priority,
    and due date with visual indicators for completed vs incomplete tasks
    and color-coded priorities.

    Args:
        tasks: List of tasks to display (not modified)

    Returns:
        None: Prints to console, no return value
    """
    # Handle empty list
    if is_empty_list(tasks):
        print(f"{Colors.YELLOW}No tasks found. Add tasks using add task functionality.{Colors.RESET}")
        return

    print(f"{Colors.BOLD}{Colors.CYAN}=== Tasks ==={Colors.RESET}")
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
        if task.due_date:
            due_date_str = f" | Due: {Colors.PURPLE}{task.due_date}{Colors.RESET}"
        else:
            due_date_str = ""

        # Print task with all attributes
        print(f"{status} {Colors.BOLD}{Colors.CYAN}[{task.id}]{Colors.RESET} {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET}")
        print(f"    Desc: {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
        print(f"    Priority: {priority_color}{task.priority}{Colors.RESET} | Category: {Colors.PINK}{task.category}{Colors.RESET}{due_date_str}")
        print()

    print(f"{Colors.BOLD}{Colors.CYAN}Total: {Colors.RESET}{len(tasks)}{Colors.BOLD}{Colors.CYAN} tasks{Colors.RESET}")


def run_sort_ui(tasks):
    """
    Interactive console UI for selecting and executing sorting options.

    Args:
        tasks: List of tasks to sort (not modified)

    Returns:
        None: Displays menu and sorted results, then returns
    """
    # Handle empty list
    if is_empty_list(tasks):
        display_tasks(tasks)
        return

    print(f"{Colors.BOLD}{Colors.CYAN}=== Sort Tasks ==={Colors.RESET}")
    print()
    print("1. Sort by Title")
    print("2. Sort by Priority")
    print("3. Sort by Due Date")
    print()

    # Get user selection
    while True:
        choice = input(f"{Colors.BOLD}{Colors.ORANGE}Enter your choice (1-3): {Colors.RESET}").strip()

        if choice == "1":
            sorted_tasks = sort_by_title(tasks)
            print(f"{Colors.BOLD}{Colors.CYAN}=== Tasks Sorted by Title ==={Colors.RESET}")
            print()
            display_tasks(sorted_tasks)
            break
        elif choice == "2":
            sorted_tasks = sort_by_priority(tasks)
            print(f"{Colors.BOLD}{Colors.CYAN}=== Tasks Sorted by Priority ==={Colors.RESET}")
            print()
            display_tasks(sorted_tasks)
            break
        elif choice == "3":
            sorted_tasks = sort_by_due_date(tasks)
            print(f"{Colors.BOLD}{Colors.CYAN}=== Tasks Sorted by Due Date ==={Colors.RESET}")
            print()
            display_tasks(sorted_tasks)
            break
        else:
            print(f"{Colors.BOLD}{Colors.RED}Invalid choice. Please enter 1, 2, or 3.{Colors.RESET}")


if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Sorter ==={Colors.RESET}")

    # Create sample tasks for testing
    from add import _tasks

    if is_empty_list(_tasks):
        print(f"{Colors.YELLOW}No tasks to sort. Add some tasks first.{Colors.RESET}")
    else:
        run_sort_ui(_tasks)

    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

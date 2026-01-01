from add import _tasks, Task


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


def get_all_tasks() -> list[Task]:
    """
    Retrieve all tasks from in-memory storage.

    Returns:
        list[Task]: List of all tasks currently stored. Returns empty list if no tasks exist.
    """
    return _tasks

def run_view_tasks_ui() -> None:
    """
    Display all tasks in a user-friendly console format.

    Shows task ID, title, description, completion status, priority, category,
    and due date with visual indicators for completed vs incomplete tasks
    and color-coded priorities.

    Returns:
        None
    """
    tasks = get_all_tasks()

    if not tasks:
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
        due_date_str = f" | Due: {Colors.PURPLE}{task.due_date}{Colors.RESET}" if task.due_date else ""

        # Print task with all attributes
        print(f"{status} {Colors.BOLD}{Colors.CYAN}[{task.id}]{Colors.RESET} {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET}")
        print(f"    Desc: {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
        print(f"    Priority: {priority_color}{task.priority}{Colors.RESET} | Category: {Colors.PINK}{task.category}{Colors.RESET}{due_date_str}")
        print()

    print(f"{Colors.BOLD}{Colors.CYAN}Total: {Colors.RESET}{len(tasks)}{Colors.BOLD}{Colors.CYAN} tasks{Colors.RESET}")

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Viewer ==={Colors.RESET}")
    run_view_tasks_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

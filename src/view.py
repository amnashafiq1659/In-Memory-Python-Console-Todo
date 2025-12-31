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

    Shows task ID, title, description, and completion status
    with visual indicators for completed vs incomplete tasks.

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
        status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"
        print(f"{Colors.BOLD}{Colors.CYAN}{task.id}{Colors.RESET} | {status} | {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET} | {Colors.DIM_CYAN}{task.description}{Colors.RESET}")

    print()
    print(f"{Colors.BOLD}{Colors.CYAN}Total: {Colors.RESET}{len(tasks)}{Colors.BOLD}{Colors.CYAN} tasks{Colors.RESET}")

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Viewer ==={Colors.RESET}")
    run_view_tasks_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

from dataclasses import dataclass

# In-memory storage
_tasks: list["Task"] = []
_next_id: int = 1

@dataclass(frozen=True)
class Task:
    id: int
    title: str
    description: str
    completed: bool


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


def add_task(title: str, description: str) -> Task:
    """
    Create a new task with given title and description.

    Args:
        title: The title/name of task. Must not be empty.
        description: Optional description of task. Can be empty string.

    Returns:
        Task: The newly created task object.

    Raises:
        ValueError: If title is empty or whitespace-only.
    """
    global _next_id, _tasks

    if not title or title.isspace():
        raise ValueError("Title cannot be empty")

    task = Task(id=_next_id, title=title, description=description, completed=False)
    _tasks.append(task)
    _next_id += 1

    return task

def run_add_task_ui() -> None:
    """
    Interactive console interface for adding tasks.

    Prompts user for title and description, validates input,
    and calls add_task() to create task.

    Displays success or error messages to user.

    Returns:
        None
    """
    while True:
        print()  # Blank line for readability

        # Get title
        while True:
            title = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task title: {Colors.RESET}").strip()
            if title:
                break
            print(f"{Colors.BOLD}{Colors.RED}Error: Title cannot be empty{Colors.RESET}")

        # Get description
        description = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task description (optional, press Enter to skip): {Colors.RESET}").strip()

        # Add task
        task = add_task(title, description)
        print(f"{Colors.BOLD}{Colors.GREEN}Task added with ID: {Colors.BOLD}{Colors.CYAN}{task.id}{Colors.RESET}")

        # Ask if user wants to continue
        choice = input(f"\n{Colors.BOLD}{Colors.ORANGE}Add another task? (y/n): {Colors.RESET}").strip().lower()
        if choice != "y":
            break

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Creator ==={Colors.RESET}")
    run_add_task_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

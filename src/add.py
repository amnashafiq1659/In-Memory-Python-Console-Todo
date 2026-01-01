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
    priority: str = "Medium"  # High / Medium / Low
    category: str = "General"  # user-defined label
    due_date: str | None = None  # optional value (string-based)


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


def map_priority_to_number(priority_input: str) -> int:
    """
    Map priority input to numeric value.

    Args:
        priority_input: Priority string (case-insensitive) or number

    Returns:
        int: 1 (High), 2 (Medium), or 3 (Low)
    """
    if not priority_input or not priority_input.strip():
        return 2

    priority_lower = priority_input.strip().lower()

    if priority_lower in ('1', 'high'):
        return 1
    elif priority_lower in ('2', 'medium', 'med'):
        return 2
    elif priority_lower in ('3', 'low'):
        return 3
    else:
        # Default to Medium for invalid input
        return 2


def number_to_priority_string(priority_num: int) -> str:
    """
    Convert numeric priority to string representation.

    Args:
        priority_num: Priority number (1, 2, or 3)

    Returns:
        str: "High", "Medium", or "Low"
    """
    if priority_num == 1:
        return "High"
    elif priority_num == 2:
        return "Medium"
    elif priority_num == 3:
        return "Low"
    else:
        return "Medium"  # Default to Medium for invalid input


def add_task(title: str, description: str, priority: str = "Medium",
              category: str = "General", due_date: str | None = None) -> Task:
    """
    Create a new task with given title, description, and optional attributes.

    Args:
        title: The title/name of task. Must not be empty.
        description: Optional description of task. Can be empty string.
        priority: Task priority (High/Medium/Low). Defaults to Medium.
        category: User-defined label for task. Defaults to General.
        due_date: Optional due date as string. Defaults to None.

    Returns:
        Task: The newly created task object.

    Raises:
        ValueError: If title is empty or whitespace-only.
    """
    global _next_id, _tasks

    if not title or title.isspace():
        raise ValueError("Title cannot be empty")

    task = Task(
        id=_next_id,
        title=title,
        description=description,
        completed=False,
        priority=priority,
        category=category,
        due_date=due_date
    )
    _tasks.append(task)
    _next_id += 1

    return task

def run_add_task_ui() -> None:
    """
    Interactive console interface for adding tasks.

    Prompts user for title, description, priority, category, and optional due date,
    validates input, and calls add_task() to create task.

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

        # Get priority
        while True:
            priority_input = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task priority (1=High, 2=Medium, 3=Low, press Enter for Medium): {Colors.RESET}").strip()

            if not priority_input:
                priority_num = 2
                priority = "Medium"
                break

            # Map to number first
            priority_num = map_priority_to_number(priority_input)
            priority = number_to_priority_string(priority_num)
            break

        # Get category
        category = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task category (press Enter for General): {Colors.RESET}").strip()
        if not category:
            category = "General"

        # Get due date (optional)
        due_date_input = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task due date (optional, press Enter to skip): {Colors.RESET}").strip()
        due_date = due_date_input if due_date_input else None

        # Add task
        task = add_task(title, description, priority, category, due_date)
        print(f"{Colors.BOLD}{Colors.GREEN}Task added with ID: {Colors.BOLD}{Colors.CYAN}{task.id}{Colors.RESET}")

        # Ask if user wants to continue
        choice = input(f"\n{Colors.BOLD}{Colors.ORANGE}Add another task? (y/n): {Colors.RESET}").strip().lower()
        if choice != "y":
            break

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Creator ==={Colors.RESET}")
    run_add_task_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

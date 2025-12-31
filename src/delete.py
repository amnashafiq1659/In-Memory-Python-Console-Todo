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


def find_task_by_id(task_id: int) -> Task | None:
    """
    Search for a task in memory by its ID.

    Args:
        task_id: The unique ID of task to find.

    Returns:
        Task | None: The Task object if found, None otherwise.
    """
    for task in _tasks:
        if task.id == task_id:
            return task
    return None


def validate_task_id(task_id: int) -> int:
    """
    Validate that a task ID exists and return it.

    Args:
        task_id: The task ID to validate.

    Returns:
        int: The validated task ID.

    Raises:
        ValueError: If task_id does not exist in _tasks.
    """
    task = find_task_by_id(task_id)
    if task is None:
        raise ValueError(f"Task with ID {task_id} not found")
    return task_id


def delete_task(task_id: int) -> None:
    """
    Delete a task from memory by its ID.

    Args:
        task_id: The unique ID of the task to delete.

    Raises:
        ValueError: If task_id does not exist in _tasks.
        ValueError: If task_id is not a positive integer.
    """
    # Validate task exists
    task = find_task_by_id(task_id)
    if task is None:
        raise ValueError(f"Task with ID {task_id} not found")

    # Find and remove task from _tasks list
    for i, t in enumerate(_tasks):
        if t.id == task_id:
            del _tasks[i]
            break


def prompt_for_task_id() -> int:
    """
    Prompt user to enter a task ID.

    Returns:
        int: The task ID entered by user.

    Raises:
        ValueError: If input cannot be parsed as integer.
    """
    user_input = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task ID: {Colors.RESET}").strip()
    try:
        task_id = int(user_input)
        if task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Invalid task ID format. Please enter a number.")
        raise e


def display_task_details(task: Task) -> None:
    """
    Display details of a task to the user.

    Args:
        task: The Task object to display.

    Returns:
        None
    """
    status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"
    print(f"\n{Colors.BOLD}{Colors.CYAN}Current task:{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.CYAN}ID:{Colors.RESET} {Colors.BOLD}{Colors.CYAN}{task.id}{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.CYAN}Title:{Colors.RESET} {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.CYAN}Description:{Colors.RESET} {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.CYAN}Status:{Colors.RESET} {status}")


def prompt_for_confirmation() -> bool:
    """
    Prompt user for confirmation to proceed with deletion.

    Returns:
        bool: True if user confirms with 'y', False otherwise.
    """
    choice = input(f"{Colors.BOLD}{Colors.ORANGE}Delete this task? (y/n): {Colors.RESET}").strip().lower()
    return choice == "y"


def run_delete_task_ui() -> None:
    """
    Interactive console interface for deleting tasks.

    Prompts user for task ID, displays task details,
    requests confirmation, and deletes task if confirmed.

    Displays success or error messages to the user.

    Returns:
        None
    """
    while True:
        print()  # Blank line for readability

        # Display available tasks for reference
        if _tasks:
            print(f"{Colors.BOLD}{Colors.CYAN}Available tasks:{Colors.RESET}")
            for task in _tasks:
                status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"
                print(f"  {Colors.BOLD}{Colors.CYAN}{task.id}{Colors.RESET} | {status} | {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET} | {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
            print()
        else:
            print(f"{Colors.YELLOW}No tasks available. Add tasks using add task functionality.{Colors.RESET}")
            return

        # Get task ID
        try:
            task_id = prompt_for_task_id()
        except ValueError as e:
            print(f"{Colors.BOLD}{Colors.RED}Error: {Colors.RESET}{e}")
            continue

        # Find task
        task = find_task_by_id(task_id)
        if task is None:
            print(f"{Colors.BOLD}{Colors.RED}Error: Task with ID {task_id} not found{Colors.RESET}")
            continue

        # Display current task details
        display_task_details(task)

        # Confirm deletion
        if prompt_for_confirmation():
            try:
                delete_task(task_id)
                print(f"\n{Colors.BOLD}{Colors.GREEN}Task deleted successfully!{Colors.RESET}")
            except ValueError as e:
                print(f"{Colors.BOLD}{Colors.RED}Error: {Colors.RESET}{e}")
        else:
            print(f"\n{Colors.YELLOW}Deletion cancelled.{Colors.RESET}")

        # Ask if user wants to continue
        choice = input(f"\n{Colors.BOLD}{Colors.ORANGE}Delete another task? (y/n): {Colors.RESET}").strip().lower()
        if choice != "y":
            break


if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Deleter ==={Colors.RESET}")
    run_delete_task_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

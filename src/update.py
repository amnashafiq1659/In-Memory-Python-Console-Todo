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
        task_id: The unique ID of the task to find.

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


def update_task(task_id: int, new_title: str | None = None, new_description: str | None = None) -> Task:
    """
    Update a task's title and/or description by its ID.

    Args:
        task_id: The unique ID of the task to update.
        new_title: New title for the task. None or empty string to keep existing.
        new_description: New description for the task. None or empty string to keep existing.

    Returns:
        Task: The updated Task object with new values.

    Raises:
        ValueError: If task_id does not exist.
        ValueError: If new_title is provided but empty/whitespace-only.
    """
    # Validate task exists
    task = find_task_by_id(task_id)
    if task is None:
        raise ValueError(f"Task with ID {task_id} not found")

    # Validate title if provided
    if new_title is not None and new_title.strip():
        if not new_title.strip():
            raise ValueError("Title cannot be empty or whitespace-only")

    # Determine final values (keep existing if not provided or empty)
    final_title = new_title.strip() if (new_title and new_title.strip()) else task.title
    final_description = new_description if new_description is not None else task.description

    # Create new Task instance (frozen dataclass requires new instance)
    updated_task = Task(
        id=task.id,
        title=final_title,
        description=final_description,
        completed=task.completed  # Preserve completion status
    )

    # Find and replace in _tasks list
    for i, t in enumerate(_tasks):
        if t.id == task_id:
            _tasks[i] = updated_task
            break

    return updated_task


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


def prompt_for_title() -> str | None:
    """
    Prompt user for a new task title.

    Returns:
        str | None: The new title, or None to keep existing title.
    """
    title = input(f"{Colors.BOLD}{Colors.ORANGE}Enter new title (press Enter to keep current): {Colors.RESET}").strip()
    return title if title else None


def prompt_for_description() -> str | None:
    """
    Prompt user for a new task description.

    Returns:
        str | None: The new description, or None to keep existing description.
    """
    description = input(f"{Colors.BOLD}{Colors.ORANGE}Enter new description (press Enter to keep current): {Colors.RESET}")
    return description if description is not None else None


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


def run_update_task_ui() -> None:
    """
    Interactive console interface for updating tasks.

    Prompts user for task ID and new values, validates input,
    and calls update_task() to modify task.

    Displays success or error messages to user.

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

        # Get new values
        new_title = prompt_for_title()
        new_description = prompt_for_description()

        # Check if user wants to make any changes
        if not new_title and new_description is None:
            print(f"{Colors.YELLOW}No changes provided. Task remains unchanged.{Colors.RESET}")
        else:
            try:
                # Update task
                updated_task = update_task(task_id, new_title, new_description)

                # Display success
                print(f"\n{Colors.BOLD}{Colors.GREEN}Task updated successfully!{Colors.RESET}")
                display_task_details(updated_task)
            except ValueError as e:
                print(f"{Colors.BOLD}{Colors.RED}Error: {Colors.RESET}{e}")

        # Ask if user wants to continue
        choice = input(f"\n{Colors.BOLD}{Colors.ORANGE}Update another task? (y/n): {Colors.RESET}").strip().lower()
        if choice != "y":
            break


if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== Task Updater ==={Colors.RESET}")
    run_update_task_ui()
    print(f"\n{Colors.BOLD}{Colors.CYAN}Goodbye!{Colors.RESET}")

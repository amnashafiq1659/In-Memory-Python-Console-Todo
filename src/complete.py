"""
Mark Task Complete / Incomplete Feature

This module provides functionality to mark tasks as complete or incomplete
by their unique ID, updating the completion status in memory.
"""

from add import Task, _tasks


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


def validate_task_id(task_id: int) -> None:
    """
    Validate that a task ID is a positive integer and exists in the task list.

    Args:
        task_id: The task ID to validate.

    Raises:
        ValueError: If task_id is not a positive integer or task doesn't exist.
    """
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Task ID must be a positive integer")

    for task in _tasks:
        if task.id == task_id:
            return

    raise ValueError("Task not found")


def mark_complete(task_id: int) -> Task:
    """
    Mark a task as complete by creating a new Task instance with completed=True.

    Args:
        task_id: The ID of the task to mark as complete.

    Returns:
        Task: The updated task object with completed=True.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    validate_task_id(task_id)

    for i, task in enumerate(_tasks):
        if task.id == task_id:
            if task.completed:
                raise ValueError(f"Task {task_id} is already complete")

            new_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=True
            )
            _tasks[i] = new_task
            return new_task

    raise ValueError("Task not found")


def mark_incomplete(task_id: int) -> Task:
    """
    Mark a task as incomplete by creating a new Task instance with completed=False.

    Args:
        task_id: The ID of the task to mark as incomplete.

    Returns:
        Task: The updated task object with completed=False.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    validate_task_id(task_id)

    for i, task in enumerate(_tasks):
        if task.id == task_id:
            if not task.completed:
                raise ValueError(f"Task {task_id} is already incomplete")

            new_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=False
            )
            _tasks[i] = new_task
            return new_task

    raise ValueError("Task not found")


def run_complete_task_ui() -> None:
    """
    Interactive console interface for marking tasks complete/incomplete.

    Allows user to:
    - Choose between marking complete or incomplete
    - Enter task ID
    - See confirmation or error messages
    - Continue marking multiple tasks

    Returns:
        None
    """
    print()
    print(f"{Colors.BOLD}{Colors.CYAN}=== Mark Task Complete / Incomplete ==={Colors.RESET}")

    while True:
        print()  # Blank line for readability

        # Check if tasks exist
        if not _tasks:
            print(f"{Colors.YELLOW}No tasks to update. Add tasks first.{Colors.RESET}")
            break

        # Display available tasks for reference
        print(f"{Colors.BOLD}{Colors.CYAN}Available tasks:{Colors.RESET}")
        for task in _tasks:
            status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"
            print(f"  {Colors.BOLD}{Colors.CYAN}{task.id}{Colors.RESET} | {status} | {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET} | {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
        print()

        # Get action selection
        while True:
            action = input(f"{Colors.BOLD}{Colors.MAGENTA}Do you want to mark a task as (c)omplete or (i)ncomplete? {Colors.RESET}").strip().lower()
            if action in ('c', 'i'):
                break
            if not action:
                print(f"{Colors.BOLD}{Colors.RED}Error: Please enter 'c' or 'i'{Colors.RESET}")
            else:
                print(f"{Colors.BOLD}{Colors.RED}Error: Please enter 'c' for complete or 'i' for incomplete{Colors.RESET}")

        # Get task ID
        while True:
            id_input = input(f"{Colors.BOLD}{Colors.ORANGE}Enter task ID: {Colors.RESET}").strip()

            if not id_input:
                print(f"{Colors.BOLD}{Colors.RED}Error: Task ID cannot be empty{Colors.RESET}")
                continue

            try:
                task_id = int(id_input)
                break
            except ValueError:
                print(f"{Colors.BOLD}{Colors.RED}Error: Invalid ID format. Please enter a positive integer.{Colors.RESET}")

        # Perform the action
        try:
            if action == 'c':
                task = mark_complete(task_id)
                print(f"{Colors.BOLD}{Colors.GREEN}Task {task_id} marked as complete{Colors.RESET}")
            else:  # action == 'i'
                task = mark_incomplete(task_id)
                print(f"{Colors.BOLD}{Colors.GREEN}Task {task_id} marked as incomplete{Colors.RESET}")
        except ValueError as e:
            print(f"{Colors.BOLD}{Colors.RED}Error: {str(e)}{Colors.RESET}")

        # Ask if user wants to continue
        choice = input(f"\n{Colors.BOLD}{Colors.MAGENTA}Mark another task? (y/n): {Colors.RESET}").strip().lower()
        if choice != "y":
            break


if __name__ == "__main__":
    run_complete_task_ui()

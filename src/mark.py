from add import _tasks, Task


def validate_task_id(task_id: int) -> None:
    """
    Validate that a task ID is valid and exists.

    Args:
        task_id: The task ID to validate.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    if not isinstance(task_id, int) or task_id <= 0:
        raise ValueError("Invalid ID format")

    # Check if task exists
    for task in _tasks:
        if task.id == task_id:
            return

    raise ValueError("Task not found")


def mark_complete(task_id: int) -> Task:
    """
    Mark a task as complete by its ID.

    Args:
        task_id: The unique ID of task to mark complete.

    Returns:
        Task: The updated task with completed=True.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    global _tasks

    for i, task in enumerate(_tasks):
        if task.id == task_id:
            # Check if already complete
            if task.completed:
                return task

            # Create new task with completed=True
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=True
            )
            # Replace in list
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")


def mark_incomplete(task_id: int) -> Task:
    """
    Mark a task as incomplete by its ID.

    Args:
        task_id: The unique ID of task to mark incomplete.

    Returns:
        Task: The updated task with completed=False.

    Raises:
        ValueError: If task_id is invalid or task not found.
    """
    global _tasks

    for i, task in enumerate(_tasks):
        if task.id == task_id:
            # Check if already incomplete
            if not task.completed:
                return task

            # Create new task with completed=False
            updated_task = Task(
                id=task.id,
                title=task.title,
                description=task.description,
                completed=False
            )
            # Replace in list
            _tasks[i] = updated_task
            return updated_task

    raise ValueError("Task not found")


def run_complete_task_ui() -> None:
    """
    Interactive console interface to mark tasks complete or incomplete.

    Returns:
        None
    """
    if not _tasks:
        print("No tasks to update. Add tasks first.")
        return

    print("=== Mark Task Complete / Incomplete ===")
    print()

    while True:
        # Get action
        action = input("Do you want to mark a task as (c)omplete or (i)ncomplete? ").strip().lower()
        if action not in ('c', 'i'):
            print("Invalid choice. Please enter 'c' or 'i'.")
            continue

        # Get task ID
        task_id_str = input("Enter task ID: ").strip()

        # Validate and convert ID
        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Invalid ID format")
            continue

        # Perform operation
        try:
            if action == 'c':
                updated_task = mark_complete(task_id)
                status_word = "complete"
                # Check if status actually changed
                if not updated_task.completed:
                    print(f"Task {task_id} is already complete")
                else:
                    print(f"Task {task_id} marked as {status_word}")
            else:
                updated_task = mark_incomplete(task_id)
                status_word = "incomplete"
                # Check if status actually changed
                if updated_task.completed:
                    print(f"Task {task_id} is already incomplete")
                else:
                    print(f"Task {task_id} marked as {status_word}")

        except ValueError as e:
            print(f"Error: {e}")

        print()  # Blank line for readability

        # Ask if continue
        choice = input("Mark another task? (y/n): ").strip().lower()
        if choice != 'y':
            break


if __name__ == "__main__":
    print("=== Task Completion Manager ===")
    run_complete_task_ui()
    print("\nGoodbye!")

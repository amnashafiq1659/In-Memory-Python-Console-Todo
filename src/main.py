"""
Main entry point for Todo Console Application.

Provides a unified menu-driven interface for all Todo operations:
- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks complete/incomplete

All operations share the same in-memory task storage from add module.
"""

from add import _tasks, Task, run_add_task_ui
from view import run_view_tasks_ui
from update import run_update_task_ui
from delete import run_delete_task_ui
from complete import mark_complete, mark_incomplete, run_complete_task_ui


class Colors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'  # Purple
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ORANGE = '\033[38;5;208m'  # Orange
    BRIGHT_YELLOW = '\033[93;1m'  # Bright Yellow for task titles
    LIGHT_MAGENTA = '\033[95;1m'  # Light Magenta for task titles
    DIM_CYAN = '\033[96;2m'  # Dim Cyan for descriptions
    LIGHT_PURPLE = '\033[38;5;147m'  # Light Purple for descriptions


def print_header(text: str) -> None:
    """Print a colored header (Cyan + Bold)."""
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text:^60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.RESET}")


def print_subheader(text: str) -> None:
    """Print a colored subheader (Blue + Bold)."""
    print()
    print(f"{Colors.BOLD}{Colors.BLUE}-- {text} --{Colors.RESET}")
    print()


def print_success(message: str) -> None:
    """Print a success message in bold green."""
    print(f"{Colors.BOLD}{Colors.GREEN}{message}{Colors.RESET}")


def print_error(message: str) -> None:
    """Print an error message in bold red."""
    print(f"{Colors.BOLD}{Colors.RED}{message}{Colors.RESET}")


def print_warning(message: str) -> None:
    """Print a warning message in yellow."""
    print(f"{Colors.YELLOW}{message}{Colors.RESET}")


def print_info(message: str) -> None:
    """Print an info message in yellow."""
    print(f"{Colors.YELLOW}{message}{Colors.RESET}")


def print_highlight(message: str) -> None:
    """Print highlighted text in pink."""
    print(f"{Colors.MAGENTA}{message}{Colors.RESET}")


def print_menu() -> None:
    """Display the main menu options."""
    print()
    print(f"{Colors.BOLD}{Colors.BLUE}MAIN MENU{Colors.RESET}")
    print()
    print(f"{Colors.GREEN}{Colors.BOLD}1.{Colors.RESET} {Colors.MAGENTA}Add Task{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}2.{Colors.RESET} {Colors.MAGENTA}View Tasks{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}3.{Colors.RESET} {Colors.MAGENTA}Update Task{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}4.{Colors.RESET} {Colors.MAGENTA}Delete Task{Colors.RESET}")
    print(f"{Colors.GREEN}{Colors.BOLD}5.{Colors.RESET} {Colors.MAGENTA}Mark Task Complete/Incomplete{Colors.RESET}")
    print(f"{Colors.RED}{Colors.BOLD}0.{Colors.RESET} {Colors.RED}Exit{Colors.RESET}")
    print()

def get_menu_choice() -> str:
    """
    Get and validate user's menu choice.

    Returns:
        str: The validated menu choice ('0', '1', '2', '3', '4', '5').

    Raises:
        ValueError: If input is invalid.
    """
    choice = input(f"{Colors.BOLD}{Colors.ORANGE}Enter choice (0-5): {Colors.RESET}").strip()
    valid_choices = {'0', '1', '2', '3', '4', '5'}

    if choice not in valid_choices:
        raise ValueError("Invalid choice. Please enter a number between 0 and 5.")

    return choice


def handle_add_task() -> None:
    """Handle the add task menu option."""
    print()
    print_header("ADD TASK")
    run_add_task_ui()
    print()
    print_success("Returned to main menu")


def handle_view_tasks() -> None:
    """Handle the view tasks menu option."""
    print()
    print_header("VIEW TASKS")
    print_subheader("All Tasks")
    run_view_tasks_ui()
    print()
    print_info("Press Enter to return to menu...")
    input()


def handle_update_task() -> None:
    """Handle the update task menu option."""
    print()
    print_header("UPDATE TASK")
    run_update_task_ui()
    print()
    print_success("Returned to main menu")


def handle_delete_task() -> None:
    """Handle the delete task menu option."""
    print()
    print_header("DELETE TASK")
    run_delete_task_ui()
    print()
    print_success("Returned to main menu")


def handle_mark_task() -> None:
    """Handle the mark task complete/incomplete menu option."""
    print()
    print_header("MARK TASK")
    print_subheader("Mark Complete / Incomplete")
    run_complete_task_ui()
    print()
    print_success("Returned to main menu")


def handle_exit() -> None:
    """Handle the exit menu option."""
    print()
    total_tasks = len(_tasks)
    completed_tasks = sum(1 for t in _tasks if t.completed)
    incomplete_tasks = total_tasks - completed_tasks

    print_header("GOODBYE!")
    print()
    print(f"{Colors.BOLD}{Colors.CYAN}Summary:{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.CYAN}Total tasks:{Colors.RESET} {total_tasks}")
    print(f"  {Colors.BOLD}{Colors.GREEN}Completed:{Colors.RESET} {completed_tasks}")
    print(f"  {Colors.BOLD}{Colors.YELLOW}Incomplete:{Colors.RESET} {incomplete_tasks}")
    print()
    print_success("Thank you for using Todo Console Application!")


def show_quick_tasks() -> None:
    """Show a quick summary of recent tasks (up to 5)."""
    if _tasks:
        print()
        print(f"{Colors.YELLOW}Recent tasks (last 5):{Colors.RESET}")
        print()
        recent_tasks = _tasks[-5:] if len(_tasks) > 5 else _tasks
        for task in recent_tasks:
            status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"
            print(f"  {status} {Colors.BOLD}{Colors.CYAN}{task.id}:{Colors.RESET} {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET}")
        print()
    else:
        print()
        print_warning("No tasks available. Add tasks first!")
        print()


def show_detailed_tasks() -> None:
    """Show all tasks with full colored output."""
    if _tasks:
        print()
        print_subheader("All Tasks")
        for task in _tasks:
            status = f"{Colors.BOLD}{Colors.GREEN}[X]{Colors.RESET}" if task.completed else f"{Colors.BOLD}{Colors.YELLOW}[ ]{Colors.RESET}"
            print(f"  {status} {Colors.BOLD}{Colors.CYAN}{task.id}:{Colors.RESET}")
            print(f"     {Colors.BOLD}{Colors.CYAN}Title:{Colors.RESET} {Colors.BRIGHT_YELLOW}{task.title}{Colors.RESET}")
            print(f"     {Colors.BOLD}{Colors.CYAN}Description:{Colors.RESET} {Colors.DIM_CYAN}{task.description}{Colors.RESET}")
            print()
    else:
        print()
        print_warning("No tasks available. Add tasks first!")
        print()


def run_main_menu() -> None:
    """
    Run the main menu loop.

    Continuously displays menu and handles user choices
    until user selects exit option.
    """
    while True:
        show_quick_tasks()
        print_menu()

        try:
            choice = get_menu_choice()
        except ValueError as e:
            print_error(str(e))
            print()
            continue

        if choice == '1':
            handle_add_task()
        elif choice == '2':
            handle_view_tasks()
        elif choice == '3':
            handle_update_task()
        elif choice == '4':
            handle_delete_task()
        elif choice == '5':
            handle_mark_task()
        elif choice == '0':
            handle_exit()
            break


if __name__ == "__main__":
    # Clear screen (works on most terminals)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Run main menu
    print_header("TodoCLI - In-Memory Python Console Application")
    run_main_menu()

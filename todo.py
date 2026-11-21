import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    """Load tasks from the JSON file, or return an empty list."""
    if not TASKS_FILE.exists():
        return []
    try:
        return json.loads(TASKS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print("tasks.json is damaged, starting with an empty list.")
        return []


def save_tasks(tasks: list[dict]) -> None:
    """Write all tasks to the JSON file."""
    TASKS_FILE.write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def add_task(tasks: list[dict], title: str) -> None:
    """Add a new task with the next free id."""
    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "done": False})


def list_tasks(tasks: list[dict]) -> None:
    """Print all tasks, marking finished ones with x."""
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"{task['id']}. [{mark}] {task['title']}")


def main() -> None:
    tasks = load_tasks()
    while True:
        print()
        print("Todo list")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Quit")
        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            title = input("Task title: ").strip()
            if title:
                add_task(tasks, title)
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Title cannot be empty.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
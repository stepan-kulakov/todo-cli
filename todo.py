import json
from pathlib import Path
from typing import Optional

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


def find_task(tasks: list[dict], task_id: int) -> Optional[dict]:
    """Return the task with the given id, or None if it does not exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def complete_task(tasks: list[dict], task_id: int) -> bool:
    """Mark a task as done. Return False if the id does not exist."""
    task = find_task(tasks, task_id)
    if task is None:
        return False
    task["done"] = True
    return True


def delete_task(tasks: list[dict], task_id: int) -> bool:
    """Remove a task. Return False if the id does not exist."""
    task = find_task(tasks, task_id)
    if task is None:
        return False
    tasks.remove(task)
    return True


def read_task_id(prompt: str) -> Optional[int]:
    """Ask for a task id. Return None if the input is not a number."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print("Task id must be a number.")
        return None


def main() -> None:
    tasks = load_tasks()
    while True:
        print()
        print("Todo list")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Choose 1-5: ").strip()

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
            task_id = read_task_id("Task id to mark as done: ")
            if task_id is not None:
                if complete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("Task marked as done.")
                else:
                    print("No task with that id.")
        elif choice == "4":
            task_id = read_task_id("Task id to delete: ")
            if task_id is not None:
                if delete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("Task deleted.")
                else:
                    print("No task with that id.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
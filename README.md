# Todo CLI

A small command-line todo list written in Python. Tasks are saved to a JSON file, so they are still there the next time you run the program.

## Features

- Add tasks
- Show all tasks, finished ones are marked with `x`
- Mark a task as done
- Delete a task
- Tasks are saved between runs
- Input validation: empty titles, unknown ids and non-numeric input do not crash the program

## Requirements

Python 3.9 or newer. No external packages are needed.

## How to run

```
python todo.py
```

## Example session

```
Todo list
1. Show tasks
2. Add task
3. Mark task as done
4. Delete task
5. Quit
Choose 1-5: 2
Task title: Write README
Task added.

Choose 1-5: 3
Task id to mark as done: 1
Task marked as done.

Choose 1-5: 1
1. [x] Learn Python
2. [ ] Write README
```

## Project structure

| File | Purpose |
|---|---|
| `todo.py` | The whole program: storage, task functions and the menu |
| `tasks.json` | Created automatically on first save, ignored by Git |
| `.gitignore` | Keeps `tasks.json` and `__pycache__/` out of the repository |

## How it works

Each task is a dictionary with an `id`, a `title` and a `done` flag. The list of tasks is read from `tasks.json` at start and written back after every change.
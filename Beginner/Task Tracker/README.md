# Task Tracker CLI

A simple command line interface (CLI) to track and manage your tasks.

## Features

- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List tasks by status (todo, in-progress, done)
- Tasks are stored in a JSON file (`tasks.json`) in the current directory.

## Requirements

- Python 3.x

## Usage

Run the script using python:

```bash
python task_cli.py <command> [arguments]
```

### Commands

1.  **Add a new task**

    ```bash
    python task_cli.py add "Buy groceries"
    ```

2.  **Update a task**

    ```bash
    python task_cli.py update <id> "New description"
    ```

    Example:

    ```bash
    python task_cli.py update 1 "Buy groceries and cook dinner"
    ```

3.  **Delete a task**

    ```bash
    python task_cli.py delete <id>
    ```

    Example:

    ```bash
    python task_cli.py delete 1
    ```

4.  **Mark a task as in progress**

    ```bash
    python task_cli.py mark-in-progress <id>
    ```

    Example:

    ```bash
    python task_cli.py mark-in-progress 1
    ```

5.  **Mark a task as done**

    ```bash
    python task_cli.py mark-done <id>
    ```

    Example:

    ```bash
    python task_cli.py mark-done 1
    ```

6.  **List all tasks**

    ```bash
    python task_cli.py list
    ```

7.  **List tasks by status**
    ```bash
    python task_cli.py list todo
    python task_cli.py list in-progress
    python task_cli.py list done
    ```

## Task Properties

Each task has the following properties:

- `id`: Unique identifier
- `description`: Task description
- `status`: Task status (todo, in-progress, done)
- `createdAt`: Creation timestamp
- `updatedAt`: Last update timestamp
